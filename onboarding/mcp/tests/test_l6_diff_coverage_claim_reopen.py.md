# mcp/tests/test_l6_diff_coverage_claim_reopen.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_claim_reopen.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-07T14:30+02:00 |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f` |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
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
- `TestLocalChangesNewFile` covers the round-9 whole-new-file rule (260731-EFA-L8): a source
  absent at the stamp surfaces report-only when its anchor resolves exactly once inside a cited
  range, is enforced when the resolution lands outside the range or the source is absent from the
  working tree, and is invalid when the anchor resolves more than once now.
- `TestDependencyChanges` covers unsupported ecosystems and dependency-version branches.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the fake view helper `FakeViews` (lines 50-58). | `FakeViews` | mcp/tests/test_l6_diff_coverage_claim_reopen.py:50-58 |
| Defines the class `TestSourceViewsCandidates` (lines 59-71). | `TestSourceViewsCandidates` | mcp/tests/test_l6_diff_coverage_claim_reopen.py:59-71 |
| Defines the class `TestAnchorChange` (lines 72-142). | `TestAnchorChange` | mcp/tests/test_l6_diff_coverage_claim_reopen.py:72-142 |
| Defines the class `TestLocalChangesNewFile` (lines 143-186). | `TestLocalChangesNewFile` | mcp/tests/test_l6_diff_coverage_claim_reopen.py:143-186 |
| Defines the class `TestDependencyChanges` (lines 187-227). | `TestDependencyChanges` | mcp/tests/test_l6_diff_coverage_claim_reopen.py:187-227 |

## Update History

- 2026-08-07T14:30+02:00 — 260731-EFA-L8 curator (bounded delta): recorded
  `TestLocalChangesNewFile` (lines 143-186) — the four whole-new-file rule arms (unique anchor
  in a cited range surfaces report-only; out-of-range resolution enforced; ambiguous-now invalid;
  source absent from the working tree enforced) — and refreshed the class ranges. Verification
  metadata stays pinned until closeout stamps the code commit.
- 2026-08-05T23:20+02:00 — 260731-EFA-L16 curator: recorded the two closeout flow tests — a changed construct completes with the stamp advanced to the new code commit, and a deleted construct refuses in the citation gate BEFORE the code commit with `citation_anchor_absent_from_range` (no commit spent) — plus the phase-payload contract (citation pair before, sanity checks after). Verification metadata stays pinned until closeout stamps the L16 commit.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
