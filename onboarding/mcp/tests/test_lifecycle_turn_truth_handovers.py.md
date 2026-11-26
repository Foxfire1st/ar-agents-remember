# mcp/tests/test_lifecycle_turn_truth_handovers.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Cross-role handover agreement and corpus-convergence proofs for turn-truth doctrine, split from `test_lifecycle_turn_truth_doctrine.py`.

## Code Commentary

`OWED_STATEMENTS` declares the boundary clauses owed by `core/acceptance.md`, `templates/master-handover-packet.md`, and `templates/turn-report.md`. `AgreementAcrossTheRoleSetTests` sweeps all `canonical_surfaces()` for contradictions (failing closed if the tree shrinks), enforces exact equality between `COMPLETION_TRUTH_ROSTER` and surfaces matching `COMPLETION_TRUTH_VOCABULARY`, verifies `Reading.STATED` on every roster surface, proves direct Worker-to-Reviewer and Worker-to-Curator handover routes with mutation teeth, and confirms delivered Architect, Manager, and Orchestrator capsules check candidate evidence before acceptance. `ConvergenceTeethTests` confirms four reconciled sites (`core/acceptance.md`, `roles/architect.md`, `roles/orchestrator.md`, `roles/reviewer.md`) read clean while synthetic contradicting mutants, appended contradictions, and removed owed clauses fail.

## Relationships

Imports normalization, vocabulary, roster, classifier, and contradiction detector from `mcp/tests/test_lifecycle_turn_truth_doctrine.py`. Inspects `skills/l-01-agent-lifecycles/` directly.

## Evidence

- `AgreementAcrossTheRoleSetTests` sweeps canonical surfaces for turn-truth contradictions, enforces roster/vocabulary parity, and checks owed boundary statements on `core/acceptance.md` and handover templates. [1]
- Direct Worker-to-Reviewer/Curator handovers and coordinator candidate-evidence checks are verified with mutation tests across roles, operations, core, and `sync-and-repairs.md`. [2]
- `ConvergenceTeethTests` confirms reconciled sites read clean while paired synthetic mutants, appended contradictions, and removed owed clauses fail. [3]
