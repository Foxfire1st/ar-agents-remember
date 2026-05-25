# sources.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/system/defaults/examples/coordinator/sources.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `a8ee8440dfa920d1153a4bb4bb43cc77534c3c90` |
| lastVerifiedCommitDate | 2026-05-25T15:22:52+02:00|

## Purpose

This example documents the coordinator-level source registry surface.

## Code Commentary

### Logic

The file says coordinator sources are for workspace-wide registries useful across many repositories, while domain docs and repo-specific sources usually belong in the selected memory layer.

### Conventions

Keep repository-specific domain documentation, task systems, tech-stack references, and schema notes in the memory layer unless they are genuinely global.

### Invariants And Boundaries

Coordinator sources should not hide or replace memory-layer sources for a target repository.

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
| The coordinator sources example distinguishes global source registries from repository-specific domain documentation. | L1-L12 | [mcp/src/agents_remember/package_data/runtime/system/defaults/examples/coordinator/sources.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/system/defaults/examples/coordinator/sources.md) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-13T13:38: Created onboarding for the coordinator sources example.
