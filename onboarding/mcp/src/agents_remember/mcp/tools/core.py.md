# mcp/src/agents_remember/mcp/tools/core.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Server, context, install, and skills payload builders.

Builds server-info and orientation/install tool payloads through the shared token envelope.

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
`PUBLIC_TOOLS`/`RESERVED_TOOLS` plus the caller-supplied, boot-resolved `ServingBuildPayload`. The
payload builder serializes that strict model directly and never reprobes or fabricates build
identity. **Since 260915-CAPS-L9 `runtime_install_payload(config, request)` takes the run's own
`RuntimeInstallRequest` unchanged** — the tool builds the request and hands it over, so the knobs
the tool exposes and the fields the application entry point reads cannot drift apart. That is
what makes `request.experiment` this run's own selection input: the tool's `experiment` parameter
supplies it, the `AR_EXPERIMENT` environment variable of the server process is the documented
fallback for a short-lived CLI/developer run, and the install payload names which one supplied
the mode in its record's `selectionSource`, so a long-lived server cannot leave an ambient switch
behind unnoticed. The `write_tool_report` label follows `request.dry_run`. The builder then
response-budgets the
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
- `server_info_payload` requires an explicit `ServingBuildPayload`; package version alone cannot identify
  equal-version source or installed candidates.

### Role Runtime and Scope

server_info_payload adds toolServer and AgentBindingPayload only for readable bound identity; servingBuild remains the process/build owner fact. context_packet_payload derives optional call-local admitted config before invoking the existing context packet owner. No binding creates a second globally selected repository root.

## Series-Contract Notes

`resolve_context_payload` still resolves a nested task root and a specific leaf enclosure — the
`parent_task` and `leaf_id` locators now travel inside the `TaskRef` rather than as their own
keyword arguments, through the same response-model validation path as the rest of the core payload.

## L23 Runtime Package Review

Core tool adapters now import runtime installation from `application.runtime.install` and skill
installation from `application.runtime.skills`. Payload validation and transport-thin forwarding
remain unchanged; the move removes the former flat application-module ownership.

## Evidence



### Runtime Source References

- Frozen implementation of server_info_payload supporting the stated file behavior. [1]
- Frozen implementation of context_packet_payload supporting the stated file behavior. [2]
