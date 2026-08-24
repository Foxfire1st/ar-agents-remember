# dashboard/src/data/taskHierarchy.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/taskHierarchy.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T15:04+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is configured. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Tests define normalization, precedence, and identity-cache expectations. | "normalizes ..-relative ref files across folders"; "prefers the first series in list order when two series name the same doc"; "prefers the earliest ref by creation order within a series"; "caches per seriesList identity: a fresh array observes new refs" | dashboard/src/data/taskHierarchy.test.ts:43-52; dashboard/src/data/taskHierarchy.test.ts:54-60; dashboard/src/data/taskHierarchy.test.ts:62-74; dashboard/src/data/taskHierarchy.test.ts:97-105 |
| The `ref` / `series` factories, typed against the mirror rather than asserted past it. | "function ref("; "function series(" | dashboard/src/data/taskHierarchy.test.ts:9-9; dashboard/src/data/taskHierarchy.test.ts:13-13 |
| The production lookup owns the WeakMap index and calls `orderedByCreation` over `series.subTasks`. | `orderedByCreation` | dashboard/src/data/taskHierarchy.ts:145-150 |
| The two sub-task row models the `ref` factory had to choose between; only `SeriesSubTaskNode` declares `createdAt`. | `TaskSubTaskRefNode`; `SeriesSubTaskNode` | dashboard/src/types/projection.ts:422-429; dashboard/src/types/projection.ts:627-635 |

## Cross-Repo References

No meaningful cross-repository references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| The hierarchy helper is repository-local projection logic. | "describe(\"findParentTaskMatch\", () => {" | dashboard/src/data/taskHierarchy.test.ts:31-31 |

## 260821-CLIVE Projection Fixture Alignment

No hierarchy behavior changed. The local `series()` fixture now defaults `discardedCount` to zero
and `discardedSubTasks` to an empty list because those cells are required on projected series. Parent
matching, creation-order tie breaking, and the per-list cache boundary remain unchanged.

## Update History

- 2026-08-24T15:04+02:00 — No content impact: added the required empty discard-history cells to
  the local `SeriesNode` test builder; hierarchy assertions and lookup semantics are unchanged.

- 2026-08-20T10:45+02:00 — 260815-DAG-L12 curator: re-anchored citation range(s) to current source after the L12 line movement (cited files changed, card source unchanged); verification metadata unchanged.

- 2026-08-20T04:48+02:00 — 260815-DAG-L14 curator: re-read the `TaskSubTaskRefNode` claim — the row
  model gained the optional typed `masterRef`; wording retained and citation regenerated to the
  current interface lines. Verification stamp advanced to code commit 9c3180c1.

- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.
- 2026-08-08T23:15+02:00 — 260713-TES-L1 completion round 3 (curator): body refreshed for the supervisor -> agent-notifier rename (citation ranges and/or rename wording); verification metadata pinned until closeout stamps the 260713-TES-L1 commit.


- 2026-08-04T18:16+02:00 — 260731-EFA-L6 S18-B16 curator: corrected 1 citation range: `TaskSubTaskRefNode` lives at types/projection.ts L494-L501 (was L484-L491, which now covers `TaskSubStepNode`); `SeriesSubTaskNode` L369-L376 unchanged. Scoped fixer + non-fixing recheck green under the frozen snapshot; verification metadata unchanged.

- 2026-08-02T16:46+02:00 — 260731-EFA-L6 curator W1-B03: repaired 3 citation rows and 1 historical prose citation with exact anchors and source paths; scoped citation recheck recorded separately. Verification metadata remains pinned until closeout.

- 2026-08-01T09:10+02:00 — 260731-EFA-L4 curator: the `ref` factory changed type from
  `TaskSubTaskRefNode` to cit:([`SeriesSubTaskNode`], dashboard/src/data/taskHierarchy.test.ts:9-9), so recorded WHY in Conventions — the mirror
  split the two once-collapsed models and removed `createdAt` from the master row, and the
  cit:(["prefers the earliest ref by creation order within a series"], dashboard/src/data/taskHierarchy.test.ts:62-74) case sets `createdAt`, so under the old
  typing that case's fixture claimed a field its declared model no longer has. Verified against the
  diff that no case was added, removed or renamed and that every asserted value is unchanged (the
  factory body is still `{ name: overrides.number, status: "open", scope: "", ...overrides }`), and
  that these two factories are NOT shared builders — `test/fixtures/wire.ts` has no `SeriesNode` or
  `SeriesSubTaskNode` builder, so this file is one of the sites the sweep left local. Re-anchored the
  three drifted citations to the current 121-line source and added rows for the factory block and
  the two mirror models.

- 2026-07-24T13:17:50Z — Created for cached parent-task lookup regression coverage. Verification
  hash/date remain pinned to the pre-commit source stamp.
