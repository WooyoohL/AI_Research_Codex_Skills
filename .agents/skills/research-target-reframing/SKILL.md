---
name: research-target-reframing
description: Use when analyzing research papers, research ideas, ML/AI methods, or project proposals to identify the core problem representation, hidden complexity, simplifying target, first-principles reformulation, ablation plan, and “why not simpler?” research taste. 适用于论文拆解、研究品味蒸馏、idea 评估、方法重构、实验设计、找 surprise/不对劲现象。
---

# Research Target Reframing Skill

Use this skill to analyze a research paper, method, idea, or project proposal through the lens of target reframing: find where the current formulation makes the problem unnecessarily hard, then rewrite the target, parameterization, supervision signal, or boundary condition so that the correct behavior becomes natural.

This skill is especially useful for ML/AI research, but can also be used for scientific or technical research strategy more broadly.

## Core stance

Do not treat complexity as proof of depth. Treat complexity as a diagnostic signal.

A strong research move often starts from an abnormal phenomenon, not from a generic desire to improve a metric. Ask why the current field needs so many tricks, whether those tricks are compensating for a bad representation, and whether a simpler formulation would make the desired behavior easy.

The goal is not to worship simplicity. The goal is to distinguish necessary complexity from accidental complexity.

## Default output structure

When invoked, produce an analysis with these sections unless the user asks for a different format:

1. **One-sentence thesis**
   - State the core judgment directly.
   - Example: “This idea is promising because it changes the prediction target, not merely the architecture.”

2. **The abnormal phenomenon**
   - Identify the surprising or uncomfortable fact that motivates the work.
   - Prefer “why is this necessary?” questions over “how can we add more?” questions.
   - Examples:
     - Why does a deeper network train worse than a shallower one?
     - Why does this self-supervised method require negative samples, momentum encoders, or collapse-prevention tricks?
     - Why does one-step generation require distillation, curriculum, or self-consistency constraints?
     - Why is the model predicting an indirect variable instead of the desired object?

3. **Current formulation and its bad smell**
   - Write down what the existing method asks the model to learn.
   - Identify whether the target is:
     - directly supervised,
     - network-dependent,
     - teacher-dependent,
     - constraint-only,
     - solver-dependent,
     - schedule-dependent,
     - or held together by multiple auxiliary losses.
   - Call out hidden sources of complexity: curriculum, distillation, special initialization, large batch assumptions, extra encoders, memory banks, hand-tuned schedules, fragile losses, or implicit constraints.

4. **The trivial correct behavior**
   - Define what should be easy if the problem were well represented.
   - Look for identity, zero residual, copy/reconstruction, clean target, endpoint prediction, conservation law, average quantity, closed-form statistic, or another network-independent object.
   - Ask: “What is the simplest correct output in the limiting case?”

5. **Target reframing move**
   - Propose or identify the change in representation:
     - direct target → residual target,
     - contrastive proxy → reconstruction target,
     - instantaneous local quantity → averaged/global quantity,
     - noisy indirect variable → clean data target,
     - network-behavior constraint → independently defined mathematical object,
     - hard function → deviation from an easy baseline.
   - Explain why this makes the desired behavior easier to optimize or verify.

6. **What becomes simpler**
   - List which pieces of machinery may become unnecessary or less central.
   - Be precise: do not claim “no tricks” unless the method truly removes them.
   - Separate removed complexity from remaining necessary engineering.

7. **What is still nontrivial**
   - Identify the parts that remain technically hard.
   - Avoid overselling. A better target can still require careful architecture, optimization, sampling, scaling, or implementation details.
   - State any assumptions that must hold.

8. **Experiments that would convince me**
   - Propose the smallest experiment that tests the core reframing.
   - Include ablations that remove old tricks one by one.
   - Include scaling and transfer tests if the claim is about generality.
   - Include failure-mode probes.

9. **Verdict**
   - Classify the idea as one of:
     - strong target reframing,
     - plausible but under-validated reframing,
     - mostly engineering improvement,
     - metric-chasing without conceptual simplification,
     - or misleading simplification.

## Heuristics

### Find the “why not simpler?” question

Before proposing a new method, ask:

- Why does the standard method need this much machinery?
- Is the model being asked to predict the thing we actually want?
- Is the supervision signal independent of the model, or produced by the model/teacher/history?
- What is the easiest correct behavior, and is it easy under the current parameterization?
- Could a residual, average, endpoint, reconstruction, or clean target make the problem more direct?

