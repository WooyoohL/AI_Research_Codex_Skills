---
name: ai-research-orchestrator
description: Entry point for modular AI/ML research idea discovery. Use when the user wants to find, evaluate, sharpen, or execute paper-oriented AI research ideas. Routes through literature bootstrapping, signal mining, problem formulation, claim formation, prior-work triangulation, scope gating, decision-value experiments, reviewer risk checks, and paper-shape planning while maintaining research_state artifacts.
---

# AI Research Orchestrator

## Purpose

Coordinate the modular AI/ML research-idea pipeline. Do not run the whole pipeline in one pass. Route to the next appropriate skill, maintain persistent state documents, and keep each stage bounded by its exit condition.

This orchestrator is for paper-oriented AI/ML research idea development, not startup ideation or generic brainstorming.

## Default pipeline

1. `entry-source-intake`
2. `representative-literature-bootstrap`
3. `research-signal-mining`
4. `problem-formulation`
5. `candidate-claim-set`
6. `research-move-router`
7. `claim-prior-work-triangulation`
8. `paper-unit-scope-gate`
9. `decision-value-experiment-planner`
10. `reviewer-risk-check`
11. `paper-shape-generator`

Specialist lens available when appropriate:

- `research-target-reframing`

Infrastructure skill:

- `research-state-artifact-management`

## Core rule

The workflow is not linear bureaucracy. It is a finite decision process:

```text
field map → signals → problem formulation → candidate claims → prior-work collision → residual contribution → paper unit → decision-value experiments → reviewer risks → paper shape
```

At each stage, ask:

```text
What is the most decision-relevant uncertainty right now?
Which next action most reduces that uncertainty?
What state artifact must be updated so the work can resume later?
```

## Entry routing

First inspect the user’s state:

| User starts with | Route |
|---|---|
| only a broad area | `entry-source-intake` → `representative-literature-bootstrap` |
| a paper list or folder of PDFs | `representative-literature-bootstrap` |
| a vague idea | `problem-formulation` → `candidate-claim-set` |
| a concrete method idea | `problem-formulation` → `candidate-claim-set` → `claim-prior-work-triangulation` |
| failed experiments or results | `problem-formulation` → `candidate-claim-set` → `decision-value-experiment-planner` |
| a near-paper proposal | `claim-prior-work-triangulation` → `paper-unit-scope-gate` |
| a draft/paper plan | `reviewer-risk-check` → `paper-shape-generator` |

Ask at most two clarifying questions before proceeding. If the missing information is not blocking, make an explicit assumption, record it, and continue.

## State management

Before doing substantive work, ensure a `research_state/` directory exists. If not, initialize it using the templates in:

```text
.agents/skills/research-state-artifact-management/assets/templates/
```

Optional helper:

```bash
python .agents/skills/research-state-artifact-management/scripts/init_research_state.py --project-name "My Research Project"
```

The two source-of-truth files are:

```text
research_state/00_state/current_state.md
research_state/00_state/decision_log.md
```

Every decision-relevant milestone must update these files.

## Stage exit conditions

Do not move to the next stage until the current stage has produced its required artifact.

| Stage | Required artifact / exit condition |
|---|---|
| Entry | area, entry state, available sources, resource constraints, next module |
| Literature | `field_map.md`, method families, evaluation protocols, closest works, at least 3 signals |
| Signals | `signal_bank.md` with sources, abnormality, candidate moves |
| Problem | problem statement, why it matters, current gap, problem owner, non-problem boundary |
| Claims | 2–4 candidate claims linked to a source problem, with prediction and disproof |
| Move routing | provisional contribution type for each active claim |
| Prior work | collision map, residual contribution, novelty coverage status |
| Scope | verdict: too thin / too broad / well-scoped / pivot / abandon |
| Experiments | hypothesis, decision, minimum valid setup, stop condition |
| Reviewer | top fatal risks only |
| Paper shape | thesis, contributions, necessary evidence, next action |

## Global hard rules

1. No clear problem, no claim generation.
2. No clear claim, no novelty check.
3. No prior-work collision, no final paper-worthiness judgment.
4. Evaluate residual contribution, not raw idea.
5. Do not expand scope to compensate for a weak core claim.
6. Experiments must have decision value.
7. Minimal experiments must preserve the problem essence; cheap invalid proxies are not acceptable.
8. Every decision-relevant milestone must checkpoint to `research_state/`.
9. Research moves are provisional until prior-work triangulation.
10. Novelty can be partially verified, not proven from memory.
11. Reviewer simulation diagnoses risks; it does not predict acceptance.

## How to chain modules

Codex skills are not function calls. Do not assume one skill automatically invokes another. Instead:

1. Use this orchestrator to decide the next skill.
2. Explicitly continue with the next `$skill-name` when needed.
3. Write stage outputs into `research_state/`.
4. Start the next stage by reading `research_state/00_state/current_state.md`.

When in doubt, call the next skill explicitly in your response, for example:

```text
Next: use $representative-literature-bootstrap on the papers listed in research_state/01_literature/paper_index.md.
```

## Output format

For each turn, keep the output compact:

```text
Current stage:
What I used:
Decision / result:
State files updated or to update:
Next skill:
Next concrete action:
```
