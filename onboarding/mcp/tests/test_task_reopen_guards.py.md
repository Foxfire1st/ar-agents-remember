# mcp/tests/test_task_reopen_guards.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_reopen_guards.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T10:24+02:00 |
| lastVerifiedCommitHash | `17987fa66a642306eb8d20fa9a4bff2b881550d2` |
| lastVerifiedCommitDate | 2026-08-15T14:36:30+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Holds the bounded refusal-only reopen cases split from `test_task_reopen.py` so both suites remain
below the repository file-size limit while preserving direct production-path coverage.

## Code Commentary

### Logic

The suite reuses the canonical landed-leaf and task-document fixtures. It refuses incomplete
closeout/cleanup, non-leaf contracts, surviving worktrees, and stale transitive source lineage;
the last case also proves the contract and leaf task document remain byte-identical.

### Invariants And Boundaries

- Every test calls the real `reopen_task` owner.
- The split changes only test location; blocker assertions and mutation checks are preserved.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Incomplete, non-leaf, and surviving-worktree contracts refuse reopen. | `ReopenGuardTests` | mcp/tests/test_task_reopen_guards.py:15-44 |
| Moved super ancestry refuses before contract or task-document mutation. | `test_moved_super_refuses_before_reopen_mutates_task_state` | mcp/tests/test_task_reopen_guards.py:46-67 |

## Update History

- 2026-08-15T10:24+02:00 — Created by the L3 file-size repair from `ReopenGuardTests`; behavior,
  fixtures, and assertions are unchanged.
