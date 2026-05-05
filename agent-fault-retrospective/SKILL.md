---
name: agent-fault-retrospective
description: Use when the user says the AI agent, Codex, assistant, or model made a mistake, overstepped, misunderstood instructions, needs a postmortem/retrospective/review, should record fault keywords in AGENTS.md, or should automatically trigger a fault-review skill for future similar cases. This skill guides the agent to ask the user what counted as the fault, update AGENTS.md with concise trigger keywords and behavior rules, and use a Superpowers-style root-cause review before writing durable agent behavior constraints.
version: 0.1.0
---

# Agent Fault Retrospective

This skill turns a user-identified agent mistake into durable operating rules.

The goal is not to write a long apology. The goal is to extract the user's judgment, identify the failure mechanism, and update the relevant `AGENTS.md` with short, executable guardrails.

## Use This Skill When

Use this skill when the user says or implies any of the following:

- the agent made a mistake, overstepped, or violated instructions
- the agent should reflect, review, inspect, postmortem, or do a retrospective
- the agent should remember a mistake, record a fault, or update `AGENTS.md`
- the user wants keywords or trigger phrases added so future similar cases automatically invoke this skill
- the task mentions fault keywords already recorded in `AGENTS.md`

Trigger examples include: `过失`, `失误`, `错误`, `检讨`, `复盘`, `越权`, `记住这次`, `写进 agents.md`, `自动调用该 skill`, `mistake`, `fault`, `postmortem`, `retrospective`.

## Non-Negotiable Boundaries

- Do not defend, debate, or dilute the user's claim that a fault occurred.
- Do not assume where `AGENTS.md` lives if the target is unclear.
- Do not create a new project `AGENTS.md` just because the current directory lacks one.
- Do not write a long retrospective into `AGENTS.md`.
- Do not expand ambiguous user wording into broader tool actions or irreversible operations.

## Required Workflow

### 1. Locate the Correct Agent Record

Use this priority order:

1. A path explicitly named by the user.
2. The active `AGENTS.md` supplied in the conversation context.
3. A clearly discoverable repository `AGENTS.md`, only if the user is talking about the current repo.
4. If none is clear, ask which agent record should be updated before writing.

If the user says "你的 agent.md" or "你的 agents.md", treat that as an instruction to update the agent's actual durable instruction record, not automatically the current project's root file.

### 2. First-Use Bootstrap

If the target `AGENTS.md` does not already contain a fault-retrospective trigger rule, ask the user for:

1. The exact words or situations that should trigger this skill in the future.
2. The specific mistake category this incident belongs to.
3. Whether the agent may update the target `AGENTS.md` after summarizing the new rule.

Keep the questions short. Ask at most three at once.

After confirmation, add a concise trigger rule like:

```markdown
## 过失复盘 Skill 触发规则

- 当使用者指出 AI/Codex/agent 有「过失、失误、错误、越权、检讨、复盘、记住这次」等情境，必须优先调用 `agent-fault-retrospective`。
- 当任务命中已记录的高风险关键词时，必须先确认语义与操作边界，不得自行扩大解读。
- 复盘后只能将短规则、触发词、禁止事项、必做确认写入 `AGENTS.md`；不得把完整长篇检讨塞入 `AGENTS.md`。
```

### 3. Superpowers-Style Retrospective

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

### 4. Update `AGENTS.md`

Write only durable behavior constraints:

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

If a matching section already exists, update it in place. Do not duplicate sections.

## Output Expectations

When responding to the user during a retrospective, use this order:

1. `我理解的过失`
2. `需要你确认的关键词`
3. `根因复盘`
4. `准备写入 AGENTS.md 的短规则`
5. `请确认`

After the user confirms, perform the edit and report the file path changed.

## Quality Bar

A successful run leaves the agent with a sharper future constraint, not just a record that the agent felt sorry.

The final rule must be concrete enough that another agent can follow it without reading the original conversation.
