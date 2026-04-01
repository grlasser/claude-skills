---
name: context-check
description: |
  Save session state to CLAUDE.md and git before context compaction. Use when the user says "context check", "save state", "checkpoint", "prepare for compact", "save session", or when you notice context is getting high. Works with the PreCompact hook for automatic protection, but can also be invoked manually at any time. Use this skill proactively if the user mentions context is above 50%. Also trigger when the user says "wrap up", "save progress", "I'm done for now", or "hand off."
---

# Context Guardian — Save Session State

Your job is to preserve session state to persistent storage (CLAUDE.md + git) so nothing important is lost during compaction or session transitions. Be thorough but concise — a bloated checkpoint defeats the purpose by eating the context it's trying to protect.

## When This Skill Runs

1. **Manually by the user** — they say "context check," "save state," "checkpoint," "wrap up"
2. **Automatically via PreCompact hook** — fires before any compact (auto at ~75% or manual)

In both cases, follow the same steps below.

## Step 1: Gather State Automatically

Before writing anything, collect real data — don't rely on your memory of the session:

```bash
# What files were actually modified
git diff --name-only HEAD 2>/dev/null || git status --short

# Current branch and recent commits
git log --oneline -5 2>/dev/null

# Check for active plans
ls .claude/plans/ 2>/dev/null

# Check for decision log
cat .claude/plans/decisions.md 2>/dev/null | tail -20

# Check for running processes relevant to the project
pgrep -a ollama 2>/dev/null; pgrep -a containerlab 2>/dev/null
```

Use this output to populate the checkpoint — it's more reliable than reconstructing from conversation memory, especially at high context.

## Step 2: Update CLAUDE.md

Read the existing CLAUDE.md (or create one). Write or update a `## Session State` section using this template:

```markdown
## Session State
**Last updated**: [YYYY-MM-DD HH:MM]
**Branch**: [current git branch]
**Task**: [what we're building/fixing — one sentence]
**Plan phase**: [if an active plan exists in .claude/plans/, note which task/phase we're on, e.g. "Task 12 of 18 — Opus integration"]
**Status**: [current progress — what's done, what's in progress]

### Key decisions
- [decision and rationale — check .claude/plans/decisions.md for any that were logged]

### Active files (from git diff)
- [file paths actually modified this session, pulled from git, not from memory]

### Environment
- [model configured, MCP servers connected, running services like Ollama/containerlab]
- [any relevant env vars, ports, or config that a new session would need to know]

### Known issues
- [bugs, blockers, or concerns]

### Next steps
- [immediate actions in priority order]

### Patterns established
- [conventions, naming patterns, architecture choices established this session]
```

### Decision Logger Cross-Check

If `.claude/plans/decisions.md` exists, scan the current conversation for significant decisions that haven't been logged yet. If you find any, either:
- Log them now using the decision-logger format (if time permits)
- Or note them under "Key decisions" with a flag: `[NOT YET LOGGED]`

This checkpoint is a natural catch-all for missed decisions.

## Step 3: Git Commit

```bash
git add -A && git commit -m "checkpoint: [brief task description]"
```

Use a descriptive message — not "session checkpoint" but something like `checkpoint: Opus integration for GSM pipeline — Task 12 complete`. This makes `git log` a readable session history.

Skip if working tree is clean, but still update CLAUDE.md and commit that.

## Step 4: Report to User

Keep the report tight — 5-8 lines max:

- What was saved (files committed, CLAUDE.md updated)
- Current context level if known
- Any unlogged decisions flagged
- Recommendation:
  - Above 50%: "Good checkpoint. You have room to continue."
  - Above 70%: "Consider running `/compact` soon."
  - Above 90%: "Recommend starting a fresh session."

## Session Handoff

If the user says "wrap up," "I'm done for now," or "hand off," add a `## Handoff Notes` section to CLAUDE.md in addition to the Session State:

```markdown
## Handoff Notes
**Session ended**: [timestamp]

### Accomplished
- [completed items]

### In progress
- [partially done work with specific status]

### Gotchas
- [non-obvious things the next session needs to know]
- [things that almost worked but didn't — save debugging time]

### Resume with
- [key files to read first]
- [specific command or action to pick up where we left off]
```

Then tell the user:
```
State saved. Start a fresh session with:
"Read CLAUDE.md and continue from where the last session left off"
```

## After Any Compaction

If you've just been through a compaction (the conversation feels freshly compressed):
1. Re-read CLAUDE.md immediately
2. Run `git log --oneline -5` and `git diff --name-only` to re-orient
3. State back to the user what you understand the current task to be
4. Ask: "Does this match? Anything I'm missing?"

## What NOT To Do

- **Don't dump the entire conversation into CLAUDE.md.** The checkpoint should be 30-50 lines, not 200. If you're writing more than a screen of text, you're defeating the purpose.
- **Don't assess your own context percentage.** You can't do this accurately. Rely on the user telling you, or on the PreCompact hook firing.
- **Don't skip the git commands.** Even if it feels redundant, `git diff` output is ground truth — your memory of which files you touched is not.
- **Don't overwrite previous Handoff Notes.** If there are existing handoff notes from a prior session, move them under a `## Previous Sessions` section before writing new ones. The history is valuable.
- **Don't spend 5 minutes on the checkpoint.** This should take under 60 seconds. Gather, write, commit, report. Move fast — context is burning while you checkpoint.
