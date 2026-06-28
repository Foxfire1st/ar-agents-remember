# dashboard/src/data/selectors.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/selectors.ts`                |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-28T07:32+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Pure derivations over the dashboard Zustand store. These helpers keep React panels small and make
dashboard grouping, wait-time formatting, provider-stack grouping, drift segmentation, and attention
queue filtering unit-testable without a live browser stream.

## Code Commentary

### Logic

`selectQueue` reads the server-computed `analytics.attentionQueue` and filters ids currently present in
`DashboardState.suppressedAttentionIds`. It returns a stable shared empty array when analytics is absent,
and caches the filtered result by queue reference plus suppression-map reference so Zustand
`useStore(selectQueue)` does not see a fresh array on every render. `buildTree` pivots lifecycle rows by
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant documentation found after checking local project source and package contracts. | N/A | [dashboard/src/data/selectors.ts](selectors.ts) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `selectQueue` caches filtered queue arrays by source references and filters optimistic suppression ids. | L16-L32 | [selectors.ts](selectors.ts) |
| Lifecycle tree grouping and wait formatting are pure display derivations. | L34-L100 | [selectors.ts](selectors.ts) |
| Store state owns `suppressedAttentionIds`, not this selector. | L29-L39 | [store.ts](store.ts) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This selector layer does not cross repository boundaries. | N/A | [selectors.ts](selectors.ts) |

## Update History

- 2026-06-28T07:32+02:00 — Task 29 S7 follow-up: created the missing sidecar and documented the cached
  `selectQueue` suppression filter added for optimistic attention dismissals. Verification metadata is
  pinned to the last committed file version until closeout stamps the task-29 code commit.
