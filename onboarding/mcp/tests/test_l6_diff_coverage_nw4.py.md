# mcp/tests/test_l6_diff_coverage_nw4.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_nw4.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout diff-coverage tests for batch NW4. Each test exercises one changed line or untaken branch edge from `/tmp/l6-cov-NW4.json` without modifying production code: claim-change-router parsing, unclaimed-entity ranking, application-boundary checks, abandon terminal outputs, orchestration nudges, gate payload adapters, and leaf-doc asserted reads.

## Code Commentary

- `TestClaimChangeRouterNw4` covers working-status and historical-diff parsing plus HEAD-tree failure.
- `TestUnclaimedEntitiesNw4` covers priority authority/schema and call-name fallbacks.
- `TestApplicationBoundaryNw4` covers empty relative-import bases and permitted unknown packages.
- `TestAbandonTerminalOutputsNw4` covers provider/worktree blocker ordering.
- `TestGatePayloadAdaptersNw4` covers registered lifecycle-gate and gate-decide payload adapters.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `TestClaimChangeRouterNw4` (lines 111-155). | `TestClaimChangeRouterNw4` | mcp/tests/test_l6_diff_coverage_nw4.py:111-155 |
| Defines the class `TestUnclaimedEntitiesNw4` (lines 158-174). | `TestUnclaimedEntitiesNw4` | mcp/tests/test_l6_diff_coverage_nw4.py:158-174 |
| Defines the class `TestApplicationBoundaryNw4` (lines 177-191). | `TestApplicationBoundaryNw4` | mcp/tests/test_l6_diff_coverage_nw4.py:177-191 |
| Defines the class `TestAbandonTerminalOutputsNw4` (lines 194-227). | `TestAbandonTerminalOutputsNw4` | mcp/tests/test_l6_diff_coverage_nw4.py:194-227 |
| Defines the class `TestGatePayloadAdaptersNw4` (lines 261-306). | `TestGatePayloadAdaptersNw4` | mcp/tests/test_l6_diff_coverage_nw4.py:261-306 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
