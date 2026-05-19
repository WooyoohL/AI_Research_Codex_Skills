---
name: claim-prior-work-triangulation
description: Use to collide a candidate claim with nearest prior work and extract the residual contribution that remains after accounting for existing papers.
---

# 05. Claim–Prior Work Triangulation

## Purpose

判断一个 claim 和前人工作碰撞后，还剩下什么 residual contribution。这里不直接判断“是否足够顶会”。

## Core principle

不要问：

```text
有没有人做过这个 idea？
```

要问：

```text
当前 claim 中哪些部分已被 prior work 覆盖？扣除后真正剩下什么？
```

## Process

对每个 active claim：

```text
1. Restate the preliminary claim.
2. Identify prior-work search targets: method / benchmark / dataset / theory / analysis / system / negative result.
3. Build collision map with closest works.
4. Mark overlap and uncovered parts.
5. Extract residual contribution.
6. Decide whether contribution type should pivot.
7. Assign novelty coverage status.
```

## Collision map format

```text
Claim ID:
Closest work:
What it already does:
Which part of our claim it covers:
What remains uncovered:
Difference type: conceptual / empirical / setting / scale / terminology / implementation
Incrementality risk:
```

## Novelty status labels

```text
unverified
user-provided papers only
partially verified
likely novel within checked scope
heavily overlapped
already done
```

不要说“没人做过”，除非系统性检索后仍要谨慎表述。

## Possible outcomes

| 情况 | 处理 |
|---|---|
| 核心 claim 已被做过 | pivot 或 abandon |
| 方法已有，但机制没人解释 | 转 mechanism / analysis paper |
| 方法已有，但 evaluation 有缺陷 | 转 evaluation / negative result |
| 旧工作只在小规模做过 | 判断是否存在真实 regime shift |
| 没人做过但太薄 | 不能仅凭 novel 说 paper-worthy |
| A/B 都有人做过，但 interaction 未被研究 | 判断 interaction 是否产生新知识 |

## Output

写入：

```text
04_prior_work/collision_maps/collision_map_Cxxx.md
04_prior_work/residual_contributions/residual_contribution_Cxxx.md
```

## Exit condition

可以进入 paper-unit scope gate，当：

- active claim 有 collision map；
- 有明确 residual contribution；
- 有 novelty coverage status；
- 如果 contribution type 需要 pivot，已记录。

## Failure modes

- 凭 AI 记忆判断 novelty。
- 只查 method papers，忽略 evaluation / benchmark / analysis papers。
- 把术语差异当 novelty。
- 在 prior work 未查清前说 idea 足以撑顶会。

## Pipeline integration

When used inside the modular pipeline, finish by updating or creating the relevant research-state artifacts. Do not rely on chat context as the only source of truth.

State artifacts to update:

- `research_state/04_prior_work/collision_maps/`
- `research_state/04_prior_work/residual_contributions/`

Recommended next step:

- Continue with `paper-unit-scope-gate`, unless the exit condition is not met.

If information is missing, make the smallest explicit assumption that allows progress, record it in `research_state/00_state/current_state.md`, and mark the status as provisional.
