# mcp/src/agents_remember/providers/grepai/context/constants.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/grepai/context/constants.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-25T09:55+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`grepai/constants.py` centralizes Docker-owned GrepAI provider identifiers, pins, image/container names, and preferred loopback host ports.

## Code Commentary

### Logic

The module is constant-only: it declares the GrepAI package pin, Docker network, runner/Postgres/Ollama container names, preferred host ports, and image references used by the context and lifecycle GrepAI modules. The managed provider prefers host `61432` for Postgres and host `61434` for Ollama when a host port is configured as `auto`; the Docker container ports remain owned by the lifecycle settings (`5432` and `11434` respectively).

### Invariants And Boundaries

- GrepAI is Docker-owned; these constants do not point to a host `_bin` or `_venv` install path.
- Preferred host ports intentionally avoid common neighboring service ports `5432` and `11434`.
- `.grepai` is grepai's per-root working dir; it lives inside each live indexed root and is kept out of git via the root's `.gitignore` (see `layout.py`).
- This file is imported through `providers.context`; there is no `context_providers.py` compatibility fallback.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| GrepAI layout consumes these constants for provider-owned runtime paths through `grepai_runtime_layout`. | `grepai_runtime_layout` | mcp/src/agents_remember/providers/grepai/context/layout.py:111-156 |
| GrepAI lifecycle modules consume Docker container/image constants through `grepai_network_name`, `grepai_runner_settings`, and `grepai_backend_settings` in `providers.context`. | `grepai_network_name`; `grepai_runner_settings`; `grepai_backend_settings` | mcp/src/agents_remember/providers/grepai/lifecycle/core.py:148-152; mcp/src/agents_remember/providers/grepai/lifecycle/core.py:166-189; mcp/src/agents_remember/providers/grepai/lifecycle/core.py:339-362 |

## Update History
- 2026-08-03T02:57+02:00 — W3-B03 curator: curated 2 table citations for the runtime layout and backend/network settings; fixer-generated ranges verified.

- 2026-06-25T09:55+02:00: Changed managed GrepAI's preferred auto host ports to Postgres `61432` and Ollama `61434`; container ports remain configured by lifecycle settings.
- 2026-06-02T01:15+02:00: Removed `GREPAI_ROOT_ARTIFACT_NAMES` (and the artifact-cleanup reference) after `artifacts.py` was deleted; `.grepai/` is now git-ignored in each live root rather than guarded.
- 2026-05-25T19:33+02:00: Created when GrepAI context constants were split out of `grepai/core.py`.
