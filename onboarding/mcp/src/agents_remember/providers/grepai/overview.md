# mcp/src/agents_remember/providers/grepai/ - GrepAI Provider Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| sourceRoute            | `mcp/src/agents_remember/providers/grepai/` |
| doc_type               | `route-overview`                           |
| lastUpdated            | 2026-06-02T01:15+02:00                     |
| lastVerifiedCommitHash | `ae9c4e5b6af38eda7f2b29006130c4263e9db62f` |
| lastVerifiedCommitDate | 2026-05-25T19:55:09+02:00                  |
| governingOverview      | `../../../../overview.md`                  |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Purpose

`grepai/` is the provider-owned home for Docker-only GrepAI setup, context
layout, workspace generation, and lifecycle operations. It replaces the former
top-level `grepai_setup.py` plus mixed `context_modules/grepai` and
`lifecycle_modules/grepai` routes.

## Hot Path Summary

Use `setup.py` for setup-time refresh/install wiring. Use `context/` for
Docker runtime layout, workspace YAML, and per-root `.gitignore` of grepai's
`.grepai/` working dir. Use `lifecycle/` for Postgres, Ollama, runner
image/container, and high-level GrepAI actions.

## Route Model

- `setup.py` wires enabled GrepAI setup through lifecycle commands.
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

- 2026-06-02T01:15+02:00: Updated for watch-live — `context/` now indexes the live memory roots in place and git-ignores grepai's `.grepai/` working dir; removed the `.grepai/` artifact-cleanup reference (`artifacts.py` deleted).
- 2026-05-25T21:14+02:00: Created when provider modules were reorganized provider-first under `providers/grepai/`.
