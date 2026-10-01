# mcp/src/agents_remember/certification/replay/scenarios.py

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

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root. The governing task artifacts (the CCR-R17 approved replay protocol requirement packet and the 17_measured-replay-and-reduction leaf doc) define the seventeen mandatory acceptance scenarios; task artifact paths are not repo-relative citations, so these facts are recorded as prose here.

- The replay scenario catalog records each required scenario and its expected views. [1]
- Every mandatory replay scenario is evaluated against measured evidence in declared order. [2]

### Repo-Internal References

- Scenarios consume the measured evidence envelope and rail placement vocabulary. [3]
- Certification contract findings carry typed refusal details. [4]
- Rail identity binds its declared rail id and version. [5]
- Unknown scenario ids raise the shared certification contract error. [6]
- The comparison builder evaluates all scenarios over measured evidence. [7]
- The facade exports replay scenarios and their evaluators alongside shared replay contracts. [8]

### Cross-Repo References

No cross-repository implementation boundary is owned here.

Acceptance projection stays repository-neutral over the measured evidence envelope.
