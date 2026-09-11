# dashboard/src/panels/lifecycle-list/test-utils.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/lifecycle-list/test-utils.tsx`        |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-24T15:04+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

Shared fixture builders for the split LifecycleList test files, extracted from
`LifecycleList.test.tsx` by the 260731-EFA-L8 split. Seeds lifecycles, enclosures,
task documents, series, collapsible hierarchies, and the shared localStorage/store
cleanup.

## Code Commentary

### Logic

`lifecycle` / `enclosure` / `taskDoc` / `seriesNode` build typed nodes;
`collapsibleHierarchyProjection` builds the grouping scenario;
`installLifecycleListCleanup` registers the afterEach reset the split files rely on
(a side-effect import).

### Conventions

Typed through the projection mirror; test-only.

### Invariants And Boundaries

Never imported by production code; split test files must import it for the shared
cleanup.

### Todos

None recorded.

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The shared fixture builders and cleanup. | `seed`; `collapsibleHierarchyProjection`; `installLifecycleListCleanup` | dashboard/src/panels/lifecycle-list/test-utils.tsx:111-140; dashboard/src/panels/lifecycle-list/test-utils.tsx:130-235; dashboard/src/panels/lifecycle-list/test-utils.tsx:236-243 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## 260821-CLIVE Projection Fixture Alignment

No helper behavior changed. `seriesNode()` now defaults the required `discardedCount: 0` and
`discardedSubTasks: []` cells. Existing seat/execution-wave defaults and shared store/localStorage
cleanup remain unchanged.

## Update History

- 2026-08-24T15:04+02:00 — No content impact: aligned the shared series fixture with the required
  discard-history projection fields.

- 2026-08-20T04:44+02:00 — 260815-DAG-L14: `taskDoc` fixture defaults `seats: []`. Verified at
  code commit 9c3180c1.


- 2026-08-15T02:16:50+02:00 — No content impact: 260815-DAG-L1 only makes lifecycle-list TaskDocNode fixtures carry the
  required empty `executionWaves` projection field; lifecycle-list behavior is unchanged.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the shared
  test fixtures extracted from `LifecycleList.test.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
