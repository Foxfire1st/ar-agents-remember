# tools.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/system/defaults/examples/coordinator/tools.md`     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-20T20:01+02:00                     |
| lastVerifiedCommitHash | `e4ae4955d888d3ce58b55b5ca99d20039cbcb214` |
| lastVerifiedCommitDate | 2026-05-20T20:01:26+02:00 |

## Purpose

This example documents the coordinator-level tools surface, including expected manual command shapes for configured context providers before or beside lifecycle tooling.

## Code Commentary

### Logic

The file says coordinator tools are commands useful across many repositories. Repo-specific checks, branch workflow, and coding tools belong in memory-layer `system/tools.md`. When `contextProviders` are enabled, it records bounded GrepAI status/search commands and CodeGraphContext install/doctor command shapes that keep provider output small and run CGC with explicit contained runtime environment.

### Conventions

Global commands stay here; repository-specific command details stay in the selected memory layer. CGC Kuzu runtime env keys are process env only; for CGC v0.4.10 they should not be written into `<runtimeRoot>/.codegraphcontext/.env`.

### Invariants And Boundaries

Agents should resolve the target repository with C-08 before choosing task, worktree, memory, validation paths, or context provider roots. Provider output is discovery evidence only, and source/onboarding proof remains required.

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
| The coordinator tools example separates global commands from repository-specific checks and branch workflow. | L1-L9; L52-L56 | [runtime/system/defaults/examples/coordinator/tools.md](agents-remember-md/runtime/system/defaults/examples/coordinator/tools.md) |
| The provider command section records GrepAI status/search probes and CGC install/doctor command shapes using the shared provider venv, pinned requirements file, and contained process env. | L13-L40 | [runtime/system/defaults/examples/coordinator/tools.md](agents-remember-md/runtime/system/defaults/examples/coordinator/tools.md) |
| The CGC notes distinguish process env from persisted `.env` and require containment checks before managed use. | L42-L50 | [runtime/system/defaults/examples/coordinator/tools.md](agents-remember-md/runtime/system/defaults/examples/coordinator/tools.md) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-20T19:11+02:00: Documented provider command shapes for GrepAI and CodeGraphContext, including CGC process-env-only keys and containment checks.
- 2026-05-13T13:38: Created onboarding for the coordinator tools example.
