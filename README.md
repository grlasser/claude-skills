# Claude Skills

Custom skills for [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) — reusable prompt frameworks that extend Claude's capabilities with structured, domain-specific workflows.

## What Are Skills?

Skills are markdown instruction sets that Claude Code loads automatically based on trigger phrases. When you say something like "red team this plan," Claude finds the matching skill and follows its framework instead of improvising — giving you consistent, high-quality output every time.

## Available Skills

| Skill | Description | Triggers |
| --- | --- | --- |
| [give-options](./give-options) | Adversarial options analysis — generates candidate solutions, stress-tests each one, and delivers a clear recommendation. Supports parallel agent mode. | "give me options," "what are my options," "propose approaches," "how should I tackle," "trade-off analysis" |
| [plan-review](./plan-review) | Adversarial audit and stress-testing of plans, strategies, and proposals | "review this plan," "stress-test this," "what could go wrong," "red team this" |
| [assumption-mapper](./assumption-mapper) | Surfaces and stress-ranks the unstated assumptions embedded in any plan or decision — before you commit. Identifies assumption clusters, ranks by confidence × consequence-if-wrong, and specifies validation actions. | "what are we assuming here," "map the assumptions," "what has to be true for this to work," "assumption check this" |
| [pre-mortem](./pre-mortem) | Narrative failure analysis — imagines the project already failed and works backward through the causal chain | "pre-mortem this," "imagine this fails," "what kills this project," "war-game this" |
| [retro](./retro) | Post-execution retrospective that extracts causal chains, decision quality, and forward-learning from real outcomes. Separates good decisions from good luck. | "retro this," "debrief this," "what did we learn," "why did this go wrong," "what should we take forward" |
| [decision-logger](./decision-logger) | Captures key decisions with alternatives, rationale, risks, and revisit triggers into a persistent log | "log this decision," "capture that choice," "show me decisions," "why did we choose X" |
| [context-check](./context-check) | Saves session state to CLAUDE.md and git before context compaction or session transitions | "context check," "save state," "checkpoint," "wrap up" |
| [comms-frame](./comms-frame) | Translates technical decisions, analyses, or proposals into targeted communications for a specific audience — executives, customers, engineering peers, regulators, or non-technical stakeholders. Produces Framing Notes including divergence risk flags. | "frame this for execs," "translate this for the customer," "write this up for non-technical," "make this land with [stakeholder]" |
| [research-scout](./research-scout) | Analyzes code to surface cutting-edge research papers and engineering techniques that could improve or optimize the implementation | "research-scout this," "find new techniques for this," "what does recent research say about this code" |
| [code-prep](./code-prep) | Prepares Python codebases for Claude Code — generates a `CONTEXT.md` with architecture map, class/function inventory, namespaced call graph, and change risk table. Optionally enriches docstrings in place. | "prep this code," "document this for Claude Code," "map this codebase," "make this easier to debug," "generate a context file" |

### How They Work Together

The skills form a **decision intelligence loop** covering the full lifecycle from exploration through execution, review, and communication:

```
Explore → Validate Assumptions → Plan → Audit → Execute → Review → Communicate
   │               │               │       │         │        │          │
give-options  assumption-mapper  plan-  pre-mortem  code-   retro   comms-frame
(generates &    (excavates what  review  (narrative  prep   (what    (translates
 stress-tests    has to be true) (structural  failure  (prepares  actually  findings for
 candidates)     before commit)  audit)  modes)    codebase) happened) any audience)
                                             │
                                      decision-logger
                                    (captures choices
                                     made at any phase)
                                             │
                                       context-check
                                      (preserves state
                                       across sessions)
```

**give-options** generates multiple candidate solutions, stress-tests each adversarially, and recommends the strongest survivor.

**assumption-mapper** excavates the unstated beliefs embedded in any plan across six categories (people, technical, market, resources, knowledge, strategic), identifies assumption clusters where one failure cascades into others, ranks everything by confidence × consequence-if-wrong, and specifies the fastest validation path for each risk. Runs between option generation and plan review.

**plan-review** dissects the plan analytically — assumptions, failure modes, internal contradictions, second-order effects, and the single strongest counterargument a skeptic could make.

**pre-mortem** generates realistic failure narratives that surface timing, political, and compounding risks that structured analysis misses. Different angle from plan-review: narrative rather than analytical.

