# dashboard/src/data/store.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/store.test.ts`               |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-01T09:16+02:00 |
| lastVerifiedCommitHash | `1c1629fc97dd4daf352cf9b3529d210be167d2af`       |
| lastVerifiedCommitDate | 2026-08-08T22:29:45+02:00|
| governingOverview | `overview.md` |

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

### Invariants And Boundaries

- The sliding-window test fixes the `EVENT_WINDOW` (2000) memory bound — the contract that `pushEvent`
  never lets the client buffer grow unbounded, dropping the oldest past the bound.
- Because `beforeEach` does not clear `events`, the event test resets `events`/`eventsHydrated`
  explicitly so it is independent of prior tests.
- These are store-contract tests; the Event-River rendering/virtualization is covered separately by
  `../panels/EventRiver.test.tsx`.
- The two `agentNotifierHeartbeat` cases pin that `applySnapshot`'s idle early-return branch must use a
  field-literal comparator (`heartbeatEquals`) for the heartbeat, never `stableEquals` — reusing
  `stableEquals` would strip `ageSeconds` and silently defeat detection of a genuinely advancing tick.

### Todos

No file-local todos.

## Docs References

No relevant external documentation found after checking live sources. This file exercises repo-local
dashboard store behavior with the in-repo vitest harness.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found after checking live sources for the dashboard store unit tests. | n/a | n/a |

## Repo-Internal References

The suite is the contract guard for the dashboard store reducers; the task-34 sliding-window test pins
the bounded buffer documented in the store sidecar.

| Finding | Anchor | Source |
| --- | --- | --- |
| System under test: the Zustand store these reducers belong to. | `dashboardStore` | dashboard/src/data/store.ts:225-347 |
| Sliding-window guard pins `EVENT_WINDOW` (2000): newest retained, oldest slid off. | `EVENT_WINDOW` | dashboard/src/data/store.ts:56-56 |
| Snapshot fold + named-delta upsert/removed + wholesale metrics/analytics + conn channel. | "folds a snapshot into id-keyed maps and goes live" | dashboard/src/data/store.test.ts:51-82 |
| `agentNotifierHeartbeat` no-op (incl. null/null) vs. genuine-change write-through cases. | "applies an idle re-snapshot with an unchanged agentNotifierHeartbeat (incl. null/null) with zero store writes"; "applies an idle re-snapshot with a genuinely changed agentNotifierHeartbeat" | dashboard/src/data/store.test.ts:121-159 |
| The fixture narrowing and the fixture-derived lifecycle count. | "export function asServedProjection" | dashboard/src/test/servedProjection.ts:22-43 |
| The parameter type that IS the check, and why the double cast was not one. | `AsJsonModule`; `asServedProjection` | dashboard/src/test/servedProjection.ts:22-32; dashboard/src/test/servedProjection.ts:41-43 |
| `reparsed` (the `structuredClone` behind `volatileBump`) and the `agentNotifierHeartbeat` builder. | `reparsed`; `agentNotifierHeartbeat` | dashboard/src/test/fixtures/wire.ts:352-366; dashboard/src/test/fixtures/wire.ts:396-398 |
| Projection / observer-event types the store maps over. | `WorkspaceProjection` | dashboard/src/types/projection.ts:517-528 |

## Cross-Repo References

No meaningful cross-repo references found. These tests are local to the dashboard store.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-04T18:40+02:00 — 260731-EFA-L6 S18-B18 curator: normalized the 6 citation rows
  (deduplicated the servedProjection citation; bound the fold, heartbeat and fixture rows to
  51-82, 121-159 and 4-20) and rewrote the historical single-number line shorthand below (the
  snapshot-fold and long-session line references) as plain prose, which the checker otherwise
  counts as unchecked prose ranges. Zero findings and zero unchecked spans/ranges remain.

- 2026-08-01T09:16+02:00 — 260731-EFA-L4 curator: corrected two Conventions/Logic claims the diff
  against `abc7cbc` falsified. (1) "`../fixtures/snapshot.json` is cast to `WorkspaceProjection`" —
  the `as unknown as WorkspaceProjection` double cast is gone; the fixture now narrows through
  `test/servedProjection.ts::asServedProjection`, whose parameter type is a real structural check,
  so this file gained assignability checking it did not have. (2) "`volatileBump` … (JSON
  round-trip, like a real wire parse)" — it now calls `test/fixtures/wire.ts::reparsed`, which is a
  `structuredClone`; the JSON round-trip is gone precisely because it answered `any`. Also recorded
  `FIXTURE_LIFECYCLES`, which replaced the hard-coded `2` in the snapshot-fold and
  long-session assertions (then at lines 57 and 238) — the fixture now carries six lifecycles, so the literal was about
  to become wrong. Re-anchored the three test citations, all of which the +15-line header shift had
  broken: L22-L35 → L36-L49 (the sliding-window `it`), L37-L68 → L51-L82 (fold/delta/metrics/conn),
  L106-L146 → L121-L159 (the two `supervisorHeartbeat` cases).

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

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
