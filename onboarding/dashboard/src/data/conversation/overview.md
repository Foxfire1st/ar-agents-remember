# dashboard/src/data/conversation/ — Reconstructable Active-Conversation Projection Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/src/data/conversation/`               |

## Governing Overview

[data overview](../overview.md) — this child owns the browser-side ACTIVE conversation projection
while the data overview owns the surrounding cockpit state and authority boundaries. Its sibling
[data/conversation-library overview](../conversation-library/overview.md) owns the separate DORMANT
library projection (the two stores are deliberately disjoint — R1).

## Purpose

`data/conversation/` is the **reconstructable browser projection of one live structured conversation**
(design §6, §9, §11). It rebuilds the active transcript PURELY from the landed
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
  `arSessionId`+`bridgeEpoch` FIELDS, never by digest — precision note 4), `ConversationItem`,
  the `ConversationContentBlock` union, `ConversationStatus` (the canonical turn/process/freshness
  state whose `turn.turnId` is null on the hosted-codex wire), `ConversationCapabilities`
  (whose `controls.interrupt` is the KNOWN-STALE L1 view), the page + event envelope + mutation ops,
  telemetry (`MetricEvidence` — absent metrics omitted, never zero), `InterruptOperation`, and
  `ConversationRouteError`, plus the additive harness sub-agent identity
  (`ConversationAgentStatus`/`ConversationAgentRef`, optional `ConversationItem.agent` — absent =
  the parent conversation; identity fields evidence-bound, never fabricated).
- `agents.ts` — the sub-agent roster derivation + timeline focus model (R7), pure
  functions over projection evidence ONLY. The roster itself stays server-derived: the backend
  projectors mint ONE roster item per sub-agent on the parent timeline (codex
  `codex-agent-<threadId>`, claude `claude-agent-<taskId>`; notice/system, `agent` set) and this
  module only READS it — `isAgentRosterItem` (the ruled shape), `agentLabel` (evidence-bound
  precedence, `agent <short-id>` last resort), terminal-only final-message previews, `deriveAgents`
  (first-evidence order, upsert-replaces), `cycleAgentFocus`/`effectiveAgentFocus` (stale id →
  parent), and `filterItemsForFocus` (parent keeps roster rows; an agent lane keeps its own items,
  roster row included). No optimistic rows, no polling.
- `reducer.ts` — the authority-sensitive PURE reducer: cursor-ordered apply, `eventId`+`cursor` dedupe
  (bounded 4096, copy-on-write), block-delta revision gating, `previousCursor` gap tolerance,
  gap→re-page, same-revision-divergence→reset (§6.4), older-page anchor-preserving prepend, replace-page
  rehydrate. It NEVER authors an item — the only paths that add a user item are projector events, so
  there is no optimistic user echo (R2/§12.5/R7).
- `client.ts` — the active-page/telemetry reads, selected-child history POST, and interrupt
  request/status/reconcile over the landed routes. Typed outcomes are discriminated by payload
  shape and never guessed into success; selected-child non-2xx/invalid/network/timeout errors stay
  child-local, while a failed page read threads the server's typed `ConversationRouteError` to the
  parent banner (F15).
- `stream.ts` — the resumable SSE controller. It manually re-opens a FRESH `EventSource` from the
  latest cursor (`after=` query only) precisely to avoid the landed `cursor-conflict` preflight that
  fires when a native `Last-Event-ID` header disagrees with `after=`.
- `store.ts` — the `activeConversationStore` (vanilla zustand) + connect/recovery/older-page/LRU
  orchestration. Per-session runtime lives outside the store to avoid re-render churn and is never
  conversation authority. A bounded LRU (6) may evict an unfocused session's projection; it simply
  rehydrates on refocus. The store also carries `agentFocusBySession` + `setAgentFocus` — the
  operator's timeline focus, keyed OUTSIDE `bySession` so an LRU eviction keeps the operator's
  place; the surface revalidates the stored id via `agents.effectiveAgentFocus` rather than
  re-applying it blindly. It also owns selected-child history orchestration: same-child
  singleflight, visible loading/ready/failed state, successful-id LRU, retry, and explicit 64-entry
  in-flight/retained bounds that never call the parent `failStream`.
- `format.ts` — the shared presentation conventions (A1/A4/A5/A8): em-dash = genuinely absent,
  interpunct = separator, `joinChips` drops empties (no dash-chains), humanized durations, quiet
  long-stale tone, boundary truncation with a full-value affordance. Its reach was widened
  beyond the conversation surfaces: `humanizeDuration` is now the SINGLE duration authority for the
  whole cockpit chrome (supervisor badge, rail-footer heartbeat/cutoff, uptime — `StatusLine` also imports
  `joinChips` for its collapse-or-explain segments), and a NEW `shortId(id, tail)` collapses a long
  ULID/UUID to `…SUFFIX` (R6) with the full value the caller's `title` (rail task badges, focus-handoff
  banner).
