# mcp/tests/test_worktree_and_observer_helpers.py

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `mcp/tests/test_worktree_and_observer_helpers.py`  |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated | 2026-08-26T18:38+02:00 |
| lastVerifiedCommitHash | `c51373425be3e3f488590ad2f444810df89b4ffb` |
| lastVerifiedCommitDate | 2026-08-26T19:22:10+02:00|
| governingOverview      | `overview.md`                                      |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Behavioural cover for worktree and observer helpers **that only had happy-path use**. Every
test asserts the value returned, the file that moved, or the error raised — never merely
that a line ran.

## Code Commentary

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
| `RouteOverviewMetadataRefreshPlanTests` | Route planning, stamping, and classification — source-matched and baseline-relative task-edited overviews, external-overview revision limits, metadata-only refusal, and the narrowly generated citation-coordinate exception. |
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

The external-memory parent-series fixture now commits a canonical `memory.md` row mapping the
exact code super tip before admission. Existing-series adoption also creates the recorded
integration ref first and asserts that adoption retains it; adoption proves an existing contract
and branch pair and never invents the missing ref as a fallback.

## Invariants And Boundaries

- "Already gone" and "failed" are distinct outcomes for every removal helper; collapsing
  them would hide a real failure behind an idempotent-looking success.
- Branch deletion is refusal-first: unmerged work is never lost silently, and the refusal
  carries its reason.
- Archival is idempotent — a second call must not move anything.
- A route overview edited since the verified memory baseline is required even
  when the current leaf code paths are unrelated; a metadata-only edit is still
  classified stale rather than accepted as review.
- The same baseline-relative plan feeds metadata refresh: the unrelated-code
  fixture proves its task-edited overview receives the supplied verified commit
  hash and date rather than only appearing in preview.
- A source-matched overview outside the supplied memory Git tree remains a
  required refresh target. Because its prior memory revision cannot be read
  from that unrelated tree, body classification emits no fabricated stale,
  untraced, attested, or unstamped-review bucket for it.
- A task-edited overview whose only meaningful-body delta is the sanctioned
  final reference-cell `path:line[-line]` coordinate may pass without invented
  history; the fixture keeps claim, anchor, path, and table shape unchanged.
- No container runtime and no network; git and the filesystem are real.
- External-memory success fixtures carry an exact code-to-memory ledger mapping, and existing
  series adoption supplies the branch whose authority production validates.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The application provider-runtime teardown helpers under test are `_docker_rm_f` / `_docker_network_rm` (moved from worktrees by L9). | "def _docker_rm_f"; "def _docker_network_rm" | mcp/src/agents_remember/application/provider_runtime.py:254-254; mcp/src/agents_remember/application/provider_runtime.py:269-269 |
| The cleanup helper under test is capability-bound `delete_branch_if_merged`. | "def delete_branch_if_merged(" | mcp/src/agents_remember/worktrees/modules/cleanup.py:188-210 |
| The onboarding helper under test is `route_overview_metadata_refresh_plan_for_context`. | "def route_overview_metadata_refresh_plan_for_context" | mcp/src/agents_remember/worktrees/modules/onboarding.py:125-125 |
| The start-contract helper under test is `_parent_series_contract`. | "def _parent_series_contract" | mcp/src/agents_remember/worktrees/modules/startup/start_contract.py:865-865 |
| The task-resolver helpers under test are `archive_completed_root_task` and `series_contract_path`. | "def archive_completed_root_task"; "def series_contract_path" | mcp/src/agents_remember/worktrees/task_resolver.py:47-47; mcp/src/agents_remember/worktrees/task_resolver.py:147-147 |
| The observer helpers under test: `_inspect_containers` and `_inspect_containers_individually`. Both modules import `run_command`/`docker_command` at module level, so the tests patch `snapshots.run_command` and `provider_teardown.run_command` separately — patching one does not cover the other. | `_inspect_containers`; `_inspect_containers_individually` | mcp/src/agents_remember/serving/projections/snapshots.py:353-375; mcp/src/agents_remember/serving/projections/snapshots.py:378-401 |
| The lifecycle suites whose happy paths these arms complete. | `WorktreeSupportTests`; `ContractMemoryModeTests` | mcp/tests/test_worktree_edge_paths.py:123-192; mcp/tests/test_worktree_support.py:767-842 |

## Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned helper suite.

| Finding | Anchor | Source |
| --- | --- | --- |

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## Update History

- 2026-08-26T18:38+02:00 — Citation-only repair: the bootstrap preflight mutex moved
  `_parent_series_contract` seven lines; repointed its exact source anchor without changing the
  documented helper behavior. Verification remains closeout-owned.

- 2026-08-26T08:45+02:00 — Restored the canonical commentary and Docs/Cross-Repo reference section
  shape for this changed helper suite card.

- 2026-08-26T08:15+02:00 — Reconciled parent-series fixtures with paired-source admission: seed
  the canonical external-memory ledger and pre-create the exact integration ref before adoption.
  Verification metadata remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: citation-only repair repointed moved lifecycle, tool-model, direct-landing, legacy, or startup evidence to its canonical committed source path; this card's own documented behavior is unchanged.

- 2026-08-19T22:32+02:00 — No content impact: 260815-DAG-L13 narrowed parent-series contract assertions with isinstance after the lane-blocked result union; documented helper behavior is unchanged. Also re-pointed the `_parent_series_contract` citation to `start_contract.py:850-850` after the same leaf moved the function. Verification remains closeout-owned.

- 2026-08-19T04:20+02:00 — No content impact: 260815-DAG-L10 moved `_parent_series_contract` three lines down in `start_contract.py`; re-pointed the citation to `start_contract.py:778-778`. The documented helper behavior is unchanged.

- 2026-08-17T12:30+02:00 — No content impact: L5 helper-signature alignment only; the documented behavior is unchanged.

- 2026-08-16T04:06+02:00 — Dagger fixture repair: parent-series adoption cases use the task-derived sprint super as their source rather than repository default.
- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.
- 2026-08-14T06:40+02:00 — L23 final candidate review: helper tests pin task-addressed operation
  projection and lineage guidance while keeping recovery identity plane-private.
- 2026-08-12T23:27+02:00 — 260731-EFA-L23 Dagger diff-coverage follow-up: added the external-overview boundary case. A source-matched route outside the supplied memory Git tree remains required, while absence of comparable memory revision evidence yields no false body-review classification. The owner reports the focused test passing, exact four-branch coverage restored, and exact-file Ruff clean. Verification remains closeout-owned.
- 2026-08-12T22:45+02:00 — 260731-EFA-L23 curator follow-up: added the third baseline-relative case, proving a generated citation-coordinate-only route edit clears classification without invented history while the existing metadata-only refusal remains intact; the substantively edited case also proves the planned route receives the supplied verification hash/date during refresh. The owner reports 10/10 focused plan tests and 16/16 combined route-overview tests green. Verification remains closeout-owned.
- 2026-08-12T22:25+02:00 — 260731-EFA-L23 curator follow-up: documented the two new baseline-relative route-overview cases. One proves a substantively edited overview enters the plan despite unrelated current-leaf code; the other proves a metadata-only edit remains `stale`. The owner reports all eight focused route-plan tests green with xdist auto. Verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-04T00:22:04+02:00 — 260731-EFA-L6 S18-B05 curator: repaired and normalised mechanical citation findings with current source anchors and fixer-generated ranges; no semantic claim changes. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T09:38+02:00 — 260731-EFA-L4 curator: `ParentSeriesContractTests` moved both its
  fixtures from `workflow_kind="master-task"` to `"light-task"`, because `WorkflowKind` is now
  `Literal["chat-task", "light-task"]` (cit:(["WorkflowKind = Literal["], mcp/src/agents_remember/models/worktree.py:20-20)). The Classes-table
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
