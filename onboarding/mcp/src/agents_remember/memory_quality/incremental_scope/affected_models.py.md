# mcp/src/agents_remember/memory_quality/incremental_scope/affected_models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/incremental_scope/affected_models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:23:26+00:00 |
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

CCR-R07@v3 (requirements/CCR-R07-v3-incremental-affected-closure-validation.md,
"Preserved Behavior"; "Exclusions And Forbidden Overreach") requires incremental
validation not to waive the final full Gate-5 pass and forbids safe-full fallback or
caller-declared completeness.


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The plan binds one unit per incremental document/checker and the exact Gate 1-4 prefix. | `AffectedClosurePlan`; `AffectedUnitPlan` | mcp/src/agents_remember/memory_quality/incremental_scope/affected_models.py:117-246; mcp/src/agents_remember/memory_quality/incremental_scope/affected_models.py:44-90 |
| Results and reuse are terminal, partitioned, and aggregate blocked > fail > pass. | `AffectedClosureResult`; `SubresultReusePlan` | mcp/src/agents_remember/memory_quality/incremental_scope/affected_models.py:332-405; mcp/src/agents_remember/memory_quality/incremental_scope/affected_models.py:303-329 |
| The planner compiles these models; the executor consumes them. | `compile_affected_closure_plan`; `execute_affected_closure` | mcp/src/agents_remember/memory_quality/incremental_scope/affected_planning.py:65-130; mcp/src/agents_remember/memory_quality/incremental_scope/affected_execution.py:183-250 |
| The declared affected-closure plan is the production shape authority; deleted tests do not establish a current validation run. | `AffectedClosurePlan` | mcp/src/agents_remember/memory_quality/incremental_scope/affected_models.py:117-246 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Gate certificate identities come from the R21 certificate owners inside the same repository. | `GateCertificateIdentity` | mcp/src/agents_remember/certification/certificate_models.py:100-102 |

## Update History
- 2026-09-06T22:41:21+00:00: Generated citation repair: `GateCertificateIdentity` repointed to mcp/src/agents_remember/certification/certificate_models.py:100-102. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-06T00:23:26+00:00 — L30 recovery: Corrected incoming references and schema ownership against the reviewed candidate; unchanged source retains its genuine verification stamp.

- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): rewrote the task-artifact Docs References row as prose.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 993953760ef65c4670a40c63a6d6ef0fbcddbe3b (CCR-R07@v3/L07): created the card for the new R07 affected-closure contract models; no prior sidecar existed.
