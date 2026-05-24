# mcp/src/agents_remember/providers/context_providers.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/context_providers.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T19:25+02:00                     |
| lastVerifiedCommitHash | `31846c1136f0fe75503a63fb557303a79fa022e8` |
| lastVerifiedCommitDate | 2026-05-24T23:07:31+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`context_providers.py` owns provider runtime layout helpers, provider-owned
requirements/binary paths, GrepAI workspace configuration, CGC runtime layout,
provider artifact cleanup, and managed CodeGraphContext patch application.

## Code Commentary

### Logic

The module defines pinned provider package names, runtime artifact names, Docker
backend identifiers, provider layout dataclasses, path expansion helpers,
requirements/binary helpers, GrepAI workspace-mode root and config generation,
CGC runtime layout derivation, source/provider artifact containment checks, and
CGC patch detectors/applicators for upstream package files.

CGC FalkorDB process environment is derived from package/MCP provider defaults
and recorded backend state. Ambient host `FALKORDB_HOST` and `FALKORDB_PORT`
environment variables are not an authority source for layout defaults.

### Conventions

Provider runtime paths are derived from coordinator provider roots rather than
caller-supplied host paths. GrepAI root artifacts and CGC source artifacts are
treated as runtime/cache state that must not leak into durable memory or source
trees.

### Invariants And Boundaries

- Provider binaries belong under `providers/_bin/`.
- Provider venvs belong under `providers/_venvs/`.
- Provider instances, cache, state, and mirrored roots belong under
  `providers/runners/`.
- Durable provider database data belongs under `providers/data/`.
- CGC backend host/port values come from provider settings and backend state,
  not ambient process environment.
- Upstream CGC patches should be detected by marker text before being applied.

### Todos

- This file remains large and should be split during Phase 06 into layout,
  GrepAI, CGC, cleanup, and patch modules.

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
| The module defines CGC and GrepAI pins, Docker backend names, runtime artifact names, and provider artifact exclusion keys. | L14-L41; L56-L83 | [context_providers.py](agents-remember-md/mcp/src/agents_remember/providers/context_providers.py) |
| `CgcRuntimeLayout`, `GrepaiMemoryRoot`, and `GrepaiRuntimeLayout` capture provider runtime paths and backend settings. | L338-L455 | [context_providers.py](agents-remember-md/mcp/src/agents_remember/providers/context_providers.py) |
| Requirements, binary, GrepAI root/config, and CGC layout helpers derive runtime paths from coordinator/provider settings. | L474-L839; L852-L1121 | [context_providers.py](agents-remember-md/mcp/src/agents_remember/providers/context_providers.py) |
| Artifact containment and cleanup helpers identify source-tree CGC artifacts and memory-root GrepAI artifacts as removable runtime state. | L1138-L1206 | [context_providers.py](agents-remember-md/mcp/src/agents_remember/providers/context_providers.py) |
| CGC patch detector/applicator helpers locate upstream modules and apply marker-based runtime patches. | L1253-L1546 | [context_providers.py](agents-remember-md/mcp/src/agents_remember/providers/context_providers.py) |

## Cross-Repo References

No sibling repository evidence is needed; provider package behavior is mediated
through this package-local code and provider install/runtime modules.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Provider setup and lifecycle modules import these helpers for runtime layout and install work. | L8-L12; L78-L83 | [provider_setup.py](agents-remember-md/mcp/src/agents_remember/providers/provider_setup.py) |

## Update History

- 2026-05-24T19:25+02:00: Updated after CGC FalkorDB layout defaults stopped reading host `FALKORDB_*` environment variables.
- 2026-05-23T22:37+02:00: Created during quality-pass closeout after direct-closeout preview found the changed file lacked sidecar onboarding.