**retro** runs after execution to extract the real causal chain from what actually happened, audit decision quality vs. outcome quality (separating skill from luck), and produce specific forward-learning. The mirror of pre-mortem.

**decision-logger** captures decisions made at any point in the loop — with alternatives considered, rationale, risks, and triggers for revisiting — so the reasoning survives beyond the session.

**context-check** preserves full session state to CLAUDE.md and git before context compaction, ensuring nothing is lost across session boundaries.

**comms-frame** takes output from any other skill and produces audience-calibrated communications for executives, customers, engineering peers, regulators, press, or non-technical stakeholders. Includes Framing Notes with divergence risk flags — places where the reframe could cause the audience to form a different picture than the underlying reality warrants.

**research-scout** analyzes code patterns and searches arXiv, Papers With Code, and engineering blogs to find recent techniques, then maps each finding to a specific code location and proposes a concrete redesign.

**code-prep** runs before any Claude Code session on an unfamiliar or large Python codebase — it extracts the architecture, call graph, and change risk map into a `CONTEXT.md` file that Claude Code reads to orient itself instantly, without burning tokens on file exploration.

## Installation

### Quick Setup

```bash
git clone https://github.com/grlasser/claude-skills.git ~/Projects/claude-skills

ln -s ~/Projects/claude-skills/give-options ~/.claude/skills/give-options
ln -s ~/Projects/claude-skills/plan-review ~/.claude/skills/plan-review
ln -s ~/Projects/claude-skills/assumption-mapper ~/.claude/skills/assumption-mapper
ln -s ~/Projects/claude-skills/pre-mortem ~/.claude/skills/pre-mortem
ln -s ~/Projects/claude-skills/retro ~/.claude/skills/retro
ln -s ~/Projects/claude-skills/decision-logger ~/.claude/skills/decision-logger
ln -s ~/Projects/claude-skills/context-check ~/.claude/skills/context-check
ln -s ~/Projects/claude-skills/comms-frame ~/.claude/skills/comms-frame
ln -s ~/Projects/claude-skills/research-scout ~/.claude/skills/research-scout
ln -s ~/Projects/claude-skills/code-prep ~/.claude/skills/code-prep
```

`code-prep` requires two Python packages on first use:

```bash
pip install tree-sitter tree-sitter-python --break-system-packages
```

Repomix (used for compressed source bundles on large codebases) runs via `npx` with no install needed.

### How It Works

Claude Code looks for skills in `~/.claude/skills/` (global) and `.claude/skills/` (project-level). This repo uses symlinks so skills stay in a single git-managed location while remaining discoverable by Claude.

```
~/.claude/skills/
├── give-options       -> ~/Projects/claude-skills/give-options
├── plan-review        -> ~/Projects/claude-skills/plan-review
├── assumption-mapper  -> ~/Projects/claude-skills/assumption-mapper
├── pre-mortem         -> ~/Projects/claude-skills/pre-mortem
├── retro              -> ~/Projects/claude-skills/retro
├── decision-logger    -> ~/Projects/claude-skills/decision-logger
├── context-check      -> ~/Projects/claude-skills/context-check
├── comms-frame        -> ~/Projects/claude-skills/comms-frame
├── research-scout     -> ~/Projects/claude-skills/research-scout
├── code-prep          -> ~/Projects/claude-skills/code-prep
├── docx               -> ...  (built-in)
├── pdf                -> ...  (built-in)
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

# on other machine:
cd ~/Projects/claude-skills && git pull
```

Symlinks pick up changes immediately — no reinstall needed.

## Complementary Tools

These skills are designed to work alongside the [Superpowers plugin](https://github.com/obra/superpowers) for Claude Code, which covers Brainstorm → Plan → Execute → Debug. The skills in this repo fill the gaps Superpowers doesn't cover: adversarial option analysis, assumption excavation, plan review, narrative failure analysis, post-execution retrospectives, decision capture, session continuity, audience-calibrated communications, research-backed code improvement, and codebase preparation for AI-assisted work.

## Contributing

Skills are markdown files — no build step, no dependencies beyond the optional Python packages for `code-prep`. To contribute a skill, open a PR with a new folder containing `SKILL.md` and `README.md`.
