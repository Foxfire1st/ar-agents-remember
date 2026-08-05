# mcp/tests/test_l6_diff_coverage_provenance.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_provenance.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout coverage tests for citation provenance helpers: git history reads, requirement/package candidates, and locked-version history comparison.

## Code Commentary

- `TestGitHistory` covers commit success, rev-parse failure, unreachable commits, and file lookups.
- `TestRequirements` covers requirement candidates, versions, package locks, ecosystems, and manifest errors.
- `TestHistoriesVersions` covers locked-version history for python/npm and working-tree errors.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `TestGitHistory` (lines 55-86). | `TestGitHistory` | mcp/tests/test_l6_diff_coverage_provenance.py:55-86 |
| Defines the class `TestRequirements` (lines 89-160). | `TestRequirements` | mcp/tests/test_l6_diff_coverage_provenance.py:89-160 |
| Defines the class `TestHistoriesVersions` (lines 163-183). | `TestHistoriesVersions` | mcp/tests/test_l6_diff_coverage_provenance.py:163-183 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
