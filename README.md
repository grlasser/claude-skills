# Claude Skills

Custom skills for [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) — reusable prompt frameworks that extend Claude's capabilities with structured, domain-specific workflows.

## What Are Skills?

Skills are markdown instruction sets that Claude Code loads automatically based on trigger phrases. When you say something like "red team this plan," Claude finds the matching skill and follows its framework instead of improvising — giving you consistent, high-quality output every time.

## Available Skills

| Skill | Description | Triggers |
|-------|-------------|----------|
| [plan-review](./plan-review/) | Adversarial audit and stress-testing of plans, strategies, and proposals | "review this plan," "stress-test this," "what could go wrong," "red team this" |
| [pre-mortem](./pre-mortem/) | Narrative failure analysis — imagines the project already failed and works backward through the causal chain | "pre-mortem this," "imagine this fails," "what kills this project," "war-game this" |
| [decision-logger](./decision-logger/) | Captures key decisions with alternatives, rationale, risks, and revisit triggers into a persistent log | "log this decision," "capture that choice," "show me decisions," "why did we choose X" |
| [context-check](./context-check/) | Saves session state to CLAUDE.md and git before context compaction or session transitions | "context check," "save state," "checkpoint," "wrap up" |
| [research-scout](./research-scout/) | Analyzes code to surface cutting-edge research papers and engineering techniques that could improve or optimize the implementation | "research-scout this," "find new techniques for this," "are there better patterns," "what does recent research say about this code" |

### How They Work Together

```
Brainstorm → Plan → Audit → Execute → Review → Improve
                      │                           │
              ┌───────┼───────┐           research-scout
              │       │       │           (surfaces research
         plan-review  │  pre-mortem        and proposes new
         (structural) │  (narrative)       designs based on
                      │                    recent papers)
               decision-logger
              (captures choices
               made at any phase)
                      │
               context-check
              (preserves state
               across sessions)
```

**plan-review** dissects the plan analytically — assumptions, failure modes, gaps, contradictions. **pre-mortem** generates realistic failure stories that surface timing, political, and compounding risks that structured analysis misses. **decision-logger** captures the choices you make at any point so rationale survives beyond the session. **context-check** preserves the full session state to CLAUDE.md and git before context compaction wipes the slate. **research-scout** analyzes code patterns and searches arXiv, Papers With Code, and engineering blogs to find recent techniques — then maps each finding to a specific code location and proposes a concrete redesign.

## Installation

### Quick Setup

```bash
git clone https://github.com/grlasser/claude-skills.git ~/Projects/claude-skills

ln -s ~/Projects/claude-skills/plan-review ~/.claude/skills/plan-review
ln -s ~/Projects/claude-skills/pre-mortem ~/.claude/skills/pre-mortem
ln -s ~/Projects/claude-skills/decision-logger ~/.claude/skills/decision-logger
ln -s ~/Projects/claude-skills/context-check ~/.claude/skills/context-check
ln -s ~/Projects/claude-skills/research-scout ~/.claude/skills/research-scout
```

### How It Works

Claude Code looks for skills in `~/.claude/skills/` (global) and `.claude/skills/` (project-level). This repo uses symlinks so skills stay in a single git-managed location while remaining discoverable by Claude.

```
~/.claude/skills/
├── plan-review      -> ~/Projects/claude-skills/plan-review
├── pre-mortem       -> ~/Projects/claude-skills/pre-mortem
├── decision-logger  -> ~/Projects/claude-skills/decision-logger
├── context-check    -> ~/Projects/claude-skills/context-check
├── research-scout   -> ~/Projects/claude-skills/research-scout
├── docx             -> ...  (built-in)
├── pdf              -> ...  (built-in)
└── ...
```

### Adding a New Skill

1. Create a folder in this repo with a `SKILL.md` file
2. Symlink it: `ln -s ~/Projects/claude-skills/<skill-name> ~/.claude/skills/<skill-name>`
3. Start a new Claude session — the skill is live

### Syncing Across Machines

```bash
cd ~/Projects/claude-skills
git add . && git commit -m "description" && git push

cd ~/Projects/claude-skills && git pull
```

Symlinks pick up changes immediately — no reinstall needed.

## Complementary Tools

These skills are designed to work alongside the [Superpowers plugin](https://github.com/obra/superpowers) for Claude Code, which covers Brainstorm → Plan → Execute → Debug. The skills in this repo fill the gaps Superpowers doesn't cover: adversarial review, narrative failure analysis, decision capture, session continuity, and research-backed code improvement.

## Author

Greg Lasserre — Director of Product Management AI & Research, Nokia IP Networks
