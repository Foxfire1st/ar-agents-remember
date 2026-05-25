# mcp/src/agents_remember/providers/context_modules/ - Provider Context Modules Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| sourceRoute            | `mcp/src/agents_remember/providers/context_modules/` |
| doc_type               | `route-overview`                           |
| lastUpdated            | 2026-05-25T19:33+02:00                     |
| lastVerifiedCommitHash | `a8ee8440dfa920d1153a4bb4bb43cc77534c3c90` |
| lastVerifiedCommitDate | 2026-05-25T15:22:52+02:00                  |
| governingOverview      | `../../../../overview.md`                  |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Purpose

`context_modules/` contains the extracted implementation for provider context layout, settings expansion, runtime cleanup, and patch support. The route replaces the former monolithic `context_providers.py`; `providers.context` is now the only public facade.

## Hot Path Summary

Start with `common.py` for shared error, pin, template, state, hash, and removal helpers. CGC behavior lives under `cgc/`: `constants.py` owns provider constants and patch snippets, `core.py` owns runtime layout/config/artifact cleanup, and `patches.py` owns upstream module discovery and idempotent patch application. GrepAI behavior lives under `grepai/`: `constants.py` owns Docker defaults, `layout.py` owns runtime layout and mirror roots, `workspace.py` owns workspace YAML, and `artifacts.py` owns `.grepai/` cleanup.

## Route Model

- Shared helper primitives live in `common.py`.
- `cgc/` owns CodeGraphContext provider context layout and patch behavior.
- `grepai/` owns Docker-owned GrepAI provider context layout and workspace behavior.
- `providers.context` re-exports this route as the public API.

## Invariants And Boundaries

- There is no `context_providers.py` compatibility module.
- CGC venv/runtime layout remains CGC-specific and lives under `cgc/`.
- GrepAI remains Docker-owned; the runner image owns the GrepAI binary.
- Common modules must stay provider-agnostic.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Public context exports are collected by the facade. | [context.py](../context.py.md) |
| CGC context behavior is grouped under the CGC subpackage. | [CGC context overview](cgc/overview.md) |
| GrepAI context behavior is grouped under the GrepAI subpackage. | [GrepAI context overview](grepai/overview.md) |

## Update History

- 2026-05-25T19:33+02:00: Updated after GrepAI context logic was split out of `grepai/core.py` into focused submodules.
- 2026-05-25T19:16+02:00: Created when provider context logic was split out of `context_providers.py` into focused modules.
