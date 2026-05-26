# mcp/src/agents_remember/providers/cgc/lifecycle/compose.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/compose.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-26T23:59+02:00                     |
| lastVerifiedCommitHash | `45214435fd2de65765a8230ceb1dcfe188d1944d` |
| lastVerifiedCommitDate | 2026-05-27T00:09:33+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[CGC Lifecycle Overview](overview.md)

## Purpose

`compose.py` renders the CodeGraphContext Docker Compose override from
MCP-derived provider settings and runtime layouts. It is the CGC-specific bridge
between stable package Compose templates and dynamic local backend/watcher
state.

## Code Commentary

### Logic

`cgc_compose_render()` validates that at least one layout exists, derives the
shared FalkorDB backend settings from the first layout, fills dynamic backend
image/container/port/data-volume values, points the runner build context at the
committed package Docker asset, and renders one watcher service fragment per
configured repository root. User mapping is optional and only emitted on hosts
with UID/GID support. `cgc_compose_summary()` exposes the project, base file,
override hash, and stdin override mode for status and dry-run payloads.

### Invariants And Boundaries

- CGC dynamic service values must come from provider settings and lifecycle
  layouts, not tool-supplied arbitrary Compose content.
- The first layout anchors shared backend settings; every configured layout can
  contribute one watcher service.
- Runner and watcher containers mount the runtime root read/write and the code
  repository read-only.
- Container-visible `FALKORDB_HOST` points to the managed backend container
  name, keeping CGC access inside the Compose network.

## Docs References

No external domain documentation is configured for this repository; the
resolved `system/sources.md` currently contains no entries.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation source is configured for this file. | L1-L3 | [system/sources.md](../../../../../../../../../../system/sources.md) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `cgc_compose_render()` fills backend image, container, port, data volume, runner image/build context, mounts, environment, watcher services, and network name into the package override template. | L22-L74 | [compose.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/compose.py) |
| CGC watcher service names are derived from layout repo IDs, and watcher fragments mount runtime and code roots with generated environment. | L77-L116 | [compose.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/compose.py) |
| The summary reports Compose project, package base file, override SHA-256, and stdin override mode. | L119-L125 | [compose.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/compose.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo boundary is required beyond mounted repository roots configured by provider settings. | n/a | n/a |

## Update History

- 2026-05-26T23:59+02:00: Created for the provider Compose migration and closeout missing-onboarding gate.
