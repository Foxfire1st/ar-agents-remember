# mcp/src/agents_remember/certification/replay/scenarios.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/replay/scenarios.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T22:23+02:00 |
| lastVerifiedCommitHash | `e84c004c37a4bad082e1a7f1bdc4bd062282a185` |
| lastVerifiedCommitDate | 2026-09-04T22:06:05+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Certification contract overview](../overview.md)

## Purpose

Owns the CCR-R17 (leaf 260831-CCR-L17) seventeen mandatory acceptance scenarios and their deterministic projection over measured replay evidence. Each scenario is a pure function of the evidence envelope (a treatment run and, where the scenario is inherently a comparison, its baseline): green only when the measured export proves the scenario, red when the export contradicts it, and not-applicable when the scenario precondition never occurred. Outcomes never carry numeric reduction thresholds.

## Code Commentary

### Logic

- `REPLAY_ACCEPTANCE_SCENARIOS` (lines 34-174) fixes the seventeen ordered `ReplayScenarioExpectation` records (r17-scenario-01 through r17-scenario-17), each with a title, requirement, and views. The scenarios cover two failing Gate-1 rails in one catalog (01), prerequisite-only blocking (02), file-size failure with zero later starts (03), pyright failure without hiding companion results (04), Gate-2 failure with zero Gate 3-5 starts (05), Gate-3 offender reporting (06), Gate-3/Gate-4 failure zero-start cascades (07/08), memory-only repair reusing Gates 1-4 and re-running Gate 5 (09), code-change invalidation of Gates 1-5 (10), per-gate profile/config closure invalidation (11), metadata changes invalidating nothing (12), interrupted finalization resuming with zero unchanged gate starts (13), identical canonical rail definitions pre-commit and closeout (14), no legacy/fallback/safe-full/diagnostic/stale evidence certifying (15), repository-owned Gate 1-4 profile parity under one framework contract (16), and the Agents Remember migrated profile preserving every current hard rail (17).
- `evaluate_replay_scenario` (lines 177-185) looks the scenario id up in `_EVALUATORS` (lines 608-626) and refuses unknown ids; `evaluate_all_replay_scenarios` (lines 188-192) projects all seventeen in fixed order.
- Shared helpers `_not_applicable` / `_red` / `_finding` (lines 195-213) build typed scenario outcomes and findings (`not-applicable` and `scenario-contradicted` codes).
- Individual evaluators (lines 215-533) implement each scenario: e.g. `_evaluate_01` (lines 215-225) requires at least two distinct failed Gate-1 rail keys in one complete catalog; `_evaluate_09` (lines 343-368) proves the memory repair reuses the exact green Gates 1-4 certificates and re-runs Gate 5; `_evaluate_17` (lines 524-533) checks the migrated reference profile against `_scenario_17_missing` (lines 536-548).
- Cross-cutting helpers `_later_gates_zero_start` (lines 554-570), `_placements` (lines 573-580), `_reference_profile` (lines 584-591), and `_class_rail` (lines 594-605) back the red/not-applicable arms shared by scenarios 05/07/08, 04, 17, and 16/17.

### Conventions

Scenario expectations and outcomes use the models vocabulary; evaluators are pure and deterministic and never fabricate a green when the evidence is absent.

### Invariants And Boundaries

- The catalog fixes exactly seventeen scenarios; evaluation order is stable.
- A scenario is not-applicable when its precondition never occurred and red when the export contradicts it; no fallback outcome exists.
- Outcomes carry typed findings only; numeric reduction thresholds never appear.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this memory root. The governing task artifacts (the CCR-R17 approved replay protocol requirement packet and the 17_measured-replay-and-reduction leaf doc) define the seventeen mandatory acceptance scenarios; task artifact paths are not repo-relative citations, so these facts are recorded as prose here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Every mandatory acceptance scenario is projected over measured evidence only, green/red/not-applicable. | `REPLAY_ACCEPTANCE_SCENARIOS`; `evaluate_all_replay_scenarios` | mcp/src/agents_remember/certification/replay/scenarios.py:34-174; mcp/src/agents_remember/certification/replay/scenarios.py:188-192 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Scenarios consume the measured evidence envelope and rail placement vocabulary. | `ReplayScenarioEvidence`; `RunMeasurement`; `ReplayRailPlacement`; `ReplayProfileSnapshot` | mcp/src/agents_remember/certification/replay/models.py:362-385; mcp/src/agents_remember/certification/replay/models.py:255-286; mcp/src/agents_remember/certification/replay/models.py:313-340; mcp/src/agents_remember/certification/replay/models.py:350-359 |
| Findings reuse the shared typed certification finding contract. | `CertificationContractFinding`; `RailIdentity` | mcp/src/agents_remember/certification/models.py:169-172 |
| Unknown scenario ids raise the shared certification contract error. | `CertificationContractError` | mcp/src/agents_remember/errors.py:22-31 |
| The comparison builder evaluates all scenarios over measured evidence. | `evaluate_all_replay_scenarios` | mcp/src/agents_remember/certification/replay/compare.py:72-96 |
| The public subpackage facade re-exports the scenario surface. | `replay.__all__` | mcp/src/agents_remember/certification/replay/__init__.py:56-88 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Acceptance projection stays repository-neutral over the measured evidence envelope. | - | - |

## Update History

- 2026-09-04T22:23+02:00 - 260831-CCR-L17 Gate-5 memory pass: created this card for the new CCR-R17 seventeen-scenario projector delivered in code commit `e84c004c37a4bad082e1a7f1bdc4bd062282a185` (tree `f97c4969d7ddb93eed75c80a4936fc05fab8e2eb`).
