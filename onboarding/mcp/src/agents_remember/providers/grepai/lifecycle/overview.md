# mcp/src/agents_remember/providers/grepai/lifecycle/ - GrepAI Lifecycle Modules Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| sourceRoute            | `mcp/src/agents_remember/providers/grepai/lifecycle/` |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-06-10T07:40+02:00|
| lastVerifiedCommitHash | `ab7e21b4ab4b8526adcdad8ea2243657b8aea7a0` |
| lastVerifiedCommitDate | 2026-06-10T08:21:41+02:00|
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
current-state packets can report running state, health, and uptime; since
2.5.1 `runner.py` also reads the watcher's initial-scan log markers
(`Performing initial scan` / `Initial scan complete` since container start)
into an `initialScan` field, giving GrepAI real `indexing`/`indexed` states
instead of `unknown`.

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
- Modules in this route import context helpers from the leaf modules
  (`grepai.context`, `context.common`), never the `providers.context`
  aggregator: the aggregator star-imports this provider's context back, so
  routing through it is a circular import that breaks any entry point touching
  grepai modules first (2.5.1 fix).

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The parent lifecycle facade imports the GrepAI package facade. | [__init__.py](agents-remember/mcp/src/agents_remember/providers/lifecycle/__init__.py) |
| Provider lifecycle tests cover Docker-only GrepAI install, run, and watcher behavior. | [test_provider_lifecycle.py](agents-remember/mcp/tests/test_provider_lifecycle.py) |

## Update History

- 2026-06-10T07:40+02:00 — No route impact: `actions.py`/`backend.py`/`core.py`/`embedder.py` only updated the shared-helper import path to `providers/context_common.py` (GitHub #58).
- 2026-06-10T05:30+02:00 — Route body caught up with 2.5.1: `initialScan` scan-marker reading in `runner.py` and the leaf-import invariant (circular-import fix). Previous closeouts had only stamped the verification header (developer-flagged gap).
- 2026-06-06T12:15: Re-verified against the current GrepAI lifecycle package; backend, embedder, runner, and action composition still match.
- 2026-05-28T12:32+02:00: Updated after GrepAI backend/embedder/watcher status began surfacing container-state summaries for provider current-state reporting.
- 2026-05-25T21:14+02:00: Moved under the provider-owned `providers/grepai/lifecycle/` route.
- 2026-05-25T19:09+02:00: Created when flat `grepai_*` lifecycle modules moved under `lifecycle_modules/grepai/` with prefix-free filenames.
