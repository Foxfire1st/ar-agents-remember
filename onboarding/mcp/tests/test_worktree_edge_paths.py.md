# mcp/tests/test_worktree_edge_paths.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_worktree_edge_paths.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T09:46+02:00                     |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51` |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
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
| `ContractMemoryModeTests` | A contract is the durable record of a task; an unknown memory mode is refused **at construction**, rather than written out and discovered later — and the refusal reaches the caller as a payload, not a traceback. |
| `DeclaredLeafCandidateTests` | Leaf ids come out of hand-editable task documents, so a blank one is **data, not a programming error**: it is skipped rather than minting a candidate nothing can address. |
| `RetireWorkBranchTests` | `_retire_work_branch` deletes a task branch only when it is safe to — including stepping off the branch it is about to delete. |
| `StartPipelineTests` | `start_result`'s composition: which stage's answer wins, and what start does **not** do once a stage refuses. |
| `MemoryDisabledStartTests` | `_contract_after_memory_start` — the recovery from a start that asked for external memory and could not get it: the whole memory topology goes, or none of it does. |
| `ExistingContractStartTests` | What `worktree_start` does when a contract already exists at the path. |
| `PreflightedContractTests` | `_preflighted_contract` returns the contract the rest of start must use — a blocked preflight is handed straight back instead of creating worktrees. |
| `MemorySyncBlockTests` | The two memory-side sync refusals, and what each tells the caller to do next. |
| `MoveMemoryBranchTests` | A merge that cannot be resolved automatically **leaves the worktree usable**. |
| `FetchSourceUpstreamsTests` | The best-effort pre-sync fetch reports per side rather than failing the sync. |
| `OverviewRevisionTests` | Which route overviews the closeout classifier can speak for at all. |
| `IntegrationRefusalTests` | Integration refuses **before it moves any branch**. |

## Two Refusals Worth Reading Together

`ContractMemoryModeTests` proves both halves of the vocabulary refusal, and the second half is
the one that is easy to lose. `test_leaf_contract_refuses_an_unknown_memory_mode` and its series
twin prove `default_contract` / `default_series_contract` **raise** `ContractError`;
`test_a_refused_request_leaves_the_start_as_a_result_not_an_exception` (L143-L164) then proves
`build_start_contract` converts that raise into a `WorktreeCommandResult(2, {"state":
"invalid-request", ...})` whose summary still carries the message. Its docstring states the reason
the conversion is load-bearing: nothing on `worktree_start`'s path — not
`mcp/registration/worktrees.py`, not `controllers/worktree_tools.py`, not `mcp/tools/worktree.py` —
catches `ContractError`, so an escaping raise would surface as a traceback instead of a blocked
result the agent can read and correct. It patches `start_contract_module._build_start_contract`
with a `side_effect`, since the refusal is the subject and reaching it for real would mean standing
up a git repository to test an argument check. The production half is `build_start_contract`'s
`except ContractError -> invalid_contract_request_result` (`modules/start_contract.py` L187-L200,
`modules/leaf_ref_start.py` L38-L53).

The refusal now covers `workflow_kind` too — the message the fixture uses,
`"workflow_kind must be one of ['chat-task', 'light-task']"`, is the shape `_task_vocabulary`
produces since `WorkflowKind` became a `Literal`.

`MemoryDisabledStartTests` covers the other direction: not a refusal, a **recovery**.
`memory_choice='disable'` answers the blocked-memory refusal, and
`_contract_after_memory_start(contract, {"state": "disabled"})` has to stop describing a memory
topology that will not exist — all of `memory_mode`, `memory_state`, `memory_repo_path`,
`memory_worktree`, `ledger_path`, `memory_source_branch`, `memory_work_branch` and
`memory_base_commit` together, and the test asserts each one, plus that `code_work_branch` did not
move with them. Half of that would leave closeout hunting for a memory repository the start
declined to create. The other two cases pin the narrow paths: a
`{"state": "ready", "reconciledMemoryBaseCommit": ...}` advances **only** `memory_base_commit` and
leaves `memory_mode` external, and a plain `{"state": "ready"}` returns the *identical object*
(`assertIs`), not an equal copy — so the no-op path is proven to allocate nothing.

