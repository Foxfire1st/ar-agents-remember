# dashboard/src/data/store.ts

## Governing Overview

[data overview](overview.md)

## Purpose

The Zustand vanilla store backing the whole dashboard cockpit. It holds connection state, the latest
projection split into tasks keyed by entry.key and enclosures keyed by `enclosure`, plus published taskCounts,
`activeWorktreeGroups` (the worktree-group basenames with a live enclosure — the Topology's active
scope), projected `closeoutQueues`, `metrics`, `analytics`, the boot-time `servingBuild` stamp
(260703-L15 S3), a bounded
sliding window of raw Event-River events (`EVENT_WINDOW`) retained client-side until reset/reload,
the event-stream hydration flag, and optimistic attention suppression ids. `useDashboard` is the
React selector hook every cockpit component reads through. This store also owns bounded body/preparation and conditional HTTP resources across navigation; cache records do not retain React handlers. Budgets bound history, not active render size. Since 260703-L15 both apply paths are
**identity-preserving and change-gated**: a payload that stable-equals what is stored (volatile
ages ignored — `data/servedAges.ts`) performs NO store write and keeps every object identity, the
long-session flatness contract for a tab left open all day.

## Code Commentary

### Logic

`createStore` (zustand/vanilla) builds the single `dashboardStore`; `useDashboard(selector)` wraps it
in `useStore` for React subscribers. State mutates through these actions:

- `setConn` — flips the `conn` channel (`connecting` / `live` / `signal-lost`); a same-value set
  is skipped (no write).
- `applySnapshot` — merges a full `WorkspaceProjection` through `mergeKeyed` (tasks by `key`, enclosures by `enclosure`): every incoming node that `stableEquals` its stored twin
  REUSES the stored object (identity + age anchor kept); only changed/new nodes are stamped
  (`stampServed`) and swapped in, and an entirely-unchanged collection returns the EXISTING map
  object. `taskCounts`/`metrics`/`analytics`/`activeWorktreeGroups`/`servingBuild` go through the same `reuse`
  gate (a replaced analytics re-anchors all its age-bearing nodes via `stampAnalytics`). When
  nothing changed and conn is already live, applySnapshot returns without any store write. There is no agentNotifierHeartbeat field, dedicated heartbeat comparator or notifier early-return write. On a changed-content path, generatedAt advances only for content applied; a reconnect with unchanged content preserves that age anchor while restoring conn to live.
- `applyDelta` — routes the server's named deltas through `reduceDelta`, which now returns
  `null` for a no-op (a stable-equal node, a removed-marker for an absent id, an equal
  whole-value) — the caller then skips `set` entirely. Real upserts stamp the node and merge as
  before; `taskCounts`/`activeWorktreeGroups`/`metrics`/`analytics` whole-value replacements and the
  suppression prune are unchanged in semantics; unknown events are a no-op (`null`).
- `pushEvent` — parses one observer line and appends to `events` (newest last), keeping a bounded
  **sliding window** of `EVENT_WINDOW` (2000) rows: once past the bound the oldest is dropped (`slice`),
  so a long-lived tab never grows the buffer without limit. Malformed lines are swallowed so the feed
  never breaks. This is a memory bound, not the removed silent newest-N display cap — backend
  observer-log retention is the real history bound and `EventRiver` virtualizes the window.
- `markEventsHydrated` — marks the raw event stream ready after the backend emits the retained backlog
  and the `ready` SSE marker. Since 260928-MIK-L114 it also records `eventsLastTs`: the
  ready marker's last feed, else the window's newest event, else the kept value — so the
  panel names the last feed on a silent river.
- `suppressAttention` / `releaseAttention` — optimistically hide queue rows while dismiss/clear POSTs
  are in flight, and restore failed dismissals. Analytics replacement prunes suppression ids that no
  longer exist in the server-computed queue.

**Slice 05o** added the `gen` number field (init `0`) and a `reset()` action. `reset()` is the one
full dashboard-projection reset: one Zustand update increments `gen` exactly once and restores every
scenario-owned collection to its clean initial value, including fresh taskDocuments/changeSets/changeSetFiles/intentSummaries resources, zero taskCounts and `closeoutQueues: []` alongside the
id-keyed maps, `activeWorktreeGroups`, metrics/analytics, event state, servingBuild state, and
attention suppression. The dev bench calls `reset()` on each scenario mount; the engine-room canvas
is keyed by `gen` so it REMOUNTS cleanly on a scenario switch, preventing an exiting Motion
failure-overlay (e.g. the FleetingEnclosure) from the previous mode from orphaning and bleeding
through the scenario dropdown. Production does not call this reset, and the correction does not
change snapshot/delta queue ingestion, queue ordering/filtering, scheduling, or server task authority.

### Invariants And Boundaries

- `applySnapshot` merges by key with identity reuse; `applyDelta` only ever merges the named
  upsert/removed deltas the server emits — the two paths must keep the same keying
  (tasks by `key`, enclosures by `enclosure`) or deltas will fail to land on
  snapshot-seeded entries.
- **The change gate (260703-L15):** equality at the apply boundary is `stableEquals` (volatile age
  fields ignored — the exact mirror of the server diff), so a reconnect snapshot whose only
  differences are ages/`generatedAt` is a true no-op: `getState()` returns the SAME state object,
  subscribers never fire. Every node the store APPLIES is stamped through `stampServed` so age
  displays can advance locally; nodes reused by identity keep their original (correct) anchor.
- `servingBuild` is wire-optional (a pre-L15 server sends none → `null`, the stamp renders
  nothing); `reset()` clears it like every other collection.
- Unchanged live snapshots are complete zero-write no-ops; no notifier-specific comparator bypasses the content gate. reset clears only the actual current projection/state fields.
- The store keeps only a bounded sliding window of received Event River rows (`EVENT_WINDOW`), dropping
  the oldest past the bound — a memory bound for a long-lived tab, NOT the removed silent newest-N display
  cap. The real history bound is backend observer-log retention; `EventRiver` virtualizes this window, so
  the store bound is about memory, not what the user can scroll.
- Optimistic attention suppression is client-local display state only; the server remains the authority
  for `analytics.attentionQueue`.
- A full scenario reset is total over scenario-owned projected state. `closeoutQueues` must clear in
  the same canonical Zustand transaction as every other projection; a caller-local queue cleanup,
  second reset authority, or render-time filter would leave shared state dishonest.
- In PRODUCTION nothing calls `reset()`, so `gen` stays `0` and the canvas is never remounted by it —
  `gen` is a dev-bench affordance, not a production projection field. `reset()` is the only writer of
  `gen`, clears queue/event/suppression state for the next scenario, and must not be expanded into a
  production queue-retention policy.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The stable-equality + arrival-anchor module the merge is built on (volatile set mirror). [1]
- `servingBuild` [2]
- Observer event type for the Event River tail. [3]

- Store state initializes every projected collection, including `closeoutQueues`, and the canonical reset restores them together while incrementing `gen` once. [4]

- `pushEvent` keeps a bounded `EVENT_WINDOW` sliding window (oldest dropped); `reset` clears event/suppression state. [5]
- `EventRiver` virtualizes this window, so the store bound is memory-only, not a display cap. [6]
- `ScenarioPlayer` invokes the one store reset when a development scenario changes. [9]
- The mounted queue consumer reads `closeoutQueues` directly, scopes by sprint, and renders nothing when no matching queue remains. [10]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
