---
name: candidate-claim-set
description: Use after problem-formulation to convert clearly defined research problems into 2–4 falsifiable candidate claims without prematurely committing to one paper shape.
---

# 03. Candidate Claim Set

## Purpose

If the input is only a signal, vague method, or broad direction, first use `$problem-formulation`. Candidate claims must be grounded in a clear problem statement.


将已经定义清楚的 research problem 转成少量可证伪 candidate claims。不要一开始只锁定一个 claim。

## Why multiple claims

一个 signal 可能发展成多种论文：method、evaluation、mechanism、negative result、scaling analysis、benchmark、theory 等。过早选择一个 claim 会错过更好的 paper shape。

## Process

对每个 active problem，生成 2–4 个 candidate claims。不要超过 4 个。

每个 claim 必须包含：

```text
Claim ID:
Source problem:
Problem statement:
Main claim:
Scope:
Falsifiable prediction:
Possible disproof:
Provisional research move:
Fast uncertainty:
Current status: active / parked / rejected / merged / superseded
```

## Claim quality rules

坏 claim：

```text
We make RAG more reliable.
We propose a better agent framework.
We improve robustness.
```

好 claim：

```text
Current RAG failures under conflicting evidence are caused less by retrieval miss than by evidence aggregation failure; LLMs systematically over-trust lexical overlap when high-confidence passages conflict.
```

## Output

写入：

```text
03_claims/candidate_claims.md
03_claims/claim_ledger.md
```

## Exit condition

可以进入 research move router，当：

- 每个 active problem 有 2–4 个 candidate claims；
- 每个 claim 有 falsifiable prediction 和 possible disproof；
- claim 状态已记录在 claim ledger。

## Failure modes

- 生成 10+ 个 claim，导致 pipeline 爆炸。
- 只生成 method claim，忽略 evaluation / negative / mechanism 形态。
- claim 太泛，导致无法查 prior work。
- claim 没有 disproof，变成不可证伪叙事。

## Pipeline integration

When used inside the modular pipeline, finish by updating or creating the relevant research-state artifacts. Do not rely on chat context as the only source of truth.

State artifacts to update:

- `research_state/03_claims/candidate_claims.md`
- `research_state/03_claims/claim_ledger.md`

Recommended next step:

- Continue with `research-move-router`, unless the exit condition is not met.

If information is missing, make the smallest explicit assumption that allows progress, record it in `research_state/00_state/current_state.md`, and mark the status as provisional.


## Additional failure mode

- Claim has no clear source problem and is only packaging a method, module, or metric improvement.

## State updates

Update `research_state/03_claims/candidate_claims.md` and `research_state/03_claims/claim_ledger.md`. Link every claim to a Problem ID from `research_state/02_problems/problem_formulations.md`.
