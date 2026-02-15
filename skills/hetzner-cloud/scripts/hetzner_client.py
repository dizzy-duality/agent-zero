import os
import requests
import json
import sys

class HetznerCloudClient:
    BASE_URL = "https://api.hetzner.cloud/v1"

    def __init__(self, token=None):
        self.token = token or os.getenv("HETZNER_CLOUD_TOKEN")
        if not self.token:
            print("Error: HETZNER_CLOUD_TOKEN not found in environment.")
            sys.exit(1)
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def request(self, method, endpoint, data=None, params=None):
        url = f"{self.BASE_URL}/{endpoint.lstrip('/')}"
        response = requests.request(method, url, headers=self.headers, json=data, params=params)
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            return {"error": str(e), "details": response.text}

    def list_servers(self):
        return self.request("GET", "servers")

    def get_server(self, server_id):
        return self.request("GET", f"servers/{server_id}")

    def create_server(self, name, server_type, image, location=None, ssh_keys=None):
        data = {
            "name": name,
            "server_type": server_type,
            "image": image
        }
        if location: data["location"] = location
        if ssh_keys: data["ssh_keys"] = ssh_keys
        return self.request("POST", "servers", data=data)

    def delete_server(self, server_id):
        return self.request("DELETE", f"servers/{server_id}")

if __name__ == "__main__":
    # Simple CLI interface for the script
    import argparse
    parser = argparse.ArgumentParser(description='Hetzner Cloud API Client')
    parser.add_argument('action', choices=['list-servers', 'get-server', 'delete-server'])
    parser.add_argument('--id', help='Server ID')

    args = parser.parse_args()
    client = HetznerCloudClient()

    if args.action == 'list-servers':
        print(json.dumps(client.list_servers(), indent=2))
    elif args.action == 'get-server' and args.id:
        print(json.dumps(client.get_server(args.id), indent=2))
    elif args.action == 'delete-server' and args.id:
        print(json.dumps(client.delete_server(args.id), indent=2))
