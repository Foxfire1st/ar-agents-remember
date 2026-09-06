# mcp/tests/test_replay_model_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_replay_model_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:42:13+00:00 |
| lastVerifiedCommitHash | `e84c004c37a4bad082e1a7f1bdc4bd062282a185` |
| lastVerifiedCommitDate | 2026-09-04T22:06:05+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Fully standalone CCR-R17 (leaf 260831-CCR-L17) edge forcing suite for the measured-replay model, freeze, reducer, and report contracts. These tests drive the defensive branches that scenario tests leave cold: model validators that refuse malformed records, freeze comparability refusals, reducer fold and refusal paths, digest self-verification refusals, and comparison-report digest verification. All fixtures are constructed here; nothing is shared with another suite.

## Code Commentary

### Logic

- Vocabulary refusals (`test_semantic_text_refuses_blank_or_padded_values`, lines 174-187; `test_scenario_outcome_refuses_green_with_findings`, lines 190-201; `test_scenario_outcome_refuses_non_green_without_findings`, lines 204-207).
- Span-reduction edges (`test_span_category_totals_refuse_active_above_wall`, lines 209-217; `test_span_reduction_refuses_duplicate_categories`, lines 219-228; `test_span_reduction_refuses_wrong_span_count`, lines 231-241; `test_span_reduction_refuses_tampered_digest`, lines 243-257).
- Gate/run measurement shape refusals (`test_gate_measurement_refuses_started_count_without_start`, lines 260-263; `test_gate_measurement_refuses_blocked_and_started_together`, lines 265-268; `test_gate_measurement_refuses_zero_start_evidence_when_started`, lines 270-273; `test_gate_measurement_refuses_counts_without_disposition`, lines 275-288; `test_gate_measurement_refuses_catalog_without_disposition`, lines 290-297; `test_gate_measurement_rail_properties_partition_catalog`, lines 299-317; `test_run_measurement_refuses_wrong_gate_order`, lines 320-324; `test_run_measurement_refuses_admitted_and_refused`, lines 326-329; `test_run_measurement_refuses_tampered_digest`, lines 331-336).
- Placement/evidence/profile edges (`test_rail_placement_refuses_class_gate_mismatch`, lines 338-345; `test_evidence_placement_helpers_filter_by_gate_and_rail`, lines 347-370; `test_profile_snapshot_placements_for_gate`, lines 372-386).
- Comparability and population refusals (`test_comparability_report_refuses_comparable_with_change`, lines 389-401; `test_comparability_report_refuses_incomparable_without_change`, lines 403-411; `test_candidate_digest_change_is_a_source_change`, lines 414-426; `test_population_refuses_duplicate_generations`, lines 429-441; `test_population_refuses_tampered_digest`, lines 443-452; `test_population_stratum_helpers_route_by_stratum`, lines 454-467; `test_append_only_refuses_new_non_supplement_row`, lines 469-480).
- Report and reducer refusals (`test_comparison_report_refuses_tampered_digest`, lines 483-510; `test_reducer_refuses_empty_export`, lines 545-547; `test_reducer_requires_gate_identity_on_gate_events`, lines 550-553; `test_reducer_refuses_diagnostic_envelope`, lines 556-559).

### Conventions

Standalone per the evidence-lifecycle isolation rule; imports no pre-existing mcp/tests support module.

### Invariants And Boundaries

- Every tested validator refuses the malformed record instead of silently coercing it.
- Digest self-verification refusals are proven for every digest-bearing record.
- Green outcomes never carry findings; non-green outcomes always carry one.

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
| The model vocabulary under test. | `ReplayScenarioExpectation`; `ScenarioOutcome`; `SpanReduction`; `GateRunMeasurement`; `RunMeasurement` | mcp/src/agents_remember/certification/replay/models.py:83-89; mcp/src/agents_remember/certification/replay/models.py:92-105; mcp/src/agents_remember/certification/replay/models.py:150-175; mcp/src/agents_remember/certification/replay/models.py:196-252; mcp/src/agents_remember/certification/replay/models.py:255-286 |
| The freeze comparability/population refusals under test. | `ReplayComparabilityReport`; `ReplayPopulation`; `compare_replay_freezes` | mcp/src/agents_remember/certification/replay/freeze.py:74-90; mcp/src/agents_remember/certification/replay/freeze.py:93-116; mcp/src/agents_remember/certification/replay/freeze.py:134-157 |
| The comparison report digest under test. | `ReplayComparisonReport`; `build_replay_comparison_report` | mcp/src/agents_remember/certification/replay/compare.py:47-69; mcp/src/agents_remember/certification/replay/compare.py:72-96 |
| The reducer refusal paths under test. | `measure_replay_run`; `_required_gate` | mcp/src/agents_remember/certification/replay/measure.py:53-86; mcp/src/agents_remember/certification/replay/measure.py:243-250 |
| The explicit unit-regression lane registration. | "mcp/tests/test_replay_model_edges.py" | mcp/tests/test-evidence-lanes.toml:161-161 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Same-repository forcing suite; nothing crosses repositories. | - | - |

## Update History

- 2026-09-06T00:42:13+00:00 — Gate-5 citation repair: re-read the cited evidence-lane member and its declared classification and corrected its incoming range. Existing source verification provenance is retained.

- 2026-09-05T06:39:59+00:00 — L31 scoped citation curation against frozen ea359649: repaired anchor grammar and exact source coordinates while preserving the current behavioral claims. No content impact; source verification metadata was not advanced.

- 2026-09-04T22:23+02:00 - 260831-CCR-L17 Gate-5 memory pass: created for the new CCR-R17 model-edge forcing suite (validator, comparability, reducer, and digest refusals). Verification stamp is the full leaf code commit `e84c004c37a4bad082e1a7f1bdc4bd062282a185` (tree `f97c4969d7ddb93eed75c80a4936fc05fab8e2eb`).
