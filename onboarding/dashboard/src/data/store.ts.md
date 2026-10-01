# dashboard/src/data/store.ts

## Governing Overview

[data overview](overview.md)

## Purpose

The Zustand vanilla store backing the whole dashboard cockpit. It holds connection state, the latest
projection split into flat id-keyed maps (`lifecycles` / `enclosures` / `providers`),
`activeWorktreeGroups` (the worktree-group basenames with a live enclosure — the Topology's active
scope), projected `closeoutQueues`, `metrics`, `analytics`, the boot-time `servingBuild` stamp
(260703-L15 S3), a bounded
sliding window of raw Event-River events (`EVENT_WINDOW`) retained client-side until reset/reload,
the event-stream hydration flag, and optimistic attention suppression ids. `useDashboard` is the
React selector hook every cockpit component reads through. Since 260703-L15 both apply paths are
**identity-preserving and change-gated**: a payload that stable-equals what is stored (volatile
ages ignored — `data/servedAges.ts`) performs NO store write and keeps every object identity, the
long-session flatness contract for a tab left open all day.

## Code Commentary

### Logic

`createStore` (zustand/vanilla) builds the single `dashboardStore`; `useDashboard(selector)` wraps it
in `useStore` for React subscribers. State mutates through these actions:

- `setConn` — flips the `conn` channel (`connecting` / `live` / `signal-lost`); a same-value set
  is skipped (no write).
