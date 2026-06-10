# mcp/src/agents_remember/providers/grepai/ - GrepAI Provider Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| sourceRoute            | `mcp/src/agents_remember/providers/grepai/` |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-06-10T10:30+02:00                     |
| lastVerifiedCommitHash | `592274a52cec61d97521771c630272c72240ed01` |
| lastVerifiedCommitDate | 2026-06-10T01:38:42+02:00|
| governingOverview      | `../../../../overview.md`                  |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Purpose

`grepai/` is the provider-owned home for Docker-only GrepAI setup, context
layout, workspace generation, and lifecycle operations. It replaces the former
top-level `grepai_setup.py` plus mixed `context_modules/grepai` and
`lifecycle_modules/grepai` routes.

## Hot Path Summary

Use `setup.py` for setup-time refresh/install wiring, `seed.py` for worktree
PostgreSQL database clone/reuse, and `isolated.py` for worktree-scoped provider
settings. Use `context/` for Docker runtime layout, workspace YAML, live memory
roots, and per-root `.gitignore` of grepai's `.grepai/` working dir. Use
`lifecycle/` for Postgres, Ollama, runner image/container, and high-level
GrepAI actions.

## Route Model

- `setup.py` wires enabled GrepAI setup through lifecycle commands.
- `seed.py` clones the source GrepAI database into an isolated worktree backend
  so embeddings can be reused instead of rebuilt. The clone runs under a stall
  watchdog (killed after `GREPAI_CLONE_STALL_SECONDS` of zero progress in dump
  growth / target database size) and is never capped by total duration — a
  wedge's signature is silence, not size (2.5.1).
- `isolated.py` rewrites provider settings for worktree-specific containers,
  roots, logs, and runtime paths while preserving the logical workspace key.
- `context/` owns GrepAI runtime layout, workspace config, and live-root indexing.
- `lifecycle/` owns Docker backend, embedder, runner, and top-level actions.

## Invariants And Boundaries

- GrepAI is Docker-or-bust; there is no host binary or host Ollama fallback.
- GrepAI-specific behavior belongs under this package, not in CGC modules or
  shared lifecycle helpers.
- Shared helpers must stay provider-agnostic.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| GrepAI setup delegates to provider lifecycle commands. | [setup.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/setup.py) |
| GrepAI context behavior is grouped under the provider-owned context package. | [context overview](context/overview.md) |
| GrepAI lifecycle behavior is grouped under the provider-owned lifecycle package. | [lifecycle overview](lifecycle/overview.md) |

## Update History

- 2026-06-10T10:30+02:00 — Route body caught up with 2.5.1: the `seed.py` clone stall watchdog and no-total-cap contract. Previous closeouts had only stamped the verification header (developer-flagged gap).
- 2026-06-06T12:15: Re-verified against the current GrepAI provider package; added the worktree database-clone (`seed.py`) and isolated-settings (`isolated.py`) surfaces.
- 2026-06-02T01:15+02:00: Updated for watch-live — `context/` now indexes the live memory roots in place and git-ignores grepai's `.grepai/` working dir; removed the `.grepai/` artifact-cleanup reference (`artifacts.py` deleted).
- 2026-05-25T21:14+02:00: Created when provider modules were reorganized provider-first under `providers/grepai/`.
