# Context Guardian — Session State Preservation

A Claude Code skill that saves session state to `CLAUDE.md` and git before context compaction hits. Ensures nothing important is lost when Claude's context window fills up or when you switch sessions.

## The Problem

Claude Code sessions accumulate context — file edits, decisions, debugging paths, architecture choices. When context hits ~75%, compaction compresses the conversation and details disappear. Without a checkpoint, the next session (or post-compaction continuation) starts from a degraded understanding.

## How to Use

```
> context check
> save state
> checkpoint
> wrap up
```

Also works automatically via the PreCompact hook — fires before any compaction without you asking.

## What It Does

1. **Gathers state from git** — runs `git diff` and `git status` to identify actually-modified files instead of relying on Claude's memory (which degrades at high context)
2. **Updates CLAUDE.md** — writes a structured checkpoint: task, plan phase, active files, decisions, environment state, known issues, next steps
3. **Cross-checks decision-logger** — flags any significant decisions from the session that haven't been logged to `decisions.md` yet
4. **Git commits** — with a descriptive message that makes `git log` a readable session history
5. **Reports** — concise status with context-level recommendations

## What's Improved Over v1

- Uses `git diff` for ground truth instead of Claude's session memory
- Captures environment state (Ollama, containerlab, MCP servers, model config)
- Links to active plan phase ("Task 12 of 18" not just "in progress")
- Cross-references with decision-logger for missed captures
- Descriptive git commit messages instead of generic "session checkpoint"
- Explicit time budget — under 60 seconds, not a 5-minute context dump
- Preserves previous handoff notes instead of overwriting

## Installation

```bash
ln -s ~/Projects/claude-skills/context-check ~/.claude/skills/context-check
```
