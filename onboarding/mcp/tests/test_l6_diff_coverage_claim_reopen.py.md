# mcp/tests/test_l6_diff_coverage_claim_reopen.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_claim_reopen.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `a3e43cb0877c18b9d2b0e6ada4eb5719a01f251f` |
| lastVerifiedCommitDate | 2026-08-06T05:49:07+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout coverage tests for claim-reopen evaluation branches: source-view candidates, anchor change detection, and dependency-change evaluation.

## Code Commentary

- `FakeViews` is the candidate-view double used by the source-view tests.
- `TestSourceViewsCandidates` covers none-lines and cache behavior.
- `TestAnchorChange` covers the three-way split (260731-EFA-L16): empty and non-unique anchors,
  a missing current resolution (enforced), a changed construct whose citation is current
  (report-only surface), and a changed construct with a stale range (enforced).
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

- 2026-08-05T23:20+02:00 — 260731-EFA-L16 curator: recorded the two closeout flow tests — a changed construct completes with the stamp advanced to the new code commit, and a deleted construct refuses in the citation gate BEFORE the code commit with `citation_anchor_absent_from_range` (no commit spent) — plus the phase-payload contract (citation pair before, sanity checks after). Verification metadata stays pinned until closeout stamps the L16 commit.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
