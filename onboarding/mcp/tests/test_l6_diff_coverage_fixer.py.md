# mcp/tests/test_l6_diff_coverage_fixer.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_fixer.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout coverage tests for citation fixer refusal branches: scoped source refusals, citation refusals, and repair/scoped decline paths.

## Code Commentary

- `TestDecideRefused` covers the scoped source refusal decision.
- `TestScopedSourceRefusal` covers citation refusal for out-of-scope sources.
- `TestScopedCitationRefusals` covers repair-decline and scoped-decline branches.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `TestDecideRefused` (lines 45-58). | `TestDecideRefused` | mcp/tests/test_l6_diff_coverage_fixer.py:45-58 |
| Defines the class `TestScopedSourceRefusal` (lines 61-76). | `TestScopedSourceRefusal` | mcp/tests/test_l6_diff_coverage_fixer.py:61-76 |
| Defines the class `TestScopedCitationRefusals` (lines 79-118). | `TestScopedCitationRefusals` | mcp/tests/test_l6_diff_coverage_fixer.py:79-118 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
