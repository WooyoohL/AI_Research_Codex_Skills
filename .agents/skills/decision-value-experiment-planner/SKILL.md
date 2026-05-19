---
name: decision-value-experiment-planner
description: Use to design AI/ML experiments that answer explicit hypotheses and support research decisions, avoiding low-information-gain exhaustive experiments and invalid cheap proxies.
---

# 07. Decision-Value Experiment Planner

## Purpose

设计有决策价值的实验。实验不是为了填表、补齐口径或让 ablation 看起来完整，而是为了回答明确假设或支持决策。

## Experiment modes

先判断当前模式：

```text
Exploration mode:
  实验用于判断 claim 是否值得继续。

Evidence mode:
  实验用于支撑 residual claim。

Reviewer-defense mode:
  实验用于回应合理 reviewer 质疑或补投稿完整性。
```

Decision-value 原则在三种模式都成立，但“决策价值”的定义不同。

## Required fields for every experiment

```text
Experiment ID:
Hypothesis:
Decision this experiment informs:
Minimum valid setup:
Invalid cheap proxy to avoid:
Expected outcomes:
Decision for each outcome:
Stop condition:
```

## Valid minimal experiment

初期探索应使用少量但有效的 decisive experiments。可以缩小范围，但不能改变问题本质。

合格做法：

- 选择代表性任务，而不是十个任务；
- 只比较关键 baseline，而不是完整表格；
- 在小规模但机制不失真的 setting 下完整训练到合理收敛；
- 保留 claim 所依赖的关键变量；
- 控制最重要 confound；
- 结果足以决定 continue / pivot / kill。

不合格 cheap proxy：

- 本来需要 40 epoch 收敛，只跑 10 epoch；
- 用 MLP / simple attention 替代真正要测试的复杂模块；
- 用 toy setting 替代 claim 所依赖的真实 setting；
- 用弱 baseline 证明自己有效；
- 用小到失真的 dataset 支撑 scaling claim。

## Evidence categories

```text
Necessary evidence:
  没有它，claim 站不住。

Supporting evidence:
  增强说服力，但不是必须。

Cuttable evidence:
  看似完整，但信息增益低，会膨胀论文。

Future work:
  有价值，但不属于当前 paper unit。
```

## Stop low-information-gain experiments

如果一组实验预计不会改变以下任何决策，就不做：

1. 是否继续这个方向；
2. 是否修改 main claim；
3. 是否改变 paper type；
4. 是否补强 reviewer defense；
5. 是否指导后续方法改进。

尤其当实验只是重复确认“不可行 / 无效果”，且不会改变决策时，应停止。

## User explicitly asks for full comparison

如果用户明确要求补满对比实验，原则不阻止执行，但要标记实验模式为 reviewer-defense / completeness mode。

仍需问：

```text
这个对比是否是合理 reviewer 会要求的？
它是否覆盖真实 competing method？
它是否会改变 paper 可信度？
```

## Output

写入：

```text
06_experiments/decision_value_plan_Cxxx.md
06_experiments/experiment_log.md
```

## Exit condition

可以进入 reviewer risk check 或 execution，当：

- 每个核心实验有 hypothesis、decision、minimum valid setup、stop condition；
- necessary / supporting / cuttable evidence 已区分；
- 没有低信息增益穷举；
- 没有用失真的 cheap proxy 作为最小实验。

## Pipeline integration

When used inside the modular pipeline, finish by updating or creating the relevant research-state artifacts. Do not rely on chat context as the only source of truth.

State artifacts to update:

- `research_state/06_experiments/decision_value_plan_Cxxx.md`
- `research_state/06_experiments/experiment_log.md`

Recommended next step:

- Continue with `reviewer-risk-check`, unless the exit condition is not met.

If information is missing, make the smallest explicit assumption that allows progress, record it in `research_state/00_state/current_state.md`, and mark the status as provisional.
