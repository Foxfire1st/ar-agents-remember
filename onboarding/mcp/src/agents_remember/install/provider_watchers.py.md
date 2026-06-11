# mcp/src/agents_remember/install/provider_watchers.py

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                 |
| path                   | `mcp/src/agents_remember/install/provider_watchers.py` |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-06-04T22:15+02:00                             |
| lastVerifiedCommitHash |                                                    `0eba27a75a37ebc4ce1baeb9da9d7b7a879a8974`|
| lastVerifiedCommitDate |                                                    2026-06-04T22:38:48+02:00|
| governingOverview      | `../../../overview.md`                             |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`install/provider_watchers.py` owns provider watcher rebind orchestration for
`runtime_install(install_provider_deps=true)`. It keeps watcher stop/start/status
sequencing out of `install/runtime.py` while preserving the runtime install
summary contract and recovery guidance.

## Code Commentary

### Logic

`ProviderWatcherRebindReport` records lifecycle runs, final readiness, recovery
actions, and operator-facing messages. The helper writes temporary lifecycle
settings from the trusted provider settings, calls `lifecycle.watchers_run()` for
`stop`, `start`, and `status`, and records each result with an install phase.

`stop_provider_watchers_before_refresh()` performs the pre-refresh stop and
raises if the stop result is not fully ok, preventing provider runner pruning
while a watcher could still be mounted to the old runtime tree.
`complete_provider_watcher_rebind()` starts watchers, checks status, and if the
status is degraded or partial, performs one additional non-destructive
stop/start/status restart before marking the report ok or adding recovery
actions.

### Conventions

- Use generated lifecycle settings rather than coordinator-local settings files.
- Record dry-run watcher operations the same way as real runs so
  `runtime_install(dry_run=true)` can report the plan.
- Recovery actions use shared provider recovery wording from
  `providers/recovery.py`.

### Invariants And Boundaries

- This helper never invalidates provider indexes and never calls the destructive
  `invalidate-indexes` action.
- Provider data under `providers/data/**` is outside this module's scope; the
  runtime installer owns filesystem preservation while this helper owns watcher
  lifecycle calls.
- A degraded post-install status gets exactly one automatic non-destructive
  restart/rebind attempt before reporting the remaining issue.

### Todos

None.

## Docs References

No external documentation is configured for this repository slice.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant documentation found after checking configured sources. | n/a | n/a |

## Repo-Internal References

The helper is called from runtime installation and is covered by the installer
regression suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The rebind report stores lifecycle runs, readiness, recovery actions, messages, and the MCP payload shape. | L16-L31 | [provider_watchers.py](agents-remember/mcp/src/agents_remember/install/provider_watchers.py) |
| Watcher lifecycle calls use temporary provider settings, `lifecycle.watchers_run`, and per-phase result recording. | L34-L103 | [provider_watchers.py](agents-remember/mcp/src/agents_remember/install/provider_watchers.py) |
| The pre-refresh stop aborts on non-ok/partial watcher stop before runtime provider refresh proceeds. | L127-L151 | [provider_watchers.py](agents-remember/mcp/src/agents_remember/install/provider_watchers.py) |
| The post-install path starts watchers, checks status, and attempts one non-destructive restart/rebind before adding recovery guidance. | L154-L214 | [provider_watchers.py](agents-remember/mcp/src/agents_remember/install/provider_watchers.py) |
| Runtime install creates and attaches the report, stops watchers before provider refresh, and completes rebind/recovery before returning. | L437-L527 | [runtime.py](agents-remember/mcp/src/agents_remember/install/runtime.py) |
| Focused tests cover stop/start ordering, dry-run reporting, degraded retry, unrecovered failure guidance, and dependency-failure recovery. | L162-L452 | [test_install_runtime.py](agents-remember/mcp/tests/test_install_runtime.py) |

## Cross-Repo References

No sibling repository evidence is needed for this helper.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-04T22:15+02:00 — Created for the extracted runtime-install provider watcher rebind helper.
