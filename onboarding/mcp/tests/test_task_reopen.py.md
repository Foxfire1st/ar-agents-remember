# mcp/tests/test_task_reopen.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_task_reopen.py`            |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash | `346507af24396ab7b491e02511c4af006ccd3dc5` |
| lastVerifiedCommitDate | 2026-08-30T07:51:57+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[tests/overview.md](overview.md)

## Purpose

`test_task_reopen.py` covers the L11 reopen semantics in isolation: the `task_reopen`
resets, the task-domain leaf-doc lookup/restamp helpers, the
worktree-start recreate path for reopened contracts, and the abandon-side ambient
lifecycle end. The small refusal-only guard class is split into `test_task_reopen_guards.py`.

## Code Commentary

### Logic

`_completed_leaf_contract` hand-builds a fully landed leaf enclosure (closeout,
integration, and cleanup all completed, worktrees absent) under a temp coordination
root; `_leaf_doc`/`_master_doc` author the matching task documents through the real
store and are also reused by the split guard suite. `ReopenResetTests` prove the happy path
(contract fields reset, `cleanup: reopened`,
leaf id unchanged, doc back to `planning` with the audit decision, master index row
flipped), the dry-run writes-nothing contract, and the doc-less leaf case.
`LeafDocLookupTests` cover the case-insensitive id/enclosure-ref/stem joins and the
overwrite-idempotent restamp. `AbandonAmbientLifecycleTests` installs a real
`AmbientLifecycle` over an `EventStore` and proves `_end_ambient_lifecycle_if_anchored`
ends only the anchored lifecycle (owner-written `lifecycle.ended` tail).
`StartAfterReopenTests` run the real `start_result` against an initialized git repo:
a `cleanup: reopened` contract recreates fresh with the new lifecycle and restamps the
doc's `lifecycleId`, while a live contract still attaches unchanged. HFX-L4 pins legacy
stem-shaped contract loading by expecting a reopened legacy enclosure to load with the canonical
task doc id when the task tree proves the mapping.

### Invariants And Boundaries

- The reopen tests exercise the module API directly (`reopen_task(contract_path)`),
  not the MCP transport; the representative-payload conformance for the `task_reopen`
  tool lives in `test_tool_response_conformance.py`.
- The start tests create the memory-repo skeleton dirs because coordination context
  resolution requires them even with memory disabled.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module under test. | `reopen_task` | mcp/src/agents_remember/worktrees/reopen.py:169-265 |
| The lookup helper under test. | `find_leaf_doc` | mcp/src/agents_remember/tasks/leaf_doc.py:56-70 |
| The lifecycle restamp helper under test. | `restamp_leaf_doc_lifecycle` | mcp/src/agents_remember/tasks/leaf_doc.py:178-197 |
| The recreate-fresh start path publishes its restamp through task-first mutation and projection invalidation. | `_create_start_enclosure` | mcp/src/agents_remember/worktrees/modules/start.py:620-682 |
| Contract loading preserves a legacy stem-shaped leaf id when the task tree proves the mapping. | `load_contract` | mcp/src/agents_remember/worktrees/worktree_contract.py:436-469 |
| The canonical contract leaf-id normalization helper is `normalize_contract_leaf_id`. | `normalize_contract_leaf_id` | mcp/src/agents_remember/worktrees/worktree_contract.py:556-579 |
| The abandon-side ambient end helper under test. | `end_ambient_lifecycle_if_anchored` | mcp/src/agents_remember/application/worktree_tools.py:1026-1035 |

## L23 Reopen Lineage Regression

The reopen fixture now builds a real organizational sprint-super-to-leaf lineage with no
series contract. Advancing super proves reopen returns a blocked strict projection before
changing either the enclosure contract or leaf document; ordinary start-after-reopen coverage
continues on the same organizational master topology.

## 260815-DAG-L3 Restamp Publisher Contract

Leaf lifecycle restamp tests now inject the ordinary task-doc publisher explicitly. The assertions
for changed, unchanged, blocked, same-lifecycle, missing-doc, and exact identity behavior remain,
while the production start path can route the same planned write through queue governance.

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## 260821-CLIVE-L2 Start Publication Seam

The reopened-start test now patches `publish_new_lifecycle_operation_location` on the start owner,
not the lower contract writer. The assertion boundary therefore follows the canonical bootstrap
sequence: task/contract preparation may occur, but lifecycle state becomes discoverable only when
the enclosure-root locator and immutable manifest are published.

| Finding | Anchor | Source |
| --- | --- | --- |
| Start-after-reopen forcing intercepts the lifecycle-location publication owner. | `test_false_terminal_leaf_blocks_absent_and_reopened_starts_before_any_effect` | mcp/tests/test_task_reopen.py:698-821 |

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces completed-leaf reopen, exact task reset, predecessor transition, ambient lifecycle retirement, and subsequent start behavior.

### Current Invariants

- Reopen is an explicit task/contract transition and preserves historical evidence.
- Projection effects follow task publication; queue state never freezes the reopen write.

## Update History

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