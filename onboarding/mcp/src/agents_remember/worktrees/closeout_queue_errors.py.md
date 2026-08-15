# mcp/src/agents_remember/worktrees/closeout_queue_errors.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/closeout_queue_errors.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T11:07+02:00 |
| lastVerifiedCommitHash | `17987fa66a642306eb8d20fa9a4bff2b881550d2` |
| lastVerifiedCommitDate | 2026-08-15T14:36:30+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Defines the shared typed fail-closed error crossing the queue application, evidence, store-facing,
and lifecycle services.

## Code Commentary

### Logic

`CloseoutQueueError` retains a machine-readable status while the base exception carries the status
and human detail together, preserving the mechanistic refusal in detached worker diagnostics.

### Conventions

Queue refusal sites use stable status strings rather than exposing internal exception classes.

### Invariants And Boundaries

- Every refusal has both a status and a detail.
- This module contains no recovery or policy logic.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The shared queue error stores the exact public status and detail. | `CloseoutQueueError` | mcp/src/agents_remember/worktrees/closeout_queue_errors.py:1-11 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-08-15T11:07+02:00 — L3 Dagger repair: included the stable status in exception text while
  retaining the typed `status` field, so lifecycle failure records do not erase the refusal class.
- 2026-08-15T09:10+02:00 — Created for L3's typed queue refusal boundary; verification remains closeout-owned.
