# dashboard/src/data/conversation-library/ — Dormant Conversation Library Projection Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/data/conversation-library/`       |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-07-26T15:40+02:00                           |
| lastVerifiedCommitHash | `4e5fbcf872bbc1ec2566a6ccb17276a6bad80c7f`       |
| lastVerifiedCommitDate | 2026-07-26T18:40:37+02:00|
| governingOverview      | `../overview.md`                                 |

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
  is reconciled under the SAME id, never a fresh one (§9.4, invariant 27).
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

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This route's statements were verified from its direct agents-remember source/tests and the
reviewed worker report and final-PASS review verdict.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this route. | `system/sources.md` checked | — |

## Cross-Repo References

The route mirrors this repository's own landed library wire contract and talks only to this package's
serving endpoints; no cross-repository implementation source governs it.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The landed native-library serving routes this client consumes. | [library/api.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/api.py) |
| The in-stage browser view that renders this store. | [session-cockpit/conversation-library overview](../../panels/session-cockpit/conversation-library/overview.md) |
| The sibling active-conversation projection. | [data/conversation overview](../conversation/overview.md) |
| The parent data authority boundary. | [data overview](../overview.md) |

## Update History

- 2026-07-26T15:40+02:00 — 260718-CHATS-L7 curator: extended the wire+store contract for the harness
  sub-agent grouping — `ConversationLibraryRow.agents` (capability-free `ConversationLibraryAgentRow`
  children, server-minted keys), the page-level `agentsNote` capability-honesty field, and the store's
  carry-through-loading / freshest-page-wins note rule. The L7 source is uncommitted, so
  lastVerifiedCommit* stays on the prior stamp and closeout re-stamps verification.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the governing pillar for the reconstructable
  dormant conversation-library projection — the exact-open focus gate (R4: focus only on
  `opened`/`opened`, no active-marking field), the caller-stable open requestId reconciled under one id
  (invariant 27), the F6 open-flow hardening (dispatch-time busy, transport-retained id, poll-exhaustion
  reconcile), and the no-durable-index rule. Verification is pinned to the leaf base (`0be0099`) because
  the new source route is uncommitted; closeout owns its first source stamp.
