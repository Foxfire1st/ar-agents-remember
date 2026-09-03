# mcp/tests/test_l6_diff_coverage_fixer.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_fixer.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T01:15+02:00 |
| lastVerifiedCommitHash | `709dd07671b07d85ac49eaf3b77f4609b1e5fc5f` |
| lastVerifiedCommitDate | 2026-09-04T00:53:17+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout coverage tests for citation fixer refusal branches: scoped source refusals, citation
refusals, and repair/scoped decline paths. Since CCR-R10 (260831-CCR-L10) the
`TestDecideRefused` seam drives `_decide` through the new `fixer.Staging`
argument (the `edits` dict parameter was replaced by a `Staging` object), keeping the
refusal-branch coverage current with the staging seam.

## Code Commentary

- `TestDecideRefused` (`test_l6_diff_coverage_fixer.py:45-58) covers the scoped source
  refusal decision through `_decide` with a `fixer.Staging()` and an explicit
  onboarding root (signature updated for CCR-R10).
- `TestScopedSourceRefusal` (`test_l6_diff_coverage_fixer.py:61-76) covers citation
  refusal for out-of-scope sources.
- `TestScopedCitationRefusals` (`test_l6_diff_coverage_fixer.py:79-118) covers
  repair-decline and scoped-decline branches.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `TestDecideRefused` (lines 45-58) - the `_decide` refusal seam driven with `fixer.Staging()` and an explicit onboarding root (CCR-R10 signature). | `TestDecideRefused` | mcp/tests/test_l6_diff_coverage_fixer.py:45-58 |
| Defines the class `TestScopedSourceRefusal` (lines 61-76). | `TestScopedSourceRefusal` | mcp/tests/test_l6_diff_coverage_fixer.py:61-76 |
| Defines the class `TestScopedCitationRefusals` (lines 79-118). | `TestScopedCitationRefusals` | mcp/tests/test_l6_diff_coverage_fixer.py:79-118 |

## Update History

- 2026-09-04T01:15+02:00 - 260831-CCR-L10 Gate-5 memory pass: refreshed for the CCR-R10
  deterministic anchor-range projection change-set (code commit 709dd076). `TestDecideRefused`
  now calls `_decide` with `fixer.Staging()` plus an explicit onboarding root instead
  of the removed `edits` dict parameter, matching the new fixer signature; body updated and
  verification metadata pinned to 709dd076.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
