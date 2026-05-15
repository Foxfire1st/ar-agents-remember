# tools.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/system/defaults/examples/coordinator/tools.md`     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-13T13:38                           |
| lastVerifiedCommitHash | `398184b757e336211e335569284f2cde309cd964` |
| lastVerifiedCommitDate | 2026-05-15T04:04:02+02:00|

## Purpose

This example documents the coordinator-level tools surface.

## Code Commentary

### Logic

The file says coordinator tools are commands useful across many repositories. Repo-specific checks, branch workflow, and coding tools belong in memory-layer `system/tools.md`.

### Conventions

Global commands stay here; repository-specific command details stay in the selected memory layer.

### Invariants And Boundaries

Agents should resolve the target repository with C-08 before choosing task, worktree, memory, or validation paths.

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
| The coordinator tools example separates global commands from repository-specific checks and branch workflow. | L1-L17 | [runtime/system/defaults/examples/coordinator/tools.md](agents-remember-md/runtime/system/defaults/examples/coordinator/tools.md) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-13T13:38: Created onboarding for the coordinator tools example.
