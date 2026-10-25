# dashboard/src/data/reviewMemoryWatch.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Scope live-review invalidation to a mounted repository/master/leaf on the existing state SSE, rather than poll memory or open an additional connection. The module owns registration and revision-baseline fanout; stream.ts owns EventSource and the review cycle owns rereading.

## Code Commentary

Registrations are held in insertion order; reviewMemoryScope selects the first registered scope. Additional registrations are not an independent multiplexed transport. Adding/removing a registration resets revision and notifies scope listeners only if the effective first scope changes. Disposal removes the callback, and the last registration leaves no scope/baseline.

publishReviewMemory ignores a different scope and a non-string revision. The first baseline, an explicit initial/reconnect flag, or a changed revision notifies matching registrations. The first native baseline is deliberately a reconciliation point: it cannot prove the independently read HTTP snapshot was already current during admission/arming. After that, an identical noninitial revision is quiet. Errors fan out only to the effective matching scope and carry the supplied detail or the explicit Retry/reopen fallback.

useReviewMemoryWatch derives liveness from an enclosure matching repoName/taskName/leafId whose worktree-group basename is in activeWorktreeGroups; recorded history never registers. A latest ref supplies current cycle/entry callbacks without resubscribing on every render. A matching change first retains/engages the visible selection, then calls memoryChanged and the shared entry revalidate. A failure calls memoryWatchFailed, not a success or empty result. Cleanup reclaims the registration. This does not promise watches for every detail panel or parallel transport scopes, a fixed publication latency, or current tests.

The same module also has a separate moved-notice subscriber set keyed by exact repository/master/leaf. publishReviewExplainerMoved accepts the host's repo/repository, master/task and leaf/leaf_id spellings, rejects an unaddressed payload and notifies only matching subscriptions. It carries comparison/master moves and cleared notices without opening an EventSource, re-reading state or waking an agent itself.

## Evidence

- First effective registration owns the scope and scope changes reset the baseline. [1]

- First/reconnect baseline reconciles once; unchanged matching revisions then stay quiet. [2]

- Errors are matched to the effective scope and forwarded as named failures. [3]

- Only live non-recorded reviews register; matching changes retain selection then refresh cycle/entry. [4]

- Existing state transport carries scope query and both memory event types. [5]

- ReviewSurface supplies the watch its scope and cycle only: `useReviewMemoryWatch({ repo, master, leaf, history }, cycle)`; no retain-selection callback travels with it. [6]

- The same module also has a separate moved-notice subscriber set keyed by exact repository/master/leaf. publishReviewExplainerMoved accepts the host's repo/repository, master/task and leaf/leaf_id spellings, rejects an unaddressed payload and notifies only matching subscriptions. It carries comparison/master moves and cleared notices without opening an EventSource, re-reading state or waking an agent itself. [7]
