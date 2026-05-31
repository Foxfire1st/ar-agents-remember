# mcp/src/agents_remember/providers/grepai/lifecycle/compose.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/grepai/lifecycle/compose.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[GrepAI Lifecycle Overview](overview.md)

## Purpose

`compose.py` renders the GrepAI Docker Compose override from MCP-derived
provider settings, runtime layout, and runner/backend settings. It keeps
Postgres, Ollama, and watcher dynamic values out of Python `docker run`
assembly while still letting lifecycle code choose ports and paths.

## Code Commentary

### Logic

`grepai_compose_render()` derives Ollama embedder settings, chooses caller
provided or configured host ports, fills Postgres and Ollama images,
containers, ports, and data volumes, points the runner build context at the
committed GrepAI Docker asset, injects runner version/architecture build args,
and renders watcher runtime/log mounts, environment, workspace name, and
network name into the package override template. Port mappings go through the
shared Compose helper so configured `auto` host ports render as Compose's empty
published-port syntax instead of the literal string `auto`. The watcher
environment is rendered from container-local runtime paths, and the Compose
override includes a host UID/GID user block on POSIX hosts so watcher-created
runtime artifacts stay removable by the developer user.
`grepai_compose_summary()` returns the project, package base file, override
hash, and stdin override mode. GrepAI Compose rendering requires generated
`instance.labels` from MCP/provider settings and fails instead of rendering
legacy unlabeled provider resources.

### Invariants And Boundaries

- GrepAI override values must come from provider settings, lifecycle layout, and
  runner/backend derivation, not arbitrary tool input.
- Rendered overrides are fed to Compose through stdin by shared lifecycle
  helpers; this module only renders and summarizes.
- `auto` host ports must remain valid Compose input because every `docker
  compose` invocation parses the whole provider project, even when only one
  service is targeted.
- The watcher uses package-owned runner build assets and mounted runtime/log
  directories from the resolved provider layout.
- The watcher must not receive host-path `HOME`/XDG environment values inside
  the container; GrepAI discovers its workspace config through the mounted
  `/grepai/runtime/home/.grepai` tree.
- GrepAI Docker resources must render with generated Agents Remember ownership
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
| `grepai_compose_render()` fills Postgres, Ollama, runner build, watcher user/environment, ownership labels, mounts, workspace, log mount, and network values into the package override template, using shared port mapping rendering for `auto` ports. | L40-L97 | [compose.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/compose.py) |
| The optional POSIX UID/GID Compose user block for the watcher is rendered via the shared `host_user_block()` helper. | L76 | [compose.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/compose.py) |
| The summary reports Compose project, package base file, override SHA-256, and stdin override mode. | L100-L106 | [compose.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/compose.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo boundary is required beyond mounted runtime roots configured by provider settings. | n/a | n/a |

## Update History

- 2026-05-31T12:30+02:00 — Fixed Repo-Internal citation: local `grepai_user()`/`grepai_user_block()` replaced by shared `host_user_block()` helper; refreshed line ranges (1.0.0 review remediation).
- 2026-05-28T14:21:08+02:00: Updated after GrepAI Compose label rendering began
  rejecting provider settings without generated `instance.labels`.
- 2026-05-27T00:41+02:00: Updated after GrepAI watcher Compose rendering
  switched to container-local env paths and POSIX UID/GID execution.
- 2026-05-27T00:25+02:00: Updated after GrepAI Compose port mappings switched
  to shared `auto`-safe rendering.
- 2026-05-26T23:59+02:00: Created for the provider Compose migration and closeout missing-onboarding gate.
