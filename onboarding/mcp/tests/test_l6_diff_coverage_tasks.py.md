# mcp/tests/test_l6_diff_coverage_tasks.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_tasks.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout coverage tests for task-document helpers: step disposition and master sync, write/rollback behavior, and terminal leaf resolution.

## Code Commentary

- `TestStepDispositionAndMasterSync` covers blank skip reasons and collapsed leaf step status.
- `TestWriteTaskDocs` covers write success and single/both-failed rollback.
- `TestTerminalLeafResolution` covers blank leaf ids, asserted-path validation, ambiguity, and unreadable candidates.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `TestStepDispositionAndMasterSync` (lines 42-64). | `TestStepDispositionAndMasterSync` | mcp/tests/test_l6_diff_coverage_tasks.py:42-64 |
| Defines the class `TestWriteTaskDocs` (lines 67-87). | `TestWriteTaskDocs` | mcp/tests/test_l6_diff_coverage_tasks.py:67-87 |
| Defines the class `TestTerminalLeafResolution` (lines 90-129). | `TestTerminalLeafResolution` | mcp/tests/test_l6_diff_coverage_tasks.py:90-129 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
