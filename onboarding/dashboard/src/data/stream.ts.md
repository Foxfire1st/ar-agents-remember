# dashboard/src/data/stream.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Thin EventSource wiring for the dashboard frontend. `connectState` subscribes to the folded projection
stream and merges snapshot/delta events into the Zustand store; `connectEvents` subscribes to the raw
observer-event stream that feeds the Event River.

## Code Commentary

### Logic

`STATE_EVENTS` lists every named state delta the backend emits — the keyed-collection events
(`lifecycle`/`enclosure`/`provider` plus their `.removed` markers) and the whole-value replacements
(`activeWorktreeGroups`, `metrics`, `analytics`). `activeWorktreeGroups` (task 33) is the bounded
active-enclosure set the Topology constellation filters on; its delta arrives as a wrapped
`{activeWorktreeGroups: [...]}` marker the store unwraps. `connectState(base)` opens
`GET /api/stream`, applies full `snapshot` payloads through `store.applySnapshot`, sends named deltas to
`store.applyDelta`, and maps EventSource `open`/`error` to the connection badge state. `connectEvents`
opens `GET /api/events`, forwards each raw `event` payload to the supplied `onLine` callback, and invokes
the optional `onReady` callback when the backend emits its explicit `ready` marker after retained backlog
delivery. 260715-FEUI-L2 (review finding 2) adds the optional **`onInterrupt`** callback, fired on
the EventSource `error` event: every connection replays a backlog before its own `ready` (an
undecodable `Last-Event-ID` cursor makes the server fall back to the full initial window), so a
consumer gating application on `ready` must RE-CLOSE its gate on interrupt — the seat-event
reconciler's per-connection backlog gate in `Cockpit.tsx` is the consumer this exists for.

### Conventions

Actions are captured once from `dashboardStore.getState()` because Zustand action references are stable.
The module does not parse raw event objects itself; it forwards the EventSource `data` string to the
store's parser.

### Invariants And Boundaries

Projection state and raw event history use separate EventSource connections because they have different
resume models: `/api/stream` re-snapshots; `/api/events` resumes by raw event cursor and now signals
readiness separately. This module owns only browser transport wiring, not projection interpretation or
retention.

### 2026-07-24 Curator Delta

The state EventSource now has an open deadline and uses the shared liveness watchdog. Sleep/wake can
quietly cycle an open corpse, but a fresh subscribe that never opens drops the connection to the honest
signal-lost state instead of retaining a live badge forever.

## Evidence

### Docs References

No relevant external documentation is needed beyond the browser EventSource API used directly here.

- No relevant documentation found after checking local project source and package contracts. [1]

### Repo-Internal References

- State stream snapshot and named deltas merge into the Zustand store. [2]
- Raw event stream forwards `event` rows and the backend `ready` marker. [3]
- `Cockpit` passes `markEventsHydrated` as the raw stream ready callback. [4]
- The backend raw stream emits a `ready` event once after backlog delivery. [5]

### Cross-Repo References

No meaningful cross-repo references found.

- This client transport module talks only to this package's dashboard serving endpoints. [6]
