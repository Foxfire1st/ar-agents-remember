# dashboard/src/data/conversation/reducer.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/conversation/reducer.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd` |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
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
  `ConversationMutation`); a drift in `types.ts` surfaces here first.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The pure reducer under test (recovery signals, dedupe, revision gating). | — | [reducer.ts](reducer.ts) |
| The wire grammar the fixtures mirror. | — | [types.ts](types.ts) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the reducer negative-proof
  suite (R7) — no-dup-optimistic-user-item, cursor order/idempotence, L1.4 revision-skew and L1.5
  previousCursor gap re-pages, same-revision-divergence reset, cross-identity drop, and replay-delivery
  marking. Verification is pinned to the leaf base (`0be0099`) because the new source file is
  uncommitted; closeout owns its first source stamp.
