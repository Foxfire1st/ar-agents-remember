# mcp/src/agents_remember/providers/lifecycle/ - Provider Lifecycle Facade Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| sourceRoute            | `mcp/src/agents_remember/providers/lifecycle/` |
| doc_type               | `route-overview`                           |
| lastUpdated            | 2026-05-28T12:32+02:00                     |
| lastVerifiedCommitHash | `a8ee8440dfa920d1153a4bb4bb43cc77534c3c90` |
| lastVerifiedCommitDate | 2026-05-25T15:22:52+02:00                  |
| governingOverview      | `../../../../overview.md`                  |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Purpose

`lifecycle/` contains the public provider-lifecycle package facade, CLI
entrypoints, watcher aggregation, and shared lifecycle helper modules.
Provider-specific lifecycle implementations now live under
`providers/cgc/lifecycle/` and `providers/grepai/lifecycle/`.

## Hot Path Summary

Start with `cli.py` for parser/action dispatch, `watchers.py` for aggregate
provider start/status/stop orchestration, and the named shared modules for
provider-agnostic lifecycle primitives: `command_runner.py`,
`docker_runtime.py`, `host_ports.py`, `process_status.py`,
`provider_settings.py`, `result_rendering.py`, `runtime_environment.py`, and
`state_files.py`. CGC behavior lives under `../cgc/lifecycle/`; GrepAI
behavior lives under `../grepai/lifecycle/`. Docker helpers now expose
normalized container state, health, and uptime summaries used by provider
current-state reporting.

## Route Model

- Shared lifecycle primitives live in named modules by responsibility.
- CLI construction and top-level provider/action dispatch live in `cli.py`.
- `watchers.py` composes enabled GrepAI and CGC lifecycle results.
- `../cgc/lifecycle/` owns CodeGraphContext settings/layout, backend container,
  install/patch/status, and process actions.
- `../grepai/lifecycle/` owns Docker GrepAI settings, PostgreSQL, Ollama, runner
  image/container, bounded run, install, status, and refresh actions.

## Invariants And Boundaries

- `providers.lifecycle` is the only public facade; implementation belongs here.
- GrepAI is Docker-or-bust: no host GrepAI binary and no host Ollama fallback.
- Shared helpers should stay provider-agnostic; provider-specific branching
  belongs in CGC or GrepAI modules.
- Shared Docker helpers can normalize container facts, but provider readiness
  and current-state aggregation belong in provider-specific modules and
  `providers/current_state.py`.
- Lifecycle service callers should dispatch to implementation functions through
  the `providers.lifecycle` facade, not through CLI subprocess capture.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Public lifecycle exports are collected by the package facade. | [__init__.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/__init__.py) |
| Package execution delegates to the lifecycle CLI. | [__main__.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/__main__.py) |
| CGC lifecycle implementation is grouped under the CGC provider package. | [CGC lifecycle overview](../cgc/lifecycle/overview.md) |
| GrepAI lifecycle implementation is grouped under the GrepAI provider package. | [GrepAI lifecycle overview](../grepai/lifecycle/overview.md) |
| Provider lifecycle tests cover Docker-only GrepAI behavior, CGC bounded run behavior, and watcher aggregation. | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |

## Update History

- 2026-05-28T12:32+02:00: Updated after shared Docker helpers began exposing container-state summaries for provider current-state reporting.
- 2026-05-25T21:14+02:00: Updated when provider lifecycle implementation moved to provider-first packages and shared lifecycle helpers were split by responsibility.
- 2026-05-25T19:16+02:00: Updated after the legacy `provider_lifecycle.py` compatibility shim was removed and `providers.lifecycle` became the sole facade.
- 2026-05-25T19:09+02:00: Updated after CGC and GrepAI lifecycle modules moved into `cgc/` and `grepai/` subpackages with prefix-free filenames.
- 2026-05-25T19:01+02:00: Created after provider lifecycle was split out of the monolithic implementation into focused modules.
