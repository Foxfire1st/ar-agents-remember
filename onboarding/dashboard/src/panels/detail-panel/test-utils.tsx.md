# dashboard/src/panels/detail-panel/test-utils.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/detail-panel/test-utils.tsx`          |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`                  |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

Shared fixture builders for the split DetailPanel test files, extracted from
`DetailPanel.test.tsx` by the 260731-EFA-L8 split. Seeds task documents, series,
enclosures, projections, promoted-lifecycle scenarios, and counter stubs.

## Code Commentary

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

## Update History

- 2026-08-11T19:58+02:00 — Canonicalized DetailPanel fixture document paths under the
  repository-qualified `/tasks/<repository>/...` topology.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the shared
  test fixtures extracted from `DetailPanel.test.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
