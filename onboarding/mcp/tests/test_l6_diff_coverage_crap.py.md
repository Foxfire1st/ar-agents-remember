# mcp/tests/test_l6_diff_coverage_crap.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_crap.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout coverage tests for CRAP offenders and the new CLI split helpers. They cover the branch surface of `scope_reporting.main` and `scope.eslint_result_files` so the strict quality gate's CRAP rail and changed-line floor can pass for this wave.

## Code Commentary

- `TestScopeReportingMain` covers generated, dashboard, randomized, untracked, hook-tier, and fixed-step command generation plus the error path.
- `TestEslintResultFiles` covers missing executables, failure branches, and valid ESLint results.
- `TestScopeReportingCoverage` covers scope-line derivation, push-update parsing, invocation descriptions, tsconfig inputs, and dashboard scope lines.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `TestScopeReportingMain` (lines 91-138). | `TestScopeReportingMain` | mcp/tests/test_l6_diff_coverage_crap.py:91-138 |
| Defines the class `TestEslintResultFiles` (lines 141-177). | `TestEslintResultFiles` | mcp/tests/test_l6_diff_coverage_crap.py:141-177 |
| Defines the class `TestScopeReportingCoverage` (lines 180-459). | `TestScopeReportingCoverage` | mcp/tests/test_l6_diff_coverage_crap.py:180-459 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
