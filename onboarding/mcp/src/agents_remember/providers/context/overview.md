# mcp/src/agents_remember/providers/context/ - Provider Context Facade Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| sourceRoute            | `mcp/src/agents_remember/providers/context/` |

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

## Evidence

### Repo-Internal References

- Public context exports are collected by the package facade. [1]
- CGC context behavior is grouped under the CGC provider package. [2]
- GrepAI context behavior is grouped under the GrepAI provider package. [3]
