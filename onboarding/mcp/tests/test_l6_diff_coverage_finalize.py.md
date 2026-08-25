# mcp/tests/test_l6_diff_coverage_finalize.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_finalize.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash | `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e` |
| lastVerifiedCommitDate | 2026-08-25T17:21:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout coverage tests for task finalization helpers: task-target resolution, parent-target resolution, asserted reads, and reconcile/candidate logic.

## Code Commentary

- `TestResolveTaskTargets` covers series and leaf target resolution with and without task documents.
- `TestResolveParentTarget` covers parent-argument and standalone/leaf-with-master resolution.
- `TestAssertAndRead` covers parent-argument assertion, parent reads, and parent-row checks.
- `TestReconcileAndCandidates` covers reconcile skip/missing/write paths and candidate enumeration.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `TestResolveTaskTargets` (lines 68-105). | `TestResolveTaskTargets` | mcp/tests/test_l6_diff_coverage_finalize.py:68-105 |
| Defines the class `TestResolveParentTarget` (lines 108-151). | `TestResolveParentTarget` | mcp/tests/test_l6_diff_coverage_finalize.py:108-151 |
| Defines the class `TestAssertAndRead` (lines 154-208). | `TestAssertAndRead` | mcp/tests/test_l6_diff_coverage_finalize.py:154-208 |
| Defines the class `TestReconcileAndCandidates` (lines 211-261). | `TestReconcileAndCandidates` | mcp/tests/test_l6_diff_coverage_finalize.py:211-261 |

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Covers task-finalization helper branches for exact leaf/parent target resolution, source validation, candidate completion, reconciliation, and result rendering.

### Current Invariants

- Finalization mutates authoritative task documents only after their exact JSON/Markdown sources remain current.
- Completion is an explicit task transition and is not inferred from queue state.


## PDLS Reconciliation

Finalize diff-coverage forcing now includes typed task-document projection effects and current terminal disposition.

The test continues to exercise production-owned behavior. No diagnostic result is treated as
certifying evidence and no fallback or threshold exception was introduced.
## Update History

- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-15T09:53+02:00 — No content impact: L3's Pyright repair supplies the newly required
  contract fixture to finalization-helper calls and isolates queue publication in the write test;
  the L6 helper assertions remain unchanged.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
