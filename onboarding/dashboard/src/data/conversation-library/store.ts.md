# dashboard/src/data/conversation-library/store.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/conversation-library/store.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:40+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c` |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

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

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The client verbs (list/read/open/status/reconcile) this store orchestrates. | `openConversation` | dashboard/src/data/conversation-library/client.ts:127-135 |
| The wire types the tracker and views hold. | `OpenConversationOperation` | dashboard/src/data/conversation-library/types.ts:91-110 |
| The in-stage browser view that reads this store and renders list/preview/open. | `ConversationLibrarySurface` | dashboard/src/panels/session-cockpit/conversation-library/ConversationLibrarySurface.tsx:75-171 |
| The sole resume action consuming `beginOpen`/`reconcileOpen` and the `openedForFocus` gate. | `OpenConversationAction` | dashboard/src/panels/session-cockpit/conversation-library/OpenConversationAction.tsx:72-174 |
| The open-flow (R4/F6) regression suite over this store. | "conversation library open flow (R4 — focus only on exact opened proof)" | dashboard/src/data/conversation-library/store.test.ts:34-136 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-11T19:58+02:00 — Recorded the store's typed task-document launch context while
  preserving caller-stable request identity and exact-open focus discipline.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-04T17:52+02:00 — 260731-EFA-L6 S18-B15 curator: resolved 18 citation findings. Converted the
  eight Logic line-cite parentheticals to cit form with exact anchors/ranges (`ConversationLibraryState`
  through `runOpenPolls`), and re-anchored + re-ranged the five Repo-Internal References rows (client
  verbs, wire types, library surface, resume action, open-flow suite). Scoped recheck clean.
- 2026-07-26T15:40+02:00 — 260718-CHATS-L7 curator: refreshed for the page-level `agentsNote` on
  `LibraryListView` — `loadLibraryList` carries the previous note through loading/error states and
  takes the freshest page's note on success; all downstream line citations re-stamped against the
  post-L7 source. The L7 source is uncommitted, so lastVerifiedCommit* stays on the prior stamp and
  closeout re-stamps verification.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the reconstructable
  library store — paged list/preview state, the caller-stable open tracker (`dispatching`/
  `pollsExhausted`/`openedForFocus`), the bounded escalating poll loop, and the R4 discipline that
  never marks a row active and focuses only on exact opened proof (F6a/F6b/F6c). Verification is pinned
  to the leaf base (`0be0099`) because the new source file is uncommitted; closeout owns its first
  source stamp.
