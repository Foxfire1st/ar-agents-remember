# mcp/src/agents_remember/observer/reducer.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Pure assembly of workspace task, worktree and analytical projections from supplied structural, task-source and host facts; no event-log session-state fold or inferred task-stage writer.

## Code Commentary

`project_workspace` enriches enclosures with exactly integrate/cleanup availability, builds Engine Room facts, then calls `build_task_entries` once with canonical task sources, worktrees and `HostActivitySnapshot`. It publishes tasks, taskCounts and unbound enclosures, providers, active worktree groups and closeout queues. Metrics contain the staleness histogram and ignored host-agent count.

Attention and analytics remain pure over supplied facts. Authored planned/aborted/completed stages are not overridden by activity; unavailable host facts are not proof of pause or completion. There is no `project_lifecycle`, correction fold, synthetic persistent lifecycle or stale-heartbeat abandonment. Enclosure action prerequisite/refusal distinctions and landing-operation ownership survive independently.

## Evidence boundary

This account is current source interpretation only. It creates no executed test/host/bootstrap result and supplies no new CODE or MEMORY grade.

## Evidence

- One task-source/host join supplies state/membership/counts; action and analytics assembly remain pure. [1]
