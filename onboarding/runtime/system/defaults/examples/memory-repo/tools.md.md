# tools.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/system/defaults/examples/memory-repo/tools.md`     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-13T13:38                           |
| lastVerifiedCommitHash | `398184b757e336211e335569284f2cde309cd964` |
| lastVerifiedCommitDate | 2026-05-15T04:04:02+02:00|

## Purpose

This example is the tools starter for a memory layer.

## Code Commentary

### Logic

The file tells users to copy the example to memory-layer `system/tools.md` and use it for CLI commands, MCPs, branch workflow notes, and checks that agents should reference for the target code repository.

### Conventions

Repo-specific validation and branch workflow guidance belongs here, not in coordinator tools.

### Invariants And Boundaries

Coordinator tools may set global defaults, but memory-layer tools are the authority for repository-specific commands.

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
| The memory-repo tools example says it belongs in memory-layer `system/tools.md` and can carry branch workflow notes plus checks. | L1-L12 | [runtime/system/defaults/examples/memory-repo/tools.md](agents-remember-md/runtime/system/defaults/examples/memory-repo/tools.md) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-13T13:38: Created onboarding for the memory-repo tools example.
