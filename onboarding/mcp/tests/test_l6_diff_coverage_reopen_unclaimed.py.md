# mcp/tests/test_l6_diff_coverage_reopen_unclaimed.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_reopen_unclaimed.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `aeca9a2839c965218a61a3040e15cb84367ebeca` |
| lastVerifiedCommitDate | 2026-08-14T13:35:55+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout coverage tests for reopen helpers and unclaimed-entity ranking: frozen-landing cleanup, reopen blockers, and unclaimed-entity declaration/rank reporting.

## Code Commentary

- `TestClearFrozenLanding` covers absent, dry-run/deleted, and failed-delete branches.
- `TestReopenBlockers` covers reopen blocker enumeration.
- `TestUnclaimedEntities` covers declaration signals, rank-key tiers, and rank reporting.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `TestClearFrozenLanding` (lines 19-42). | `TestClearFrozenLanding` | mcp/tests/test_l6_diff_coverage_reopen_unclaimed.py:19-42 |
| Defines the class `TestReopenBlockers` (lines 45-73). | `TestReopenBlockers` | mcp/tests/test_l6_diff_coverage_reopen_unclaimed.py:45-73 |
| Defines the class `TestUnclaimedEntities` (lines 76-125). | `TestUnclaimedEntities` | mcp/tests/test_l6_diff_coverage_reopen_unclaimed.py:76-125 |

## L23 Final Candidate Disposition

This regression keeps the unclaimed reopen path inside canonical task-reopen planning and verifies
that the Dagger changed-line contract still sees the reopened candidate without consuming approval.

## Update History
- 2026-08-14T06:38+02:00 — L23 final candidate review: the reopened unclaimed path remains covered
  under exact task-reopen planning and the Dagger-only changed-line contract. Verification remains
  closeout-owned.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
