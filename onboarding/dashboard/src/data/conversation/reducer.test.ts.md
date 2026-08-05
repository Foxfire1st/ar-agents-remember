# dashboard/src/data/conversation/reducer.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/conversation/reducer.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-01T09:50+02:00 |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51` |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview | `overview.md` |

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

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The pure reducer under test (recovery signals, dedupe, revision gating). | `applyInitialPage`; `applyEvent`; `applyOlderPage` | dashboard/src/data/conversation/reducer.ts:168-202; dashboard/src/data/conversation/reducer.ts:205-229; dashboard/src/data/conversation/reducer.ts:246-286 |
| The wire grammar the fixtures mirror. | `ConversationItem`; `ConversationEventEnvelope`; `ConversationMutation` | dashboard/src/data/conversation/types.ts:158-176; dashboard/src/data/conversation/types.ts:300-325; dashboard/src/data/conversation/types.ts:327-336 |
| The local `page`/`envelope` wrappers and the fourteen cases they drive. | "function page", "function envelope" | dashboard/src/data/conversation/reducer.test.ts:27-27; dashboard/src/data/conversation/reducer.test.ts:31-31 |
| The shared item/page/identity builders and the `eventCursor` mint the fixtures now use. | `eventCursor` | dashboard/src/test/fixtures/conversationWire.ts:58-60 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-01T09:50+02:00 — 260731-EFA-L4 curator: the Invariants section said "Fixtures mirror the
  SC1 wire grammar … a drift in `types.ts` surfaces here first", which the diff against `abc7cbc`
  made only half true — the 60-line local fixture block (the `item` factory, the whole hand-built
  page including its `cap()`/`attachCap()` capability tree) is gone, replaced by
  `test/fixtures/conversationWire.ts`, so grammar drift now lands in that shared builder and reaches
  this suite through it. Corrected that, and recorded the `eventCursor` mints that replaced the
  `"evt-0" as ActiveEventCursor` casts. Confirmed the suite is still exactly fourteen cases with
  unchanged names, and checked the one data delta the swap introduces before leaving the behavioral
  bullets alone: the shared `conversationCapabilities()` leaves carry `evidenceTier: "adapter"` and
  `reason: ""` where the local `cap()` wrote `"runtime-fixture"`/`"ok"`, and the attachment leaves
  carry real limits instead of zeros — but `reducer.ts` contains no reference to `capabilities` at
  all (it stores the page's tree and never reads it), so no case's outcome depends on any of it. The
  page shape is otherwise the same, including `page.totalItems = items.length`, which the local
  helper also set and which the first case still asserts as `proj.totalItems === 2`.

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the reducer negative-proof
  suite (R7) — no-dup-optimistic-user-item, cursor order/idempotence, L1.4 revision-skew and L1.5
  previousCursor gap re-pages, same-revision-divergence reset, cross-identity drop, and replay-delivery
  marking. Verification is pinned to the leaf base (`0be0099`) because the new source file is
  uncommitted; closeout owns its first source stamp.
