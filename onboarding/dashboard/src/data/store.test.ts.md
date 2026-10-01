# dashboard/src/data/store.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Vitest unit tests for the dashboard Zustand store (`store.ts`). They pin the store's public reducer
contract without rendering React: the bounded sliding-window `pushEvent` behavior, snapshot
folding into id-keyed maps, the named-delta upsert/removed paths, whole-object metrics/analytics
replacement, the connection state channel, and — since 260703-L15 — the **change gate** (idle
payloads cost zero store writes, identity stays stable) plus the **long-session guard** (500
simulated idle ticks with event traffic stay flat). Since the 260707-HFX2-L2 fix round, the change
gate also pins the **`agentNotifierHeartbeat` no-op/write-through split**: an idle re-snapshot with an
unchanged heartbeat costs zero writes, but a genuinely advanced heartbeat still rides through as
exactly one write. The suite also pins full scenario reset semantics directly: a typed, nonempty
closeout queue must become exactly empty through the canonical reset while `gen` advances once.
The sliding-window test is the task-34 guard that the raw Event-River buffer stays bounded.

## Code Commentary

### Logic

The suite drives the vanilla `dashboardStore` directly (`getState()` / `setState()`), not through a
React render. A `beforeEach` resets `conn`/`generatedAt` and the id-keyed maps plus `metrics`/`analytics`
to an empty baseline (it does NOT reset `events`/`eventsHydrated`, so the event test seeds those itself).

- `slides the event window so the buffer never grows without bound` — seeds `events: []`, pushes 2100
  lines through `pushEvent`, then asserts the buffer is capped at `EVENT_WINDOW` (2000), the newest row
  is retained (`e-2099`), and the oldest beyond the window slid off (`e-100`). This is the regression
  guard for the bounded sliding window.
- `folds a snapshot into id-keyed maps and goes live` — `applySnapshot` rekeys lifecycles/enclosures and
  flips `conn` to `live` with `metrics` populated.
- `upserts a lifecycle delta by id` / `drops a lifecycle on the removed marker` — exercise
  `applyDelta`'s `lifecycle` upsert and `lifecycle.removed` paths.
- `replaces metrics / analytics wholesale` — `applyDelta("metrics", …)` swaps the whole object.
- `marks the connection signal-lost` — `setConn` flips the channel.
- `clears a seeded closeout queue and increments generation exactly once on reset` — seeds the
  typed `RESET_QUEUE`, proves the authoritative store is nonempty, invokes
  `dashboardStore.getState().reset()`, then asserts exact queue emptiness and `gen + 1`. It never
  hand-clears the queue, so removing the canonical reset assignment makes the regression fail.

**The change-gate describe (260703-L15):** `volatileBump(source, tick)` builds a byte-fresh copy —
a new object graph, which is what the identity assertions need — with `generatedAt` moved and every
volatile age bumped, the exact shape of an idle tick. The copy comes from
`test/fixtures/wire.ts::reparsed`, which is a `structuredClone`, NOT the `JSON.parse(JSON.stringify(…))`
round-trip this helper used to run inline: that round-trip answers `any`, and `any` assigns to
anything, so the helper could have handed the store a shape the server cannot send and nothing would
have objected. The cases: 50 idle re-snapshots fire ZERO subscriber
notifications and leave `getState()` the SAME object (lifecycles/analytics/generatedAt identity
included); an idle re-snapshot with an unchanged `agentNotifierHeartbeat` (including the `null`/`null`
case, i.e. no supervisor attached, and since HFX2-L8 the backlog/duration fields) is also zero store writes and the state object stays identical —
this pins the `applySnapshot` early-return branch's `heartbeatEquals(a, b)` guard (added in the
260707-HFX2-L2 fix round) that gates the `set({ agentNotifierHeartbeat })` call on the heartbeat
literally changing, comparing `lastTickAt`/`ageSeconds`/`staleCutoffSeconds`/`stale` field-for-field
rather than reusing the general `stableEquals` helper (which strips `ageSeconds` as a
`VOLATILE_AGE_FIELDS` entry and would wrongly treat a real tick advance as unchanged); a companion
case then advances `ageSeconds` on an otherwise-identical heartbeat and asserts exactly ONE
notification, a new state object, `agentNotifierHeartbeat` equal to the advanced value, and that
`lifecycles`/`analytics`/`generatedAt` keep their prior identity — only the heartbeat rode through.
A redundant volatile-only `lifecycle` delta and a removed-marker for an absent id are both
no-writes; a real delta still applies exactly as before; a snapshot carrying ONE real change
applies it while every untouched node keeps identity; and the `servingBuild` stamp rides the
snapshot and keeps identity across stable re-sends. **The long-session guard describe:** 500
simulated idle ticks interleaved with 2,500 `pushEvent` lines leave the lifecycles/analytics
references untouched, the event window ≤ 2000, and the collection sizes constant — the
CI-encoded "a working day stays flat" contract.

