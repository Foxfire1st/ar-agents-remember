# dashboard/src/data/selectors.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Pure derivations over the dashboard Zustand store. These helpers keep React panels small and make
dashboard grouping, wait-time formatting, provider-stack grouping, drift segmentation, and attention
queue filtering unit-testable without a live browser stream.

## Code Commentary

### Logic

`selectQueue` reads the server-computed `analytics.attentionQueue` and drops a row only when that row is dismissible and its id is present in
`DashboardState.suppressedAttentionIds`; a non-dismissible row stays visible however the local map is written. It returns a stable shared empty array when analytics is absent,
and caches the filtered result by queue reference plus suppression-map reference so Zustand
`useStore(selectQueue)` does not see a fresh array on every render. `hasLiveWorktree(enclosure)`
selects physical worktree surfaces only: true when `codeWorktreeExists ||
memoryWorktreeExists`, using the projection’s server-observed existence flags rather than a cleanup-state proxy. A reopened enclosure with neither path remains absent from Hangar; its task entry is still reachable regardless of whether worktrees exist, were cleaned up or have yet to start. Hangar retains physical-existence admission. Operations instead admits every served TaskEntry, including planned and terminal tasks without a worktree. `selectWorktrees` memoizes entry-bound worktrees plus unbound enclosures by source map identities, without matching identities. `fmtWait` formats server-computed ages only. The lower
helpers translate provider snapshots into engine-room display groupings and drift snapshot counts into a
stable segment list. `DRIFT_ORDER` also orders the converted names `stale` and `violation`, so a converted
repository's bar reads the same good-to-actionable way as a legacy one.

`selectHostActivityUnknown` reads whether the served workspace unknown count is nonzero. Its consumers suppress unavailable per-row activity figures and show one shell notice; the selector neither polls the host nor decides a task's activity from time.

### Conventions

No React imports; selectors stay pure functions over projection/store values. Server-projected ordering
is preserved unless this module explicitly defines a display pivot order.

### Invariants And Boundaries

The queue is still computed server-side by the reducer. Suppression here is optimistic UI display state
for in-flight dismiss/clear commands, not durable dismissal authority, and it applies only to a row that carries an acknowledgement: a live native cause has none, so local state cannot take it off the queue. Wait times are formatted from
projected `waitSeconds`/`staleSeconds`; this module never calls the clock.

## Evidence

### Docs References

No relevant external documentation is needed for these store selectors.

No relevant documentation found after checking live sources.

### Repo-Internal References

- Host-observation availability is read from the served unknown count, not recomputed from agents or elapsed time. [4]

- selectQueue caches filtered queue arrays by queue and suppression-map identity and suppresses only dismissible rows whose ids are present in the local map. [1]

- The converted drift names order with the legacy classifications, healthy first. [3]


### Cross-Repo References

No meaningful cross-repo references found.

No meaningful cross-repo references found.
