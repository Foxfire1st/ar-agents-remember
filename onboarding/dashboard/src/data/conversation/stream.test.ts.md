# dashboard/src/data/conversation/stream.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/conversation/stream.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:50Z |
| lastVerifiedCommitHash |  `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate |  2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation entries are configured in this memory worktree's source registry.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is configured. | Source discovery checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Stream lifecycle and watchdog behavior are covered with controlled sources. | L11-L335 | [stream.test.ts](stream.test.ts) |
| The production EventSource controller consumes these callbacks. | L1-L240 | [stream.ts](stream.ts) |

## Cross-Repo References

No meaningful cross-repository references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The tests exercise this repository's conversation transport. | L1-L335 | [stream.test.ts](stream.test.ts) |

## Update History

- 2026-07-24T13:17:50Z — Created for boot-aware reconnect and half-open stream regression coverage.
  Verification hash/date remain pinned to the pre-commit source stamp.
