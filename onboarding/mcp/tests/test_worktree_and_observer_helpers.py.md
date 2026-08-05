# mcp/tests/test_worktree_and_observer_helpers.py

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `mcp/tests/test_worktree_and_observer_helpers.py`  |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-08-01T09:38+02:00                             |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`         |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                                      |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Behavioural cover for worktree and observer helpers **that only had happy-path use**. Every
test asserts the value returned, the file that moved, or the error raised — never merely
that a line ran.

## Method

The docker-facing helpers are exercised through their own module-level
`run_command` / `docker_command` seam, so **no container runtime is ever contacted**;
`_StubRunner` replays canned results (or raises them) and records every call. The git- and
filesystem-facing helpers run against **real throwaway repositories and directory trees**,
as the rest of the worktree suite does. Docker inspect payloads carry docker's leading-slash
container names, which is what the name-matching under test has to cope with.

## Classes

| Class | Helper |
| --- | --- |
| `InspectContainersTests` | `_inspect_containers` — batch inspect, with per-name fallback and hard-failure `None`s. |
| `InspectContainersIndividuallyTests` | `_inspect_containers_individually` — per-name results, aborting on runtime failure. |
| `DockerRemoveHelpersTests` | `_docker_rm_f` / `_docker_network_rm` — dry run, success, already-gone, failure. |
| `DeleteBranchIfMergedTests` | `delete_branch_if_merged` — **refuses to lose unmerged work, and says why.** |
| `RouteOverviewMetadataRefreshPlanTests` | `route_overview_metadata_refresh_plan_for_context` — which overviews a change implicates. |
| `ArchiveCompletedRootTaskTests` | `archive_completed_root_task` — only finished root tasks move, and only once. |
| `ParentSeriesContractTests` | `_parent_series_contract` — adopt an existing series, or mint one for a master task. |

"Master task" in that last row means the **task document's** `**Type:** Master`, read off the
`task.md` the fixture writes — not a workflow kind. The `WorktreeArgs` these tests pass carry
`workflow_kind="light-task"`, because `WorkflowKind` is `Literal["chat-task", "light-task"]` and
has no master member, and `test_master_task_mints_the_series_contract_and_integration_branch`
still mints the `kind="series"` contract, the `ar/<task>` integration branch and the
`series-contract.md` file. So the suite now demonstrates the separation rather than assuming it:
series-ness comes from the task artifact, and the workflow kind travels beside it without
deciding anything.

## Invariants And Boundaries

- "Already gone" and "failed" are distinct outcomes for every removal helper; collapsing
  them would hide a real failure behind an idempotent-looking success.
- Branch deletion is refusal-first: unmerged work is never lost silently, and the refusal
  carries its reason.
- Archival is idempotent — a second call must not move anything.
- No container runtime and no network; git and the filesystem are real.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The worktree provider-teardown helpers under test are `_docker_rm_f` / `_docker_network_rm`. | "def _docker_rm_f"; "def _docker_network_rm" | mcp/src/agents_remember/worktrees/modules/provider_teardown.py:120-120; mcp/src/agents_remember/worktrees/modules/provider_teardown.py:135-135 |
| The cleanup helper under test is `delete_branch_if_merged`. | "def delete_branch_if_merged(repo: Path, branch: str, dry_run: bool) -> dict[str, object]:" | mcp/src/agents_remember/worktrees/modules/cleanup.py:64-64 |
| The onboarding helper under test is `route_overview_metadata_refresh_plan_for_context`. | "def route_overview_metadata_refresh_plan_for_context" | mcp/src/agents_remember/worktrees/modules/onboarding.py:123-123 |
| The start-contract helper under test is `_parent_series_contract`. | "def _parent_series_contract" | mcp/src/agents_remember/worktrees/modules/start_contract.py:117-117 |
| The task-resolver helpers under test are `archive_completed_root_task` and `series_contract_path`. | "def archive_completed_root_task"; "def series_contract_path" | mcp/src/agents_remember/worktrees/task_resolver.py:47-47; mcp/src/agents_remember/worktrees/task_resolver.py:147-147 |
| The observer helpers under test: `_inspect_containers` and `_inspect_containers_individually`. Both modules import `run_command`/`docker_command` at module level, so the tests patch `snapshots.run_command` and `provider_teardown.run_command` separately — patching one does not cover the other. | `_inspect_containers`; `_inspect_containers_individually` | mcp/src/agents_remember/observer/snapshots.py:370-392; mcp/src/agents_remember/observer/snapshots.py:395-418 |
| The lifecycle suites whose happy paths these arms complete. | `WorktreeSupportTests`; `ContractMemoryModeTests` | mcp/tests/test_worktree_edge_paths.py:95-164; mcp/tests/test_worktree_support.py:573-3091 |

## Update History

- 2026-08-04T00:22:04+02:00 — 260731-EFA-L6 S18-B05 curator: repaired and normalised mechanical citation findings with current source anchors and fixer-generated ranges; no semantic claim changes. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T09:38+02:00 — 260731-EFA-L4 curator: `ParentSeriesContractTests` moved both its
  fixtures from `workflow_kind="master-task"` to `"light-task"`, because `WorkflowKind` is now
  `Literal["chat-task", "light-task"]` (cit:([`WorkflowKind`], mcp/src/agents_remember/worktrees/worktree_contract.py:63-63)). The Classes-table
  claim "mint one for a master task" survives, and the note added under the table says why it is
  now a demonstration rather than a coincidence: `_parent_series_contract` reads `**Type:** Master`
  off the `task.md` the fixture writes, so with the workflow kind no longer able to say "master",
  `test_master_task_mints_the_series_contract_and_integration_branch` still produces the
  `kind="series"` contract, the `ar/<task>` branch and the `series-contract.md`.
  Repaired both Repo-Internal reference rows, which pointed at a package that does not exist and
  never did: `agents_remember/worktree/` — the package is `agents_remember/worktrees/` (checked
  against the tree at both the leaf base and HEAD). Replaced the two vague directory rows with the
  modules the imports actually name — `modules/provider_teardown.py`, `modules/cleanup.py` (L43
  `delete_branch_if_merged`), `modules/onboarding.py` (L123
  `route_overview_metadata_refresh_plan_for_context` — the "route-overview helper" was filed under
  `observer/`, where it does not live), `modules/start_contract.py`, `task_resolver.py` (L147
  `archive_completed_root_task`), and `observer/snapshots.py` (L377/L402 for the two inspect
  helpers). Verified the suite is unchanged otherwise: 47 tests across the 7 documented classes
  plus `_StubRunner`, no test added, removed or renamed.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new worktree /
  observer helper suite. Verification metadata is pinned to the leaf's reformat commit until
  closeout stamps the code commit.
