# mcp/tests/test_worktree_and_observer_helpers.py

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `mcp/tests/test_worktree_and_observer_helpers.py`  |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-07-31T15:32+02:00                             |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`         |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
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

## Invariants And Boundaries

- "Already gone" and "failed" are distinct outcomes for every removal helper; collapsing
  them would hide a real failure behind an idempotent-looking success.
- Branch deletion is refusal-first: unmerged work is never lost silently, and the refusal
  carries its reason.
- Archival is idempotent — a second call must not move anything.
- No container runtime and no network; git and the filesystem are real.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The worktree lifecycle helpers under test. | [worktree/](agents-remember/mcp/src/agents_remember/worktree/) |
| The observer/route-overview helpers under test. | [observer/](agents-remember/mcp/src/agents_remember/observer/) |
| The lifecycle suites whose happy paths these arms complete. | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py), [test_worktree_edge_paths.py](agents-remember/mcp/tests/test_worktree_edge_paths.py) |

## Update History

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new worktree /
  observer helper suite. Verification metadata is pinned to the leaf's reformat commit until
  closeout stamps the code commit.
