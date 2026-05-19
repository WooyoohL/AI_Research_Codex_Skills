# AI Research Idea Discovery Skills for Codex

A modular Codex skill suite for AI/ML research idea discovery, paper-claim development, prior-work triangulation, scope control, decision-value experiments, and reviewer-risk checking.

This repository is designed so you can unzip it into a repository root or your home directory and invoke the skills directly from Codex.

## What this is

This is **not** an automatic top-conference paper generator. It is a structured workflow for converting a broad research direction, paper list, failed experiment, or vague idea into a paper-shaped research proposal with:

- a representative literature map;
- research signals and tensions;
- candidate falsifiable claims;
- prior-work collision analysis;
- residual contribution judgment;
- paper-unit scope control;
- decision-value experiment planning;
- top reviewer-risk checks;
- persistent state artifacts.

## Install

### Option A: Repo-scoped install

Unzip this package into the root of the GitHub repository where you want Codex to use the skills:

```bash
unzip AI_Research_Codex_Skills_v1.zip -d /path/to/your/repo
cd /path/to/your/repo
codex
```

The important path is:

```text
.agents/skills/<skill-name>/SKILL.md
```

Codex reads repository skills from `.agents/skills` under the current directory or its parent directories up to the repository root.

### Option B: User-global install

Unzip this package into your home directory:

```bash
unzip AI_Research_Codex_Skills_v1.zip -d ~
```

This creates:

```text
~/.agents/skills/
```

These skills will be available from any repository.

## Quick start

From Codex, invoke the orchestrator explicitly:

```text
$ai-research-orchestrator

我要在 LLM agents / multi-agent reasoning 方向找一个可投 ICLR 或 COLM 的论文 idea。
请先创建 research_state 目录，然后从 literature bootstrap 开始。
```

Or, if you already have a concrete idea:

```text
$ai-research-orchestrator

我有一个 idea：multi-agent reasoning 的收益可能主要来自 token budget 而不是真正 collaboration。
请把它转成 candidate claims，并做 claim-prior-work triangulation。
```

## Initialize project state

The workflow relies on persistent state documents instead of long chat context.

Run:

```bash
python .agents/skills/research-state-artifact-management/scripts/init_research_state.py \
  --project-name "Multi-Agent Reasoning Evaluation"
```

This creates:

```text
research_state/
  00_state/
  01_literature/
  02_signals/
  03_claims/
  04_prior_work/
  05_scope/
  06_experiments/
  07_reviewer/
  08_paper_shape/
  99_archive/
```

The two source-of-truth files are:

```text
research_state/00_state/current_state.md
research_state/00_state/decision_log.md
```

## How the skills chain together

Codex skills are not normal function calls. A skill does not automatically call another skill as code.

The chaining works through:

1. `$ai-research-orchestrator` deciding the next stage;
2. explicit `$skill-name` invocation when useful;
3. state files under `research_state/`;
4. each skill's exit condition.

Default order:

```text
entry-source-intake
→ representative-literature-bootstrap
→ research-signal-mining
→ candidate-claim-set
→ research-move-router
→ claim-prior-work-triangulation
→ paper-unit-scope-gate
→ decision-value-experiment-planner
→ reviewer-risk-check
→ paper-shape-generator
```

Infrastructure:

```text
research-state-artifact-management
```

Specialist lens:

```text
research-target-reframing
```

## Available skills

| Skill | Use when |
|---|---|
| `$ai-research-orchestrator` | Entry point; routes through the pipeline and maintains state. |
| `$entry-source-intake` | Identify entry state, sources, target area, and resource constraints. |
| `$representative-literature-bootstrap` | Build a working field map from representative papers. |
| `$research-signal-mining` | Extract abnormal phenomena, tensions, evaluation artifacts, and failure modes. |
| `$candidate-claim-set` | Convert signals or vague ideas into 2–4 falsifiable candidate claims. |
| `$research-move-router` | Classify claims as method, evaluation, mechanism, negative result, scaling, system, theory, dataset, or taxonomy. |
| `$claim-prior-work-triangulation` | Collide claims with prior work and extract residual contribution. |
| `$paper-unit-scope-gate` | Decide whether residual contribution is too thin, too broad, or paper-shaped. |
| `$decision-value-experiment-planner` | Plan experiments by hypothesis and decision value, not table-filling. |
| `$reviewer-risk-check` | Identify top fatal reviewer risks late in the process. |
| `$paper-shape-generator` | Produce thesis, contribution bullets, evidence plan, risks, and execution plan. |
| `$research-state-artifact-management` | Create and maintain `research_state/` artifacts. |
| `$research-target-reframing` | Specialist lens for target/formulation/supervision reframing and accidental complexity. |

## Example workflows

### 1. Start from a broad direction

```text
$ai-research-orchestrator

方向：LLM agents / multi-agent reasoning。
目标：找一个可投 ICLR/COLM 的 idea。
资源：API-only 或小模型实验。
请先做 entry intake，并说明 literature bootstrap 需要哪些代表性论文类型。
```

Expected result:

- creates or requests `research_state/`;
- records constraints;
- routes to `$representative-literature-bootstrap`.

### 2. Start from a paper list

```text
$representative-literature-bootstrap

请阅读 research_state/01_literature/paper_index.md 中的论文，优先看 introduction、related work、problem formulation、experiment setup、limitations。
输出 field_map.md 和至少 3 个 research signals。
```

### 3. Start from a vague idea

```text
$candidate-claim-set

Idea: RAG 的主要失败可能不是 retrieval miss，而是 retrieved evidence conflict。
请生成 2–4 个 candidate claims，并写出 falsifiable prediction 和 possible disproof。
```

### 4. Check whether an idea survives prior work

```text
$claim-prior-work-triangulation

Active claim: C002。
请根据 literature/field_map.md 和 paper_index.md，分析它和最近工作的 overlap，提取 residual contribution。
```

### 5. Plan early experiments without table-filling

```text
$decision-value-experiment-planner

Claim C002 已通过初步 scope gate。
请设计最小但有效的 kill-test。
注意：最小实验不能用失真的 cheap proxy，例如该完整训练的任务只跑 10 epoch，或用过弱 baseline。
```

## Design principles

1. No clear claim, no novelty check.
2. No prior-work collision, no final paper-worthiness judgment.
3. Evaluate residual contribution, not raw idea.
4. Do not expand scope to compensate for a weak core claim.
5. Experiments must have decision value.
6. Minimal experiments must preserve the problem essence; invalid cheap proxies are not acceptable.
7. Every decision-relevant milestone must checkpoint to `research_state/`.
8. Novelty can be partially verified; do not claim novelty from memory.

## Notes for GitHub use

Commit the `.agents/skills/` directory with this README. Teammates using Codex from the repository root or a subdirectory should be able to mention the skills with `$skill-name`.

Optional: copy `AGENTS.example.md` to `AGENTS.md` if you want Codex to default to this research workflow in the repository.

## References

- Codex Agent Skills: https://developers.openai.com/codex/skills
- Codex AGENTS.md guidance: https://developers.openai.com/codex/guides/agents-md
