# settings.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `system/examples/memory-repo/settings.md`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-13T13:38                           |
| lastVerifiedCommitHash | `f314b0d369e7f68125670caa99986cde1328e08a` |
| lastVerifiedCommitDate | 2026-05-14T20:13:45+02:00|

## Purpose

This file is the human-facing settings example for a repo-local or external memory layer.

## Code Commentary

### Logic

The example explains that memory-layer settings belong under either `<repo>/ar-memory/system/` or `ar-coordination/memory-repos/ar-<repo>/system/`. It assigns onboarding storage, path eligibility, cross-repo allowances, repo-specific sources/tools/coding guidance, and workflow notes to the memory layer.

### Conventions

Coordinator settings can define global instructions and locate memory repos, but they should not own rules valid only for this memory layer.

### Invariants And Boundaries

Memory-layer settings own repository-specific truth; coordinator settings may define global defaults.

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
| The memory settings example identifies internal and external memory-layer locations. | L1-L11 | [system/examples/memory-repo/settings.md](agents-remember-md/system/examples/memory-repo/settings.md) |
| The scope section lists memory-owned policy and distinguishes it from global coordinator settings. | L13-L25 | [system/examples/memory-repo/settings.md](agents-remember-md/system/examples/memory-repo/settings.md) |
| The storage, path eligibility, and cross-repo sections describe memory-layer ownership for settings JSON policy. | L27-L44 | [system/examples/memory-repo/settings.md](agents-remember-md/system/examples/memory-repo/settings.md) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-13T13:38: Created onboarding for the memory-repo settings Markdown example.
