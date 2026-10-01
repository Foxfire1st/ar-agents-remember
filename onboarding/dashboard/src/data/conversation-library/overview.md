# dashboard/src/data/conversation-library/ — Dormant Conversation Library Projection Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/src/data/conversation-library/`       |

## Governing Overview

[data overview](../overview.md) — this child owns the browser-side DORMANT conversation-library
projection while the data overview owns the surrounding cockpit state. Its sibling
[data/conversation overview](../conversation/overview.md) owns the separate ACTIVE-conversation store.
The two are deliberately DISJOINT stores (R1/design §11): the library never marks a session active and
the active store never lists dormant history.

## Purpose

`data/conversation-library/` is the **reconstructable browser projection of the native
previous-conversation library** (design §4.4, §9.4, §11.2). It holds paged list-query
state, read-only preview pages, the selected preview identity, and the caller-stable open-operation
phase/revision — all rebuilt from the landed library routes. It has **no durable browser index**:
reload reconstructs from server authority. Its single most load-bearing rule is the **exact-open focus
gate**: opening a dormant conversation focuses a NEW live rail row ONLY on catalog-proven
`phase="opened" && outcome="opened"`; every other outcome leaves the current chat/draft/focus/scroll
intact (R4).

## Route Model

- `types.ts` — the browser mirror of the landed native-library wire grammar (`library/api.py`,
  `models.py`). Library responses KEEP null keys (not `exclude_none`), so `nextCursor`/`olderCursor`/
  `safeNativeIdSuffix`/`lastActivityAt` arrive as explicit `null` (treated identically to absent). A
  `ConversationLibraryRow` is read-only dormant history and is NEVER a live AR session. Carries the
  `OpenConversationOperation` with its `OpenPhase`/`OpenOutcome` unions and the branded list/read/key
  cursors. **Sub-agent grouping:** a row may carry `agents` —
  `ConversationLibraryAgentRow` children grouped under it (own server-minted `conversationKey`,
  optional `agentPath`/`nickname`/`role`/`model`/`joinKey`, NO capabilities block of their own), and
  the page carries `agentsNote` — capability honesty: the exact native reason sub-agent conversations
  are (partially) unavailable, when they are, never silently absent.
- `client.ts` — list/read (or-null reads) + open/open-status/open-reconcile (typed `OpenResult`
  evidence; a refusal is discriminated by the `phase`+`outcome` payload shape, never guessed into
  success). The open `requestId` is caller-stable and reused across status/reconcile — a lost response
  is reconciled under the SAME id, never a fresh one (§9.4, invariant 27). Optional launch context
  carries the canonical `TaskDocumentRef` plus seat role; it does not expose or reconstruct a leaf or
  runtime-session address.
- `store.ts` — the `conversationLibraryStore` + list/preview/open orchestration. `openedForFocus` is the
  sole focus gate (set only on `opened`/`opened`); there is no active-marking field. The open flow is
  hardened per fix-round F6: `dispatching` from dispatch blocks a double-open (F6c); the requestId is
  retained across a transport failure (F6b); a spent poll budget stops and offers a manual reconcile
  under the same id (F6a). `LibraryListView` carries the page's `agentsNote`:
  `loadLibraryList` preserves the previous note through loading/error and takes the freshest page's
  note on success (it describes the query's current agent availability).

## Invariants And Boundaries

- **Reconstructable, no durable index (R1).** The store holds only server-derived rows/previews; reload
  reconstructs.
- **A library row is never active (R4).** The store surfaces `arSessionId` for focus ONLY when the open
  operation is `phase="opened" && outcome="opened"`; it has no field that marks a row live. Only exact
  catalog evidence in the LIVE session store can make a session active.
- **Every non-opened outcome preserves the current state.** `unsupported`/`stale-identity`/
  `timeout-unknown`/`launch-failed`/`identity-mismatch`/`request-conflict` are surfaced without focusing,
  and the current draft/focus/scroll survive.
- **One id across the whole open lifecycle.** `beginOpen`/`reconcileOpen`/the poll loop all carry the
  caller-stable requestId; `applyOpen` keeps the id on failure so the next attempt reconciles, never
  re-opens under a new id (invariant 27). `dispatching` closes the TOCTOU double-open window.
- **Preview is read-only history.** A stale preview (selection moved on) is dropped, never mis-applied.

## Hot Path Summary

1. `loadLibraryList` pages the native list for a harness/scope (append on cursor); `loadLibraryPreview`
   reads one conversation's read-only historical page and drops the result if the selection moved on.
2. `beginOpen` POSTs one exact-open under a caller-stable requestId with `dispatching` set from dispatch;
   while pending/timeout-unknown it re-drives open-status/open-reconcile under the same id until terminal.
3. On terminal `opened`/`opened`, `openedForFocus` flips true and the caller (OpenConversationAction →
   ChatsStageBody) focuses the new live row; every other outcome leaves the current state intact.

## Child Route Onboarding Map

No deeper child route exists below `data/conversation-library/`; each source has a one-to-one file card
and this overview is their governing pillar.

## File Onboarding Map

| Responsibility | File onboarding |
| --- | --- |
| Library wire mirror | [types.ts](types.ts.md) |
| List/read/open HTTP client | [client.ts](client.ts.md) |
| Reconstructable store + open orchestration | [store.ts](store.ts.md) · [store.test.ts](store.test.ts.md) |

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This route's statements were verified from its direct agents-remember source/tests and the
reviewed worker report and final-PASS review verdict.

No configured Domain Documentation source exists for this route.

### Cross-Repo References

The route mirrors this repository's own landed library wire contract and talks only to this package's
serving endpoints; no cross-repository implementation source governs it.

No applicable cross-repository source was found.

### Repo-Internal References

- The browser client and native serving route expose library listing for a harness with optional query fields. [1]
- The browser client and native serving route read a historical conversation page. [2]
- The browser client and native serving route open a conversation. [3]
- The browser client and native serving route report open-request status. [4]
- The browser client and native serving route reconcile an open request. [5]
- The in-stage browser view reads this library state and starts list loading. [6]
- The sibling active-conversation state is a separate projection. [7]
- The parent data boundary keeps `dashboardStore`/`DashboardState` separate from `conversationLibraryStore`. [8]
