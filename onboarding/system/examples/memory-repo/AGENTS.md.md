# AGENTS.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `system/examples/memory-repo/AGENTS.md`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-13T13:38                           |
| lastVerifiedCommitHash | `6d413269e6f3b0317829def3b5c77b11631285ac` |
| lastVerifiedCommitDate | 2026-05-13T13:50:13+02:00                  |

## Purpose

This example shows the `AGENTS.md` entrypoint for an individual memory layer.

## Code Commentary

### Logic

The example scopes memory-layer instructions to one code repository, requires C-08 and C-02 before relying on memory, and lists the system files agents should read first.

### Conventions

Repo-specific branch and workflow notes belong in `system/tools.md`; `AGENTS.md` routes agents to those files and states precedence.

### Invariants And Boundaries

Coordinator-wide guidance may apply as a default, but this memory layer is the more specific authority for its code repository.

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
| The memory-repo `AGENTS.md` example scopes instructions to one repository and requires C-08 plus C-02 before relying on memory. | L1-L9 | [system/examples/memory-repo/AGENTS.md](agents-remember-md/system/examples/memory-repo/AGENTS.md) |
| The example tells agents to read settings, path policy, tools, sources, and coding guidelines in the memory layer. | L11-L18 | [system/examples/memory-repo/AGENTS.md](agents-remember-md/system/examples/memory-repo/AGENTS.md) |
| The example places branch strategies in `system/tools.md` and gives memory-layer guidance precedence for the repository. | L20-L28 | [system/examples/memory-repo/AGENTS.md](agents-remember-md/system/examples/memory-repo/AGENTS.md) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-13T13:38: Created onboarding for the memory-repo `AGENTS.md` example.
