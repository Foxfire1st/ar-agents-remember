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

`data/conversation/` provides the reconstructable browser projection of a live structured conversation. The transcript comes from server/native page and event authority; control routes return evidence about requested operations. The browser holds the active projection in memory, with no durable conversation index or optimistic durable item authority. Reload, eviction, and recovery reacquire server evidence; older paging adds server history without moving the live resume cursor. The boolean hide-thinking preference is persisted separately and does not delete transcript content.

The reducer centralizes identity, deduplication, predecessor continuity, and revision handling. Its standing intent is a pure, side-effect-free projection core. The implementation preserves prior projection structures through copying, but reset diagnostics read the current clock, so identical inputs do not guarantee an identical fault timestamp.

## Hot Path Summary

1. The stage resolves submission authority and supplies its bridge epoch to `connectConversation`. The store fetches a native-hydrated page; `applyInitialPage` establishes the projection and its resume cursor.
2. Only the focused conversation owns a physical SSE stream. `openConversationStream` creates a fresh EventSource using the latest cursor; decoded envelopes reach the store, which invokes `applyEvent`.
3. Gap/reset recovery stops the stream, fetches a fresh page, and resumes from that page's cursor. Initial hydration and recovery page reads share transient boot retry handling: a 30-second retry window with exponential delays starting at 250 ms and capped at 1000 ms. Initial hard failures surface immediately; recovery failures use the bounded recovery escalation. The retry window is checked after requests finish and is not an exact end-to-end deadline.
4. Warm refocus retains projection/runtime state and resumes from the retained cursor without another page fetch. LRU eviction forces subsequent reconstruction. The stage's cold epoch resolution also retries transient failures within its own 30-second window.
5. The surface reads the projection through `useActiveConversation`, derives roster/focus state, and requests history only for a validated effective child focus. Child acquisition singleflights independently of parent page/SSE ownership. The interrupt hook reads the same projection and prefers canonical turn identity before correlating item evidence when needed.

## Construction

### Wire, projection, and transport

- `types.ts` mirrors the repository's conversation wire models under `mcp/src/agents_remember/models/conversations/`. The server's WireModel supplies camelCase aliases; the browser interfaces are consumed types, not runtime schema validators. They include conversation identity, content blocks/items, status, capabilities, page/event mutations, telemetry evidence, interrupt operations, route errors, and optional sub-agent identity. An absent item agent denotes the parent conversation. Optional telemetry fields represent absence rather than fabricated zero values.
- `reducer.ts` materializes server pages and mutations. Identity matching uses `arSessionId` and `bridgeEpoch`, not digest equality. Deduplication combines `eventId` and cursor and retains at most 4096 keys through copy-on-write structures. Live predecessor discontinuity and missing delta prerequisites request re-page; same-revision divergent item/status payloads request reset. Older pages retain newer item revisions and the live resume cursor. Replacement pages establish a new baseline. The reducer consumes supplied items rather than inventing an optimistic user echo.
- `client.ts` owns active-page and telemetry GETs, selected-child history POSTs, and interrupt request/status/reconcile POSTs. Requests carry a 15-second abort timeout. Page HTTP errors retain typed route evidence; transport/JSON failures return an unsuccessful page result. Successful page/telemetry payloads are type casts, while child-history outcomes and interrupt/error responses receive limited payload-shape discrimination. This is not complete browser schema validation.
- `stream.ts` owns transport reopening and liveness, not projection mutation decisions. Each reopen creates a fresh EventSource with `after=` from the current resume cursor, avoiding native auto-reconnect's combination of an old query cursor and a newer Last-Event-ID header. It ignores JSON parse failures, forwards decoded envelopes, retries faster before the first successful open, and uses the shared liveness watchdog plus an open deadline to recover or escalate stalled instances.

### Retained sessions and selected-child history

`store.ts` owns the vanilla zustand projection and per-session acquisition runtimes. The runtime map is outside reactive projection state. An LRU limit of six bounds retained conversation seats, including cold hydrates reserved before their first page succeeds. Focus switching stops the previous physical stream and aborts its pending page request while preserving retained runtime/projection state. Refocus resumes a usable retained projection; eviction disconnects and removes it. Explicit reconnect, disconnect, and reset also dispose transport state, so disposal is not limited to eviction and session termination.

The operator's `agentFocusBySession` is outside evictable `bySession`, allowing focus to survive projection eviction. This focus is retained in memory, not persisted across browser reload. The surface recomputes `effectiveAgentFocus` against the current roster; an unknown stored id resolves to the parent. A visible surface hydrates an effective child focus on mount or focus/epoch change, and a stale id produces no child request.

Selected-child history has session/child-local loading, ready, and failed states. Same-child requests singleflight. Successful child ids use a 64-entry recency cache; in-flight requests and retained child states also have explicit 64-entry bounds. Non-2xx, invalid payload, network/timeout, unavailable/not-eligible outcomes, and local-capacity refusal remain visible child failures with retry rather than invoking parent `failStream`.

