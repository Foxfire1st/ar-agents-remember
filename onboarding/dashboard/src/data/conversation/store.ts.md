# dashboard/src/data/conversation/store.ts

## Governing Overview

[data/conversation overview](overview.md)

## Purpose

The **reconstructable active-conversation store** (design §11.1, §11.3, R1). It holds ONLY a browser
projection rebuilt from public server/native authority — no IndexedDB/localStorage/SQLite, no
optimistic durable item authority. It uses the house zustand idiom (a vanilla `createStore` + a thin
`useActiveConversation(selector)` hook, matching `store.ts`/`sessionCockpitStore.ts`). It orchestrates
the page↔stream contract: connect hydrates a native page then opens the resumable stream; a
reducer-signalled `gap`/`reset` recovery stops the stream, re-pages native authority, and resumes ONLY
from the fresh page's atomically-captured `eventCursor` (§6.8). A bounded LRU may evict an unfocused
session's projection; it is simply rehydrated on refocus — history authority is always native.

## Code Commentary

### Logic

- `activeConversationStore` state: `bySession` (id → `ActiveConversationProjection`), `errorBySession`
  (the server's typed `ConversationRouteError` per session, threaded to the banner — F15/§14.5),
  `agentFocusBySession` (the operator's timeline focus per session; absent = the
  parent conversation, an agentId = that sub-agent's lane), and `touchOrder` (LRU order). Actions:
  `applyPage` (initial/older, clears any prior error on a successful hydrate), `ingestEvent` (drops
  events for an un-hydrated session, applies through the reducer, no-op-skips when unchanged),
  `setStreamPhase`, `setAgentFocus` (null clears the focus back to the parent), `failStream`
  (records the typed reason and marks the projection `projection-failed`; when no projection exists
  yet the error alone lets the surface render the reason on a first-connect failure), `evict`,
  `reset` (clears the focus map with the rest). `agentFocusBySession` is deliberately keyed OUTSIDE
  `bySession`: an LRU eviction drops the projection but keeps the operator's place with the
  keep-warm runtime, and the surface revalidates the stored id against the rehydrated roster via
  `effectiveAgentFocus` instead of re-applying it blindly. Scroll restoration is no longer reducer
  state: the UI owns its short-lived per-session geometry memory so protocol reduction stays DOM-free.
- Orchestration (outside the store, `runtimeBySession` Map, to avoid re-render churn — the
  identity-preserving pattern; never conversation authority): `connectConversation` disposes any prior
  runtime, bumps a `generation`, enforces the LRU, then `hydrateAndStream` fetches the page (guarded by
  `disposed`/generation), applies it initial, and `startStream` opens the SSE with `getResumeCursor`
  reading the store's `eventCursor`; `onEnvelope` ingests then, if the reducer set `recovery`, triggers
- **Initial-hydrate boot-race retry (R10, audit V13):** `hydrateAndStream` is now a
  bounded retry loop over the first page fetch (`INITIAL_CONNECT_ATTEMPTS=8`,
  `INITIAL_CONNECT_RETRY_MS=400`). A fresh chat's first fetch races the runner/bridge boot (the seat row
  appears before the bridge is listening; the diagnosis saw a 503 during codex boot), and the stream
  auto-retry covers only a DROPPED live stream, not this first-connect race — so a healthy launch used to
  flash the fail-loud `projection-failed` strip until a manual retry. Now, while the fetch fails
  TRANSIENTLY (`isTransientBootFailure`: `error === null` transport drop, `httpStatus === 0`, or
  `httpStatus >= 500`), the loop stays on the quiet `connecting` phase and waits `INITIAL_CONNECT_RETRY_MS`
  between tries, escalating to `failStream` only when the window exhausts. A hard 4xx — 409 epoch/cursor,
  404 unknown session — is a real terminal answer and `failStream`s IMMEDIATELY (never masked). The strip
  is deferred, never hidden.
  `handleRecovery` (stop the stream, re-page native authority, `applyPage` initial which clears
  recovery/fault and re-establishes the resume cursor, then resume). `disconnectConversation` disposes
  and stops but KEEPS the projection (keep-alive). `loadOlderConversation` prepends one older page.
  `enforceLru` keeps exactly `LRU_LIMIT=6` warm conversations and evicts the least-recently used
  runtime; focus switches only touch the order, while eviction and termination are the disconnectors.

### 2026-07-24 Curator Delta

The store now treats a rejected resume cursor and a never-opening stream as recoverable transport
failures: it re-pages for a fresh server cursor, limits repeated dead-stream recovery, and eventually
surfaces the typed failure instead of leaving a fabricated connecting state. It also preserves warm
projections across focus changes, disconnecting only on LRU eviction or termination, and tests the
exact six-chat bound. Scroll state moved out of the protocol reducer into the timeline's per-session
view memory; no `setScrollAnchor` action remains here.

### Invariants And Boundaries

- **Agent focus survives eviction, never trusted blindly.** `agentFocusBySession`
  lives outside the evictable `bySession` projection so the operator's place rides the keep-warm
  runtime; a stale id (agent gone after rehydrate) is recomputed to the parent by
  `effectiveAgentFocus`, not re-applied.

- **No durable browser authority (R1).** The store holds only the server-derived projection; reload,
  re-page, eviction, and recovery all rebuild from native authority.
- **Keep-alive + rehydrate.** `disconnectConversation` keeps the projection; an evicted session
  rehydrates on refocus. The LRU is a memory bound on DOM/projection, not a history bound.
- **Recovery re-pages, never patches blindly.** A reducer `recovery` signal stops the stream, re-hydrates
  native authority, and resumes from the fresh cursor (§6.8).
- **Runtime is not authority.** The per-session runtime (epoch/base/fetch/controller/generation/disposed)
  lives outside the store; generation + `disposed` guards discard results owned by a superseded connect.
- **First-connect failure renders honestly.** `failStream` with no projection still records the typed
  reason so the surface shows it (never a silent blank).
- **Transient-only retry never masks a real failure.** Only a `null`/transport-drop, `httpStatus === 0`,
  or `>= 500` first-connect result is treated as the boot race and retried quietly; every 4xx fails loud
  immediately, and the retry window is bounded so a genuinely broken session still escalates to the honest
  strip. This hardens ONLY the initial hydrate — the epoch-resolve/repage path in `ChatsStageBody` is a
  separate, pre-existing cried-wolf class (routed as a product follow-on).

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The pure reducer whose page/event/recovery this store drives. [1]
- The page/telemetry/interrupt client this store fetches through. [2]
- The SSE controller this store opens/reconnects/stops. [3]
- The store-level keep-alive + LRU-eviction suite (F4), plus the initial-connect retry pins: a transient 503 retries quietly and never flashes the alarm; a hard 409 fails loud immediately. [4]
- The roster derivation + focus recompute this focus state defers to (`effectiveAgentFocus`). [5]
- The focus LRU-survival + reset pins for `agentFocusBySession`. [6]
- The stage body that connects/disconnects on focus + epoch resolution. [7]
- The house vanilla-zustand store idiom this matches. [8]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## 260727-CHATS-IM-L2 Selected-Child Store Delta

`agentHistoryBySession` is child-scoped UI acquisition state and never changes the parent's stream
phase cit:(["agentHistoryBySession: Record<string", `hydrateAgentConversation`], dashboard/src/data/conversation/store.ts:64-64; dashboard/src/data/conversation/store.ts:143-143; dashboard/src/data/conversation/store.ts:795-795).
singleflights duplicate callers, retains successful child ids in LRU order, and publishes
loading/ready/failed states without calling `failStream` cit:([`hydrateAgentConversation`], dashboard/src/data/conversation/store.ts:795-834). Both in-flight and retained
child bookkeeping are capped at 64. This explicit bound is necessary because multiple mounted
consumers can call the exported function and abandoned requests/success rows otherwise form
unbounded browser state; capacity refusal is a visible `local-resource-limit`, not silent defense.

Disconnect/reconnect clears child acquisition state with its runtime, while the existing raw focus
survives and is revalidated against the next roster. A failed child is retryable; a successful
child is not re-posted within the same runtime.
