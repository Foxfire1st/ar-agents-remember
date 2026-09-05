# mcp/tests/test_diagnostic_executor.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_diagnostic_executor.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T17:50+02:00 |
| lastVerifiedCommitHash | `4ba18bb23ba90e201bb37341d61c0efc64161fcf` |
| lastVerifiedCommitDate | 2026-09-04T17:23:11+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Standalone CCR-R13 diagnostic run-control tests (leaf 260831-CCR-L13, code commit 4ba18bb2). It covers admission ordering (R12 Gates 1-3 green first), the trusted R12 authority freeze with live-owner registration, one-replication terminalization (pass/fail/aborted/hard-failure), exact-owner release, in-flight and authority-transition refusals, frozen-snapshot retry, R16 diagnostic telemetry envelopes, and diagnostic-namespace isolation. Every scenario runs zero Dagger commands: engine inspection is a fake and the authority registry is a temporary directory.

## Code Commentary

### Logic

The suite is registered in the `integration` lane. Its scaffolding rebuilds the canonical registry and gate manifests (`RailSpec`/`_rail`/`scenario_registry`/`certifying_plan`/`manifest_for`, lines 108-266; `green_gates`, lines 269-271), fakes engine inspection (`FakeInspector`, lines 274-303), records scenario runs (`RecordingRunner`, lines 321-379), raises typed hard failures (`hard_failure`, lines 382-409), and assembles an engine/registry/store triple (`make_engine`, lines 412-435) plus a run spec (`make_spec`, lines 438-447).

`DiagnosticExecutorAdmissionTests` (lines 454-559) covers: admission only after the exact certifying Gates 1-3 are green and complete (lines 455-473); diagnostic-altitude evidence refused (lines 475-482); candidate mismatch refused (lines 484-497); a missing host declaration as a typed refusal (lines 499-508); ambient conflict refused before the scenario starts (lines 510-517); an authority-transition barrier blocking a fresh diagnostic (lines 519-534); an in-flight diagnostic blocking a second attempt (lines 536-545); and fresh-owner release when the reservation refuses (lines 547-559).

`DiagnosticExecutorRunTests` (lines 562-769) covers: one pass replication binding the frozen authority with exact-owner release and R16 telemetry (lines 563-606); scenario failure being non-certifying and blocking the lane (lines 608-624); typed hard failures releasing the exact owner (lines 626-647); abort with teardown evidence, no pass, and blocking (lines 649-674); one-replication-per-attempt enforcement (lines 676-686); retry appending a new result on the frozen snapshot (lines 688-713); terminalization releasing only the diagnostic owner while a foreign closeout owner stays live on the shared runner/store (lines 715-753); and proof that no private runner or store is ever created (lines 755-769).

### Conventions

Every scenario runs zero real Dagger commands; the authority registry is a temporary directory and the layer store is never deleted or retired.

### Invariants And Boundaries

- Admission requires the exact complete certifying Gate 1-3 green manifests for the candidate.
- Each attempt executes at most one replication; retry appends a new result and never promotes.
- Terminalization releases only the attempt's own runtime owner.
- The frozen R12 snapshot is bound into every attempt/result; no private runner/store is ever created.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this memory root. CCR-R13@v2 (frozen digest f0387b1627c5e8f48073b55d40dc362065e46943c5688f0f863fddb480770d3a) and the R12@v4 authority contract govern the run control; task artifact paths are not repo-relative citations, so clauses are recorded as prose.

| Finding | Anchor | Source |
| --- | --- | --- |
| A diagnostic may run only after the exact candidate's R12 Gates 1-3 are green and every run binds the trusted frozen authority. | `test_admission_runs_only_after_gates_1_3_are_green`; `test_one_pass_replication_binds_the_frozen_authority` | mcp/tests/test_diagnostic_executor.py:455-473; mcp/tests/test_diagnostic_executor.py:563-606 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exercises the diagnostic run controller directly. | `DiagnosticExecutionEngine` | mcp/src/agents_remember/worktrees/modules/quality/diagnostic_executor.py:176-563 |
| Fakes the R12 engine inspector and authority registry so no engine is contacted. | `FakeInspector`; `AuthorityRegistry` | mcp/tests/test_diagnostic_executor.py:274-303; mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:588-833 |
| Asserts R16 diagnostic telemetry envelope shape on started/terminal events. | `RecordingRunner`; `compile_diagnostic_started` | mcp/src/agents_remember/certification/telemetry/adapters.py:433-448; mcp/tests/test_diagnostic_executor.py:321-379 |
| Reusable builders are imported by the diff-coverage closure module. | `test_diagnostic_executor` | mcp/tests/test_diagnostic_diff_coverage.py:63-79 |

## Update History

- 2026-09-05T06:39:59+00:00 — L31 scoped citation curation against frozen ea359649: repaired anchor grammar and exact source coordinates while preserving the current behavioral claims. No content impact; source verification metadata was not advanced.
- 2026-09-05T06:24:16+00:00: Generated citation repair: `RecordingRunner`; `compile_diagnostic_started` repointed to mcp/tests/test_diagnostic_executor.py:321-379; mcp/src/agents_remember/certification/telemetry/adapters.py:433-448. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-04T17:50+02:00 - 260831-CCR-L13 Gate-5 memory pass: created this card for the new standalone CCR-R13 run-control suite delivered in code commit 4ba18bb2; anchors and ranges derived from the current worktree source and pinned to that commit (tree 631145bf3e0d5899b1dcbccf8c0d4a8257821f0d).
