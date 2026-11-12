# dashboard/src/data/selectors.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Pure derivations over the dashboard Zustand store. These helpers keep React panels small and make
dashboard grouping, wait-time formatting, drift segmentation, worktree flattening, and attention
queue filtering unit-testable without a live browser stream.

## Code Commentary

### Logic

`selectQueue` reads the server-computed `analytics.attentionQueue`, drops the two attention kinds the server retired with the search providers (`provider-down`, `failed-setup`) so a legacy payload cannot raise them, and filters ids currently present in
`DashboardState.suppressedAttentionIds`. It returns a stable shared empty array when analytics is absent,
and caches the filtered result by queue reference plus suppression-map reference so Zustand
`useStore(selectQueue)` does not see a fresh array on every render. `hasLiveWorktree(enclosure)`
selects physical worktree surfaces only: true when `codeWorktreeExists ||
memoryWorktreeExists`, using the projection’s server-observed existence flags rather than a cleanup-state proxy. A reopened enclosure with neither path remains absent from Hangar; its task entry is still reachable regardless of whether worktrees exist, were cleaned up or have yet to start. Hangar retains physical-existence admission. Operations instead admits every served TaskEntry, including planned and terminal tasks without a worktree. `selectWorktrees` memoizes entry-bound worktrees plus unbound enclosures by source map identities, without matching identities. `fmtWait` formats server-computed ages only. The lower
helpers turn drift snapshot counts into a stable segment list and flatten the already-bound worktree facts
for operational surfaces. `DRIFT_ORDER` also orders the converted names `stale` and `violation`, so a converted
repository's bar reads the same good-to-actionable way as a legacy one.

`selectHostActivityUnknown` reads whether the served workspace unknown count is nonzero. Its consumers suppress unavailable per-row activity figures and show one shell notice; the selector neither polls the host nor decides a task's activity from time.

### Conventions

No React imports; selectors stay pure functions over projection/store values. Server-projected ordering
is preserved — the queue arrives newest first by served age and then id — unless this module explicitly
defines a display pivot order.

### Invariants And Boundaries

The queue is still computed server-side by the reducer. Suppression here is optimistic UI display state
for in-flight dismiss/clear commands, not durable dismissal authority, and it applies to every served
row: each entry is one acknowledgement of its own occurrence, so local state hides a live native cause
exactly as it hides a notice (`selectors.ts:39-43`). Wait times are formatted from
projected `waitSeconds`/`staleSeconds`; this module never calls the clock and never re-sorts the queue.

## Evidence

### Docs References

No relevant external documentation is needed for these store selectors.

No relevant documentation found after checking live sources.

### Repo-Internal References

- Host-observation availability is read from the served unknown count, not recomputed from agents or elapsed time. [4]


- selectQueue caches the visible queue by the queue array's identity and the suppression map's identity, and hides every row whose id is in that map, whatever the entry's kind. [1]



- The converted drift names order with the legacy classifications, healthy first. [3]



### Cross-Repo References

No meaningful cross-repo references found.

No meaningful cross-repo references found.
