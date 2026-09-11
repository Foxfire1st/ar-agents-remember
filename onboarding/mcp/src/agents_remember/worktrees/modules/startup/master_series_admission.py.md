# mcp/src/agents_remember/worktrees/modules/startup/master_series_admission.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/startup/master_series_admission.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-08T19:16:43+02:00 |
| lastVerifiedCommitHash | `602143bd1d48226f4d53b83ff7c5002a695dcdff` |
| lastVerifiedCommitDate | 2026-09-09T00:26:24+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[worktrees/modules overview](../../overview.md)

## Purpose

Startup-side validation of the persisted master-series contract edge. This module reads the
existing series contract, compares task, repository, memory, and branch identity with the
commanding sprint specification, and projects an actionable refusal through the shared atomic
series admission response.

## Code Commentary

### Logic

`MasterSeriesContractSpecLike` describes the identity fields needed for validation without
coupling the checker to one concrete startup object. `MasterSeriesContractAdmissionEvidence`
retains the contract path, existing contract, and expected/observed edge dictionaries;
`MasterSeriesContractAdmissionError` carries that evidence through the startup boundary.

`_master_series_admission_refusal` derives the requested task-document reference when the task is
under the repository task root, then calls `atomic_series_admission_projection`. Its
`WorktreeCommandResult` preserves the refusal status/detail, exact contract path, retryability,
structured admission, and contract-bound `worktree_status` action. Both the top-level refusal and
the nested observed parser detail are bounded before serialization, so a malformed contract cannot
overflow the public response while losing its actionable error prefix.

`_existing_master_series_contract` treats absence as a fresh bootstrap, preserves unreadable and
wrong-kind errors with expected/observed evidence, and ignores terminal series artifacts that no
longer own the lane. A live non-terminal contract must satisfy all three edge groups:
`_same_master_task_edge`, `_same_master_repository_edge`, and `_same_master_branch_edge`.
`_master_series_expected_edges` and `_master_series_observed_edges` provide the explicit values for
each mismatch. A `ContractError` from the authoritative contract read is preserved as the concrete
parser reason in both the refusal detail and the observed evidence. The repository helpers compare
actual Git repository identity and require the external-memory ledger to remain rooted at the
selected memory repository/worktree.

### Conventions

The module returns typed startup results for expected contract-edge refusal instead of allowing a
traceback to cross the MCP boundary. Terminal-series cleanup is treated as a stale artifact and
returns no existing contract so fresh bootstrap can proceed. Repository comparison uses Git common
identity, not checkout path spelling or ambient branch state.

### Invariants And Boundaries

- This module validates and explains persisted edges; it does not repair or write the series
  contract, selector authority, branches, or memory ledger.
- Task identity, repository/memory identity, and source/work-branch identity are checked as separate
  edge groups so the refusal names the exact mismatch.
- External-memory contracts require the expected memory repository/worktree/ledger relationship;
  internal or disabled memory has no external memory edge.
- A terminal series artifact has relinquished ownership and is eligible for fresh bootstrap; a
  non-terminal mismatched artifact is a fail-closed startup refusal.
- The returned retry action is read-only `worktree_status` addressed by repository and exact
  contract path.

### Todos

The source is an uncommitted L38 candidate. Closeout owns the eventual commit-derived verification
stamp; this sidecar does not claim acceptance or Gate 5 evidence.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The startup protocol and admission error retain the fields needed for contract-edge diagnostics. | `MasterSeriesContractSpecLike`; `MasterSeriesContractAdmissionEvidence`; `MasterSeriesContractAdmissionError` | mcp/src/agents_remember/worktrees/modules/startup/master_series_admission.py:26-77 |
| Refusal projection preserves expected/observed edges, bounds public parser detail, and emits a contract-bound read-only status action. | `_master_series_admission_refusal` | mcp/src/agents_remember/worktrees/modules/startup/master_series_admission.py:91-150 |
| Existing contract loading distinguishes absent, unreadable, wrong-kind, terminal, and mismatched series artifacts, preserving concrete parser detail for unreadable contracts. | `_existing_master_series_contract` | mcp/src/agents_remember/worktrees/modules/startup/master_series_admission.py:153-215 |
| Task, repository/memory, and branch edge checks remain separate and fail closed. | `_same_master_task_edge`; `_same_master_repository_edge`; `_same_master_branch_edge` | mcp/src/agents_remember/worktrees/modules/startup/master_series_admission.py:218-276 |
| Expected and observed edge payloads expose the exact persisted values used in a mismatch. | `_master_series_expected_edges`; `_master_series_observed_edges` | mcp/src/agents_remember/worktrees/modules/startup/master_series_admission.py:279-374 |
| Repository identity and external-memory ledger relationship are checked against actual Git roots. | `_repository_root`; `_same_repository_root`; `_same_optional_repository_root`; `_same_series_memory_edge` | mcp/src/agents_remember/worktrees/modules/startup/master_series_admission.py:377-418 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-08T19:16:43+02:00 — CCR-L38 CQ04 preparation rebound the refusal projector after oversized malformed-contract diagnostics were reproduced. Public and observed detail now retain bounded parser evidence; focused proof remains non-certifying and closeout-owned.
- 2026-09-08T18:54:49+02:00 — CCR-L38 CQ04 preparation reconciled the authoritative contract reread and preserved concrete `ContractError` parser detail in typed observed evidence. The validator/test result is source evidence only; verification remains closeout-owned with no acceptance claim.
- 2026-09-08T17:36:08+02:00 — CCR-L38 source-grounded preparation added the one-to-one sidecar for the current `master_series_admission.py` edge validator and refusal projector. The source remains uncommitted; the base metadata is retained and closeout owns the eventual verification stamp. No acceptance or Gate 5 claim.
