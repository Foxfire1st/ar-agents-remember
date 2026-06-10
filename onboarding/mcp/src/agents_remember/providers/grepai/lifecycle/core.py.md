# mcp/src/agents_remember/providers/grepai/lifecycle/core.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/grepai/lifecycle/core.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T07:30+02:00     |
| lastVerifiedCommitHash | `ab7e21b4ab4b8526adcdad8ea2243657b8aea7a0` |
| lastVerifiedCommitDate | 2026-06-10T08:21:41+02:00|
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

Root container paths resolve under the runner `rootsMount` (default
`/grepai/roots/<project_id>`) via `grepai_root_container_path`, where each live
memory root is bind-mounted; the prior host-path translator
(`grepai_container_path`) is gone. `prepare_grepai_workspace` no longer syncs a
mirror or scrubs artifacts -- it calls `ensure_grepai_root_gitignore` so each
root's `.gitignore` ignores grepai's `.grepai/` working dir.

`grepai_embedder_backend_settings` now conditionally propagates
`seedFromContainer` from the embedder backend settings into the resolved dict.
The key is present only when the raw backend settings carry a non-empty
`seedFromContainer` string (populated by `isolated.py` for worktree embedders
to name the workspace Ollama container); it is absent for the workspace embedder
itself. This lets `embedder.py`'s `_seed_ollama_model_from_source` find the
seed target without the caller needing to pass it separately.

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
  builders) are typed against the `GrepaiRuntimeLayout` dataclass, not an
  opaque `Any`.
- Imports come from the leaf modules (`grepai.context`, `context.common`),
  never the `providers.context` aggregator: the aggregator star-imports this
  provider's context back, so routing through it is a circular import that
  breaks any entry point touching grepai modules first.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| GrepAI PostgreSQL backend lifecycle consumes backend settings from this module. | [backend.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/backend.py) |
| GrepAI Ollama lifecycle consumes embedder settings from this module. | [embedder.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/embedder.py) |
| GrepAI runner image/container lifecycle consumes runner settings and workspace config from this module. | [runner.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/runner.py) |

## Update History

- 2026-06-10T07:30+02:00 — No content impact: import path updated to `providers/context_common.py` (shared helpers moved out of the facade package, GitHub #58); documented behavior unchanged.
- 2026-06-10T05:30+02:00 — Imports moved off the `providers.context` aggregator to leaf modules (`grepai.context` + `context.common`): the aggregator star-imports grepai context back, a circular import that broke any entry point touching grepai modules first.
- 2026-06-02T01:15+02:00 — Added `rootsMount` (default `/grepai/roots`) to runner settings; `grepai_container_project_paths` now maps via `grepai_root_container_path` to `/grepai/roots/<project_id>` and the host-path translator `grepai_container_path` was removed; `prepare_grepai_workspace` now calls `ensure_grepai_root_gitignore` instead of the mirror sync + artifact scrub (watch-live).
- 2026-06-01T00:00+02:00 — `grepai_embedder_backend_settings` now propagates `seedFromContainer` from raw backend settings into the resolved dict when the key is a non-empty string; updated Logic.
- 2026-05-31T12:50+02:00 — Removed the unused `grepai_run_checked_command` helper and its `run_command` import, and typed the `layout` params plus the `grepai_layout_from_args` return on `GrepaiRuntimeLayout` (newly imported) instead of `Any`; reinforced the "derives configuration only" boundary and recorded the layout typing in Invariants And Boundaries (1.0.0 review remediation).
- 2026-05-27T00:41+02:00: Updated after container GrepAI environment rendering
  switched to container-local runtime paths for the Compose watcher.
- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created from GrepAI settings and workspace logic extracted out of provider lifecycle.
