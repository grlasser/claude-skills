# Claude Skills

Custom skills for [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code): reusable prompt frameworks that extend Claude's capabilities with structured, domain-specific workflows.

## What Are Skills?

Skills are markdown instruction sets that Claude Code loads automatically based on trigger phrases. When you say something like "red team this plan," Claude finds the matching skill and follows its framework instead of improvising, giving you consistent, high-quality output every time.

## Available Skills

| Skill | Description | Triggers |
| --- | --- | --- |
| [give-options](https://github.com/grlasser/claude-skills/blob/main/give-options) | Adversarial options analysis — generates candidate solutions, stress-tests each one, and delivers a clear recommendation. Supports parallel agent mode. | "give me options," "what are my options," "propose approaches," "how should I tackle," "trade-off analysis" |
| [plan-review](https://github.com/grlasser/claude-skills/blob/main/plan-review) | Adversarial audit and stress-testing of plans, strategies, and proposals | "review this plan," "stress-test this," "what could go wrong," "red team this" |
| [pre-mortem](https://github.com/grlasser/claude-skills/blob/main/pre-mortem) | Narrative failure analysis — imagines the project already failed and works backward through the causal chain | "pre-mortem this," "imagine this fails," "what kills this project," "war-game this" |
| [decision-logger](https://github.com/grlasser/claude-skills/blob/main/decision-logger) | Captures key decisions with alternatives, rationale, risks, and revisit triggers into a persistent log | "log this decision," "capture that choice," "show me decisions," "why did we choose X" |
| [context-check](https://github.com/grlasser/claude-skills/blob/main/context-check) | Saves session state to CLAUDE.md and git before context compaction or session transitions | "context check," "save state," "checkpoint," "wrap up" |
| [research-scout](https://github.com/grlasser/claude-skills/blob/main/research-scout) | Analyzes code to surface cutting-edge research papers and engineering techniques that could improve or optimize the implementation | "research-scout this," "find new techniques for this," "what does recent research say about this code" |
| [code-prep](https://github.com/grlasser/claude-skills/blob/main/code-prep) | Prepares Python codebases for Claude Code — generates a `CONTEXT.md` with architecture map, class/function inventory, namespaced call graph, and change risk table. Optionally enriches docstrings in place. Uses Tree-sitter for error-tolerant parsing and Repomix for compressed source bundles. | "prep this code," "document this for Claude Code," "map this codebase," "make this easier to debug," "generate a context file" |

### How They Work Together

```
Explore Options → Plan → Audit → Execute → Review → Improve
       │                   │                 │          │
  give-options     ┌───────┼───────┐   code-prep   research-scout
  (generates and   │       │       │   (prepares   (surfaces research
   stress-tests   plan-review │  pre-mortem  codebase    and proposes new
   candidates)   (structural) │  (narrative) for Claude   designs based on
                              │              Code before   recent papers)
                       decision-logger       any session)
                      (captures choices
                       made at any phase)
                              │
                       context-check
                      (preserves state
                       across sessions)
```

**give-options** generates multiple candidate solutions, stress-tests each adversarially, and recommends the strongest survivor. **plan-review** dissects the plan analytically — assumptions, failure modes, gaps, contradictions. **pre-mortem** generates realistic failure stories that surface timing, political, and compounding risks that structured analysis misses. **decision-logger** captures the choices you make at any point so rationale survives beyond the session. **context-check** preserves the full session state to CLAUDE.md and git before context compaction wipes the slate. **research-scout** analyzes code patterns and searches arXiv, Papers With Code, and engineering blogs to find recent techniques — then maps each finding to a specific code location and proposes a concrete redesign. **code-prep** runs before any Claude Code session on an unfamiliar or messy Python codebase — it extracts the architecture, call graph, and change risk map into a `CONTEXT.md` file that Claude Code reads to orient itself instantly, without burning tokens on file exploration.

## Installation

### Quick Setup

```
git clone https://github.com/grlasser/claude-skills.git ~/Projects/claude-skills

ln -s ~/Projects/claude-skills/give-options ~/.claude/skills/give-options
ln -s ~/Projects/claude-skills/plan-review ~/.claude/skills/plan-review
ln -s ~/Projects/claude-skills/pre-mortem ~/.claude/skills/pre-mortem
ln -s ~/Projects/claude-skills/decision-logger ~/.claude/skills/decision-logger
ln -s ~/Projects/claude-skills/context-check ~/.claude/skills/context-check
ln -s ~/Projects/claude-skills/research-scout ~/.claude/skills/research-scout
ln -s ~/Projects/claude-skills/code-prep ~/.claude/skills/code-prep
```

`code-prep` requires two Python packages on first use:

```
pip install tree-sitter tree-sitter-python --break-system-packages
```

Repomix (used for compressed source bundles on large codebases) runs via `npx` with no install needed.

### How It Works

Claude Code looks for skills in `~/.claude/skills/` (global) and `.claude/skills/` (project-level). This repo uses symlinks so skills stay in a single git-managed location while remaining discoverable by Claude.

```
~/.claude/skills/
├── give-options     -> ~/Projects/claude-skills/give-options
├── plan-review      -> ~/Projects/claude-skills/plan-review
├── pre-mortem       -> ~/Projects/claude-skills/pre-mortem
├── decision-logger  -> ~/Projects/claude-skills/decision-logger
├── context-check    -> ~/Projects/claude-skills/context-check
├── research-scout   -> ~/Projects/claude-skills/research-scout
├── code-prep        -> ~/Projects/claude-skills/code-prep
├── docx             -> ...  (built-in)
├── pdf              -> ...  (built-in)
└── ...
```

### Adding a New Skill

1. Create a folder in this repo with a `SKILL.md` file
2. Symlink it: `ln -s ~/Projects/claude-skills/<skill-name> ~/.claude/skills/<skill-name>`
3. Start a new Claude session — the skill is live

### Syncing Across Machines

```
cd ~/Projects/claude-skills
git add . && git commit -m "description" && git push

cd ~/Projects/claude-skills && git pull
```

Symlinks pick up changes immediately — no reinstall needed.

## Complementary Tools

These skills are designed to work alongside the [Superpowers plugin](https://github.com/obra/superpowers) for Claude Code, which covers Brainstorm → Plan → Execute → Debug. The skills in this repo fill the gaps Superpowers doesn't cover: adversarial option analysis, plan review, narrative failure analysis, decision capture, session continuity, research-backed code improvement, and codebase preparation for AI-assisted work.

## Author

Greg Lasserre
