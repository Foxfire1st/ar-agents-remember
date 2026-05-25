# mcp/src/agents_remember/providers/lifecycle_modules/ - Provider Lifecycle Modules Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| sourceRoute            | `mcp/src/agents_remember/providers/lifecycle_modules/` |
| doc_type               | `route-overview`                           |
| lastUpdated            | 2026-05-25T19:16+02:00                     |
| lastVerifiedCommitHash | `a8ee8440dfa920d1153a4bb4bb43cc77534c3c90` |
| lastVerifiedCommitDate | 2026-05-25T15:22:52+02:00                  |
| governingOverview      | `../../../../overview.md`                  |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Purpose

`lifecycle_modules/` contains the extracted implementation for optional context
provider lifecycle operations. The route replaces the previous oversized
monolithic provider lifecycle implementation with focused modules for shared
helpers, CLI dispatch, watcher aggregation, CodeGraphContext, and Docker-owned
GrepAI.

## Hot Path Summary

Start with `cli.py` for parser/action dispatch, `common.py` for shared command,
JSON, process, rendering, and Docker helpers, and `watchers.py` for aggregate
provider start/status/stop orchestration. CGC behavior lives under `cgc/`:
`cgc/__init__.py` is the export facade, `cgc/core.py` derives settings/layout,
`cgc/backend.py` manages FalkorDB, `cgc/installation.py` owns install/patch
status, and `cgc/process.py` owns watcher/process/query actions. GrepAI
behavior lives under `grepai/`: `grepai/__init__.py` is the export facade,
`grepai/core.py` derives Docker/workspace settings, `grepai/backend.py`
manages Postgres, `grepai/embedder.py` manages Ollama, `grepai/runner.py`
manages the runner image/container, and `grepai/actions.py` composes top-level
actions.

## Route Model

- Shared lifecycle primitives live in `common.py`.
- CLI construction and top-level provider/action dispatch live in `cli.py`.
- `watchers.py` composes enabled GrepAI and CGC lifecycle results.
- `cgc/` owns CodeGraphContext settings/layout, backend container,
  install/patch/status, and process actions.
- `grepai/` owns Docker GrepAI settings, PostgreSQL, Ollama, runner
  image/container, bounded run, install, status, and refresh actions.

## Invariants And Boundaries

- `providers.lifecycle` is the only public facade; implementation belongs here.
- GrepAI is Docker-or-bust: no host GrepAI binary and no host Ollama fallback.
- Shared helpers should stay provider-agnostic; provider-specific branching
  belongs in CGC or GrepAI modules.
- Lifecycle service callers should dispatch to implementation functions through
  the `providers.lifecycle` facade, not through CLI subprocess capture.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Public lifecycle exports are collected by the renamed facade. | [lifecycle.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle.py) |
| CGC lifecycle implementation is grouped under the prefix-free CGC package. | [CGC lifecycle overview](cgc/overview.md) |
| GrepAI lifecycle implementation is grouped under the prefix-free GrepAI package. | [GrepAI lifecycle overview](grepai/overview.md) |
| Provider lifecycle tests cover Docker-only GrepAI behavior, CGC bounded run behavior, and watcher aggregation. | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |

## Update History

- 2026-05-25T19:16+02:00: Updated after the legacy `provider_lifecycle.py` compatibility shim was removed and `providers.lifecycle` became the sole facade.
- 2026-05-25T19:09+02:00: Updated after CGC and GrepAI lifecycle modules moved into `cgc/` and `grepai/` subpackages with prefix-free filenames.
- 2026-05-25T19:01+02:00: Created after provider lifecycle was split out of the monolithic implementation into focused modules.
