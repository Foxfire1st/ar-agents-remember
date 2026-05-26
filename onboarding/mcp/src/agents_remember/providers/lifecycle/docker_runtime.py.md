# mcp/src/agents_remember/providers/lifecycle/docker_runtime.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/docker_runtime.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T21:14+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Overview](overview.md)

## Purpose

`docker_runtime.py` owns the shared Docker adapter helpers used by CGC and
GrepAI lifecycle modules.

## Code Commentary

### Logic

The module resolves the Docker executable, inspects containers and images,
reads published port and mount metadata, normalizes host paths, ensures Docker
networks and network attachments, checks local image presence, and waits for
FalkorDB ping health.

### Invariants And Boundaries

- Docker absence is an error; provider lifecycle code must not fall back to
  host binaries.
- The helpers expose Docker facts and requested mutations, but provider-owned
  modules decide what those facts mean.
- FalkorDB ping polling is shared here because it is Docker health plumbing for
  the CGC backend container.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CGC backend lifecycle uses Docker inspection, mount matching, image locks, and FalkorDB ping polling. | [backend.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/backend.py) |
| GrepAI backend, embedder, and runner lifecycles use Docker inspection and network helpers. | [backend.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/backend.py); [embedder.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/embedder.py); [runner.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/runner.py) |

## Update History

- 2026-05-25T21:14+02:00: Created from the Docker adapter portion of the former shared lifecycle common module.
