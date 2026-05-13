# README.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `system/examples/README.md`                |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-13T13:38                           |
| lastVerifiedCommitHash | `6d413269e6f3b0317829def3b5c77b11631285ac` |
| lastVerifiedCommitDate | 2026-05-13T13:50:13+02:00                  |

## Purpose

`system/examples/README.md` explains why system examples are split into target-shaped folders instead of encoded through file names.

## Code Commentary

### Logic

The file defines two example targets: `examples/coordinator/` for workspace-wide coordinator files and `examples/memory-repo/` for repository-specific memory-layer files. It states that coordinator files can define global defaults but should not encode one-repository rules, while memory-layer rules win for their own repository.

### Conventions

Examples are arranged by destination folder shape so users can copy a whole directory and preserve normal target file names such as `AGENTS.md`, `settings.md`, and `tools.md`.

### Invariants And Boundaries

Coordinator guidance is global by default; memory-repo guidance is more specific and overrides it for the target code repository.

### Todos

None.

### Docs References

No external documentation is needed for this example index.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

The source file itself is the active example index.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The README states that examples are split by target folder rather than by inferred ownership from file names. | L1-L4 | [system/examples/README.md](agents-remember-md/system/examples/README.md) |
| The README defines coordinator examples as workspace-wide/global and memory-repo examples as repository-specific. | L8-L31 | [system/examples/README.md](agents-remember-md/system/examples/README.md) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-13T13:38: Created onboarding for the folder-shaped system examples index.
