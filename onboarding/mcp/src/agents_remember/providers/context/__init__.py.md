# mcp/src/agents_remember/providers/context/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/context/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T07:30+02:00     |
| lastVerifiedCommitHash | `ab7e21b4ab4b8526adcdad8ea2243657b8aea7a0` |
| lastVerifiedCommitDate | 2026-06-10T08:21:41+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

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

## Docs References

No live external documentation was needed for this closeout note. Provider
version pins and patch logic are represented directly in source.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed to prove the current package-local provider layout helpers. | n/a | n/a |

## Repo-Internal References

Same-repository source defines the active provider layout and patch behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Shared provider context helpers live in the common context module. | n/a | [common.py](agents-remember/mcp/src/agents_remember/providers/context/common.py) |
| CGC provider context constants, layout, cleanup, and patches live under the CGC provider package. | n/a | [CGC context overview](../cgc/context/overview.md) |
| GrepAI provider context layout, live-root workspace config, and artifact cleanup live under the GrepAI provider package. | n/a | [GrepAI context overview](../grepai/context/overview.md) |

## Cross-Repo References

No sibling repository evidence is needed; provider package behavior is mediated
through this package-local code and provider install/runtime modules.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Provider setup and lifecycle modules import this facade for runtime layout and install work. | n/a | [provider_setup.py](agents-remember/mcp/src/agents_remember/providers/provider_setup.py) |

## Update History

- 2026-06-10T07:30+02:00 — Shared helpers moved out to `providers/context_common.py`: importing `providers.context.common` initialized this facade, whose star-import of a mid-init `cgc.context` collected nothing and left the facade permanently missing every CGC name (import-order-dependent ImportError; GitHub #58). The facade now star-imports `context_common` alongside the two provider packages, and nothing loaded during their package inits re-enters this module.
- 2026-06-06T12:28+02:00: Corrected the GrepAI context reference from the old mirror-root model to current live-root workspace behavior; source behavior unchanged.
- 2026-05-29T18:35+02:00: Removed the unsupported computed `__all__` (relies on default star-export like the `cgc/context` facade), clearing the `reportUnsupportedDunderAll` warning; behavior-preserving (commit `0549b28`).
- 2026-05-25T21:14+02:00: Updated after provider context implementation moved into provider-owned packages.
- 2026-05-25T19:16+02:00: Renamed from `context_providers.py` to `context.py`; implementation moved into `context_modules/` with CGC and GrepAI subpackages and no compatibility fallback.
- 2026-05-25T18:07+02:00: Updated after the GrepAI runtime layout dropped the host binary path; the Docker runner image owns GrepAI binaries.
- 2026-05-25T17:40+02:00: Updated after GrepAI gained Docker network/runner/Ollama constants and workspace config support for container-visible project paths.
- 2026-05-24T19:25+02:00: Updated after CGC FalkorDB layout defaults stopped reading host `FALKORDB_*` environment variables.
- 2026-05-23T22:37+02:00: Created during quality-pass closeout after direct-closeout preview found the changed file lacked sidecar onboarding.
