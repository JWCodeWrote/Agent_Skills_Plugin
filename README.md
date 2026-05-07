# Agent Skills Plugin

_Read this in [简体中文](./README_CN.md)._

Welcome to the **Agent Skills Plugin** repository. This project is a curated collection of specialized "Cognitive Modules" (Skills) designed to upgrade AI Agents with distinct personas, philosophical frameworks, and execution capabilities.

Instead of simple Python tools, these skills provide **Mental Operating Systems** that force the Agent to assume specific roles—from a dialectical philosopher to a high-speed executor.

### 🧩 Featured Skills

| Skill Name                       | Description                                                                                                                                   | Key Persona                   |
| :------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------- |
| **`Dialectical_Materialism`**    | **Cognitive OS**: Forces objective, non-linear analysis using Marxist dialectics (Unity of Opposites, Quantity-Quality Leap).                 | _The Dialectical Philosopher_ |
| **`Meihua_Yishu`** (梅花易数)    | **Hybrid Divination**: A strategic decision support system combining traditional I-Ching math with Gemini AI for deep, modern interpretation. | _Metaphysical Strategist_     |
| **`AI-search-browser-use-main`** | **Research Mode**: Advanced web research capabilities using Chrome CDP and browser automation for deep synthesis.                             | _The Deep Researcher_         |
| **`HighTriad`**                | **Architecture Mode**: Plans systems for high concurrency, high performance, and high availability with SLOs, scaling, resilience, and validation. | _The Systems Architect_     |
| **`story-commentary-workflow`** | **Story Commentary Mode**: Organizes game story footage, chapter breakdowns, subtitles, narration drafts, and voiceover-to-visual mapping. | _The Story Commentary Producer_ |
| **`story-worldbuilding-planner`** | **Worldbuilding Mode**: Creates and refines game stories, web novel plots, light novel arcs, characters, factions, power systems, and lore bibles. | _The Narrative Designer_ |
| **`European-Chinese-Cleaner`** | **Chinese Rewrite Mode**: Rewrites translationese, Europeanized grammar, AI-generated stiffness, and English calques into natural Chinese. | _The Chinese Language Editor_ |
| **`PUA`**                      | **AI Compliance Pressure Mode**: Applies strict, no-excuse pressure to the AI agent for immediate self-correction; explicitly forbids user-targeted PUA. | _The Agent Discipline Enforcer_ |
| **`agent-fault-retrospective`** | **Agent Fault Retrospective**: When the user flags an AI agent mistake, overstep, or misunderstanding, asks for user-defined trigger keywords, applies a Superpowers-style root-cause review, and records concise behavior rules in the correct instruction file (`AGENTS.md`, `CLAUDE.md`, Cursor rules, Copilot instructions, etc.). | _The Fault Retrospective Officer_ |
| **`Impeccable-design-ui`**                   | **Design Workflow Hub**: An Impeccable design menu that routes to 14 specialized sub-skills (critique, colorize, animate, polish, etc.) with auto-install via `npx skills add pbakaus/impeccable`. | _The Design Director_ |
| **`awesome-design-setup`**     | **Brand Design Picker**: Browse 58 curated brand DESIGN.md files (Linear, Stripe, Apple, Tesla, etc.) and download the chosen one to your project root for AI-agent-driven UI development.        | _The Brand Stylist_   |
| **`frontend-imagegen-director`** | **Front-end Image-to-Implementation Director**: Inspects the project's existing style and product nature, uses `superpowers` for requirement discovery, generates front-end visuals with `gpt-image2` or the environment's `imagegen` path, and then builds the actual page from the approved image. If `superpowers` is unavailable, it falls back explicitly instead of pretending it was used. | _The Front-end Visual Director_ |

### 🚀 How to Use

1. **Installation**: Copy the desired skill folder (e.g., `HighTriad`) into your Agent's `skills/` directory.
2. **Activation**: Add the `SKILL.md` content of the chosen skill to your Agent's **System Prompt** or **Context**.
3. **Usage**: The agent adopts the persona and utilizes the linked tools/references automatically.

### 📂 Repository Structure

```text
.
├── Dialectical_Materialism/ # [Skill] Philosophical Reasoning
│ ├── SKILL.md
│ └── references/ # The Three Laws of Dialectics
├── Meihua_Yishu/ # [Skill] Hybrid AI Divination
│ ├── SKILL.md
│ ├── scripts/ # Calculation & Gemini Integration
│ └── references/ # Hexagrams & Strategy Database
├── AI-search-browser-use-main/ # [Skill] AI-assisted browser research
│ ├── SKILL.md
│ ├── ai_query.py
│ ├── scripts/ # Browser planning and page cleanup helpers
│ └── references/ # AI search target notes
├── HighTriad/ # [Skill] Three-High Architecture (Concurrency/Performance/Availability)
│ ├── SKILL.md
│ └── references/ # Tech/Industry/Templates
├── story-commentary-workflow/ # [Skill] Story commentary planning
│ ├── SKILL.md
│ └── references/ # Chapter schema, templates, and playbook
├── story-worldbuilding-planner/ # [Skill] Story and worldbuilding planner
│ └── SKILL.md
├── European-Chinese-Cleaner/ # [Skill] Translationese-to-native-Chinese rewrite
│ └── SKILL.md
├── PUA/ # [Skill] AI-Agent Under-Pressure Compliance Mode
│ └── SKILL.md
├── agent-fault-retrospective/ # [Skill] Agent fault retrospective and instruction-file guardrails
│ └── SKILL.md
├── Impeccable-design-ui/ # [Skill] Impeccable Design Workflow Hub
│ └── SKILL.md
├── awesome-design-setup/ # [Skill] Brand Design Picker (58 brands)
│ ├── SKILL.md
│ ├── references/ # Brand catalog with path keys
│ └── scripts/ # fetch_design.sh download helper
├── frontend-imagegen-director/ # [Skill] Generate front-end visuals from project style and build the page from the approved image
│ └── SKILL.md
└── README.md # Project Overview
```

## 🛡️ License

MIT License. Free to use for both personal and commercial Agent development.

---

_Powered by Antigravity-Team & K-Dense Inc._
