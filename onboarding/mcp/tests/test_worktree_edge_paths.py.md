# mcp/tests/test_worktree_edge_paths.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_worktree_edge_paths.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-12T22:36+02:00                     |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d` |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
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
| `OverviewRevisionTests` | Which route overviews the closeout classifier can speak for at all, including its three-value revision result and typed evidence boundary. |
| `IntegrationRefusalTests` | Integration refuses **before it moves any branch**. |

## Two Refusals Worth Reading Together

`ContractMemoryModeTests` proves both halves of the vocabulary refusal, and the second half is
the one that is easy to lose. `test_leaf_contract_refuses_an_unknown_memory_mode` and its series
twin prove `default_contract` / `default_series_contract` **raise** `ContractError`;
cit:([`test_a_refused_request_leaves_the_start_as_a_result_not_an_exception`], mcp/tests/test_worktree_edge_paths.py:168-189) then proves
`build_start_contract` converts that raise into a `WorktreeCommandResult(2, {"state":
"invalid-request", ...})` whose summary still carries the message. Its docstring states the reason
the conversion is load-bearing: nothing on `worktree_start`'s path — not
`mcp/registration/worktrees.py`, not `application/worktree_tools.py`, not `mcp/tools/worktree.py` —
catches `ContractError`, so an escaping raise would surface as a traceback instead of a blocked
result the agent can read and correct. It patches `start_contract_module._build_start_contract`
with a `side_effect`, since the refusal is the subject and reaching it for real would mean standing
up a git repository to test an argument check. The production half is `build_start_contract`'s
`except ContractError -> invalid_contract_request_result` cit:([`build_start_contract`], mcp/src/agents_remember/worktrees/modules/start_contract.py:192-211) and cit:([`invalid_contract_request_result`], mcp/src/agents_remember/worktrees/modules/leaf_ref_start.py:38-53).

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
- Overview revision exposes body-change, added-history, and citation-only facts
  together; ordinary new prose is explicitly not citation-only. Bucket probes use
  the typed `source` evidence value, while absent/outside-baseline overviews still
  drop out rather than becoming false gates.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The construction refusal rejects unknown workflow and memory values through `_task_vocabulary`. | `_task_vocabulary` | mcp/src/agents_remember/worktrees/worktree_contract.py:161-178 |
| `WorkflowKind` limits workflow selection to `chat-task` and `light-task` (declared in models/worktree.py since L9). | "WorkflowKind = Literal[" | mcp/src/agents_remember/models/worktree.py:14-14 |
| `build_start_contract` catches `ContractError` and `LeafRefResolutionError` so neither leaves the tool handler. | `build_start_contract` | mcp/src/agents_remember/worktrees/modules/start_contract.py:192-211 |
| `_contract_after_memory_start` is the memory-disabled/reconciled recovery. | `_contract_after_memory_start` | mcp/src/agents_remember/worktrees/modules/start.py:136-160 |
| `invalid_contract_request_result` returns the `exit 2` / `state: invalid-request` payload for a refusal. | `invalid_contract_request_result` | mcp/src/agents_remember/worktrees/modules/leaf_ref_start.py:38-53 |
| The happy-path lifecycle suites these guards sit beside. | `WorktreeSupportTests`; `WorktreeSyncTests`; `ContractLifecycleAnchorTests` | mcp/tests/test_worktree_contract_lifecycle.py:51-81; mcp/tests/test_worktree_support.py:539-614; mcp/tests/test_worktree_sync.py:111-244 |
| Helper-level arms of the same lifecycle. | `InspectContainersTests`; `InspectContainersIndividuallyTests`; `DockerRemoveHelpersTests`; `RouteOverviewMetadataRefreshPlanTests` | mcp/tests/test_worktree_and_observer_helpers.py:93-180; mcp/tests/test_worktree_and_observer_helpers.py:183-231; mcp/tests/test_worktree_and_observer_helpers.py:234-348; mcp/tests/test_worktree_and_observer_helpers.py:421-526 |

## L23 Status And Attach Edges

Existing-contract coverage now pins stale-lineage refusal before reattach,
attach refusal before stale context resumes, status projection of blocked
lineage, and omission when no task edge applies. Older preflight tests mark
lineage non-applicable so their stale-base/rebuild branches retain isolated
ownership.

## Update History
- 2026-08-12T22:36+02:00 — L23 pre-commit type-check curator follow-up: updated `OverviewRevisionTests` for the three-value revision result (`citation_only=False` on ordinary prose) and the typed `evidence="source"` bucket call. The owner reports 14/14 combined route/overview tests and repository-wide Pyright green. Verification remains closeout-owned.
- 2026-08-12T20:10+02:00 — L23 curator: documented lineage status/attach edge coverage, including no-applicable-edge omission; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.
- 2026-08-04T13:47:55+02:00 — 260731-EFA-L6 S18-B11 same-reviewer correction: split task-vocabulary and WorkflowKind ownership, extended the start-contract exception claim, and removed hidden line-number shorthand from result claims. Verification metadata unchanged.

- 2026-08-03T03:56+02:00 — 260731-EFA-L6 W3-B10 curator: anchored 4 table citations and 1 prose citation; no unresolved Tier-3 claims.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T09:46+02:00 — 260731-EFA-L4 curator: the suite grew by 95 lines and the card's
  Classes table had gone from complete to eleven-of-twelve. Added the missing class,
  `MemoryDisabledStartTests` (L285-L353, three tests over
  `start_module._contract_after_memory_start`), and extended the `ContractMemoryModeTests` row for
  its fourth test, `test_a_refused_request_leaves_the_start_as_a_result_not_an_exception`
  cit:([`test_a_refused_request_leaves_the_start_as_a_result_not_an_exception`], mcp/tests/test_worktree_edge_paths.py:168-189). Wrote both up in a new section, because between them they are the leaf's real
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

- 2026-08-01T09:46+02:00 — 260731-EFA-L4 curator: the suite grew by 95 lines and the card's
  Classes table had gone from complete to eleven-of-twelve. Added the missing class,
  `MemoryDisabledStartTests` (L285-L353, three tests over
  `start_module._contract_after_memory_start`), and extended the `ContractMemoryModeTests` row for
  its fourth test, `test_a_refused_request_leaves_the_start_as_a_result_not_an_exception`
  cit:([`test_a_refused_request_leaves_the_start_as_a_result_not_an_exception`], mcp/tests/test_worktree_edge_paths.py:168-189). Wrote both up in a new section, because between them they are the leaf's real
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
