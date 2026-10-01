# dashboard/src/data/conversation-library/store.ts

## Governing Overview

[data/conversation-library overview](overview.md)

## Purpose

The reconstructable conversation-library store (design §11.2, §11.3, R4): a vanilla zustand
`createStore` + a `useConversationLibrary(selector)` hook (house idiom, matching
`../conversation/store.ts` and `data/store.ts`). It holds paged list-query state, the read-only
preview page, the selected preview identity, and the caller-stable open-operation phase/revision — and
NOTHING durable. Reload reconstructs from server authority; there is no IndexedDB/localStorage/SQLite
library index. Its defining discipline is R4 focus honesty: it never marks a row active and exposes a
focus signal ONLY on exact opened-catalog proof.

## Code Commentary

### Logic

- **State shape** (cit:([`ConversationLibraryState`], dashboard/src/data/conversation-library/store.ts:65-75)): `list?: LibraryListView` (rows + `nextCursor` + scope + `agentsNote` +
  loading/error), `preview?: LibraryPreview`, `selectedKey`, and `open?: OpenTracker`. `OpenTracker` carries
  `requestId`, `dispatching` (from dispatch until the first response — blocks a double-dispatch, F6c),
  `pollsExhausted` (poll budget spent while non-terminal — offer a manual reconcile, F6a), and
  `openedForFocus` (true ONLY when `phase==="opened" && outcome==="opened"` — the sole focus gate).
- **`loadLibraryList`** (cit:([`loadLibraryList`], dashboard/src/data/conversation-library/store.ts:153-169)): sets a loading view (preserving prior rows when appending under a
  cursor), fetches, and either records `history unavailable for this harness` on `null` or merges
  rows and threads `canonicalProjectScope`/`nextCursor`. Append is detected by a non-null cursor on
  the same harness. **Agents note:** the previous view's `agentsNote` is carried
  through the loading and error states; on success the FRESHEST page's note wins (`page.agentsNote
  ?? null`) — it describes the query's current agent availability.
- **`loadLibraryPreview`** (cit:([`loadLibraryPreview`], dashboard/src/data/conversation-library/store.ts:171-187)): sets `selectedKey`, shows a loading preview, fetches the
  historical read page, and DROPS a stale preview if the selection moved on (`selectedKey !== key`).
- **`applyOpen`** (cit:([`applyOpen`], dashboard/src/data/conversation-library/store.ts:192-205)): folds an `OpenResult` into the tracker — on failure it KEEPS the
  requestId (F6b, reconcile under the same id) and clears `dispatching`/`openedForFocus`; on success
  it stores the operation and sets `openedForFocus` only for the opened/opened terminal.
- **`isTerminalOpen`** (cit:([`isTerminalOpen`], dashboard/src/data/conversation-library/store.ts:207-210)): `pending`/`timeout-unknown` keep polling under the same id;
  every other outcome is terminal.
- **`beginOpen`** (cit:([`beginOpen`], dashboard/src/data/conversation-library/store.ts:229-263)): sets `dispatching:true` BEFORE the first POST (F6c — a second click
  cannot open a second operation into the TOCTOU window), dispatches `openConversation`, folds the
  result, and starts polling only if non-terminal. Its optional launch context uses the shared
  `ConversationLaunchContext`, whose routing identity is `TaskDocumentRef` plus seat role.
- **`reconcileOpen`** (cit:([`reconcileOpen`], dashboard/src/data/conversation-library/store.ts:269-291)): the poll-exhaustion / transport-retry re-drive — reuses the
  EXISTING requestId and re-enters the poll loop with `reconcileFirst`, never minting a fresh id.
- **`runOpenPolls`** (cit:([`runOpenPolls`], dashboard/src/data/conversation-library/store.ts:262-300)): the bounded poll loop (`OPEN_POLL_MS`=1200, `OPEN_POLL_LIMIT`=25).
  It escalates `open-status`→`open-reconcile` every 5th poll (or immediately on a re-drive), aborts if
  the tracked requestId is superseded, and on budget exhaustion while still non-terminal sets
  `pollsExhausted` and stops (no dead-end "reconciling…" forever).

### Invariants And Boundaries

- **Never marks a row active.** No state field can flag a library row as a live AR session — the
  store's ONLY focus signal is `openedForFocus`, gated on `phase==="opened" && outcome==="opened"`.
  Every other outcome (`unsupported`/`stale-identity`/`timeout-unknown`/`launch-failed`/
  `identity-mismatch`/`request-conflict`) is surfaced without focusing (R4/§9.4). The caller leaves
  the current chat/draft/focus/scroll intact on all non-opened outcomes.
- **One caller-stable requestId per open, retained across failure.** Transport failure and poll
  exhaustion both reconcile under the SAME id (F6a/F6b); `dispatching` from dispatch time blocks a
  double-open (F6c).
- **Reconstructable, not durable.** The store caches only server-derived list/preview/open state;
  reload rebuilds it from `list`/`read` reads. There is no durable browser conversation index (R1).
- Preview reads never regress the selection: a preview that resolves after the user picks another row
  is dropped.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The client verbs (list/read/open/status/reconcile) this store orchestrates. [1]
- The wire types the tracker and views hold. [2]
- The in-stage browser view that reads this store and renders list/preview/open. [3]
- The sole resume action consuming `beginOpen`/`reconcileOpen` and the `openedForFocus` gate. [4]
- The open-flow (R4/F6) regression suite over this store. [5]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
