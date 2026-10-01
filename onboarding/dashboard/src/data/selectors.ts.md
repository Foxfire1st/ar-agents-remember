# dashboard/src/data/selectors.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Pure derivations over the dashboard Zustand store. These helpers keep React panels small and make
dashboard grouping, wait-time formatting, provider-stack grouping, drift segmentation, and attention
queue filtering unit-testable without a live browser stream.

## Code Commentary

### Logic

`selectQueue` reads the server-computed `analytics.attentionQueue` and filters ids currently present in
`DashboardState.suppressedAttentionIds`. It returns a stable shared empty array when analytics is absent,
and caches the filtered result by queue reference plus suppression-map reference so Zustand
`useStore(selectQueue)` does not see a fresh array on every render. `hasLiveWorktree(enclosure)`
(260703-L11) is the shared tasks-surface visibility rule: true when `codeWorktreeExists ||
memoryWorktreeExists` — the projection's stat'ed worktree-existence truth — never inferring liveness
from a cleanup-state proxy (a `cleanup: reopened` contract stays hidden until `worktree_start`
recreates its worktrees). **Its consumers read the same way again (corrected by the `260921-ICR-L34`
curation).** `Hangar` renders a leaf ONLY while a worktree physically exists, and so does
`LifecycleList`: the selector is the whole admission rule for both. **The landed-leaf rule this
paragraph used to describe is withdrawn** — commit `a9a1a41b` (*"Revert L33's operations-list change;
clear the pre-existing ruff-format red"*, a direct emergency commit with no curator pass behind it)
deleted `panels/lifecycle-list/landedLeaves.ts` after `260921-ICR-L33` added it, so a `Completed` leaf
whose worktree closeout removed is **not** rendered as a row under its master and the module that owned
that second rule exists in neither tree. `buildTree` pivots lifecycle rows by
l-01 phase or repo with deterministic ordering. `fmtWait` formats server-computed ages only. The lower
helpers translate provider snapshots into engine-room display groupings and drift snapshot counts into a
stable segment list.

### Conventions

No React imports; selectors stay pure functions over projection/store values. Server-projected ordering
is preserved unless this module explicitly defines a display pivot order.

### Invariants And Boundaries

The queue is still computed server-side by the reducer. Suppression here is optimistic UI display state
for in-flight dismiss/clear commands, not durable dismissal authority. Wait times are formatted from
projected `waitSeconds`/`staleSeconds`; this module never calls the clock.

## Evidence

### Docs References

No relevant external documentation is needed for these store selectors.

No relevant documentation found after checking live sources.

### Repo-Internal References

- `selectQueue` caches filtered queue arrays by source references and filters optimistic suppression ids. [1]
- Lifecycle tree grouping and wait formatting are pure display derivations. [2]

### Cross-Repo References

No meaningful cross-repo references found.

No meaningful cross-repo references found.
