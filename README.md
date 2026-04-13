# Claude Skills

Custom skills for [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) — reusable prompt frameworks that extend Claude's capabilities with structured, domain-specific workflows.

## What Are Skills?

Skills are markdown instruction sets that Claude Code loads automatically based on trigger phrases. When you say something like "red team this plan," Claude finds the matching skill and follows its framework instead of improvising — giving you consistent, high-quality output every time.

## Available Skills

### Decision & Planning

| Skill | Description | Triggers |
| --- | --- | --- |
| [give-options](give-options) | Adversarial options analysis — generates candidate solutions, stress-tests each one, and delivers a clear recommendation | "give me options," "what are my options," "propose approaches," "how should I tackle," "trade-off analysis" |
| [plan-review](plan-review) | Adversarial audit and stress-testing of plans, strategies, and proposals | "review this plan," "stress-test this," "what could go wrong," "red team this" |
| [pre-mortem](pre-mortem) | Narrative failure analysis — imagines the project already failed and works backward through the causal chain | "pre-mortem this," "imagine this fails," "what kills this project," "war-game this" |
| [assumption-mapper](assumption-mapper) | Surfaces and stress-ranks the unstated assumptions embedded in any plan, decision, or design | "what are we assuming here," "map the assumptions," "what has to be true for this to work" |
| [decision-logger](decision-logger) | Captures key decisions with alternatives, rationale, risks, and revisit triggers into a persistent log | "log this decision," "capture that choice," "show me decisions," "why did we choose X" |
| [signal-tracker](signal-tracker) | Derives a structured early-warning watchlist from any plan or architecture so you know during execution whether things are going off track | "what should I be monitoring," "set up early warning signals," "signal-track this" |
| [retro](retro) | Structured post-execution retrospective that extracts causal chains, decision quality, and forward-learning from real outcomes | "retro this," "debrief this," "what did we learn," "post-mortem this," "why did this go wrong" |

### Research & Code Analysis

| Skill | Description | Triggers |
| --- | --- | --- |
| [research-scout](research-scout) | Analyzes code to surface cutting-edge research papers and engineering techniques that could improve or optimize the implementation | "research-scout this," "find new techniques for this," "what does recent research say about this code" |
| [research-lineage](research-lineage) | Maps code to the published research papers and techniques it implements, with canonical citations and a technique timeline | "research-lineage this," "what research is this code based on," "map this code to papers" |
| [code-prep](code-prep) | Generates a CONTEXT.md companion file with architecture map, dependency graph, and change risk map for optimal Claude Code comprehension | "prep this code," "map out this codebase," "generate a context file," "help Claude Code understand this" |

### Product & GTM

| Skill | Description | Triggers |
| --- | --- | --- |
| [competitive-diff](competitive-diff) | Technically grounded competitive differentiation — compares your actual code and architecture against competitor public documentation | "how do we compare to X," "competitive brief," "battle card for X," "what do we win on" |
| [positioning-stress-test](positioning-stress-test) | Adversarial stress-test of positioning statements, value propositions, and differentiation claims before they reach a technical buyer | "stress-test this positioning," "is this defensible," "does this positioning hold," "red team this messaging" |
| [proof-point-miner](proof-point-miner) | Mines a codebase or technical artifact for concrete, defensible claims that land with technical buyers | "find proof points in this," "what claims can we make," "ground our positioning in the code" |
| [technical-narrative](technical-narrative) | Constructs a compelling technical narrative from a codebase or architecture docs — the story of why the system was built this way | "write the technical story," "explain our design philosophy," "why did we build it this way" |
| [release-brief](release-brief) | Produces a complete, multi-format release asset pack from a git diff or changelog — calibrated per audience | "brief this release," "generate release assets," "prepare the launch kit," "what do I tell sales about this release" |

### Communication & Knowledge

| Skill | Description | Triggers |
| --- | --- | --- |
| [comms-frame](comms-frame) | Translates technical decisions, architectures, or proposals into communications calibrated for a specific audience | "frame this for execs," "translate this for the customer," "help me explain this to leadership" |
| [evergreen-extractor](evergreen-extractor) | Extracts durable atomic notes from any session or analysis, formatted for direct insertion into an Obsidian vault | "extract notes from this," "make this Obsidian-ready," "atomic notes," "save this to my vault" |
| [context-check](context-check) | Saves session state to CLAUDE.md and git before context compaction or session transitions | "context check," "save state," "checkpoint," "wrap up" |

### How They Work Together

