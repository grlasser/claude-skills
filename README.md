# Claude Skills

Custom skills for [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) — reusable prompt frameworks that extend Claude's capabilities with structured, domain-specific workflows.

## What Are Skills?

Skills are markdown instruction sets that Claude Code loads automatically based on trigger phrases. When you say something like "red team this plan," Claude finds the matching skill and follows its framework instead of improvising — giving you consistent, high-quality output every time.

---

## Skill Suites

Skills are organized into two suites plus supporting utilities. They share a canonical audience taxonomy and a common evidence tier system, and are designed to be chained — output from one feeds directly into the next.

### Suite 1 — Decision Intelligence

For planning, execution, and retrospection. Use these when building, designing, or deciding.

| Skill | What it does | Key triggers |
|---|---|---|
| [give-options](./give-options) | Generates candidate solutions, stress-tests each adversarially, delivers the strongest recommendation | "give me options," "what are my options," "trade-off analysis" |
| [assumption-mapper](./assumption-mapper) | Excavates unstated assumptions; ranks by confidence × consequence-if-wrong; specifies validation actions | "what are we assuming," "map the assumptions," "what has to be true" |
| [plan-review](./plan-review) | Adversarial structural audit of any plan, strategy, or architecture | "review this plan," "stress-test this," "red team this" |
| [pre-mortem](./pre-mortem) | Imagines the project already failed and works backward through the causal chain | "pre-mortem this," "imagine this fails," "what kills this project" |
| [signal-tracker](./signal-tracker) | Derives a structured early-warning watchlist — leading indicators, cadence, and pre-committed response protocols | "what should I be monitoring," "leading indicators for this," "signal-track this" |
| [retro](./retro) | Post-execution retrospective: causal chains, decision quality audit, luck vs. skill accounting | "retro this," "what did we learn," "why did this go wrong" |
| [decision-logger](./decision-logger) | Captures key decisions with alternatives, rationale, risks, and revisit triggers | "log this decision," "capture that choice," "why did we choose X" |
| [context-check](./context-check) | Saves session state to CLAUDE.md and git before context compaction | "context check," "save state," "checkpoint" |

**How they chain:**
```
give-options → assumption-mapper → plan-review → pre-mortem
                                                      |
                                               [execution]
                                                      |
                                            signal-tracker (monitors)
                                                      |
                                                   retro
                                      (decision-logger throughout)
                                      (context-check each session)
```

---

### Suite 2 — Technical Product Marketing

For TPM engineers, technical writers, and anyone with code and docs access who needs positioning, competitive intelligence, or release collateral.

| Skill | What it does | Key triggers |
|---|---|---|
| [proof-point-miner](./proof-point-miner) | Mines code and docs for defensible claims; rates by credibility tier; detects positioning gaps | "find proof points," "what can we back up," "mine this for marketing material" |
| [positioning-stress-test](./positioning-stress-test) | Adversarially challenges positioning through three buyer personas; generates falsification scenarios | "stress-test this positioning," "is this defensible," "red team this messaging" |
| [competitive-diff](./competitive-diff) | Architectural-level competitive analysis with asymmetric win/loss/draw map and field-ready battle card | "how do we compare to X," "competitive brief," "battle card for X" |
| [technical-narrative](./technical-narrative) | Constructs a technical story from design decisions — three depths simultaneously | "write the technical story," "build the architecture narrative," "explain our design philosophy" |
| [comms-frame](./comms-frame) | Translates any content for a specific audience; includes framing notes and divergence risk flags | "frame this for execs," "translate this for the customer," "make this land with [stakeholder]" |
| [release-brief](./release-brief) | Produces a full 6-format release asset pack calibrated per audience, with proof point delta | "brief this release," "generate release assets," "prepare the launch kit" |
| [evergreen-extractor](./evergreen-extractor) | Extracts durable atomic notes formatted for Obsidian with wikilinks, routing, and expiry flags | "extract notes from this," "make this Obsidian-ready," "atomic notes" |

**How they chain:**
```
proof-point-miner ──────────────────────────────────┐
      |                                              |
positioning-stress-test → technical-narrative → comms-frame
      |                          |
competitive-diff         release-brief ──→ proof-point-miner (delta loop)
                                |
                        evergreen-extractor ← all skills feed this
                               |
                         Obsidian vault
```

**Shared standards across Suite 2:**

*Credibility tier system (your product claims):*

| Tier | Type | Use |
|---|---|---|
| **1** | Measured/Benchmarked | Lead with. Fully defensible. |
| **2** | Architectural Decision | Strong. Implies expertise. |
| **3** | Design Intent | Usable with care. |
| **4** | Assertion | Flag for elevation or retirement. |

*Competitor evidence system:* **V** Verified · **S** Stated · **I** Inferred (hedge) · **A** Assumed (internal only)

*Canonical audience taxonomy:* Technical evaluator · Architect/technical lead · DevOps/SRE/ops · Compliance/security/risk · Procurement/vendor risk · Executive/budget owner · Technical buyer (customer) · Business buyer (customer)

---

### Supporting Skills

