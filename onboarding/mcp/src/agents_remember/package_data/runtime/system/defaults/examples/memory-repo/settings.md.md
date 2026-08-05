# settings.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/settings.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `a8ee8440dfa920d1153a4bb4bb43cc77534c3c90` |
| lastVerifiedCommitDate | 2026-05-25T15:22:52+02:00|

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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The memory settings example identifies internal and external memory-layer locations. | "ar-coordination/memory-repos/ar-<repo>" | mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/settings.md:3-11 |
| The scope section lists memory-owned policy and distinguishes it from global coordinator settings. | "onboarding storage policy" | mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/settings.md:13-25 |
| The storage, path eligibility, and cross-repo sections describe memory-layer ownership for settings JSON policy. | "crossRepo.allow" | mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/settings.md:27-42 |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-04T18:40+02:00 — 260731-EFA-L6 S18-B18 curator: normalized the 3 citation rows to plain
  sources with literal anchors (settings.md 3-11, 13-25, 27-42). Zero findings remain.

- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-13T13:38: Created onboarding for the memory-repo settings Markdown example.
