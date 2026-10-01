# mcp/src/agents_remember/providers/context_common.py

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`context_common.py` contains shared provider context helpers that are not specific to CGC or GrepAI. It lives at the `providers/` package level — deliberately OUTSIDE the `providers/context/` facade package — so modules loaded during `cgc.context`/`grepai.context` package init can import it without re-entering the facade's own initialization.

## Code Commentary

### Logic

It defines `ContextProviderError` (subclass of `AgentsRememberError`), `to_container_path` (host → in-container POSIX path: Windows drive letter stripped, POSIX identity), template expansion, copied requirements-file helpers, provider pin parsing, generic provider state JSON writing, file hashing, and guarded runtime-path removal. `stable_provider_id` is no longer defined here; it is re-exported from `agents_remember.providers.identity` (its canonical source) so the `providers.context` facade still exposes the name.

`to_container_path` moved here from `cgc/context/core.py` (which keeps a re-export): it is provider-agnostic Docker plumbing. The module itself moved out of `providers/context/` in the same change: as `providers.context.common`, importing it initialized the parent facade package, and any import of `cgc.context` before `providers.context` re-entered the facade init mid-flight, star-collected an empty `cgc.context`, and left the facade permanently missing every CGC name — an import-order-dependent ImportError (GitHub #58). At `providers.context_common` no facade init is triggered, and its minimal imports (errors + identity only) keep it cycle-safe for low-level modules like `cgc/seed.py`.

### Invariants And Boundaries

- The `providers.context` facade star-exports this module's names; there is no `context_providers.py` compatibility fallback.
- This module must stay OUTSIDE the `providers/context/` package: moving it back re-creates the facade re-entrancy diamond.
- Provider runtime paths stay under configured provider roots unless a helper explicitly validates another source path.
- Keep this module's imports minimal (errors + identity); it is the cycle-safe import target for low-level provider modules, which must not import the `providers.context` or `cgc.context` package facades.

## Evidence

### Repo-Internal References

- CGC context module imports shared error, path, pin, and removal helpers from here. [1]
- GrepAI context module imports shared error, path, pin, and removal helpers from here. [2]
