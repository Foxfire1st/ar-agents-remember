# dashboard/src/grammar/TokenGauge.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/grammar/TokenGauge.tsx`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-15T17:00                                 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`       |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[grammar/ overview](overview.md)

## Purpose

`TokenGauge` is the cumulative-token fuel gauge — a dependency-free SVG sparkline over a
`TokenSample[]`. uPlot stays deferred to slice 08 (where streaming-telemetry density justifies a
canvas dep); a handful of cumulative points needs no charting library.

## Code Commentary

### Logic

With `< 2` points it renders a flat `{total} tok` label (`gaugeFlat`). Otherwise it maps each sample
to a `points` string for an SVG `<polyline>` (x = even step, y = inverted cumulative/max), styled by
Panda `css()` (`gaugeLine` strokes the cyan). The total is `series.at(-1).cumulative`.

### Invariants And Boundaries

Pure render over the server-computed `tokenSeries`; no charting dependency (the deliberate
uPlot-deferral). Cyan = the progress/charge grammar.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The `TokenSample` shape (ts + cumulative) it plots. | `TokenSample` | dashboard/src/types/projection.ts:511-514 |

## Update History

- 2026-08-04T11:32:09+02:00 — 260731-EFA-L6 S18-B02 curator: reconciled the frozen-source ledger and generated final citation ranges with the scoped fixer.

- 2026-06-15T17:00 — Created for slice 5d: `TokenGauge` migrated to Panda `css()` (was `.gauge*`).
  Verification metadata pinned until closeout stamps the 5d code commit.
