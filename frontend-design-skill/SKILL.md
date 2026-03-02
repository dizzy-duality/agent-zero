---
name: "frontend-design"
description: "Guide for creating distinctive, production-grade frontend interfaces that avoid generic AI slop aesthetics. Implement real working code with exceptional attention to aesthetic details and creative choices."
version: "1.0.0"
author: "anthropics/claude-code"
tags: ["frontend", "design", "ui", "ux", "aesthetics"]
trigger_patterns:
  - "frontend"
  - "design"
  - "user interface"
  - "web design"
  - "create page"
  - "build interface"
---

# frontend-design

**Author**: anthropics/claude-code
**Version**: 1.0.0
**Description**: Guide for creating distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics. Implement real working code with exceptional attention to aesthetic details and creative choices.

## Overview

This skill provides comprehensive guidelines for building frontend interfaces that are memorable, distinctive, and production-ready. It emphasizes bold aesthetic choices, unique typography, cohesive color themes, purposeful motion, and unexpected spatial compositions.

## Use Cases

- Building custom components, pages, or full applications
- Creating distinctive user interfaces with memorable aesthetics
- Avoiding generic "AI slop" design patterns
- Implementing production-grade frontend code (HTML/CSS/JS, React, Vue, etc.)

---

## Design Thinking Framework

Before writing any code, understand the context and commit to a **BOLD aesthetic direction**:

### 1. Purpose
- What problem does this interface solve?
- Who is the target audience?
- What are the user goals and workflows?

### 2. Tone
Pick an extreme aesthetic direction:
- **Brutally minimal** - Clean, stripped-back, essential only
- **Maximalist chaos** - Bold, layered, vibrant, overwhelming
- **Retro-futuristic** - Vintage meets future, synthwave, neon
- **Organic/natural** - Earthy, flowing, botanical, soft
- **Luxury/refined** - Elegant, premium, understated sophistication
- **Playful/toy-like** - Cheerful, whimsical, cartoonish
- **Editorial/magazine** - Sophisticated, typography-driven, print-inspired
- **Brutalist/raw** - Unpolished, bold, structural, industrial
- **Art deco/geometric** - Ornate, symmetrical, golden ratio
- **Soft/pastel** - Gentle, dreamy, muted colors
- **Industrial/utilitarian** - Functional, raw materials, functional

### 3. Constraints
- Technical requirements (framework, performance, accessibility)
- Browser compatibility
- Performance budgets
- Responsive design needs

### 4. Differentiation
- What makes this **UNFORGETTABLE**?
- What's the one thing someone will remember?

> **CRITICAL**: Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work - the key is intentionality, not intensity.

---

## Frontend Aesthetics Guidelines

### 1. Typography

**Do:**
- Choose fonts that are beautiful, unique, and interesting
- Pair a distinctive display font with a refined body font
- Use unexpected, characterful font choices that elevate the design

**Avoid:**
- Generic fonts like Arial, Inter, Roboto
- System fonts as primary choices
- Overused "AI" font families (Space Grotesk, etc.)

### 2. Color & Theme

**Do:**
- Commit to a cohesive aesthetic
- Use CSS variables for consistency
- Use dominant colors with sharp accents
- Create memorable color combinations

**Avoid:**
- Timid, evenly-distributed palettes
- Cliched purple gradients on white backgrounds
- Predictable color schemes

### 3. Motion

**Do:**
- Use animations for effects and micro-interactions
- Prioritize CSS-only solutions for HTML
- Use Motion library for React when available
- Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions
- Use scroll-triggering and hover states that surprise

**Best Practices:**
- Staggered reveals on page load
- Smooth hover transitions
- Scroll-triggered animations
- Subtle micro-interactions on buttons/inputs

### 4. Spatial Composition

**Do:**
- Create unexpected layouts
- Use asymmetry
- Allow elements to overlap
- Create diagonal flow
- Break the grid
- Use generous negative space OR controlled density

### 5. Backgrounds & Visual Details

**Do:**
- Create atmosphere and depth
- Add contextual effects and textures
- Apply creative forms:
  - Gradient meshes
  - Noise textures
  - Geometric patterns
  - Layered transparencies
  - Dramatic shadows
  - Decorative borders
  - Custom cursors
  - Grain overlays

---

## Anti-Patterns to Avoid

### Never Use:
1. Overused font families (Inter, Roboto, Arial, system fonts)
2. Cliched color schemes (purple gradients on white backgrounds)
3. Predictable layouts and component patterns
4. Cookie-cutter design lacking context-specific character
5. Generic "AI-generated" aesthetics
6. Common choices like Space Grotesk that have become cliché

### Remember:
- No design should be the same
- Vary between light and dark themes
- Different fonts, different aesthetics
- **NEVER converge on common choices**

---

## Implementation Guidelines

### Match Complexity to Vision
- **Maximalist designs**: Need elaborate code with extensive animations and effects
- **Minimalist/refined designs**: Need restraint, precision, and careful attention to spacing, typography, and subtle details
- Elegance comes from executing the vision well

### Code Quality Standards
- Production-grade and functional
- Visually striking and memorable
- Cohesive with a clear aesthetic point-of-view
- Meticulously refined in every detail

### Tech Stack Recommendations
- HTML/CSS/JS for vanilla implementations
- React with Motion library for animations
- Vue with VueUse/Motion
- CSS custom properties for theming
- Modern CSS (Grid, Flexbox, subgrid)

---

## Installation

```bash
npx skills add https://github.com/anthropics/claude-code --skill frontend-design
```

---

## Related Skills

- UI/UX Design Principles
- CSS Architecture
- React Component Design
- Animation & Motion Design
- Accessibility (a11y)

---

*This skill is part of the anthropics/claude-code collection.*