# sources.md

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

No relevant external documentation found.

## Evidence

### Repo-Internal References

- The coordinator sources example distinguishes global source registries from repository-specific domain documentation. [1]

### Cross-Repo References

No sibling repository evidence is needed.

No meaningful cross-repo references found.
