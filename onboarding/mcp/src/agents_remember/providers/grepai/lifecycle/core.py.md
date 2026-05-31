# mcp/src/agents_remember/providers/grepai/lifecycle/core.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/grepai/lifecycle/core.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
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
container-visible root paths, builds container DSNs and container-local
environment variables, selects a supported runner release architecture, and
derives PostgreSQL, Ollama, and runner image settings.

### Invariants And Boundaries

- Settings-backed GrepAI lifecycle must use Docker mode.
- Workspace config must use container-visible project paths, the Postgres
  container DSN, and the Ollama container endpoint.
- Containerized GrepAI watcher environment must point at mounted container
  paths such as `/grepai/runtime/home`, not host runtime paths.
- This module derives configuration only; container start/status logic belongs
  in backend, embedder, and runner modules. It no longer runs commands itself:
  the `grepai_run_checked_command` helper and the `run_command` import were
  removed, so command execution lives solely in the lifecycle command runner.
- Layout-consuming helpers (`grepai_layout_from_args` return value,
  `prepare_grepai_workspace`, runner/backend/embedder/container/template-vars
  builders) are typed against the `GrepaiRuntimeLayout` dataclass imported from
  `providers.context`, not an opaque `Any`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| GrepAI PostgreSQL backend lifecycle consumes backend settings from this module. | [backend.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/backend.py) |
| GrepAI Ollama lifecycle consumes embedder settings from this module. | [embedder.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/embedder.py) |
| GrepAI runner image/container lifecycle consumes runner settings and workspace config from this module. | [runner.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/runner.py) |

## Update History

- 2026-05-31T12:50+02:00 — Removed the unused `grepai_run_checked_command` helper and its `run_command` import, and typed the `layout` params plus the `grepai_layout_from_args` return on `GrepaiRuntimeLayout` (newly imported) instead of `Any`; reinforced the "derives configuration only" boundary and recorded the layout typing in Invariants And Boundaries (1.0.0 review remediation).
- 2026-05-27T00:41+02:00: Updated after container GrepAI environment rendering
  switched to container-local runtime paths for the Compose watcher.
- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created from GrepAI settings and workspace logic extracted out of provider lifecycle.
