# mcp/src/agents_remember/memory_quality/incremental_scope/affected_models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/incremental_scope/affected_models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `993953760ef65c4670a40c63a6d6ef0fbcddbe3b`|
| lastVerifiedCommitDate | 2026-09-03T02:13:10+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory quality overview](../overview.md)

## Purpose

Owns the immutable, content-addressed contracts of the CCR-R07 affected closure: one
`AffectedClosurePlan` for the proven incremental subset, `AffectedUnitPlan`/result records for
each checker/document unit, explicit member populations, the unit-level reuse plan, the aggregate
`AffectedClosureResult`, and the pending final-full visibility — all self-verifying and
fail-closed so incremental proof can never masquerade as final certification.

## Code Commentary

### Logic

`CheckerExecutionPolicy` (`affected_models.py:26-32`) and `ClosureDependencyIdentity`
(`affected_models.py:35-41`) fix one R07 execution/identity contract; `AffectedUnitPlan`
(`affected_models.py:44-90`) validates one canonical relative `.md` document, requires unique
canonical dependencies that exclude the checked node, and self-verifies `unitDigest`.
`AffectedMemberPlan` (`affected_models.py:93-106`) distinguishes check-target members from
dependency inputs; `PendingFinalFullCheck` (`affected_models.py:109-114`) keeps R06 full-only
checkers visible. `AffectedClosurePlan` (`affected_models.py:117-246`) requires members to
equal the exact R06 selected population, units to equal every incremental document-by-checker
pair, the exact green Gate 1-4 certificate prefix, canonical subrecord coherence, and
`acceptanceEligible=False`/`fullFinalRequired=True`, and self-verifies `planDigest`.
`AffectedUnitResult` (`affected_models.py:249-278`) binds status to finding count and the
blocked state to zero checked files; `AffectedMemberResult` (`affected_models.py:281-300`)
derives disposition/status from its units; `SubresultReusePlan` (`affected_models.py:303-329`)
requires reused and executed populations to partition the plan. `AffectedClosureResult`
(`affected_models.py:332-405`) aggregates exactly the planned units, sets
`incrementalMemoryReady` iff every unit passes, computes `terminalStatus` by blocked > fail >
pass, and keeps `closeoutReady=False`. `dependency_identity` and `full_only_disposition` (`affected_models.py:416-426`) are the compilers' helper factories.

### Conventions

Every model is strict and frozen; digests are computed over the same canonical JSON spelling used
by validation, so a model that does not self-verify refuses construction.

### Invariants And Boundaries

- The closure result and its plan pin the exact same unit population; reused and executed digests
  partition the plan.
- `acceptanceEligible` and `closeoutReady` are hard `False`; `fullFinalRequired` is hard
  `True` — incremental closure can never stand in for R08 final full certification.
- Pending full-only checkers are never hidden or converted to green rails.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured for this memory root. The governing task artifact
below closes the informational gap for the plan/result semantics.

| Finding | Anchor | Source |
| --- | --- | --- |
| CCR-R07@v3 required behavior and exclusions: incremental validation does not waive the final full Gate-5 pass; no safe-full fallback or caller-declared completeness. | "Preserved Behavior"; "Exclusions And Forbidden Overreach" | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R07-v3-incremental-affected-closure-validation.md |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The plan binds one unit per incremental document/checker and the exact Gate 1-4 prefix. | `AffectedClosurePlan`; `AffectedUnitPlan` | mcp/src/agents_remember/memory_quality/incremental_scope/affected_models.py:117-246; mcp/src/agents_remember/memory_quality/incremental_scope/affected_models.py:44-90 |
| Results and reuse are terminal, partitioned, and aggregate blocked > fail > pass. | `AffectedClosureResult`; `SubresultReusePlan` | mcp/src/agents_remember/memory_quality/incremental_scope/affected_models.py:332-405; mcp/src/agents_remember/memory_quality/incremental_scope/affected_models.py:303-329 |
| The planner compiles these models; the executor consumes them. | `compile_affected_closure_plan`; `execute_affected_closure` | mcp/src/agents_remember/memory_quality/incremental_scope/affected_planning.py:65-130; mcp/src/agents_remember/memory_quality/incremental_scope/affected_execution.py:171-238 |
| Model-edge proofs cover plan/result/reuse refusal shapes. | `test_r07_closure_plan_model_refuses_incomplete_or_rebound_populations`; `test_r07_result_and_reuse_models_refuse_inconsistent_exact_state`; `test_r07_aggregate_model_refuses_incomplete_or_inconsistent_result` | mcp/tests/test_memory_incremental_scope_model_edges.py:660-730; mcp/tests/test_memory_incremental_scope_model_edges.py:741-785; mcp/tests/test_memory_incremental_scope_model_edges.py:786-843 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Gate certificate identities come from the R21 certificate owners inside the same repository. | `GateCertificateIdentity` | mcp/src/agents_remember/certification/certificate_models.py |

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 993953760ef65c4670a40c63a6d6ef0fbcddbe3b (CCR-R07@v3/L07): created the card for the new R07 affected-closure contract models; no prior sidecar existed.
