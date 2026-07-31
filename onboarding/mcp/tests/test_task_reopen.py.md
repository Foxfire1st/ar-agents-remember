# mcp/tests/test_task_reopen.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_task_reopen.py`            |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-07T20:50+02:00 |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
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

| Finding | Source Path |
| --- | --- |
| The module under test. | [reopen.py](agents-remember/mcp/src/agents_remember/tasks/reopen.py) |
| The lookup/restamp helpers under test. | [leaf_doc.py](agents-remember/mcp/src/agents_remember/tasks/leaf_doc.py) |
| The recreate-fresh + restamp start path under test. | [start.py](agents-remember/mcp/src/agents_remember/worktrees/modules/start.py) |
| Contract load/write normalization for legacy leaf ids. | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| The abandon-side ambient end helper under test. | [worktree_tools.py](agents-remember/mcp/src/agents_remember/controllers/worktree_tools.py) |

## Update History

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
