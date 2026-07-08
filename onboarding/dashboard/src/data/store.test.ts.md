# dashboard/src/data/store.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/store.test.ts`               |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-08T23:59+02:00                           |
| lastVerifiedCommitHash | `5f9163882857114319552d303e2e301082b588ba`       |
| lastVerifiedCommitDate | 2026-07-08T18:21:20+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Vitest unit tests for the dashboard Zustand store (`store.ts`). They pin the store's public reducer
contract without rendering React: the bounded sliding-window `pushEvent` behavior, snapshot
folding into id-keyed maps, the named-delta upsert/removed paths, whole-object metrics/analytics
replacement, the connection state channel, and — since 260703-L15 — the **change gate** (idle
payloads cost zero store writes, identity stays stable) plus the **long-session guard** (500
simulated idle ticks with event traffic stay flat). Since the 260707-HFX2-L2 fix round, the change
gate also pins the **`supervisorHeartbeat` no-op/write-through split**: an idle re-snapshot with an
unchanged heartbeat costs zero writes, but a genuinely advanced heartbeat still rides through as
exactly one write. The sliding-window test is the task-34 guard that the raw Event-River buffer
stays bounded.

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

**The change-gate describe (260703-L15):** `volatileBump(source, tick)` builds a byte-fresh copy
(JSON round-trip, like a real wire parse) with `generatedAt` moved and every volatile age bumped —
the exact shape of an idle tick. The cases: 50 idle re-snapshots fire ZERO subscriber
notifications and leave `getState()` the SAME object (lifecycles/analytics/generatedAt identity
included); an idle re-snapshot with an unchanged `supervisorHeartbeat` (including the `null`/`null`
case, i.e. no supervisor attached, and since HFX2-L8 the backlog/duration fields) is also zero store writes and the state object stays identical —
this pins the `applySnapshot` early-return branch's `heartbeatEquals(a, b)` guard (added in the
260707-HFX2-L2 fix round) that gates the `set({ supervisorHeartbeat })` call on the heartbeat
literally changing, comparing `lastTickAt`/`ageSeconds`/`staleCutoffSeconds`/`stale` field-for-field
rather than reusing the general `stableEquals` helper (which strips `ageSeconds` as a
`VOLATILE_AGE_FIELDS` entry and would wrongly treat a real tick advance as unchanged); a companion
case then advances `ageSeconds` on an otherwise-identical heartbeat and asserts exactly ONE
notification, a new state object, `supervisorHeartbeat` equal to the advanced value, and that
`lifecycles`/`analytics`/`generatedAt` keep their prior identity — only the heartbeat rode through.
A redundant volatile-only `lifecycle` delta and a removed-marker for an absent id are both
no-writes; a real delta still applies exactly as before; a snapshot carrying ONE real change
applies it while every untouched node keeps identity; and the `servingBuild` stamp rides the
snapshot and keeps identity across stable re-sends. **The long-session guard describe:** 500
simulated idle ticks interleaved with 2,500 `pushEvent` lines leave the lifecycles/analytics
references untouched, the event window ≤ 2000, and the collection sizes constant — the
CI-encoded "a working day stays flat" contract.

### Conventions

Vitest with the `dashboardStore` vanilla store; `../fixtures/snapshot.json` is cast to
`WorkspaceProjection` as the projection fixture. Tests assert on `getState()` snapshots rather than
rendered output.

### Invariants And Boundaries

- The sliding-window test fixes the `EVENT_WINDOW` (2000) memory bound — the contract that `pushEvent`
  never lets the client buffer grow unbounded, dropping the oldest past the bound.
- Because `beforeEach` does not clear `events`, the event test resets `events`/`eventsHydrated`
  explicitly so it is independent of prior tests.
- These are store-contract tests; the Event-River rendering/virtualization is covered separately by
  `../panels/EventRiver.test.tsx`.
- The two `supervisorHeartbeat` cases pin that `applySnapshot`'s idle early-return branch must use a
  field-literal comparator (`heartbeatEquals`) for the heartbeat, never `stableEquals` — reusing
  `stableEquals` would strip `ageSeconds` and silently defeat detection of a genuinely advancing tick.

### Todos

No file-local todos.

## Docs References

No relevant external documentation found after checking live sources. This file exercises repo-local
dashboard store behavior with the in-repo vitest harness.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found after checking live sources for the dashboard store unit tests. | n/a | n/a |

## Repo-Internal References

The suite is the contract guard for the dashboard store reducers; the task-34 sliding-window test pins
the bounded buffer documented in the store sidecar.

| Finding | Citations | Source Path |
| --- | --- | --- |
| System under test: the Zustand store these reducers belong to. | — | [store.ts](store.ts) |
| Sliding-window guard pins `EVENT_WINDOW` (2000): newest retained, oldest slid off. | L22-L35 | [store.test.ts](store.test.ts) |
| Snapshot fold + named-delta upsert/removed + wholesale metrics/analytics + conn channel. | L37-L68 | [store.test.ts](store.test.ts) |
| `supervisorHeartbeat` no-op (incl. null/null) vs. genuine-change write-through cases. | L106-L146 | [store.test.ts](store.test.ts) |
| Projection / observer-event types the store maps over. | — | [../types/projection.ts](../types/projection.ts) |

## Cross-Repo References

No meaningful cross-repo references found. These tests are local to the dashboard store.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 (dead-seat storm observability, R6): updated the
  `supervisorHeartbeat` change-gate fixtures to include the inbox backlog count fields and last sweep
  duration that `heartbeatEquals` now compares. Verification metadata pinned until closeout stamps
  the 260707-HFX2-L8 commit.
- 2026-07-08T05:36+02:00 — 260707-HFX2-L2 fix round (`260707-HFX2-L2-fix2-report.md`): added two
  `supervisorHeartbeat` regression cases to the change-gate describe, covering the
  `store.ts` `applySnapshot` idle-branch fix that gates `set({ supervisorHeartbeat })` on
  `heartbeatEquals` (field-literal comparison) instead of writing unconditionally on every idle
  re-snapshot — one case pins the zero-write no-op (incl. `null`/`null`), the other pins the
  single-write pass-through on a genuine `ageSeconds` advance. Verification metadata pinned until
  closeout stamps the fix-round commit.
- 2026-07-07T05:20+02:00 — 260703-L15: added the change-gate describe (`volatileBump` idle-tick
  builder; zero-writes/identity across 50 idle re-snapshots; redundant delta + absent removed-
  marker no-writes; real-delta semantics preserved; per-node identity reuse; `servingBuild`
  identity) and the long-session guard (500 idle ticks + 2,500 events stay flat); `beforeEach`
  baseline gained `servingBuild: null`.
  Verification metadata pinned until closeout stamps the L15 commit.
- 2026-06-28T13:54+02:00 — Created for task 34: this previously-untracked store test file gained a
  bounded sliding-window guard (`slides the event window …`) asserting `EVENT_WINDOW` (2000) caps the
  client buffer (newest retained, oldest dropped), alongside the existing snapshot/delta/metrics/conn
  reducer tests. Verification metadata pinned until closeout stamps the task-34 code commit.
