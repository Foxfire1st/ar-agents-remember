# mcp/src/agents_remember/providers/grepai/lifecycle/runner.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/grepai/lifecycle/runner.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-27T00:25+02:00                     |
| lastVerifiedCommitHash | `767790a0a90c9cdc97eb3e291d42622aced82a14` |
| lastVerifiedCommitDate | 2026-05-27T01:14:04+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`runner.py` owns the Docker runner image and watcher container for
GrepAI.

## Code Commentary

### Logic

The module builds the pinned GrepAI runner image from the upstream Linux release
asset, records runner image locks, reports watcher container status, runs
`grepai watch` in the managed runner container with runtime and log mounts,
stops the watcher container, and validates workspace status through
`docker exec`. Watcher startup receives the backend and embedder host ports
chosen earlier in the same GrepAI start flow so its Compose override matches
the already-started dependency services, and it shares the GrepAI project
migration helper for standalone watcher startup.

### Invariants And Boundaries

- Bounded GrepAI commands run through the managed watcher container; no host
  GrepAI binary is required.
- Watcher containers must use container-visible runtime and log mounts.
- Runner image build/status must stay separate from Postgres and Ollama
  container lifecycle.
- Watcher `up` should render dependency port mappings from the current start
  result when those services were just started.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Runner settings and workspace paths are derived in GrepAI core. | [core.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/core.py) |
| GrepAI action dispatch uses this module for start, stop, refresh, and bounded run readiness. | [actions.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/actions.py) |
| GrepAI project migration lives with backend startup and is reused here. | [backend.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/backend.py) |

## Update History

- 2026-05-27T00:25+02:00: Updated after watcher startup began rendering
  dependency ports from the current start flow and sharing GrepAI project
  migration.
- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created from GrepAI runner image and watcher lifecycle extracted out of provider lifecycle.
