---
name: representative-literature-bootstrap
description: Use before deep idea generation to build a working map of a target AI/ML field by reading representative papers, especially introductions, related work, formulations, experiments, limitations, and reviews.
---

# 01. Representative Literature Bootstrapping

## Purpose

在生成或评估新 idea 之前，先建立领域地图。目标不是读完整个领域，而是形成一个足以支持 idea discovery 的 working map。

## Why this comes early

没有领域地图，后面的 signal mining、claim generation、prior-work triangulation 都会悬空。最常见错误是：

- 把已知问题当新问题；
- 把作者 introduction 的叙事当事实；
- 不知道领域默认假设；
- 不知道最危险的 closest work；
- 无法判断 residual contribution。

## Reading batches

推荐第一批覆盖：

```text
3–5 篇 anchor papers
5–10 篇 recent representative papers
2–5 篇 critical / analysis / negative / benchmark papers
1–2 篇 survey / tutorial，如果存在
```

如果用户已经是该方向专家，可以压缩为：

```text
3–5 篇 closest papers
用户认为最危险的 prior work
已有失败实验或观察
```

## What to read in each paper

优先读：

1. Abstract：作者声称贡献是什么。
2. Introduction：作者如何定义问题和 gap。
3. Related Work：作者如何划分领域和区别前人。
4. Problem Formulation / Method Overview：真正技术动作是什么。
5. Experiment Setup：claim 如何被验证。
6. Limitations：作者承认哪里没解决。
7. Reviews / OpenReview comments，如果有：外部认为哪里弱。

## Output: field map, not summary

不要输出普通 paper summary。输出：

```text
Main problem formulations:
Method families:
Evaluation protocols:
Common claims:
Repeated limitations:
Unstable assumptions:
Closest work clusters:
Potential research tensions:
Literature coverage status:
```

## Exit condition

可以进入 signal mining，当已经有：

- `field_map.md` 初稿；
- 主要 method families；
- 主要 evaluation protocols；
- 5–10 个 closest work candidates；
- 至少 3 个 potential research signals；
- literature coverage status。

## Stopping rule

不要无限读论文。第一批读完后必须产出 field map 和 signal bank。后续再根据 claim 精确补文献。

## Failure modes

- 读太多，永远不开始。
- 只相信 introduction / related work。
- 只读最新 SOTA，不读 anchor / critical papers。
- 只读单一方法族。
- 把 survey 当成真理，而不是地图。

## Pipeline integration

When used inside the modular pipeline, finish by updating or creating the relevant research-state artifacts. Do not rely on chat context as the only source of truth.

State artifacts to update:

- `research_state/01_literature/paper_index.md`
- `research_state/01_literature/field_map.md`

Recommended next step:

- Continue with `research-signal-mining`, unless the exit condition is not met.

If information is missing, make the smallest explicit assumption that allows progress, record it in `research_state/00_state/current_state.md`, and mark the status as provisional.
