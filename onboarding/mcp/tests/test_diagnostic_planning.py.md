# mcp/tests/test_diagnostic_planning.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_diagnostic_planning.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T17:50+02:00 |
| lastVerifiedCommitHash | `4ba18bb23ba90e201bb37341d61c0efc64161fcf` |
| lastVerifiedCommitDate | 2026-09-04T17:23:11+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Standalone CCR-R13 diagnostic plan-projection tests (leaf 260831-CCR-L13, code commit 4ba18bb2). The diagnostic plan must project the exact R11 canonical scenario rail at diagnostic altitude - same rail identity, posture, and applicability semantics as the certifying plan - never a second scenario implementation. Refusals cover non-diagnostic profiles, unplanned scenario gates, missing certifying plans, and rail-catalog drift.

## Code Commentary

### Logic

The suite is registered in the `unit-regression` lane. `RailSpec` (lines 61-135) and `registry` (lines 136-175) build the canonical registry with the certifying (portable-ci, gates 1-5) and diagnostic (diagnostic-ci, gates 1-4) profiles; `certifying_plan` (lines 177-183) compiles the certifying plan and `codes` (lines 185-186) extracts typed finding codes. `DiagnosticPlanningTests` (lines 189-317) covers: the scenario gate projecting the exact canonical rails with the complete earlier-gate prefix (lines 190-210); an unplanned scenario gate at gate 5 or a prefixless gate 3 (lines 212-234); non-diagnostic and unknown profile refusal (lines 236-256); a certifying plan that does not name the scenario gate (lines 258-273); rail-catalog drift refused as a second scenario (lines 275-288); applicability drift on the scenario rail (lines 290-304); and exact candidate binding (lines 306-317).

### Conventions

Every refusal is asserted through the typed `CertificationContractError` finding codes (diagnostic-profile-kind-mismatch, diagnostic-profile-unknown, diagnostic-scenario-gate-unplanned, diagnostic-certifying-plan-missing, diagnostic-scenario-rail-mismatch).

### Invariants And Boundaries

- The diagnostic profile must be diagnostic altitude and plan the complete earlier-gate prefix through the scenario gate.
- The scenario rail catalog must be byte-equivalent to the certifying plan's rails in identity, posture, and applicability.
- The compiled diagnostic plan binds the exact candidate.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this memory root. CCR-R13@v2 (frozen digest f0387b1627c5e8f48073b55d40dc362065e46943c5688f0f863fddb480770d3a) forbids a second scenario implementation; task artifact paths are not repo-relative citations, so clauses are recorded as prose.

| Finding | Anchor | Source |
| --- | --- | --- |
| Diagnostics may only replicate the exact canonical scenario rails at diagnostic altitude. | `test_rail_catalog_drift_is_refused_as_a_second_scenario` | mcp/tests/test_diagnostic_planning.py:275-288 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exercises the diagnostic plan compiler and scenario-gate selectors. | `compile_diagnostic_plan`; `diagnostic_scenario_gate` | mcp/src/agents_remember/certification/diagnostics/planning.py:30-96; mcp/src/agents_remember/certification/diagnostics/planning.py:99-114 |
| Uses the canonical five-gate registry and certifying plan compiler as inputs. | `registry`; `compile_certification_plan` | mcp/tests/test_diagnostic_planning.py:136-183 |
| The planning registry builders are shared with the diff-coverage closure module. | `planning_registry` | mcp/tests/test_diagnostic_diff_coverage.py:92-97 |

## Update History

- 2026-09-05T06:39:59+00:00 — L31 scoped citation curation against frozen ea359649: repaired anchor grammar and exact source coordinates while preserving the current behavioral claims. No content impact; source verification metadata was not advanced.

- 2026-09-04T17:50+02:00 - 260831-CCR-L13 Gate-5 memory pass: created this card for the new standalone CCR-R13 diagnostic plan-projection suite delivered in code commit 4ba18bb2; anchors and ranges derived from the current worktree source and pinned to that commit (tree 631145bf3e0d5899b1dcbccf8c0d4a8257821f0d).
