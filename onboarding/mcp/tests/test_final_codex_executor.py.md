# mcp/tests/test_final_codex_executor.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_final_codex_executor.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T22:45+02:00 |
| lastVerifiedCommitHash | `54ff803a05209e06f732f2de1f90e2a71a069e08` |
| lastVerifiedCommitDate | 2026-09-04T22:31:30+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Standalone CCR-R14 run-control tests for the two-fresh no-retry certifying runs (leaf 260831-CCR-L14, code commit 54ff803a). Covers admission ordering (R12 Gates 1-3 green first against the exact frozen plan), the trusted R12 authority freeze with live-owner registration, two fresh certifying repetitions with distinct client/process identities and retryCount zero, no-compensation red aggregates, typed hard failures, teardown and process-cleanliness records, abort, exact-owner release, in-flight and authority-transition refusals, and the retry-disabled same-plan barrier. Every scenario runs zero Dagger commands: engine inspection is a fake and the authority registry is a temporary directory. Fully standalone.

## Code Commentary

### Logic

`RecordingRunner` (lines 58-120) and `ScriptedRunner` (lines 122-175) inject zero-Dagger scenario executions; `hard_failure` (lines 177-208) builds typed infrastructure/parser failures; `make_engine` (lines 209-222) constructs the engine over a temporary authority registry; `make_spec` (lines 223-237) and `green_gates` (lines 238-243) supply the run spec and predecessor manifests. `FinalCodexExecutorAdmissionTests` (lines 244-332) covers admission only after Gates 1-3 green, typed admission refusal on a missing host, ambient-conflict refusal before any scenario step, authority-transition barrier blocking a fresh run, in-flight blocking of a second attempt, and fresh-admission owner release when the store refuses reservation. `FinalCodexExecutorRunTests` (lines 333-464) covers two fresh runs binding the frozen authority, a one-pass/one-fail red aggregate that cannot certify, typed hard failure still releasing the exact owner, abort with teardown evidence and no pass, terminalization releasing only the final-codex owner, retry disabled for the exact same plan, and never creating a private runner or store.

### Conventions

All execution crosses the R12 trusted authority; every refusal is a typed `CertificationContractError` and every hard failure stays a hard failure with no fabricated pass.

### Invariants And Boundaries

- Admission runs only after the exact candidate's certifying Gate-1..3 manifests are green against the frozen plan.
- Exactly two fresh independent certifying repetitions; one pass never compensates the other.
- Every terminalization releases only the run's own runtime owner.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this memory root. CCR-R14@v3 (approved packet, leaf 14_final-real-codex-certification) requires every Dagger-backed certifying repetition to bind the exact R12 host authority; task artifact paths are not repo-relative citations, so clauses are recorded as prose.

| Finding | Anchor | Source |
| --- | --- | --- |
| The two-fresh run control binds the frozen R12 authority and never provisions. | `FinalCodexExecutorRunTests` | mcp/tests/test_final_codex_executor.py:333-464 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exercises the final-codex run controller. | `FinalCodexExecutionEngine`; `build_final_codex_run_spec` | mcp/src/agents_remember/worktrees/modules/quality/final_codex_executor.py:179-600; mcp/src/agents_remember/worktrees/modules/quality/final_codex_executor.py:612-640 |
| The fake inspector mirrors the R12 engine-inspection protocol. | `EngineInspectionProtocol` | mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:1-120 |
| Lane readiness comes from the projection contract. | `project_final_codex_lane` | mcp/src/agents_remember/certification/final_codex/projection.py:88-113 |

## Cross-Repo References

No cross-repository evidence is required; the R12 host authority is exercised through its module boundary only.

| Finding | Anchor | Source |
| --- | --- | --- |
| The authority registry is a temporary directory in every case; no external engine runs. | `make_engine` | mcp/tests/test_final_codex_executor.py:209-222 |

## Update History

- 2026-09-04T22:45+02:00 - 260831-CCR-L14 Gate-5 memory pass: created this card for the new standalone CCR-R14 run-control suite delivered in code commit 54ff803a; anchors and ranges derived from the current worktree source and pinned to that commit (tree aff2e268968397ab8db042a782652957a3600dda).
