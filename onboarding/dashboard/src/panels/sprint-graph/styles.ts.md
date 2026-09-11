# dashboard/src/panels/sprint-graph/styles.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/sprint-graph/styles.ts`    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-20T10:45+02:00                           |
| lastVerifiedCommitHash | `b7f2c8e2c7020642780e2c9b997ffb035a782e62`       |
| lastVerifiedCommitDate | 2026-08-20T10:42:29+02:00                        |
| governingOverview      | `overview.md`                                    |

## Governing Overview

[sprint-graph overview](overview.md)

## Purpose

The sprint graph wave-grid layout (260815-DAG-L12 R2/R6): at most 3 boxes per row before
wrapping on wide screens, collapsing to a single wave-ordered column on narrow/phone
viewports. The two declarative layout objects are exported so tests can pin the responsive
contract (jsdom cannot evaluate media queries or `ch` units).

## Code Commentary

### Logic

- `waveGridStyles`: `display: grid; grid-template-columns: repeat(3, minmax(0, 1fr))` with
  an `@media (max-width: 720px)` override to `1fr` — the ≤3-boxes-per-row and narrow
  single-column contract, exported as a plain object.
- `leafLineStyles`: one ellipsized leaf line whose visible character range grows with the
  viewport — `maxWidth: min(100%, 30ch)` base, stepped up to `48ch` at `sm` and `72ch` at
  `lg` (Panda CSS breakpoints); exported so tests pin the ch-based growth.
- The remaining exports are Panda `css()`/`cva()` tokens: `graph` (column flex),
  `wave`/`waveHead`, `waveGrid`, `box`/`boxHead`/`boxTitle`, the `frontier` cva
  (landed/ready/waiting/in-flight color variants), `leaves`/`leafLine`, `lump`, and
  `preds`/`pred`.

### Conventions

- Export the declarative style objects (`waveGridStyles`, `leafLineStyles`) for test
  pinning; the memoized component consumes them through `css(...)`.

### Invariants And Boundaries

- Narrow layout preserves box grouping and predecessor info; only the column count changes.
- No layout algorithm, no canvas, no library dependency — the documented L12-R3 fallback.

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The responsive grid contract (≤3 per row, narrow single column). | `waveGridStyles` | dashboard/src/panels/sprint-graph/styles.ts:7-12 |
| The ellipsized, viewport-growing leaf line contract. | `leafLineStyles` | dashboard/src/panels/sprint-graph/styles.ts:77-87 |
| The frontier-state color variants. | `frontier` | dashboard/src/panels/sprint-graph/styles.ts:44-64 |
| The component consuming these styles. | `SprintGraphView` | dashboard/src/panels/sprint-graph/SprintGraphView.tsx:81-107 |
| The responsive-contract forcing tests. | `SprintGraphView` (describe) | dashboard/src/panels/sprint-graph/SprintGraphView.test.tsx:146-163 |

## Cross-Repo References

No cross-repository implementation source governs this file.

## Update History

- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R2/R6): the wave-grid and

ellipsized leaf-line style contracts, exported for test pinning; frontier/lump/predecessor

tokens. Verified at code commit b7f2c8e2.



- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R2/R6): the wave-grid and
  ellipsized leaf-line style contracts, exported for test pinning; frontier/lump/predecessor
  tokens. Verified at code commit b7f2c8e2.
