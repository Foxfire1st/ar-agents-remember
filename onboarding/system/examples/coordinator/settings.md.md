# settings.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `system/examples/coordinator/settings.md`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-13T13:38                           |
| lastVerifiedCommitHash | `f314b0d369e7f68125670caa99986cde1328e08a` |
| lastVerifiedCommitDate | 2026-05-14T20:13:45+02:00|

## Purpose

This file is the human-facing coordinator settings example for `ar-coordination/system/settings.md`.

## Code Commentary

### Logic

The example describes the coordinator as workspace-wide routing and workflow state. It lists global instructions, shared tools, workspace source registries, task/worktree roots, notes, selected memory repos, and operator conventions as coordinator-owned surfaces.

### Conventions

Repo-specific rules belong in the selected memory layer rather than this coordinator settings file.

### Invariants And Boundaries

C-08 remains the route from coordinator context into the target repository's active memory settings, tools, sources, onboarding, and ledger paths.

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
| The example states that coordinator settings are workspace-wide and do not replace per-repository memory settings. | L1-L8 | [system/examples/coordinator/settings.md](agents-remember-md/system/examples/coordinator/settings.md) |
| The scope list names global instructions, shared commands, workspace sources, roots, notes, selected memory repos, and operator conventions as coordinator concerns. | L10-L25 | [system/examples/coordinator/settings.md](agents-remember-md/system/examples/coordinator/settings.md) |
| The routing section tells agents to invoke C-08 and treat repository-specific memory guidance as more specific. | L40-L48 | [system/examples/coordinator/settings.md](agents-remember-md/system/examples/coordinator/settings.md) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-13T13:38: Created onboarding for the coordinator settings Markdown example.
