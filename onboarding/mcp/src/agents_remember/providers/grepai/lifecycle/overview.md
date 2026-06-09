# mcp/src/agents_remember/providers/grepai/lifecycle/ - GrepAI Lifecycle Modules Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| sourceRoute            | `mcp/src/agents_remember/providers/grepai/lifecycle/` |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-06-06T12:15                           |
| lastVerifiedCommitHash | `592274a52cec61d97521771c630272c72240ed01` |
| lastVerifiedCommitDate | 2026-06-10T01:38:42+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[GrepAI Provider Overview](../overview.md)

## Purpose

`grepai/lifecycle/` contains the Docker-owned GrepAI provider lifecycle
implementation, organized behind a GrepAI package facade with prefix-free
filenames.

## Hot Path Summary

`__init__.py` re-exports the GrepAI public lifecycle surface. `core.py` derives
settings, layout, workspace config, container DSNs, and Docker image settings.
`backend.py` manages PostgreSQL/pgvector, `embedder.py` manages Ollama and model
readiness, `runner.py` manages the GrepAI runner image and watcher container,
and `actions.py` composes top-level install/status/start/stop/refresh/run
behavior. Status helpers include normalized container state so MCP
current-state packets can report running state, health, and uptime.

## Route Model

- `core.py` is configuration, layout, and workspace derivation.
- `backend.py` owns the Postgres container.
- `embedder.py` owns the Ollama container and configured model.
- `runner.py` owns the GrepAI image and watcher container.
- `actions.py` owns top-level GrepAI action composition.

## Invariants And Boundaries

- GrepAI remains Docker-or-bust; do not add host GrepAI or host Ollama fallbacks.
- Container-visible paths, Docker service names, and the shared Docker network
  are part of the provider contract.
- Status surfaces should include backend, embedder, and watcher container state
  so MCP current-state packets can report what is running now.
- Keep `__init__.py` as the package export facade.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The parent lifecycle facade imports the GrepAI package facade. | [__init__.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/__init__.py) |
| Provider lifecycle tests cover Docker-only GrepAI install, run, and watcher behavior. | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |

## Update History

- 2026-06-06T12:15: Re-verified against the current GrepAI lifecycle package; backend, embedder, runner, and action composition still match.
- 2026-05-28T12:32+02:00: Updated after GrepAI backend/embedder/watcher status began surfacing container-state summaries for provider current-state reporting.
- 2026-05-25T21:14+02:00: Moved under the provider-owned `providers/grepai/lifecycle/` route.
- 2026-05-25T19:09+02:00: Created when flat `grepai_*` lifecycle modules moved under `lifecycle_modules/grepai/` with prefix-free filenames.
