# dashboard/src/data/stream.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Thin EventSource wiring for the dashboard frontend. `connectState` subscribes to the folded projection
stream and merges snapshot/delta events into the Zustand store; `connectEvents` subscribes to the raw
observer-event stream that feeds the Event River.

## Code Commentary

### Logic

`STATE_EVENTS` lists the named deltas this browser connection subscribes to — the keyed-collection events
(`task`/`enclosure` plus their `.removed` markers) and the whole-value replacements
(`taskCounts`, `activeWorktreeGroups`, `metrics`, `analytics`). There is no named `closeoutQueues` listener or matching delta reducer here; full snapshot application separately retains `projection.closeoutQueues`. This listener list must not be read as proof that every snapshot field has a corresponding delta. `activeWorktreeGroups` (task 33) is the bounded
active-enclosure set the Topology constellation filters on; its delta arrives as a wrapped
`{activeWorktreeGroups: [...]}` marker the store unwraps. `connectState(base)` opens
`GET /api/stream`, applies full `snapshot` payloads through `store.applySnapshot`, sends named deltas to
`store.applyDelta`, and maps EventSource `open`/`error` to the connection badge state. Each subscribe reads `reviewMemoryScope()` and, when present, adds `reviewRepo`, `reviewMaster` and `reviewLeaf` query parameters. Guarded `review.memory` handlers mark watchdog liveness, parse and publish the payload with an initial flag, then clear that flag; `review.memory.error` handlers parse and publish errors without marking liveness. The initial flag resets on every EventSource `open`. Scope notifications reuse the reopen function, and disposal unsubscribes them before stopping the watchdog and closing the source. The imported watch owner chooses the first registered scope, checks publication scope/revision, and notifies matching registrations for a missing baseline, changed revision or initial message; matching errors invoke failure callbacks. These checks do not establish server authorization. `connectEvents`
opens `GET /api/events`, forwards each raw `event` payload to the supplied `onLine` callback, and invokes
the optional `onReady` callback when the backend emits its explicit `ready` marker after retained backlog
delivery. Since 260928-MIK-L114 the callback receives the parsed marker: `parseReady`
hands the opener `{ lastEventTs }` when it names one, and an unreadable marker still
opens the gate. The current connectEvents signature contains onLine, base and optional onReady only. It has no onInterrupt/error callback or seat-event backlog reconciler; the state stream retains its independent open/error connection status.

### Conventions

Actions are captured once from `dashboardStore.getState()` because Zustand action references are stable.
The raw `connectEvents` event handler forwards the EventSource `data` string unchanged to `onLine`; `parseReady` parses its ready marker separately. State snapshots, deltas and review-memory messages are JSON-parsed in this module.

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


- The state channel's `connectState`: one `EventSource` over `/api/stream` merging the snapshot and each named delta into the store, with a bounded open deadline and the liveness watchdog. [1]


### Repo-Internal References


- State stream snapshot and named deltas merge into the Zustand store. 


- Raw event stream forwards `event` rows and the backend `ready` marker. [3]


- `Cockpit` passes `markEventsHydrated` as the raw stream ready callback.


- The backend raw stream emits a `ready` event once after backlog delivery. [5]


- The browser listener table has task/count and operational events, but no closeoutQueues named listener. [7]
- Snapshot application separately retains closeoutQueues alongside canonical tasks and operational projections. [8]

### Cross-Repo References

No meaningful cross-repo references found.

- connectState reads optional review-memory scope into request parameters, guards handlers against stopped or replaced sources, publishes parsed memory messages with an initial flag reset on open, and publishes parsed errors separately. Memory messages mark watchdog liveness; memory errors do not. Disposal unsubscribes scope notifications. [9]
- The watch owner selects the first registered scope. Registration changes notify scope listeners when that selected scope changes and reset the revision baseline. publishReviewMemory checks matching scope and a string revision, then notifies matching registrations for an undefined baseline, initial message or changed revision. publishReviewMemoryError invokes matching failure callbacks. These are client coordination checks, not authentication. [10]
- The client opens this package’s state and raw-event endpoints through the separate connectState and connectEvents owners; memory scope reuses the existing state connection.

attachReviewListeners now owns the guarded review.memory, review.memory.error and review.explainer.moved listeners. A current moved event marks watchdog liveness and publishes to the exact-scope moved-notice subscribers; it does not change snapshot/delta ownership. One isCurrent predicate excludes a stopped or replaced source for all state handlers. The memory initial-baseline flag is a shared mutable holder reset on open, preserving the prior reconciliation behavior.

- attachReviewListeners now owns the guarded review.memory, review.memory.error and review.explainer.moved listeners. A current moved event marks watchdog liveness and publishes to the exact-scope moved-notice subscribers; it does not change snapshot/delta ownership. One isCurrent predicate excludes a stopped or replaced source for all state handlers. The memory initial-baseline flag is a shared mutable holder reset on open, preserving the prior reconciliation behavior. [11]


Anchor: `connectState` [2]

- Retired at the fifth freeze d59c3493: dashboard/src/cockpit/Cockpit.tsx:383-383 - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one; dashboard/src/data/stream.ts:29-129 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 842b487b854503d95c9c2d9dce1841198ba93c7d; dashboard/src/data/stream.ts:141-150 - the region it cited is not in the file at the candidate and no re-point was possible; dashboard/src/data/stream.ts:31-131 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit de5a7adbb21b2f6f22c3ced0eed9dd7189fe93c7; dashboard/src/data/stream.ts:162-171 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit a145b98949e9ade6a12d096568bc7d014c71607b. Retired means the anchor no longer stands, not that the cited subject was deleted.
