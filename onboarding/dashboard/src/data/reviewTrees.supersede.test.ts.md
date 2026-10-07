# dashboard/src/data/reviewTrees.supersede.test.ts

## Governing Overview

[dashboard/src/data route overview](overview.md)

## Purpose

Tests of `useReviewTrees` in `reviewTrees.ts` for two behaviours of the leaf-wide read: a read that a
newer selection supersedes is aborted, and a transient refusal is retried a bounded number of times before
the reader shows "unavailable". `fetch` is replaced by a stub, and the retry cases run on fake timers.

## Code Commentary

### A superseded read

- "aborts the superseded request and shows only the newer answer": the hook is rendered for leaf `first`
  and then for leaf `second`. The first request's signal is aborted, the second's is not, and the state
  becomes the second answer (`not-converted`).
- "aborts the request when the view goes away": unmounting the hook aborts the signal of its request.

### A transient refusal

`serveBusy(times, refusal)` answers the first `times` requests with a refusal and every request after
them with `not-converted`.

- "is asked again a moment later and the reader never sees it when a retry answers": two `reviewer_busy`
  answers, then an answer; after the first two delays the state is `not-converted` and three requests were
  made.
- "keeps showing "computing" while it retries, and its horizon covers a draining queue": after two retries
  the state is still `loading`; the test pins the literal delays `BUSY_DELAYS_MS` = [1500, 2000, 3000,
  4000, 5000, 6000, 8000], `BUSY_RETRIES` = 7 and the final request count 8; after all delays the state is
  the answer. The delays are the fake-timer horizon the test advances, not a measured queue-drain time.
- "treats "the inputs keep changing" the same way": one `inputs_changing` answer is retried.
- "is shown as unavailable only after the bounded number of retries": with refusals only, the state becomes
  `unavailable` with the code `reviewer_busy` after `BUSY_RETRIES + 1` requests.
- "stops retrying when the selection moves on": after the first refusal the leaf changes; before the first
  delay has passed only the first leaf has asked and one timer is pending; after the rerender the first
  request's signal is aborted and still one timer is pending; advancing one delay makes three requests in
  all (`first`, `second`, `second`); after unmount no timer remains and further time passes make no further
  request.

## Evidence

- The module comment. [1]
- The three stub answers: busy, changing and not converted. [2]
- A superseded request is aborted. [3]
- Unmounting aborts the request. [4]
- A refusal that a retry answers is never shown. [5]
- Loading stays shown during retries; the literal seven delays, seven retries and eight requests are pinned. [6]
- The inputs_changing refusal is retried too. [7]
- Unavailable only after the bounded retries. [8]
- A moved selection aborts the old request, keeps one timer and stops the retries; unmount clears the timer. [9]
- The hook under test. [10]
