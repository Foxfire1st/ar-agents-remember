# mcp/src/agents_remember/providers/grepai/context/constants.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/grepai/context/constants.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-02T01:15+02:00                     |
| lastVerifiedCommitHash | `ab8dda6269c2f8a69c341ae950c2e74d4ab3fe44` |
| lastVerifiedCommitDate | 2026-06-02T01:10:22+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`grepai/constants.py` centralizes Docker-owned GrepAI provider identifiers, pins, image/container names, and default loopback ports.

## Code Commentary

### Logic

The module is constant-only: it declares the GrepAI package pin, Docker network, runner/Postgres/Ollama container names, default host ports, and image references used by the context and lifecycle GrepAI modules.

### Invariants And Boundaries

- GrepAI is Docker-owned; these constants do not point to a host `_bin` or `_venv` install path.
- `.grepai` is grepai's per-root working dir; it lives inside each live indexed root and is kept out of git via the root's `.gitignore` (see `layout.py`).
- This file is imported through `providers.context`; there is no `context_providers.py` compatibility fallback.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| GrepAI layout consumes these constants for provider-owned runtime paths. | [layout.py](layout.py.md) |
| GrepAI lifecycle modules consume Docker container/image constants through `providers.context`. | [core.py](../lifecycle/core.py.md) |

## Update History

- 2026-06-02T01:15+02:00: Removed `GREPAI_ROOT_ARTIFACT_NAMES` (and the artifact-cleanup reference) after `artifacts.py` was deleted; `.grepai/` is now git-ignored in each live root rather than guarded.
- 2026-05-25T19:33+02:00: Created when GrepAI context constants were split out of `grepai/core.py`.
