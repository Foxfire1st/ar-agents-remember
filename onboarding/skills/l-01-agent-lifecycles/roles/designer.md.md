# skills/l-01-agent-lifecycles/roles/designer.md

## Governing Overview

[overview.md](overview.md)
## Purpose

The optional sprint-bound design seat and the drawing-board method an architect may collapse inline
when a separate design conversation would add no value.

## Code Commentary

### Logic

The designer binds to `(sprint document, designer)`, has no leaf worktree, and returns a master-scoped
task design plus its declared cross-master blind spot to the architect. It reframes intent, retrieves
evidence, measures the within-master blast radius, authors the requirement-derived task topology,
and never implements. A dispatched designer uses `message_parent`; an architect may perform the
same method inline without changing roles.

When separately hosted, designer is target-only. Its architect ordinarily creates or switches the
seat with one `dispatch_agent` call on the sprint document and is the plane-hosted caller. An
identity-free developer launcher may target the designer only for an explicit task-seat takeover;
the designer itself has no dispatch caller authority or ambient recovery route. Its role-table
dispatch/tools rows are structural documentation, not settings keys.

### Invariants And Boundaries

- The designer is a seat when dispatched, not an architect role mutation; inline use is explicit
  architect hat-collapse.
- It is sprint-bound, worktree-free, and master-scoped; portfolio collision review remains downstream.
- Canonical lifecycle doctrine owns this source; generated copies are synchronization outputs.

## Evidence

### Docs References

No relevant documentation was configured in the resolved source registry; task artifacts and the final candidate are the direct evidence.

### Repo-Internal References

`skills/l-01-agent-lifecycles/roles/designer.md` is the canonical role contract; the governing role
overview supplies the shared lifecycle frame.

### Cross-Repo References

No meaningful cross-repo references.
