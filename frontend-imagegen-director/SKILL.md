---
name: frontend-imagegen-director
description: Use when the user wants AI-generated front-end concept images, UI mockups, landing-page visuals, or bitmap design references that should match the current project's product nature, existing UI language, and brand constraints.
---

# Frontend Imagegen Director

Generate front-end reference images that fit the current project instead of producing generic AI mockups.

## Required Output

Produce one of these before you generate anything:

- page-level concept comp
- component reference sheet
- moodboard or style frame
- multi-variant UI exploration

State which output you are making.

## Dependency Rules

- Treat built-in `imagegen` as the preferred image generation path.
- If the environment exposes `imagegen`, use it first.
- If the user explicitly asks for CLI or model-path control, follow the environment's `imagegen` workflow or equivalent `gpt-image2` / `gpt-image-2` path.
- If no image generation capability exists, do not pretend you can generate images.
- In that fallback case, downgrade to a requirement summary, project style analysis, prompt pack, and iteration notes.

`superpowers`, `clarify`, `frontend-design`, or similar skills are optional accelerators, not hard dependencies.

- If they exist, use them.
- If they do not exist, perform their jobs manually inside this skill.
- Never claim you used an optional skill unless it was actually available and invoked.

## Workflow

### 1. Confirm Intent in Superpowers Style

If `superpowers` or a requirement-discovery skill exists, use it first.

If not, ask only the minimum questions needed:

- What screen, flow, or page should the image represent?
- Who is the target user and what kind of product is this?
- Should the result stay close to the current project, or explore new directions?
- Is this for desktop, mobile, or both?
- Are there any must-keep brand colors, copy language, logos, or avoided styles?

When the user is already specific, do not over-question. Move on to style inspection.

### 2. Inspect Project Style Before Prompting

Check the current repo for project signals such as:

- existing pages and components
- design tokens, theme files, and CSS variables
- screenshots, brand assets, and logos
- `DESIGN.md`, README, landing copy, and product positioning
- industry cues such as finance, devtools, ecommerce, education, or AI

Summarize the result in 3 buckets:

- stable brand traits
- UI patterns to preserve
- room for exploration

Do not skip this step unless the user explicitly wants a fresh direction unrelated to the repo.

### 3. Choose Generation Mode

Pick one mode:

- faithful extension
- polished redesign
- exploratory variants

If the user did not specify a mode, choose the closest fit and say which one you chose.

### 4. Build the Generation Brief

Every image prompt must include:

- product type and audience
- platform and viewport
- visual direction
- layout structure
- color, material, and typography cues
- interaction density
- exact language for UI copy
- avoid list
- how closely it should resemble the current project

If the project is Chinese-first, the default UI copy in the generated image must also be Chinese unless the user asks for another language.

### 5. Generate and Review

Use built-in `imagegen` by default.

After generation, review the result against these checks:

- does it look like this project instead of a generic AI dashboard
- is the UI copy language correct
- is the information hierarchy plausible
- does the layout fit the target device
- does the temperament match the product type

Iterate with targeted prompt changes instead of full restarts when possible.

### 6. Deliver

For each final image, report:

- what it represents
- which style cues came from the project
- what changed from the source direction
- the final prompt used
- whether the result is a generated image or a prompt-only fallback

## Guardrails

- Do not treat optional skills as mandatory.
- Do not claim `superpowers`, `frontend-design`, or `clarify` were used unless they were actually available and invoked.
- Do not default to English UI copy when the user is working in Chinese, unless the user asks for English.
- Do not present generated images as implementation-complete front-end code unless the user explicitly asks for code next.
