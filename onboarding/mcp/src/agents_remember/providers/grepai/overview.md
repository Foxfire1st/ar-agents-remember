# mcp/src/agents_remember/providers/grepai/ - GrepAI Provider Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| sourceRoute            | `mcp/src/agents_remember/providers/grepai/` |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-06-28T19:10+02:00     |
| lastVerifiedCommitHash | `9d58058e3ce4815b0356794fc21973ebe9c71345` |
| lastVerifiedCommitDate | 2026-07-06T11:47:10+02:00|
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
settings that keep the multi-root provider shape while swapping only the active
project root to the task memory worktree. Use `context/` for Docker runtime layout, workspace YAML, live memory
roots, and per-root `.gitignore` of grepai's `.grepai/` working dir. Use
`lifecycle/` for Postgres, Ollama, runner image/container, and high-level
GrepAI actions. The lifecycle package owns the current preferred auto host
ports (`61432` for Postgres, `61434` for Ollama); Docker container service
ports stay `5432` and `11434`.

## Route Model

- `setup.py` wires enabled GrepAI setup through lifecycle commands and
  announces its phases (`grepai install`, `grepai clone-db`) through the
  provider setup progress sink so background worktree setup is observable
  (GitHub #53).
- `seed.py` clones the source GrepAI database into an isolated worktree backend
  so embeddings can be reused instead of rebuilt. The clone runs under a stall
  watchdog (killed after `GREPAI_CLONE_STALL_SECONDS` of zero progress in dump
  growth / target database size) and is never capped by total duration — a
  wedge's signature is silence, not size (2.5.1). A benchmark-scoped target is
  refused up front (`_clone_skip`) so a benchmark never clones from another
  stack (hermetic; task 260619).
- `isolated.py` rewrites provider settings for worktree-specific containers,
  roots, logs, and runtime paths while preserving the logical workspace key and
  leaving unrelated repository roots on their configured paths.
- `context/` owns GrepAI runtime layout, workspace config, and live-root indexing.
- `lifecycle/` owns Docker backend, embedder, runner, and top-level actions.

## Invariants And Boundaries

- GrepAI is Docker-or-bust; there is no host binary or host Ollama fallback.
- GrepAI can be one aggregate provider instance with multiple addressable
  project roots; worktree isolation rewrites only the active project root.
- GrepAI-specific behavior belongs under this package, not in CGC modules or
  shared lifecycle helpers.
- Shared helpers must stay provider-agnostic.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| GrepAI setup delegates to provider lifecycle commands. | [setup.py](agents-remember/mcp/src/agents_remember/providers/grepai/setup.py) |
| GrepAI context behavior is grouped under the provider-owned context package. | [context overview](context/overview.md) |
| GrepAI lifecycle behavior is grouped under the provider-owned lifecycle package. | [lifecycle overview](lifecycle/overview.md) |

## Update History

- 2026-06-28T19:10+02:00 — Main-carryover reconciliation (PR #95, code 84e95ad): restored the `_clone_skip` benchmark-scoped hermetic guard (task 260619 / MCP 2.9.2) that the series carryover had dropped, while keeping the series' Task 12 multi-root / preferred-host-port content. The merged tree at 84e95ad has both.
- 2026-06-25T09:55+02:00 — No route model change: child context/lifecycle routes now record GrepAI's preferred auto host ports (`61432`/`61434`) separately from container service ports (`5432`/`11434`).
- 2026-06-23T22:31+02:00 — Clarified the worktree-isolation invariant behind Task 12 provider
  projection: GrepAI remains a multi-root provider instance while only the active project root is
  redirected to the task memory worktree. Verification metadata will be stamped at closeout.
- 2026-06-10T07:50+02:00 — GitHub #53: `setup.py` announces install/clone-db phases through the setup progress sink for background worktree provider setup.
- 2026-06-10T05:30+02:00 — Route body caught up with 2.5.1: the `seed.py` clone stall watchdog and no-total-cap contract. Previous closeouts had only stamped the verification header (developer-flagged gap).
- 2026-06-06T12:15: Re-verified against the current GrepAI provider package; added the worktree database-clone (`seed.py`) and isolated-settings (`isolated.py`) surfaces.
- 2026-06-02T01:15+02:00: Updated for watch-live — `context/` now indexes the live memory roots in place and git-ignores grepai's `.grepai/` working dir; removed the `.grepai/` artifact-cleanup reference (`artifacts.py` deleted).
- 2026-05-25T21:14+02:00: Created when provider modules were reorganized provider-first under `providers/grepai/`.
