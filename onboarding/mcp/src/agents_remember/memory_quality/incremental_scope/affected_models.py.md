# mcp/src/agents_remember/memory_quality/incremental_scope/affected_models.py

## Governing Overview

[memory quality overview](../overview.md)

## Purpose

Owns strict frozen per-unit identity and terminal result contracts: `ClosureDependencyIdentity`, `AffectedUnitPlan`, `AffectedUnitResult`, and `UnitStatus`. Canonical dependencies, selected-document identity and evidence/result self-digests permit dependency-exact per-unit records; they do not assemble an affected closure or authorize finalization.

## Code Commentary

### Logic

`ClosureDependencyIdentity` requires a nonempty node ID, content digest, authority namespace and validator version. `AffectedUnitPlan` requires one canonical relative `.md` path, nonempty checker/version/owner identities, bounded dependency and edge tuples, exact code/source-index/registry identities and a self-verifying `unitDigest`.

Dependencies and dependency edges must be unique and sorted; dependencies exclude the checked node. `AffectedUnitResult` binds pass to zero findings and fail to nonzero findings; blocked results have zero checked files and other results exactly one. Evidence and result digests must equal their canonical payloads. Aggregate plans/results, member populations, reuse partitions and pending-full factories are absent.

### Conventions

Every model is strict and frozen; digests are computed over the same canonical JSON spelling used
by validation, so a model that does not self-verify refuses construction.

### Invariants And Boundaries

- Canonical `.md` identity, dependency/edge populations and unit/evidence/result digests are self-verified.
- Per-unit status agrees with finding count and selected-document count.
- These models do not supply aggregate readiness or finalization flags.

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

This module now retains per-unit identity and result models rather than an aggregate closure API. Its reduced exports do not themselves retire the requirement above.


### Repo-Internal References

- AffectedUnitPlan verifies canonical relative .md identity, exact canonical dependency/edge sets and self-digest. [1]

- AffectedUnitResult verifies terminal status, finding/selected-file counts, evidence digest and result digest without aggregate readiness. [2]






### Cross-Repo References

No cross-repository implementation boundary is owned here.

- GateCertificateIdentity remains owned by the certification certificate models; the surviving per-unit models no longer import it for an aggregate closure. [5]
