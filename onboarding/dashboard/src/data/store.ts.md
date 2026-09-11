# dashboard/src/data/store.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/store.ts`                    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-24T12:59+02:00 |
| lastVerifiedCommitHash |                                                  `dc03c64a91947cee470622c560c516854eec86b5`|
| lastVerifiedCommitDate |                                                  2026-08-30T17:41:53+02:00|
| governingOverview | `overview.md` |

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

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The stable-equality + arrival-anchor module the merge is built on (volatile set mirror). | "export const VOLATILE_AGE_FIELDS" | dashboard/src/data/servedAges.ts:16-16 |
| `servingBuild` | `servingBuild` | dashboard/src/types/projection.ts:828-828 |
| Observer event type for the Event River tail. | "export interface ObserverEvent" | dashboard/src/types/event.ts:9-9 |
| Store state initializes every projected collection, including `closeoutQueues`, and the canonical reset restores them together while incrementing `gen` once. | "export const dashboardStore"; `reset` | dashboard/src/data/store.ts:329-400 |
| `pushEvent` keeps a bounded `EVENT_WINDOW` sliding window (oldest dropped); `reset` clears event/suppression state. | "export const useDashboard" | dashboard/src/data/store.ts:403-403 |
| `EventRiver` virtualizes this window, so the store bound is memory-only, not a display cap. | `EventRiver` | dashboard/src/panels/EventRiver.tsx:122-122 |
| `AgentNotifierHeartbeat` type this store carries, including the L8 backlog/duration fields, and the app-injected payload it mirrors; the wire fallback accepts the legacy `supervisorHeartbeat` key during the rename window. | `AgentNotifierHeartbeat` | dashboard/src/types/projection.ts:54-65 |
| `AgentNotifierHeartbeatBadge` reads `s.agentNotifierHeartbeat` from this store to render the top-bar tick-age and inbox-backlog indicator. | `AgentNotifierHeartbeatBadge` | dashboard/src/cockpit/Cockpit.tsx:959-984 |
| `ScenarioPlayer` invokes the one store reset when a development scenario changes. | `ScenarioPlayer`; `reset` | dashboard/src/dev/ScenarioPlayer.tsx:21-39 |
| The mounted queue consumer reads `closeoutQueues` directly, scopes by sprint, and renders nothing when no matching queue remains. | `CloseoutQueueImpl` | dashboard/src/panels/CloseoutQueue.tsx:69-83 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History
- 2026-09-05T06:24:16+00:00: Generated citation repair: `servingBuild` repointed to dashboard/src/types/projection.ts:828-828. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-24T12:59+02:00 — 260821-DAGQC-L3 curator: documented the canonical scenario reset as
  total over scenario-owned dashboard projections, including `closeoutQueues`, in one Zustand
  transaction that increments `gen` once. Preserved the dev/test-only boundary: production
  snapshot/delta ingestion, queue ordering/filtering, scheduling, and lifecycle authority remain
  unchanged. Verification metadata remains pinned until governed closeout stamps the code commit.


- 2026-08-20T10:45+02:00 — 260815-DAG-L12 curator: re-anchored citation range(s) to current source after the L12 line movement (cited files changed, card source unchanged); verification metadata unchanged.

- 2026-08-18T13:00+02:00 — No content impact: 260815-DAG-L8 added the closeout-queue projection surface (closeoutQueues); the behavior this card describes is unchanged.

- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-08T21:20+02:00 — 260713-TES-L1 curator: recorded the `agentNotifierHeartbeat` store
  field rename and the `projection.agentNotifierHeartbeat ?? projection.supervisorHeartbeat ??
  null` legacy-wire fallback in `applySnapshot`. Verification metadata pinned until closeout
  stamps the 260713-TES-L1 commit.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B24 curator: replaced the `n/a` rows with exact
  anchors and source-backed ranges; exact non-fixing check returns zero findings.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 (dead-seat storm observability, R6): `heartbeatEquals`
  now compares `pendingInboxCount`, `redeliverableInboxCount`, and `lastSweepDurationSeconds` so
  idle snapshots still write through real backlog/duration changes while preserving the no-op idle
  path for unchanged heartbeat payloads. Verification metadata pinned until closeout stamps the
  260707-HFX2-L8 commit.
