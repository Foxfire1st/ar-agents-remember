# dashboard/src/data/conversation/stream.test.ts

## Governing Overview

[data/conversation overview](overview.md)

## Purpose

Regression coverage for conversation-stream boot retry, half-open liveness recovery, and honest
never-open escalation.

## Code Commentary

### Logic

`ControlledSource` simulates EventSource lifecycle events. Tests distinguish the fast pre-first-open
retry from established reconnects, verify resume cursors across quiet sleep/wake cycles, constrain idle
backstop cycles to one episode, and require an open deadline to signal a genuinely never-open stream.

### Conventions

Fake timers model suspended wall-clock time without inventing browser transport events.

### Invariants And Boundaries

A quiet recovery must not flash a disconnect, but a replacement subscribe that never opens must not retain
a live-looking state.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory worktree's source registry.

No relevant external documentation is configured.

### Repo-Internal References

- Stream lifecycle and watchdog behavior are covered with controlled sources. [1]
- The production EventSource controller consumes these callbacks. [2]
- The `openWatched` harness supplies the watchdog replay cursor. [3]
- The replay cursor is minted by the `eventCursor` brand constructor. [4]
- The first watchdog replay assertion requires the resumed URL to contain `after=evt-7`. [5]
- The established reconnect assertion requires the resumed URL to contain `after=evt-7`. [6]
- The watchdog backstop assertion requires the resumed URL to contain `after=evt-7`. [7]
- The visibility-recovery assertion requires the resumed URL to contain `after=evt-7`. [8]

### Cross-Repo References

No meaningful cross-repository references found.
