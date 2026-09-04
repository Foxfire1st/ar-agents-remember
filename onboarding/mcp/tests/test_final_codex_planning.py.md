# mcp/tests/test_final_codex_planning.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_final_codex_planning.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T22:45+02:00 |
| lastVerifiedCommitHash | `54ff803a05209e06f732f2de1f90e2a71a069e08` |
| lastVerifiedCommitDate | 2026-09-04T22:31:30+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Standalone CCR-R14 planning and predecessor-barrier tests (leaf 260831-CCR-L14, code commit 54ff803a). Covers plan-record compilation against the canonical R11 registry and certifying plan, plus the exact Gate-1..3 must-not-run barriers: missing, red, non-certifying, candidate-mismatched, or differently bound predecessors refuse before any scenario step starts. Fully standalone: it imports only the leaf-local builder module and the package under test.

## Code Commentary

### Logic

`other_plan` (lines 36-43) builds a foreign certifying plan, and `store_codes` (lines 32-34) extracts refusal codes. `FinalCodexPlanningTests` (lines 44-140) covers: the plan record binding the exact certifying plan (45-61); a foreign certifying plan refusing (62-74); green Gate-1..3 manifests admitting while non-green predecessors refuse (75-99); a candidate mismatch refusing (100-112); an altitude mismatch refusing (113-127); and a gate-plan mismatch refusing (128-140).

### Conventions

Every refusal asserts typed `CertificationContractError` findings; barrier codes use the `final-codex-` family.

### Invariants And Boundaries

- The plan record must equal the exact canonical registry compilation for the selected certifying profile.
- The selected profile must plan the complete sorted Gate-1..4 prefix.
- Predecessor manifests must be green, certifying-altitude, candidate-bound, and plan-bound.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this memory root. CCR-R14@v3 (approved packet, leaf 14_final-real-codex-certification) requires the exact-predecessor must-not-run barriers; task artifact paths are not repo-relative citations, so clauses are recorded as prose.

| Finding | Anchor | Source |
| --- | --- | --- |
| The exact Gate-1..3 predecessor barriers refuse before any scenario step. | `FinalCodexPlanningTests` | mcp/tests/test_final_codex_planning.py:44-140 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exercises plan-record compilation and the predecessor barrier helpers. | `compile_final_codex_plan_record`; `require_gates_one_to_three_green` | mcp/src/agents_remember/certification/final_codex/planning.py:45-131; mcp/src/agents_remember/certification/final_codex/planning.py:194-256 |
| The shared leaf builders supply the scenario registry, certifying plan, and green gates. | `scenario_registry`; `certifying_plan`; `green_gates` | mcp/tests/test_final_codex_models.py:168-193; mcp/tests/test_final_codex_models.py:195-202; mcp/tests/test_final_codex_models.py:256-260 |

## Cross-Repo References

No cross-repository evidence is required.

| Finding | Anchor | Source |
| --- | --- | --- |
| Every case is in-process and repository-neutral. | - | - |

## Update History

- 2026-09-04T22:45+02:00 - 260831-CCR-L14 Gate-5 memory pass: created this card for the new standalone CCR-R14 planning and predecessor-barrier suite delivered in code commit 54ff803a; anchors and ranges derived from the current worktree source and pinned to that commit (tree aff2e268968397ab8db042a782652957a3600dda).