- 2026-07-08T18:45+02:00 — 260707-HFX2-L2 (supervisor sweep, R5): added
  `supervisorHeartbeat: SupervisorHeartbeat | null` to `DashboardState` (init `null`, reset-cleared).
  Deliberately EXCLUDED from the `unchanged` change-gate equality check — `applySnapshot`'s
  content-unchanged early-return path now still `set({ supervisorHeartbeat })` before returning, so
  the live tick age rides through even when nothing else in the projection changed. Verification
  metadata pinned until closeout stamps the 260707-HFX2-L2 commit.
- 2026-07-08T05:36+02:00 — 260707-HFX2-L2 fix round 2 (manager-caught regression, see
  `260707-HFX2-L2-fix2-report.md`): corrected the R5 entry below — the content-unchanged
  early-return path in `applySnapshot` does NOT unconditionally `set({ supervisorHeartbeat })`.
  It now only writes when `heartbeatEquals(state.supervisorHeartbeat, supervisorHeartbeat)` is
  false, then always returns, so a truly idle heartbeat (incl. `null`/`null`) across an idle
  re-snapshot performs zero store writes. Added `heartbeatEquals`, a dedicated field-literal
  comparator over `lastTickAt`/`ageSeconds`/`staleCutoffSeconds`/`stale`, used instead of the
  general `stableEquals` gate specifically because `stableEquals` strips `ageSeconds` (a
  `VOLATILE_AGE_FIELDS` member) — the exact field a genuine tick advance must be detected in, so
  reusing `stableEquals` here would have silently defeated the point of a live tick.
- 2026-07-07T05:18+02:00 — 260703-L15 (S1 + S3): both apply paths became identity-preserving and
  change-gated — `mergeKeyed`/`reuse` over `stableEquals`, `reduceDelta` returns `null` for
  no-ops, an unchanged snapshot performs zero store writes, applied nodes are age-anchored via
  `stampServed`/`stampAnalytics`, `generatedAt` advances only with applied content; `byKey` left
  (replaced by `mergeKeyed`). Added `servingBuild: ServingBuild | null` (snapshot-fed, reset-
  cleared) for the top-bar stale-server stamp.
  Verification metadata pinned until closeout stamps the L15 commit.
- 2026-06-28T13:54+02:00 — Task 34: `pushEvent` now keeps a bounded **sliding window** of the raw feed
  (`EVENT_WINDOW` = 2000), dropping the oldest past the bound, so `events` is no longer unbounded. This is
  a memory bound for a long-lived tab, NOT the removed silent newest-N display cap — backend observer-log
  retention is the real history bound and `EventRiver` virtualizes the window. Verification metadata pinned
  until closeout stamps the task-34 code commit.
- 2026-06-28T07:32+02:00 — Task 29 S7 follow-up: removed stale bounded-tail documentation; the store now
  keeps all received Event River rows until reset/reload, tracks raw-event hydration readiness, and holds
  optimistic attention suppression ids for sluggish dismiss/clear POSTs. Verification metadata pinned
  until closeout stamps the task-29 code commit.
- 2026-06-28T07:30+02:00 — Task 33: added `activeWorktreeGroups: string[]` to `DashboardState` (init `[]`),
  populated by `applySnapshot` (`projection.activeWorktreeGroups ?? []`), cleared by `reset()`, and
  carried by a new `reduceDelta` case `"activeWorktreeGroups"` (whole-value replacement that unwraps the
  `{activeWorktreeGroups}` marker). This is the Topology's active-scope input. Verification metadata
  pinned until closeout stamps the code commit.
- 2026-06-22T16:00 — slice 05o: added the `gen` generation counter (init 0) and the `reset()` action
  that clears every collection back to empty AND bumps `gen`, so the dev bench can force a clean
  engine-room canvas REMOUNT (keyed by `gen`) on each scenario switch and avoid orphaned
  previous-mode overlay bleed; production never calls `reset()`, so `gen` stays 0. Created this
  sidecar for the previously-untracked store. Verification metadata pinned until closeout stamps the
  05o code commit.
