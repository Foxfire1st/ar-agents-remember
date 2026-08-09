# mcp/tests/test_l6_diff_coverage_small_tools.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_small_tools.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-09T06:48+02:00 |
| lastVerifiedCommitHash | `cdca11264fb4d27ee08f5e8b37ac5496e67c0840` |
| lastVerifiedCommitDate | 2026-08-09T07:36:31+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout coverage tests for small application/serving tool branches: step-skip logic, lifecycle blocking, operator-inbox posts and consume, nudge-manager composition, and leaf-ref refusals.

## Code Commentary

- `TestSkipStep` covers master rejection, missing-step/blank-reason, and done-target/success branches.
- `TestOperatorInboxPostsAndDispatch` covers redelivery floors, disabled delivery, and expectation SLA dispatch.
- `TestOperatorInboxConsumeAck` covers the attribution-only consume (N16): it no longer marks
  any ack-by row met — no expectation store is touched.
- `TestNudgeManager` covers nudge-manager request composition.
- `TestLeafRefRefusal` covers leaf-ref payload kinds.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `TestSkipStep` (lines 45-66). | `TestSkipStep` | mcp/tests/test_l6_diff_coverage_small_tools.py:45-66 |
| Defines the class `TestOperatorInboxPostsAndDispatch` (lines 80-129). | `TestOperatorInboxPostsAndDispatch` | mcp/tests/test_l6_diff_coverage_small_tools.py:80-129 |
| Defines the class `TestOperatorInboxConsumeAck` (lines 132-150). | `TestOperatorInboxConsumeAck` | mcp/tests/test_l6_diff_coverage_small_tools.py:132-150 |
| Defines the class `TestNudgeManager` (lines 153-175). | `TestNudgeManager` | mcp/tests/test_l6_diff_coverage_small_tools.py:149-171 |
| Defines the class `TestLeafRefRefusal` (lines 178-189). | `TestLeafRefRefusal` | mcp/tests/test_l6_diff_coverage_small_tools.py:174-185 |

## Update History

- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the attribution-only consume
  coverage update (N16 — consume touches no expectation machinery). Verification metadata
  pinned until closeout stamps the 260713-TES-L4 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round 2 (curator): No content impact: the supervisor -> agent-notifier rename does not change the behavior this sidecar documents; reviewed current against the changed source. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
