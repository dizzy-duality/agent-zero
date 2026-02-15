---
name: "hetzner-cloud"
description: "Manage Hetzner Cloud resources like servers, volumes, and networks using the Hetzner Cloud API."
version: "1.0.0"
author: "Agent Zero"
tags: ["cloud", "infrastructure", "hetzner", "api"]
trigger_patterns:
  - "hetzner"
  - "cloud server"
  - "hcloud"
---

# Hetzner Cloud Skill

This skill allows you to manage your Hetzner Cloud infrastructure directly through the API.

## Prerequisites

- A Hetzner Cloud API Token. Generate one in the [Hetzner Cloud Console](https://console.hetzner.cloud/).
- Set the token as an environment variable `HETZNER_CLOUD_TOKEN` or provide it via secret placeholder `§§` + `secret(HETZNER_CLOUD_TOKEN)`.

## Helper Script

A Python helper script is available at `scripts/hetzner_client.py`. It provides a `HetznerCloudClient` class for easy API interaction.

### Usage Examples

#### List all servers
```bash
python /a0/usr/skills/hetzner-cloud/scripts/hetzner_client.py list-servers
```

#### Get server details
```bash
python /a0/usr/skills/hetzner-cloud/scripts/hetzner_client.py get-server --id <server_id>
```

#### Delete a server
```bash
python /a0/usr/skills/hetzner-cloud/scripts/hetzner_client.py delete-server --id <server_id>
```

## API Reference

- **Base URL:** `https://api.hetzner.cloud/v1`
- **Authentication:** `Authorization: Bearer <API_TOKEN>`
- **Documentation:** [Hetzner Cloud API Docs](https://docs.hetzner.cloud/)

## Common Tasks

### Creating a Server
You can use the `HetznerCloudClient.create_server` method in a Python script:

```python
from hetzner_client import HetznerCloudClient
client = HetznerCloudClient(token="your_token")
response = client.create_server(
    name="my-server",
    server_type="cx22",
    image="ubuntu-22.04"
)
print(response)
```

### Managing Volumes
Endpoints for volumes are available at `/volumes`. Use the `request` method of the client for custom endpoints:

```python
client.request("GET", "volumes")
```
