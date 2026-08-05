# mcp/src/agents_remember/providers/grepai/lifecycle/actions.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/grepai/lifecycle/actions.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`actions.py` owns top-level GrepAI lifecycle action dispatch and the
Docker-only install/run/status composition.

## Code Commentary

### 260731-EFA-L2 Call Sites For The New Bundles

The action wrappers construct the parameter objects their callees now take (all defined in
`grepai/lifecycle/core.py` and `runner.py`):

- `prepare_grepai_workspace(layout, provider_settings, GrepaiWorkspaceConfig(dsn=…,
  project_paths=…, embedder_settings=…))` — in both `grepai_docker_workspace_state` and
  `grepai_install_workspace`.
- `grepai_watcher_container_start(..., ports=GrepaiServicePorts(postgres=…, ollama=…))` — the two
  published host ports read out of the backend and embedder results.
- `grepai_docker_state(layout, GrepaiStackResults(backend=…, embedder=…, watcher=…), action=…,
  runner=…)` — the per-container lifecycle results.

The written state file and every returned payload are unchanged.

### Logic

The module reports aggregate GrepAI status, validates bounded native GrepAI CLI
arguments, executes bounded commands through `docker exec ar-grepai-watcher`,
starts/stops/refreshes the Docker watcher, prepares the workspace after backend
and embedder startup, builds the runner image during install, and returns
structured unsupported results for non-Docker settings. Full Docker start
passes the backend and embedder host ports selected by their startup steps into
watcher startup so later Compose calls use the same dependency port mappings.

### Invariants And Boundaries

- Direct `grepai run` is for bounded CLI commands only; watcher commands route
  through lifecycle start/stop/refresh.
- Non-Docker GrepAI paths must report unsupported instead of installing host
  binaries or using host Ollama.
- Full install/start health is the composed state of Postgres, Ollama, runner
  image, watcher container, and workspace config. Presence of grepai's `.grepai/`
  working dir in a root is expected (roots are watched live) and no longer fails
  status.
- Watcher startup should receive the current backend/embedder port mappings
  from the same GrepAI start flow.
- The `layout` parameter throughout is the concrete `GrepaiRuntimeLayout`
  dataclass (re-exported via the `core` star-import), not an untyped `Any`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| PostgreSQL, Ollama, and runner modules provide the Docker stack that this module composes. | `docker_wait_for_postgres`; `docker_wait_for_ollama`; `grepai_runner_image_build` | mcp/src/agents_remember/providers/grepai/lifecycle/backend.py:51-68; mcp/src/agents_remember/providers/grepai/lifecycle/embedder.py:46-62; mcp/src/agents_remember/providers/grepai/lifecycle/runner.py:37-74 |
| Tests protect Docker-only direct-run rejection, Docker bounded run construction, and full dry-run stack creation. | `test_grepai_direct_run_requires_settings_backed_docker`; `test_grepai_start_dry_run_builds_complete_docker_stack` | mcp/tests/test_provider_lifecycle.py:282-316; mcp/tests/test_provider_lifecycle.py:354-409 |

## Update History

- 2026-08-04T18:16+02:00 — 260731-EFA-L6 S18-B16 curator: repaired 2 citation rows: the Docker stack module functions (backend.py L51-L68, embedder.py L46-L62, runner.py L37-L74) and the lifecycle tests (test_provider_lifecycle.py L282-L410). Scoped fixer + non-fixing recheck green under the frozen snapshot; verification metadata unchanged.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2: call-site updates for the new
  `GrepaiWorkspaceConfig` / `GrepaiServicePorts` / `GrepaiStackResults` signatures. Same payloads
  and state file. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-06-10T07:30+02:00 — No content impact: import path updated to `providers/context_common.py` (shared helpers moved out of the facade package, GitHub #58); documented behavior unchanged.
- 2026-06-10T05:30+02:00 — Leaf imports replace the `providers.context` aggregator import (circular-import fix; see core.py 2026-06-10 entry).
- 2026-06-02T01:15+02:00 — Removed `grepai_root_artifacts` and dropped the `rootArtifacts` term from the status ok-gate (roots are watched live; `.grepai/` is expected); `grepai_roots_payload` no longer emits `sourcePath` (watch-live).
- 2026-05-31T12:50+02:00 — Every `layout: Any` parameter re-typed to the concrete `GrepaiRuntimeLayout` (re-exported via the `core` star-import); behaviour-preserving, added an Invariants note pinning the `layout` type (1.0.0 review remediation).
- 2026-05-27T00:25+02:00: Updated after Docker start began passing
  backend/embedder port mappings into watcher startup.
- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created from GrepAI top-level action dispatch extracted out of provider lifecycle.
