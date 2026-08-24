# mcp/src/agents_remember/serving/projections/snapshots_impl/_closeout_queue.py

| Field                  | Value                                                                        |
| ---------------------- | ---------------------------------------------------------------------------- |
| repository             | agents-remember                                                              |
| path                   | `mcp/src/agents_remember/serving/projections/snapshots_impl/_closeout_queue.py` |
| doc_type               | `file-level-onboarding`                                                      |
| lastUpdated            | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview      | `../overview.md`                                                             |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Top-level reader covers every orchestrating sprint. | `read_closeout_queues` | `mcp/src/agents_remember/serving/projections/snapshots_impl/_closeout_queue.py` |
| Effective state is joined against the exact current source. | `_project_queue` | `mcp/src/agents_remember/serving/projections/snapshots_impl/_closeout_queue.py` |
| Waiting-generation members project classification, priority, order, and reasons. | `_candidate_node` | `mcp/src/agents_remember/serving/projections/snapshots_impl/_closeout_queue.py` |

## 260821-CLIVE Effective Projection Reader

The reader now emits one node for every orchestrating sprint, including graph-less
atomic-sequential sprints. It captures the current canonical source identity and asks
`CloseoutQueueStore.read_effective` for the disposable result. The dashboard receives service
condition, source classification/fingerprint/problems, and waiting-generation members with
classification, priority, order, and reasons. Missing, stale, malformed, or source-mismatched bytes
surface as invalid-empty; candidate lifecycle states, grades, blockers, commits, and certification
are not projected here.

This section supersedes the earlier authoritative-queue and active-blocker description.

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: rewrote the card for the effective disposable projection reader. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-18T00:00+02:00 — 260815-DAG-L8: created the read-only closeout-queue serving projection.
  Verification metadata pinned until closeout stamps the L8 commit.
