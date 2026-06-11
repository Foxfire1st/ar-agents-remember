# mcp/src/agents_remember/controllers/runtime_install.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/controllers/runtime_install.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-30T21:33+02:00                     |
| lastVerifiedCommitHash | `8927f038535bdb514526156df72603708bc89e19` |
| lastVerifiedCommitDate | 2026-05-30T19:59:15+02:00|
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
`no_cache` (default `False`). `run_runtime_install()` delegates to
`install_runtime_from_config()` with the trusted `McpRuntimeConfig`, forwarding
all four flags. It does not accept host paths or provider path overrides.

### Invariants And Boundaries

- Keep this controller thin; install mechanics belong in
  `agents_remember.install.runtime`.
- Do not add path fields to `RuntimeInstallRequest`; keep it to typed install
  booleans (`no_cache` forces a from-scratch provider image rebuild downstream).
- Default `dry_run` is false — the tool applies by default (act-by-default
  contract). Pass `dry_run=true` to inspect the planned reconcile before
  mutation; the packaged install skills tell the agent to preview first.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| MCP tool payload construction maps tool booleans into `RuntimeInstallRequest`. | [tools/core.py](agents-remember/mcp/src/agents_remember/mcp/tools/core.py) |
| Server registration exposes `runtime_install` as a public tool. | [server.py](agents-remember/mcp/src/agents_remember/mcp/server.py) |
| The service layer performs the actual runtime install. | [runtime.py](agents-remember/mcp/src/agents_remember/install/runtime.py) |

## Update History

- 2026-05-30T21:33+02:00: Added the `no_cache` flag to `RuntimeInstallRequest` (forwarded to `install_runtime_from_config`) and repaired the builder reference — `runtime_install_payload` now lives in `tools/core.py` after the `01f503d` `mcp/tools.py` split. Verified against `8927f03`.
- 2026-05-24T00:37+02:00: Refreshed verification after MCP command capture callers moved to service-backed controllers; the runtime install controller contract stayed unchanged.
- 2026-05-23T04:29+02:00: Created for the MCP runtime install tool controller.
