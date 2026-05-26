# mcp/src/agents_remember/providers/grepai/lifecycle/runner.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/grepai/lifecycle/runner.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:09+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
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
`docker exec`.

### Invariants And Boundaries

- Bounded GrepAI commands run through the managed watcher container; no host
  GrepAI binary is required.
- Watcher containers must use container-visible runtime and log mounts.
- Runner image build/status must stay separate from Postgres and Ollama
  container lifecycle.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Runner settings and workspace paths are derived in GrepAI core. | [core.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/core.py) |
| GrepAI action dispatch uses this module for start, stop, refresh, and bounded run readiness. | [actions.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/actions.py) |

## Update History

- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created from GrepAI runner image and watcher lifecycle extracted out of provider lifecycle.
