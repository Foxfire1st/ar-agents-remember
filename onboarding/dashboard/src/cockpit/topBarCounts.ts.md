# dashboard/src/cockpit/topBarCounts.ts

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Write the top bar's task-count line, `N planned · N started · …`, from the served `taskCounts` and whether host activity is unknown.

## Code Commentary

`topBarCountsLine(taskCounts, hostUnknown)` lists planned, started, completed, aborted, works, waiting and paused in that order, each as its served count and the shared `statusLabel` word, joined with ` · `. A waiting count shows only while it is above zero, so the line keeps its form while nothing waits. While host activity is unknown the works, waiting and paused counts are left out and the line ends with `host activity unavailable`, the one place the dashboard says so. The served `unknown` count is never written as a figure. The function formats served counts only; it neither counts tasks nor decides their activity.

## Relationships

`Cockpit.tsx`'s `TopBar` renders the line in its `task-counts` span, passing the served `taskCounts` and the `selectHostActivityUnknown` reading (a served unknown count above zero). The words come from `panels/detail-panel/pageParts.tsx` (`statusLabel`). The mounted shell cases in `Cockpit.test.tsx` and `panels/lifecycle-list/waiting.test.tsx` exercise the line.

## Evidence

- The line writes each shown count with the shared status word, joined by a middle dot, and adds the unavailability notice while host activity is unknown. [1]
- While host activity is unknown the activity counts are left out; otherwise waiting shows only when nonzero. [2]
- The activity counts are works, waiting and paused. [3]
- TopBar renders the line in its task-counts span. [4]
- Host activity is unknown while the served unknown count is above zero. [5]
