# dashboard/src/data/selectors.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/selectors.test.ts`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Vitest coverage for pure store selectors in `dashboard/src/data/selectors.ts`: lifecycle grouping,
wait-time formatting, and attention queue display filtering.

## Code Commentary

### Logic

The `lifecycle(...)` fixture builds minimal `LifecycleProjection` rows so `buildTree` can be tested by
phase pipeline order, repo grouping, and the `(unassigned)` fallback. `fmtWait` coverage pins s/m/h/d
formatting plus the unknown dash. The `hasLiveWorktree` case (260703-L11) pins the four-flag truth
table of the tasks-surface visibility rule: either existing worktree (code or memory) admits, and only
both-false hides — no cleanup-state input exists in the signature at all. The `selectQueue` tests
assert the server-computed queue is returned
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation applies to these pure selector tests. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `selectQueue` coverage includes empty analytics and optimistic suppression. | "reads the server-computed queue, empty when analytics is absent" | dashboard/src/data/selectors.test.ts:74-89 |
| Tree grouping and wait formatting tests cover the unchanged selector behavior. | "BY PHASE groups by l-01 phase in pipeline order, members id-sorted"; "scales seconds → s/m/h/d and renders unknown as a dash" | dashboard/src/data/selectors.test.ts:25-36; dashboard/src/data/selectors.test.ts:64-70 |
| The selector under test caches and filters attention rows. | `selectQueue` | dashboard/src/data/selectors.ts:37-46 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-02T20:43+02:00 — W2-B08: anchored 3 selector-test citation claims and normalized two generic no-document/boundary placeholders to `n/a | n/a`; no Tier 3 rows remain. Verification metadata stays pinned until closeout.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-06T02:55+02:00 — 260703-L11: added the `hasLiveWorktree` truth-table case pinning the
  existence-only tasks-surface visibility rule. Verification metadata pinned until closeout stamps the
  L11 commit.
- 2026-06-28T07:32+02:00 — Task 29 S7 follow-up: created the missing sidecar and documented coverage for
  the optimistic attention suppression selector behavior. Verification metadata is pinned to the last
  committed file version until closeout stamps the task-29 code commit.
