# mcp/src/agents_remember/providers/context.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/context.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:16+02:00                     |
| lastVerifiedCommitHash | `ae9c4e5b6af38eda7f2b29006130c4263e9db62f` |
| lastVerifiedCommitDate | 2026-05-25T19:55:09+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`context.py` is the public provider context facade. It re-exports the split
context provider modules for shared helpers, CodeGraphContext layout/patch
behavior, and Docker-owned GrepAI layout/workspace behavior.

## Code Commentary

### Logic

The facade imports all public names from `context_modules.common`,
`context_modules.cgc`, and `context_modules.grepai`, then builds `__all__` from
those public globals. Implementation belongs in `context_modules/`; callers use
this facade directly.

### Conventions

Provider runtime paths are derived from coordinator provider roots rather than
caller-supplied host paths. GrepAI root artifacts and CGC source artifacts are
treated as runtime/cache state that must not leak into durable memory or source
trees. GrepAI workspace configuration can substitute container-visible project
paths while the host-side layout remains provider-owned.

### Invariants And Boundaries

- Keep the facade import-only; implementation belongs in `context_modules/`.
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
| Shared provider context helpers live in the common context module. | n/a | [common.py](agents-remember-md/mcp/src/agents_remember/providers/context_modules/common.py) |
| CGC provider context constants, layout, cleanup, and patches live under the CGC context subpackage. | n/a | [CGC context overview](context_modules/cgc/overview.md) |
| GrepAI provider context layout, mirror roots, workspace config, and artifact cleanup live under the GrepAI context subpackage. | n/a | [GrepAI context overview](context_modules/grepai/overview.md) |

## Cross-Repo References

No sibling repository evidence is needed; provider package behavior is mediated
through this package-local code and provider install/runtime modules.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Provider setup and lifecycle modules import this facade for runtime layout and install work. | n/a | [provider_setup.py](agents-remember-md/mcp/src/agents_remember/providers/provider_setup.py) |

## Update History

- 2026-05-25T19:16+02:00: Renamed from `context_providers.py` to `context.py`; implementation moved into `context_modules/` with CGC and GrepAI subpackages and no compatibility fallback.
- 2026-05-25T18:07+02:00: Updated after the GrepAI runtime layout dropped the host binary path; the Docker runner image owns GrepAI binaries.
- 2026-05-25T17:40+02:00: Updated after GrepAI gained Docker network/runner/Ollama constants and workspace config support for container-visible project paths.
- 2026-05-24T19:25+02:00: Updated after CGC FalkorDB layout defaults stopped reading host `FALKORDB_*` environment variables.
- 2026-05-23T22:37+02:00: Created during quality-pass closeout after direct-closeout preview found the changed file lacked sidecar onboarding.
