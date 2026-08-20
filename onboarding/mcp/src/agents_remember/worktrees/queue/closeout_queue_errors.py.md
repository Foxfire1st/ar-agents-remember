# mcp/src/agents_remember/worktrees/queue/closeout_queue_errors.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_queue_errors.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Defines the shared typed fail-closed error crossing the queue application, evidence, store-facing,
and lifecycle services, plus the shared request-reference validator.

## Code Commentary

### Logic

`CloseoutQueueError` retains a machine-readable status while the base exception carries the status
and human detail together, preserving the mechanistic refusal in detached worker diagnostics.
`queue_task_ref` (extracted from `closeout_queue.py` in 260815-DAG-L13) validates one
request-carried task-document reference, failing closed with `closeout-queue-reference-required` /
`closeout-queue-reference-invalid`.

### Conventions

Queue refusal sites use stable status strings rather than exposing internal exception classes.

### Invariants And Boundaries

- Every refusal has both a status and a detail.
- This module contains no recovery or policy logic beyond reference validation.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The shared queue error stores the exact public status and detail. | `CloseoutQueueError` | mcp/src/agents_remember/worktrees/queue/closeout_queue_errors.py:13-18 |
| Request-carried task references validate fail-closed in one place. | `queue_task_ref` | mcp/src/agents_remember/worktrees/queue/closeout_queue_errors.py:21-34 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/queue/closeout_queue_errors.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13: added `queue_task_ref`, the shared request-reference
  validator extracted from `closeout_queue.py` so the queue service and the extracted blocker
  module validate refs identically. Verification remains closeout-owned.

- 2026-08-15T11:07+02:00 — L3 Dagger repair: included the stable status in exception text while
  retaining the typed `status` field, so lifecycle failure records do not erase the refusal class.
- 2026-08-15T09:10+02:00 — Created for L3's typed queue refusal boundary; verification remains closeout-owned.