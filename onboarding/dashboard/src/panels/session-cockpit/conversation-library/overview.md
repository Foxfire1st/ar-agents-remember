# dashboard/src/panels/session-cockpit/conversation-library/ — In-Stage History Browser Overview

| Field                  | Value                                                               |
| ---------------------- | ------------------------------------------------------------------- |
| sourceRoute            | `dashboard/src/panels/session-cockpit/conversation-library/`        |

## Governing Overview

[session-cockpit overview](../overview.md) — this child owns the in-stage previous-conversation browser
while the session-cockpit overview owns the one-roof Chats composition. Its data authority is the
reconstructable [data/conversation-library](../../../data/conversation-library/overview.md) projection;
the sibling live renderer is [conversation/](../conversation/overview.md).

## Purpose

`session-cockpit/conversation-library/` browses a harness's normalized previous-conversation history inside the Chats stage. Selecting a row reads a historical preview using the live renderer's block grammar; it does not activate that history. The browser provides the `Open as new chat` resume action for a selected top-level row. It delegates list, preview and open-operation state to the reconstructable library projection, which has no durable browser index.

## Hot Path Summary

1. `ChatsStageBody` enables the library for a controlled session when library mode is requested and a harness id is available; `LibraryAndDiagnostics` mounts the surface.
2. The surface loads the harness list. Parent or child selection loads a read-only preview; only a selected top-level row supplies the open action.
3. The open action dispatches under one request id. Status polling and reconciliation retain that id; transport failure or poll exhaustion permits a manual reconciliation.
4. Only `phase="opened" && outcome="opened"`, together with a returned session id, reaches the cockpit focus callback. Other outcomes remain visible in the library.
5. Back, eligible Escape and palette return close the library through the shared focus-return handler.

## Route Model

- `ConversationLibrarySurface.tsx` composes the list, preview and open action. On mount or harness/scope dependency changes it focuses its heading and loads the list. Back calls `onBack`; Escape does so unless its target is an input, textarea or contenteditable element. List and preview updates do not explicitly move DOM focus. The page's `agentsNote` passes through the list-view adapter to the list.
- The surface establishes an inline-size container. Its columns use single-line flex, clipped overflow and `min-height:0`; a container query stacks them at widths up to `56rem`. The list and preview bases are `16rem` and `20rem`, and each delegates overflow to an interior scroller. This avoids the content-sized flex lines that wrapping would create inside the height clip. Shared Markdown prose uses `overflow-wrap: break-word`, inline code uses `white-space: nowrap`, and the application root overrides inherited `word-break` to `normal`.
- `ConversationLibraryList.tsx` renders boundary-truncated titles with the full title in the `title` attribute, humanized activity ages, safe native-id suffixes, completeness badges and explicit `Load more` paging. Sub-agent conversations appear as child rows with a `2ch` indent, dashed border, an `agent` badge and an optional role badge. Selection promotes a child to the parent row shape using the child's own key and identity digest, the parent's capabilities and an empty `agents` array. Child selection uses the same preview loader as parent selection. However, the surface resolves the open-action row only in the top-level `list.rows`; a child selection therefore does not mount the open action. The list renders a non-empty `agentsNote` verbatim when it reaches its populated-list branch; its error, initial-loading and empty branches return before that note.
- `ConversationHistoryPreview.tsx` labels loaded history `history preview · not active` and renders its items through `ConversationItemView`. It has no composer or live conversation action controls. Its partial note chooses the tool-completeness reason when that capability is unsupported, otherwise the completeness reason when unsupported, otherwise no note.
- `OpenConversationAction.tsx` starts an open with a new request id, the row's opaque key and expected identity digest, and optional cwd and launch context. It reflects operation outcomes and rollback state. A transport error or exhausted poll budget offers reconciliation under the existing request id. Its callback runs only for the selected row when the store's exact-open gate is true and the operation contains an `arSessionId`.
- The stage caller supplies launch context only when the focused session has a canonical `TaskDocumentRef`, forwarding that reference and its seat role through the shared contract. A successful open closes the library and passes the returned session id to the cockpit focus handler. Back, Escape and the palette's Back-to-current-chat command share the close handler, which restores the captured invoker if it remains connected and clears the return token.

## Invariants And Boundaries

- **Read-only history and a separate live projection.** Preview selection updates library selection/preview state, not live-session activation. The library store has no active-row field and persists no browser index. Reload reconstructs its list and preview from the serving APIs.
- **Exact-open focus gate.** The library store sets `openedForFocus` only when both operation phase and outcome equal `opened`. The action additionally requires the selected conversation key and an `arSessionId` before invoking the parent callback. Unsupported, stale-identity, timeout-unknown, launch-failed, identity-mismatch and request-conflict outcomes are reflected without that callback. This path does not write the current composer draft or live scroll state.
- **Stable reconciliation identity.** Dispatch marks the selected row busy before awaiting the first response, disabling its open button during dispatch and nonterminal polling. Transport errors retain the request id; exhausted polling stops and offers reconciliation under the same id. This is a guard for the displayed row, not a global prohibition on opening another row.
- **One resume action in this browser.** The list selects history and the preview renders history; the open-action component owns resume dispatch. Child-row preview support does not currently imply child-row resume support.
- **Exclusive stage presentation.** The stage keeps its live layers mounted but hides their wrapper with `display:none` while the library is shown. The conversation pool receives false visibility and scroll-geometry flags. The diagnostics drawer renders only when the library is not shown, so the two presentations do not overlap.
- **Height containment.** Columns remain a single flex line until the container query changes their direction; zero minimum heights and interior scrollers contain list and preview overflow.

## Child Route Onboarding Map

No deeper child route exists below `conversation-library/`; each source has a one-to-one file card and
this overview is their governing pillar.

## File Onboarding Map

| Responsibility | File onboarding |
| --- | --- |
| In-stage browser shell + return paths + layout | [ConversationLibrarySurface.tsx](ConversationLibrarySurface.tsx.md) |
| Native history list | [ConversationLibraryList.tsx](ConversationLibraryList.tsx.md) · [ConversationLibraryList.test.tsx](ConversationLibraryList.test.tsx.md) |
| Read-only preview | [ConversationHistoryPreview.tsx](ConversationHistoryPreview.tsx.md) |
| Sole exact-open resume action | [OpenConversationAction.tsx](OpenConversationAction.tsx.md) |

## Evidence

- The reconstructable library projection this browser reads. [1]

- The one-roof composition mounts this browser in-stage. [2]

- The historical preview reuses the live renderer block grammar. [3]
