---
name: "docker-engine"
description: "Containerization technology for building and containerizing applications. Use when working with Docker containers, images, or Docker CLI commands."
version: "1.0.0"
author: "Agent Zero"
tags: ["docker", "containers", "devops", "deployment"]
trigger_patterns:
  - "docker"
  - "container"
  - "dockerfile"
  - "build image"
---

# Docker Engine Skill

This skill provides Docker containerization capabilities for building and managing applications.

## Features
- Docker CLI command execution
- Container management (start, stop, remove)
- Image building and management
- Docker Compose support
- Volume management

## Usage

Use the code_execution_tool with runtime "terminal" to run Docker commands.

### Common Commands

```bash
# List containers
docker ps -a

# List images
docker images

# Build an image
docker build -t myimage:latest .

# Run a container
docker run -d myimage:latest

# Stop a container
docker stop <container_id>

# Remove a container
docker rm <container_id>
```

## Prerequisites
- Docker installed on the system
- Proper permissions to access Docker daemon
