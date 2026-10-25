# dashboard/src/data/store.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Pure store assertions cover bounded events, task-keyed snapshots/deltas, published taskCounts, metrics/connection state, idle identity and canonical nonempty-queue reset. Removed lifecycle/heartbeat cases are not current coverage.

## Code Commentary

### Logic

The suite drives the vanilla store without React. beforeEach calls canonical reset; event tests also seed events explicitly.

- `slides the event window so the buffer never grows without bound` — seeds `events: []`, pushes 2100
  lines through `pushEvent`, then asserts the buffer is capped at `EVENT_WINDOW` (2000), the newest row
  is retained (`e-2099`), and the oldest beyond the window slid off (`e-100`). This is the regression
  guard for the bounded sliding window.
- Snapshot folding goes live with native task keys, fixture-derived population and published taskCounts.
- `task` upserts by qualified key; `task.removed` removes by key, not lifecycle id.
- Whole-object metrics replacement uses ignoredHostAgents rather than lifecycle buckets.
- `marks the connection signal-lost` — `setConn` flips the channel.
- `clears a seeded closeout queue and increments generation exactly once on reset` — seeds the
  typed `RESET_QUEUE`, proves the authoritative store is nonempty, invokes
  `dashboardStore.getState().reset()`, then asserts exact queue emptiness and `gen + 1`. It never
  hand-clears the queue, so removing the canonical reset assignment makes the regression fail.

Typed reparsed cloning bumps generatedAt and attention waits, not a removed TaskEntry age. Content-equal reparsed task deltas remain no-writes. Fifty idle snapshots require zero writes and stable state/tasks/analytics/time identity; redundant task deltas and absent removals are no-writes. Real eventAt changes apply, untouched tasks and equal servingBuild keep identity. The 500-tick/five-events-per-tick control retains task population/identity and a <=2000 event window; these are simulated source bounds, not a day-long performance result.

### Conventions

Vitest with the `dashboardStore` vanilla store. `../fixtures/snapshot.json` reaches the store through
`test/servedProjection.ts::asServedProjection`, NOT the `snapshot as unknown as WorkspaceProjection`
double cast this file used to open with. That cast switched assignability off for the whole file, so
a fixture that dropped a field the store reads would have typechecked; the helper's parameter type
(`AsJsonModule<WorkspaceProjection>`) is a full structural check of everything `resolveJsonModule`'s
literal-widening does not touch, and the cast inside it only re-narrows the erased vocabularies. This
file therefore gained a check it never had.

FIXTURE_TASKS and FIRST_KEY/SECOND_KEY come from projection.tasks, not a copied lifecycle population or count rollup.

Tests assert on `getState()` snapshots rather than rendered output.
The reset regression uses a real `CloseoutQueueNode` fixture and the store's public reset action;
mounted derived-view clearance belongs to `SprintGraphPage.test.tsx` rather than this unit seam.

### Invariants And Boundaries

- The sliding-window test fixes the `EVENT_WINDOW` (2000) memory bound — the contract that `pushEvent`
  never lets the client buffer grow unbounded, dropping the oldest past the bound.
- beforeEach calls canonical reset; event-window cases also explicitly seed events/eventsHydrated.
- These are store-contract tests; the Event-River rendering/virtualization is covered separately by
  `../panels/EventRiver.test.tsx`.
- Reset proof must begin from a nonempty queue, call the one canonical reset, assert exact
  authoritative-store emptiness, and retain the existing one-step generation contract. A manual
  `setState({ closeoutQueues: [] })`, mock reset, or empty initial fixture would not prove it.
- This regression covers dev/test scenario infrastructure. It does not specify production queue
  ingestion, retention, ordering, scheduling, or lifecycle behavior.
- The removed heartbeat no-op/write-through cases are not current source coverage.

### Todos

No file-local todos.

## Evidence

### Docs References

No relevant external documentation found after checking live sources. This file exercises repo-local
dashboard store behavior with the in-repo vitest harness.

No relevant external documentation found after checking live sources for the dashboard store unit tests.

### Repo-Internal References

The suite is the contract guard for the dashboard store reducers; the task-34 sliding-window test pins
the bounded buffer documented in the store sidecar.


- System under test: the Zustand store these reducers belong to, including its one full reset transaction. [1]

- Sliding-window guard pins `EVENT_WINDOW` (2000): newest retained, oldest slid off. [2]

- Snapshot fold + named-delta upsert/removed + wholesale metrics/analytics + conn channel. [3]


- The typed nonempty queue fixture and direct canonical-reset regression force exact queue clearance plus one generation increment. [4]


- Fixture narrowing and task-derived keys/count replace lifecycle population. [6]
- The parameter type that IS the check, and why the double cast was not one. [7]
- Typed reparsed supplies cloning; the heartbeat builder is no longer used here. [8]

- The projection mirror the store folds into its id-keyed maps on each snapshot. [9]


### Cross-Repo References

No meaningful cross-repo references found. These tests are local to the dashboard store.

No meaningful cross-repo references found.
