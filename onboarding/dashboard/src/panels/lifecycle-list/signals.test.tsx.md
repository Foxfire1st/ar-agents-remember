# dashboard/src/panels/lifecycle-list/signals.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/lifecycle-list/signals.test.tsx`      |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-11T15:20+02:00                                      |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`                  |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The independent Operations-signals suite split from `LifecycleList.test.tsx` by the
260731-EFA-L8 test split. Pins the independent signal rendering on rows
(state marks, attention, gate hints) without coupling to the detail panel.

## Code Commentary

### Logic

Seeds rows with varied lifecycle states and asserts the per-row signal marks
(including the `awaiting-developer` live-state mark rule).

### Invariants And Boundaries

Assertions preserved from the monolithic suite.

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
| The Operations-signals suite. | "describe(\"LifecycleList independent Operations signals\", () => {" | dashboard/src/panels/lifecycle-list/signals.test.tsx:23-185 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-11T15:20+02:00 — Replaced the generic test-runner anchor with the Operations-signals
  suite's unique declaration.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  signals suite split from `LifecycleList.test.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
