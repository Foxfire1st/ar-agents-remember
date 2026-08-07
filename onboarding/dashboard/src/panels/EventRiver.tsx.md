# dashboard/src/panels/EventRiver.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/EventRiver.tsx`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`       |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/ overview](overview.md)

## Purpose

The Event River (right rail): the readable activity feed over the raw observer feed with **trust
provenance** — the trust class is the colour, so the feed never pretends `declared` is `observed`.
Fed by the raw `/api/events` channel into the store's bounded sliding-window event list (separate from
`/api/stream`); backend observer-log retention decides what a fresh connection receives. The list is
**virtualized** with `@tanstack/react-virtual`, so only the visible window of rows mounts and render cost
stays flat no matter how long the feed grows. The panel delegates schema-aware copy to `eventSummary.ts`,
so known protocol events render as human activity text while unknown events fall back honestly to raw
`event.kind`.

## Code Commentary

### Logic

Reads `store.events`, `eventsHydrated`, lifecycle projections, enclosures, and analytics task documents.
A **memoized** `displayEvents` reshape (recomputed only when its inputs change, not every render) builds an
`EventSummaryContext` with `buildEventSummaryContext`, copies and reverses all received events (newest
first), drops lifecycle/enclosure-bound rows until `eventSummaryContextReady` says their summary context
exists, summarizes the rest through `summarizeEvent`, and hides rows whose summary visibility is `hidden`
(currently lifecycle heartbeats). The list is **virtualized**: `useVirtualizer` is driven by a state-backed
scroll ref (`useState`, not `useRef`, so attaching the element re-renders and the virtualizer measures it —
a `useRef` would see a null element on the first measure and mount nothing), counts `displayEvents`,
estimates `ROW_ESTIMATE` per row, and keys rows by event id. Only `getVirtualItems()` mounts; the `ul` is
sized to `getTotalSize()` and each `EventRow` is absolutely positioned at `translateY(item.start)` with
`measureElement` as its ref so real heights replace the estimate. Before the raw stream hydration marker
arrives it shows `Syncing event history.` and titles the panel with `syncing`, so a reload does not briefly
claim an empty river before backlog delivery finishes. Each `EventRow` is a `row` Panda `cva` keyed on
`trust` (observed/approved -> mint, declared -> amber, inferred -> cyan; unknown -> grid base). The meta
line uses `actorLabel` (so protocol `model` displays as `agent`), `trustLabel`, existing task labels from
the summary context, formatter metadata, and `formatEventTime` instead of slicing ISO strings.

The panel no longer owns per-kind protocol logic. `eventSummary.ts` formats `read.packet`,
`tool.completed`, lifecycle phase/block/start/resume/promote/end events, gate events, heartbeat
suppression, and the unknown fallback. The component remains rendering glue: it renders the `Panel` with
`fill` so the Panel hosts the scroll viewport (the virtualized list scrolls beneath the sticky header band
instead of growing the panel), preserves the raw event count in the panel title, shows an empty state when
no events exist, and shows a separate "No displayable events." state when only hidden/noisy events are
present.

### Invariants And Boundaries

