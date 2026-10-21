# dashboard/src/data/reviewTrees.ts

## Governing Overview

[dashboard/src/data route overview](overview.md)

## Purpose

The client adapter of the reviewer's tree view, `GET /api/review/trees`. It declares the types of the
answer, builds the request, turns an answer into a read state, and provides the React hooks that read
the leaf-wide view and the cards of the page’s shown invariant set. Declared contract fields use snake_case; open facts/rows remain opaque maps rather than a runtime key validator.

`data/reviewTrees.ts` is the tree-view adapter for one leaf: the four-tree comparison, knowledge-side states, per-side currentness, worklist gate verdicts/witnesses, leaf-wide implementation facts, and focused card entries. In W03 it no longer carries the memory-tree knowledge diff; changed knowledge files are read on the change-set page instead.
## Code Commentary

The page reads cards for its shown invariant set through `useChangeSetCards`, independently of subject selection. IDs are sorted and deduplicated, cut into at most 500 invariants per request, and merged in chunk order. The module-shared completed store is capped at 20 chunk answers; in-flight questions are shared without a separate concurrency cap. Keys include repository/master/leaf, comparison and the sorted chunk. A new question shows loading instead of another set’s answer.

Only keepable trees answers enter that store. `unavailable-history` on a knowledge or code side, or unavailable entry-memory values with a readable after knowledge side, makes the answer transient. This mount shows it; remount or the shared Refresh generation asks for it again. A kept successful answer is reused, and a genuinely unconverted side is retained as the record’s own answer. One chunk’s unavailable memory state makes the merged memory values unavailable, preserving its first reason.

### Types

- `ReviewTreesResult` has the state `trees`, `not-converted` or `refused`, with the comparison
  (`ReviewTreeComparison`: four tree sides, the pinning refs, an optional converted base), the knowledge
  sides with their index state, the code sides of a reopened comparison,
  the currentness of each side, the worklist view, the entries of named
  invariants, or the refusal.
  It has no `knowledge_diff` field; changed memory files are read through the comparison change-set viewer.
- `ReviewWorklistView` has the source `computed`, `persisted` or `absent`, the `bound` flag, the items, the
  history rows, optional `item_states` gate verdicts/witnesses, changes with linkage and incomplete entries.
  `ReviewItemVerdict` distinguishes `answered`, `open` and `undecided`; `witness`, `row_id` and `reason`
  remain optional. A history annotation is not itself the native predicate verdict.
- Optional `code_changes` is `ReviewCodeChanges`: `facts` or `unavailable`, with each `ReviewCodeChange`
  carrying invariant IDs, implementation fact, proof/range flags, evidence and unknown reasons. Missing
  facts are not a measured empty population; these are supplied owner values, not browser reclassification.
- `ReviewTreeEntry` locates one realization or proof entry on both code sides (`ReviewTreeEntrySide`).

### Request and read state

- `reviewTrees(repo, master, leaf, address, base, signal)` builds the query from the task context and the
  address: `comparison=<n>`, `history=recorded`, `invariants=<a,b,...>`. It never sends a path or a tree ID.
  The optional `signal` is passed to `getReviewJson`.
- `reviewTreesRead` turns an answer into one of three phases of `ReviewTreesRead`: `trees` (only with its
  comparison), `not-converted`, and `unavailable`, which carries the owner's refusal or, for any other
  body, an unreadable-answer failure. The fourth phase, `loading`, is set only by the hooks.
- `degradedKnowledgeSides` returns every side that is not `available` or was read from a `partial` index.
  `invariantCurrentness` reads one invariant's state on each side. `unexplainedHunks` lists the hunks the
  gate linked to no knowledge. `treeComparisonNumber` reads the comparison number from the limitation
  token `review:trees:<n>`; without it no comparison number was supplied, so the caller must not guess
  one or infer a surviving dataset-review mode.

### Retrying a transient refusal

- `TRANSIENT_CODES` is `reviewer_busy` and `inputs_changing`. `BUSY_DELAYS_MS` is 1500, 2000, 3000, 4000,
  5000, 6000 and 8000 milliseconds, and `BUSY_RETRIES` is its length, 7.
