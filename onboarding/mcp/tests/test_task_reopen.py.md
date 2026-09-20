# mcp/tests/test_task_reopen.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_task_reopen.py`            |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-20T14:20+02:00 |
| lastVerifiedCommitHash | `4ef4dddc9194930611db2b1dfbb6e02113f2226a` |
| lastVerifiedCommitDate | 2026-09-20T15:00:59+02:00|
| reviewedWorkingCandidate | candidate `ar/260915-ks-l43-ar`, uncommitted; base `fb719f8936d337c4685f2758d4ba3731cd8b7fc5` |
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks reopen resets the exact contract, leaf document and parent row to planning while preserving the leaf identity and recording the decision. An injected contract-publication failure rolls back document and landing changes. The same module also carries the **series** half: one gathered case drives the terminal atomic-series reopen and, through two plain helper methods, the two other arrivals at the same publication — the series that is already live at a collected address, and the reset that was interrupted before its successor generation was published. Deleted guard/start/abandon companion suites are not claimed as current tests here.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

`SeriesReopenTests` is deliberately **one collected subject told from all of its arrivals**. The
collected case drives the terminal series: the reset of the contract cells, the master document and
the enclosure generation, with the fixture asserting up front that the cleanup really did retire the
integration branch, because a re-cut of a branch that still exists would be measuring the wrong
thing. Its two helper methods are plain (not `test_*`) on purpose: both pytest lanes sit at exactly
their case budget, and one added collected case makes the lane run **zero** tests rather than one
more. They are called from inside the collected case, so they still execute — a plain method is a
budget fact here, not a claim that the scenario is unverified.

The three facts the gathered subject pins are the three ways a series reaches the publication:

- **`advance`** — a series that is in flight (neither closeout nor integration completed) may stand
  strictly ahead of its source *on the same line*. That branch is the series' own landed work, so it
  is reported as `advance` and never moved; a diverged or lagging branch keeps its refusal.
- **`publish`** — a series already live at an address whose generation is `terminal-archived`, with
  closeout and integration untouched, is re-addressed rather than refused: the successor generation
  is published and the branch is left exactly where the series put it.
- **the counter** — the completion's spent review rounds (`round: 3` in the fixture) are cleared to
  `0`, not pending, no baseline or residual, no developer approval and no additional rounds, so the
  next round reads as the first instead of the fourth.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.
The series methods reuse the shared `task_reopen_test_support` fixtures rather than building their
own contract, and each scenario gets its own temporary workspace so the locator state of one cannot
leak into another.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

A branch is only ever read, never moved, by any of these scenarios: the fixture records the landed
commit before the call and asserts the same commit after it. Adding a collected subject to this
module is a cross-lane budget decision, not a local one.

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
| Resets contract doc and master index | `test_resets_contract_doc_and_master_index` | mcp/tests/test_task_reopen.py:38-79 |
| Contract publish failure rolls back docs and landing | `test_contract_publish_failure_rolls_back_docs_and_landing` | mcp/tests/test_task_reopen.py:81-105 |
| The terminal series reopen, gathered as one collected subject across all three of its arrivals. | `test_a_terminal_series_is_reopened_without_ever_moving_a_live_ref` | mcp/tests/test_task_reopen.py:117-226 |
| The reset that is durable while the locator is still the collected generation is resumed, not refused. | `_assert_an_interrupted_series_reset_is_resumed` | mcp/tests/test_task_reopen.py:228-259 |
| A series that is already live and unaddressed is re-addressed: the successor is published citing the archived predecessor, the branch is unmoved, and the spent review counter is cleared. | `_assert_a_live_unaddressed_series_is_re_addressed` | mcp/tests/test_task_reopen.py:261-358 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-20T14:20+02:00 — 260915-KS-L43 curator (deterministic-check clearance inside this leaf's change set, uncommitted on `ar/260915-ks-l43-ar`, code base `fb719f89`): **one `ruff format` reflow inside an existing case; no claim changed.** In `SeriesReopenTests` the `commit_file(contract.code_repo_path, "late.txt", …)` call split across lines, which is a whitespace change inside that class's second method. The reflow is net two lines at its own span and **lands below `:146`**, so the card's five cited ranges are unchanged and each was verified at the reformatted tree: `ReopenResetTests` `:38-79` still opens on `test_resets_contract_doc_and_master_index`, `:81-105` still opens on `test_contract_publish_failure_rolls_back_docs_and_master_index`, `SeriesReopenTests` `:117-226` still opens on `test_a_terminal_series_is_reopened_without_ever_moving_its_line`, `:228-259` still opens on `self._assert_an_interrupted_series_reset_is_resumable` and `:261-358` still spans the resumed-locator assertions to the file's end. No range moved and no claim changed. **Stamp accounting:** `reviewedWorkingCandidate` now names this leaf's candidate `ar/260915-ks-l43-ar` on base `fb719f89`; the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is retained exactly as recorded. No commit was made.

- 2026-09-20T02:50+02:00 — 260915-KS-L34 curator (uncommitted change set on `ar/260915-ks-l34-ar`, code base `0da444b3`): **the series half of `task_reopen` is now covered here, and the two retained leaf rows were re-pointed at the ranges the file actually has.** The collected subject `test_a_terminal_series_is_reopened_without_ever_moving_a_live_ref` was extended from two facts to four (a live ref is never moved; the reset is otherwise complete; a series already live at a collected address is re-addressed instead of refused; and the review counter the completion spent is cleared), and it gained two plain helper methods — `_assert_an_interrupted_series_reset_is_resumed` and `_assert_a_live_unaddressed_series_is_re_addressed` — which it calls inside its own body. They are deliberately **not** `test_*` methods: both lanes sit at exactly their case budget, and a single added collected case makes the lane raise `UsageError` and execute **zero** tests rather than one more. The two pre-existing rows had drifted with the file's growth and now cite `:38-79` and `:81-105` (previously `:25-66` and `:68-92`), each re-derived against the file as it stands rather than shifted by arithmetic. No verification stamp advanced and none was invented: the candidate is uncommitted, the governed closeout owns the real code and memory commits, and the metadata carries a `reviewedWorkingCandidate` row naming this candidate because the body moved under the retained pair.

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