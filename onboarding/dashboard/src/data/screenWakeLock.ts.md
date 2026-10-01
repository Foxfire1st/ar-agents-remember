# dashboard/src/data/screenWakeLock.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Keep the monitoring cockpit's screen awake while its document is visible, without pinning a backgrounded
tab or creating an operator alarm for an unavailable platform API.

## Code Commentary

### Logic

`startScreenWakeLock` requests a screen sentinel when visible, reacquires after a UA release or visible
return, and returns a stop function that removes the listener and releases its owned sentinel.

### Conventions

The narrow local `WakeLockLike` shapes avoid making optional platform APIs global dashboard state.

### Invariants And Boundaries

The `acquiring` guard coalesces overlapping requests so only one sentinel is owned. Unsupported or denied
APIs log one informational note and remain a no-op; the feature never implies that a wake lock is held.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory worktree's source registry.

No relevant external documentation is configured.

### Repo-Internal References

- Visibility, release, and overlapping-acquire handling. [1]
- Cockpit startup owns the returned lifecycle. [2]

### Cross-Repo References

No meaningful cross-repository references found.

- The optional browser API is wrapped locally. [3]
