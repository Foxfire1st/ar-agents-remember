# mcp/tests/test_l6_diff_coverage_nw3.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_nw3.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout diff-coverage tests for worker batch NW3. Each test targets one line or branch edge listed in `/tmp/l6-cov-NW3.json` for gate-tool helpers, claim-reopen evaluation, citation grammars, worktree cleanup, single-owner task-writer bindings, dispatch expectations, and citation tree resolution.

## Code Commentary

- `TestGateToolBranches` covers deciding-actor resolution, gate creation, lifecycle-gate blocking, and gate-decision records.
- `TestClaimReopenEvaluationBranches` covers memory-commit cache use, source-classify errors, and local-source evaluation errors.
- `TestCitationGrammarBranches` covers anchor-identifier signature and declaration branches.
- `TestCleanupBranches` covers origin-refusal queries and terminal-output drift blockers.
- `TestResolutionBranches` covers operation-tree resolution without cache authority.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `TestGateToolBranches` (lines 115-235). | `TestGateToolBranches` | mcp/tests/test_l6_diff_coverage_nw3.py:115-235 |
| Defines the class `TestClaimReopenEvaluationBranches` (lines 238-290). | `TestClaimReopenEvaluationBranches` | mcp/tests/test_l6_diff_coverage_nw3.py:238-290 |
| Defines the class `TestCitationGrammarBranches` (lines 322-369). | `TestCitationGrammarBranches` | mcp/tests/test_l6_diff_coverage_nw3.py:322-369 |
| Defines the class `TestCleanupBranches` (lines 372-405). | `TestCleanupBranches` | mcp/tests/test_l6_diff_coverage_nw3.py:372-405 |
| Defines the class `TestResolutionBranches` (lines 443-448). | `TestResolutionBranches` | mcp/tests/test_l6_diff_coverage_nw3.py:443-448 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
