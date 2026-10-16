# dashboard/src/panels/detail-panel/state.ts

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

DetailPanel selection state over the tasks map, with scoped local jump state, canonical viewed reference and optional role-chat leaf context.

## Code Commentary

Only taskdoc-prefixed opaque entry keys resolve tasks; raw lifecycle, series, slug and projected-path fallbacks are absent. The body hook receives the selected entry; parent/worktrees come from its served fields.

### Logic

The hook follows served parent/worktrees, reports the actual reference/leaf through onViewTask and scopes local jumps to incoming selectedId. The existing callback name remains navigation, not runtime identity.

### Conventions

State derivation is pure and unit-testable.

### Invariants And Boundaries

The hook never mutates server data; it only projects the current selection.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The state hook and its pure resolvers. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
