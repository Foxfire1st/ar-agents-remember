# mcp/src/agents_remember/providers/cgc/lifecycle/compose.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/compose.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-09T22:10+02:00                     |
| lastVerifiedCommitHash | `6beccd0545a2d5c161059715d5ed7830917eba03` |
| lastVerifiedCommitDate | 2026-06-09T22:39:28+02:00|
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
configured repository root. The FalkorDB data volume binds the host
`backend_data_root` to the backend settings' `dataDestination` (default
`/var/lib/falkordb/data`, where FalkorDB v4 actually writes) — binding `/data`
left graph data in the ephemeral container layer, lost on every recreate. Backend port mappings go through the shared Compose
helper so configured `auto` host ports render as Compose's empty
published-port syntax instead of the literal string `auto`. User mapping is
optional and only emitted on hosts with UID/GID support; it is now produced by
the shared `host_user_block()` helper imported from `compose_runtime` (the
former local `cgc_user()` / `cgc_user_block()` helpers and the `os` import were
removed). `cgc_compose_summary()`
exposes the project, base file, override hash, and stdin override mode for
status and dry-run payloads. CGC Compose rendering now requires generated
`instance.labels` from MCP/provider settings and fails instead of falling back
to unlabeled legacy provider settings.

Runner and watcher services bind-mount the host runtime and code roots at the
layout's driveless container paths (`container_runtime_root` /
`container_code_repo_root`), set `working_dir` and the watcher repo argument to
those container paths, and inject the container environment through
`cgc_compose_env()`, which calls `layout.env(for_container=True)`. Only the host
side of each mount keeps the native path. This keeps mount targets and
in-container paths valid on Windows hosts, where the host path's drive-letter
colon would otherwise make Docker's `host:container:mode` mount string
ambiguous ("too many colons").

### Invariants And Boundaries

- CGC dynamic service values must come from provider settings and lifecycle
  layouts, not tool-supplied arbitrary Compose content.
- The first layout anchors shared backend settings; every configured layout can
  contribute one watcher service.
- Runner and watcher containers mount the runtime root read/write and the code
  repository read-only; the container-side mount targets, `working_dir`, watch
  repo path, and injected environment are driveless POSIX paths
  (`container_runtime_root` / `container_code_repo_root`,
  `env(for_container=True)`), while only the host side keeps the native path.
  This is identity on POSIX hosts and only changes behavior on Windows hosts.
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

- 2026-06-09T22:10+02:00 — FalkorDB data volume now binds to the configurable backend `dataDestination` (default `/var/lib/falkordb/data`) instead of hardcoded `/data`, fixing graph data loss on container recreate; the watcher service template gained a `cgc-watch-guard.py` entrypoint that clears poisoned empty graph keys before exec'ing `cgc watch`.
- 2026-05-31T12:50+02:00 — Source consolidated host user mapping: local `cgc_user()` / `cgc_user_block()` and the `os` import were removed, `RUNNER_USER_BLOCK` / `WATCHER_USER_BLOCK` now use the shared `host_user_block()` imported from `compose_runtime`, and `layouts` plus the layout-taking helpers are now typed `CgcRuntimeLayout` (imported from `core`) instead of `Any`; corrected the Logic section's user-mapping prose to name the shared helper (1.0.0 review remediation).
- 2026-05-29T07:19+02:00: Updated after runner/watcher bind-mount targets,
  `working_dir`, watch repo path, and container environment switched to driveless
  POSIX container paths (`container_runtime_root` / `container_code_repo_root`,
  `env(for_container=True)`) for Windows-host support.
- 2026-05-28T14:21:08+02:00: Updated after CGC Compose label rendering began
  rejecting provider settings without generated `instance.labels`.
- 2026-05-27T00:25+02:00: Updated after CGC Compose port mappings switched to
  shared `auto`-safe rendering.
- 2026-05-26T23:59+02:00: Created for the provider Compose migration and closeout missing-onboarding gate.
