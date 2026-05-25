# mcp/src/agents_remember/providers/lifecycle_modules/common.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle_modules/common.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:09+02:00                     |
| lastVerifiedCommitHash | `ae9c4e5b6af38eda7f2b29006130c4263e9db62f` |
| lastVerifiedCommitDate | 2026-05-25T19:55:09+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`common.py` holds shared lifecycle primitives used by both provider families:
UTF-8 setup, process namespace checks, subprocess wrappers, JSON IO, lifecycle
rendering, settings lookup, Docker inspection/network helpers, port allocation,
and FalkorDB ping polling.

## Code Commentary

### Logic

Command helpers separate bounded foreground commands from detached long-running
processes. Rendering helpers keep captured native command output streamable
without wrapping it in lifecycle JSON. Docker helpers inspect containers,
resolve published ports and mounts, allocate host ports, ensure networks, attach
containers to networks, check local image presence, and wait for CGC FalkorDB
health.

### Invariants And Boundaries

- Shared helpers must not know provider-specific settings schemas beyond small
  settings-file lookups.
- Long-running process starts must detach from MCP stdin and process lifetime.
- Docker helper failures must return structured lifecycle data or raise
  `ContextProviderError`; they must not silently fall back to host binaries.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CGC backend lifecycle uses shared Docker inspection, port, network, and ping helpers. | [cgc/backend.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/cgc/backend.py) |
| GrepAI backend/embedder/runner lifecycles use the same shared Docker primitives. | [grepai/backend.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/grepai/backend.py); [grepai/embedder.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/grepai/embedder.py); [grepai/runner.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/grepai/runner.py) |
| CLI rendering delegates captured command output handling here. | [cli.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/cli.py) |

## Update History

- 2026-05-25T19:09+02:00: Updated references after CGC and GrepAI modules moved under package subfolders.
- 2026-05-25T19:01+02:00: Created from shared helpers extracted out of the monolithic provider lifecycle implementation.
