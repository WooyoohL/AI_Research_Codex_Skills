# AGENTS.md example for AI research idea workflow

When the user asks for AI/ML research idea discovery, paper-claim refinement, prior-work analysis, experiment planning, or reviewer-risk checking, prefer using:

```text
$ai-research-orchestrator
```

Do not run the entire research pipeline in one pass. Work one bounded stage at a time, update `research_state/`, and use the next skill only after the current stage exit condition is met.

Keep these source-of-truth files current:

```text
research_state/00_state/current_state.md
research_state/00_state/decision_log.md
```

Core rules:

1. No clear claim, no novelty check.
2. No prior-work collision, no final paper-worthiness judgment.
3. Evaluate residual contribution, not raw idea.
4. Experiments must have decision value.
5. Minimal experiments must preserve the problem essence.
6. Checkpoint every decision-relevant milestone.


For AI/ML research idea discovery, first ensure the workflow distinguishes signal, problem, claim, and method. Use `$problem-formulation` before `$candidate-claim-set` when the problem is not explicit.
