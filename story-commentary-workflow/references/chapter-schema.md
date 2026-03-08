# Chapter Schema

This document defines the chapter-card fields and templates used by the skill.

## Core Fields

Each chapter card should include at least:

- `title`: chapter name
- `function`: narrative role
- `summary`: one-line summary
- `key_events`: major events
- `key_lines`: critical lines
- `visual_targets`: visuals worth preserving
- `trim_candidates`: sections that can be cut or condensed
- `must_keep`: whether the chapter is essential

## Narrative Function Enum

- `setup`
- `conflict`
- `progress`
- `reveal`
- `twist`
- `payoff`
- `ending`

## Generic Chapter Template

```yaml
title: Background Setup
function: setup
summary: Establishes the protagonist's current situation and the story's starting point.
key_events:
  - The protagonist receives the first clear mission.
  - The world's rules are introduced.
key_lines:
  - "This is not a mission you can refuse."
visual_targets:
  - Mission trigger cutscene
  - Dialogue between the protagonist and key NPC
trim_candidates:
  - Meaningless walking before the quest starts
must_keep: true
```

## Common Chapter Types for Game Stories

### Opening Hook

- function: establish tension, mystery, or urgency
- typical material: defeat scenes, pre-reveal footage, unstable character moments

### Background Setup

- function: introduce character, world, and goal
- typical material: early mission scenes, tutorial dialogue, faction setup

### Conflict Introduction

- function: show the main problem or opposition
- typical material: enemy entrance, failed mission, emerging conspiracy

### Plot Progression

- function: move the story from one major state to another
- typical material: mission completion, ally recruitment, intel acquisition

### Turning-Point Reveal

- function: force the viewer to reinterpret prior events
- typical material: truth reveal, betrayal, identity reversal

### Climax Confrontation

- function: resolve or peak the main conflict
- typical material: boss fight, final confrontation, decisive choice

### Ending Resolution

- function: land the outcome and emotional aftermath
- typical material: ending cutscene, character epilogues, world-state change

### Post-Credit Hook or Foreshadowing

- function: extend meaning toward a sequel or hidden layer
- typical material: hidden dialogue, post-credit scene, unresolved mystery

## Condensation Heuristics

A chapter is often a compression candidate if it has all of the following:

- few key events
- no irreplaceable lines
- highly repetitive visuals
- little new information

A chapter should usually be preserved if any of the following is true:

- it contains the first reveal of a key rule or fact
- it changes a character's position or allegiance
- it locks in a main quest outcome
- it pays off ending information
