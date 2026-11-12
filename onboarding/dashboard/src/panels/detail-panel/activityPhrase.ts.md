# dashboard/src/panels/detail-panel/activityPhrase.ts

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Write a master's child activity, `N works · N waiting · N paused`, from its served counts.

## Code Commentary

`activityPhrase(counts)` takes the served `works`, `waiting` and `paused` child counts and writes them in that order; the waiting part appears only while it is nonzero, so a master with nothing waiting reads `N works · N paused`. It formats served counts only. Its callers decide when it is shown: both leave it out while host activity is unknown.

## Relationships

The Operations row figure for non-task forms (`lifecycle-list/LifecycleList.tsx`, `RowFigure`) and the master page's Now cells (`task-groups.tsx`, `MasterNowCells`) render it. `activityPhrase.test.ts` pins both forms; the row figure is also exercised in `lifecycle-list/hierarchy.test.tsx`.

## Evidence

- The phrase is works, an optional waiting part, then paused. [1]
- The row figure renders it for non-task forms and hides it while host activity is unknown. [2]
- The master Now cells render it and leave it out while host activity is unknown. [3]
