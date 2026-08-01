# dashboard/src/data/taskHierarchy.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/taskHierarchy.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-01T09:10+02:00 |
| lastVerifiedCommitHash |  `e52edaf5b655f495580efd93306afdf922b19b51`|
| lastVerifiedCommitDate |  2026-08-01T11:01:51+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation entries are configured in this memory worktree's source registry.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is configured. | Source discovery checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Tests define normalization, precedence, and identity-cache expectations. | L30-L120 | [taskHierarchy.test.ts](taskHierarchy.test.ts) |
| The `ref` / `series` factories, typed against the mirror rather than asserted past it. | L7-L28 | [taskHierarchy.test.ts](taskHierarchy.test.ts) |
| The production lookup owns the WeakMap index and calls `orderedByCreation` over `series.subTasks`. | L22-L41 | [taskHierarchy.ts](taskHierarchy.ts) |
| The two sub-task row models the `ref` factory had to choose between; only `SeriesSubTaskNode` declares `createdAt`. | `TaskSubTaskRefNode`; `SeriesSubTaskNode` | [projection.ts](../types/projection.ts) |

## Cross-Repo References

No meaningful cross-repository references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The hierarchy helper is repository-local projection logic. | L1-L120 | [taskHierarchy.test.ts](taskHierarchy.test.ts) |

## Update History

- 2026-08-01T09:10+02:00 — 260731-EFA-L4 curator: the `ref` factory changed type from
  `TaskSubTaskRefNode` to `SeriesSubTaskNode` (L9), so recorded WHY in Conventions — the mirror
  split the two once-collapsed models and removed `createdAt` from the master row, and the
  "prefers the earliest ref by creation order" case (L61-L73) sets `createdAt`, so under the old
  typing that case's fixture claimed a field its declared model no longer has. Verified against the
  diff that no case was added, removed or renamed and that every asserted value is unchanged (the
  factory body is still `{ name: overrides.number, status: "open", scope: "", ...overrides }`), and
  that these two factories are NOT shared builders — `test/fixtures/wire.ts` has no `SeriesNode` or
  `SeriesSubTaskNode` builder, so this file is one of the sites the sweep left local. Re-anchored the
  three drifted citations to the current 121-line source and added rows for the factory block and
  the two mirror models.

- 2026-07-24T13:17:50Z — Created for cached parent-task lookup regression coverage. Verification
  hash/date remain pinned to the pre-commit source stamp.
