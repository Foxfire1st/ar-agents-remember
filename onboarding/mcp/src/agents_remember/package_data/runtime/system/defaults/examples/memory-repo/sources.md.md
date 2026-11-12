# sources.md

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

No external documentation is needed for this package starter. The resolved `agents-remember` source registry has no configured `Domain Documentation` entries, so the relevant evidence for this example is repository source.

No relevant external documentation found after checking live sources.

## Evidence

### Repo-Internal References

- The memory-repo sources example tells users to install it into a memory layer and defines task, domain, tech-stack, and schema sections. [1]
- Domain documentation placeholders name the authoritative live source and retrieval tool/MCP, treat local mirrors as orientation caches, and require live retrieval before recording that no domain docs exist. [2]

### Cross-Repo References

No sibling repository evidence is needed.

No meaningful cross-repo references found.
