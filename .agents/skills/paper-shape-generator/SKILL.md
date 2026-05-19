---
name: paper-shape-generator
description: Use at the end of the pipeline to turn a residual claim, scoped contribution, evidence plan, and reviewer risks into a coherent paper pitch and execution plan.
---

# 09. Paper Shape & Execution Plan

## Purpose

将前面收敛出的 residual claim 转化为 paper shape 和短期执行计划。

不要基于 raw idea 写 pitch；必须基于 residual contribution。

## Output

```text
Paper shape:
  method / analysis / evaluation / negative result / benchmark / system / theory / dataset / taxonomy

Title candidates:

One-sentence thesis:

Main claim:

Contribution bullets:
  1.
  2.
  3.

Necessary evidence:

Cuttable parts:

Top risks:

Current novelty coverage:

Next 1–2 week execution plan:
```

## Execution plan quality

坏计划：

```text
继续调研相关工作。
继续跑实验。
完善方法。
```

好计划：

```text
先查是否已有 work 控制 token budget 比较 multi-agent debate vs self-consistency；
如果已有，转向 task-regime analysis；
如果没有，跑两个代表任务上的 fixed-budget pilot。
```

## Exit condition

paper pitch 完成，当：

- 主 claim 一句话清楚；
- contribution bullets 不超过 3 个；
- 必要证据和 cuttable parts 明确；
- top risks 已知；
- 下一步动作具体到阅读 / 实验 / 写作任务。

## Failure modes

- 用漂亮标题掩盖 claim 不清楚。
- pitch 中加入未经 prior work 检查的 novelty claim。
- 把 cuttable / future work 又塞回 contribution bullets。
- execution plan 太泛，不可执行。

## Pipeline integration

When used inside the modular pipeline, finish by updating or creating the relevant research-state artifacts. Do not rely on chat context as the only source of truth.

State artifacts to update:

- `research_state/08_paper_shape/paper_pitch_Cxxx.md`
- `research_state/08_paper_shape/execution_plan.md`

Recommended next step:

- Continue with the orchestrator (`ai-research-orchestrator`) chooses the next stage, unless the exit condition is not met.

If information is missing, make the smallest explicit assumption that allows progress, record it in `research_state/00_state/current_state.md`, and mark the status as provisional.
