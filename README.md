# AI Research Codex Skills

一个用于 AI/ML 研究 idea 发现、筛选和论文 proposal 成形的模块化 Codex skill pipeline。

它不是自动生成“顶会 idea”的机器，而是帮助研究者把一个模糊方向、文献观察、失败实验或初步想法，逐步推进成：

- 代表性文献地图；
- research signals；
- 明确 research problems；
- candidate claims；
- prior-work collision analysis；
- residual contributions；
- paper-unit scope 判断；
- decision-value experiment plan；
- reviewer-risk check；
- paper pitch 和执行计划。

---

## 仓库结构

本仓库使用 Codex 原生 skill 目录结构：

```text
.agents/skills/<skill-name>/SKILL.md
```

主要入口：

```text
$ai-research-orchestrator
```

除非你明确知道要调用哪个子 skill，否则建议先从 orchestrator 开始。

---

## 安装方式

### 方式 A：直接使用本仓库

```bash
git clone https://github.com/WooyoohL/AI_Research_Codex_Skills.git
cd AI_Research_Codex_Skills
codex
```

然后调用：

```text
$ai-research-orchestrator

我要在 LLM agents / multi-agent reasoning 方向找一个可投 ICLR 或 COLM 的论文 idea。
请先创建 research_state 目录，然后从 literature bootstrap 开始。
```

### 方式 B：复制到另一个项目

```bash
mkdir -p /path/to/your/project/.agents
cp -r .agents/skills /path/to/your/project/.agents/
cd /path/to/your/project
codex
```

### 方式 C：全局安装

```bash
mkdir -p ~/.agents
cp -r .agents/skills ~/.agents/
```

---

## 核心流程

推荐流程：

```text
00. Entry & Source Intake
01. Representative Literature Bootstrapping
02. Research Signal Mining
03. Problem Formulation
04. Candidate Claim Set
05. Research Move Router
06. Claim–Prior Work Triangulation
07. Paper-Unit Scope Gate
08. Decision-Value Experiment Planner
09. Reviewer Risk Check
10. Paper Shape & Execution Plan
X.  Research State & Artifact Management
```

关键依赖是：

```text
signal → problem → claim → prior work → residual contribution → paper unit → experiments
```

---

## 为什么新增 Problem Formulation

一个 research idea 首先要回答：

```text
我解决、解释、测量或反驳什么问题？
```

Signal 只是线索，problem 才是论文要处理的对象，claim 是论文要证明的主张，method/experiment 是支持 claim 的手段。

例子：

```text
Signal:
很多 multi-agent reasoning paper 报告提升，但没有严格控制 token budget。

Problem:
我们无法判断 multi-agent reasoning 的收益到底来自 agent collaboration，还是只是更多 sampling / token budget。

Claim:
在固定 token budget 下，许多 reported multi-agent gains 会显著下降；真正的 collaboration gain 只出现在需要信息分工或冲突协调的任务中。
```

没有清楚 problem，就不要生成 claim；没有清楚 claim，就不要查 novelty；没有 prior-work collision，就不要判断 paper-worthiness。

---

## 初始化 research_state

```bash
python .agents/skills/research-state-artifact-management/scripts/init_research_state.py   --project-name "Multi-Agent Reasoning Evaluation"
```

它会创建：

```text
research_state/
  00_state/
  01_literature/
  02_signals/
  02_problems/
  03_claims/
  04_prior_work/
  05_scope/
  06_experiments/
  07_reviewer/
  08_paper_shape/
  99_archive/
```

最重要的文件：

```text
research_state/00_state/current_state.md
research_state/00_state/decision_log.md
research_state/02_problems/problem_formulations.md
research_state/03_claims/claim_ledger.md
research_state/06_experiments/experiment_log.md
```

---

## 使用示例

### 从新方向开始

```text
$ai-research-orchestrator

我要在 LLM agents / multi-agent reasoning 方向找一个可投 ICLR 或 COLM 的论文 idea。
请先初始化 research_state，然后从代表性文献阅读和 field map 开始。
```

### 从已有论文开始

```text
$ai-research-orchestrator

我已经有一组 RAG 相关论文。请先建立 literature field map，然后从 introduction、related work、limitations 和 evaluation setup 中提取 research signals。
```

### 从已有 idea 开始

```text
$ai-research-orchestrator

我有一个 idea：现有 multi-agent reasoning 的提升主要来自更高 token budget，而不是真正的 agent collaboration。
请先定义它要解决的问题，再转成 candidate claims。
```

### 直接调用 problem formulation

```text
$problem-formulation

请把这个 signal 转成清楚的 research problem：很多 long-context RAG paper 没有区分 retrieval failure 和 evidence conflict。
```

### 设计实验

```text
$decision-value-experiment-planner

基于当前 active problem 和 active claim，设计第一轮实验。实验必须有决策价值，不要为了填满 ablation 表格而设计低信息增益实验。
```

---

## 核心原则

1. 先建立 field map，再追逐 idea。
2. 从 signal 开始，不从方法开始。
3. 先定义 problem，再生成 claim。
4. 生成 candidate claims，而不是泛泛的 ideas。
5. 评估 residual contribution，而不是 raw idea。
6. 不要强行套 target reframing。
7. 不要崇拜简单。
8. 不要用扩大 scope 来掩盖 weak novelty。
9. 实验必须有决策价值。
10. 最小实验必须有效，不能用失真的 cheap proxy 偷懒。
11. 研究状态必须 checkpoint。

---

## Skills 如何环环相扣

Codex skills 不是普通程序里的函数调用链。连续性来自：

1. `$ai-research-orchestrator` 判断下一阶段；
2. 每个阶段更新 `research_state/`；
3. 每个 skill 有 exit condition；
4. 必要时显式调用下一个 `$skill-name`。

Chat 是工作区，文档是长期记忆。


