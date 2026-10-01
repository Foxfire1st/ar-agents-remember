# dashboard/src/panels/session-cockpit/SessionRail.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Renders the canonical Chats seat rail from the structural rail model, including stable sprint,
master, leaf, and role rows whose live occupant may be replaced.

## Code Commentary

### Logic

`SessionRail` consumes the task-projected model, maintains local tree expansion, focus, attention,
and bulk controls, and delegates the row layout to `sessionRailParts.tsx`. Focus remains a runtime
session choice; hierarchy and row identity come from the structural model.

### Conventions

The rail is a view over the model, not an alternate hierarchy builder. Runtime ancestry is available
only through the separate diagnostic projection.

### Invariants And Boundaries

- Replacement preserves the structural row and changes only its current occupant.
- Tree nesting follows sprint/master/leaf containment.
- Long live labels must remain on one line.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- The component renders the structural rail model and focus behavior. [1]
- Row and tree composition is delegated to the shared rail body. [2]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
