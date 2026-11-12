# dashboard/src/panels/lifecycle-list/waiting.test.tsx

## Governing Overview

[panels overview](../overview.md)

## Purpose

Pins that a started task the server serves as `waiting`, with its `waitingSeats`, is shown as waiting and never as paused: on the Operations row, on the task page, in the row hover, in the BY PHASE grouping and in the header count. The wait is served; the dashboard only shows it.

## Code Commentary

`SEAT` is one served `WaitingSeat`: a worker that waits for background since 10:00 with its check due at 10:03 and its own words as `detail`. `waiting(id)` builds a `task()` entry with `activity: 'waiting'`, `eventAt` at the seat's `since` and `waitingSeats` holding that seat.

The first case runs at a fixed display clock (10:02, two minutes after `since`) with a fetch that never answers. The row's `task-word` and the task page's `doc-status` both read `waiting for background 2m` and the row word carries `data-status="waiting"`. The row word's title is the single line `waitLines` builds for the seat — role, agent id, what it waits for since when, the check due and the seat's words — and `rowHover` at that instant holds `State: waiting` followed by that line. The second case serves a seat that declared both waits and expects the word to start `waiting for subagents and background`, with `taskStatusKey` returning `waiting`.

The third case serves a started task as waiting with a `taskCounts.waiting` of one. BY PHASE draws one group headed `waiting` with count one, and the mounted shell's `task-counts` header holds `1 waiting` and `0 paused`. The fourth case serves a paused task with a waiting count of zero and expects no `waiting` in the header, so the line keeps its earlier form while nothing waits.

These are jsdom component cases over the real store, list, page and shell: they are not a browser or accessibility acceptance, and they do not cover the master child-count cells, a waiting seat with no served `checkDueAt`, or the server's rules for when a task counts as waiting.

## Relationships

The cases render `LifecycleList`, `DetailPanel` and `CockpitShell` from a store seeded through `applySnapshot` with the `projection` builder from `test/fixtures/wire`, and take `task` and `installListCleanup` from the lifecycle-list `test-utils`. The cases take `taskStatusKey` from `detail-panel/pageParts`, `waitLines` from `detail-panel/waitWords`, `formatLimitTime` from `detail-panel/limitTime` and `rowHover` from `rowState`. The served shape is `WaitingSeat` in `types/projection`, produced by the observer's task-entry join; this file never decides that a task waits.

## Evidence

- The served seat the cases use is a worker waiting for background with its start, its check due and its own words. [10]
- At a fixed clock the row and the page read the waiting word, the row word's title and the hover carry the seat line. [11]
- A seat that declared both waits reads waiting for subagents and background. [12]
- BY PHASE groups the waiting task under waiting and the header counts it as waiting. [13]
- The header line has no waiting count while no task waits. [14]
- The word joins the served wait names with and. [15]
- The hover line is role, agent, what it waits for since when, the check due and the seat's words. [16]
- BY PHASE orders the waiting group between works and paused. [17]
- The header omits a waiting count of zero and drops it while host activity is unknown. [18]
