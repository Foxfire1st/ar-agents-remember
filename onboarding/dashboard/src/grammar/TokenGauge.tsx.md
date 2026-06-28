# dashboard/src/grammar/TokenGauge.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/grammar/TokenGauge.tsx`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-15T17:00                                 |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| The `TokenSample` shape (ts + cumulative) it plots. | — | [observer/projection.py](agents-remember/mcp/src/agents_remember/observer/projection.py) |
| uPlot deferral is pinned to slice 08. | — | [08_boot-audio-polish.md](agents-remember/../tasks/agents-remember/260610_browser-dashboard/08_boot-audio-polish.md) |

## Update History

- 2026-06-15T17:00 — Created for slice 5d: `TokenGauge` migrated to Panda `css()` (was `.gauge*`).
  Verification metadata pinned until closeout stamps the 5d code commit.
