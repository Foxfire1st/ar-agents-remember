# dashboard/src/data/conversation/reducer.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/conversation/reducer.ts`     |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-20T22:30+02:00                           |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd`       |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
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
  true announcer/scroll target, not a DOM guess), `recovery?`/`fault?`, the view-owned `scrollAnchor`,
  and the bounded dedupe pair `appliedKeys`/`appliedKeySet`.
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The wire types the reducer reduces. | L17-L28 | [types.ts](types.ts) |
| The store that drives page/event application and consumes `recovery`. | L63-L104 | [store.ts](store.ts) |
| The 14-test suite pinning no-dup-item, cursor order/idempotence, gap→repage, L1.5, revision→reset. | — | [reducer.test.ts](reducer.test.ts) |
| The interrupt hook that reads `orderedItemIds`/`status` for turn-id correlation. | L61-L78 | [../../panels/session-cockpit/conversation/useConversationControls.ts](../../panels/session-cockpit/conversation/useConversationControls.ts) |
| The server active-serving routes whose events this reduces. | — | [active/api.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/api.py) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the authority-sensitive
  pure reducer — cursor-ordered apply, bounded copy-on-write `eventId+cursor` dedupe (F17), block-delta
  revision gating and `previousCursor` gap tolerance (L1.4/L1.5) as conservative re-page,
  same-revision-divergence reset, anchor-preserving older prepend, replace-page rehydrate, and the
  no-optimistic-item rule. Verification is pinned to the leaf base (`0be0099`) because the new source
  file is uncommitted; closeout owns its first source stamp.
