# mcp/src/agents_remember/observer/reducer.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Pure assembly of workspace task, worktree and analytical projections from supplied structural, task-source and host facts; no event-log session-state fold or inferred task-stage writer.

## Code Commentary

`project_workspace` enriches enclosures with exactly integrate/cleanup availability, builds Engine Room facts, then calls `build_task_entries` once with canonical task sources, worktrees and `HostActivitySnapshot`. It publishes tasks, taskCounts and unbound enclosures, active worktree groups and closeout queues. The former providers collection is absent. Metrics carry only the ignored host-agent count; task counts are published on `taskCounts` beside the tasks, and no staleness histogram is projected.

Attention and analytics remain pure over supplied facts: the queue is built once from the providers, the drift findings, the joined task entries, the native attention facts and the pass clock, and it appends no second interpretation of task state. Authored planned/aborted/completed stages are not overridden by activity; unavailable host facts are not proof of pause or completion. There is no `project_lifecycle`, correction fold, synthetic persistent lifecycle or stale-heartbeat abandonment. Enclosure action prerequisite/refusal distinctions and landing-operation ownership survive independently.

### Retained L56 converted-memory boundary

The facade keeps the one host-observation metric — `Metrics(ignoredHostAgents=...)`, whose model carries no other field — and the narrowed analytical bundle, including `closeout_queues`; lifecycle vocabulary counts, verification-age histograms and stalest-sidecar rollups remain removed, with task counts published on `taskCounts`. Optional `given` defaults to `AnalyticalInputs()`, but supplied structural facts can still populate derived attention or engine surfaces: empty input does not promise universally empty analytics. The incoming removal of gate, pickup and expectation assembly remains in force. [18]

## Evidence boundary

This account is current source interpretation only. It creates no executed test/host/bootstrap result and supplies no new CODE or MEMORY grade.

## Evidence


- Anchor: Current output projection shape. [1]


- The facade composes metrics and the narrowed analytical bundle, including closeout queue input, without verification-age rollups. Current counts are task-entry-owned; lifecycle-only counting describes the predecessor, not the current native task fold. [18]

- The current WorkspaceProjection constructor publishes native tasks/counts, unbound enclosures, active groups, queues, host metric and analytics, with no providers collection. [19]

## Historical provider collection

These former current claims are retained as history, not as instructions or present implementation evidence.

> It publishes tasks, taskCounts and unbound enclosures, providers, active worktree groups and closeout queues.
