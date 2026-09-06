# mcp/tests/test_worktree_integrate_quality_gate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_worktree_integrate_quality_gate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks that leaf integration reuses closeout acceptance without launching another quality run, and that source movement after quality refuses before memory or merge mutation. Master-end full validation remains lifecycle-owned; the old complete altitude/profile matrix is not all retained in this file.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Leaf integration reuses closeout acceptance without running a gate | `test_leaf_integration_reuses_closeout_acceptance_without_running_a_gate` | mcp/tests/test_worktree_integrate_quality_gate.py:199-216 |
| Source movement after quality refuses before memory or merge | `test_source_movement_after_quality_refuses_before_memory_or_merge` | mcp/tests/test_worktree_integrate_quality_gate.py:218-251 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the profile_reference forwarding in integration quality gate tests.


- 2026-08-28T06:40+02:00 — No content impact: synthetic integration repositories now place the
  quality wrapper at its verification-package path; integration altitude and gate assertions are
  unchanged.
- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-20T05:12+02:00 — L11 landed-wave refresh: the leaf-segment graph-model commit
  (f2e2f4b9) touched this source; card re-verified against the current file, verification stamp
  advanced to f2e2f4b9. Body unchanged — the documented contract still holds.


- 2026-08-17T12:30+02:00 — No content impact: L5 extends the suite for the altitude-routed organizational full gate; the documented quality-gate ownership is unchanged.

- 2026-08-16T07:05+02:00 — L4 review repair: completed apply without a durable recovery tuple now refuses before queue completion; read-only completed preview remains non-mutating.
- 2026-08-16T05:18+02:00 — Dagger fixture repair: the post-memory source-move unit case executes its publication callback through an isolated queue-owner seam with a valid operation key, retaining the real two-stage source recheck.
- 2026-08-16T04:06+02:00 — Dagger fixture repair: series gates use a real approved closeout commit, queue-claim mocks isolate pre-merge memory blockers, and source movement patches exact named-ref reads.
- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.

- 2026-08-15T11:07+02:00 — No content impact: corrected the synthetic task root to the canonical
  coordination hierarchy required by queue scope resolution; quality-gate assertions are unchanged.
- 2026-08-14T12:13:26+02:00 — R43 curator: added the consumer-master non-blocking counterpart to
  the self-repository missing-wrapper refusal. Verification remains closeout-owned.

- 2026-08-14T11:27+02:00 — R39 curator: replaced leaf rerun expectations with certified-commit
  reuse and master-only full enforcement. Verification remains closeout-owned.
- 2026-08-14T09:37+02:00 — Reopened L23 cadence proof: the leaf seam asserts zero quality-decider
  and executor calls, while the series seam retains the single full Dagger run and refusal boundary.
- 2026-08-14T06:40+02:00 — L23 final candidate review: integration tests prove targeted leaf versus
  full master Dagger altitude, mandatory diff base, pre/post-quality lineage rechecks, pinned source
  tips, and failure atomicity before refs move.

- 2026-08-13T12:53+02:00 — L23 Dagger-rail coverage: recorded exact source-tip unchanged/moved
  behavior, both post-quality/pre-merge rechecks, and the complete memory replay helper branch
  matrix. Verification provenance remains closeout-owned.


- 2026-08-13T08:40+02:00 — L23 integration-gate repair: added the post-quality source-tip movement refusal and proved memory replay plus source merge remain untouched. Verification metadata remains closeout-owned.

- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: added the
  absent-cap/host-managed integration proof while retaining explicit settings-
  cap and altitude-routing coverage. Verification metadata remains pinned
  until closeout stamps L24.

- 2026-08-11T19:58+02:00 — Reconciled `test_worktree_integrate_quality_gate.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: created this file-level
  onboarding card for the new integration-altitude suite; content derived from
  the current worktree source. Verification metadata pinned until closeout
  stamps the 260731-EFA-L17 commit.
