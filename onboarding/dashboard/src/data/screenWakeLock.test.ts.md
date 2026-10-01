# dashboard/src/data/screenWakeLock.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Verify visible-tab wake-lock acquisition, release, reacquisition, graceful API absence, and overlapping
request coalescing.

## Code Commentary

### Logic

Fake documents, navigators, and sentinels expose visibility events and deferred `request` resolution.
The overlap case proves only one held sentinel exists and that `stop()` releases every issued sentinel.

### Conventions

The suite injects the DOM and Navigator dependencies rather than mutating browser globals.

### Invariants And Boundaries

No test treats unsupported or denied wake lock as an application failure.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory worktree's source registry.

No relevant external documentation is configured.

### Repo-Internal References

- Deferred sentinel tests cover acquisition coalescing and release. [1]
- The production owner holds one sentinel at a time. [2]

### Cross-Repo References

No meaningful cross-repository references found.

- This is local browser-API test coverage. [3]
