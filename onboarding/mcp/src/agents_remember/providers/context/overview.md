# mcp/src/agents_remember/providers/context/ - Provider Context Facade Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| sourceRoute            | `mcp/src/agents_remember/providers/context/` |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-06-10T07:05+02:00                     |
| lastVerifiedCommitHash | `ab7e21b4ab4b8526adcdad8ea2243657b8aea7a0` |
| lastVerifiedCommitDate | 2026-06-10T08:21:41+02:00|
| governingOverview      | `../../../../overview.md`                  |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Purpose

`context/` contains the public provider-context facade and shared context helpers. Provider-specific context implementations now live under `providers/cgc/context/` and `providers/grepai/context/`.

## Hot Path Summary

Start with `__init__.py` for the public context facade. Shared error, pin, template, state, hash, removal, and host→container path helpers (`to_container_path` — drive letter stripped on Windows, identity on POSIX) live in `../context_common.py`, deliberately OUTSIDE this package (GitHub #58). CGC behavior lives under `../cgc/context/`; GrepAI behavior lives under `../grepai/context/`.

## Route Model

- Shared helper primitives live in `../context_common.py` (outside this package).
- `../cgc/context/` owns CodeGraphContext provider context layout and patch behavior.
- `../grepai/context/` owns Docker-owned GrepAI provider context layout and workspace behavior.
- `providers.context` re-exports this route as the public API.

## Invariants And Boundaries

- There is no `context_providers.py` compatibility module.
- CGC runtime layout remains CGC-specific and lives under `cgc/`.
- GrepAI remains Docker-owned; the runner image owns the GrepAI binary.
- Common modules must stay provider-agnostic.
- `common.py` keeps minimal imports (errors + identity): it is the cycle-safe
  import target for low-level provider modules. The package facades
  (`providers.context`, `cgc.context`, `grepai.context`) form a star-import
  diamond — importing a facade from a module that loads during a facade's own
  init leaves `providers.context` permanently missing names (GitHub #58).

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Public context exports are collected by the package facade. | [__init__.py](agents-remember-md/mcp/src/agents_remember/providers/context/__init__.py) |
| CGC context behavior is grouped under the CGC provider package. | [CGC context overview](../cgc/context/overview.md) |
| GrepAI context behavior is grouped under the GrepAI provider package. | [GrepAI context overview](../grepai/context/overview.md) |

## Update History

- 2026-06-10T07:30+02:00 — `common.py` moved out of this package to `providers/context_common.py`: importing it here initialized the facade mid-`cgc.context`-init and left the facade permanently missing CGC names (GitHub #58). Added the no-shared-helpers-inside invariant.
- 2026-06-10T07:05+02:00 — `to_container_path` canonical home moved into the shared helpers module (GitHub #58); documented the facade star-import diamond and the minimal-imports rule.
- 2026-06-06T12:15: Re-verified against the current shared provider-context facade; corrected the CGC boundary wording after CGC became Docker-runner owned.
- 2026-05-25T21:14+02:00: Updated when provider context implementation moved to provider-first packages.
- 2026-05-25T19:33+02:00: Updated after GrepAI context logic was split out of `grepai/core.py` into focused submodules.
- 2026-05-25T19:16+02:00: Created when provider context logic was split out of `context_providers.py` into focused modules.
