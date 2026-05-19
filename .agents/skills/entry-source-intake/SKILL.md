---
name: entry-source-intake
description: Use at the beginning of an AI/ML research-idea session to identify the user's entry state, available materials, target area, and resource constraints before invoking deeper modules.
---

# 00. Entry & Source Intake

## Purpose

判断用户当前从哪个状态进入研究流程，并收集最小必要上下文。不要一开始就让用户填写完整表单。

## Trigger

当用户想找 AI/ML research idea、评估 idea、整理论文方向、分析失败实验、准备 proposal 或投稿前检查时调用。

## Minimal questions

最多先问两个问题：

```text
1. 你现在是只有大方向，还是已经有具体 idea / 实验结果 / paper list？
2. 你的资源约束大概是什么：API-only、小模型实验、可以微调，还是可以训练较大模型？
```

如果用户已经提供足够信息，不要追问，直接进入相应模块。

## Entry states and routing

| 用户状态 | 进入模块 | 处理方式 |
|---|---|---|
| 只有大方向 | literature-bootstrap → signal-mining | 先建 field map，不直接生成方法 |
| 有一批论文 | literature-bootstrap | 先提取 field map / tensions / closest work |
| 有 vague idea | candidate-claim-set | 转成 2–4 个 candidate claims |
| 有具体 method idea | candidate-claim-set → prior-work-triangulation | 防止方法已被做过 |
| 有实验结果 / 失败实验 | decision-value-experiment-planner → claim-set | 解释结果，可能转 analysis / negative result |
| 准备投稿 | reviewer-risk-check → paper-shape-generator | 检查 top fatal risks 和证据链 |

## Output

```text
Research area:
Entry state:
Available sources:
Resource constraints:
Immediate next module:
Assumptions:
```

## Exit condition

可以进入下一步，当以下信息基本明确：

- 研究领域或方向；
- 用户已有材料类型；
- 当前任务是找 idea、评估 idea、实验规划还是投稿前检查；
- 粗略资源约束；
- 是否需要先做 literature bootstrap。

## Failure modes

- 不要把所有请求都当成“从零找 idea”。
- 不要在没有必要时问完整表单。
- 不要忽略资源约束，否则后面会设计不可执行的 paper。

## Pipeline integration

When used inside the modular pipeline, finish by updating or creating the relevant research-state artifacts. Do not rely on chat context as the only source of truth.

State artifacts to update:

- `research_state/00_state/project_brief.md`
- `research_state/00_state/current_state.md`

Recommended next step:

- Continue with `representative-literature-bootstrap`, unless the exit condition is not met.

If information is missing, make the smallest explicit assumption that allows progress, record it in `research_state/00_state/current_state.md`, and mark the status as provisional.
