---
name: "github-handling"
description: "Use this skill when you need to interact with GitHub repositories - searching, reading files, creating branches, pushing code, managing issues and pull requests."
version: "1.0.0"
author: "Agent Zero"
tags: ["github", "git", "repository", "version-control", "pull-request"]
trigger_patterns:
  - "github"
  - "repository"
  - "pull request"
  - "create branch"
  - "push code"
  - "github search"
  - "github issue"
---

# GitHub Handling Skill

This skill provides comprehensive guidance on interacting with GitHub repositories using the GitHub MCP (Model Context Protocol).

## Overview

The GitHub MCP enables autonomous agents to perform various GitHub operations including searching repositories, reading/writing files, managing branches, creating issues and pull requests, and more.

## Prerequisites

- A GitHub Personal Access Token with appropriate scopes
- Token must be configured in the Agent Zero environment
- Required scopes: `repo` for private repos, `read:user`, `read:org`

## Critical Workflow Rules

**NEVER push directly to main or master branch.** Always follow this workflow:

1. **Create a feature branch** from the target branch
2. **Commit and push** your changes to the feature branch
3. **Create a Pull Request** from feature branch to main

### Correct Workflow

```python
# Step 1: Create feature branch
github.create_branch(
    owner="username",
    repo="repository-name",
    branch="feature/your-feature",
    from_branch="main"
)

# Step 2: Push changes to feature branch
github.push_files(
    owner="username",
    repo="repository-name",
    branch="feature/your-feature",
    message="Add new feature",
    files=[{"path": "file.txt", "content": "..."}]
)

# Step 3: Create Pull Request
github.create_pull_request(
    owner="username",
    repo="repository-name",
    title="Feature description",
    body="PR description...",
    head="feature/your-feature",
    base="main"
)
```

## Available Tools

### Repository Operations
- `search_repositories` - Search public repositories
- `get_file_contents` - Read files from repo
- `create_or_update_file` - Create or update single file
- `push_files` - Push multiple files in one commit
- `create_repository` - Create new repository
- `fork_repository` - Fork a repository

### Branch & Commit Operations
- `create_branch` - Create new branch
- `list_commits` - List commits on branch

### Issue Operations
- `list_issues` - List repository issues
- `create_issue` - Create new issue
- `get_issue` - Get issue details
- `update_issue` - Update existing issue
- `add_issue_comment` - Add comment to issue

### Pull Request Operations
- `list_pull_requests` - List PRs
- `create_pull_request` - Create new PR
- `get_pull_request` - Get PR details
- `get_pull_request_files` - Get files changed in PR
- `get_pull_request_comments` - Get PR comments
- `get_pull_request_reviews` - Get PR reviews
- `create_pull_request_review` - Create PR review
- `merge_pull_request` - Merge a PR
- `update_pull_request_branch` - Update PR with latest base

### Search Operations
- `search_code` - Search code across repos
- `search_issues` - Search issues and PRs
- `search_users` - Search GitHub users

## Common Use Cases

### Reading Repository Contents

```python
github.get_file_contents(
    owner="username",
    repo="repository-name",
    path="path/to/file.ext"
)
```

### Updating a File

```python
# First get the file SHA for existing files
github.create_or_update_file(
    owner="username",
    repo="repository-name",
    path="path/to/file.ext",
    content="file content here",
    message="Update file",
    branch="feature/my-branch",
    sha="file_sha_if_updating"
)
```

### Creating an Issue

```python
github.create_issue(
    owner="username",
    repo="repository-name",
    title="Issue title",
    body="Issue description...",
    labels=["bug", "enhancement"]
)
```

## Best Practices

1. **Always use feature branches** - Never commit directly to main
2. **Write descriptive PR titles** - Clear titles help reviewers
3. **Include detailed PR descriptions** - Explain what, why, and how
4. **Check permissions first** - Verify token has required scopes
5. **Use base64 encoding** - For binary or special content files
6. **Handle rate limits** - GitHub API has rate limits; implement backoff
7. **Validate before pushing** - Review changes before committing

## Troubleshooting

### Permission Denied Errors
- Check token has required scopes
- For private repos, ensure token has `repo` scope
- Verify token hasn't expired

### Not Found Errors
- Confirm owner/repo name is correct
- Check if repository exists and is accessible
- Verify branch name exists

### Validation Failed Errors
- For PRs, ensure head and base branches are different
- Check that head branch exists before creating PR