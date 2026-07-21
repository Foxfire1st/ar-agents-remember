# dashboard/src/data/conversation/ — Reconstructable Active-Conversation Projection Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/data/conversation/`               |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-07-21T11:30+02:00                           |
| lastVerifiedCommitHash | `38c3fd81bdf851dce96e9b2b14e2bff741e7b383`       |
| lastVerifiedCommitDate | 2026-07-21T11:31:07+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[data overview](../overview.md) — this child owns the browser-side ACTIVE conversation projection
while the data overview owns the surrounding cockpit state and authority boundaries. Its sibling
[data/conversation-library overview](../conversation-library/overview.md) owns the separate DORMANT
library projection (the two stores are deliberately disjoint — R1).

## Purpose

`data/conversation/` is the **reconstructable browser projection of one live structured conversation**
(260718-CHATS-L4, design §6, §9, §11). It rebuilds the active transcript PURELY from the landed
server/native authority — the native-hydrated page, the resumable SSE event stream, and the control
routes — and holds it as an in-memory zustand projection only. There is **no durable browser
authority**: no IndexedDB/localStorage/SQLite conversation index and no optimistic durable item. A
reload, a page turn, an LRU eviction, or a recovery all reconstruct from the server; the only persisted
bit in the whole subsystem is the boolean hide-thinking preference. The reducer is a pure,
side-effect-free core the store, the stream, and the tests all share, so the authority-sensitive rules
(cursor order, dedupe, gap tolerance, revision-fault reset) have exactly one implementation.

## Route Model

- `types.ts` — the browser mirror of the landed SC1 normalized wire grammar (`serving/conversation/
  models.py`), exact camelCase from the server's `to_camel` WireModel. CONSUMED types only — nothing
  here validates a schema; the server is the sole authority and the reducer defends only against
  faults it can actually observe. Carries `ActiveConversationRef` (identity matched by
  `arSessionId`+`bridgeEpoch` FIELDS, never by digest — L4-facing note 4), `ConversationItem`,
  the `ConversationContentBlock` union, `ConversationStatus` (the canonical turn/process/freshness
  state whose `turn.turnId` is null on the hosted-codex wire — L4.R1), `ConversationCapabilities`
  (whose `controls.interrupt` is the KNOWN-STALE L1 view), the page + event envelope + mutation ops,
  telemetry (`MetricEvidence` — absent metrics omitted, never zero), `InterruptOperation`, and
  `ConversationRouteError`.
- `reducer.ts` — the authority-sensitive PURE reducer: cursor-ordered apply, `eventId`+`cursor` dedupe
  (bounded 4096, copy-on-write), block-delta revision gating, `previousCursor` gap tolerance (L1.5),
  gap→re-page, same-revision-divergence→reset (§6.4), older-page anchor-preserving prepend, replace-page
  rehydrate. It NEVER authors an item — the only paths that add a user item are projector events, so
  there is no optimistic user echo (R2/§12.5/R7).
- `client.ts` — the active-page/telemetry reads + interrupt request/status/reconcile over the landed
  routes. Typed control evidence: a refusal is discriminated by the payload shape and NEVER guessed
  into a success; a failed page read threads the server's typed `ConversationRouteError` to the banner
  (F15), never a generic message.
- `stream.ts` — the resumable SSE controller. It manually re-opens a FRESH `EventSource` from the
  latest cursor (`after=` query only) precisely to avoid the landed `cursor-conflict` preflight that
  fires when a native `Last-Event-ID` header disagrees with `after=` (L4.3).
- `store.ts` — the `activeConversationStore` (vanilla zustand) + connect/recovery/older-page/LRU
  orchestration. Per-session runtime lives outside the store to avoid re-render churn and is never
  conversation authority. A bounded LRU (6) may evict an unfocused session's projection; it simply
  rehydrates on refocus.
- `format.ts` — the shared presentation conventions (A1/A4/A5/A8): em-dash = genuinely absent,
  interpunct = separator, `joinChips` drops empties (no dash-chains), humanized durations, quiet
  long-stale tone, boundary truncation with a full-value affordance. **260718-CHATS-L5P** widened its
  reach beyond the conversation surfaces: `humanizeDuration` is now the SINGLE duration authority for the
  whole cockpit chrome (supervisor badge, rail-footer heartbeat/cutoff, uptime — `StatusLine` also imports
  `joinChips` for its collapse-or-explain segments), and a NEW `shortId(id, tail)` collapses a long
  ULID/UUID to `…SUFFIX` (R6) with the full value the caller's `title` (rail task badges, focus-handoff
  banner).
