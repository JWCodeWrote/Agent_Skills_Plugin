---
name: story-commentary-workflow
description: A specialized Agent Skill for organizing game story footage, planning story commentary videos, splitting chapters, transcribing subtitles, drafting narration, and matching narration to visuals. Use when the user mentions story commentary, game plot recaps, story condensation, chapter breakdowns, narration scripts, voiceover-to-visual mapping, or no-timeline editing workflows.
---

# Story Commentary Workflow

This skill turns a generic video-editing request into a dedicated story commentary workflow.

It is not centered on timelines, multi-track effects, or flashy editing. Its primary operating model is:

- story chapters
- subtitles and transcription
- narration scripts
- key visual mapping
- story condensation

## When to Use This Skill

Use this skill when the user needs any of the following:

- organize a game story
- turn long footage into a story recap
- write a story commentary script
- map voiceover to visuals
- design a story-focused no-timeline editing flow
- plan a story commentary editing tool
- structure plot chapters, event beats, or character-thread breakdowns

## Goal

Convert raw material into structured outputs that can directly support story commentary production, instead of leaving the user with an unstructured pile of clips.

Expected outputs usually include:

- chapter cards
- plot summaries
- key event lists
- narration sections
- narration-to-visual mappings
- condensation rules
- output-version strategy

## Core Principles

1. Understand the story before cutting the footage.
2. Preserve dialogue, cutscenes, and reveals first.
3. Compress travel, repetitive combat, grinding, and empty downtime first.
4. Default to chapter cards and transcript-driven editing instead of falling back to a traditional timeline.
5. Narration should improve understanding, not just describe what is already visible.
6. Full-story output and condensed-story output should be treated as separate products.

## Standard Workflow

For detailed steps and mode differences, see [references/workflow-playbook.md](references/workflow-playbook.md).

### 1. Confirm Source Material and Goal

Clarify the following first:

- source type: gameplay footage, stream clips, voiceover audio, subtitle files, images
- target format: full story, condensed story, story commentary
- target length: short, medium, full-length
- audience: newcomers, returning players, or viewers who only want the ending

If information is missing, prioritize:

- total video length
- whether subtitles already exist
- whether narration is needed
- whether spoiler warnings are required

### 2. Transcribe and Create Initial Segments

Convert the material into editable text first.

Preferred source order:

1. existing subtitle files
2. speech-to-text transcription
3. OCR from in-game subtitles
4. manual correction

Segmentation rules:

- each segment should contain one clear event or one complete unit of meaning
- prioritize dialogue-based segmentation
- treat cutscenes as standalone segments when appropriate
- split long battles by event beats, not by preserving the entire fight

### 3. Build Chapter Cards

Organize segments into chapters rather than stacking raw clips.

Default chapter framework:

- opening hook
- background setup
- conflict introduction
- plot progression
- turning-point reveal
- climax confrontation
- ending resolution
- post-credit hook or foreshadowing

For quest-heavy RPGs, AVGs, JRPGs, or visual novels, you can also add:

- character introduction
- faction conflict
- side-story support
- truth reveal

Each chapter card should include at least:

- chapter title
- linked source segments
- key lines
- narrative function
- whether it must be kept

For field definitions and chapter-type templates, see [references/chapter-schema.md](references/chapter-schema.md).

## Narrative Function Tags

Whenever possible, label each segment or chapter with its narrative role:

- `setup`: establishes background
- `conflict`: introduces tension
- `progress`: moves the plot forward
- `reveal`: discloses new information
- `twist`: reframes prior understanding
- `payoff`: resolves prior setup
- `ending`: closes the story

These tags exist to support condensation and structure, not just UI decoration.

## Three Output Modes

### Full Story Mode

Best for viewers who want the story with minimal loss.

Retention rules:

- keep most dialogue and cutscenes
- trim only repetitive battle content
- use narration to clarify, not replace the source

### Condensed Story Mode

Best for viewers who want to understand the plot quickly.

Retention rules:

- keep only core events and essential lines
- keep battle entry, mechanic showcase, and outcome
- heavily reduce travel, grinding, and menu time

### Story Commentary Mode

Best for narration-led videos.

Retention rules:

- narration becomes the structural backbone
- visuals serve as proof, pacing, and emphasis
- multiple clips may support a single narration block

## Narration Workflow

### 1. Write in Blocks, Not as One Monolith

Each narration block should correspond to a chapter function or event beat.

Recommended block format:

```text
[Chapter Name]
What does this section need to explain?
What does the viewer need to understand here?
Which visuals or lines should support it?
```

### 2. Every Narration Block Should Answer Three Questions

- What happened?
- Why does it matter?
- How does it affect what comes next?

### 3. Writing Patterns to Avoid

- pure visual description without explanation
- overloading a section with too much lore
- revealing information too early
- long, dense sentences with no natural pause points

## Visual Mapping Rules

Every narration block should be paired with one set of supporting visuals.

Acceptable visual sources:

- original dialogue scenes
- key cutscenes
- character close-ups
- map or UI evidence shots
- battle outcome shots
- supporting images or title cards

Priority order:

1. visuals that directly prove the narration
2. visuals from the exact turning point being discussed
3. expressive character shots
4. supplementary footage that does not weaken comprehension

## Condensation Rules

The following are default compression candidates:

- repetitive combat
- long travel sequences
- menu navigation
- loading downtime
- low-information exploration
- repeated NPC dialogue

The following should usually be preserved first:

- main-story dialogue
- cutscenes
- reveals
- character alignment shifts
- key quest outcomes
- endings and foreshadowing

## Output Requirements

When using this skill, prefer structured outputs over vague advice.

For complete templates and examples, see [references/output-templates.md](references/output-templates.md).

Preferred output forms:

### Story Chapter Table

```text
Chapter Name:
Narrative Function:
Key Events:
Recommended Visuals:
Compression Candidates:
```

### Narration Draft

```text
Section Title:
Narration:
Visual Pairing:
Pacing Notes:
```

### Editing Decision Summary

```text
Keep:
Condense:
Remove:
Reason:
```

## Response Style

When responding with this skill:

- prioritize actionable workflow steps
- prioritize chapter and section structure
- avoid generic editing advice
- if the task is product design, answer from the perspective of a dedicated story commentary tool
- if the task is feature planning, first ask whether the feature improves story comprehension

## Quick Checklist

Before considering the task complete, confirm:

- full story, condensed story, and commentary modes are clearly distinguished
- transcription happens before editing decisions
- clips have been organized into chapter cards
- every narration block is matched to visuals
- low-information content has been compressed
- key lines and turning points are preserved

## What Not to Do

- do not let this collapse into a generic video-editing skill
- do not make timeline-first thinking the primary workflow
- do not focus on effects, transitions, or filters as the main answer
- do not ignore story beats or the order of information reveal

## References

- Workflow guide: [references/workflow-playbook.md](references/workflow-playbook.md)
- Chapter templates: [references/chapter-schema.md](references/chapter-schema.md)
- Output templates: [references/output-templates.md](references/output-templates.md)
