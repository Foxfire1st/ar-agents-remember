# dashboard/src/data/selectors.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Vitest source assertions for pure store selectors: physical-worktree existence, wait-time formatting, server-queue display suppression and converted drift segment ordering. Lifecycle buildTree grouping tests are removed.

## Code Commentary

### Logic

hasLiveWorktree pins either-side physical existence; fmtWait retains s/m/h/d and unknown dash. selectQueue consumes served rows, stable empty analytics and optimistic suppression of dismissible rows only; both
cases here build dismissible operational rows, so this suite does not itself pin the non-dismissible case — that
assertion lives in `AttentionQueue.test.tsx`. Drift segments retain converted ordering/shares with legacy names first. Removed buildTree lifecycle grouping is not coverage.

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

- `selectQueue` coverage includes absent analytics and optimistic suppression. [1]
- Pure selector assertions make hasLiveWorktree depend only on stat-derived flags: either existing code/memory worktree admits and neither hides, never a cleanup-state proxy. fmtWait asserts seconds/minutes/hours/days formatting and an em dash for unknown input; this file has no lifecycle buildTree grouping case. [2]
- The selector under test caches and filters attention rows. [3]



### Cross-Repo References

No meaningful cross-repo references found.

No meaningful cross-repo references found.

- Converted drift segments order current, stale and violation with exact shares. [4]