- `thinkingPreference.ts` — the global persisted hide-thinking preference (`cockpit.chats.hide-thinking.v1`,
  the only durable UI bit — non-destructive, instant).

## Invariants And Boundaries

- **Reconstructable, never durable (R1).** This route holds only a server-derived projection. Reload,
  re-page, LRU eviction, and recovery all rebuild from native authority; grep the route for
  IndexedDB/localStorage/SQLite and you find only the hide-thinking boolean.
- **The reducer never authors an item.** No optimistic user echo exists — the only writers of a user
  item are the projector's `append/upsert/replace-page` mutations (proven by `reducer.test.ts`).
- **Recovery is deterministic, not a guess.** A cursor gap, a missed intermediate delta, or a
  `previousCursor` naming an unreceived retained cursor all conservatively RE-PAGE (never corrupt or
  silently drop); a same-revision-different-payload divergence RESETS. A re-page/reset always re-hydrates
  native authority and resumes ONLY from the fresh page's atomically-captured `eventCursor` (§6.8).
- **Identity is field-matched, never digest-matched.** Digests are domain-scoped across the L1/L2/L3
  services, so `sameIdentity` compares `arSessionId`+`bridgeEpoch` (L4-facing precision note 4).
- **Manual SSE resume only.** Native EventSource auto-reconnect is deliberately not used (the
  `after=`-vs-`Last-Event-ID` cursor-conflict trap); a reconnect is a fresh instance with no lastEventId.
- **Transport is not interpretation.** `stream.ts` delivers ordered envelopes and reports
  connect/disconnect; all projection interpretation lives in the reducer.

## L5-Facing Register (durable rulings the next conversation leaf must carry)

- **Retention-gap re-page tolerance (L1.4/L1.5) is the contract, not defensive gold-plating.** A
  healthy consumer whose live `previousCursor` names a retained gap must conservatively re-page; a
  missed intermediate block delta must re-page rather than guess; `replace-page`/native-rehydrate
  bypass the gap check because they establish a new baseline. These are tested and load-bearing — do
  not "optimize" them into a silent apply.
- **Interrupt capability gating is attempt-and-reflect — the honest wire maximum (L4.1/L4.R3).** No
  route in the landed seventeen exposes a proactive `ControlCapabilities` read; the active page's
  `capabilities.controls` is the register's named STALE L1 view (`unverified` for all three harnesses).
  So the renderer gates on a working+resolvable turn and reflects the server's typed refusal reactively,
  and it must gate on the L3 routes' own evidence — never enable/disable purely from the stale L1 view.
  A clean proactive gate awaits a control-capabilities GET or an L1-view refresh; hiding a landed
  feature on the stale view is the failure to avoid.
- **Hosted-codex `ConversationStatus.turn` carries no `turnId` during working turns (L4.R1).** The
  turn id must be correlated from projector item evidence (`resolveWorkingTurnId`) until a substrate
  leaf populates status; a status fix that carries `turn.turnId` on this topology invalidates the
  correlation path.
- **The E1/E2 backend faults gate L5/half-time (L4.R2).** E1 (hosted-interactions vendor-correlation
  500) and E2 (L1 unknown-input provenance validator 500) reproduce under ordinary hosted-codex
  chatting; this leaf touched no backend and the L4 surface handled both fail-loud (no silent PTY
  fallback), but L5's production E2E cannot pass over this substrate until they are dispositioned.
- **Virtualization at 10k items is architecturally bounded but unmeasured here (L4.4).** The
  reducer/store scale is O(1) amortized on in-order append; the measured DOM/interaction baseline is
  an L5 hardening artifact (the unit env has no layout).

## Hot Path Summary

1. `store.connectConversation` reads the bridge epoch, calls `client.fetchConversationPage` for the
   native-hydrated page, and `reducer.applyInitialPage` establishes the baseline + resume cursor.
2. `stream.openConversationStream` opens the resumable SSE from that cursor; each envelope flows through
   `reducer.applyEvent` (cursor-ordered, deduped, revision-gated).
