# settings.json

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `system/examples/coordinator/settings.json` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-13T13:38                           |
| lastVerifiedCommitHash | `f314b0d369e7f68125670caa99986cde1328e08a` |
| lastVerifiedCommitDate | 2026-05-14T20:13:45+02:00|

## Purpose

This JSON example models machine-readable coordinator layout hints.

## Code Commentary

### Logic

The example has a `coordination` block for task, worktree, notes, and memory-repo folder names, plus a `memoryRepos` block for external-topology defaults and selected repository entries.

### Conventions

The file intentionally describes coordinator routing rather than onboarding storage or repository-specific path rules.

### Invariants And Boundaries

Durable repo policy should remain in the selected memory repo's `settings.json`; this coordinator JSON is for workspace-level routing and defaults.

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
| The JSON example declares coordinator folder names under `coordination`. | L1-L8 | [system/examples/coordinator/settings.json](agents-remember-md/system/examples/coordinator/settings.json) |
| The JSON example keeps memory-repo routing separate from repo-specific memory settings. | L9-L12 | [system/examples/coordinator/settings.json](agents-remember-md/system/examples/coordinator/settings.json) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-13T13:38: Created onboarding for the coordinator settings JSON example.
