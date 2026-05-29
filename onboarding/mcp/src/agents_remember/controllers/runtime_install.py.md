# mcp/src/agents_remember/controllers/runtime_install.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/controllers/runtime_install.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T00:37+02:00                     |
| lastVerifiedCommitHash | `23f4d7681f7fcd729049c5f27878c84bbb8f8e58` |
| lastVerifiedCommitDate | 2026-05-29T20:24:00+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`runtime_install.py` is the thin controller layer for the MCP
`runtime_install` operation.

## Code Commentary

### Logic

`RuntimeInstallRequest` carries the safe model-facing install flags:
`dry_run`, `include_benchmarks`, and `install_provider_deps`.
`run_runtime_install()` delegates to `install_runtime_from_config()` with the
trusted `McpRuntimeConfig`. It does not accept host paths or provider path
overrides.

### Invariants And Boundaries

- Keep this controller thin; install mechanics belong in
  `agents_remember.install.runtime`.
- Do not add path fields to `RuntimeInstallRequest`.
- Default `dry_run` is false — the tool applies by default (act-by-default
  contract). Pass `dry_run=true` to inspect the planned reconcile before
  mutation; the packaged install skills tell the agent to preview first.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| MCP tool payload construction maps tool booleans into `RuntimeInstallRequest`. | [tools.py](agents-remember-md/mcp/src/agents_remember/mcp/tools.py) |
| Server registration exposes `runtime_install` as a public tool. | [server.py](agents-remember-md/mcp/src/agents_remember/mcp/server.py) |
| The service layer performs the actual runtime install. | [runtime.py](agents-remember-md/mcp/src/agents_remember/install/runtime.py) |

## Update History

- 2026-05-24T00:37+02:00: Refreshed verification after MCP command capture callers moved to service-backed controllers; the runtime install controller contract stayed unchanged.
- 2026-05-23T04:29+02:00: Created for the MCP runtime install tool controller.
