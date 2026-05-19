---
name: research-state-artifact-management
description: Use throughout the research pipeline to checkpoint progress into documents, manage project directories, preserve decisions, and prevent context drift caused by long conversations.
---

# 10. Research State & Artifact Management

## Purpose

Chat context 是临时工作区，文档才是长期记忆。每完成一个会影响后续判断的研究决策单元，就要 checkpoint 到文档。

## What counts as a decision unit

一个决策单元通常包含：

```text
输入 → 分析 → 判断 → 下一步变化
```

不是每个小想法都要建文档；只有 decision-relevant milestone 才 checkpoint。

## Core files

最重要的两个 source of truth：

```text
00_state/current_state.md
00_state/decision_log.md
```

`current_state.md` 回答：现在在哪里？

`decision_log.md` 回答：为什么走到这里？

## Recommended directory structure

```text
project_name/
  README.md
  00_state/
    project_brief.md
    current_state.md
    decision_log.md
    open_questions.md
  01_literature/
    paper_index.md
    field_map.md
    method_family_map.md
    evaluation_map.md
    reading_notes/
  02_signals/
02_problems/
    signal_bank.md
  03_claims/
    candidate_claims.md
    claim_ledger.md
    research_move_routing.md
    claim_versions/
  04_prior_work/
    collision_maps/
    residual_contributions/
  05_scope/
    paper_unit_gate_Cxxx.md
  06_experiments/
    decision_value_plan_Cxxx.md
    experiment_log.md
    results/
  07_reviewer/
    reviewer_risk_Cxxx.md
  08_paper_shape/
    paper_pitch_Cxxx.md
    execution_plan.md
  99_archive/
    abandoned_claims.md
    superseded_notes/
```

## ID system

```text
P001 = paper
S001 = signal
C001 = claim
D001 = decision
E001 = experiment
R001 = reviewer risk
```

这样可以追踪：

```text
Papers → Signals → Claims → Experiments → Decisions → Paper Shape
```

## Checkpoint triggers

- Entry intake 完成 → 更新 `project_brief.md` 和 `current_state.md`。
- 每个 literature batch 完成 → 更新 `paper_index.md` 和 `field_map.md`。
- Signal mining 完成 → 更新 `signal_bank.md`。
- Candidate claims 生成 → 更新 `claim_ledger.md`。
- Prior-work collision 完成 → 更新 collision map 和 residual contribution。
- Scope gate 完成 → 更新 paper unit gate。
- 实验计划完成 → 更新 decision-value plan。
- 实验结果改变判断 → 更新 experiment log、claim ledger、decision log、current state。
- Reviewer check 完成 → 更新 reviewer risk。
- Paper shape 完成 → 更新 paper pitch 和 execution plan。

## Avoid documentation overhead

- 小更新写入 log，不新建文件。
- `current_state.md` 只放摘要和链接，不写长文。
- 旧 claim 必须在 claim ledger 中标记 active / parked / rejected / merged / superseded。
- 没有 decision impact 的实验不进入核心记录。

## Exit condition

每次重新开始工作前，必须能通过 `current_state.md` 快速恢复：

```text
Current active claim:
Current paper shape:
Current residual contribution:
Literature coverage:
Key prior works:
Evidence status:
Top risks:
Next decision:
Next action:
```

## Pipeline integration

When used inside the modular pipeline, finish by updating or creating the relevant research-state artifacts. Do not rely on chat context as the only source of truth.

State artifacts to update:

- `research_state/00_state/current_state.md`
- `research_state/00_state/decision_log.md`

Recommended next step:

- Continue with the orchestrator (`ai-research-orchestrator`) chooses the next stage, unless the exit condition is not met.

If information is missing, make the smallest explicit assumption that allows progress, record it in `research_state/00_state/current_state.md`, and mark the status as provisional.


## Problem formulation checkpoint

After `$problem-formulation`, update:

```text
research_state/02_problems/problem_formulations.md
research_state/00_state/current_state.md
```

`current_state.md` should include the active problem before the active claim.