### Treat tricks as evidence

Tricks are not automatically bad. They are evidence.

For each trick, classify it as:

- **Essential complexity**: required by the problem or data.
- **Optimization patch**: needed because the formulation is hard to train.
- **Historical artifact**: inherited from earlier methods without being central.
- **Evaluation hack**: helps the benchmark but does not clarify the problem.

A good reframing should eliminate or downgrade at least one optimization patch or historical artifact.

### Prefer network-independent targets

A target is stronger when it is defined independently of the current model’s predictions.

Prefer:

- labels,
- masked inputs,
- clean data,
- endpoint differences,
- physical quantities,
- closed-form statistics,
- mathematical identities,
- known boundary conditions.

Be cautious with:

- self-distillation targets,
- teacher-generated pseudo-labels,
- consistency constraints with no independent ground truth,
- targets that depend on the current network’s output,
- targets that only exist because of a training schedule.

Network-dependent targets can still work, but they should be named honestly.

### Use simplification to test understanding

A simpler formulation is meaningful only if it preserves or improves the important behavior.

Check:

- Does it work without the old stabilizers?
- Does it scale with model size and data size?
- Does it transfer to related tasks?
- Does it reduce failure cases or merely hide them?
- Does it clarify why previous methods were complicated?

## Research-template prompt

When helping the user generate or evaluate an idea, use this template internally:

```text
Phenomenon: What is the surprising or uncomfortable fact?
Current formulation: What does the field currently ask the model/system to learn?
Bad smell: Which parts look like patches for a bad representation?
Trivial correct behavior: What should be easy in the simplest case?
Reframing: What target, variable, coordinate system, or boundary condition can be changed?
Independent target: Is the new target defined without the current network or teacher?
Complexity removed: Which tricks become unnecessary?
Remaining complexity: What is still genuinely hard?
Minimal experiment: What is the smallest experiment that tests the reframing?
Ablation plan: Which old mechanisms should be removed one by one?
Scaling/transfer: What would show this is not a toy result?
Failure modes: Where should the reframing break?
Verdict: Is this a conceptual simplification or just an engineering tweak?
```

## Style guidelines

- Be direct and critical, but not dismissive.
- Separate conceptual claims from empirical claims.
- Do not overclaim novelty or simplicity.
- If the user provides a paper or claims about recent work, verify details when possible before making factual assertions.
- If there is uncertainty, state it explicitly.
- When writing in Chinese, use clear research-discussion language rather than motivational prose.
- Avoid turning every method into the same story. Use the target-reframing lens only where it actually fits.

## Example compressed analysis pattern

Use this short pattern when the user wants a quick judgment:

```text
我的判断：这个 idea 的核心价值不在于换了 [architecture/module]，而在于把 [old target] 改写成了 [new target]。

合理之处：它让 [trivial correct behavior] 变得容易，并减少了对 [trick/mechanism] 的依赖。

风险：它仍然依赖 [remaining complexity]，所以不能说已经完全消解复杂性。

最关键实验：去掉 [old trick]，只保留 [new target]，看 [metric/stability/scaling] 是否仍然成立。
```

## Invocation examples

The user may invoke this skill explicitly with:

- `$research-target-reframing 分析这篇论文的研究 taste`
- `$research-target-reframing 帮我判断这个 ML idea 是否只是 trick`
- `$research-target-reframing 用何恺明式 why-not-simpler 视角拆解这个方法`
- `$research-target-reframing 把这个方向蒸馏成一个 research skill`


---

# Integration note for the modular pipeline

This specialist lens should be invoked by `04-research-move-router` only when the active claim appears to involve bad formulation, awkward target definition, accidental complexity, or unnecessary reliance on tricks.

It should not be used as the default explanation for all good research ideas. If the better paper shape is evaluation, benchmark, negative result, mechanism analysis, scaling/regime shift, system, theory, dataset, or taxonomy, use the corresponding research move instead.

## Pipeline integration

When used inside the modular pipeline, finish by updating or creating the relevant research-state artifacts. Do not rely on chat context as the only source of truth.

State artifacts to update:

- `research_state/03_claims/claim_ledger.md`
- `research_state/05_scope/paper_unit_gate_Cxxx.md`

Recommended next step:

- Continue with `claim-prior-work-triangulation`, unless the exit condition is not met.

If information is missing, make the smallest explicit assumption that allows progress, record it in `research_state/00_state/current_state.md`, and mark the status as provisional.
