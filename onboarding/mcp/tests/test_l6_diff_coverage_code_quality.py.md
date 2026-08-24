# mcp/tests/test_l6_diff_coverage_code_quality.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_code_quality.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T21:23+02:00 |
| lastVerifiedCommitHash | `b99501852bcfa5f499a25e7183063751f6133a28` |
| lastVerifiedCommitDate | 2026-08-24T21:21:58+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout coverage tests for code-quality gate internals: application boundary checks, single-owner bindings, fixed-check rails, and scope-module branches.

## Code Commentary

L23 supplies the new progress and coverage-data seams to fixed-check test configurations so the legacy rail assertions exercise the current runner shape.

- `TestApplicationBoundary` covers contract reads, resolved imports, and required-module errors.
- `TestSingleOwner` covers import-origin and task-writer bindings.
- `TestCheckRails` covers fixed-check runners, coverage-report failure, CRAP-calculator branches, and config-from-args errors.
- `TestScopeModuleBranches` covers untracked files, pyright venv validation, quality-config validation, and dashboard build inputs.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `TestApplicationBoundary` (lines 75-143). | `TestApplicationBoundary` | mcp/tests/test_l6_diff_coverage_code_quality.py:75-143 |
| Defines the class `TestSingleOwner` (lines 146-171). | `TestSingleOwner` | mcp/tests/test_l6_diff_coverage_code_quality.py:146-171 |
| Defines the class `TestCheckRails` (lines 174-339). | `TestCheckRails` | mcp/tests/test_l6_diff_coverage_code_quality.py:174-339 |
| Defines the class `TestScopeModuleBranches` (lines 342-497). | `TestScopeModuleBranches` | mcp/tests/test_l6_diff_coverage_code_quality.py:342-497 |

## 260824-PDLS Admission Boundary

Argument-to-config forcing now supplies the already-validated Dagger admission capability.
Diff-coverage and wrapper failure semantics remain unchanged.

## Update History

- 2026-08-24T21:23+02:00 — Added the typed admission precondition.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
