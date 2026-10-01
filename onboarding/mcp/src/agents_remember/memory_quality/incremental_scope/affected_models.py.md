# mcp/src/agents_remember/memory_quality/incremental_scope/affected_models.py

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
Its incremental document population excludes nodes marked `historical Git tree member`, so
deleted or renamed predecessor cards remain visible as dependency inputs without becoming
current execution units (`_incremental_documents`, `affected_models.py:221-228`).
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

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root. The governing task artifact
below closes the informational gap for the plan/result semantics.

CCR-R07@v3 (requirements/CCR-R07-v3-incremental-affected-closure-validation.md,
"Preserved Behavior"; "Exclusions And Forbidden Overreach") requires incremental
validation not to waive the final full Gate-5 pass and forbids safe-full fallback or
caller-declared completeness.


### Repo-Internal References

- The plan binds one unit per incremental document/checker and the exact Gate 1-4 prefix. [1]
- Results and reuse are terminal, partitioned, and aggregate blocked > fail > pass. [2]
- The planner compiles these models; the executor consumes them. [3]
- The declared affected-closure plan is the production shape authority; deleted tests do not establish a current validation run. [4]

| Historical Git-tree members remain dependency inputs and are excluded from current unit population. | `_incremental_documents` | mcp/src/agents_remember/memory_quality/incremental_scope/affected_models.py:221-228 |

### Cross-Repo References

No cross-repository implementation boundary is owned here.

- Gate certificate identities come from the R21 certificate owners inside the same repository. [5]
