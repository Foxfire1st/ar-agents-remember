# mcp/tests/test_task_reopen.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_task_reopen.py`            |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks reopen resets the exact contract, leaf document and parent row to planning while preserving the leaf identity and recording the decision. An injected contract-publication failure rolls back document and landing changes. Deleted guard/start/abandon companion suites are not claimed as current tests here.

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
| Resets contract doc and master index | `test_resets_contract_doc_and_master_index` | mcp/tests/test_task_reopen.py:25-66 |
| Contract publish failure rolls back docs and landing | `test_contract_publish_failure_rolls_back_docs_and_landing` | mcp/tests/test_task_reopen.py:68-92 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-08-26T10:44:52+02:00 — No behavior change: common reopen contract/memory fixtures moved to `task_reopen_test_support`; reopen publication and authority assertions are unchanged.

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-24T00:51+02:00 — 260821-CLIVE-L2: reconciled the L2 test boundary represented by the changed source. Verified at code commit `1d446724`.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-16T05:18+02:00 — Dagger repair: reopen preview proves byte preservation now that dry-run start does not create an authority lock; a missing legacy `master` field still resets the exact canonical parent row derived from task topology.
- 2026-08-16T04:06+02:00 — 260815-DAG-L4 Dagger repair: migrated the shared reopen and start-after-reopen fixtures from the retired universal master-series chain to the production organizational direct-super lineage; exact Git commits replace placeholder candidate ids, and successful restart asserts that no series contract is created.
- 2026-08-16T03:12+02:00 — No content impact: the sprint execution-graph fixture now validates its
  raw payload through `SprintExecutionGraph` before passing it to `TaskDocument`, satisfying the
  typed constructor while preserving the same atomic graph and reopen assertions.

- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.

- 2026-08-15T10:24+02:00 — L3 file-size repair: moved `ReopenGuardTests` into the focused
  `test_task_reopen_guards.py` suite; helpers and all reset/restamp/start behavior stay here.
- 2026-08-15T09:10+02:00 — L3 content update: reconciled the restamp tests with publisher injection
  and removed the retired direct-call citation; verification remains closeout-owned.
- 2026-08-14T05:26Z — L23 final curator: re-anchored the ambient-end regression after the helper
  became the public application-level owner; the single-writer lifecycle contract is unchanged.
  Verification remains closeout-owned.
- 2026-08-12T20:10+02:00 — L23 curator: documented no-mutation reopen refusal on moved super ancestry; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-04T11:42:15+02:00 — 260731-EFA-L6 S18-B04 — same-reviewer semantic correction: split reopen lookup/restamp and legacy
  load/write normalization claims, with generated ranges delegated to the scoped fixer.

- 2026-08-03T03:59:59+02:00 — Curated 10 citation findings (5 table rows, 5 source-form repairs): added exact anchors and source paths; scoped fixer generated the final ranges.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T16:50+02:00 — No content impact: 260731-EFA-L2 curator checked this file against the
  leaf diff. Only fixture construction changed: the three `default_contract(...)` fixtures
  (`_completed_leaf_contract` and both `StartAfterReopenTests` cases) now pass
  `ContractTask(...)`, `leaf=LeafIdentity(...)` and `code=RepoBranchPlan(...)` instead of twelve
  loose keyword arguments, and `AbandonAmbientLifecycleTests` builds
  `AmbientLifecycle(store, timing=AmbientTiming(heartbeat_seconds=3600))`. Every field value,
  test name, guard blocker and reset expectation is unchanged; this sidecar names neither
  builder's argument list and carries no line citations, so the reopen-guard, reset, leaf-doc
  lookup/restamp and start-after-reopen descriptions all still match.
- 2026-07-07T20:50+02:00 — 260707-HFX-L4: legacy reopened contract fixtures now expect `load_contract`
  to normalize a proven stem-shaped leaf id to the canonical task doc id. Verification metadata pinned
  until closeout stamps the 260707-HFX-L4 commit.
- 2026-07-03T12:50+02:00 — No content impact: L15 typed the blockers payload access (cast to list[str]) at three join sites for pyright; assertions unchanged.
- 2026-07-03T00:30+02:00 — Created for L11: guards/resets for task_reopen, leaf-doc lookup/restamp,
  start-after-reopen recreation with doc restamp, and abandon's ambient lifecycle end. Verification
  metadata pinned until closeout stamps the code commit.