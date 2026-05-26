# mcp/src/agents_remember/providers/grepai/lifecycle/actions.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/grepai/lifecycle/actions.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:09+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
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
structured unsupported results for non-Docker settings.

### Invariants And Boundaries

- Direct `grepai run` is for bounded CLI commands only; watcher commands route
  through lifecycle start/stop/refresh.
- Non-Docker GrepAI paths must report unsupported instead of installing host
  binaries or using host Ollama.
- Full install/start health is the composed state of Postgres, Ollama, runner
  image, watcher container, workspace config, and root artifact cleanup.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| PostgreSQL, Ollama, and runner modules provide the Docker stack that this module composes. | [backend.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/backend.py); [embedder.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/embedder.py); [runner.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/runner.py) |
| Tests protect Docker-only direct-run rejection, Docker bounded run construction, and full dry-run stack creation. | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |

## Update History

- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created from GrepAI top-level action dispatch extracted out of provider lifecycle.
