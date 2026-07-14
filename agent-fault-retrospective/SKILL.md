---
name: agent-fault-retrospective
description: Use when a user identifies an AI agent fault, overreach, misunderstanding, unauthorized action, or asks for a retrospective, durable fault rule, trigger keyword, or future automatic invocation; also use when existing fault records need to be consulted.
---

# Agent Fault Retrospective

This skill turns a user-identified agent mistake into durable operating rules.

The canonical fault history is the skill's `references/fault.md` file. The goal is not to write a long apology. The goal is to extract the user's judgment, identify the failure mechanism, and maintain short, executable guardrails that future agents can consult.

## Use This Skill When

Use this skill when the user says or implies any of the following:

- the agent made a mistake, overstepped, or violated instructions
- the agent should reflect, review, inspect, postmortem, or do a retrospective
- the agent should remember a mistake, record a fault, or update an agent instruction file
- the user wants keywords or trigger phrases added so future similar cases automatically invoke this skill
- the task mentions fault keywords already recorded in `agent-fault-retrospective/references/fault.md`

Trigger examples include: `过失`, `失误`, `错误`, `检讨`, `复盘`, `越权`, `记住这次`, `写进 agents.md`, `写进 claude.md`, `写进 cursor rules`, `自动调用该 skill`, `mistake`, `fault`, `postmortem`, `retrospective`.

## Non-Negotiable Boundaries

- Do not defend, debate, or dilute the user's claim that a fault occurred.
- After the skill triggers, both Codex and Claude must read the skill's `references/fault.md` before analyzing the fault or editing files.
- Treat `agent-fault-retrospective/references/fault.md` as the canonical store for historical fault rules; do not use the global `AGENTS.md` or `CLAUDE.md` as the fault database.
- Do not copy an entire global agent instruction file into `fault.md`.
- Do not write a long retrospective into `fault.md` or an instruction file.
- Do not expand ambiguous user wording into broader tool actions or irreversible operations.

## Required Workflow

### 1. Load the Fault Reference

Resolve `references/fault.md` relative to this skill directory and read it in full before interpreting the current fault. Apply any matching trigger keywords, prohibited actions, and required confirmations from that file.

If the reference file is missing, do not reconstruct it from `AGENTS.md`, `CLAUDE.md`, or another instruction file. Report the missing reference and ask whether it may be created.

### 2. Locate Any Additional Instruction File

Only locate an additional instruction file when the user explicitly asks for a separate reminder or rule outside the fault reference. Use this priority order:

1. A path explicitly named by the user.
2. The active instruction file supplied in the conversation context.
3. A clearly discoverable instruction file for the current agent and repository, only if the user is talking about the current repo.
4. If none is clear, ask which instruction file should be updated before writing.

Known instruction files may include:

- `AGENTS.md` for Codex, Copilot agent instructions, and agents.md-compatible tools
- `CLAUDE.md` for Claude Code
- `GEMINI.md` for Gemini CLI
- `.cursor/rules/*` or legacy `.cursorrules` for Cursor
- `.github/copilot-instructions.md` or `.github/instructions/*.instructions.md` for GitHub Copilot
- `.windsurfrules` for Windsurf-style workspace rules

If the user says "你的 agent.md", "你的 agents.md", "your memory", or "your rules", treat that as an instruction to update the agent's actual durable instruction record, not automatically the current project's root file.

### 3. First-Use Bootstrap

If `references/fault.md` does not already contain a matching fault rule, ask the user for:

1. The exact words or situations that should trigger this skill in the future.
2. The specific mistake category this incident belongs to.
3. Whether the agent may update `references/fault.md` after summarizing the new rule.

Keep the questions short. Ask at most three at once.

After confirmation, add a concise trigger rule like:

```markdown
## 过失复盘 Skill 触发规则

- 当使用者指出 AI/Codex/agent 有「过失、失误、错误、越权、检讨、复盘、记住这次」等情境，必须优先调用 `agent-fault-retrospective`。
- 当任务命中已记录的高风险关键词时，必须先确认语义与操作边界，不得自行扩大解读。
- 复盘后只能将短规则、触发词、禁止事项、必做确认写入 `agent-fault-retrospective/references/fault.md`；全域 `AGENTS.md` 或 `CLAUDE.md` 只保留调用提醒，不存放完整过失记录。
```

### 4. Superpowers-Style Retrospective

Use available Superpowers workflows when the environment provides them, especially systematic debugging or root-cause tracing. If no Superpowers tool is available, follow the same discipline manually:

1. Establish the failure fact.
   - What did the agent do?
   - What did the user expect instead?
   - What instruction, boundary, or preference was violated?

2. Trace the root cause.
   - Did the agent assume location, scope, language, permissions, or user intent?
   - Did the agent skip a required confirmation?
   - Did the agent execute a broader action than requested?

3. Extract trigger keywords.
   - Record exact user wording.
   - Record semantic variants.
   - Avoid overly broad keywords that would cause noisy false triggers.

4. Convert the lesson into an executable rule.
   - Bad rule: "Be more careful."
   - Good rule: "When the user's wording is ambiguous, ask for confirmation before taking a broader or irreversible action."

5. Confirm before writing.
   - Show the proposed short rule.
   - Ask for confirmation unless the user has already explicitly authorized the write.

### 5. Update the Fault Reference

After the user confirms or has already authorized the write, update only `references/fault.md` with durable behavior constraints:

- fault summary
- trigger keywords or high-risk phrases
- prohibited actions
- required confirmation behavior
- language or formatting preference if relevant

Prefer this compact format:

```markdown
## Agent 行为记录

### 过失复盘触发规则

- 使用者指出「过失、失误、错误、检讨、复盘、越权、记住这次」或命中已记录高风险关键词时，必须调用 `agent-fault-retrospective`。
- 调用后必须先询问使用者认定的过失事实与触发关键词，再进行 Superpowers 式根因复盘。
- 复盘结果只能整理成短规则写入本档，不得写入冗长完整检讨。

- ...
```

If a matching section already exists, update it in place. Do not duplicate sections. Keep global agent instruction files limited to their invocation reminder unless the user explicitly requests a separate change.

## Output Expectations

When responding to the user during a retrospective, use this order:

1. `我理解的过失`
2. `需要你确认的关键词`
3. `根因复盘`
4. `准备写入 references/fault.md 的短规则`
5. `请确认`

After the user confirms, perform the edit and report the path of `references/fault.md` that changed.

## Quality Bar

A successful run leaves the agent with a sharper future constraint, not just a record that the agent felt sorry.

The final rule must be concrete enough that another agent can follow it without reading the original conversation.
