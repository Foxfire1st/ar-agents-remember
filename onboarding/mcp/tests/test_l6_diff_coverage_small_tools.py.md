# mcp/tests/test_l6_diff_coverage_small_tools.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_small_tools.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout coverage tests for small application/serving tool branches: step-skip logic, lifecycle blocking, operator-inbox posts and consume, nudge-manager composition, and leaf-ref refusals.

## Code Commentary

- `TestSkipStep` covers master rejection, missing-step/blank-reason, and done-target/success branches.
- `TestOperatorInboxPostsAndDispatch` covers redelivery floors, disabled delivery, and expectation SLA dispatch.
- `TestOperatorInboxConsumeAck` covers consume marking ack met.
- `TestNudgeManager` covers nudge-manager request composition.
- `TestLeafRefRefusal` covers leaf-ref payload kinds.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `TestSkipStep` (lines 45-66). | `TestSkipStep` | mcp/tests/test_l6_diff_coverage_small_tools.py:45-66 |
| Defines the class `TestOperatorInboxPostsAndDispatch` (lines 80-129). | `TestOperatorInboxPostsAndDispatch` | mcp/tests/test_l6_diff_coverage_small_tools.py:80-129 |
| Defines the class `TestOperatorInboxConsumeAck` (lines 132-150). | `TestOperatorInboxConsumeAck` | mcp/tests/test_l6_diff_coverage_small_tools.py:132-150 |
| Defines the class `TestNudgeManager` (lines 153-175). | `TestNudgeManager` | mcp/tests/test_l6_diff_coverage_small_tools.py:153-175 |
| Defines the class `TestLeafRefRefusal` (lines 178-189). | `TestLeafRefRefusal` | mcp/tests/test_l6_diff_coverage_small_tools.py:178-189 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
