# dashboard/src/panels/sprint-graph/SprintGraphView.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/sprint-graph/SprintGraphView.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-20T10:45+02:00                           |
| lastVerifiedCommitHash | `b7f2c8e2c7020642780e2c9b997ffb035a782e62`       |
| lastVerifiedCommitDate | 2026-08-20T10:42:29+02:00                        |
| governingOverview      | `overview.md`                                    |

## Governing Overview

[sprint-graph overview](overview.md)

## Purpose

Component forcing suite for the sprint graph wave-grid view (260815-DAG-L12 R2/R6/R7): the
zero-edge graph and segmented-master scenarios that route review requires as mounted-UI
evidence, plus the frontier badge and the declarative responsive contracts.

## Code Commentary

### Logic

Renders real `SprintGraphView` components with @testing-library: a zero-edge graph renders
one wave row of independent boxes with no predecessor labels (an atomic master renders as
the lump); a segmented master renders across three wave rows with labeled edge reasons
(`← Master One — OM1's early segment lands before the atomic block`); each box exposes
`data-frontier` for the frontier badge; the grid and narrow single-column declarations are
pinned against the exported `waveGridStyles` (jsdom cannot evaluate media queries); and the
ellipsized leaf line's ch-based growth is pinned against `leafLineStyles`.

### Invariants And Boundaries

- Renders mounted components — projection-only assertions are insufficient for the L12-R7
  rendering requirements.
- jsdom limitations are worked around by exporting and asserting the declarative style
  objects rather than computed layout.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The component forcing suite. | `SprintGraphView` (describe) | dashboard/src/panels/sprint-graph/SprintGraphView.test.tsx:102-163 |
| The component under test. | `SprintGraphView` | dashboard/src/panels/sprint-graph/SprintGraphView.tsx:81-107 |
| The style contracts asserted. | `waveGridStyles`; `leafLineStyles` | dashboard/src/panels/sprint-graph/styles.ts:7-12; dashboard/src/panels/sprint-graph/styles.ts:77-87 |

## Cross-Repo References

No cross-repository implementation source governs this file.

## Update History

- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R2/R6/R7): mounted component tests —

zero-edge, segmented-master with edge reasons, frontier badges, and the exported

responsive/ellipsis contracts. Verified at code commit b7f2c8e2.



- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R2/R6/R7): mounted component tests —
  zero-edge, segmented-master with edge reasons, frontier badges, and the exported
  responsive/ellipsis contracts. Verified at code commit b7f2c8e2.
