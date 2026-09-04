# mcp/tests/test_worktree_support_tests_2.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_worktree_support_tests_2.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-04T10:05+02:00 |
| lastVerifiedCommitHash | `cfd0938103b1392e471144b6997c51a41591ad2b` |
| lastVerifiedCommitDate | 2026-09-04T08:34:11+02:00 |
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_worktree_support_tests_2.py`'s source module; covers the behaviours named by its test classes, including the ordered memory-quality phases reported by external-memory closeout.


CCR-R22@v1 (L22, commit `685f83c44055`): closeout fixtures now carry
`certification_profile=TEST_CERTIFICATION_PROFILE_REFERENCE` and
`run_authorized_closeout_mechanics(args, publish_code_quality=True)` so the mechanics closeout
runs profile-bound passing evidence.


CCR-R12@v4 (260831-CCR-L12, commit `cfd09381`): the memory-preflight failure regression now runs
after a stubbed green staged-code gate (`code_gate_probe` under `mock.patch.object(closeout_module,
`_gate_staged_code`)`), proving the closeout memory-quality preflight still aborts closeout when the
code gate is green, while the closeout-gate suite itself pins that a red code gate blocks the memory
preflight entirely (Gate-5 order).

## Code Commentary

- `WorktreeSupport2` now asserts every integration/re-closeout branch through the contract-derived
  code and memory source branches, not a literal `main`. When either a non-overlapping or
  conflicting master source change lands after leaf closeout, integration returns
  `source-lineage-stale` with `sync_source_lineage`; it does not attempt obsolete integration-time
  replay. Conflict classification belongs after the leaf has synchronized onto current master.
- The existing-head closeout-apply fixture publishes a passing route-review record before invoking
  the real closeout mechanics. This keeps the case focused on stamping an already-committed code
  range while still satisfying the production admission contract that route review is bound to
  the exact candidate.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_worktree_support_tests_2.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## L23 Final Candidate Disposition

This support split covers closeout, integration, lineage refusal, and recovery projections across
transport or process replacement. Exact-once irreversible work remains plane-owned and task-addressed.

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## 260821-CLIVE-L1 Support Fixture Migration

Affected closeout, recovery, and contract cases now use canonical publication and normalized effective input. The existing worktree behavior remains under test while journal authority and explicit enabled messages satisfy the same boundary as production.


## PDLS Reconciliation

The second worktree support suite was aligned with current lifecycle output identity without changing its behavioral contract.

The test continues to exercise production-owned behavior. No diagnostic result is treated as
certifying evidence and no fallback or threshold exception was introduced.
## Update History

- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass for cfd09381 (CCR-R12@v4): recorded the Gate-5-order update - memory-preflight failure is forced after a green (stubbed) code gate and a red code gate blocks the memory preflight.

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the profile args and publish_code_quality in worktree support tests 2.


- 2026-08-29T16:54+02:00 — Added the exact passing route-review fixture required by current
  closeout admission to the existing-head stamping proof and documented that boundary.
- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated relationship changes against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout.

- 2026-08-16T05:18+02:00 — Dagger fixture repair: a refused direct unjournaled conflicting replay leaves integration not-started and therefore projects `integration-pending`, without inventing a durable blocked operation.
- 2026-08-16T04:06+02:00 — Dagger fixture repair: retired direct integration CLI success paths retain their no-mutation assertions against the exact plane-owned journaled-integration refusal.
- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.
- 2026-08-14T06:40+02:00 — L23 final candidate review: this split support suite retains closeout,
  integration, recovery, and lineage regressions without exposing private operation identity.

- 2026-08-13T12:53+02:00 — L23 lineage-fixture repair: replaced literal-main assertions with the
  task-derived source branches and replaced both post-closeout replay expectations with the
  fail-closed `source-lineage-stale`/`sync_source_lineage` contract. Verification provenance
  remains closeout-owned.

- 2026-08-10T00:00+02:00 — 260731-EFA-L9 follow-up: the clean-claim closeout assertion now proves entity-catalog alignment precedes citation checks in the reported pre-metadata-refresh phase. Verification metadata remains pinned until closeout stamps the code commit.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
## Docs References

No external Domain Documentation source is configured for this internal route; task `260821-CLIVE-L1` and the cited repository source/tests govern this curation.


## Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.
