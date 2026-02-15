---
name: "agent-deployer"
description: "Deploy Agent Zero instances to remote servers via Docker. Supports automated configuration using A0_SET_ environment variables and remote access via tunnels."
version: "1.1.0"
author: "Agent Zero"
tags: ["deployment", "docker", "remote", "automation", "tunnel"]
trigger_patterns:
  - "deploy agent zero"
  - "setup remote agent"
  - "install agent zero on server"
  - "setup agent zero tunnel"
---

# Agent Deployer Skill

This skill automates the deployment and configuration of Agent Zero instances on remote servers.

## Features
- **Docker Deployment**: Pulls and runs the official `agent0ai/agent-zero` image.
- **Automated Configuration**: Uses `A0_SET_` environment variables for zero-touch setup.
- **Persistence**: Configures volume mapping for `/a0/usr` to persist user data.
- **Remote Access**: Supports setting up Microsoft Dev Tunnels for secure remote access (if requested).

## Prerequisites
- SSH access to the target server.
- Docker installed (the script can install it for you).
- For Hetzner Cloud, use the `hetzner-cloud` skill to provision the server first.

## Usage

### Deploying a New Instance
```bash
python /a0/usr/skills/agent-deployer/scripts/deploy_a0.py --ip <SERVER_IP> --env "A0_SET_chat_model_name=gemini-3-flash-preview,GOOGLE_API_KEY=YOUR_KEY"
```

### Setting up a Tunnel
To enable remote access via tunnel, include the tunnel setup in your request. The script can be extended to run `python /a0/python/helpers/run_tunnel.py` inside the container.

## Configuration Variables
- `A0_SET_chat_model_provider`: e.g., `google`, `openai`
- `A0_SET_chat_model_name`: e.g., `gemini-3-flash-preview`
- `A0_SET_agent_profile`: e.g., `agent0`, `hacker`
