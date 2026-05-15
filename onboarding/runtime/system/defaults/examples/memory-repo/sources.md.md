# sources.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/system/defaults/examples/memory-repo/sources.md`   |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-13T13:38                           |
| lastVerifiedCommitHash | `398184b757e336211e335569284f2cde309cd964` |
| lastVerifiedCommitDate | 2026-05-15T04:04:02+02:00|

## Purpose

This example is the source-registry starter for a memory layer.

## Code Commentary

### Logic

The file defines sections for task sources, domain documentation, tech-stack documentation, and database schema. It also points local mirrors to the resolved memory layer's `docs/` folder.

### Conventions

Memory-layer sources describe the target code repository's real domain and technical references.

### Invariants And Boundaries

Coordinator-wide sources should not replace repo-specific memory-layer source registries when a repository has its own documentation.

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
| The memory-repo sources example tells users to install it into a memory layer and defines task, domain, tech-stack, and schema sections. | L1-L22 | [runtime/system/defaults/examples/memory-repo/sources.md](agents-remember-md/runtime/system/defaults/examples/memory-repo/sources.md) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-13T13:38: Created onboarding for the memory-repo sources example.
