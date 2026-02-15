import argparse
import subprocess
import sys

def run_ssh_command(ip, command):
    ssh_cmd = ["ssh", "-o", "StrictHostKeyChecking=no", f"root@{ip}", command]
    result = subprocess.run(ssh_cmd, capture_output=True, text=True)
    return result

def deploy(ip, name, env_vars, port=80, volume="/home/a1:/a0/usr", tunnel=False):
    print(f"[*] Deploying Agent Zero to {ip}...")
    
    env_flags = ""
    if env_vars:
        for item in env_vars.split(","):
            env_flags += f" -e {item}"

    remote_script = f"""
    if ! command -v docker &> /dev/null; then
        echo "[*] Installing Docker..."
        curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh
    fi

    docker stop {name} || true
    docker rm {name} || true

    echo "[*] Starting Agent Zero container..."
    docker run -d --name {name} \
      -p {port}:80 \
      -v {volume} \
      {env_flags} \
      agent0ai/agent-zero

    if [ "{tunnel}" = "True" ]; then
        echo "[*] Setting up tunnel..."
        docker exec -d {name} python3 /a0/python/helpers/run_tunnel.py
    fi

    sleep 5
    docker ps -a --filter name={name}
    """

    result = run_ssh_command(ip, remote_script)
    if result.returncode == 0:
        print("[+] Deployment successful!")
        print(result.stdout)
    else:
        print("[-] Deployment failed!")
        print(result.stderr)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deploy Agent Zero to a remote server.")
    parser.add_argument("--ip", required=True, help="Target server IP address")
    parser.add_argument("--name", default="agent-zero", help="Container name")
    parser.add_argument("--env", help="Comma-separated environment variables")
    parser.add_argument("--port", type=int, default=80, help="Host port")
    parser.add_argument("--tunnel", action="store_true", help="Enable remote access tunnel")
    
    args = parser.parse_args()
    deploy(args.ip, args.name, args.env, args.port, tunnel=args.tunnel)