- `thinkingPreference.ts` — the global persisted hide-thinking preference (`cockpit.chats.hide-thinking.v1`,
  the only durable UI bit — non-destructive, instant).

## 2026-07-24 Warm Projection And Liveness Refinement

Focus changes keep up to `LRU_LIMIT=6` active projections warm; only LRU eviction and session termination
disconnect their runtime. The UI's scroll geometry is deliberately outside the reducer/store protocol
state: per-session view memory restores only after stable rendering and cannot alter replay authority.
HTTP page, telemetry, and interrupt calls are abort-bounded. The stream retries faster before first open,
uses a visible-tab one-shot watchdog for sleep or half-open channels, and turns a replacement instance
that never opens into an honest failure rather than perpetual connecting.

## 2026-07-26 Sub-Agent Roster And Timeline Focus

Harness sub-agents now appear on the parent timeline as ONE backend-minted roster item each (codex
`codex-agent-<threadId>`, claude `claude-agent-<taskId>`; kind `notice`, role `system`, `agent`
set — every upsert bound to concrete collab/join evidence, never optimistic). The projection itself
stays server-derived: the NEW `agents.ts` only READS that roster to derive the agents-area rows
(`deriveAgents`), the evidence-bound labels (`agentLabel`, `agent <short-id>` last resort), and the
parent↔agent timeline focus model (`cycleAgentFocus`/`effectiveAgentFocus`/`filterItemsForFocus`).
The store's `agentFocusBySession` holds the raw focus id OUTSIDE the evictable `bySession`
projection, so an LRU eviction keeps the operator's place with the keep-warm runtime and a stale id
honestly recomputes to the parent on rehydrate.

## 2026-07-27 Selected-Child History Hydration

Roster discovery remains metadata/live-event first. Once `effectiveAgentFocus` validates one child,
the browser posts only that id for native backfill. A valid persisted focus hydrates on mount;
a stale stored id sends no request. Same-child callers singleflight, failures remain visible and
retryable per child, and the parent stream phase is unchanged. The 64-entry in-flight and retained
maps are necessary explicit bounds because the exported hydration function can be called by
multiple mounted consumers and abandoned requests/state must not grow without limit.

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
  services, so `sameIdentity` compares `arSessionId`+`bridgeEpoch` (precision note 4).
- **Manual SSE resume only.** Native EventSource auto-reconnect is deliberately not used (the
  `after=`-vs-`Last-Event-ID` cursor-conflict trap); a reconnect is a fresh instance with no lastEventId.
- **Transport is not interpretation.** `stream.ts` delivers ordered envelopes and reports
  connect/disconnect; all projection interpretation lives in the reducer.
- **The agent roster is server-derived; the focus is browser-only.** Roster rows are minted by
  the backend projectors from bound evidence — the browser never authors, polls, or fabricates one
  (an unresolved identity is `agent <short-id>`). Conversely the operator's focus
  (`agentFocusBySession`) is pure UI state that survives LRU eviction OUTSIDE the projection and is
  always revalidated against the live roster (`effectiveAgentFocus`), never re-applied blindly.
- **Child history failure is not parent stream failure.** Hydration state is keyed by session and
  child; non-2xx, invalid payload, network, timeout, server unavailability, and local capacity are
  shown on that child and can be retried without `failStream`.

## Follow-On Register (durable rulings a future conversation surface must carry)

- **Retention-gap re-page tolerance is the contract, not defensive gold-plating.** A
  healthy consumer whose live `previousCursor` names a retained gap must conservatively re-page; a
  missed intermediate block delta must re-page rather than guess; `replace-page`/native-rehydrate
  bypass the gap check because they establish a new baseline. These are tested and load-bearing — do
  not "optimize" them into a silent apply.
- **Interrupt capability gating is attempt-and-reflect — the honest wire maximum.** No
  route in the landed seventeen exposes a proactive `ControlCapabilities` read; the active page's
  `capabilities.controls` is the register's named STALE L1 view (`unverified` for all three harnesses).
  So the renderer gates on a working+resolvable turn and reflects the server's typed refusal reactively,
  and it must gate on the L3 routes' own evidence — never enable/disable purely from the stale L1 view.
  A clean proactive gate awaits a control-capabilities GET or an L1-view refresh; hiding a landed
  feature on the stale view is the failure to avoid.
