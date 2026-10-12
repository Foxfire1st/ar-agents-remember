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

`data/conversation-library/` holds the reconstructable browser projection of the native
previous-conversation library: paged list-query state, read-only historical preview pages,
the selected preview identity, and the caller-stable open operation with its phase and revision.
The store has no persistence adapter or durable browser index; a new browser instance rebuilds its
list from the server. Library history remains separate from the active-conversation projection
and the surrounding dashboard state.

Opening history requests a controlled session for that exact conversation. The browser permits the
opened-session callback only when the returned operation has both `phase="opened"` and
`outcome="opened"`, and supplies an `arSessionId`. The server establishes the opened result after
observing matching native identity and reading submission authority from the catalog entry.
Other results are reported without invoking that callback.

## Hot Path Summary

1. `ConversationLibrarySurface` reads the library store and starts list loading for its harness and
   scope. Load-more supplies the list cursor. Selecting a row loads its historical preview; a response
   for a superseded selection is discarded.
2. `beginOpen` sends the conversation key, expected identity digest and caller-supplied request ID.
   For pending or timeout-unknown results, subsequent status/reconcile requests reuse the ID until
   terminal, transport failure, supersession or poll-budget exhaustion. Manual reconciliation also
   uses that ID.
3. `applyOpen` sets `openedForFocus` only for the exact opened phase/outcome pair.
   `OpenConversationAction` additionally requires the matching conversation key and an `arSessionId`
   before calling `onOpened`. `ConversationLibrarySurface` forwards that callback;
   `LibraryAndDiagnostics`, rendered by `ChatsStageBody`, closes the library and forwards the session
   ID through `onSessionOpened`. Other operation outcomes do not trigger this handoff.

## Construction

- `types.ts` mirrors the library wire models. It defines branded list/read cursors and conversation
  keys, dormant-history rows, historical pages, and the open phase/outcome unions. Optional nullable
  identity-display fields accompany each row. A parent row may group `ConversationLibraryAgentRow`
  children with their own conversation key and identity digest, optional agent path, nickname, role,
  model and join key, and no separate capabilities block. The page may carry `agentsNote`, describing
  unavailable or partially available agent history.
- `client.ts` requests harness-scoped list and historical-read routes, returning `null` on failed
  reads. The open, status and reconcile routes return typed operation-or-error results. A body with
  both `phase` and `outcome` is treated as an operation even on a refusal HTTP status; success is not
  inferred from HTTP status alone. Optional launch context carries a canonical task document reference
  and seat role rather than a leaf or runtime-session address. Library serialization retains null
  fields rather than using `exclude_none`.
- `store.ts` owns the independent `conversationLibraryStore` and its loaders. List loading appends
  when a cursor is supplied and the previous list has the same harness; otherwise it replaces rows.
  Loading and failure retain the previous `agentsNote`; success adopts the latest page's note.
  Preview loading selects a key and drops the response if that key is no longer selected.
- Open orchestration records `dispatching` before sending the initial request and retains the supplied
  request ID on transport failure. Pending and timeout-unknown operations are polled under that same
  ID. Polling has a finite budget; exhaustion exposes a manual reconcile state. The UI disables the
  tracked row's action while dispatching or polling and reuses its ID after transport failure or
  exhaustion. This is a UI guard for that row, not a store-level exclusion of all concurrent opens.

## Invariants And Boundaries

- **Reconstructable history.** This store holds server-returned library rows and previews plus browser
  query, selection and open-tracking state. It does not persist a browser index or mark history rows
  active. The active-conversation and dashboard projections have separate state owners.
- **Exact-open handoff.** `openedForFocus` depends on both opened discriminants. The store can retain
  operation identity data for other outcomes; the presence of `arSessionId` alone is not permission
  to focus a session.
- **Non-opened outcomes do not select another chat.** Unsupported, stale-identity, timeout-unknown,
  launch-failed, identity-mismatch and request-conflict results remain status evidence. The library
  orchestration does not write the current chat's draft, focus or scroll state, and its action invokes
  the opened-session callback only through the exact-open gate. Opening the library itself focuses
  its heading; this boundary does not promise unchanged DOM focus throughout library interaction.
- **One ID for an unresolved open.** Initial dispatch, automatic status/reconcile and manual recovery
  carry the same request ID. A transport error preserves it so the UI can reconcile. A later fresh
  open after a terminal result may receive a new ID.
- **Read-only preview.** Preview requests read historical pages and do not mutate the active
  conversation. A response is applied only while its conversation key remains selected.
- **Agent availability remains visible in state.** The list view carries `agentsNote` through loading
  and failure and replaces it with the latest successful page's note. Agent rows carry their own
  identity fields without inventing a child capabilities block.

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

- The browser client and native serving route expose library listing for a harness with optional query fields. [1]
- The browser client and native serving route read a historical conversation page. [2]
- The browser client and native serving route open a conversation. [3]
- The browser client and native serving route report open-request status. [4]
- The browser client and native serving route reconcile an open request. [5]
- The in-stage browser view reads this library state and starts list loading. [6]
- The sibling active-conversation state is a separate projection. [7]
- The parent data boundary keeps dashboardStore/DashboardState separate from conversationLibraryStore. [8]
