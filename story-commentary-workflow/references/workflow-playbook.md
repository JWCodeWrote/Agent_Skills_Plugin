# Workflow Playbook

This document expands the practical execution flow for `story-commentary-workflow`.

## When to Use It

Once the request is clearly about:

- organizing game story material
- condensing plot footage
- producing story commentary
- matching narration to visuals

the workflow should stay story-first instead of reverting to generic video editing.

## Standard Execution Order

1. confirm source material
2. confirm output goal
3. transcribe or obtain subtitles
4. split into event segments
5. organize into chapter cards
6. choose an output mode
7. draft narration
8. pair visuals
9. make condensation decisions
10. produce structured output

## Step 1: Confirm Source Material

List:

- video sources
- audio sources
- existing subtitles
- narration availability
- spoiler constraints

If material is incomplete, identify the gap before continuing.

## Step 2: Confirm Output Goal

Classify the request as one of:

- `full story mode`
- `condensed story mode`
- `story commentary mode`

Do not mix all three into one decision model.

## Step 3: Transcribe or Obtain Subtitles

Preferred order:

1. existing subtitle files
2. speech-to-text
3. OCR from in-game subtitles
4. manual correction

If transcription is weak, mark:

- missing words
- incorrect character names
- incorrect place names
- unresolved proper nouns

## Step 4: Split into Event Segments

Segments should not be based on fixed durations.

Prefer:

- one complete line of dialogue
- one reveal
- one quest turn
- one character alignment shift
- one full cutscene beat

Avoid fixed-second chunking by default.

## Step 5: Organize into Chapter Cards

Every chapter card should answer:

- what this part does in the story
- why the viewer needs it
- what is lost if it is removed

If a section cannot answer those questions, it is usually a compression candidate.

## Step 6: Choose Output Mode

### Full Story Mode

- source material remains primary
- narration only fills comprehension gaps

### Condensed Story Mode

- information density comes first
- keep outcomes and plot movement, not every process step

### Story Commentary Mode

- narration is the structural backbone
- visuals support and validate the explanation

## Step 7: Draft Narration

Each block should answer:

- what happened
- why it matters
- what it changes next

Do not reduce narration to literal play-by-play description.

## Step 8: Pair Visuals

Prioritize:

1. key dialogue
2. key cutscenes
3. emotional close-ups
4. shots that prove the narration

Only fall back to supplementary footage when direct evidence is unavailable.

## Step 9: Make Condensation Decisions

Default compression targets:

- travel
- repeated combat
- menu idle time
- low-information exploration

Default retention priorities:

- main-story lines
- key cutscenes
- truth reveals
- ending payoffs

## Step 10: Produce Structured Output

At minimum, output one of:

- story chapter table
- narration draft
- editing decision summary

If the request is more product-design oriented, output:

- feature flow
- user flow
- chapter-card data structure

## Common Failure Modes

- discussing effects before understanding the story
- treating transcripts as final narration
- naming chapters by events only, without narrative purpose
- cutting the dialogue that actually carries the plot
- using timeline language where chapter language is more appropriate
