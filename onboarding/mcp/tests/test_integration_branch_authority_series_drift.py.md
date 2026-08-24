# mcp/tests/test_integration_branch_authority_series_drift.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_integration_branch_authority_series_drift.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Forces an atomic series whose sprint source advanced after closeout to refuse the leaf-owned
replay/conflict path instead of treating the ambient repository checkout as a writable leaf.

## Code Commentary

The focused regression uses the real configured atomic blocker, series contract, named atomic
candidate ref, and lifecycle operation owner. It advances the sprint super after series closeout,
requests replay, and proves operation creation refuses before a durable journal is written.

## Invariants And Boundaries

- Atomic-series source drift cannot be resolved through an ambient leaf worktree.
- A refused replay attempt creates no integration operation record.
- The test is moved from the broader edge suite without duplicated behavior or compatibility code.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The focused suite owns the atomic-series source-drift replay refusal. | `IntegrationBranchAuthoritySeriesDriftTests` | mcp/tests/test_integration_branch_authority_series_drift.py:22-52 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_atomic_series_source_drift_cannot_open_an_ambient_leaf_replay`. The L2 additions force journal-owned claim transfer, exact protected-ref decisions, source-movement reconciliation, and organizational disposition/repair without queue-owned lifecycle evidence.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current test source exercises `test_atomic_series_source_drift_cannot_open_an_ambient_leaf_replay`. | L23-L52 | `mcp/tests/test_integration_branch_authority_series_drift.py` |

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces atomic-series protected-ref refusal when the exact series source lineage drifts.

### Current Invariants

- The live series contract and ref authority own the exclusion.
- Drift does not freeze unrelated task-document authoring.

## Update History

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-16T07:46+02:00 — 260815-DAG-L4: created by moving the atomic source-drift/replay refusal from `test_integration_branch_authority_edges.py` to keep both discovered modules below the enforced file-size limit without duplication. Verification remains closeout-owned.