## Invariants And Boundaries

- A refusal must be reached before any destructive or creative side effect: no worktrees on
  a blocked preflight, no branch moved on a refused integration.
- A refusal the caller cannot read is not a refusal: argument-vocabulary errors return a
  `WorktreeCommandResult` with exit 2 and `state: invalid-request`, because no layer between
  `build_start_contract` and the tool handler catches `ContractError`.
- Hand-editable inputs (task documents) produce skips, not exceptions.
- A conflicting memory merge aborts and leaves the worktree in a usable state.
- Disabling memory mid-start clears the memory topology *whole* — mode, repo path, both branches,
  base commit, worktree and ledger — and touches nothing on the code side.
- The fast-forward recovery rebuilds the contract when branch tips moved under it.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The worktree lifecycle under test: contract, start, sync, integrate, retire. | [worktrees/](agents-remember/mcp/src/agents_remember/worktrees/) |
| The construction refusal and its conversion to a result: `_task_vocabulary` (L150-L167, the `must be one of` messages) and `WorkflowKind = Literal["chat-task", "light-task"]` (L50). | [worktrees/worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| `build_start_contract` (L187-L200), which catches `ContractError` and `LeafRefResolutionError` so neither leaves the tool handler; `_contract_after_memory_start` (`modules/start.py` L137-L161) is the memory-disabled/reconciled recovery. | [worktrees/modules/start_contract.py](agents-remember/mcp/src/agents_remember/worktrees/modules/start_contract.py) |
| `invalid_contract_request_result` (L38-L53) — the `exit 2` / `state: invalid-request` payload the refusal becomes. | [worktrees/modules/leaf_ref_start.py](agents-remember/mcp/src/agents_remember/worktrees/modules/leaf_ref_start.py) |
| The happy-path lifecycle suites these guards sit beside. | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py), [test_worktree_sync.py](agents-remember/mcp/tests/test_worktree_sync.py), [test_worktree_contract_lifecycle.py](agents-remember/mcp/tests/test_worktree_contract_lifecycle.py) |
| Helper-level arms of the same lifecycle. | [test_worktree_and_observer_helpers.py](agents-remember/mcp/tests/test_worktree_and_observer_helpers.py) |

## Update History

- 2026-08-01T09:46+02:00 — 260731-EFA-L4 curator: the suite grew by 95 lines and the card's
  Classes table had gone from complete to eleven-of-twelve. Added the missing class,
  `MemoryDisabledStartTests` (L285-L353, three tests over
  `start_module._contract_after_memory_start`), and extended the `ContractMemoryModeTests` row for
  its fourth test, `test_a_refused_request_leaves_the_start_as_a_result_not_an_exception`
  (L143-L164). Wrote both up in a new section, because between them they are the leaf's real
  subject here: a vocabulary refusal that used to escape as a traceback now returns
  `WorktreeCommandResult(2, {"state": "invalid-request", ...})`, and a memory-disabled recovery
  has to clear the *whole* memory topology at once. Verified each production anchor rather than
  taking the test docstrings on trust — `build_start_contract` L187-L200 with its
  `except ContractError -> invalid_contract_request_result`, that helper at
  `modules/leaf_ref_start.py` L38-L53 returning exactly exit 2 / `invalid-request`,
  `_contract_after_memory_start` at `modules/start.py` L137-L161 (the disabled branch writes
  `memory_mode` through `amend_contract(..., ContractCells(memory_mode="disabled"))` while the
  free-text `memory_state` rides `replace`), and `_task_vocabulary` at
  `worktrees/worktree_contract.py` L150-L167, whose message is the
  `"workflow_kind must be one of ['chat-task', 'light-task']"` the fixture reproduces. Added two
  invariants for those. Also repaired the lifecycle reference row, which pointed at
  `agents_remember/worktree/` — a package that exists neither at the leaf base nor at HEAD; it is
  `agents_remember/worktrees/`. File is now 708 lines, 31 tests across 12 classes.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new worktree
  refusal/recovery suite. Verification metadata is pinned to the leaf's reformat commit until
  closeout stamps the code commit.
