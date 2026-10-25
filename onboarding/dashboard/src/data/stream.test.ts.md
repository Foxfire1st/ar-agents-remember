# dashboard/src/data/stream.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Verify state-stream sleep/wake recovery and the open-deadline honesty boundary.

## Code Commentary

### Logic

A controlled EventSource proves that an open channel quietly cycles after a sleep-sized clock jump,
hidden tabs are exempt from watchdog cycling, ordinary transport errors still signal loss, and a replacement
that neither opens nor errors is eventually marked signal-lost and retried.

### 260928-MIK-L114 Ready Last-Feed Cases

Two cases prove the ready-marker parsing the store hydration depends on: the marker's
last feed reaches the opener, and an unreadable marker still opens the gate.

### Conventions

Fake timers model the post-wake wall-clock discontinuity.

### Invariants And Boundaries

Quiet recovery avoids unnecessary visual churn; never opening is not quiet health and cannot retain live
connection state.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory worktree's source registry.

No relevant external documentation is configured.

### Repo-Internal References


- Controlled state-stream cases cover wake, hidden, error, and never-open paths. [1]


- Production state-stream transport owns the deadline. [2]


### Cross-Repo References

No meaningful cross-repository references found.


- The test covers dashboard-local state transport. [3]

The moved-notice cases drive ControlledSource through the named review.explainer.moved event: a matching mounted subscriber receives the exact payload, another leaf does not, and no-work and cleared notices reach the same subscriber without reopening the page. These are event-wiring assertions over a stubbed EventSource, not live transport latency measurements.

- The moved-notice cases drive ControlledSource through the named review.explainer.moved event: a matching mounted subscriber receives the exact payload, another leaf does not, and no-work and cleared notices reach the same subscriber without reopening the page. These are event-wiring assertions over a stubbed EventSource, not live transport latency measurements. [4]
