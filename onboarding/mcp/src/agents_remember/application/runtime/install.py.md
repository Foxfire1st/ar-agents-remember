# mcp/src/agents_remember/application/runtime/install.py

## Governing Overview

[runtime overview](overview.md)

## Purpose

`runtime/install.py` is the application entry point for the MCP
`runtime_install` operation: it composes the lower service result with the public host step.

## Code Commentary

### Logic

`RuntimeInstallRequest` carries the safe model-facing install flags:
`dry_run`, `include_benchmarks`, `install_provider_deps` (default `True`), and
`no_cache` (default `False`). It does not accept host paths or provider path overrides.

The dataclass is **defined in `agents_remember.install.runtime`** and this
module re-exports it (`__all__ = ["RuntimeInstallRequest", "run_runtime_install"]`) for its
runtime application surface. `run_runtime_install(config, request)` calls the lower
service (`install_runtime_from_config(config, request)`), then calls the public host step
(`install_host(config, request.dry_run)`), sets `result["host"]` to the host part and
`result["ok"] = result["ok"] and host["ok"]`. The lower function returns its payload without a host
field: **the host-producing composition is owned here.** The application entry point therefore does not
restate the flag list, which is what used to make the two definitions drift.

### Invariants And Boundaries

- Keep this application entry point thin: the earlier install mechanics and the request type itself
  belong in `agents_remember.install.runtime`. This module is a re-export plus the host-step
  composition, and the host part and its `ok` conjunction are owned here.
- Do not add path fields to `RuntimeInstallRequest`; keep it to typed install
  booleans (`no_cache` forces a from-scratch provider image rebuild downstream).
- Default `dry_run` is false — the tool applies by default (act-by-default
  contract). Pass `dry_run=true` to inspect the planned reconcile before
  mutation; the packaged install skills tell the agent to preview first.

## Evidence

### Repo-Internal References

- MCP tool payload construction maps tool booleans into `RuntimeInstallRequest`. [1]
- The tool declaration exposes `runtime_install` as a public tool. [2]
- The service layer defines `RuntimeInstallRequest` and performs the actual runtime install. [3]

## 260928-MIK-L96 The host step

`run_runtime_install` now composes exactly one host step after the steps it had: `install_host` reads the shared host block at call time, provisions or previews it, and its report is carried under the result's `host` part while `ok` is the conjunction of both. A settings file without the block yields the host part that says so.

- The application entry that composes the host step onto the lower service result, including the `ok` conjunction. [4]
