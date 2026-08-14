# mcp/tests/test_l6_diff_coverage_claim_router.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_claim_router.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout coverage tests for the claim-change router: git status parsing, claim classification and partitioning, repository-change routing, and proven/unchanged versus semantic-required routing.

## Code Commentary

- `RepoPair` provisions a real code/memory repository pair for the router tests.
- `TestNulAndStatusParsers` covers NUL-field and status path parsing.
- `TestClassifyAndPartition` covers resolved-code-and-memory classification and citation partitioning.
- `TestRepositoryChanges` covers route states and git failure paths.
- `TestClaimChangeRouterRoutes` covers the proven-unchanged, memory-mapping-missing, and ambiguous-classification routes.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `RepoPair` (lines 42-72). | `RepoPair` | mcp/tests/test_l6_diff_coverage_claim_router.py:42-72 |
| Defines the class `TestNulAndStatusParsers` (lines 79-101). | `TestNulAndStatusParsers` | mcp/tests/test_l6_diff_coverage_claim_router.py:79-101 |
| Defines the class `TestClassifyAndPartition` (lines 104-140). | `TestClassifyAndPartition` | mcp/tests/test_l6_diff_coverage_claim_router.py:104-140 |
| Defines the class `TestRepositoryChanges` (lines 143-185). | `TestRepositoryChanges` | mcp/tests/test_l6_diff_coverage_claim_router.py:143-185 |
| Defines the class `TestClaimChangeRouterRoutes` (lines 188-228). | `TestClaimChangeRouterRoutes` | mcp/tests/test_l6_diff_coverage_claim_router.py:188-228 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
