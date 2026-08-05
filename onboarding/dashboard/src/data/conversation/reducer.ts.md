# dashboard/src/data/conversation/reducer.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/conversation/reducer.ts`     |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-20T22:30+02:00                           |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[data/conversation overview](overview.md)

## Purpose

The **authority-sensitive pure reducer** (design §6.7-6.8, §11.1) — the core of the reconstructable
projection. It rebuilds the browser transcript PURELY from server page + event evidence and NEVER
invents an item (no optimistic user echo — R2/§12.5/R7). It is transport-agnostic and side-effect-free,
so the store, the stream, and the tests share one truth. It is the single place the load-bearing
protocol rules (cursor order, dedupe, revision gating, gap tolerance, fault reset) are enforced.

## Code Commentary

### Logic

- `ActiveConversationProjection` is the reduced state: `orderedItemIds` + `itemsById`, `eventCursor`
  (the resume point), `lastApplied` (the last cursor whose event actually applied — used for
  `previousCursor` gap detection), `olderCursor`/`hasOlder`/`totalItems`, `status`/`capabilities`,
  `lastAppliedDelivery` (so announcers can tell replay/hydration from live), `lastTouchedItemId` (the
  true announcer target, not a DOM guess), `recovery?`/`fault?`, and the bounded dedupe pair
  `appliedKeys`/`appliedKeySet`. Scroll geometry is deliberately not part of this transport reducer.

### 2026-07-24 Curator Delta

The removed `scrollAnchor` field was stale view state, not protocol evidence. The reducer now remains
strictly about page/event reduction; the timeline records and restores per-session scroll geometry only
after stable rendering, without changing cursor, replay, or recovery semantics.
- `applyInitialPage` replaces the whole projection from a freshly-hydrated page (initial/reset/native
  rehydrate), sorting by `globalOrdinal`, seeding `lastApplied = page.eventCursor` (so the very first
  live event's `previousCursor` is gap-checked against it), and clearing the dedupe set.
- `applyOlderPage` PREPENDS an older page while preserving the live resume cursor and never regressing
  a live-updated item (keeps the newer revision); `totalItems` moves only on an honest exact total.
- `applyEvent` is the gate: drop cross-identity events (`sameIdentity` = `arSessionId`+`bridgeEpoch`,
  never digest — L4-facing note 4); drop `eventId+cursor` duplicates (idempotent reconnect/replay); a
  `gap` mutation freezes apply and signals `repage`; a LIVE event whose `previousCursor` names a cursor
  never applied signals `repage` (`previous-cursor-gap`, L1.5 — `replace-page` bypasses it as a new
  baseline); otherwise `applyMutation` runs and, on success, `rememberKey` records the key and advances
  `eventCursor`/`lastApplied`/`lastAppliedDelivery`.
- `applyMutation` handles each op: `append/upsert-item` (stale revision ignored; **same revision +
  different `itemSignature` → reset** protocol fault; newer revision replaces in place; new item
  inserts by ordinal); `append-block-delta` (unknown item / revision skew / unknown block all →
  conservative `repage` — L1.4; else appends to the target block and bumps `revision`); `status` (stale
  ignored; same-revision divergence → reset); `replace-page` (rehydrates a new baseline and clears the
  dedupe set + recovery/fault).
- Helpers: `rememberKey` COPY-ON-WRITES the dedupe structures (F17 — the freshly-spread projection
  still aliases the previous state's set until replaced) and bounds them to `APPLIED_KEY_LIMIT` (4096);
  `insertOrdered` is push-to-end O(1) with a binary path only for a rare out-of-order native-rehydrate
  row; `itemSignature` is the same-revision fault fingerprint, WIDENED (F17) to
  phase/kind/role/lane/source/provenance/blocks/correlation/updatedAt; `withRecovery` builds the
  `RecoverySignal` (`{mode: repage|reset, reason, afterCursor: eventCursor}`); `clearRecovery` /
  `orderedItems` are the store/renderer seams.

### Invariants And Boundaries

- **Never authors an item.** The only writers of a user item are projector `append/upsert/replace-page`
  events — no optimistic echo path exists (R2/§12.5, tested).
- **Recovery is deterministic and conservative.** Any cursor gap or missed intermediate delta RE-PAGES
  (never corrupts streamed text, never silently drops); a same-revision-different-payload divergence
  RESETS. A repage/reset re-hydrates native authority and resumes ONLY from the fresh page's cursor.
- **Idempotent.** `eventId+cursor` dedupe makes reconnect/replay safe; replay/hydration deliveries are
  applied and marked so announcers stay silent.
- **Identity by fields, never digest** (`sameIdentity`), because digests are domain-scoped across the
  L1/L2/L3 services.
- **Pure.** No side effects, no transport; the dedupe structures are copy-on-write so a caller can never
  mutate a prior state through them.

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
| The wire page and event-envelope types consumed by the reducer entry points. | `ConversationPage`; `ConversationEventEnvelope` | dashboard/src/data/conversation/types.ts:286-298; dashboard/src/data/conversation/types.ts:327-336 |
| The reducer's initial and older-page entry points apply typed page baselines. | `applyInitialPage`; `applyOlderPage` | dashboard/src/data/conversation/reducer.ts:168-202; dashboard/src/data/conversation/reducer.ts:205-229 |
| The reducer's live event entry point applies identity, cursor, dedupe, and gap rules. | `applyEvent` | dashboard/src/data/conversation/reducer.ts:246-286 |
| The store applies pages/events and consumes the reducer's `recovery` signal. | `activeConversationStore`; `handleRecovery` | dashboard/src/data/conversation/store.ts:84-191; dashboard/src/data/conversation/store.ts:427-435 |
| The active conversation reducer suite is the focused regression source for cursor, dedupe, gap, revision, identity, replacement, and replay behavior. | "active conversation reducer" | dashboard/src/data/conversation/reducer.test.ts:50-193 |
| The interrupt hook reads reducer status and ordered item ids for working-turn correlation. | `resolveWorkingTurnId` | dashboard/src/panels/session-cockpit/conversation/useConversationControls.ts:61-78 |
| The active serving API supplies page and event evidence consumed by the reducer. | `conversation_page`; `conversation_events`; `applyInitialPage`; `applyEvent` | dashboard/src/data/conversation/reducer.ts:168-202; dashboard/src/data/conversation/reducer.ts:246-286; mcp/src/agents_remember/serving/conversation/active/api.py:126-155; mcp/src/agents_remember/serving/conversation/active/api.py:204-247 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-04T13:00:51+02:00 — 260731-EFA-L6 S18-B11 curator: reconciled the frozen-source ledger, split pooled reducer references by source owner, and supplied exact anchors with scoped fixer input for generated ranges. Verification metadata unchanged.

- 2026-07-24T13:17:50Z — Removed the stale reducer-owned scroll-anchor description and recorded the
  protocol/UI boundary. Verification hash/date remain pinned to the pre-commit source stamp.

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the authority-sensitive
  pure reducer — cursor-ordered apply, bounded copy-on-write `eventId+cursor` dedupe (F17), block-delta
  revision gating and `previousCursor` gap tolerance (L1.4/L1.5) as conservative re-page,
  same-revision-divergence reset, anchor-preserving older prepend, replace-page rehydrate, and the
  no-optimistic-item rule. Verification is pinned to the leaf base (`0be0099`) because the new source
  file is uncommitted; closeout owns its first source stamp.
