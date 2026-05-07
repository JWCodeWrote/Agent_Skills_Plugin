---
name: frontend-imagegen-director
description: Use when the user wants the agent to inspect the current project's style and product nature, clarify requirements in a Superpowers-style workflow, generate front-end visuals with gpt-image2 or the environment's imagegen path, and then build the actual front-end page from the approved image.
---

# Frontend Imagegen Director

This skill is not a prompt-only mockup generator.

Its default workflow is:

1. inspect the current project's style and product nature
2. clarify the user's page requirements in a Superpowers-style flow
3. confirm the extracted requirements before image generation
4. generate a front-end concept image with `gpt-image2` or the environment's image generation path
5. use that image as the visual contract for the actual front-end implementation

If the user explicitly asks for image-only output, you may stop after the image stage.
Otherwise, do not stop at the image.

## Required Outcome

Before finishing, state which of these outcomes you are delivering:

- image plus implemented page
- image-only exploration
- prompt-only fallback

If the user asked to "draw the front end and then build it", the required outcome is `image plus implemented page`.

## Dependency Rules

- Requirement clarification should use `superpowers` when it is actually available.
- If `superpowers` is not available, do the same requirement-discovery discipline manually and explicitly say it is a fallback.
- Prefer `gpt-image2` or `gpt-image-2` when the environment allows model-path selection.
- If the environment only exposes built-in `imagegen`, use that path and describe it accurately instead of pretending direct model control exists.
- If no image generation capability exists, do not pretend you generated anything.
- In that fallback case, stop at a requirement summary, project style analysis, implementation brief, and image prompts for later generation.

This skill's intended stack is:

- `superpowers` for requirement discovery
- `gpt-image2` / `gpt-image-2` or built-in `imagegen` for front-end image generation

Do not introduce extra dependency skills unless the user explicitly asks for them.

## Mandatory Workflow

### 1. Clarify User Intent First

If `superpowers` exists, use it for requirement discovery before drafting prompts or code.

If it does not exist, ask only the minimum needed questions:

- What screen, flow, or page should be built?
- Who is the target user and what kind of product is this?
- Should the result stay close to the current project, or explore a stronger redesign?
- Is this for desktop, mobile, or both?
- Are there any must-keep brand colors, copy language, logos, layout constraints, or avoided styles?

When the user is already specific, do not re-ask what was already answered.
Instead, restate the extracted brief and move on.

### 2. Confirm the Requirement Brief Before Generating

Before generating any image, present the extracted brief back to the user in a compact confirmation block.

That confirmation must cover:

- what page, flow, or screen will be built
- target users and product type
- desktop, mobile, or both
- the intended visual direction
- required brand constraints, copy language, and avoided styles

If the user already gave all of this clearly, do not ask broad new questions.
Still restate the brief and wait for confirmation before generating the image.

Do not generate the front-end image until this confirmation step is complete, unless the user explicitly says to proceed without confirmation.

### 3. Inspect Project Style Before Generating

Check the repo for project signals such as:

- existing pages and components
- design tokens, theme files, and CSS variables
- screenshots, brand assets, and logos
- `DESIGN.md`, README, landing copy, and product positioning
- product-category cues such as finance, devtools, ecommerce, education, gaming, or AI

Summarize the result in 3 buckets:

- stable brand traits
- UI patterns to preserve
- room for exploration

Do not skip this unless the user explicitly wants a fresh direction unrelated to the repo.

### 4. Choose the Visual Direction

Pick one mode:

- faithful extension
- polished redesign
- exploratory variants

If the user did not specify a mode, choose the closest fit and say which one you chose.

### 5. Build the Image Generation Brief

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
- implementation intent that this image will be used to build the real page afterward

If the project is Chinese-first, the default UI copy in the generated image must also be Chinese unless the user asks for another language.

### 6. Generate the Front-End Image

Use `gpt-image2` / `gpt-image-2` when available.

If the environment only exposes built-in `imagegen`, use it as the image generation path.

Generate one of these:

- page-level concept comp
- component reference sheet
- moodboard or style frame
- multi-variant UI exploration

State which one you are generating before you generate it.

Unless image generation capability is unavailable, generating the front-end image is mandatory before front-end implementation.

### 7. Review the Image Before Coding

Review the generated image against these checks:

- does it look like this project instead of a generic AI dashboard
- is the UI copy language correct
- is the information hierarchy plausible
- does the layout fit the target device
- does the temperament match the product type
- is there enough layout and component detail to implement the page faithfully

Iterate with targeted prompt changes instead of full restarts when possible.

If the user asked for image-first confirmation, do not start coding until the image direction is accepted.

### 8. Build the Actual Front-End From the Approved Image

After the image is approved, implement the real front-end page from it.

Implementation should preserve:

- the approved visual hierarchy
- the approved copy language
- the approved layout structure
- the approved component rhythm and density
- the project's existing technical patterns unless the user asked for broader refactoring

The image is a design contract, not a loose inspiration board.
Do not jump straight into code before this stage when the user asked for image-first workflow.

### 9. Validate Implementation Against the Image

Before finishing, compare the built page against the approved image and report:

- what visual elements were matched closely
- what had to change for responsive, technical, or content reasons
- any gaps that still need polish

## Delivery

For each final run, report:

- what the page represents
- which style cues came from the project
- what the `superpowers` or fallback clarification established
- the final image prompt used
- whether the image was generated or prompt-only
- whether front-end code was implemented from that image

## Guardrails

- Do not skip the image stage and jump straight into code when the user asked to generate a front-end visual first.
- Do not generate the front-end image before the extracted requirement brief has been restated and confirmed, unless the user explicitly waived confirmation.
- Do not stop at image delivery when the user asked to build the page from that image.
- Do not default to English UI copy when the user is working in Chinese, unless the user asks for English.
- Do not claim `superpowers` was used unless it was actually available and invoked.
- Do not present a generated image as implementation-complete front-end code.
- Do not present front-end code as compliant with this skill if no image generation step happened first, unless the user explicitly waived that requirement.
