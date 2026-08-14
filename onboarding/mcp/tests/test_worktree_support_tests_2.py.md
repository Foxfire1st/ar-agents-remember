# mcp/tests/test_worktree_support_tests_2.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_worktree_support_tests_2.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-13T12:53+02:00                                            |
| lastVerifiedCommitHash | `100b40d6be4a7d03eedbb1164ce54e2e8a314038`                                        |
| lastVerifiedCommitDate | 2026-08-14T08:23:37+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_worktree_support_tests_2.py`'s source module; covers the behaviours named by its test classes, including the ordered memory-quality phases reported by external-memory closeout.

## Code Commentary

- `WorktreeSupport2` now asserts every integration/re-closeout branch through the contract-derived
  code and memory source branches, not a literal `main`. When either a non-overlapping or
  conflicting master source change lands after leaf closeout, integration returns
  `source-lineage-stale` with `sync_source_lineage`; it does not attempt obsolete integration-time
  replay. Conflict classification belongs after the leaf has synchronized onto current master.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_worktree_support_tests_2.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## L23 Final Candidate Disposition

This support split covers closeout, integration, lineage refusal, and recovery projections across
transport or process replacement. Exact-once irreversible work remains plane-owned and task-addressed.

## Update History
- 2026-08-14T06:40+02:00 — L23 final candidate review: this split support suite retains closeout,
  integration, recovery, and lineage regressions without exposing private operation identity.

- 2026-08-13T12:53+02:00 — L23 lineage-fixture repair: replaced literal-main assertions with the
  task-derived source branches and replaced both post-closeout replay expectations with the
  fail-closed `source-lineage-stale`/`sync_source_lineage` contract. Verification provenance
  remains closeout-owned.

- 2026-08-10T00:00+02:00 — 260731-EFA-L9 follow-up: the clean-claim closeout assertion now proves entity-catalog alignment precedes citation checks in the reported pre-metadata-refresh phase. Verification metadata remains pinned until closeout stamps the code commit.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
