# AGENTS.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `system/examples/coordinator/AGENTS.md`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-13T13:38                           |
| lastVerifiedCommitHash | `6d413269e6f3b0317829def3b5c77b11631285ac` |
| lastVerifiedCommitDate | 2026-05-13T13:50:13+02:00                  |

## Purpose

This example shows the `AGENTS.md` entrypoint for a coordinator root.

## Code Commentary

### Logic

The example tells agents that coordinator instructions apply across code repositories and must route through C-08 before using repository-specific tasks, worktrees, docs, or memory. It also tells agents to read the resolved memory layer after C-08 and prefer memory-layer guidance when rules conflict.

### Conventions

Coordinator `AGENTS.md` should contain global routing and approval expectations, not rules that apply to only one repository.

### Invariants And Boundaries

The coordinator entrypoint may set global defaults, but repository-specific memory-layer files remain the more specific authority.

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
| The example routes agents through C-08 before using coordinator-managed state. | L7-L9 | [system/examples/coordinator/AGENTS.md](agents-remember-md/system/examples/coordinator/AGENTS.md) |
| The routing section separates global coordinator settings/tools/sources from one-repository rules and points agents at the resolved memory layer. | L11-L22 | [system/examples/coordinator/AGENTS.md](agents-remember-md/system/examples/coordinator/AGENTS.md) |
| The boundaries section preserves approval gates and says memory-layer guidance wins on repository-specific conflicts. | L24-L30 | [system/examples/coordinator/AGENTS.md](agents-remember-md/system/examples/coordinator/AGENTS.md) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-13T13:38: Created onboarding for the coordinator `AGENTS.md` example.
