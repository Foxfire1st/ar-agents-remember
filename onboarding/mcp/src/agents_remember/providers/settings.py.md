# mcp/src/agents_remember/providers/settings.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/settings.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T05:30+02:00     |
| lastVerifiedCommitHash | `642cca15f206cf8cf43ff7ffd6dadc5c27af2879` |
| lastVerifiedCommitDate | 2026-06-10T01:44:33+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`settings.py` converts trusted MCP runtime settings into the temporary provider
lifecycle settings consumed by package-local provider lifecycle code. Generated
settings for both `grepai-memory` and `codegraphcontext-code` describe
Docker-owned provider runtimes rather than host provider binaries or venvs.

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
backend data roots under `providers/data`, central log roots under
`logs/providers`, installed requirement paths, Docker backend image metadata,
and watcher log paths.
The generated CodeGraphContext settings include a Docker runtime/runner block
whose image comes from the single `cgc_runner_image()` derivation
(`repository:version-layerrevision`, imported from `cgc/context/core.py`) —
deriving it independently here is what shipped the 2.5.0 upgrade-path bug
where cached-image hosts kept a guard-less image (GitHub #50) — plus image
build root, image lock file, watcher container name template, and an
`ar-cgc-code` backend network entry; they no longer include a managed provider
venv root.

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
- `codegraphcontext-code` generated settings must be complete enough for Docker
  to own the runner image/container and FalkorDB backend without requiring a
  host Python virtual environment.
- The CGC backend network name in generated settings is part of the Docker-owned
  runtime contract; runner containers use it to reach FalkorDB by container
  name instead of host loopback.
- Delete temporary settings files in the caller after lifecycle operations
  finish.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| MCP config derives allowed repositories/providers and provider runtime roots from trusted settings. | [config.py](agents-remember-md/mcp/src/agents_remember/mcp/config.py) |
| Provider status writes generated lifecycle settings before calling `watchers_run`. | [status.py](agents-remember-md/mcp/src/agents_remember/providers/status.py) |
| Runtime install uses generated lifecycle settings when installing provider dependencies from the MCP tool. | [runtime.py](agents-remember-md/mcp/src/agents_remember/install/runtime.py) |
| GrepAI lifecycle settings define Docker mode, shared network, runner image/container, Postgres backend, and Ollama embedder backend. | [settings.py](agents-remember-md/mcp/src/agents_remember/providers/settings.py) |
| CodeGraphContext lifecycle settings define Docker runner image/build/lock/container settings and FalkorDB backend settings. | [settings.py](agents-remember-md/mcp/src/agents_remember/providers/settings.py) |

## Update History

- 2026-06-10T05:30+02:00 — CGC runner image comes from the single `cgc_runner_image()` derivation (GitHub #50): the independent repository:version f-string here dropped the image layer revision, so upgrading hosts kept a cached guard-less image under the guard entrypoint.
- 2026-06-09T22:10+02:00 — CGC backend default settings gained `dataDestination: /var/lib/falkordb/data` (the container path FalkorDB v4 writes to), mirroring the GrepAI/Postgres `dataDestination` pattern; the data volume now binds there instead of `/data`.
- 2026-05-28T12:32+02:00: Updated after generated provider log roots moved under the central `logs/providers/` tree.
- 2026-05-26T13:58+02:00: Updated after generated CGC settings gained the shared backend Docker network entry.
- 2026-05-26T12:51+02:00: Updated after `codegraphcontext-code` lifecycle settings switched from host venv fields to Docker runner image/container settings.
- 2026-05-25T17:40+02:00: Updated after `grepai-memory` lifecycle settings switched to a complete Docker-owned runner, Postgres, and Ollama embedder stack.
- 2026-05-24T00:37+02:00: Refreshed verification and clarified the GrepAI fallback root used when no repository memory root is configured.
- 2026-05-23T04:29+02:00: Created when MCP provider lifecycle settings moved out of coordinator `system/settings.json`.
