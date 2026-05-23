# mcp/src/agents_remember/providers/settings.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/settings.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T00:37+02:00                     |
| lastVerifiedCommitHash | `ddf6fcd5981664813c915e94e1c5229b542a28a4` |
| lastVerifiedCommitDate | 2026-05-24T00:25:39+02:00                 |
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`settings.py` converts trusted MCP runtime settings into the temporary provider
lifecycle settings consumed by package-local provider lifecycle code.

## Code Commentary

### Logic

`lifecycle_settings_from_config()` builds a `contextProviders` object from
`McpRuntimeConfig.providers` and `McpRuntimeConfig.repositories`. GrepAI roots
are derived from configured memory roots, falling back to the coordinator
`memory-repos` root when no repository memory roots are configured; CGC roots
are derived from configured code repository paths. The generated settings
include concrete provider runtime roots under `providers/runners`, backend data
roots under `providers/data`, log roots under `providers/logs`, installed
requirement paths, Docker backend image metadata, and watcher log paths.

`write_lifecycle_settings()` writes that generated object to a temporary JSON
file for lower-level lifecycle functions that already accept `--from-settings`.

### Invariants And Boundaries

- Do not read coordinator `system/settings.json` here.
- Do not accept provider path overrides from MCP settings; paths are derived by
  the server.
- Keep generated settings complete enough for dry-run and real install paths,
  including backend images and image lock paths.
- Delete temporary settings files in the caller after lifecycle operations
  finish.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| MCP config derives allowed repositories/providers and provider runtime roots from trusted settings. | [config.py](agents-remember-md/mcp/src/agents_remember/mcp/config.py) |
| Provider status writes generated lifecycle settings before calling `watchers_run`. | [status.py](agents-remember-md/mcp/src/agents_remember/providers/status.py) |
| Runtime install uses generated lifecycle settings when installing provider dependencies from the MCP tool. | [runtime.py](agents-remember-md/mcp/src/agents_remember/install/runtime.py) |

## Update History

- 2026-05-24T00:37+02:00: Refreshed verification and clarified the GrepAI fallback root used when no repository memory root is configured.
- 2026-05-23T04:29+02:00: Created when MCP provider lifecycle settings moved out of coordinator `system/settings.json`.
