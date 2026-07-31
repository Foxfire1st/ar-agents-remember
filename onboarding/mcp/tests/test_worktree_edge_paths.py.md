# mcp/tests/test_worktree_edge_paths.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_worktree_edge_paths.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T15:32+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Worktree lifecycle paths **that only a refusal or a recovery reaches**. The happy path
through start / sync / integrate / cleanup is covered elsewhere; what was not is the other
side of each guard.

Each of these is the case where getting it wrong is expensive — worktrees created on a stale
base, a half-integrated pair, a branch deleted while checked out — so each is tested for the
**verdict it produces**, not merely for running.

## Classes

| Class | Guard |
| --- | --- |
| `ContractMemoryModeTests` | A contract is the durable record of a task; an unknown memory mode is refused **at construction**, rather than written out and discovered later. |
| `DeclaredLeafCandidateTests` | Leaf ids come out of hand-editable task documents, so a blank one is **data, not a programming error**: it is skipped rather than minting a candidate nothing can address. |
| `RetireWorkBranchTests` | `_retire_work_branch` deletes a task branch only when it is safe to — including stepping off the branch it is about to delete. |
| `StartPipelineTests` | `start_result`'s composition: which stage's answer wins, and what start does **not** do once a stage refuses. |
| `ExistingContractStartTests` | What `worktree_start` does when a contract already exists at the path. |
| `PreflightedContractTests` | `_preflighted_contract` returns the contract the rest of start must use — a blocked preflight is handed straight back instead of creating worktrees. |
| `MemorySyncBlockTests` | The two memory-side sync refusals, and what each tells the caller to do next. |
| `MoveMemoryBranchTests` | A merge that cannot be resolved automatically **leaves the worktree usable**. |
| `FetchSourceUpstreamsTests` | The best-effort pre-sync fetch reports per side rather than failing the sync. |
| `OverviewRevisionTests` | Which route overviews the closeout classifier can speak for at all. |
| `IntegrationRefusalTests` | Integration refuses **before it moves any branch**. |

## Invariants And Boundaries

- A refusal must be reached before any destructive or creative side effect: no worktrees on
  a blocked preflight, no branch moved on a refused integration.
- Hand-editable inputs (task documents) produce skips, not exceptions.
- A conflicting memory merge aborts and leaves the worktree in a usable state.
- The fast-forward recovery rebuilds the contract when branch tips moved under it.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The worktree lifecycle under test: contract, start, sync, integrate, retire. | [worktree/](agents-remember/mcp/src/agents_remember/worktree/) |
| The happy-path lifecycle suites these guards sit beside. | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py), [test_worktree_sync.py](agents-remember/mcp/tests/test_worktree_sync.py), [test_worktree_contract_lifecycle.py](agents-remember/mcp/tests/test_worktree_contract_lifecycle.py) |
| Helper-level arms of the same lifecycle. | [test_worktree_and_observer_helpers.py](agents-remember/mcp/tests/test_worktree_and_observer_helpers.py) |

## Update History

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new worktree
  refusal/recovery suite. Verification metadata is pinned to the leaf's reformat commit until
  closeout stamps the code commit.
