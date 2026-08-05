# mcp/tests/test_l6_diff_coverage_abandon.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_abandon.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout coverage tests for the worktree abandon helpers: reserved-guard entry, guarded abandon flows, branch refusal and unmerged-commit checks, and external-memory branch handling.

## Code Commentary

- `TestAbandonReserved` covers guard-entry errors when the namespace is reserved.
- `TestAbandonWithGuard` covers helper failure, blocked mutation, dry-run, and publish paths.
- `TestAbandonBranch` covers branch refusals, branch-presence refusals, and unmerged commits.
- `TestAbandonBranches` covers external-memory branch handling.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `TestAbandonReserved` (lines 51-77). | `TestAbandonReserved` | mcp/tests/test_l6_diff_coverage_abandon.py:51-77 |
| Defines the class `TestAbandonWithGuard` (lines 80-140). | `TestAbandonWithGuard` | mcp/tests/test_l6_diff_coverage_abandon.py:80-140 |
| Defines the class `TestAbandonBranch` (lines 143-267). | `TestAbandonBranch` | mcp/tests/test_l6_diff_coverage_abandon.py:143-267 |
| Defines the class `TestAbandonBranches` (lines 270-277). | `TestAbandonBranches` | mcp/tests/test_l6_diff_coverage_abandon.py:270-277 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
