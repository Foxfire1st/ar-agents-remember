# coding-guidelines.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/coding-guidelines.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d` |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|

## Purpose

This file is the coding-guidelines starter for a memory layer.

## Code Commentary

L23 adds clean-quality guidance for native POSIX subprocesses, enclosure-owned self-overwriting reports, configured pytest parallelism, and the single pinned Dagger Ubuntu graph with no local-container fallback.

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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The example says repository-specific coding guidance belongs in the target memory root. | `## Coding Style` | mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/coding-guidelines.md:1-37 |
| The example documents compatibility and cleanup rules for memory-layer coding guidance. | `## Coding Style` | mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/coding-guidelines.md:1-37 |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B24 curator: replaced the `n/a` rows with exact
  heading anchors; exact non-fixing check returns zero findings.

- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-13T13:38: Created onboarding for the memory-repo coding-guidelines example.
