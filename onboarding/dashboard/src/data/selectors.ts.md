# dashboard/src/data/selectors.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/selectors.ts`                |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `2e11db883f77bb1bf2827ae537b5d1d564e020b3`       |
| lastVerifiedCommitDate | 2026-09-24T22:33:57+02:00|
| governingOverview | `overview.md` |

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
recreates its worktrees). **Its consumers no longer read the same way, and the difference matters
(260921-ICR-L33).** `Hangar` still renders a leaf ONLY while a worktree physically exists: the selector
is its whole admission rule. `LifecycleList` uses it to build its ACTIVE enclosure list — which is what
admits a LIVE leaf's row and what the landed-leaf rule reads to tell live from landed — but since that
leaf it ALSO renders a landed leaf (a non-master document whose status is `Completed`) as a row under
its open master, because closeout removed the worktree such a leaf can never match the selector again.
The selector is unchanged; what changed is that it is no longer the only way a leaf's work becomes
reachable in the Operations list. `panels/lifecycle-list/landedLeaves.ts` owns that second rule. `buildTree` pivots lifecycle rows by
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

## Docs References

No relevant external documentation is needed for these store selectors.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `selectQueue` caches filtered queue arrays by source references and filters optimistic suppression ids. | `selectQueue` | dashboard/src/data/selectors.ts:37-46 |
| Lifecycle tree grouping and wait formatting are pure display derivations. | `buildTree` | dashboard/src/data/selectors.ts:73-105 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-24T23:30:00+02:00 — 260921-ICR-L33 curator (candidate `ar/260921-icr-l33-ar`, uncommitted; code base `86639933d61528387ce106dbd4d7a334bd468671` plus the working-tree delta; adversarial round 2 `verify-l33.md` = `pass`): **one false sentence corrected in place.** The Logic paragraph said `Hangar` **and** `LifecycleList` render a leaf "ONLY while a worktree physically exists" — true of `Hangar`, false of `LifecycleList` at this candidate, which now materializes a `Completed` leaf's row under its open master. This card's source (`data/selectors.ts`) is unchanged by the leaf; only its description of the second consumer was wrong, and it now states which consumer reads the selector as its whole rule and which reads it as the live half of a two-rule admission. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-08-03T02:57+02:00 — W3-B03 curator: curated 2 table citations for selector tree construction and suppressed-attention state; fixer-generated ranges verified.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-06T02:50+02:00 — 260703-L11: added `hasLiveWorktree`, the shared tasks-surface visibility
  rule over `EnclosureNode.codeWorktreeExists`/`memoryWorktreeExists` (existence truth, never a
  cleanup-state proxy), consumed by `Hangar` and `LifecycleList`. Verification metadata pinned until
  closeout stamps the L11 commit.
- 2026-06-28T07:32+02:00 — Task 29 S7 follow-up: created the missing sidecar and documented the cached
  `selectQueue` suppression filter added for optimistic attention dismissals. Verification metadata is
  pinned to the last committed file version until closeout stamps the task-29 code commit.
