# settings.md

## Purpose

This file is the human-facing settings example for a repo-local or external memory layer.

## Code Commentary

### Logic

The example explains that memory-layer settings belong under `ar-coordination/memory-repos/ar-<repo>/system/`; repo-local internal memory under `<repo>/ar-memory/` was **removed from the product**, so it is no longer a location for anything. It assigns onboarding storage, path eligibility, cross-repo allowances, repo-specific sources/tools/coding guidance, and workflow notes to the memory layer.

### Conventions

Coordinator settings can define global instructions and locate memory repos, but they should not own rules valid only for this memory layer.

### Invariants And Boundaries

Memory-layer settings own repository-specific truth; coordinator settings may define global defaults.

### Todos

None.

### Docs References

No external documentation is needed.

No relevant external documentation found.

## Evidence

### Repo-Internal References

- The memory settings example identifies internal and external memory-layer locations. [1]
- The scope section lists memory-owned policy and distinguishes it from global coordinator settings. [2]
- The storage, path eligibility, and cross-repo sections describe memory-layer ownership for settings JSON policy. [3]

### Cross-Repo References

No sibling repository evidence is needed.

No meaningful cross-repo references found.
