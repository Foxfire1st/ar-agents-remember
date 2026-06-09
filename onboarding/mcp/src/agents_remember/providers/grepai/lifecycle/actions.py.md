# mcp/src/agents_remember/providers/grepai/lifecycle/actions.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/grepai/lifecycle/actions.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T05:30+02:00     |
| lastVerifiedCommitHash | `642cca15f206cf8cf43ff7ffd6dadc5c27af2879` |
| lastVerifiedCommitDate | 2026-06-10T01:44:33+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`actions.py` owns top-level GrepAI lifecycle action dispatch and the
Docker-only install/run/status composition.

## Code Commentary

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

| Finding | Source Path |
| --- | --- |
| PostgreSQL, Ollama, and runner modules provide the Docker stack that this module composes. | [backend.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/backend.py); [embedder.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/embedder.py); [runner.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/runner.py) |
| Tests protect Docker-only direct-run rejection, Docker bounded run construction, and full dry-run stack creation. | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |

## Update History

- 2026-06-10T05:30+02:00 — Leaf imports replace the `providers.context` aggregator import (circular-import fix; see core.py 2026-06-10 entry).
- 2026-06-02T01:15+02:00 — Removed `grepai_root_artifacts` and dropped the `rootArtifacts` term from the status ok-gate (roots are watched live; `.grepai/` is expected); `grepai_roots_payload` no longer emits `sourcePath` (watch-live).
- 2026-05-31T12:50+02:00 — Every `layout: Any` parameter re-typed to the concrete `GrepaiRuntimeLayout` (re-exported via the `core` star-import); behaviour-preserving, added an Invariants note pinning the `layout` type (1.0.0 review remediation).
- 2026-05-27T00:25+02:00: Updated after Docker start began passing
  backend/embedder port mappings into watcher startup.
- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created from GrepAI top-level action dispatch extracted out of provider lifecycle.