3. A reducer `recovery` signal (`gap`/`reset`) stops the stream, re-pages native authority, and resumes
   from the fresh cursor; a typed page failure sets `errorBySession` and marks `projection-failed`.
   Since 260718-CHATS-L5F R10 the INITIAL hydrate (`hydrateAndStream`) no longer fails loud on the first
   page fetch: a TRANSIENT boot failure (`httpStatus === 0` or `>= 500`) retries quietly on the
   `connecting` phase across a bounded window (8 × 400ms) before escalating to `projection-failed`,
   while a hard 4xx (409 epoch-rolled, 404) still fails loud immediately — closing the codex launch
   "cried-wolf" red strip (audit V13) without ever masking a real failure. The epoch-resolve/repage
   path in `ChatsStageBody` is NOT hardened by this leaf (pre-existing, recorded follow-on).
4. The renderer reads `orderedItems`/`status`/`capabilities`/`stream` through `useActiveConversation`;
   the interrupt hook reads the same projection for turn id + capability evidence.

## Child Route Onboarding Map

No deeper child route exists below `data/conversation/`; each source has a one-to-one file card and
this overview is their governing pillar.

## File Onboarding Map

| Responsibility | File onboarding |
| --- | --- |
| Wire grammar mirror | [types.ts](types.ts.md) |
| Pure authority-sensitive reducer | [reducer.ts](reducer.ts.md) · [reducer.test.ts](reducer.test.ts.md) |
| Page/telemetry/interrupt HTTP client | [client.ts](client.ts.md) |
| Resumable SSE transport | [stream.ts](stream.ts.md) |
| Reconstructable store + orchestration | [store.ts](store.ts.md) · [store.test.ts](store.test.ts.md) |
| Presentation conventions | [format.ts](format.ts.md) · [format.test.ts](format.test.ts.md) |
| Hide-thinking preference | [thinkingPreference.ts](thinkingPreference.ts.md) |

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This route's statements were verified from its direct agents-remember source/tests and the
reviewed 260718-CHATS-L4 worker report and final-PASS review verdict.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this route. | `system/sources.md` checked | — |

## Cross-Repo References

The route mirrors this repository's own landed conversation wire contract and talks only to this
package's serving endpoints; no cross-repository implementation source governs it.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The landed active serving routes this client/stream consume. | [active/api.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/api.py) |
| The wire grammar this route mirrors. | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| The control routes + L4-facing rulings the interrupt client consumes. | [conversation/control overview](../../../../mcp/src/agents_remember/serving/conversation/control/overview.md) |
| The renderer that projects this store. | [session-cockpit/conversation overview](../../panels/session-cockpit/conversation/overview.md) |
| The parent data authority boundary. | [data overview](../overview.md) |

## Update History

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: recorded the R10 initial-hydrate cried-wolf fix
  in the Hot Path Summary — `hydrateAndStream` now retries transient (network / 5xx) first-page
  failures quietly on the `connecting` phase across a bounded window before marking `projection-failed`,
  while a hard 4xx still fails loud immediately, so a healthy codex launch on a slow bridge no longer
  flashes the false "structured surface unavailable" red strip (audit V13). Noted the epoch-resolve
  repage path stays un-hardened (recorded follow-on). Governs `conversation/store.ts`; verification
  metadata stays pinned until closeout stamps the candidate commit.
- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: recorded the `format.ts` widening — `humanizeDuration`
  is now the single duration authority across the cockpit chrome and a new `shortId` (R6) was added; the
  reducer/store/stream authority contracts are unchanged (presentation-only). Verification pinned to this
  leaf's base (`352d5cd`) while the polish candidate is uncommitted; closeout owns candidate stamping.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the governing pillar for the
  reconstructable active-conversation projection — the pure authority-sensitive reducer, the
  no-durable-browser-store rule (R1), the retention-gap re-page tolerance (L1.4/L1.5), the manual
  SSE cursor-conflict avoidance (L4.3), the LRU-rehydrate contract, and the L5-facing register
  (capability gating, hosted-codex turn-id correlation, the E1/E2 faults, virtualization baseline).
  Verification is pinned to the leaf base (`0be0099`) because the new source route is uncommitted;
  closeout owns its first source stamp.
