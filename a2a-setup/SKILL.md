---
name: "a2a-setup"
description: "Enable and configure Agent-to-Agent (A2A) communication on remote Agent Zero instances. Use this skill when you need to set up or fix A2A connectivity on a remote server."
version: "1.0.0"
author: "Agent Zero"
tags: ["a2a", "setup", "remote", "configuration"]
trigger_patterns:
  - "setup a2a"
  - "enable a2a"
  - "configure a2a"
  - "a2a setup"
---

# A2A Setup Skill

This skill automates the process of enabling and configuring the Agent-to-Agent (A2A) server on a remote Agent Zero instance running in Docker.

## Features
- Updates `settings.json` to enable A2A and set a security token.
- Restarts the A2A server process inside the container.
- Verifies connectivity and provides the final A2A endpoint URL.

## Usage

To use this skill, you need the IP address of the remote server and an optional security token.

### Command
Execute the setup script using the `code_execution_tool`:

```bash
python /a0/usr/skills/a2a-setup/scripts/setup_a2a.py <REMOTE_IP> --token <YOUR_TOKEN>
```

### Parameters
- `ip`: The public IP address of the remote server.
- `--token`: (Optional) The security token for A2A authentication. Defaults to `a2a-secret-token`.

## Example

**User**: "Set up A2A on 46.225.141.106 with token my-secure-token"

**Agent Action**:
1. Load the `a2a-setup` skill.
2. Run the script: `python /a0/usr/skills/a2a-setup/scripts/setup_a2a.py 46.225.141.106 --token my-secure-token`.
3. Provide the user with the endpoint: `http://46.225.141.106/a2a/t-my-secure-token`.

## Troubleshooting
- Ensure SSH access to the remote server is configured.
- Verify that the Docker container is named `agent-zero`.
- Check if port 80 or 8000 is open on the remote firewall.
