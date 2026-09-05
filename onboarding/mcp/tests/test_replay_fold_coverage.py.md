# mcp/tests/test_replay_fold_coverage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_replay_fold_coverage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T22:23+02:00 |
| lastVerifiedCommitHash | `e84c004c37a4bad082e1a7f1bdc4bd062282a185` |
| lastVerifiedCommitDate | 2026-09-04T22:06:05+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Fully standalone CCR-R17 (leaf 260831-CCR-L17) reducer-fold and span-interval coverage forcing suite. Every R16 closeout event kind must reach its reducer fold branch in `certification/replay/measure.py`, and the span wall-union in `certification/replay/spans.py` must take its fully-contained and extending-overlap arcs. Nothing is shared with another suite; events are constructed here.

## Code Commentary

### Logic

- Union-wall arcs (`test_wall_union_handles_contained_and_extending_overlaps`, lines 83-97; `test_wall_union_touching_intervals_do_not_double_count`, lines 100-106; `test_wall_union_single_interval`, lines 108-111).
- Reducer fold branches: admission flags (`test_reducer_folds_candidate_admitted_flag`, lines 113-127; `test_reducer_folds_admission_refused_flag`, lines 130-143), finalization flags (`test_reducer_folds_finalization_flags`, lines 146-186), operation terminal (`test_reducer_records_operation_terminal`, lines 190-196), gate/rail census (`test_reducer_folds_gate_start_and_rail_census`, lines 199-242), gate pass published/reused (`test_reducer_folds_gate_pass_published_and_reused`, lines 249-277), red and blocked decisions (`test_reducer_folds_red_and_blocked_decision_kinds`, lines 280-337), certificate invalidation (`test_reducer_folds_certificate_invalidation`, lines 340-363), catalog with attached spans (`test_reducer_folds_catalog_with_spans_attached`, lines 366-400), and unknown-kind pass-through (`test_reducer_ignores_unknown_closeout_kinds`, lines 403-416).

### Conventions

Standalone per the evidence-lifecycle isolation rule; imports no pre-existing mcp/tests support module.

### Invariants And Boundaries

- Every closeout event kind reaches its fold branch; unknown closeout kinds are ignored without error.
- Union-wall arithmetic covers contained, extending, touching, and single intervals.
- The reducer never misclassifies a stream; it only records what the export says.

### Todos

None recorded.

## Docs References

No external Domain Documentation source is configured for this repository-owned suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source governs this test module. | - | - |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The reducer fold under coverage. | `measure_replay_run`; `_fold_event`; `_GATE_FOLDERS` | mcp/src/agents_remember/certification/replay/measure.py:53-86; mcp/src/agents_remember/certification/replay/measure.py:89-101; mcp/src/agents_remember/certification/replay/measure.py:225-235 |
| The span wall-union under coverage. | `_wall_union_millis`; `category_wall_union_millis`; `gross_wall_union_millis` | mcp/src/agents_remember/certification/replay/spans.py:79-90; mcp/src/agents_remember/certification/replay/spans.py:26-31; mcp/src/agents_remember/certification/replay/spans.py:34-36 |
| The measured run/catalog records produced by the folds. | `RunMeasurement`; `GateRunMeasurement`; `CatalogRailRecord` | mcp/src/agents_remember/certification/replay/models.py:255-286; mcp/src/agents_remember/certification/replay/models.py:196-252 |
| The explicit unit-regression lane registration. | "mcp/tests/test_replay_fold_coverage.py" | mcp/tests/test-evidence-lanes.toml:157-157 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Same-repository forcing suite; nothing crosses repositories. | - | - |

## Update History

- 2026-09-05T06:39:59+00:00 — L31 scoped citation curation against frozen ea359649: repaired anchor grammar and exact source coordinates while preserving the current behavioral claims. No content impact; source verification metadata was not advanced.

- 2026-09-04T22:23+02:00 - 260831-CCR-L17 Gate-5 memory pass: created for the new CCR-R17 reducer-fold and span-interval coverage suite (every closeout event kind, every union-wall arc). Verification stamp is the full leaf code commit `e84c004c37a4bad082e1a7f1bdc4bd062282a185` (tree `f97c4969d7ddb93eed75c80a4936fc05fab8e2eb`).