- `reviewTreesRetryingBusy` reads the view and, while the answer is a refusal with a transient code, waits
  the next delay and reads again. After the seventh retry it returns whatever the answer is, so a view is
  read at most eight times. The declared delay sum is29,500ms, not a fresh wall-clock measurement. Any other answer is returned at once.
- `pause(ms, signal)` waits and rejects with an `AbortError` when the signal is aborted, clearing its
  timer. A wait that is aborted starts no further request.

### Hooks

- `useReviewTrees(repo, master, leaf, address, enabled)` reads the leaf-wide view through
  `reviewTreesRetryingBusy`. Each run of its effect creates an `AbortController` and aborts it in the
  cleanup, that is, when the task context or the address changes and when the component unmounts. The
  abort cancels the request in flight and any retry wait, so the server stops computing a view nobody
  shows. An answer is applied only when its controller is not aborted and its sequence number is the
  latest. For a new question key it reports `loading` until an answer for that key is stored, including
  initial busy retries. A previously stored same-key answer can remain during a later effect run; the
  hook does not clear it merely to start a read. Failures become `unavailable` only when applied. With `enabled` false it makes no request and returns `null`.
- `useChangeSetCards(repo, master, leaf, comparison, invariants, enabled)` returns null while disabled or without a comparison number. An empty invariant set is a cards answer with no entries and a null comparison, requiring no card request. The hook shares uncancelled chunk acquisitions; cleanup suppresses updates to an unmounted consumer. Failed reads remain visible to the mount while retrying; kept answers remain reusable. This differs from the leaf-wide hook’s aborting acquisition.

The deleted `ReviewKnowledgeTreeDiff` family (`ReviewKnowledgeFileChange`, record/source groupings, the `knowledge_diff` field on `ReviewTreesResult`) was the Git diff of the two memory trees grouped by record and source path with per-file patches. That earlier removal is historical, not a claim that the current full answer is byte-identical. This leaf adds optional item verdicts and leaf-wide implementation facts to the declared mirror. The earlier emitted-JavaScript equality observation applied to its historical comparison, not this changed implementation; the card reader now has different executable behavior. `reviewTrees` task/number addressing, the busy-retry discipline (`TRANSIENT_CODES`, `BUSY_DELAYS_MS`) and the `ReviewTreesRead` phases are retained; the page-card hook composes its separate `ChangeSetCardsRead` phases.
Each `ReviewTreeEntrySide` can carry its locator’s `symbol`. A card entry can carry the four supplied after-index memory values (`invariants_at_path`, `incoming_links`, `without_proof`, `open_weaknesses`) and their path. The card result’s `entry_memory` states available or unavailable, names its tree, and may name partial index state or a reason. This adapter carries those facts; it does not compute the four values.

## Evidence

- A superseded read is aborted and only the newer answer is shown. [21]

- Stored fake-timer assertions keep loading during initial busy retries and check the declared schedule; this is not fresh elapsed-time evidence. [22]

- Unavailable is shown only after the bounded number of retries. [23]

- The module comment: what the adapter carries and the three answers it keeps apart. [10]

- The result mirrors current tree comparison, knowledge/code sides, optional gate/currentness/code-change data, entries and refusal. [11]

- The worklist carries source/bound facts, rows and optional native item verdicts/witnesses rather than deriving a gate grade from annotations. [12]

- The request, addressed by number, recorded or invariants, with the optional signal. [13]

- The transient codes and the retry delays. [14]

- A wait that an abort ends. [15]

- The bounded retry of a transient refusal. [16]

- One answer as a read state. [17]

- The comparison a payload names. [18]


- The leaf-wide hook: abort on cleanup, sequence number, retry, and the enabled flag. [20]

- The busy-retry implementation is preserved in BASE/candidate erased JavaScript; its bounds do not certify current service performance. [25]

- The trees / not-converted / unavailable phases are unchanged [26]

- The declared item verdict and implementation-fact shapes preserve answered/open/undecided and facts/unavailable without a favourable missing-data default. [27]

- Shown-set cards use sorted distinct chunks, stable answer retention and retryable per-mount failures. [19]
- Entry symbols and supplied memory values retain their optional and unavailable states. [28]
