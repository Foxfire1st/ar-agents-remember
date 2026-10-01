# mcp/src/agents_remember/application/runtime/install.py

## Governing Overview

[runtime overview](overview.md)

## Purpose

`runtime/install.py` is the thin application layer for the MCP
`runtime_install` operation.

## Code Commentary

### Logic

`RuntimeInstallRequest` carries the safe model-facing install flags:
`dry_run`, `include_benchmarks`, `install_provider_deps` (default `True`), and
`no_cache` (default `False`). It does not accept host paths or provider path overrides.

The dataclass is **defined in `agents_remember.install.runtime`** and this
module re-exports it (`__all__ = ["RuntimeInstallRequest", "run_runtime_install"]`) for its
runtime application surface. `run_runtime_install(config, request)` is
now a one-line delegation — `install_runtime_from_config(config, request)` — because the service
takes the request object itself rather than four unpacked keywords. The application entry point therefore no
longer restates the flag list, which is what used to make the two definitions drift.

### Invariants And Boundaries

- Keep this application entry point thin; install mechanics **and now the request type itself** belong in
  `agents_remember.install.runtime`. This module is a re-export plus one delegation.
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