Scroll geometry is separate view memory, not replay authority. The store exposes per-session scroll recording/reading and clears that memory on disconnect/reset. The existing surface/timeline references retain the scroll-restoration contract; this review does not independently establish all layout timing guarantees.

### Agent and presentation derivation

`agents.ts` derives roster rows and timeline focus from projection evidence. Backend roster identities are `codex-agent-<threadId>` and `claude-agent-<taskId>`, with notice/system shape and an agent reference. The browser recognizes those rows rather than creating or polling for them. Labels prefer nickname, role, then the last agent-path segment, finally `agent <first-eight-id-characters>`. Derivation preserves first-evidence order and replaces an existing agent's view with later evidence. It acquires final-message/summary previews only from terminal rows, but may retain a previously acquired preview when a later row has no new preview. The parent lane includes parent items and roster rows; a child lane includes that child's items, including its roster row.

`format.ts` supplies absent-value and separator glyphs, empty-chip filtering, humanized durations/ages, quiet stale tones, boundary truncation, harness labels, and suffix-based `shortId`. Callers are responsible for exposing full truncated values. These helpers serve conversation and surrounding cockpit presentation; a claim that every cockpit duration has one exclusive formatter is not established by this bounded review.

`thinkingPreference.ts` uses the localStorage key `cockpit.chats.hide-thinking.v1` for the global hide-thinking boolean. A storage failure leaves the in-memory toggle usable. The preference changes rendering rather than normalized transcript authority.

### Onboarding map

No deeper child route is listed in the assigned route index. This overview governs the file cards below.

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

## Invariants And Boundaries

- **Reconstructable authority (R1).** Conversation content is server-derived. Browser projection, focus, child-acquisition bookkeeping, and scroll memory do not become durable transcript authority. The hide-thinking boolean is a separate UI preference.
- **No optimistic user echo (R2).** Pages and append/upsert/replace-page mutations supply the items; the reducer does not author a user item.
- **Conservative recovery.** An explicit gap, a discontinuous live predecessor, or missing/intermediate block-delta prerequisites must re-page rather than guess. Same-revision divergent item/status payloads reset. Replacement pages bypass predecessor checking because they establish a new baseline; native-rehydrate delivery is not treated as a contiguous live stream. Recovery resumes from fresh page evidence.
- **Field identity.** Events from another session/epoch do not merge into the projection. Opaque server cursors are resume tokens; their string representation is not a browser ordering authority.
- **Fresh transport resume.** Reconnection replaces EventSource rather than relying on its native reconnect behavior. Projection interpretation remains in reducer/store even though transport parses JSON and drops parse failures.
- **Evidence-derived roster, browser-only focus.** The browser derives agent rows from backend roster evidence and revalidates retained focus. Selected-child history failure remains local to that child.
- **Interrupt intent and observed implementation.** The standing attempt-and-reflect ruling requires usable turn evidence and honest typed refusal handling rather than treating an unverified capability as conclusive denial. The hook prefers canonical `status.turn.turnId`; when that is missing during a working turn it correlates the newest active item carrying a turn id, then the newest item carrying one. Historical claims that every hosted-codex working status lacks a turn id, or that all harness capability views remain stale, are not current promises. The present hook makes the control available only for a working, resolvable turn with neither a hard-unavailable capability nor a refusal for that same turn; a merely unverified capability is not that hard-unavailable predicate. The callback is withheld while pending. This does not establish backend capability freshness.
- **Performance must be measured.** The standing 10k-item virtualization concern remains. Append handling copies the item map and ordered-id array, so the former O(1)-amortized reducer/store claim is not supported by the implementation. No DOM/interaction measurement or test execution is asserted here.

## Historical Reports And Uncertainties

The former follow-on register reported E1 hosted-interactions vendor-correlation 500s and E2 unknown-input provenance-validation 500s during hosted-codex chatting, with fail-loud surface behavior and no silent PTY substitution. Their current reproduction and disposition were not established from the assigned source owners, so that report cannot establish a present production E2E blocker or a passed production E2E run. The source still contains consequential unknown-input provenance validation; its presence alone does not prove the reported failure still occurs.

The old statements about a stale L1 capability view and hosted-codex missing turn identity remain historical concerns requiring current backend evidence. The frontend still supports canonical identity followed by working-turn correlation. No lifecycle authority was supplied or examined for the reported faults, measurements, or prior review acceptance. Their current lifecycle status is explicitly unknown and lies outside this overview's operative promises.

## Evidence

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

- Reset diagnostics read the clock; the retry window is tested after each page request rather than being an exact deadline. [14]
- Roster rows can retain an earlier terminal preview; interrupt controls use working/identity/unavailable/refusal predicates and withhold pending callbacks. [15]
