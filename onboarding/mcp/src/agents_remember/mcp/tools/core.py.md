# mcp/src/agents_remember/mcp/tools/core.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `mcp/src/agents_remember/mcp/tools/core.py`    |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview      | `overview.md`                                  |

## Purpose

Server, context, install, and skills payload builders.

## Code Commentary

### Logic

Holds `ping_payload`, `server_info_payload`, `context_packet_payload`,
`runtime_install_payload`, `resolve_context_payload`, and
`skills_install_payload`. `resolve_context_payload` takes one `TaskRef`
(`agents_remember.application.task_ref`) carrying `repo_id` plus whichever locator the caller holds
— `task_name`, `contract_path`, `leaf_id`, `parent_task` — and keeps `worktree_name`/`topology` as
separate keyword arguments, since neither is part of "which task".
`ping`/`server_info` are built locally from
`SERVER_NAME`/`SERVER_VERSION`/`TRANSPORT` and config; the rest forward typed
arguments to their application entry points (`build_context_packet`, `run_runtime_install`,
`resolve_context_tool`, `skills_install_tool`). `server_info_payload` reports
`PUBLIC_TOOLS`/`RESERVED_TOOLS`. `runtime_install_payload` forwards a full
`RuntimeInstallRequest` — `dry_run`, `include_benchmarks`, `install_provider_deps`
(default `True`), and `no_cache` (default `False`) — then response-budgets the
result (S4, 2.5.1): the full install detail goes to a temp report via
`write_tool_report`, and `compact_runtime_install_payload` returns summary
counts, a rebind digest (`{attempted, ok, phases:[{phase, action, ok}]}`), the
first 5 messages plus an overflow marker, and `reportPath` (the rebind runs
were historically >50k chars inline). `skills_install_payload`
forwards `overwrite`/`archive_existing` alongside `dry_run` (the installer is a
flat copy, so there is no layout argument). `context_packet_payload` forwards
`include_providers`/`include_drift`/`include_freshness` (issue #54) into
`ContextPacketRequest`.

### Invariants And Boundaries

- Every builder returns through `base._tool_payload`.
- Imports `SERVER_NAME`/`SERVER_VERSION` via `..` and `McpRuntimeConfig` via
  `..config`.
- `runtime_install_payload`/`skills_install_payload` default `dry_run=False`
  (act-by-default), matching the server registration; `dry_run=true` previews.
- Keep the builder signatures in lockstep with the `RuntimeInstallRequest` /
  `skills_install_tool` contracts and the server registration (e.g. `no_cache`);
  the builder stays transport-thin and does not interpret these flags.

## Series-Contract Notes

`resolve_context_payload` still resolves a nested task root and a specific leaf enclosure — the
`parent_task` and `leaf_id` locators now travel inside the `TaskRef` rather than as their own
keyword arguments, through the same response-model validation path as the rest of the core payload.

## L23 Runtime Package Review

Core tool adapters now import runtime installation from `application.runtime.install` and skill
installation from `application.runtime.skills`. Payload validation and transport-thin forwarding
remain unchanged; the move removes the former flat application-module ownership.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-13T09:05+02:00 — L23 curator: reviewed the two runtime import moves and recorded their
  package ownership without claiming a tool-contract change; final provenance remains
  closeout-owned.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2: `resolve_context_payload`'s five flat locators collapsed
  into one `TaskRef` (`resolve_context_payload(config, task, *, worktree_name=None, topology=None)`),
  forwarded to `resolve_context_tool(config, task, ...)`. `RuntimeInstallRequest` is now imported
  from `agents_remember.install.runtime` (re-exported by `controllers/runtime_install.py`) rather
  than defined in the controller. `runtime_install_payload`'s own four flags are unchanged. The
  flat MCP signature callers see is unchanged — the packing happens in
  `mcp/registration/core.py`. Verification metadata pinned until closeout stamps the L2 code commit.

- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: `resolve_context_payload` now accepts and forwards `parent_task` and `leaf_id` for nested task-root and leaf-enclosure resolution. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-10T08:39+02:00: `context_packet_payload` gained the `include_freshness` forward (issue #54 freshness section).
- 2026-06-10T05:30+02:00 — `runtime_install_payload` files the full install detail via `write_tool_report` and returns `compact_runtime_install_payload`: summary counts, rebind digest `{attempted, ok, phases}`, first 5 messages + overflow marker, `reportPath` (the rebind runs were historically >50k chars).
- 2026-06-02T04:40+02:00: `skills_install_payload` dropped the `layout` argument after the installer became a single flat copy (U-01-core-skills dissolved). `l-01-session-job-lifecycle` skill series, Sub-task B/S7, mcp 1.1.0.
- 2026-05-30T21:33+02:00: Documented `runtime_install_payload` forwarding the full `RuntimeInstallRequest` including `install_provider_deps` and the new `no_cache` flag, and `skills_install_payload`'s `layout`/`overwrite`/`archive_existing` forwarding. Verified against `8927f03`.
- 2026-05-29T20:20+02:00: Recorded the act-by-default `dry_run` default on the install payload builders.
- 2026-05-29T18:35+02:00: Created from the `mcp/tools.py` domain split (commit `01f503d`).
