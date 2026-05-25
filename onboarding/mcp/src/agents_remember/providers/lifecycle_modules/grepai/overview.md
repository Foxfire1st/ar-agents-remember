# mcp/src/agents_remember/providers/lifecycle_modules/grepai/ - GrepAI Lifecycle Modules Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| sourceRoute            | `mcp/src/agents_remember/providers/lifecycle_modules/grepai/` |
| doc_type               | `route-overview`                           |
| lastUpdated            | 2026-05-25T19:09+02:00                     |
| lastVerifiedCommitHash | `a8ee8440dfa920d1153a4bb4bb43cc77534c3c90` |
| lastVerifiedCommitDate | 2026-05-25T15:22:52+02:00                  |
| governingOverview      | `../overview.md`                           |

## Governing Overview

[Provider Lifecycle Modules Overview](../overview.md)

## Purpose

`grepai/` contains the Docker-owned GrepAI provider lifecycle implementation.
The subpackage is the former flat `grepai_*` module group, now organized behind
a GrepAI package facade with prefix-free filenames.

## Hot Path Summary

`__init__.py` re-exports the GrepAI public lifecycle surface. `core.py` derives
settings, layout, workspace config, container DSNs, and Docker image settings.
`backend.py` manages PostgreSQL/pgvector, `embedder.py` manages Ollama and model
readiness, `runner.py` manages the GrepAI runner image and watcher container,
and `actions.py` composes top-level install/status/start/stop/refresh/run
behavior.

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
- Keep `__init__.py` as the package export facade.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The parent lifecycle facade imports the GrepAI package facade. | [lifecycle.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle.py) |
| Provider lifecycle tests cover Docker-only GrepAI install, run, and watcher behavior. | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |

## Update History

- 2026-05-25T19:09+02:00: Created when flat `grepai_*` lifecycle modules moved under `lifecycle_modules/grepai/` with prefix-free filenames.
