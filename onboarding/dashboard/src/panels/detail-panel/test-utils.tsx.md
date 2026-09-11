# dashboard/src/panels/detail-panel/test-utils.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/detail-panel/test-utils.tsx`          |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-09-04T01:06+02:00 |
| lastVerifiedCommitHash | `1993dd25bdf8331a2c1e28171dff2bf92ea090e2` |
| lastVerifiedCommitDate | 2026-09-04T00:57:29+02:00 |
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

Shared fixture builders for the split DetailPanel test files, extracted from
`DetailPanel.test.tsx` by the 260731-EFA-L8 split. Seeds task documents, series,
enclosures, projections, promoted-lifecycle scenarios, and counter stubs.


## 260831-CCR-L23 Requirement-Listing Stub

`stubNotes` gained an optional third argument: the registered requirement
listing (rows shaped `{ name, path, address, size, sha256 }`). Its fetch stub
now answers `/api/requirements/list` with
`{ repo, master, document, registered, requirements }` so detail-panel suites
can exercise the requirement-links provider without a live server. Existing notes and
task-document branches are unchanged.

## Code Commentary

Since 260815-DAG-L14 the `taskDoc` fixture factory defaults `seats: []` (the new required `TaskDocNode` field).

### Logic

`seed` / `taskDoc` / `seriesNode` / `enclosure` build minimal typed nodes;
`seedProjection` assembles a workspace projection; `seedPromotedLeaf` and
`seedSeriesOrdering` prepare the promoted-identity and ordering scenarios;
`stubCounters` installs deterministic counter hooks.

### Conventions

Fixtures are typed through the projection mirror so a fixture that compiles is a shape
the mirror can produce. Task-document fixture paths use `/tasks/<repository>/...`, so tests exercise
the same repository-qualified document topology as production selection and projection code.

### Invariants And Boundaries

Test-only module; never imported by production code.

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
| The shared fixture builders. | `seed`; `seedProjection`; `seedPromotedLeaf`; `stubCounters` | dashboard/src/panels/detail-panel/test-utils.tsx:14-45; dashboard/src/panels/detail-panel/test-utils.tsx:276-305; dashboard/src/panels/detail-panel/test-utils.tsx:373-479 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## 260821-CLIVE Projection Fixture Alignment

No helper behavior changed. `seriesNode()` now defaults the required `discardedCount: 0` and
`discardedSubTasks: []` fields so every detail-panel fixture remains a valid projected series. The
existing required `seats` and repository-qualified topology defaults remain intact.

## Update History

- 2026-09-04T01:06+02:00 — 260831-CCR-L23 Gate-5 memory pass: recorded the `/api/requirements/list` branch + requirement-listing argument added to the shared `stubNotes` fixture.

- 2026-08-24T15:04+02:00 — No content impact: completed the shared `SeriesNode` fixture with the
  required empty discard-history cells.

- 2026-08-20T04:36+02:00 — 260815-DAG-L14: `taskDoc` fixture factory defaults `seats: []`. Verified at code commit 9c3180c1.

- 2026-08-15T02:16:50+02:00 — No content impact: 260815-DAG-L1 only makes shared detail-panel TaskDocNode fixtures carry
  the required empty `executionWaves` projection field; rendered detail behavior is unchanged.

- 2026-08-11T19:58+02:00 — Canonicalized DetailPanel fixture document paths under the
  repository-qualified `/tasks/<repository>/...` topology.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the shared
  test fixtures extracted from `DetailPanel.test.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
