---
name: research-signal-mining
description: Use to extract idea seeds from a field map, papers, failed experiments, reviewer comments, benchmark artifacts, or unexplained empirical phenomena.
---

# 02. Research Signal Mining

## Purpose

从领域地图和材料中提取 research signals。这个阶段不直接生成方法，而是寻找“不对劲的现象”。

## Signal types

优先寻找：

- abnormal phenomenon：和直觉不一致的现象；
- literature tension：不同论文结论冲突；
- evaluation artifact：benchmark 分数高但真实能力不匹配；
- scaling regime shift：规模、上下文、模型族变化后旧结论失效；
- complicated method smell：方法依赖大量 trick 才能工作；
- failed experiment：失败本身揭示了机制或错误假设；
- repeated reviewer complaint：OpenReview 中反复出现的质疑；
- suspicious baseline：简单 baseline 异常强。

## Process

对每个候选 signal，回答：

```text
What is the observed signal?
Why is it surprising or uncomfortable?
Where does it come from?  Paper / experiment / review / benchmark / implementation.
Which assumption does it challenge?
What research moves could it support?
What evidence would make it real rather than anecdotal?
```



## Signal vs Problem

A signal is a clue. It is not yet the research problem.

Example:

```text
Signal:
Multi-agent papers often do not control token budget.

Problem:
The community cannot tell whether reported multi-agent gains come from genuine collaboration or from increased sampling/token budget.
```

Do not jump directly from signal to method or final claim. After signal mining, use `$problem-formulation` before `$candidate-claim-set`.

## Output

写入 `02_signals/signal_bank.md`：

```text
Signal ID:
Source:
Observed phenomenon:
Why it is abnormal:
Potential research moves:
Initial strength:
Uncertainty:
Next check:
```

## Exit condition

可以进入 problem formulation，当：

- 至少有 3 个 signals，或用户明确指定一个 signal；
- 每个 active signal 有来源和异常点；
- 每个 active signal 有 1–3 个可能 research move。

## Failure modes

- 把普通 improvement wish 当 signal。
- 直接从 signal 跳到 method。
- 只记录“有趣”，不记录为什么 abnormal。
- 没有 source，导致后续无法验证。

## Pipeline integration

When used inside the modular pipeline, finish by updating or creating the relevant research-state artifacts. Do not rely on chat context as the only source of truth.

State artifacts to update:

- `research_state/02_signals/signal_bank.md`

Recommended next step:

- Continue with `problem-formulation`, unless the exit condition is not met.

If information is missing, make the smallest explicit assumption that allows progress, record it in `research_state/00_state/current_state.md`, and mark the status as provisional.
