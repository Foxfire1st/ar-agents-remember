# mcp/src/agents_remember/providers/cgc/lifecycle/compose.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/compose.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T14:21:08+02:00                     |
| lastVerifiedCommitHash | `e1382b9277d48f13b6a1cb065f2fa2638b36feba` |
| lastVerifiedCommitDate | 2026-05-29T07:08:19+02:00|
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
configured repository root. Backend port mappings go through the shared Compose
helper so configured `auto` host ports render as Compose's empty
published-port syntax instead of the literal string `auto`. User mapping is
optional and only emitted on hosts with UID/GID support. `cgc_compose_summary()`
exposes the project, base file, override hash, and stdin override mode for
status and dry-run payloads. CGC Compose rendering now requires generated
`instance.labels` from MCP/provider settings and fails instead of falling back
to unlabeled legacy provider settings.

### Invariants And Boundaries

- CGC dynamic service values must come from provider settings and lifecycle
  layouts, not tool-supplied arbitrary Compose content.
- The first layout anchors shared backend settings; every configured layout can
  contribute one watcher service.
- Runner and watcher containers mount the runtime root read/write and the code
  repository read-only.
- Container-visible `FALKORDB_HOST` points to the managed backend container
  name, keeping CGC access inside the Compose network.
- `auto` host ports must remain valid Compose input because Compose parses the
  full project even for single-service operations.
- CGC Docker resources must render with generated Agents Remember ownership
  labels; missing `instance.labels` is an invalid settings shape.

## Docs References

No external domain documentation is configured for this repository; the
resolved `system/sources.md` currently contains no entries.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation source is configured for this file. | L1-L3 | [system/sources.md](../../../../../../../../../../system/sources.md) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `cgc_compose_render()` fills backend image, container, port, data volume, runner image/build context, ownership labels, mounts, environment, watcher services, and network name into the package override template, using shared port mapping rendering for `auto` ports. | L24-L75 | [compose.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/compose.py) |
| CGC watcher service names are derived from layout repo IDs, and watcher fragments mount runtime and code roots with generated environment. | L77-L116 | [compose.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/compose.py) |
| The summary reports Compose project, package base file, override SHA-256, and stdin override mode. | L119-L125 | [compose.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/compose.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo boundary is required beyond mounted repository roots configured by provider settings. | n/a | n/a |

## Update History

- 2026-05-28T14:21:08+02:00: Updated after CGC Compose label rendering began
  rejecting provider settings without generated `instance.labels`.
- 2026-05-27T00:25+02:00: Updated after CGC Compose port mappings switched to
  shared `auto`-safe rendering.
- 2026-05-26T23:59+02:00: Created for the provider Compose migration and closeout missing-onboarding gate.
