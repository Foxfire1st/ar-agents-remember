# mcp/tests/test_l6_diff_coverage_crap.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_crap.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T11:32+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout coverage tests for CRAP offenders and the new CLI split helpers. They cover the branch surface of `scope_reporting.main` and `scope.eslint_result_files` so the strict quality gate's CRAP rail and changed-line floor can pass for this wave.

## Code Commentary

- `TestScopeReportingMain` covers generated, dashboard, randomized, untracked, hook-tier, and fixed-step command generation plus the error path.
- `TestEslintResultFiles` covers missing executables, failure branches, and valid ESLint results.
- `TestScopeReportingCoverage` covers scope-line derivation, push-update parsing, invocation descriptions, tsconfig inputs, and dashboard scope lines. Its TypeScript cases include directory-form project references and prove that nested inputs resolve relative to the referenced project's own `tsconfig.json`.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `TestScopeReportingMain` (lines 91-138). | `TestScopeReportingMain` | mcp/tests/test_l6_diff_coverage_crap.py:91-138 |
| Defines the class `TestEslintResultFiles` (lines 141-177). | `TestEslintResultFiles` | mcp/tests/test_l6_diff_coverage_crap.py:141-177 |
| Defines the class `TestScopeReportingCoverage` (lines 180-459). | `TestScopeReportingCoverage` | mcp/tests/test_l6_diff_coverage_crap.py:180-459 |

## PDLS Wave 005 Current Delta

The synthetic repository now declares product and verification package roots explicitly. This
keeps CRAP and diff-coverage scope evidence bound to the same no-silent-classification contract as
real repositories; an absent or ambiguous package role cannot be inferred as unit/product scope.

## Update History

- 2026-08-28T11:32+02:00 — Added nested directory-form TypeScript project-reference forcing with
  project-local input resolution.

- 2026-08-28T06:40+02:00 — Added explicit product/verification package ownership to the CRAP
  fixture and moved its verification helpers into `agents_remember_test_support`.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
