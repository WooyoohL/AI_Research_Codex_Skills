---
name: research-move-router
description: Use to provisionally classify each candidate claim into the most plausible paper contribution type without forcing target reframing everywhere.
---

# 04. Research Move Router

## Purpose

判断 candidate claim 最像哪类 research move。这个判断是 provisional，prior work collision 之后可能改变。

## Available research moves

1. Target reframing：当前 formulation / target / supervision signal 可能不自然。
2. Evaluation / benchmark reframing：现有评测没有测到真正能力。
3. Mechanism / explanation：方法有效但原因不清楚。
4. Negative result / assumption stress-test：社区假设可能不成立。
5. Scaling / regime shift：规模、上下文、模型族或部署条件改变规律。
6. System / efficiency：瓶颈是 latency、memory、throughput、serving cost 等。
7. Theory / formalization：需要定理、bound、impossibility、identifiability 或 formal problem definition。
8. Dataset / data-centric：关键瓶颈是数据覆盖、标注、分布或监督信号。
9. Empirical taxonomy / synthesis：领域结果混乱，需要解释性 taxonomy。

## Routing output

```text
Claim ID:
Provisional research move:
Why this move fits:
Alternative moves:
What would change this classification:
Most relevant specialist lens:
```

## Revision rule

每次 claim 大幅修改，或 prior work 证明原贡献类型已被覆盖，都必须重新 routing。

## Exit condition

可以进入 claim–prior work triangulation，当：

- 每个 active claim 有 provisional research move；
- 已标记可能 pivot 的 alternative move；
- 没有把 target reframing 强行套到不适合的 claim 上。

## Failure modes

- 把 research move 当最终论文类型。
- 把所有好 idea 都解释成 target reframing。
- 忽略 negative result / evaluation / mechanism 这些非 method paper 形态。
- prior work 变化后没有重新 routing。

## Pipeline integration

When used inside the modular pipeline, finish by updating or creating the relevant research-state artifacts. Do not rely on chat context as the only source of truth.

State artifacts to update:

- `research_state/03_claims/research_move_routing.md`
- `research_state/00_state/current_state.md`

Recommended next step:

- Continue with `claim-prior-work-triangulation`, unless the exit condition is not met.

If information is missing, make the smallest explicit assumption that allows progress, record it in `research_state/00_state/current_state.md`, and mark the status as provisional.
