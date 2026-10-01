# mcp/src/agents_remember/serving/projections/snapshots_impl/_closeout_queue.py

## Governing Overview

[../overview.md](../overview.md)

## Purpose

Read-only serving reader that exposes each orchestrating sprint's effective disposable closeout
projection to the dashboard.

## Code Commentary

### Logic

`read_closeout_queues(coordination_root, now)` keeps every valid orchestrating master, including a
graph-less atomic-sequential sprint. `_project_queue` captures the exact current source identity and
uses `CloseoutQueueStore.read_effective`; it maps service condition, source
classification/fingerprint/problems, and waiting-generation members into observer nodes.

### Invariants And Boundaries

- Strictly read-only: it never mutates projections, contracts, doors, or task documents.
- Missing, invalid, unreadable, stale, or source-mismatched projection bytes surface as invalid-empty.
- It exposes no claim, blocker, grade mutation, commit, certification, integration, or lifecycle state.

## Evidence

### Repo-Internal References

- Top-level reader covers every orchestrating sprint. [1]
- Effective state is joined against the exact current source. [2]
- Waiting-generation members project classification, priority, order, and reasons. [3]

## 260821-CLIVE Effective Projection Reader

The reader now emits one node for every orchestrating sprint, including graph-less
atomic-sequential sprints. It captures the current canonical source identity and asks
`CloseoutQueueStore.read_effective` for the disposable result. The dashboard receives service
condition, source classification/fingerprint/problems, and waiting-generation members with
classification, priority, order, and reasons. Missing, stale, malformed, or source-mismatched bytes
surface as invalid-empty; candidate lifecycle states, grades, blockers, commits, and certification
are not projected here.

This section supersedes the earlier authoritative-queue and active-blocker description.
