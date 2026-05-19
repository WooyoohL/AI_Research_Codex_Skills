---
name: paper-unit-scope-gate
description: Use after prior-work triangulation to judge whether the residual contribution is too thin, too broad, or well-scoped enough to form one coherent AI/ML paper.
---

# 06. Paper-Unit Scope Gate

## Purpose

Judge the residual contribution against the stated problem, not only against the claim. A paper can have a clear residual claim but still be weak if the underlying problem is unimportant or poorly framed.


只评估 residual contribution 是否构成一篇 scope 合适的论文。不要评估 raw idea。

## Input

```text
Residual main claim:
Novelty coverage status:
Candidate contribution type:
Known overlap with prior work:
Resource constraints:
```

## Paper-unit test

```text
如果这篇论文只能保留一个 main claim、三个 contribution bullets、三组核心实验/分析，它还成立吗？
```

## Judgments

### Too thin

表现：

- 小 setting change；
- minor engineering tweak；
- missing ablation；
- benchmark variant；
- obvious extension。

处理：寻找 mechanism、evaluation protocol、regime boundary、stronger failure taxonomy 或降级。

### Too broad

表现：

- 为弥补 novelty 弱，同时加入 method + dataset + benchmark + theory + system；
- 多个 independent claims；
- 每个 claim 都证明不足。

处理：保留一个主 claim，其余 cut / future work / split。

### Well-scoped

标准：

- 一个主 claim；
- 2–3 个 contribution bullets；
- 必要但不冗余的证据链；
- 明确 prior work boundary；
- 明确 limitations。

## Output

Required input context:

```text
Problem statement:
Why the problem matters:
Residual main claim:
Prior-work overlap:
```


```text
Residual main claim:
Scope verdict: not enough / workshop-scale / promising if strengthened / well-scoped / too broad / split / abandon
Minimum publishable unit:
Required strengthening:
What to cut:
What to defer:
```

## Exit condition

可以进入 experiment planner，当：

- scope verdict 明确；
- minimum publishable unit 明确；
- cut / defer 的部分已记录；
- 没有用增加 scope 来掩盖 core claim 弱。

## Failure modes

- 把 elegant idea 当 paper-worthy。
- 用堆工作量补 novelty 不足。
- 试图把三篇论文塞进一篇。
- 因为 novelty 弱而无限加实验、加模块、加数据集。

## Pipeline integration

When used inside the modular pipeline, finish by updating or creating the relevant research-state artifacts. Do not rely on chat context as the only source of truth.

State artifacts to update:

- `research_state/05_scope/paper_unit_gate_Cxxx.md`

Recommended next step:

- Continue with `decision-value-experiment-planner`, unless the exit condition is not met.

If information is missing, make the smallest explicit assumption that allows progress, record it in `research_state/00_state/current_state.md`, and mark the status as provisional.


## Problem-solution fit check

Ask:

- Does the residual claim actually solve, explain, measure, or refute the stated problem?
- If the claim is true, does it change how the problem should be studied or solved?
- Is the problem important enough to justify a paper?
- What adjacent problems are explicitly out of scope?

Add `problem is not important enough even if the claim is true` as a too-thin risk.

Paper-unit test:

```text
If this paper could keep only one problem, one main claim, three contribution bullets, and three core experiments/analyses, would it still stand?
```
