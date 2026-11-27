# mcp/src/agents_remember/application/runtime/install.py

## Governing Overview

[overview](overview.md)

## Purpose

`runtime/install.py` is the application entry point for the MCP
`runtime_install` operation: it composes the lower service result with the public host step, the
refresh (or, on a dry run, the read-only plan) of a running dashboard, and the inventory of running
servers with their build currentness.

## Code Commentary

### Logic

`RuntimeInstallRequest` carries the model-facing install flags
`dry_run` (default `False`), `include_benchmarks` (default `False`), and `reconcile_shared_held_stores` (default `False`), plus the run's own `experiment` selection. Its `source_root` field stays unset for MCP callers, so the tool accepts no host path overrides.

The dataclass is **defined in `agents_remember.install.runtime`** and this
module re-exports it (`__all__ = ["RuntimeInstallRequest", "open_user_settings_notice", "run_runtime_install"]`) for its
runtime application surface. `run_runtime_install(config, request)` calls the lower
service (`install_runtime_from_config(config, request)`), then calls the public host step
(`install_host(config, request.dry_run)`), sets `result["host"]` to the host part and
`result["ok"] = result["ok"] and host["ok"]`. The lower function returns its payload without a host
field: **the host-producing composition is owned here.** The application entry point therefore does not
restate the flag list. A settings file without the `paseoRuntime` block yields a host part that says so.

After the host step the entry reads the running dashboard. A dry run calls `plan_running_dashboard`,
a read-only preview that names `would-adopt`, `would-restart`, `unknown` or `failed` for an observed
dashboard; an applied install calls `ensure_running_dashboard`, which leaves an absent dashboard
stopped and otherwise adopts a dashboard already serving the installed version and source digest or
stops and restarts a mismatched one. When a dashboard is observed, its `action`, `detail` and, when
known, `pid` and `sourceDigest` are carried under `result["dashboard"]`, and a `failed` or
`lock-held` action makes `ok` false. Last, `result["runningServers"]` lists each live MCP and
dashboard server record under the coordination root's `runtime/servers/` with its observed build
currentness: a dry run calls read-only `preview_server_inventory` (leaving dead record files on disk), whereas an applied install calls `server_inventory` (removing dead process records). When `request.reconcile_shared_held_stores` is true and a `shared_held_stores` reconciler is supplied, `run_runtime_install` previews or reconciles legacy shared held-message stores, records the result under `result["sharedHeldStores"]`, and sets `ok` to false if reconciliation reports `state == "blocked"`. When the `agents-remember` repository is configured in `config.repositories`, `run_runtime_install` also attaches `result["checkoutEnvironments"] = inspect_checkout_environments(repository.path)` (read-only diagnosis of the primary checkout and active worktrees' `mcp/.venv` runtimes against the uv-managed Python 3.14 contract, without mutating any checkout).

### Invariants And Boundaries

- Keep this application entry point thin: the earlier install mechanics and the request type itself
  belong in `agents_remember.install.runtime`. This module is a re-export plus the host, dashboard
  and running-server composition, and those parts and their `ok` conjunction are owned here.
- Do not add path fields to `RuntimeInstallRequest`; keep it to typed install flags (`dry_run`, `include_benchmarks`, `experiment`). Removed-store detection reports leftover stores (`removedPartStores`) without deleting them.
- Default `dry_run` is false — the tool applies by default (act-by-default
  contract). Pass `dry_run=true` to inspect the planned reconcile before
  mutation.

## Evidence

### Repo-Internal References



- The tool maps its flags (`dry_run`, `include_benchmarks`, `experiment`) into `RuntimeInstallRequest` and hands that request unchanged to `runtime_install_payload`. [1]




- The tool declaration exposes `runtime_install` as a public tool. [2]



- The service layer defines `RuntimeInstallRequest` and performs the actual runtime install. [3]





- The application entry that composes the host step onto the lower service result, including the `ok` conjunction. [4]






- A dry run plans and an applied install refreshes a running dashboard; an observed dashboard's action is reported under `dashboard`, a `failed` or `lock-held` action fails `ok`, and the running servers are reported with their currentness. [6]



- An applied install leaves an absent dashboard stopped and otherwise ensures it serves the installed build. [7]
- The dry-run dashboard plan only observes and names the transition. [8]