Read-only; the trust->colour mapping is the provenance contract (North-Star "never pretend declared
is observed"). The single-encoded raw channel is the `serving/events.py` source. The component does
not mutate or normalize event data; all display translation is client-side presentation. Task context
comes from the existing lifecycle/enclosure/task-document identity helpers via `eventSummary.ts`, not
a second lifecycle-id resolver. Hidden heartbeat rows remain in `store.events`; only the default river
render suppresses them. Lifecycle-bound rows without live lifecycle, enclosure, or task-document context
also stay out of the displayed list, avoiding reload flicker where raw ids briefly paint before projection
context arrives. The component has no newest-N display cap — the store's bounded sliding window plus
virtualization replace the removed slice, so every retained row is reachable by scrolling while only the
visible window mounts; backend retention and the store reset/reload boundary own event lifetime.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The raw event channel (single-encoded) it consumes. | `RawEvent` | mcp/src/agents_remember/serving/events.py:63-77 |
| The `ObserverEvent` shape (trust/actor/kind/data). | `ObserverEvent` | dashboard/src/types/event.ts:9-22 |
| The formatter layer that owns per-kind Event River copy. | `summarizeEvent` | dashboard/src/panels/eventSummary.ts:113-143 |
| The emitter of `tool.completed` and `read.packet` facts this row renders. | `emit_tool`; `emit_read_packet` | mcp/src/agents_remember/observer/ambient.py:405-424; mcp/src/agents_remember/observer/ambient.py:426-453 |
| Existing lifecycle/enclosure/task-document helpers used for task labels. | `taskLabel` | dashboard/src/data/taskIdentity.ts:239-256 |
| The store's bounded sliding window this virtualizes over. | `EVENT_WINDOW` | dashboard/src/data/store.ts:56-56 |
| The render tests pinning readable event rows (now over a virtualized list). | "EventRiver readable activity feed" | dashboard/src/panels/EventRiver.test.tsx:143-351 |
| `EventRiver` memoizes the displayed list (reverse to newest-first, gate on `eventSummaryContextReady`, drop hidden rows). | `EventRiver` | dashboard/src/panels/EventRiver.tsx:122-122 |
| `eventSummaryContextReady` requires lifecycle/enclosure/task-document context for bound events. | `eventSummaryContextReady` | dashboard/src/panels/eventSummary.ts:143-156 |
| The reload-order regression keeps a lifecycle-bound tool row hidden until task-document context arrives. | "waits for lifecycle summary context before rendering lifecycle-bound rows" | dashboard/src/panels/EventRiver.test.tsx:240-265 |
| `EventRiver` virtualizes the displayed rows with `@tanstack/react-virtual` (`useVirtualizer`) over a state-backed scroll ref; only the visible window mounts as absolutely-positioned measured rows, with no newest-N slice. | `virtualizer` | dashboard/src/panels/EventRiver.tsx:79-85 |

## Current L5I Maintenance

`EventRiver` is now memoized as a persistent rail panel. Shell rerenders caused solely by cockpit
view changes no longer reconstruct this virtualized subtree; its own dashboard-store subscriptions
remain the source of genuine event updates.

## Update History

- 2026-08-02T23:59:26+02:00 — L6 Wave 2 duplicate-range correction: removed 1 repeated path:start-end Citation objects from 1 same-claim citation group(s) at card line(s) 77; retained the first occurrence/order, all non-repeated anchor coverage and source ranges; scoped non-fixing result 0.
- 2026-08-02T21:08+02:00 — 260731-EFA-L6 W2-B09 curator: repaired 9 citation entries (18 findings); no Tier-3 findings.

- 2026-07-24T13:17:17Z — Curator: documented the keep-alive memo boundary for tab-switch CPU;
  verification fields remain pre-commit.

- 2026-06-28T13:54+02:00 — Task 34: the list is now **virtualized** with `@tanstack/react-virtual`
  (`useVirtualizer`) — only the visible window of rows mounts, so render cost stays flat regardless of feed
  length. Uses the `Panel` `fill` viewport + an inner scroll container via a state-backed ref (`useState`,
  not `useRef`, so attaching the element re-measures), a memoized `displayEvents` reshape, and
  absolutely-positioned measured rows (`measureElement`, `translateY(start)`). No hard display cap — the
  store's bounded sliding window plus virtualization replace the removed newest-N slice. New dependency
  `@tanstack/react-virtual`. Verification metadata pinned until closeout stamps the task-34 code commit.
- 2026-06-28T07:32+02:00 — Task 29 S7 follow-up: removed the obsolete newest-60 display-window
  documentation; the river now waits for raw-stream hydration and renders all received displayable rows
  in newest-first order, with retention owned by the backend/store boundary. Verification metadata
  pinned until closeout stamps the task-29 code commit.
- 2026-06-28T05:38+02:00 — Task 29: the displayed Event River list now gates lifecycle/enclosure-bound
  rows on summary-context readiness before summarizing/filtering, preventing reload flicker from raw
  lifecycle ids while preserving the raw event buffer. Verification metadata pinned until closeout stamps
  the task-29 code commit.
- 2026-06-26T18:14+02:00 — Task 20 readability pass: `EventRiver` now delegates
  schema-aware copy to `eventSummary.ts`, joins lifecycle events to task labels,
  renders actor/trust/time metadata through display helpers, and suppresses
  heartbeat rows in the default river while preserving raw events in the store.
  Verification metadata pinned until closeout stamps the task-20 code commit.
- 2026-06-23T01:40+02:00 — Slice 07b v1: documented the `read.packet` per-kind treatment — the river's
  one non-generic row (`readPacketSummary`): **"Read: `<basename>`"** (+ "+N more" for a batch), the
  read's repo (`data.repoId`) in the meta line, and the full path(s) on hover (`title`); everything else
  stays generic. Added the `ambient.py` emitter + `EventRiver.test.tsx` references. Body and references
  only — verification metadata pinned until closeout stamps the slice-07b code commit.
- 2026-06-15T17:00 — Created for slice 5d: migrated onto `Panel` + Panda `cva`. Verification metadata
  pinned until closeout stamps the 5d code commit.
