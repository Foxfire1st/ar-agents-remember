# mcp/src/agents_remember/providers/context/ - Provider Context Facade Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| sourceRoute            | `mcp/src/agents_remember/providers/context/` |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-06-10T07:05+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| Public context exports are collected by the package facade. | "starred submodules" | mcp/src/agents_remember/providers/context/__init__.py:18-18 |
| CGC context behavior is grouped under the CGC provider package. | `## Layout Construction Is Now Four Named Things` | onboarding/mcp/src/agents_remember/providers/cgc/context/overview.md:28-50 |
| GrepAI context behavior is grouped under the GrepAI provider package. | `## Layout Construction Is Now Three Named Things` | onboarding/mcp/src/agents_remember/providers/grepai/context/overview.md:21-44 |

## Update History

- 2026-08-02T17:36:56+02:00 — 260731-EFA-L6 curator W1-B09: repaired 6 citation finding(s); scoped recheck clean.

- 2026-06-10T07:30+02:00 — `common.py` moved out of this package to `providers/context_common.py`: importing it here initialized the facade mid-`cgc.context`-init and left the facade permanently missing CGC names (GitHub #58). Added the no-shared-helpers-inside invariant.
- 2026-06-10T07:05+02:00 — `to_container_path` canonical home moved into the shared helpers module (GitHub #58); documented the facade star-import diamond and the minimal-imports rule.
- 2026-06-06T12:15: Re-verified against the current shared provider-context facade; corrected the CGC boundary wording after CGC became Docker-runner owned.
- 2026-05-25T21:14+02:00: Updated when provider context implementation moved to provider-first packages.
- 2026-05-25T19:33+02:00: Updated after GrepAI context logic was split out of `grepai/core.py` into focused submodules.
- 2026-05-25T19:16+02:00: Created when provider context logic was split out of `context_providers.py` into focused modules.
