# mcp/src/agents_remember/mcp/registration/worktrees.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                               |
| path                   | `mcp/src/agents_remember/mcp/registration/worktrees.py`       |
| doc_type               | `file-level-onboarding`                                       |
| lastUpdated            | 2026-07-31T15:31+02:00                                        |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`                    |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                                                 |

## Governing Overview

[registration route overview](overview.md)

## Purpose

`register_worktree_tools(server, config)` declares the **working half** of a worktree-backed task:
`worktree_start`, `worktree_attach`, `worktree_status`, `worktree_sync`. The landing half
(closeout, integrate, cleanup, abandon) is a separate family in `closeout.py`.

## Code Commentary

### Logic

`worktree_start` is the widest declaration in the family and splits into the three parameter objects
its controller takes — who the task is, what it is cut from, and how the start runs:

- `TaskIdentity(repo_id, task_name, worktree_name, leaf_id, parent_task, workflow_kind)` —
  `workflow_kind` defaults to `light-task` (the other value is `chat-task`).
- `TaskBases(source_branch, work_branch, memory_mode, memory_choice, stale_base_choice)`.
- `StartExecution(dry_run, skip_provider_setup, retry_provider_setup)`.

Its docstring carries two contracts that are invisible in the types. The **stale-base preflight**:
a start refuses when the source branch is behind or diverged from its remote tracking branch, and
the blocked `choose_stale_base_recovery` result is cleared by re-running with
`stale_base_choice='fast-forward'` or `'proceed-stale'`. And the **async provider setup**: start
returns within seconds with the providers block reporting `starting` plus a `progressFile`; the
caller polls `worktree_status` until a terminal state (a seed copy takes seconds, a refused seed
falls back to a full reindex flagged `seedFallback`), and re-runs with `retry_provider_setup=true`
after a failed or stale setup.

`worktree_attach` and `worktree_status` both pack their five locators into a `TaskRef` — the same
bundle `resolve_context` uses. Attach is read-only (it mutates no git) and takes `on_unsaved`
(`save` promotes an unsaved fleeting lifecycle, `discard` abandons it) to clear the save gate.
Status reports phase, dirty flags, next-step hints, and the live provider-setup block.

`worktree_sync(contract_path, memory_sync_choice, dry_run)` forwards flat. Its docstring states the
atomic base-pair advance, the mid-cycle block (the new code tip must be ledger-mapped at the
official memory tip, otherwise run carryover first), the `merge-memory` / `skip-memory` recovery,
and the sync-early doctrine.

### Invariants And Boundaries

- Flat signature, packing in the body — `TaskIdentity`/`TaskBases`/`StartExecution` and `TaskRef`
  belong to the controller boundary.
- `worktree_start` and `worktree_sync` are mutating and register `dry_run=False`; `worktree_attach`
  and `worktree_status` are read-only and take no dry-run flag.
- Contract creation, git mechanics, provider setup, and lifecycle promotion live in
  `controllers/worktree_tools.py` and the `worktrees/` package.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The payload builders these forward to. | [tools/worktree.py](agents-remember/mcp/src/agents_remember/mcp/tools/worktree.py) |
| `TaskIdentity`, `TaskBases`, `StartExecution`. | [controllers/worktree_tools.py](agents-remember/mcp/src/agents_remember/controllers/worktree_tools.py) |
| `TaskRef` — the shared task locator attach and status pack. | [controllers/task_ref.py](agents-remember/mcp/src/agents_remember/controllers/task_ref.py) |
| The three-way split and the light-task default proved through a live server. | [test_mcp_registration_wiring.py](agents-remember/mcp/tests/test_mcp_registration_wiring.py) |

## Update History

- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the package. The four working-half
  declarations moved out of `server.py`; start now packs into `TaskIdentity`/`TaskBases`/
  `StartExecution` and attach/status into `TaskRef`. Verification metadata pinned to the pre-change
  commit until closeout stamps the L2 code commit.
