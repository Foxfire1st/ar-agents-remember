# dashboard/src/panels/lifecycle-list/progress.ts

## Governing Overview

[panels overview](../overview.md)

## Purpose

One row's progress figure. Abandoned sub-task rows (a retired master's row is one) will not run: they are neither done nor part of the total, and the figure names them beside it instead, so a master whose remaining rows are all Completed reads complete ("5/5, 1 abandoned"). The same rule as `tasks/document.py::series_done` / `series_total` / `series_abandoned` on the server.

## Code Commentary

`RowProgress` carries `done`, `total` and an optional `abandoned` count. `taskStepProgress`, `subTaskProgress` and `seriesProgress` derive the figure, and `progressHint` renders it with the discarded count beside it.

## Evidence

- Abandoned sub-task rows are neither done nor part of the total and are named beside the progress figure. [1]
- The dashboard progress rule matches the server's series_done, series_total and series_abandoned rule. [2]
