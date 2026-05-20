# settings.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/system/defaults/examples/coordinator/settings.md`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-20T20:01+02:00                     |
| lastVerifiedCommitHash | `e4ae4955d888d3ce58b55b5ca99d20039cbcb214` |
| lastVerifiedCommitDate | 2026-05-20T20:01:26+02:00 |

## Purpose

This file is the human-facing coordinator settings example for `ar-coordination/system/settings.md`, including the human-readable doctrine for optional context providers.

## Code Commentary

### Logic

The example describes the coordinator as workspace-wide routing and workflow state. It lists global instructions, shared tools, workspace source registries, task/worktree roots, notes, selected memory repos, and operator conventions as coordinator-owned surfaces. The context provider section frames providers as local discovery accelerators, maps semantic discovery to GrepAI, relationship discovery to CodeGraphContext, and intent retrieval back to onboarding plus bounded source confirmation.

### Conventions

Repo-specific rules belong in the selected memory layer rather than this coordinator settings file. Provider settings should stay declarative: configured roots, runtime locations, watch modes, freshness hooks, and transport policy belong in settings, while start/stop/status/refresh behavior belongs in lifecycle tooling.

### Invariants And Boundaries

C-08 remains the route from coordinator context into the target repository's active memory settings, tools, sources, onboarding, and ledger paths. Context providers must not replace source proof, verified onboarding, drift checks, branch validity, or memory promotion rules. CGC runtime artifacts must stay under `providers/codegraphcontext/<repo-id>/.codegraphcontext/`, and its process-only env keys must not be persisted into `.env` when CGC v0.4.10 rejects them as invalid config.

### Todos

None.

### Docs References

No external documentation is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The example states that coordinator settings are workspace-wide and do not replace per-repository memory settings. | L1-L8 | [runtime/system/defaults/examples/coordinator/settings.md](agents-remember-md/runtime/system/defaults/examples/coordinator/settings.md) |
| The scope list names global instructions, shared commands, workspace sources, roots, notes, selected memory repos, and operator conventions as coordinator concerns. | L10-L25 | [runtime/system/defaults/examples/coordinator/settings.md](agents-remember-md/runtime/system/defaults/examples/coordinator/settings.md) |
| The routing section tells agents to invoke C-08 and treat repository-specific memory guidance as more specific. | L40-L48 | [runtime/system/defaults/examples/coordinator/settings.md](agents-remember-md/runtime/system/defaults/examples/coordinator/settings.md) |
| The context provider section defines semantic, relationship, and intent retrieval substrates, keeps provider settings declarative, and requires provider installs to be coordination-owned. | L50-L74 | [runtime/system/defaults/examples/coordinator/settings.md](agents-remember-md/runtime/system/defaults/examples/coordinator/settings.md) |
| The CGC notes require runtime artifacts under `providers/codegraphcontext/<repo-id>/.codegraphcontext/`, keep process-only Kuzu env keys out of persisted `.env`, and reject source-repo `.cgcignore` creation in managed mode. | L76-L90 | [runtime/system/defaults/examples/coordinator/settings.md](agents-remember-md/runtime/system/defaults/examples/coordinator/settings.md) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-20T19:11+02:00: Documented context provider doctrine for semantic, relationship, and intent retrieval plus CGC containment and `.env` caveats.
- 2026-05-13T13:38: Created onboarding for the coordinator settings Markdown example.
