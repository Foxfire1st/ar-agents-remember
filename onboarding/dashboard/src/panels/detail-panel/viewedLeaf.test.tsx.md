# dashboard/src/panels/detail-panel/viewedLeaf.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/detail-panel/viewedLeaf.test.tsx`     |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-11T15:20+02:00                                      |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The viewed-leaf reporting suite split from `DetailPanel.test.tsx` by the
260731-EFA-L8 test split. Pins the L5 fix-1 viewed-leaf reporting behavior of the
detail panel.

## Code Commentary

### Logic

Selects a leaf and asserts the panel reports the viewed leaf key/identity as
expected.

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
| The viewed-leaf reporting suite. | "describe(\"DetailPanel viewed-task reporting\", () => {" | dashboard/src/panels/detail-panel/viewedLeaf.test.tsx:11-52 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-11T15:20+02:00 — Replaced the generic test-runner anchor with the suite's unique
  declaration and complete current extent.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  viewed-leaf suite split from `DetailPanel.test.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
