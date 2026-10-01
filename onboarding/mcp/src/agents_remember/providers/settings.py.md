# mcp/src/agents_remember/providers/settings.py

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`settings.py` converts trusted MCP runtime settings into the temporary provider
lifecycle settings consumed by package-local provider lifecycle code. Since L12 each generated CGC root entry can carry per-repo managed
`cgcignorePatterns` from `CGC_REPO_CGCIGNORE_EXTRAS` (feeding the layout's
`_cgcignore_patterns_from_settings` hook, which previously had no config feeder).
Generated
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

## Evidence

### Repo-Internal References

- MCP config derives allowed repositories/providers and provider runtime roots from trusted settings. [1]
- Provider status writes generated lifecycle settings before calling `watchers_run`. [2]
- Runtime install uses generated lifecycle settings when installing provider dependencies from the MCP tool. [3]
- GrepAI lifecycle settings define Docker mode, shared network, runner image/container, Postgres backend, and Ollama embedder backend. [4]
- CodeGraphContext lifecycle settings define Docker runner image/build/lock/container settings and FalkorDB backend settings. [5]
