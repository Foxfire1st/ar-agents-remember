# mcp/tests/test_replay_scenario_branches.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_replay_scenario_branches.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T22:23+02:00 |
| lastVerifiedCommitHash | `e84c004c37a4bad082e1a7f1bdc4bd062282a185` |
| lastVerifiedCommitDate | 2026-09-04T22:06:05+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Fully standalone CCR-R17 (leaf 260831-CCR-L17) scenario branch-matrix forcing suite. Every mandatory acceptance scenario in `certification/replay/scenarios.py` is exercised through its green, red, and not-applicable arms so the deterministic evaluators cannot hide a cold branch. Nothing is shared with another suite; all evidence is constructed here.

## Code Commentary

### Logic

- The suite walks each scenario's preconditions and outcomes: e.g. scenario 02 arms (`test_scenario_02_no_red_catalog_is_not_applicable`, lines 142-146; `test_scenario_02_no_failed_rail_is_not_applicable`, lines 147-157; `test_scenario_02_green_red_and_not_applicable_arms`, lines 158-222), scenario 09 repair arms (lines 360-473, including `test_scenario_09_full_repair_is_green`, lines 448-473), and scenario 16 parity arms (lines 689-761, including `test_scenario_16_shared_contract_two_repositories_is_green`, lines 734-747).
- Zero-start helpers are forced directly (`test_scenario_05_gate_three_started_after_gate_two_red_is_red`, lines 824-835; `test_scenario_07_gate_four_started_after_gate_three_red_is_red`, lines 836-848; `test_scenario_08_gate_five_started_after_gate_four_red_is_red`, lines 849-861; `test_zero_start_not_applicable_when_gate_not_red`, lines 862-867; `test_zero_start_green_when_no_later_starts`, lines 868-878).
- The migrated-profile and catalog helpers (`test_reference_profile_traversal_returns_none_when_absent`, lines 881-885; `test_acceptance_catalog_is_complete`, lines 888-891; `test_evaluate_returns_typed_outcome`, lines 893-895) pin the closed seventeen-scenario catalog and typed outcomes.

### Conventions

Standalone per the evidence-lifecycle isolation rule; imports no pre-existing mcp/tests support module.

### Invariants And Boundaries

- Every scenario arm (green/red/not-applicable) is exercised; no evaluator branch stays cold.
- A not-applicable or red outcome always carries its typed finding; a green never does.
- The scenario catalog stays exactly seventeen entries.

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
| The scenario evaluators under test. | `evaluate_replay_scenario`; `evaluate_all_replay_scenarios` | mcp/src/agents_remember/certification/replay/scenarios.py:177-185; mcp/src/agents_remember/certification/replay/scenarios.py:188-192 |
| The acceptance scenario catalog under test. | `REPLAY_ACCEPTANCE_SCENARIOS` | mcp/src/agents_remember/certification/replay/scenarios.py:34-174 |
| The evidence envelope and profile/placement vocabulary used to build scenarios. | `ReplayScenarioEvidence`; `ReplayProfileSnapshot`; `ReplayRailPlacement` | mcp/src/agents_remember/certification/replay/models.py:362-385; mcp/src/agents_remember/certification/replay/models.py:350-359; mcp/src/agents_remember/certification/replay/models.py:313-340 |
| The explicit unit-regression lane registration. | "mcp/tests/test_replay_scenario_branches.py" | mcp/tests/test-evidence-lanes.toml:160-160 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Same-repository forcing suite; nothing crosses repositories. | - | - |

## Update History

- 2026-09-05T06:39:59+00:00 — L31 scoped citation curation against frozen ea359649: repaired anchor grammar and exact source coordinates while preserving the current behavioral claims. No content impact; source verification metadata was not advanced.

- 2026-09-04T22:23+02:00 - 260831-CCR-L17 Gate-5 memory pass: created for the new CCR-R17 scenario branch-matrix forcing suite (green/red/not-applicable arms for all seventeen scenarios). Verification stamp is the full leaf code commit `e84c004c37a4bad082e1a7f1bdc4bd062282a185` (tree `f97c4969d7ddb93eed75c80a4936fc05fab8e2eb`).
