#!/usr/bin/env python3
"""Initialize a research_state directory for the AI research idea pipeline.

Usage:
  python .agents/skills/research-state-artifact-management/scripts/init_research_state.py --project-name "My Project"
  python .agents/skills/research-state-artifact-management/scripts/init_research_state.py --target my_state --project-name "RAG Evidence Conflict"
"""
from __future__ import annotations

import argparse
from pathlib import Path
from datetime import date

ROOT_DIRS = [
    "00_state",
    "01_literature/reading_notes",
    "02_signals",
    "02_problems",
    "03_claims/claim_versions",
    "04_prior_work/collision_maps",
    "04_prior_work/residual_contributions",
    "05_scope",
    "06_experiments/results",
    "07_reviewer",
    "08_paper_shape",
    "99_archive/superseded_notes",
]

BASE_FILES = {
    "00_state/project_brief.md": "# Project Brief\n\nProject: {project_name}\nCreated: {today}\n\n## Target area\n\nTBD\n\n## Goal\n\nTBD\n\n## Resource constraints\n\nTBD\n",
    "00_state/current_state.md": "# Current State\n\nProject: {project_name}\nUpdated: {today}\n\n## Current stage\n\nentry-source-intake\n\n## Active claim\n\nNone yet.\n\n## Current paper shape\n\nUnknown.\n\n## Literature coverage\n\nUninitialized.\n\n## Top risks\n\nTBD\n\n## Next decision\n\nDefine entry state and source intake.\n\n## Next action\n\nUse $ai-research-orchestrator or $entry-source-intake.\n",
    "00_state/decision_log.md": "# Decision Log\n\nUse immutable decision records.\n\n## D001\n\nDate: {today}\nDecision: Initialize research state.\nWhy: Start the modular AI research idea pipeline.\nEvidence: User/project setup.\nConsequence: Proceed to entry-source-intake.\n",
    "00_state/open_questions.md": "# Open Questions\n\n- What is the target area?\n- What sources are available?\n- What resource constraints apply?\n",
    "01_literature/paper_index.md": "# Paper Index\n\n| Paper ID | Title | Year | Type | Why included | Status |\n|---|---|---:|---|---|---|\n",
    "01_literature/field_map.md": "# Field Map\n\n## Main problem formulations\n\n## Method families\n\n## Evaluation protocols\n\n## Common claims\n\n## Repeated limitations\n\n## Unstable assumptions\n\n## Closest work clusters\n\n## Potential research tensions\n\n## Literature coverage status\n",
    "01_literature/method_family_map.md": "# Method Family Map\n\n",
    "01_literature/evaluation_map.md": "# Evaluation Map\n\n",
    "02_signals/signal_bank.md": "# Signal Bank\n\n| Signal ID | Source | Abnormal phenomenon | Why it matters | Linked problem | Candidate move | Status |\n|---|---|---|---|---|---|---|\n",
    "02_problems/problem_formulations.md": "# Problem Formulations\n\n| Problem ID | Source signal | Problem statement | Why it matters | Problem owner | Current gap | Status |\n|---|---|---|---|---|---|---|\n",
    "03_claims/candidate_claims.md": "# Candidate Claims\n\n",
    "03_claims/claim_ledger.md": "# Claim Ledger\n\n| Claim ID | Source problem | Problem statement | Claim | Status | Research move | Last update | Notes |\n|---|---|---|---|---|---|---|---|\n",
    "03_claims/research_move_routing.md": "# Research Move Routing\n\n",
    "06_experiments/experiment_log.md": "# Experiment Log\n\n| Experiment ID | Claim ID | Hypothesis | Decision value | Result | Decision impact |\n|---|---|---|---|---|---|\n",
    "08_paper_shape/execution_plan.md": "# Execution Plan\n\n## Next 1–2 weeks\n\n",
    "99_archive/abandoned_claims.md": "# Abandoned Claims\n\n",
}

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", default="research_state", help="Target state directory to create")
    parser.add_argument("--project-name", default="AI Research Project", help="Project name")
    args = parser.parse_args()

    target = Path(args.target)
    today = date.today().isoformat()
    for d in ROOT_DIRS:
        (target / d).mkdir(parents=True, exist_ok=True)
    for rel, content in BASE_FILES.items():
        path = target / rel
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content.format(project_name=args.project_name, today=today), encoding="utf-8")
    print(f"Initialized {target} for {args.project_name}")

if __name__ == "__main__":
    main()
