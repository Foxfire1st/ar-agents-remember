# dashboard/src/data/selectors.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/selectors.test.ts`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-28T07:32+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Vitest coverage for pure store selectors in `dashboard/src/data/selectors.ts`: lifecycle grouping,
wait-time formatting, and attention queue display filtering.

## Code Commentary

### Logic

The `lifecycle(...)` fixture builds minimal `LifecycleProjection` rows so `buildTree` can be tested by
phase pipeline order, repo grouping, and the `(unassigned)` fallback. `fmtWait` coverage pins s/m/h/d
formatting plus the unknown dash. The `selectQueue` tests assert the server-computed queue is returned
when analytics exists, a stable empty queue is returned when it does not, and optimistic
`suppressedAttentionIds` hide a matching queue row.

### Conventions

Pure unit tests only; no React render helpers or browser globals. Fixtures use the smallest projected
shape needed by the selector under test.

### Invariants And Boundaries

These tests do not prove backend attention derivation or dismissal persistence. They pin the frontend
selector contract: panels can subscribe to `selectQueue` without local filtering loops, and optimistic
suppression affects display only.

## Docs References

No relevant external documentation is needed for these pure selector tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant documentation found after checking local project source and package contracts. | N/A | [dashboard/src/data/selectors.test.ts](selectors.test.ts) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `selectQueue` coverage includes empty analytics and optimistic suppression. | L62-L95 | [selectors.test.ts](selectors.test.ts) |
| Tree grouping and wait formatting tests cover the unchanged selector behavior. | L23-L60 | [selectors.test.ts](selectors.test.ts) |
| The selector under test caches and filters attention rows. | L16-L32 | [selectors.ts](selectors.ts) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This test module does not cross repository boundaries. | N/A | [selectors.test.ts](selectors.test.ts) |

## Update History

- 2026-06-28T07:32+02:00 — Task 29 S7 follow-up: created the missing sidecar and documented coverage for
  the optimistic attention suppression selector behavior. Verification metadata is pinned to the last
  committed file version until closeout stamps the task-29 code commit.