- **Hosted-codex `ConversationStatus.turn` carries no `turnId` during working turns.** The
  turn id must be correlated from projector item evidence (`resolveWorkingTurnId`) until a substrate
  fix populates status; a status fix that carries `turn.turnId` on this topology invalidates the
  correlation path.
- **The E1/E2 backend faults block a full production E2E pass.** E1 (hosted-interactions vendor-correlation
  500) and E2 (L1 unknown-input provenance validator 500) reproduce under ordinary hosted-codex
  chatting; the surface handled both fail-loud (no silent PTY
  fallback), but a production E2E cannot pass over this substrate until they are dispositioned.
- **Virtualization at 10k items is architecturally bounded but unmeasured here.** The
  reducer/store scale is O(1) amortized on in-order append; the measured DOM/interaction baseline is
  a future hardening artifact (the unit env has no layout).

## Hot Path Summary

1. `store.connectConversation` reads the bridge epoch, calls `client.fetchConversationPage` for the
   native-hydrated page, and `reducer.applyInitialPage` establishes the baseline + resume cursor.
2. `stream.openConversationStream` opens the resumable SSE from that cursor; each envelope flows through
   `reducer.applyEvent` (cursor-ordered, deduped, revision-gated).
3. A reducer `recovery` signal (`gap`/`reset`) stops the stream, re-pages native authority, and resumes
   from the fresh cursor; a typed page failure sets `errorBySession` and marks `projection-failed`.
   The INITIAL hydrate (`hydrateAndStream`) no longer fails loud on the first
   page fetch: a TRANSIENT boot failure (`httpStatus === 0` or `>= 500`) retries quietly on the
   `connecting` phase across a bounded window (8 × 400ms) before escalating to `projection-failed`,
   while a hard 4xx (409 epoch-rolled, 404) still fails loud immediately — closing the codex launch
   "cried-wolf" red strip (audit V13) without ever masking a real failure. The epoch-resolve/repage
   path in `ChatsStageBody` is NOT hardened by this fix (pre-existing, recorded follow-on).
4. The renderer reads `orderedItems`/`status`/`capabilities`/`stream` through `useActiveConversation`;
   the interrupt hook reads the same projection for turn id + capability evidence.
5. A validated effective child focus calls `hydrateAgentConversation`; the store singleflights the
   POST, applies the local outcome, and leaves page/SSE ownership untouched.

## Child Route Onboarding Map

No deeper child route exists below `data/conversation/`; each source has a one-to-one file card and
this overview is their governing pillar.

## File Onboarding Map

| Responsibility | File onboarding |
| --- | --- |
| Wire grammar mirror | [types.ts](types.ts.md) |
| Sub-agent roster derivation + timeline focus model | [agents.ts](agents.ts.md) · [agents.test.ts](agents.test.ts.md) |
| Pure authority-sensitive reducer | [reducer.ts](reducer.ts.md) · [reducer.test.ts](reducer.test.ts.md) |
| Page/telemetry/selected-child-history/interrupt HTTP client | [client.ts](client.ts.md) |
| Resumable SSE transport | [stream.ts](stream.ts.md) |
| Stream boot and liveness regression coverage | [stream.test.ts](stream.test.ts.md) |
| Reconstructable store + parent and selected-child orchestration | [store.ts](store.ts.md) · [store.test.ts](store.test.ts.md) |
| Presentation conventions | [format.ts](format.ts.md) · [format.test.ts](format.test.ts.md) |
| Hide-thinking preference | [thinkingPreference.ts](thinkingPreference.ts.md) |

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This route's statements were verified from its direct agents-remember source/tests and the
reviewed worker report and final-PASS review verdict.

No configured Domain Documentation source exists for this route.

### Cross-Repo References

The route mirrors this repository's own landed conversation wire contract and talks only to this
package's serving endpoints; no cross-repository implementation source governs it.

No applicable cross-repository source was found.

### Repo-Internal References

- The active serving API exposes page, selected-child history, and event routes. [1]
- The dashboard client fetches the active page. [2]
- The dashboard client requests selected-child history. [3]
- The dashboard stream opens the active events URL built by `conversationEventsUrl`. [4]
- The wire grammar this route mirrors (moved to `models/conversations/` by 260731-EFA-L9). [5]
- The codex backend mints one evidence-bound roster item per sub-agent. [6]
- The Claude backend maps task lifecycle evidence into the roster. [7]
- The control API exposes interrupt, status, and reconcile routes. [8]
- The dashboard client posts interrupt requests through one shared body. [9]
- The dashboard client exposes the exact-turn interrupt wrapper. [10]
- The dashboard client exposes status and reconcile wrappers. [11]
- The active conversation surface owns projection/focus behavior and renders the reconnect, agent, and timeline body. [12]
- The chats stage body mounts the active conversation surface. [13]
