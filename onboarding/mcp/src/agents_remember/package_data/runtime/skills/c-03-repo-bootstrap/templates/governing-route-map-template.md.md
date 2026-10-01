# governing-route-map-template.md

## Purpose

This template defines the governing route map that decides where durable route-local `overview.md` files should live, move, retire, or be removed.

## Code Commentary

### Logic

The route map records placement principles, proposed governing routes, deferred routes, moved or deleted routes, cross-cutting concept anchors, parent/child overview relationships, and developer questions.

### Conventions

The map chooses local anchors in the mirrored onboarding hierarchy, avoids creating an overview merely because a folder exists, and records stale route-memory decisions during existing-memory slice maintenance.

### Invariants And Boundaries

Route-local overviews are durable memory, but they must remain local to source traversal and must not replace file-level onboarding.

### Todos

Fill verification metadata after the source file is committed.

### Docs References

No external documentation is needed for this repository-local template.

No relevant external documentation found.

## Evidence

### Repo-Internal References

- The governing route map template defines placement principles for route-local overviews and keeps file-level onboarding separate. [1]
- The template records proposed routes, deferred routes, moved/deleted routes, cross-cutting concepts, parent/child overview relationships, and developer questions. [2]
- `c-03-repo-bootstrap` skill Phase 4B writes `bootstrap/governing-route-map.md` from this template before overview cards and waves, and records stale, moved, or deleted routes for existing-memory slice maintenance. [3]

### Cross-Repo References

No sibling repository evidence is needed for this template.

No meaningful cross-repo references found.
