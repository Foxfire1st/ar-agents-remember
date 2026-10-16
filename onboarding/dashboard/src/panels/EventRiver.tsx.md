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

Reads store events and hydration; memoized displayEvents reverses raw rows, calls summarizeEvent directly and filters only explicit hidden visibility, with no lifecycle/document context join or readiness gate. The list is **virtualized**: `useVirtualizer` is driven by a state-backed
scroll ref (`useState`, not `useRef`, so attaching the element re-renders and the virtualizer measures it —
a `useRef` would see a null element on the first measure and mount nothing), counts `displayEvents`,
estimates `ROW_ESTIMATE` per row, and keys rows by event id. Only `getVirtualItems()` mounts; the `ul` is
sized to `getTotalSize()` and each `EventRow` is absolutely positioned at `translateY(item.start)` with
`measureElement` as its ref so real heights replace the estimate. Before the raw stream hydration marker
arrives it shows `Syncing event history.` and titles the panel with `syncing`, so a reload does not briefly
claim an empty river before backlog delivery finishes. Each `EventRow` is a `row` Panda `cva` keyed on
`trust` (observed/approved -> mint, declared -> amber, inferred -> cyan; unknown -> grid base). The meta
line uses `actorLabel` (so protocol `model` displays as `agent`), `trustLabel`, explicit caller/task context, formatter metadata, and `formatEventTime` instead of slicing ISO strings.

eventSummary formats read.packet and tool.completed from explicit fields and preserves unknown kinds verbatim. EventRiver remains rendering glue: Panel fill bounds its scroll viewport, title count names raw rows and empty/displayable states are distinguished.

### 260928-MIK-L114 Last-Fed Head

The head names when the river was last fed: `newestFedTs` takes the newest valid timestamp
across the window and the store's last feed — never arrival position, so a source-order
replay or a late older arrival cannot move it backwards. With an empty window and a known
feed it says so with that time; with no feed anywhere it keeps "No events yet".

### Invariants And Boundaries

Read-only: trust colour never promotes declared evidence to observed. Raw events are not rewritten or joined to task/lifecycle catalogues. Every retained raw row can be summarized without projection readiness. Virtualization bounds mounted DOM, while the store window/backend retention/reset own lifetime; there is no newest-N display slice.

## Evidence

### Repo-Internal References

- The raw event channel (single-encoded) it consumes. [1]
- The `ObserverEvent` shape (trust/actor/kind/data). [2]

- The formatter layer that owns per-kind Event River copy. [3]



- Current completed calls delegate to the workspace Event River writer. Rendering old read.packet data does not restore the deleted ambient emitter. [4]
- The store's bounded sliding window this virtualizes over. [6]

- The render tests pinning readable event rows (now over a virtualized list). [7]

- `EventRiver` virtualizes the displayed rows with `@tanstack/react-virtual` (`useVirtualizer`) over a state-backed scroll ref; only the visible window mounts as absolutely-positioned measured rows, with no newest-N slice. [11]

## Current L5I Maintenance

`EventRiver` is now memoized as a persistent rail panel. Shell rerenders caused solely by cockpit
view changes no longer reconstruct this virtualized subtree; its own dashboard-store subscriptions
remain the source of genuine event updates.
