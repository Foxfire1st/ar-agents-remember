# dashboard/src/grammar/TokenGauge.tsx

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

## Evidence

### Repo-Internal References

- The `TokenSample` shape (ts + cumulative) it plots. [1]
