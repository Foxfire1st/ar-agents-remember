# dashboard/src/panels/lifecycle-list/progress.ts

## Governing Overview

[panels overview](../overview.md)

## Purpose

One row's numeric progress facts. Abandoned sub-task rows (including a retired master's row) are neither done nor part of the total. The line shows done/total; rowState preserves abandoned and discarded counts in the hover, so completed execution stays distinct from removal. The counting rule agrees with the server's series_done / series_total / series_abandoned projection.

## Code Commentary

`RowProgress` carries `done`, `total` and an optional `abandoned` count. `taskStepProgress`, `subTaskProgress` and `seriesProgress` derive these facts only. Rendering is owned by rowState and LifecycleList; progressHint was removed when the compact row moved secondary counts into its hover.

## Evidence

- Abandoned sub-task rows are neither done nor part of the total; rendering is outside this counter module. [1]

- The dashboard progress rule matches the server's series_done, series_total and series_abandoned rule. [2]
