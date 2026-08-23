# mcp/tests/test_l6_diff_coverage_small_tools.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_small_tools.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T00:51+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
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

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `TestSkipStep` (lines 45-66). | `TestSkipStep` | mcp/tests/test_l6_diff_coverage_small_tools.py:45-66 |
| Defines the class `TestOperatorInboxPostsAndDispatch` (lines 80-129). | `TestOperatorInboxPostsAndDispatch` | mcp/tests/test_l6_diff_coverage_small_tools.py:80-129 |
| Defines the class `TestOperatorInboxConsumeAck` (lines 132-150). | `TestOperatorInboxConsumeAck` | mcp/tests/test_l6_diff_coverage_small_tools.py:132-150 |
| Defines the class `TestNudgeManager` (lines 153-175). | `TestNudgeManager` | mcp/tests/test_l6_diff_coverage_small_tools.py:149-171 |

## Update History

- 2026-08-24T00:51+02:00 — No content impact: 260821-CLIVE-L2 the test only repoints lifecycle tools to their moved application lifecycle package. Verified at code commit `1d446724`.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-11T19:58+02:00 — Aligned the regression card for `test_l6_diff_coverage_small_tools.py` with the source's current task-document, seat-routing, inbox, or lifecycle assertions.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
