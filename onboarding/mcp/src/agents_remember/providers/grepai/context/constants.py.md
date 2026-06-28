# mcp/src/agents_remember/providers/grepai/context/constants.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/grepai/context/constants.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-25T09:55+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
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

| Finding | Source Path |
| --- | --- |
| GrepAI layout consumes these constants for provider-owned runtime paths. | [layout.py](layout.py.md) |
| GrepAI lifecycle modules consume Docker container/image constants through `providers.context`. | [core.py](../lifecycle/core.py.md) |

## Update History

- 2026-06-25T09:55+02:00: Changed managed GrepAI's preferred auto host ports to Postgres `61432` and Ollama `61434`; container ports remain configured by lifecycle settings.
- 2026-06-02T01:15+02:00: Removed `GREPAI_ROOT_ARTIFACT_NAMES` (and the artifact-cleanup reference) after `artifacts.py` was deleted; `.grepai/` is now git-ignored in each live root rather than guarded.
- 2026-05-25T19:33+02:00: Created when GrepAI context constants were split out of `grepai/core.py`.