### Conventions

Vitest with the `dashboardStore` vanilla store. `../fixtures/snapshot.json` reaches the store through
`test/servedProjection.ts::asServedProjection`, NOT the `snapshot as unknown as WorkspaceProjection`
double cast this file used to open with. That cast switched assignability off for the whole file, so
a fixture that dropped a field the store reads would have typechecked; the helper's parameter type
(`AsJsonModule<WorkspaceProjection>`) is a full structural check of everything `resolveJsonModule`'s
literal-widening does not touch, and the cast inside it only re-narrows the erased vocabularies. This
file therefore gained a check it never had.

Counts that belong to the fixture are read from the fixture: `FIXTURE_LIFECYCLES =
projection.lifecycles.length` replaces the hard-coded `2` in the snapshot-fold and long-session
assertions. The fixture now carries six lifecycles (one per member of the closed state vocabulary),
so a literal `2` would have failed — and a hand-kept literal beside a hand-kept payload is the
second-copy problem itself.

Tests assert on `getState()` snapshots rather than rendered output.
The reset regression uses a real `CloseoutQueueNode` fixture and the store's public reset action;
mounted derived-view clearance belongs to `SprintGraphPage.test.tsx` rather than this unit seam.

### Invariants And Boundaries

- The sliding-window test fixes the `EVENT_WINDOW` (2000) memory bound — the contract that `pushEvent`
  never lets the client buffer grow unbounded, dropping the oldest past the bound.
- Because `beforeEach` does not clear `events`, the event test resets `events`/`eventsHydrated`
  explicitly so it is independent of prior tests.
- These are store-contract tests; the Event-River rendering/virtualization is covered separately by
  `../panels/EventRiver.test.tsx`.
- Reset proof must begin from a nonempty queue, call the one canonical reset, assert exact
  authoritative-store emptiness, and retain the existing one-step generation contract. A manual
  `setState({ closeoutQueues: [] })`, mock reset, or empty initial fixture would not prove it.
- This regression covers dev/test scenario infrastructure. It does not specify production queue
  ingestion, retention, ordering, scheduling, or lifecycle behavior.
- The two `agentNotifierHeartbeat` cases pin that `applySnapshot`'s idle early-return branch must use a
  field-literal comparator (`heartbeatEquals`) for the heartbeat, never `stableEquals` — reusing
  `stableEquals` would strip `ageSeconds` and silently defeat detection of a genuinely advancing tick.

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
- `agentNotifierHeartbeat` no-op (incl. null/null) vs. genuine-change write-through cases. [5]
- The fixture narrowing and the fixture-derived lifecycle count. [6]
- The parameter type that IS the check, and why the double cast was not one. [7]
- `reparsed` (the `structuredClone` behind `volatileBump`) and the `agentNotifierHeartbeat` builder. [8]
- Projection / observer-event types the store maps over. [9]

### Cross-Repo References

No meaningful cross-repo references found. These tests are local to the dashboard store.

No meaningful cross-repo references found.
