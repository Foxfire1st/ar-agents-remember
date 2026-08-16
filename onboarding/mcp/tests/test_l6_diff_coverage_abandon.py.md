# mcp/tests/test_l6_diff_coverage_abandon.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_abandon.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a` |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout coverage tests for the worktree abandon helpers: reserved-guard entry, guarded
abandon flows, contract-authorized branch refusal and unmerged-commit checks, and external-memory
branch handling.

## Code Commentary

- `TestAbandonReserved` covers guard-entry errors when the namespace is reserved.
- `TestAbandonWithGuard` covers helper failure, blocked mutation, dry-run, and publish paths.
- `_abandon_authority` creates a real Git repository and contract-derived abandon capability so
  helper calls retain the production terminal-ownership boundary.
- `TestAbandonBranch` covers branch refusals, branch-presence refusals, and unmerged commits while
  passing that real capability to the target-bound helper.
- `TestAbandonBranches` covers the current code-and-memory branch set; it does not preserve the
  retired synthesized replay-integration branch.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Builds a real contract-derived terminal authority for helper tests. | `_abandon_authority` | mcp/tests/test_l6_diff_coverage_abandon.py:58-85 |
| Defines the class `TestAbandonReserved`. | `TestAbandonReserved` | mcp/tests/test_l6_diff_coverage_abandon.py:88-114 |
| Defines the class `TestAbandonWithGuard`. | `TestAbandonWithGuard` | mcp/tests/test_l6_diff_coverage_abandon.py:117-177 |
| Defines the class `TestAbandonBranch`. | `TestAbandonBranch` | mcp/tests/test_l6_diff_coverage_abandon.py:180-304 |
| Defines the class `TestAbandonBranches`. | `TestAbandonBranches` | mcp/tests/test_l6_diff_coverage_abandon.py:329-336 |

## Update History

- 2026-08-16T00:10+02:00 — 260815-DAG-L4 targeted-gate repair: migrated stale
  `_abandon_branch` and `_abandon_branches` calls to the target object plus real
  contract-derived terminal authority, and removed the retired memory-integration branch
  expectation. Verification metadata remains closeout-owned.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
