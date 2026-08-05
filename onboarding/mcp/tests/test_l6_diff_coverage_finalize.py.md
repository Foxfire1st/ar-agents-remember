# mcp/tests/test_l6_diff_coverage_finalize.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_finalize.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout coverage tests for task finalization helpers: task-target resolution, parent-target resolution, asserted reads, and reconcile/candidate logic.

## Code Commentary

- `TestResolveTaskTargets` covers series and leaf target resolution with and without task documents.
- `TestResolveParentTarget` covers parent-argument and standalone/leaf-with-master resolution.
- `TestAssertAndRead` covers parent-argument assertion, parent reads, and parent-row checks.
- `TestReconcileAndCandidates` covers reconcile skip/missing/write paths and candidate enumeration.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `TestResolveTaskTargets` (lines 68-105). | `TestResolveTaskTargets` | mcp/tests/test_l6_diff_coverage_finalize.py:68-105 |
| Defines the class `TestResolveParentTarget` (lines 108-151). | `TestResolveParentTarget` | mcp/tests/test_l6_diff_coverage_finalize.py:108-151 |
| Defines the class `TestAssertAndRead` (lines 154-208). | `TestAssertAndRead` | mcp/tests/test_l6_diff_coverage_finalize.py:154-208 |
| Defines the class `TestReconcileAndCandidates` (lines 211-261). | `TestReconcileAndCandidates` | mcp/tests/test_l6_diff_coverage_finalize.py:211-261 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
