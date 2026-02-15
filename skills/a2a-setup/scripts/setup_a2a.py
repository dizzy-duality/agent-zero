import argparse
import json
import subprocess
import sys

def run_ssh_command(ip, command):
    ssh_cmd = ["ssh", "-o", "StrictHostKeyChecking=no", f"root@{ip}", command]
    result = subprocess.run(ssh_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error executing command on {ip}: {result.stderr}")
        return None
    return result.stdout

def setup_a2a(ip, token):
    print(f"Configuring A2A on {ip} with token {token}...")

    # Update settings.json inside the container
    update_json_cmd = f'''
docker exec agent-zero python3 -c "
import json, os
path = "/a0/usr/config/settings.json"
if os.path.exists(path):
    with open(path, "r") as f: data = json.load(f)
else:
    data = {{}}
data["a2a_enabled"] = True
data["a2a_server_enabled"] = True
data["mcp_server_token"] = "{token}"
with open(path, "w") as f: json.dump(data, f, indent=4)
"
'''
    run_ssh_command(ip, update_json_cmd)

    # Restart A2A server
    restart_cmd = f'''
docker exec agent-zero bash -c "pkill -9 -f uvicorn || true"
docker exec -d agent-zero bash -c "cd /a0 && PYTHONPATH=/a0 /opt/venv-a0/bin/uvicorn python.helpers.fasta2a_server:get_proxy --host 0.0.0.0 --port 8000 --factory"
'''
    run_ssh_command(ip, restart_cmd)

    print("A2A setup complete. Verifying...")
    verify_cmd = "docker exec agent-zero netstat -tulpn | grep :8000"
    output = run_ssh_command(ip, verify_cmd)
    if output and ":8000" in output:
        print(f"Success! A2A server is running on {ip}:8000")
        print(f"Endpoint: http://{ip}/a2a/t-{token}")
    else:
        print("Verification failed. Check logs on the remote server.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Setup A2A on a remote Agent Zero instance")
    parser.add_argument("ip", help="Remote server IP")
    parser.add_argument("--token", default="a2a-secret-token", help="A2A security token")
    args = parser.parse_args()
    setup_a2a(args.ip, args.token)
