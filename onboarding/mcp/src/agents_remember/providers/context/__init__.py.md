# mcp/src/agents_remember/providers/context/__init__.py

## Governing Overview

[mcp/overview.md](overview.md)

## Purpose

`providers.context` is the public provider context facade. It re-exports the split
context provider modules for shared helpers, CodeGraphContext layout/patch
behavior, and Docker-owned GrepAI layout/workspace behavior.

## Code Commentary

### Logic

The facade imports all public names from `providers.context.common`,
`providers.cgc.context`, and `providers.grepai.context`, then builds `__all__`
from those public globals. Provider-specific implementation belongs in the
provider-owned packages; callers use this facade directly.

Shared helpers were moved OUT of this package to `providers/context_common.py`
(GitHub #58): importing `providers.context.common` initialized this facade,
whose star-import of a mid-init `cgc.context` collected nothing and left the
facade permanently missing every CGC name — an import-order-dependent
ImportError. The facade now star-imports `context_common` alongside the two
provider context packages, and nothing loaded during their package inits
re-enters this module.

### Conventions

Provider runtime paths are derived from coordinator provider roots rather than
caller-supplied host paths. GrepAI root artifacts and CGC source artifacts are
treated as runtime/cache state that must not leak into durable memory or source
trees. GrepAI workspace configuration can substitute container-visible project
paths while the host-side layout remains provider-owned.

### Invariants And Boundaries

- Keep the facade import-only; implementation belongs in provider-owned
  context packages.
- There is no `context_providers.py` compatibility module.
- Keep old public symbol names available here while callers use the direct
  `providers.context` facade.

## Evidence

### Docs References

No live external documentation was needed for this closeout note. Provider
version pins and patch logic are represented directly in source.

No relevant external documentation is needed to prove the current package-local provider layout helpers.

### Repo-Internal References

Same-repository source defines the active provider layout and patch behavior.

- Shared provider context helpers live in the common context module. [1]
- CGC provider context constants, layout, cleanup, and patches live under the CGC provider package. [2]
- GrepAI provider context layout, live-root workspace config, and artifact cleanup live under the GrepAI provider package. [3]

### Cross-Repo References

No sibling repository evidence is needed; provider package behavior is mediated
through this package-local code and provider install/runtime modules.

- Provider setup and lifecycle modules import this facade for runtime layout and install work. [4]
