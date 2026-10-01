# dashboard/src/data/conversation/reducer.test.ts

## Governing Overview

[data/conversation overview](overview.md)

## Purpose

The negative-proof suite for the authority-sensitive `reducer.ts` (R7). It is the durable evidence
that the pure reducer never invents an item, never corrupts streamed text under gaps, and recovers
deterministically — the exact failure classes R7 forbids. Fourteen vitest cases run without a network
by driving `applyInitialPage`/`applyEvent`/`applyOlderPage` directly with typed page/envelope
fixtures.

## Code Commentary

### Logic — what each case proves and why it is required

- **Initial-page order + resume cursor** — `applyInitialPage` sorts by `globalOrdinal` and captures
  the atomic `eventCursor` as the resume point.
- **Live append advances the cursor + stream=live** — the normal streaming path.
- **Dedupe by `eventId`+`cursor`** — an exact replay on reconnect adds no duplicate (idempotent
  reconnect).
- **NEVER a duplicate optimistic user item** — a user item delivered `pending` then `upsert`ed to
  `completed` stays a SINGLE item; there is no client-authored echo (R2/§12.5 — the headline R7 proof).
- **Block delta at expected revision, idempotent on replay** — a streamed delta appends text and a
  replay at the already-applied revision is ignored.
- **Revision-skew → conservative re-page (L1.4)** — a delta whose `expectedRevision` does not match
  (a missed intermediate delta) re-pages rather than corrupting text; the block stays uncorrupted.
- **`previousCursor` gap → conservative re-page (L1.5)** — a live event whose `previousCursor` names
  an unreceived retained cursor re-pages and the out-of-order event is NOT applied.
- **`gap` mutation → repage recovery + `gap` stream** — an established-stream gap freezes apply and
  asks for a re-page.
- **Same-revision / different-payload → reset fault (§6.4)** — a protocol fault deterministically
  resets and records `fault`.
- **Stale/lower-revision status ignored** — an out-of-order status does not regress turn state.
- **Older-page prepend preserves items + resume cursor** — infinite-older paging never moves the live
  event resume point.
- **`replace-page` re-hydrates and clears applied keys + recovery** — a native rehydrate establishes
  a new baseline and clears the recovery signal.
- **Cross-identity/epoch events dropped** — a foreign `bridgeEpoch` never merges (no cross-generation
  merge).
- **Replay/hydration deliveries marked** — `lastAppliedDelivery` records `resume-replay` so announcers
  stay silent on non-live deliveries (§6.8/§14.5).

### Invariants And Boundaries

- Pure-reducer testing: no network, no store, no DOM — the same purity that lets the store, the
  stream, and this suite share one reducer truth.
- Fixtures mirror the SC1 wire grammar (`ConversationItem`/`ConversationEventEnvelope`/
  `ConversationMutation`). The item, page and identity fixtures come from
  `test/fixtures/conversationWire.ts` (`conversationItem`, `conversationPage`,
  `conversationIdentity`), so a drift in `types.ts` now surfaces in that shared builder first and
  reaches this suite through it; the `envelope(...)` helper stays local and is checked directly
  against `ConversationEventEnvelope`, which is where an envelope-level drift still lands first.
- The branded cursors are minted, not asserted: `eventCursor("evt-0")` replaces the
  `"evt-0" as ActiveEventCursor` casts. `ActiveEventCursor` is `string & { __brand }` — an opaque
  server-issued token with no structure to check — so a single registered mint is the honest form,
  and the mint is the only remaining assertion in these fixtures.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The pure reducer under test (recovery signals, dedupe, revision gating). [1]
- The wire grammar the fixtures mirror. [2]
- The local `page`/`envelope` wrappers and the fourteen cases they drive. [3]
- The shared item/page/identity builders and the `eventCursor` mint the fixtures now use. [4]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