```
Explore Options → Plan → Audit → Execute → Monitor → Review → Improve
       │            │       │                  │         │         │
  give-options      │  ┌────┼────┐      signal-tracker   │    research-scout
  (generates and    │  │    │    │      (early-warning    │    (surfaces new
   stress-tests     │ plan- │  pre-     watchlist)      retro    research)
   candidates)      │ review│  mortem                  (causal
                    │       │                           learning)
              assumption-  decision-
              mapper       logger          research-lineage
              (hidden      (captures       (maps code to
               deps)        choices)        published papers)

                         ──── Communication Layer ────
              comms-frame · release-brief · technical-narrative
              (audience-calibrated output from any phase)

                         ──── GTM Intelligence ────
         competitive-diff · positioning-stress-test · proof-point-miner
              (ground positioning in actual code and architecture)

                         ──── Knowledge Persistence ────
              context-check · evergreen-extractor · code-prep
```

**Decision & Planning:** **give-options** generates multiple candidate solutions and stress-tests each adversarially. **plan-review** dissects the plan analytically — assumptions, failure modes, gaps. **pre-mortem** generates realistic failure stories that surface timing, political, and compounding risks. **assumption-mapper** exposes the hidden dependencies and unstated beliefs underneath any plan. **decision-logger** captures choices so rationale survives beyond the session. **signal-tracker** creates a watchlist of leading indicators so you catch drift during execution. **retro** extracts causal chains and forward-learning after outcomes arrive.

**Research & Code Analysis:** **research-scout** searches arXiv, Papers With Code, and engineering blogs for techniques that could improve your code. **research-lineage** does the reverse — identifies which established research your code already implements. **code-prep** generates a CONTEXT.md companion so Claude Code can orient instantly in unfamiliar codebases.

**Product & GTM:** **competitive-diff** goes below features to architectural philosophy and design tradeoffs. **positioning-stress-test** runs your claims through multiple buyer personas before they go live. **proof-point-miner** extracts defensible, technically grounded statements from your actual code. **technical-narrative** builds the story of why the system was designed this way. **release-brief** turns diffs and changelogs into audience-calibrated release assets.

**Communication & Knowledge:** **comms-frame** translates technical content for any audience — execs, customers, regulators. **evergreen-extractor** distills sessions into atomic Obsidian notes. **context-check** preserves session state across context compaction boundaries.

## Installation

### Quick Setup

```bash
git clone https://github.com/grlasser/claude-skills.git ~/Projects/claude-skills

# Install all skills at once
for skill in ~/Projects/claude-skills/*/; do
  name=$(basename "$skill")
  ln -sf "$skill" ~/.claude/skills/"$name"
done
```

Or install individually:

```bash
ln -s ~/Projects/claude-skills/<skill-name> ~/.claude/skills/<skill-name>
```

### How It Works

Claude Code looks for skills in `~/.claude/skills/` (global) and `.claude/skills/` (project-level). This repo uses symlinks so skills stay in a single git-managed location while remaining discoverable by Claude.

```
~/.claude/skills/
├── assumption-mapper   -> ~/Projects/claude-skills/assumption-mapper
├── code-prep           -> ~/Projects/claude-skills/code-prep
├── comms-frame         -> ~/Projects/claude-skills/comms-frame
├── competitive-diff    -> ~/Projects/claude-skills/competitive-diff
├── context-check       -> ~/Projects/claude-skills/context-check
├── decision-logger     -> ~/Projects/claude-skills/decision-logger
├── evergreen-extractor -> ~/Projects/claude-skills/evergreen-extractor
├── give-options        -> ~/Projects/claude-skills/give-options
├── plan-review         -> ~/Projects/claude-skills/plan-review
├── positioning-stress-test -> ~/Projects/claude-skills/positioning-stress-test
├── pre-mortem          -> ~/Projects/claude-skills/pre-mortem
├── proof-point-miner   -> ~/Projects/claude-skills/proof-point-miner
├── release-brief       -> ~/Projects/claude-skills/release-brief
├── research-lineage    -> ~/Projects/claude-skills/research-lineage
├── research-scout      -> ~/Projects/claude-skills/research-scout
├── retro               -> ~/Projects/claude-skills/retro
├── signal-tracker      -> ~/Projects/claude-skills/signal-tracker
├── technical-narrative -> ~/Projects/claude-skills/technical-narrative
├── docx                -> ...  (built-in)
├── pdf                 -> ...  (built-in)
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

# On other machine:
cd ~/Projects/claude-skills && git pull
```

Symlinks pick up changes immediately — no reinstall needed.

## Complementary Tools

These skills are designed to work alongside the [Superpowers plugin](https://github.com/obra/superpowers) for Claude Code, which covers Brainstorm → Plan → Execute → Debug. The skills in this repo fill the gaps Superpowers doesn't cover: adversarial option analysis, plan review, narrative failure analysis, decision capture, session continuity, and research-backed code analysis.

## Author

Greg Lasserre — Director of Product Management AI & Research, Nokia IP Networks
