# mcp/src/agents_remember/memory_quality/incremental_scope/__init__.py

## Governing Overview

[memory quality overview](../overview.md)

## Purpose

Public facade for retained scope observations, exact candidate identity, per-unit result/store contracts, typed refusal vocabulary and checker policy registry. It adds no planner, dependency compiler, owner adapter or affected-closure executor.

## Code Commentary

### Logic

`__all__` fixes the public set: `AffectedUnitResult`, `ContentAddressedSubresultStore`, `SubresultStorePolicy`, `ContractScopeAuthority`, task/task-pair/Git-delta observers, `ScopeCandidateIdentity`, `ScopeFailure`, `ScopeUnprovenError`, `GateFiveClosureRefusedError`, and checker registry/version functions.

### Conventions

Consumers can import the retained observations, per-unit store/result contracts and typed errors through this facade without acquiring a removed plan or execution API.

### Invariants And Boundaries

- The facade adds no fallback or full-scan behavior; it only re-exports retained owned contracts.
- Typed fail-closed errors remain public.
- No aggregate execution/finalization flags are attributed to the surviving per-unit result; the facade is not an acceptance executor.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root. The governing task artifacts
below close the informational gap for the affected-closure surface.

CCR-R07@v3 (requirements/CCR-R07-v3-incremental-affected-closure-validation.md,
"Normative Requirement"; "Preserved Behavior") requires that after green Gate 1-4
certificates, Gate 5 derives a complete content-addressed affected closure, executes only
that closure, and retains unchanged valid subresults; incremental validation never waives
the final full Gate-5 pass. Leaf L07 (07_incremental-affected-closure-validation.md,
"Commit 993953760ef65c4670a40c63a6d6ef0fbcddbe3b") landed this affected-closure surface at
commit 993953760ef6.

This facade no longer exports the former affected-closure planner/executor. That source-surface deletion is not evidence that CCR-R07 was semantically retired.


### Repo-Internal References

- The facade retains per-unit result/store contracts, candidate/task/Git observers, typed errors and the checker registry. [1]

- The typed Gate-5 closure refusal is part of the public error surface. [2]

- `__all__` fixes the complete public package surface. [3]


### Cross-Repo References

No cross-repository implementation boundary is owned here.

Task and Git observation enters through the retained candidate module; no external boundary is exercised by the facade.*** End Patch
