# mcp/tests/test_replay_scenarios_and_compare.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_replay_scenarios_and_compare.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:42:13+00:00 |
| lastVerifiedCommitHash | `e84c004c37a4bad082e1a7f1bdc4bd062282a185` |
| lastVerifiedCommitDate | 2026-09-04T22:06:05+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Fully standalone CCR-R17 (leaf 260831-CCR-L17) acceptance-scenario and comparison-report forcing suite. The seventeen mandatory acceptance scenarios are projected over measured replay evidence only; scenarios that need a pair or a repository profile return not-applicable when that evidence is absent and never fabricate a green. The comparison-report builder is proven end-to-end: exact leg identities, comparability binding, ordered scenario outcomes, and digest verification. Numeric reduction thresholds are out of approved scope and are never asserted.

## Code Commentary

### Logic

- Catalog and projection basics (`test_acceptance_catalog_holds_seventeen_scenarios`, lines 140-147; `test_evaluate_all_returns_ordered_machine_readable_outcomes`, lines 150-158; `test_unknown_scenario_refuses`, lines 161-164).
- Representative scenario proofs (`test_scenario_01_two_independent_gate_one_failures_in_one_catalog`, lines 167-195; `test_scenario_03_file_size_fault_produces_zero_later_starts`, lines 198-221; `test_scenario_05_gate_two_failure_blocks_later_gates`, lines 224-234; `test_scenario_09_memory_repair_reuses_gates_one_to_four`, lines 237-261; `test_scenario_10_code_change_invalidates_every_gate`, lines 264-292; `test_scenario_16_repository_generic_profiles_share_contract`, lines 295-326; `test_scenario_17_reference_profile_places_rails_by_class`, lines 329-350).
- Comparison-report proofs (`test_comparison_report_binds_identities_and_scenarios`, lines 353-386; `test_comparison_report_refuses_when_pair_incomparable`, lines 389-408).

### Conventions

Standalone per the evidence-lifecycle isolation rule; imports no pre-existing mcp/tests support module.

### Invariants And Boundaries

- All seventeen scenarios project in fixed order to machine-readable outcomes.
- Scenarios whose evidence is absent return not-applicable rather than fabricating green.
- The comparison report binds leg freezes and always digests its full content.

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
| The scenario projection surface under test. | `evaluate_replay_scenario`; `evaluate_all_replay_scenarios`; `REPLAY_ACCEPTANCE_SCENARIOS` | mcp/src/agents_remember/certification/replay/scenarios.py:177-185; mcp/src/agents_remember/certification/replay/scenarios.py:188-192; mcp/src/agents_remember/certification/replay/scenarios.py:34-174 |
| The comparison builder under test. | `build_replay_comparison_report`; `ReplayComparisonInput`; `ReplayComparisonReport` | mcp/src/agents_remember/certification/replay/compare.py:72-96; mcp/src/agents_remember/certification/replay/compare.py:34-44; mcp/src/agents_remember/certification/replay/compare.py:47-69 |
| The measured evidence envelope used to build scenario inputs. | `ReplayScenarioEvidence`; `RunMeasurement` | mcp/src/agents_remember/certification/replay/models.py:362-385; mcp/src/agents_remember/certification/replay/models.py:255-286 |
| The explicit unit-regression lane registration. | "mcp/tests/test_replay_scenarios_and_compare.py" | mcp/tests/test-evidence-lanes.toml:163-163 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Same-repository forcing suite; nothing crosses repositories. | - | - |

## Update History

- 2026-09-06T00:42:13+00:00 — Gate-5 citation repair: re-read the cited evidence-lane member and its declared classification and corrected its incoming range. Existing source verification provenance is retained.

- 2026-09-05T06:39:59+00:00 — L31 scoped citation curation against frozen ea359649: repaired anchor grammar and exact source coordinates while preserving the current behavioral claims. No content impact; source verification metadata was not advanced.

- 2026-09-04T22:23+02:00 - 260831-CCR-L17 Gate-5 memory pass: created for the new CCR-R17 scenario and comparison-report forcing suite (seventeen ordered projections and the digest-bound pair report). Verification stamp is the full leaf code commit `e84c004c37a4bad082e1a7f1bdc4bd062282a185` (tree `f97c4969d7ddb93eed75c80a4936fc05fab8e2eb`).
