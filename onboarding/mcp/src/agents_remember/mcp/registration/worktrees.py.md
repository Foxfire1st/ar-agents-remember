# mcp/src/agents_remember/mcp/registration/worktrees.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                               |
| path                   | `mcp/src/agents_remember/mcp/registration/worktrees.py`       |
| doc_type               | `file-level-onboarding`                                       |
| lastUpdated            | 2026-08-02T01:05+02:00                                        |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d`                    |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
| governingOverview      | `overview.md`                                                 |

## Governing Overview

[registration route overview](overview.md)

## 260731-EFA-L8 Change

The tool-registration functions gained bare-`*` keyword-only signatures (the 19
PLR0917 fixes across `mcp/registration/*.py`); the rule stays enabled and call sites
already pass keywords. Registered tools are unchanged.

## Purpose

`register_worktree_tools(server, config)` declares the **working half** of a worktree-backed task:
`worktree_start`, `worktree_attach`, `worktree_status`, `worktree_sync`. The landing half
(closeout, integrate, cleanup, abandon) is a separate family in `closeout.py`.

## Code Commentary

### Logic

`worktree_start` is the widest declaration in the family and splits into the three parameter objects
its application entry point takes — who the task is, what it is cut from, and how the start runs:

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
  belong to the application entry point boundary.
- `worktree_start` and `worktree_sync` are mutating and register `dry_run=False`; `worktree_attach`
  and `worktree_status` are read-only and take no dry-run flag.
- Contract creation, git mechanics, provider setup, and lifecycle promotion live in
  `application/worktree_tools.py` and the `worktrees/` package.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The payload builders these forward to. | `worktree_start_payload`, `worktree_attach_payload`, `worktree_status_payload`, `worktree_sync_payload` | mcp/src/agents_remember/mcp/tools/worktree.py:33-43; mcp/src/agents_remember/mcp/tools/worktree.py:46-61; mcp/src/agents_remember/mcp/tools/worktree.py:64-73; mcp/src/agents_remember/mcp/tools/worktree.py:76-77 |
| `TaskIdentity`, `TaskBases`, `StartExecution`. | `TaskIdentity`, `TaskBases`, `StartExecution` | mcp/src/agents_remember/application/worktree_tools.py:40-54; mcp/src/agents_remember/application/worktree_tools.py:57-71; mcp/src/agents_remember/application/worktree_tools.py:74-82 |
| `TaskRef` — the shared task locator attach and status pack. | `TaskRef` | mcp/src/agents_remember/application/task_ref.py:14-28 |
| The three-way split and the light-task default proved through a live server. | `test_worktree_start_splits_identity_bases_and_execution`, `test_worktree_start_defaults_to_a_real_light_task_start` | mcp/tests/test_mcp_registration_wiring_tests_1.py:608-651; mcp/tests/test_mcp_registration_wiring_tests_2.py:29-46 |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the bare-`*` keyword-only signature remediation (PLR0917). Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-02T20:47+02:00 — 260731-EFA-L6 W2-B01 curator: anchored 3 citation rows; scoped citation fixing regenerated the source ranges.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the package. The four working-half
  declarations moved out of `server.py`; start now packs into `TaskIdentity`/`TaskBases`/
  `StartExecution` and attach/status into `TaskRef`. Verification metadata pinned to the pre-change
  commit until closeout stamps the L2 code commit.
