# mcp/src/agents_remember/providers/grepai/lifecycle/core.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/grepai/lifecycle/core.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:09+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`core.py` owns GrepAI settings, layout, workspace, runner, backend, and
embedder derivation shared by the Docker-owned GrepAI modules.

## Code Commentary

### Logic

The module resolves settings-backed GrepAI runtime layout, prepares workspace
state, validates Docker mode, derives the managed Docker network name, maps
container-visible root paths, builds container DSNs and environment variables,
selects a supported runner release architecture, and derives PostgreSQL,
Ollama, and runner image settings.

### Invariants And Boundaries

- Settings-backed GrepAI lifecycle must use Docker mode.
- Workspace config must use container-visible project paths, the Postgres
  container DSN, and the Ollama container endpoint.
- This module derives configuration only; container start/status logic belongs
  in backend, embedder, and runner modules.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| GrepAI PostgreSQL backend lifecycle consumes backend settings from this module. | [backend.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/backend.py) |
| GrepAI Ollama lifecycle consumes embedder settings from this module. | [embedder.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/embedder.py) |
| GrepAI runner image/container lifecycle consumes runner settings and workspace config from this module. | [runner.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/runner.py) |

## Update History

- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created from GrepAI settings and workspace logic extracted out of provider lifecycle.
