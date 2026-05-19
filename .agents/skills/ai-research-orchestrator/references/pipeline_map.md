# Pipeline Map

```text
00 entry-source-intake
01 representative-literature-bootstrap
02 research-signal-mining
03 candidate-claim-set
04 research-move-router
05 claim-prior-work-triangulation
06 paper-unit-scope-gate
07 decision-value-experiment-planner
08 reviewer-risk-check
09 paper-shape-generator
X  research-state-artifact-management
S  research-target-reframing
```

Use `ai-research-orchestrator` as the entry point. It does not run the whole flow automatically; it routes one bounded stage at a time and writes state artifacts.
