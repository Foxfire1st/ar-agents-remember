# mcp/src/agents_remember/providers/context/ - Provider Context Facade Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| sourceRoute            | `mcp/src/agents_remember/providers/context/` |
| doc_type               | `route-overview`                           |
| lastUpdated            | 2026-05-25T21:14+02:00                     |
| lastVerifiedCommitHash | `a8ee8440dfa920d1153a4bb4bb43cc77534c3c90` |
| lastVerifiedCommitDate | 2026-05-25T15:22:52+02:00                  |
| governingOverview      | `../../../../overview.md`                  |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Purpose

`context/` contains the public provider-context facade and shared context helpers. Provider-specific context implementations now live under `providers/cgc/context/` and `providers/grepai/context/`.

## Hot Path Summary

Start with `__init__.py` for the public context facade and `common.py` for shared error, pin, template, state, hash, and removal helpers. CGC behavior lives under `../cgc/context/`; GrepAI behavior lives under `../grepai/context/`.

## Route Model

- Shared helper primitives live in `common.py`.
- `../cgc/context/` owns CodeGraphContext provider context layout and patch behavior.
- `../grepai/context/` owns Docker-owned GrepAI provider context layout and workspace behavior.
- `providers.context` re-exports this route as the public API.

## Invariants And Boundaries

- There is no `context_providers.py` compatibility module.
- CGC venv/runtime layout remains CGC-specific and lives under `cgc/`.
- GrepAI remains Docker-owned; the runner image owns the GrepAI binary.
- Common modules must stay provider-agnostic.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Public context exports are collected by the package facade. | [__init__.py](agents-remember-md/mcp/src/agents_remember/providers/context/__init__.py) |
| CGC context behavior is grouped under the CGC provider package. | [CGC context overview](../cgc/context/overview.md) |
| GrepAI context behavior is grouped under the GrepAI provider package. | [GrepAI context overview](../grepai/context/overview.md) |

## Update History

- 2026-05-25T21:14+02:00: Updated when provider context implementation moved to provider-first packages.
- 2026-05-25T19:33+02:00: Updated after GrepAI context logic was split out of `grepai/core.py` into focused submodules.
- 2026-05-25T19:16+02:00: Created when provider context logic was split out of `context_providers.py` into focused modules.
