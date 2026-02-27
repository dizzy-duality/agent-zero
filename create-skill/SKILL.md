---
name: "create-skill"
description: "This skill should be used when the user asks to create a new skill, add a skill, make a skill, build a custom skill, or needs guidance on creating well-structured SKILL.md files following the agentskills.io standard."
version: "1.0.0"
author: "Agent Zero"
tags: ["skills", "agent", "custom", "creation"]
trigger_patterns:
  - "create skill"
  - "add skill"
  - "make skill"
  - "build custom skill"
  - "new skill"
---

# Create Skill

This skill helps you create new custom skills following the agentskills.io standard.

## SKILL.md Structure

A valid skill requires:

```yaml
---
name: "skill-name"
description: "What the skill does"
version: "1.0.0"
author: "Your Name"
tags: ["tag1", "tag2"]
trigger_patterns:
  - "phrases that trigger this skill"
---

# Skill Name

Detailed description...

## Features

- Feature 1
- Feature 2

## Usage

```
# Example usage
```

## Prerequisites

- Requirement 1
- Requirement 2
```

## Creating a Skill

1. Create a folder in skills/
2. Add SKILL.md with proper YAML frontmatter
3. Add scripts/ folder if needed
4. Test the skill
