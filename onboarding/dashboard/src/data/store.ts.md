# dashboard/src/data/store.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/store.ts`                    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-07T05:18+02:00                           |
| lastVerifiedCommitHash |                                                  `6ea2a422210b4b9797d2c7c8df5f9994813f9331`|
| lastVerifiedCommitDate |                                                  2026-07-06T21:07:46+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The Zustand vanilla store backing the whole dashboard cockpit. It holds connection state, the latest
projection split into flat id-keyed maps (`lifecycles` / `enclosures` / `providers`),
`activeWorktreeGroups` (the worktree-group basenames with a live enclosure — the Topology's active
scope), `metrics`, `analytics`, the boot-time `servingBuild` stamp (260703-L15 S3), a bounded
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
  NOTHING changed and `conn` is already live, the action returns without calling `set` at all —
  an idle reconnect re-snapshot costs zero writes/re-renders. `generatedAt` advances only when
  content applied (it is the "ages as of" stamp the top bar shows — coherence rule).
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

**Slice 05o** added the `gen` number field (init `0`) and a `reset()` action. `reset()` clears every
collection back to empty (`lifecycles`/`enclosures`/`providers` to `{}`, `metrics`/`analytics`/
`generatedAt` to `null`, `events` to `[]`) AND increments `gen`. The dev bench calls `reset()` on each
scenario mount; the engine-room canvas is keyed by `gen` so it REMOUNTS cleanly on a scenario switch,
preventing an exiting Motion failure-overlay (e.g. the FleetingEnclosure) from the previous mode from
orphaning and bleeding through the scenario dropdown. `reset()` also clears `activeWorktreeGroups` to
`[]`.

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
- The store keeps only a bounded sliding window of received Event River rows (`EVENT_WINDOW`), dropping
  the oldest past the bound — a memory bound for a long-lived tab, NOT the removed silent newest-N display
  cap. The real history bound is backend observer-log retention; `EventRiver` virtualizes this window, so
  the store bound is about memory, not what the user can scroll.
- Optimistic attention suppression is client-local display state only; the server remains the authority
  for `analytics.attentionQueue`.
- In PRODUCTION nothing calls `reset()`, so `gen` stays `0` and the canvas is never remounted by it —
  `gen` is a dev-bench affordance, not a production projection field. `reset()` is the only writer of
  `gen`, and it also clears event hydration and suppressed attention ids for the next scenario.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The stable-equality + arrival-anchor module the merge is built on (volatile set mirror). | — | [servedAges.ts](servedAges.ts) |
| Projection types the store maps over (incl. the optional `servingBuild`). | — | [../types/projection.ts](../types/projection.ts) |
| Observer event type for the Event River tail. | — | [../types/event.ts](../types/event.ts) |
| Store state now carries `eventsHydrated` and optimistic `suppressedAttentionIds`. | L29-L31; L120-L122 | [store.ts](store.ts) |
| `pushEvent` keeps a bounded `EVENT_WINDOW` sliding window (oldest dropped); `reset` clears event/suppression state. | L42-L46; L139-L180 | [store.ts](store.ts) |
| `EventRiver` virtualizes this window, so the store bound is memory-only, not a display cap. | — | [../panels/EventRiver.tsx](../panels/EventRiver.tsx) |

## Update History

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
