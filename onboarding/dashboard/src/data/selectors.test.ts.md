# dashboard/src/data/selectors.test.ts

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

## Evidence

### Docs References

No relevant external documentation is needed for these pure selector tests.

No relevant external documentation applies to these pure selector tests.

### Repo-Internal References

- `selectQueue` coverage includes empty analytics and optimistic suppression. [1]
- Tree grouping and wait formatting tests cover the unchanged selector behavior. [2]
- The selector under test caches and filters attention rows. [3]

### Cross-Repo References

No meaningful cross-repo references found.

No meaningful cross-repo references found.
