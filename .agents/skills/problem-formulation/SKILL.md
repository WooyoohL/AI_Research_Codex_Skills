---
name: problem-formulation
description: Use after research-signal-mining and before candidate-claim-set to define the actual research problem an AI/ML paper idea solves, explains, measures, or refutes. Separates signal, problem, claim, and method so later novelty, scope, and experiment decisions are grounded.
---

# Problem Formulation

## Purpose

Turn a signal, vague direction, or method idea into a clear research problem before generating claims.

A signal is a clue. A method is a possible response. A claim is what the paper will argue. The problem is the thing the paper is trying to solve, explain, measure, or refute.

Do not proceed to candidate claims until the problem is explicit enough to judge importance and scope.

## Trigger

Use this skill when:

- signal mining has found an abnormal phenomenon or research tension;
- the user has a vague idea but cannot say what problem it solves;
- the idea is framed as a method/module rather than a problem;
- claim generation is about to start;
- scope or experiments feel unfocused.

## Core distinction

```text
Signal: What clue suggests something is wrong or interesting?
Problem: What unresolved issue does the paper address?
Claim: What will the paper prove, show, explain, or refute?
Method: What intervention or artifact may support the claim?
```

Example:

```text
Signal:
Many multi-agent reasoning papers report gains without controlling token budget.

Problem:
The community cannot tell whether reported multi-agent gains come from genuine collaboration or from increased sampling/token budget.

Claim:
Under fixed token budgets, many reported multi-agent gains disappear, while genuine collaboration gains remain only in tasks requiring information partitioning or conflict resolution.
```

## Required output

For each active signal or vague idea, produce a problem formulation record:

```text
Problem ID:
Source signal / idea:
Problem statement:
What problem does this paper solve, explain, measure, or refute?

Why it matters:
Why should the research community care if this problem is addressed?

Problem owner:
Who cares most: method designers, benchmark builders, systems researchers, theory researchers, deployment teams, safety/alignment researchers, or another group?

Current gap:
Why do existing methods, evaluations, theories, or datasets not solve it well?

Problem type:
method / evaluation / measurement / mechanism / negative result / efficiency / theory / data / system / taxonomy

Why now:
What changed that makes this problem timely: new model scale, new benchmark, new deployment setting, new failure mode, new compute regime, or new literature tension?

Non-problem / out of scope:
What adjacent problems does this paper explicitly not solve?

Candidate claim directions:
2–4 possible claims that could address this problem.

Status:
active / parked / rejected / needs literature check
```

## Checks

Before leaving this stage, ask:

1. Is the problem more than “we need a better method”?
2. Is the problem important if the proposed claim turns out true?
3. Is the problem distinct from the signal that revealed it?
4. Is the problem distinct from the method used to address it?
5. Does the problem have a clear owner or audience?
6. Is the non-problem boundary clear enough to prevent scope creep?

## Failure modes

- Treating a signal as the problem.
- Treating a method as the problem.
- Defining the problem so broadly that any result could fit.
- Defining the problem so narrowly that it becomes an implementation detail.
- Claiming importance without explaining who should care.
- Skipping current-gap reasoning before claim generation.

## State updates

Update or create:

```text
research_state/02_problems/problem_formulations.md
research_state/00_state/current_state.md
```

If the source signal exists in `research_state/02_signals/signal_bank.md`, link the Problem ID back to that signal.

## Exit condition

This stage is complete when each active signal has at least one problem formulation with:

- problem statement;
- why it matters;
- current gap;
- problem type;
- non-problem boundary;
- 2–4 candidate claim directions.

Next skill: `$candidate-claim-set`.
