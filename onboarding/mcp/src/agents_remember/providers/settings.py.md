# mcp/src/agents_remember/providers/settings.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/settings.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T17:40+02:00                     |
| lastVerifiedCommitHash | `ae9c4e5b6af38eda7f2b29006130c4263e9db62f` |
| lastVerifiedCommitDate | 2026-05-25T19:55:09+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`settings.py` converts trusted MCP runtime settings into the temporary provider
lifecycle settings consumed by package-local provider lifecycle code. For
`grepai-memory`, those generated settings now describe a self-contained Docker
stack rather than a host GrepAI binary plus externally managed Ollama.

## Code Commentary

### Logic

`lifecycle_settings_from_config()` builds a `contextProviders` object from
`McpRuntimeConfig.providers` and `McpRuntimeConfig.repositories`. GrepAI roots
are derived from configured memory roots, falling back to the coordinator
`memory-repos` root when no repository memory roots are configured; CGC roots
are derived from configured code repository paths. The generated GrepAI settings
include Docker mode, the shared `ar-grepai-memory` network, the
`agents-remember/grepai:<pin>` runner image/container, Postgres backend
settings, and an Ollama embedder backend with `nomic-embed-text`. The generated
settings still include concrete provider runtime roots under `providers/runners`,
backend data roots under `providers/data`, log roots under `providers/logs`,
installed requirement paths, Docker backend image metadata, and watcher log
paths.

`write_lifecycle_settings()` writes that generated object to a temporary JSON
file for lower-level lifecycle functions that already accept `--from-settings`.

### Invariants And Boundaries

- Do not read coordinator `system/settings.json` here.
- Do not accept provider path overrides from MCP settings; paths are derived by
  the server.
- Keep generated settings complete enough for dry-run and real install paths,
  including backend images and image lock paths.
- `grepai-memory` generated settings must be complete enough for Docker to own
  the runner, Postgres backend, and Ollama embedder without requiring host
  GrepAI or Ollama binaries.
- Delete temporary settings files in the caller after lifecycle operations
  finish.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| MCP config derives allowed repositories/providers and provider runtime roots from trusted settings. | [config.py](agents-remember-md/mcp/src/agents_remember/mcp/config.py) |
| Provider status writes generated lifecycle settings before calling `watchers_run`. | [status.py](agents-remember-md/mcp/src/agents_remember/providers/status.py) |
| Runtime install uses generated lifecycle settings when installing provider dependencies from the MCP tool. | [runtime.py](agents-remember-md/mcp/src/agents_remember/install/runtime.py) |
| GrepAI lifecycle settings define Docker mode, shared network, runner image/container, Postgres backend, and Ollama embedder backend. | [settings.py](agents-remember-md/mcp/src/agents_remember/providers/settings.py) |

## Update History

- 2026-05-25T17:40+02:00: Updated after `grepai-memory` lifecycle settings switched to a complete Docker-owned runner, Postgres, and Ollama embedder stack.
- 2026-05-24T00:37+02:00: Refreshed verification and clarified the GrepAI fallback root used when no repository memory root is configured.
- 2026-05-23T04:29+02:00: Created when MCP provider lifecycle settings moved out of coordinator `system/settings.json`.
