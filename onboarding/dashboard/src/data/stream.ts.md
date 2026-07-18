# dashboard/src/data/stream.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/stream.ts`                   |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `e2b99dcd71fb6ca31f642dd61c3c16f3d3d05bf5`       |
| lastVerifiedCommitDate | 2026-07-17T02:52:07+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No relevant external documentation is needed beyond the browser EventSource API used directly here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant documentation found after checking local project source and package contracts. | N/A | [dashboard/src/data/stream.ts](stream.ts) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| State stream snapshot and named deltas merge into the Zustand store. | L17-L34 | [stream.ts](stream.ts) |
| Raw event stream forwards `event` rows and the backend `ready` marker. | L36-L50 | [stream.ts](stream.ts) |
| `Cockpit` passes `markEventsHydrated` as the raw stream ready callback. | L172-L181 | [../cockpit/Cockpit.tsx](../cockpit/Cockpit.tsx) |
| The backend raw stream emits a `ready` event after backlog delivery. | L151-L177 | [agents-remember/mcp/src/agents_remember/serving/events.py](agents-remember/mcp/src/agents_remember/serving/events.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This client transport module talks only to this package's dashboard serving endpoints. | N/A | [stream.ts](stream.ts) |

## Update History

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T02:30+02:00 — 260715-FEUI-L2 (review finding 2): `connectEvents` gained the optional
  `onInterrupt` callback wired to the EventSource `error` event — the reconnect signal the
  seat-event per-connection backlog gate re-closes on (a reconnect replays backlog before its own
  `ready`; an undecodable cursor replays the full initial window). Verification metadata pinned
  to the leaf base until closeout stamps the L2 code commit.
- 2026-06-28T15:30+02:00 — Task 33: documented the `activeWorktreeGroups` entry added to `STATE_EVENTS`
  (the bounded active-enclosure set the Topology filters on; delivered as a wrapped whole-value delta the
  store unwraps). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-28T07:32+02:00 — Task 29 S7 follow-up: created the missing sidecar and documented the
  `/api/events` ready callback used to prevent Event River empty-state flicker before backlog hydration.
  Verification metadata is pinned to the last committed file version until closeout stamps the task-29
  code commit.
