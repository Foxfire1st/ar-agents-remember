# dashboard/src/data/conversation/store.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/conversation/store.ts`       |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-20T22:30+02:00                           |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd`       |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
| governingOverview      | `overview.md`                                    |

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
  (the server's typed `ConversationRouteError` per session, threaded to the banner — F15/§14.5), and
  `touchOrder` (LRU order). Actions: `applyPage` (initial/older, clears any prior error on a successful
  hydrate), `ingestEvent` (drops events for an un-hydrated session, applies through the reducer,
  no-op-skips when unchanged), `setStreamPhase`, `failStream` (records the typed reason and marks the
  projection `projection-failed`; when no projection exists yet the error alone lets the surface render
  the reason on a first-connect failure), `setScrollAnchor`, `evict`, `reset`.
- Orchestration (outside the store, `runtimeBySession` Map, to avoid re-render churn — the
  identity-preserving pattern; never conversation authority): `connectConversation` disposes any prior
  runtime, bumps a `generation`, enforces the LRU, then `hydrateAndStream` fetches the page (guarded by
  `disposed`/generation), applies it initial, and `startStream` opens the SSE with `getResumeCursor`
  reading the store's `eventCursor`; `onEnvelope` ingests then, if the reducer set `recovery`, triggers
  `handleRecovery` (stop the stream, re-page native authority, `applyPage` initial which clears
  recovery/fault and re-establishes the resume cursor, then resume). `disconnectConversation` disposes
  and stops but KEEPS the projection (keep-alive). `loadOlderConversation` prepends one older page.
  `enforceLru` keeps the focused session + the newest `LRU_LIMIT-1` (LRU_LIMIT=6) and evicts only
  sessions with NO live runtime (`!runtimeBySession.has(id)`).

### Invariants And Boundaries

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
| The pure reducer whose page/event/recovery this store drives. | L19-L26 | [reducer.ts](reducer.ts) |
| The page/telemetry/interrupt client this store fetches through. | L15-L18 | [client.ts](client.ts) |
| The SSE controller this store opens/reconnects/stops. | L27 | [stream.ts](stream.ts) |
| The store-level keep-alive + LRU-eviction suite (F4). | — | [store.test.ts](store.test.ts) |
| The stage body that connects/disconnects on focus + epoch resolution. | L71-L102 | [../../panels/session-cockpit/ChatsStageBody.tsx](../../panels/session-cockpit/ChatsStageBody.tsx) |
| The house vanilla-zustand store idiom this matches. | — | [../store.ts](../store.ts) · [../sessionCockpitStore.ts](../sessionCockpitStore.ts) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the reconstructable
  active-conversation store — the no-durable-index projection (R1), the connect/recovery/older-page
  orchestration that resumes only from a fresh cursor (§6.8), the keep-alive-on-disconnect + bounded
  LRU-rehydrate (F4), and the typed first-connect failure surfacing (F15). Verification is pinned to the
  leaf base (`0be0099`) because the new source file is uncommitted; closeout owns its first source stamp.
