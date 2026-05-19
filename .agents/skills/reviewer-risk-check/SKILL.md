---
name: reviewer-risk-check
description: Use late in the research pipeline to identify the top fatal reviewer risks for a residual claim and evidence plan, without overfitting to imagined reviewers.
---

# 08. Reviewer Risk Check

## Purpose

在 claim、prior work、scope、evidence plan 基本明确后，检查最可能导致拒稿的 top fatal risks。

不要在早期 idea 发散阶段使用 full reviewer simulation，否则会过早杀死 creativity。

## Reviewer modes

检查：

- Novelty reviewer：这不就是 X + Y 吗？
- Significance reviewer：社区为什么在乎？
- Soundness reviewer：实验 / 理论是否支持 claim？
- Baseline reviewer：是否漏掉强 baseline？
- Scope reviewer：是否过度 claim 或失焦？
- Reproducibility reviewer：别人能否验证？

## Output format

只输出 top 3 fatal risks：

```text
Risk ID:
Risk type:
Severity:
Likely reviewer wording:
Required defense:
Address by experiment / writing / limitation / scope change:
```

## Important distinction

Reviewer risk check 是 risk diagnosis，不是 acceptance prediction。

## Exit condition

可以进入 paper shape generator，当：

- top fatal risks 已记录；
- 每个 risk 的处理方式明确：补证据、改写 claim、承认 limitation、或不处理；
- 没有因为防御所有 imagined reviewer 而无限扩展实验。

## Failure modes

- 过度保守，杀掉有风险但有价值的 idea。
- 为防御所有风险而无限加实验。
- 把 reviewer simulation 当成接收概率预测。
- reviewer 建议和 decision-value planner 冲突时，默认加实验。

## Pipeline integration

When used inside the modular pipeline, finish by updating or creating the relevant research-state artifacts. Do not rely on chat context as the only source of truth.

State artifacts to update:

- `research_state/07_reviewer/reviewer_risk_Cxxx.md`

Recommended next step:

- Continue with `paper-shape-generator`, unless the exit condition is not met.

If information is missing, make the smallest explicit assumption that allows progress, record it in `research_state/00_state/current_state.md`, and mark the status as provisional.
