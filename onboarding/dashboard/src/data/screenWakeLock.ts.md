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

The `acquiring` guard coalesces overlapping requests so only one sentinel is owned. An unsupported API
returns a silent no-op stop function before installing listeners. A rejected request logs at most one
informational note per started lifecycle and records no held sentinel; later visible-state events may
retry. Neither branch promises that a wake lock is held.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory worktree's source registry.

No relevant external documentation is configured.

### Repo-Internal References

- Visibility, release, and overlapping-acquire handling. [1]

- Cockpit startup owns the returned lifecycle. Anchor: `startScreenWakeLock` [2]


### Cross-Repo References

No meaningful cross-repository references found.

- The optional browser API is wrapped locally. [3]
