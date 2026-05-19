---
name: candidate-claim-set
description: Use to convert research signals or vague ideas into 2–4 falsifiable candidate claims without prematurely committing to one paper shape.
---

# 03. Candidate Claim Set

## Purpose

将 signal 或 vague idea 转成少量可证伪 candidate claims。不要一开始只锁定一个 claim。

## Why multiple claims

一个 signal 可能发展成多种论文：method、evaluation、mechanism、negative result、scaling analysis、benchmark、theory 等。过早选择一个 claim 会错过更好的 paper shape。

## Process

对每个 active signal，生成 2–4 个 candidate claims。不要超过 4 个。

每个 claim 必须包含：

```text
Claim ID:
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

- 每个 active signal 有 2–4 个 candidate claims；
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