| Skill | What it does | Key triggers |
|---|---|---|
| [research-scout](./research-scout) | Analyzes code to surface cutting-edge research papers and engineering techniques | "research-scout this," "find new techniques for this" |
| [code-prep](./code-prep) | Prepares Python codebases for Claude Code — generates CONTEXT.md with architecture map and call graph | "prep this code," "map this codebase," "generate a context file" |

---

## Installation

### Quick Setup

```bash
git clone https://github.com/grlasser/claude-skills.git ~/Projects/claude-skills

# Suite 1 — Decision Intelligence
ln -s ~/Projects/claude-skills/give-options ~/.claude/skills/give-options
ln -s ~/Projects/claude-skills/assumption-mapper ~/.claude/skills/assumption-mapper
ln -s ~/Projects/claude-skills/plan-review ~/.claude/skills/plan-review
ln -s ~/Projects/claude-skills/pre-mortem ~/.claude/skills/pre-mortem
ln -s ~/Projects/claude-skills/signal-tracker ~/.claude/skills/signal-tracker
ln -s ~/Projects/claude-skills/retro ~/.claude/skills/retro
ln -s ~/Projects/claude-skills/decision-logger ~/.claude/skills/decision-logger
ln -s ~/Projects/claude-skills/context-check ~/.claude/skills/context-check

# Suite 2 — Technical Product Marketing
ln -s ~/Projects/claude-skills/proof-point-miner ~/.claude/skills/proof-point-miner
ln -s ~/Projects/claude-skills/positioning-stress-test ~/.claude/skills/positioning-stress-test
ln -s ~/Projects/claude-skills/competitive-diff ~/.claude/skills/competitive-diff
ln -s ~/Projects/claude-skills/technical-narrative ~/.claude/skills/technical-narrative
ln -s ~/Projects/claude-skills/comms-frame ~/.claude/skills/comms-frame
ln -s ~/Projects/claude-skills/release-brief ~/.claude/skills/release-brief
ln -s ~/Projects/claude-skills/evergreen-extractor ~/.claude/skills/evergreen-extractor

# Supporting
ln -s ~/Projects/claude-skills/research-scout ~/.claude/skills/research-scout
ln -s ~/Projects/claude-skills/code-prep ~/.claude/skills/code-prep
```

`code-prep` requires two Python packages on first use:
```bash
pip install tree-sitter tree-sitter-python --break-system-packages
```

### How It Works

Claude Code looks for skills in `~/.claude/skills/` (global) and `.claude/skills/` (project-level). This repo uses symlinks so skills stay in a single git-managed location while remaining discoverable by Claude.

```
~/.claude/skills/
├── give-options            -> ~/Projects/claude-skills/give-options
├── assumption-mapper       -> ~/Projects/claude-skills/assumption-mapper
├── plan-review             -> ~/Projects/claude-skills/plan-review
├── pre-mortem              -> ~/Projects/claude-skills/pre-mortem
├── signal-tracker          -> ~/Projects/claude-skills/signal-tracker
├── retro                   -> ~/Projects/claude-skills/retro
├── decision-logger         -> ~/Projects/claude-skills/decision-logger
├── context-check           -> ~/Projects/claude-skills/context-check
├── proof-point-miner       -> ~/Projects/claude-skills/proof-point-miner
├── positioning-stress-test -> ~/Projects/claude-skills/positioning-stress-test
├── competitive-diff        -> ~/Projects/claude-skills/competitive-diff
├── technical-narrative     -> ~/Projects/claude-skills/technical-narrative
├── comms-frame             -> ~/Projects/claude-skills/comms-frame
├── release-brief           -> ~/Projects/claude-skills/release-brief
├── evergreen-extractor     -> ~/Projects/claude-skills/evergreen-extractor
├── research-scout          -> ~/Projects/claude-skills/research-scout
└── code-prep               -> ~/Projects/claude-skills/code-prep
```

### Adding a New Skill

1. Create a folder with a `SKILL.md` file (and optionally a `README.md`)
2. Symlink it: `ln -s ~/Projects/claude-skills/<name> ~/.claude/skills/<name>`
3. Start a new Claude session — the skill is live

### Syncing Across Machines

```bash
# Push
cd ~/Projects/claude-skills
git add . && git commit -m "description" && git push

# Pull (on other machine — symlinks pick up changes immediately)
cd ~/Projects/claude-skills && git pull
```

---

## Complementary Tools

These skills are designed to work alongside the [Superpowers plugin](https://github.com/obra/superpowers) for Claude Code, which covers Brainstorm → Plan → Execute → Debug. The skills in this repo fill the gaps Superpowers doesn't cover: adversarial option analysis, assumption excavation, plan review, narrative failure analysis, mid-execution monitoring, post-execution retrospectives, decision capture, session continuity, technical product marketing intelligence, audience-calibrated communications, and knowledge graph integration.

## Contributing

Skills are markdown files — no build step, no dependencies beyond the optional Python packages for `code-prep`. To contribute, open a PR with a new folder containing `SKILL.md` and `README.md`.
