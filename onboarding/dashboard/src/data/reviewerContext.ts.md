# dashboard/src/data/reviewerContext.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Defines the dashboard's shared reviewer-parent validator and the altitude-aware labels rendered for
live reviewer seats.

## Code Commentary

### Logic

`reviewerParentMatches` accepts a reviewer only when its generation-bound structural parent matches
the selected leaf, master, or sprint ownership plane. `reviewerContextLabel` projects the same parent
identity as leaf, master, plan, or super reviewer copy.

### Conventions

Reviewer role alone is insufficient identity; task-document parent plus parent role selects the
review plane.

### Invariants And Boundaries

- Leaf reviewers belong to the owning master manager.
- Master reviewers belong to that master's manager.
- Sprint reviewers retain either architect or orchestrator ownership without collapsing the two.
- Missing or mismatched parent stamps are invalid rather than guessed.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Reviewer ownership is checked at all three topology altitudes. [1]
- UI labels retain the sprint ownership plane. [2]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
