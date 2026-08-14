# mcp/tests/test_task_reopen.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_task_reopen.py`            |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00 |
| lastVerifiedCommitHash | `100b40d6be4a7d03eedbb1164ce54e2e8a314038` |
| lastVerifiedCommitDate | 2026-08-14T08:23:37+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[tests/overview.md](overview.md)

## Purpose

`test_task_reopen.py` covers the L11 reopen semantics in isolation: the `task_reopen`
guard set and resets, the task-domain leaf-doc lookup/restamp helpers, the
worktree-start recreate path for reopened contracts, and the abandon-side ambient
lifecycle end.

## Code Commentary

### Logic

`_completed_leaf_contract` hand-builds a fully landed leaf enclosure (closeout,
integration, and cleanup all completed, worktrees absent) under a temp coordination
root; `_leaf_doc`/`_master_doc` author the matching task documents through the real
store. `ReopenGuardTests` prove refusal (returncode 2 with named blockers) for an
in-flight leaf, a series contract, and a leaf whose worktree dir still exists.
`ReopenResetTests` prove the happy path (contract fields reset, `cleanup: reopened`,
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
| The recreate-fresh + restamp start path under test. | `start_result`, "restamp_leaf_doc_lifecycle(contract.task_root" | mcp/src/agents_remember/worktrees/modules/start.py:440-451; mcp/src/agents_remember/worktrees/modules/start.py:602-602 |
| Contract loading preserves a legacy stem-shaped leaf id when the task tree proves the mapping. | `load_contract` | mcp/src/agents_remember/worktrees/worktree_contract.py:436-469 |
| The canonical contract leaf-id normalization helper is `normalize_contract_leaf_id`. | `normalize_contract_leaf_id` | mcp/src/agents_remember/worktrees/worktree_contract.py:556-579 |
| The abandon-side ambient end helper under test. | `end_ambient_lifecycle_if_anchored` | mcp/src/agents_remember/application/worktree_tools.py:512-519 |

## L23 Reopen Lineage Regression

The reopen fixture now builds a real super/master/leaf contract chain. Advancing
super proves reopen returns a blocked strict projection before changing either
the enclosure contract or leaf document; ordinary start-after-reopen coverage
continues on the same thematic master topology.

## Update History
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
