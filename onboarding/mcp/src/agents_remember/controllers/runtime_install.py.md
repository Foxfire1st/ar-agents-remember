# mcp/src/agents_remember/controllers/runtime_install.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/controllers/runtime_install.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T04:29+02:00                     |
| lastVerifiedCommitHash | `7ab4b520b9178a31c4a5f5f8a5393b9b6ba82e0e` |
| lastVerifiedCommitDate | 2026-05-22T21:20:47+02:00                 |
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
- Default `dry_run` stays true so the tool is inspectable before mutation.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| MCP tool payload construction maps tool booleans into `RuntimeInstallRequest`. | [tools.py](agents-remember-md/mcp/src/agents_remember/mcp/tools.py) |
| Server registration exposes `runtime_install` as a public tool. | [server.py](agents-remember-md/mcp/src/agents_remember/mcp/server.py) |
| The service layer performs the actual runtime install. | [runtime.py](agents-remember-md/mcp/src/agents_remember/install/runtime.py) |

## Update History

- 2026-05-23T04:29+02:00: Created for the MCP runtime install tool controller.