- `applySnapshot` — merges a full `WorkspaceProjection` through `mergeKeyed` (lifecycles/providers
  by `id`, enclosures by `enclosure`): every incoming node that `stableEquals` its stored twin
  REUSES the stored object (identity + age anchor kept); only changed/new nodes are stamped
  (`stampServed`) and swapped in, and an entirely-unchanged collection returns the EXISTING map
  object. `metrics`/`analytics`/`activeWorktreeGroups`/`servingBuild` go through the same `reuse`
  gate (a replaced analytics re-anchors all its age-bearing nodes via `stampAnalytics`). When
  NOTHING changed and `conn` is already live, the action returns early (260707-HFX2-L2 R5, fix
  round 2): it calls `set({ agentNotifierHeartbeat })` only when `heartbeatEquals(state.
  agentNotifierHeartbeat, agentNotifierHeartbeat)` is false, then always returns — a truly idle
  heartbeat (including `null`/`null`) still performs zero store writes on this path. A dedicated
  `heartbeatEquals` comparator is used instead of the general `stableEquals` gate because
  `stableEquals` strips `ageSeconds` (it's in `VOLATILE_AGE_FIELDS`), which is exactly the field a
  genuine heartbeat tick advances — reusing `stableEquals` here would silently treat every
  advancing tick as unchanged. `heartbeatEquals` compares `lastTickAt`/`ageSeconds`/
  `staleCutoffSeconds`/`stale` and, since HFX2-L8, the latest pending inbox count,
  redeliverable inbox count, and sweep duration literally, ages included. Every other field on that early-return
  path stays untouched (identity-preserving). On the normal (changed-content) path, `generatedAt`
  advances only when content applied (it is the "ages as of" stamp the top bar shows — coherence
  rule); `agentNotifierHeartbeat` is set alongside it.
- `applyDelta` — routes the server's named deltas through `reduceDelta`, which now returns
  `null` for a no-op (a stable-equal node, a removed-marker for an absent id, an equal
  whole-value) — the caller then skips `set` entirely. Real upserts stamp the node and merge as
  before; `activeWorktreeGroups`/`metrics`/`analytics` whole-value replacements and the
  suppression prune are unchanged in semantics; unknown events are a no-op (`null`).
- `pushEvent` — parses one observer line and appends to `events` (newest last), keeping a bounded
  **sliding window** of `EVENT_WINDOW` (2000) rows: once past the bound the oldest is dropped (`slice`),
  so a long-lived tab never grows the buffer without limit. Malformed lines are swallowed so the feed
  never breaks. This is a memory bound, not the removed silent newest-N display cap — backend
  observer-log retention is the real history bound and `EventRiver` virtualizes the window.
- `markEventsHydrated` — marks the raw event stream ready after the backend emits the retained backlog
  and the `ready` SSE marker.
- `suppressAttention` / `releaseAttention` — optimistically hide queue rows while dismiss/clear POSTs
  are in flight, and restore failed dismissals. Analytics replacement prunes suppression ids that no
  longer exist in the server-computed queue.

**Slice 05o** added the `gen` number field (init `0`) and a `reset()` action. `reset()` is the one
full dashboard-projection reset: one Zustand update increments `gen` exactly once and restores every
scenario-owned collection to its clean initial value, including `closeoutQueues: []` alongside the
id-keyed maps, `activeWorktreeGroups`, metrics/analytics, event state, serving/notifier state, and
attention suppression. The dev bench calls `reset()` on each scenario mount; the engine-room canvas
is keyed by `gen` so it REMOUNTS cleanly on a scenario switch, preventing an exiting Motion
failure-overlay (e.g. the FleetingEnclosure) from the previous mode from orphaning and bleeding
through the scenario dropdown. Production does not call this reset, and the correction does not
change snapshot/delta queue ingestion, queue ordering/filtering, scheduling, or lifecycle authority.

### Invariants And Boundaries

- `applySnapshot` merges by key with identity reuse; `applyDelta` only ever merges the named
  upsert/removed deltas the server emits — the two paths must keep the same keying
  (lifecycles/providers by `id`, enclosures by `enclosure`) or deltas will fail to land on
  snapshot-seeded entries.
- **The change gate (260703-L15):** equality at the apply boundary is `stableEquals` (volatile age
  fields ignored — the exact mirror of the server diff), so a reconnect snapshot whose only
  differences are ages/`generatedAt` is a true no-op: `getState()` returns the SAME state object,
  subscribers never fire. Every node the store APPLIES is stamped through `stampServed` so age
  displays can advance locally; nodes reused by identity keep their original (correct) anchor.
- `servingBuild` is wire-optional (a pre-L15 server sends none → `null`, the stamp renders
  nothing); `reset()` clears it like every other collection.
- **`agentNotifierHeartbeat` is deliberately EXCLUDED from the general `unchanged` change-gate check
  (260707-HFX2-L2 R5)** — it is a live tick age injected app-side at response time (mirroring the
  backend's own `delta.py` "volatile ages excluded" posture), so it is evaluated even on the
  content-unchanged early-return path. Unlike a bypass of the identity-preserving no-write
  guarantee, it has its OWN dedicated equality check gating the write (`heartbeatEquals`, fixed in
  fix round 2 — see Update History): `if (unchanged && state.conn === "live") { if
  (!heartbeatEquals(state.agentNotifierHeartbeat, agentNotifierHeartbeat)) { set({ agentNotifierHeartbeat
  }); } return; }`. So the store still writes only when something actually changed — just via a
  heartbeat-specific comparator that (unlike `stableEquals`) does not strip `ageSeconds`, since
  that's precisely the field a genuine tick advance shows up in. `reset()` clears it to `null` like
  every other collection.
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
- `AgentNotifierHeartbeat` type this store carries, including the L8 backlog/duration fields, and the app-injected payload it mirrors; the wire fallback accepts the legacy `supervisorHeartbeat` key during the rename window. [7]
- `AgentNotifierHeartbeatBadge` reads `s.agentNotifierHeartbeat` from this store to render the top-bar tick-age and inbox-backlog indicator. [8]
- `ScenarioPlayer` invokes the one store reset when a development scenario changes. [9]
- The mounted queue consumer reads `closeoutQueues` directly, scopes by sprint, and renders nothing when no matching queue remains. [10]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
