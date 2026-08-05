# mcp/tests/test_l6_diff_coverage_claim_reopen.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_claim_reopen.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout coverage tests for claim-reopen evaluation branches: source-view candidates, anchor change detection, and dependency-change evaluation.

## Code Commentary

- `FakeViews` is the candidate-view double used by the source-view tests.
- `TestSourceViewsCandidates` covers none-lines and cache behavior.
- `TestAnchorChange` covers empty, non-unique, missing, and changed anchor scenarios.
- `TestDependencyChanges` covers unsupported ecosystems and dependency-version branches.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the fake view helper `FakeViews` (lines 49-55). | `FakeViews` | mcp/tests/test_l6_diff_coverage_claim_reopen.py:49-55 |
| Defines the class `TestSourceViewsCandidates` (lines 58-68). | `TestSourceViewsCandidates` | mcp/tests/test_l6_diff_coverage_claim_reopen.py:58-68 |
| Defines the class `TestAnchorChange` (lines 71-126). | `TestAnchorChange` | mcp/tests/test_l6_diff_coverage_claim_reopen.py:71-126 |
| Defines the class `TestDependencyChanges` (lines 129-169). | `TestDependencyChanges` | mcp/tests/test_l6_diff_coverage_claim_reopen.py:129-169 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
