# dashboard/src/data/taskHierarchy.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Cover normalized parent-task matching and the per-series-list identity cache used by task hierarchy
rendering.

## Code Commentary

### Logic

Fixtures exercise relative path normalization, deterministic first-series and creation-order matches,
document-id override, master/unknown exclusion, and the intentional behavior that a fresh series-list
array observes changed refs while the same array retains its cached index.

### Conventions

The tests build only the projection fields required by the pure lookup helpers. The local `ref`
factory is typed `SeriesSubTaskNode` — these rows feed `series.subTasks`, so they are SERIES rows.
That matters for the creation-order case specifically: it sets `createdAt`, and the mirror no longer
declares that field on `TaskSubTaskRefNode` (the master row model the server never stamps), so the
fixture is now typed against a model that can actually carry what the case asserts on. There is no
shared builder for `SeriesNode`/`SeriesSubTaskNode` in `test/fixtures/wire.ts`; these two factories
stay local and are checked directly against `types/projection.ts`.

### Invariants And Boundaries

The cache follows immutable projection-list identity; callers that mutate a list in place cannot expect
its already-built lookup index to change.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory worktree's source registry.

No relevant external documentation is configured.

### Repo-Internal References

- Tests define normalization, precedence, and identity-cache expectations. [1]
- The `ref` / `series` factories, typed against the mirror rather than asserted past it. [2]
- The production lookup owns the WeakMap index and calls `orderedByCreation` over `series.subTasks`. [3]
- The master task reference declares linkedLifecycleId and masterRef, with no createdAt field. [4]
- The series row declares optional createdAt and no linkedLifecycleId. [5]

### Cross-Repo References

No meaningful cross-repository references found.

- The hierarchy helper is repository-local projection logic. [6]

## 260821-CLIVE Projection Fixture Alignment

No hierarchy behavior changed. The local `series()` fixture now defaults `discardedCount` to zero
and `discardedSubTasks` to an empty list because those cells are required on projected series. Parent
matching, creation-order tie breaking, and the per-list cache boundary remain unchanged.
