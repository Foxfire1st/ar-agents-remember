# mcp/src/agents_remember/providers/grepai/lifecycle/compose.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/grepai/lifecycle/compose.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-27T00:41+02:00                     |
| lastVerifiedCommitHash | `f20f75e3e3c6da0c56a6ccfdedfa9d859d7329b7` |
| lastVerifiedCommitDate | 2026-05-27T18:11:35+02:00|
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
hash, and stdin override mode.

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

## Docs References

No external domain documentation is configured for this repository; the
resolved `system/sources.md` currently contains no entries.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation source is configured for this file. | L1-L3 | [system/sources.md](../../../../../../../../../../system/sources.md) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `grepai_compose_render()` fills Postgres, Ollama, runner build, watcher user/environment, mounts, workspace, log mount, and network values into the package override template, using shared port mapping rendering for `auto` ports. | L27-L83 | [compose.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/compose.py) |
| `grepai_user()` and `grepai_user_block()` render the optional POSIX UID/GID Compose user block for the watcher. | L86-L93 | [compose.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/compose.py) |
| The summary reports Compose project, package base file, override SHA-256, and stdin override mode. | L96-L102 | [compose.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/compose.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo boundary is required beyond mounted runtime roots configured by provider settings. | n/a | n/a |

## Update History

- 2026-05-27T00:41+02:00: Updated after GrepAI watcher Compose rendering
  switched to container-local env paths and POSIX UID/GID execution.
- 2026-05-27T00:25+02:00: Updated after GrepAI Compose port mappings switched
  to shared `auto`-safe rendering.
- 2026-05-26T23:59+02:00: Created for the provider Compose migration and closeout missing-onboarding gate.
