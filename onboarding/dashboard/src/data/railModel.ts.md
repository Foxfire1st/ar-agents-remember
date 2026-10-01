# dashboard/src/data/railModel.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Builds the canonical Chats hierarchy from real sprint, master, and leaf task documents, then places
each live hosted occupant at its task-document-and-role seat. Runtime spawn ancestry is retained only
as a separate diagnostic tree.

## Code Commentary

### Logic

`buildRailModel` indexes task documents by canonical reference, derives sprint/master/leaf sections,
and joins catalog sessions through `session.taskDocumentRef`. Role-altitude rows remain stable across
occupant replacement. `buildSpawnTree` deliberately projects runtime provenance outside the default
Chats hierarchy. Row layout exposes a fixed segment contract so long labels are clipped in one line.

### Conventions

Task containment supplies hierarchy; role supplies seat altitude and ordering. Runtime ids identify
the focused occupant only.

### Invariants And Boundaries

- Default Chats nesting is task-document hierarchy, not spawn ancestry.
- A row's structural address survives replacement.
- Missing task bindings do not get guessed into a task branch.
- Row titles remain single-line; status is the only declared elidable segment.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Structural rail nodes carry canonical task-document references. [1]
- The default rail joins sessions to real task topology. [2]
- Runtime provenance is a separate diagnostic projection. [3]
- The row segment contract keeps status as the only elidable segment. [4]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
