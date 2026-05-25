# sources.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/sources.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `a8ee8440dfa920d1153a4bb4bb43cc77534c3c90` |
| lastVerifiedCommitDate | 2026-05-25T15:22:52+02:00|

## Purpose

This example is the source-registry starter for a memory layer. It documents how a memory repo names authoritative live domain documentation and optional local mirrors without hard-coding a particular documentation provider.

## Code Commentary

### Logic

The file defines sections for task sources, domain documentation, tech-stack documentation, and database schema. In `Domain Documentation`, it asks memory repos to name the authoritative online or intranet source plus the retrieval tool or MCP agents should use for live searches, and it explicitly frames local mirrors under the resolved memory layer's `docs/` folder as incomplete orientation caches.

### Conventions

Memory-layer sources describe the target code repository's real domain and technical references. Provider names belong in concrete memory repos; the package example uses placeholders so each repo can declare its own ticket system, live domain docs, local mirrors, tech-stack docs, and schema sources.

### Invariants And Boundaries

Coordinator-wide sources should not replace repo-specific memory-layer source registries when a repository has its own documentation. A local documentation mirror should not be treated as authoritative when the registry names a live source; if the mirror is empty, stale, or inconclusive, agents must use the named live retrieval path before recording no domain docs.

### Todos

After this working-tree update lands, refresh verification metadata to the committed sources example revision.

### Docs References

No external documentation is needed for this package starter. The resolved `agents-remember-md` source registry has no configured `Domain Documentation` entries, so the relevant evidence for this example is repository source.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The memory-repo sources example tells users to install it into a memory layer and defines task, domain, tech-stack, and schema sections. | L1-L22 | [mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/sources.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/sources.md) |
| Domain documentation placeholders name the authoritative live source and retrieval tool/MCP, treat local mirrors as orientation caches, and require live retrieval before recording that no domain docs exist. | L11-L14 | [mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/sources.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/sources.md) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-22T13:32+02:00: Updated after the starter source registry made live domain documentation authoritative and local mirrors orientation-only in provider-neutral terms. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-13T13:38: Created onboarding for the memory-repo sources example.
