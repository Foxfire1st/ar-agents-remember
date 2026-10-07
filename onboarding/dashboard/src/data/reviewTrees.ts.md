# dashboard/src/data/reviewTrees.ts

## Governing Overview

[dashboard/src/data route overview](overview.md)

## Purpose

The client adapter of the reviewer's tree view, `GET /api/review/trees`. It declares the types of the
answer, builds the request, turns an answer into a read state, and provides the two React hooks that read
the leaf-wide view and the entries of one selection. Every key of the wire types is snake_case.

## Code Commentary

### Types

- `ReviewTreesResult` has the state `trees`, `not-converted` or `refused`, with the comparison
  (`ReviewTreeComparison`: four tree sides, the pinning refs, an optional converted base), the knowledge
  sides with their index state, the code sides of a reopened comparison, the knowledge diff grouped by
  record and by source path, the currentness of each side, the worklist view, the entries of named
  invariants, or the refusal.
- `ReviewWorklistView` has the source `computed`, `persisted` or `absent`, the `bound` flag, the items, the
  history rows, the changes with their linkage, and the incomplete entries.
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
  token `review:trees:<n>`; a payload without it is a dataset review.

### Retrying a transient refusal

- `TRANSIENT_CODES` is `reviewer_busy` and `inputs_changing`. `BUSY_DELAYS_MS` is 1500, 2000, 3000, 4000,
  5000, 6000 and 8000 milliseconds, and `BUSY_RETRIES` is its length, 7.
- `reviewTreesRetryingBusy` reads the view and, while the answer is a refusal with a transient code, waits
  the next delay and reads again. After the seventh retry it returns whatever the answer is, so a view is
  read at most eight times. Any other answer is returned at once.
- `pause(ms, signal)` waits and rejects with an `AbortError` when the signal is aborted, clearing its
  timer. A wait that is aborted starts no further request.

### Hooks

- `useReviewTrees(repo, master, leaf, address, enabled)` reads the leaf-wide view through
  `reviewTreesRetryingBusy`. Each run of its effect creates an `AbortController` and aborts it in the
  cleanup, that is, when the task context or the address changes and when the component unmounts. The
  abort cancels the request in flight and any retry wait, so the server stops computing a view nobody
  shows. An answer is applied only when its controller is not aborted and its sequence number is the
  latest. While retries run, the hook keeps returning `loading`; it returns `unavailable` only with the
  final answer. With `enabled` false it makes no request and returns `null`.
- `useReviewTreeEntries(repo, master, leaf, comparison, invariants)` reads the entries of one selection
  from the comparison the review payload names, with the same abort on cleanup. It returns `null` without
  a comparison number or without invariants, and keeps an answer together with the question it answers.

## Evidence

- The module comment: what the adapter carries and the three answers it keeps apart. [10]
- The answer of the route. [11]
- The worklist view. [12]
- The request, addressed by number, recorded or invariants, with the optional signal. [13]
- The transient codes and the retry delays. [14]
- A wait that an abort ends. [15]
- The bounded retry of a transient refusal. [16]
- One answer as a read state. [17]
- The comparison a payload names. [18]
- The entries hook aborts a superseded read. [19]
- The leaf-wide hook: abort on cleanup, sequence number, retry, and the enabled flag. [20]
- A superseded read is aborted and only the newer answer is shown. [21]
- The reader keeps showing loading while it retries, and its delays add up to at least 25 seconds. [22]
- Unavailable is shown only after the bounded number of retries. [23]
