# mcp/src/agents_remember/memory_quality/incremental_scope/__init__.py

## Governing Overview

[memory quality overview](../overview.md)

## Purpose

Public facade of the content-addressed, fail-closed incremental memory dependency scope package.
Since CCR-R07@v3 (commit 993953760ef6) it exposes the full affected-closure surface — planning,
execution, subresult storage, and the typed Gate-5 closure refusal — beside the R06 scope
observation/compilation vocabulary, so Gate-5 consumers can depend on one stable package boundary.

## Code Commentary

### Logic

The module re-exports the R07 affected-closure modules
(`affected_execution` lines 3-9, `affected_models` line 10, `affected_planning` line 11,
`subresult_store` line 27), the R06 scope observers/builders (`candidate`, `compiler`,
`owners`, `registry`, `models`), and the typed errors (now including
`GateFiveClosureRefusedError` from `errors`, line 19). `__all__` (`__init__.py:29-57`) fixes
the public set.

### Conventions

One facade per package: consumers import the compiled plan/execution/result functions and the
scope observations without reaching into package-private helpers.

### Invariants And Boundaries

- The facade does not add fallback or full-scan behavior; it only re-exports owned contracts.
- Incremental execution never promotes itself to final acceptance
  (`acceptanceEligible`/full-final flags are fixed by the models, not the facade).
- Typed fail-closed errors are part of the public surface.

### Todos

Connecting this package to the Gate-5 execution rail and the R08 final full certification remains
owned by later lifecycle layers.

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


### Repo-Internal References

- The facade re-exports the R07 affected-closure planner, models, executor, and store. [1]
- The typed Gate-5 closure refusal is part of the public error surface. [2]
- `__all__` fixes the complete public package surface. [3]

### Cross-Repo References

No cross-repository implementation boundary is owned here.

Scope observation enters through R06 owners; no external boundary is exercised by this facade.
