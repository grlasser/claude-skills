# Claude Skills

Custom skills for [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) — reusable prompt frameworks that extend Claude's capabilities with structured, domain-specific workflows.

## What Are Skills?

Skills are markdown instruction sets that Claude Code loads automatically based on trigger phrases. When you say something like "red team this plan," Claude finds the matching skill and follows its framework instead of improvising — giving you consistent, high-quality output every time.

## Available Skills

| Skill | Description | Triggers |
|-------|-------------|----------|
| [plan-review](./plan-review/) | Adversarial audit and stress-testing of plans, strategies, and proposals | "review this plan," "stress-test this," "what could go wrong," "red team this" |

## Installation

### Quick Setup

```bash
# Clone the repo
git clone https://github.com/grlasser/claude-skills.git ~/Projects/claude-skills

# Symlink into Claude's global skills directory
ln -s ~/Projects/claude-skills/plan-review ~/.claude/skills/plan-review
```

### How It Works

Claude Code looks for skills in `~/.claude/skills/` (global) and `.claude/skills/` (project-level). This repo uses symlinks so skills stay in a single git-managed location while remaining discoverable by Claude.

```
~/.claude/skills/
├── plan-review -> ~/Projects/claude-skills/plan-review   # from this repo
├── docx -> ...                                           # built-in
├── pdf -> ...                                            # built-in
└── ...
```

### Adding a New Skill

1. Create a folder in this repo with a `SKILL.md` file
2. Symlink it: `ln -s ~/Projects/claude-skills/<skill-name> ~/.claude/skills/<skill-name>`
3. Start a new Claude session — the skill is live

### Syncing Across Machines

```bash
# On the machine where you made changes
cd ~/Projects/claude-skills
git add . && git commit -m "description" && git push

# On the other machine
cd ~/Projects/claude-skills && git pull
```

Symlinks pick up changes immediately — no reinstall needed.

## Author

Greg Lasserre — Director of Product Management AI & Research, Nokia IP Networks
