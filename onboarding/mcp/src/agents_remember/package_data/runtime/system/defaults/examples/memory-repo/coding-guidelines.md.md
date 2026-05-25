# coding-guidelines.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/coding-guidelines.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `a8ee8440dfa920d1153a4bb4bb43cc77534c3c90` |
| lastVerifiedCommitDate | 2026-05-25T15:22:52+02:00|

## Purpose

This file is the coding-guidelines starter for a memory layer.

## Code Commentary

### Logic

The example tells users to keep concrete project preferences in the target repository's memory layer. It provides starter guidance for compatibility, legacy code, deletion, cleanup, and protected artifacts.

### Conventions

The generic example lives under the memory-repo example folder because coding rules are normally repository-specific.

### Invariants And Boundaries

Compatibility layers are discouraged unless required by public contracts, persisted data, staged rollout, or explicit user request.

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
| The example says repository-specific coding guidance belongs in the target memory root. | L1-L10 | [mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/coding-guidelines.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/coding-guidelines.md) |
| The example documents compatibility and cleanup rules for memory-layer coding guidance. | L12-L37 | [mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/coding-guidelines.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/coding-guidelines.md) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-13T13:38: Created onboarding for the memory-repo coding-guidelines example.
