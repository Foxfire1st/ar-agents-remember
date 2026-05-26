# mcp/src/agents_remember/providers/grepai/lifecycle/compose.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/grepai/lifecycle/compose.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-26T23:59+02:00                     |
| lastVerifiedCommitHash | `45214435fd2de65765a8230ceb1dcfe188d1944d` |
| lastVerifiedCommitDate | 2026-05-27T00:09:33+02:00|
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
network name into the package override template. `grepai_compose_summary()`
returns the project, package base file, override hash, and stdin override mode.

### Invariants And Boundaries

- GrepAI override values must come from provider settings, lifecycle layout, and
  runner/backend derivation, not arbitrary tool input.
- Rendered overrides are fed to Compose through stdin by shared lifecycle
  helpers; this module only renders and summarizes.
- The watcher uses package-owned runner build assets and mounted runtime/log
  directories from the resolved provider layout.

## Docs References

No external domain documentation is configured for this repository; the
resolved `system/sources.md` currently contains no entries.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation source is configured for this file. | L1-L3 | [system/sources.md](../../../../../../../../../../system/sources.md) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `grepai_compose_render()` fills Postgres, Ollama, runner build, watcher mount/environment, workspace, log mount, and network values into the package override template. | L23-L78 | [compose.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/compose.py) |
| The summary reports Compose project, package base file, override SHA-256, and stdin override mode. | L81-L87 | [compose.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/compose.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo boundary is required beyond mounted runtime roots configured by provider settings. | n/a | n/a |

## Update History

- 2026-05-26T23:59+02:00: Created for the provider Compose migration and closeout missing-onboarding gate.
