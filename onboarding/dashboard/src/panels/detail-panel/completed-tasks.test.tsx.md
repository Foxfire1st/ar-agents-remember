# dashboard/src/panels/detail-panel/completed-tasks.test.tsx

## Governing Overview

[Area overview](../overview.md)

## Purpose

Declare mounted regression assertions for time-first completed master rows and the newest-five preview.

## Code Commentary

Native summary.completedAt and served children replace legacy finalizer parsing. Master rows retain time/numeric-id sorting, unknown-last, aria-sort and mount-local reset. Seven/three/zero-row controls retain newest-five preview and full-view reachability.

At 100/300 children in preview/full modes, a Proxy counts native task-map reads: completedEntries requires size+1 and mounted work <=(size+1)*4. HTML matches an uninstrumented control; visible buttons navigate by served child position/key, including a completed entry with no summary. Sorting remains; these are lookup counts, not elapsed-time/global linearity proof.

Aborted-master/sprint groups retain authored order without sort controls. Seeded timestamps are not finalizer/legacy-parser, live-projection, browser or executed-test evidence.

## Evidence

- Seeded completed-table cases assert time/number ordering, preview and retained non-completed/sprint order, not timestamp production. [1]



- The parameterized lookup control uses 100 and 300 rows in whole-list and preview modes, plus an entry with no summary. A Proxy counts native task-map reads: preparation equals the uninstrumented result with size + 1 reads; mounted HTML is identical, qualified child navigation is checked, and preview shows five rows. In whole-list mode the missing-document row is observed before clicking the number and completed sort controls. After those clicks the test asserts only the total read bound, reads <= (size + 1) * 4; it does not reassert that row's presence or position. This is source-defined evidence, not a fresh test, timing or performance run; no docPath getter is instrumented. [3]
- The dataset supplies served task entries with explicit summary.completedAt values and canonical parent/child keys. [4]
