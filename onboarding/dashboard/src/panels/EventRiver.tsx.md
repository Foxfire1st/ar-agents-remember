# dashboard/src/panels/EventRiver.tsx

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

## Evidence

### Repo-Internal References

- The raw event channel (single-encoded) it consumes. [1]
- The `ObserverEvent` shape (trust/actor/kind/data). [2]
- The formatter layer that owns per-kind Event River copy. [3]
- The emitter of `tool.completed` and `read.packet` facts this row renders. [4]
- Existing lifecycle/enclosure/task-document helpers used for task labels. [5]
- The store's bounded sliding window this virtualizes over. [6]
- The render tests pinning readable event rows (now over a virtualized list). [7]
- `EventRiver` memoizes the displayed list (reverse to newest-first, gate on `eventSummaryContextReady`, drop hidden rows). [8]
- `eventSummaryContextReady` requires lifecycle/enclosure/task-document context for bound events. [9]
- The reload-order regression keeps a lifecycle-bound tool row hidden until task-document context arrives. [10]
- `EventRiver` virtualizes the displayed rows with `@tanstack/react-virtual` (`useVirtualizer`) over a state-backed scroll ref; only the visible window mounts as absolutely-positioned measured rows, with no newest-N slice. [11]

## Current L5I Maintenance

`EventRiver` is now memoized as a persistent rail panel. Shell rerenders caused solely by cockpit
view changes no longer reconstruct this virtualized subtree; its own dashboard-store subscriptions
remain the source of genuine event updates.
