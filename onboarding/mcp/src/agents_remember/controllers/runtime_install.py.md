# mcp/src/agents_remember/controllers/runtime_install.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/controllers/runtime_install.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T15:31+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`runtime_install.py` is the thin controller layer for the MCP
`runtime_install` operation.

## Code Commentary

### Logic

`RuntimeInstallRequest` carries the safe model-facing install flags:
`dry_run`, `include_benchmarks`, `install_provider_deps` (default `True`), and
`no_cache` (default `False`). It does not accept host paths or provider path overrides.

Since 260731-EFA-L2 the dataclass is **defined in `agents_remember.install.runtime`** and this
module re-exports it (`__all__ = ["RuntimeInstallRequest", "run_runtime_install"]`) so existing
imports from `controllers.runtime_install` keep working. `run_runtime_install(config, request)` is
now a one-line delegation — `install_runtime_from_config(config, request)` — because the service
takes the request object itself rather than four unpacked keywords. The controller therefore no
longer restates the flag list, which is what used to make the two definitions drift.

### Invariants And Boundaries

- Keep this controller thin; install mechanics **and now the request type itself** belong in
  `agents_remember.install.runtime`. This module is a re-export plus one delegation.
- Do not add path fields to `RuntimeInstallRequest`; keep it to typed install
  booleans (`no_cache` forces a from-scratch provider image rebuild downstream).
- Default `dry_run` is false — the tool applies by default (act-by-default
  contract). Pass `dry_run=true` to inspect the planned reconcile before
  mutation; the packaged install skills tell the agent to preview first.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| MCP tool payload construction maps tool booleans into `RuntimeInstallRequest`. | [tools/core.py](agents-remember/mcp/src/agents_remember/mcp/tools/core.py) |
| The tool declaration exposes `runtime_install` as a public tool. | [registration/core.py](agents-remember/mcp/src/agents_remember/mcp/registration/core.py) |
| The service layer defines `RuntimeInstallRequest` and performs the actual runtime install. | [runtime.py](agents-remember/mcp/src/agents_remember/install/runtime.py) |

## Update History

- 2026-07-31T15:31+02:00 — 260731-EFA-L2: `RuntimeInstallRequest`'s definition moved to
  `agents_remember.install.runtime` and this module re-exports it; `run_runtime_install` became a
  single delegation passing the request object through. Corrected the stale reference to `server.py`
  — tool registration now lives in `mcp/registration/core.py`. Verification metadata pinned until
  closeout stamps the L2 code commit.

- 2026-05-30T21:33+02:00: Added the `no_cache` flag to `RuntimeInstallRequest` (forwarded to `install_runtime_from_config`) and repaired the builder reference — `runtime_install_payload` now lives in `tools/core.py` after the `01f503d` `mcp/tools.py` split. Verified against `8927f03`.
- 2026-05-24T00:37+02:00: Refreshed verification after MCP command capture callers moved to service-backed controllers; the runtime install controller contract stayed unchanged.
- 2026-05-23T04:29+02:00: Created for the MCP runtime install tool controller.
