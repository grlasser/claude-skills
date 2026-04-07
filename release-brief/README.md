# release-brief

Produces a complete, multi-format release asset pack from a git diff, release notes, or changelog — calibrated per audience, aligned with existing positioning, and closed with a proof point delta that feeds back into the positioning intelligence system.

## What It Does

A release that ships without the right collateral reaches the wrong audiences with the wrong message. SEs get marketing copy. Executives get technical changelogs. Customers discover contradictions between what they were told and what shipped.

This skill produces all six release formats in a single pass, each purpose-built for its audience from the source material. It starts by classifying the release type (which determines which assets are needed), scores every change by significance to each audience, checks for positioning contradictions before any external assets are written, and closes with a proof point delta that updates the running positioning inventory.

## Trigger Phrases

- "brief this release"
- "generate release assets"
- "write up this feature"
- "turn these release notes into collateral"
- "prepare the launch kit"
- "what do I tell sales about this release"
- "create the release package"

## Release Classification → Asset Selection

| Release type | Assets produced |
|---|---|
| Major feature | All 6 |
| Minor improvement | 2 (SE deep-dive), 3 (exec), 5 (changelog), 6 (support) |
| Bug fix / patch | 5 (changelog), 6 (support) |
| Security patch | 5, 6, internal exec note — no external assets |
| Breaking change | All 6 + migration guide |
| Architecture refactor | 2, 3, 5 — no external blog or sales one-pager |

## Six Assets

| # | Asset | Audience | Length |
|---|---|---|---|
| 1 | Sales one-pager | AEs, sales leadership | ~400 words |
| 2 | SE technical deep-dive | Sales engineers, presales | ~800 words |
| 3 | Executive summary | Leadership, customer execs | ~200 words |
| 4 | External blog + social hook | Community, press, prospects | ~300w + 3 social variants |
| 5 | Changelog entry | Existing users, developers | As needed |
| 6 | Support talking points | CS, support, partner SEs | Calibrated to release type |

## Proof Point Delta

Every release brief closes with a structured update to the proof point inventory — new Tier 1 and Tier 2 claims with credibility tier, audience, competitive rating, falsification risk, and source. This feeds directly into `proof-point-miner` and `evergreen-extractor`, closing the loop between the release workflow and the cumulative positioning intelligence system.

## How It Fits

```
[git diff / release notes] → release-brief → proof-point-miner (delta update)
                                   ↓              ↓
                             comms-frame    evergreen-extractor
                                   ↓
                         positioning-stress-test (new claims → stress test)
                                   ↓
                          competitive-diff (high-differentiation items → battle card refresh)
```
