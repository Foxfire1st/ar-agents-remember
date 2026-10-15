# skills/c-03-repo-bootstrap/templates/governing-route-map-template.md

## Governing Overview

[Repository onboarding overview](../../../overview.md)

## Purpose

This template defines the governing route map that decides where durable route-local `overview.md` files should live, move, retire, or be removed within the mirrored onboarding hierarchy.

## Code Commentary

### Logic

The route map records placement principles, proposed governing routes, routes considered but deferred and their revisit triggers, moved or deleted routes, cross-cutting concepts and their primary local anchors, parent/child overview relationships, and developer questions. Its moved/deleted-route table records previous and current source routes, affected onboarding artifacts, a removal/move/retirement/preservation decision, and confidence.

The bootstrap skill's Phase 4B writes `bootstrap/governing-route-map.md` from this template before Phase 4C overview cards and Phase 4D overview waves. Existing-memory slice maintenance includes stale, moved, or deleted route decisions rather than treating the repository as blank.

### Conventions

Choose the local source route where an area begins rather than a detached architecture folder. A folder's existence alone is not a reason to create an overview: shared models, workflows, invariants, routing burden, documentation dependencies, cross-repo boundaries, or multiple hotspots justify a governing route. Record deferred routes and revisit triggers, and use the developer questions to check ownership and placement.

The helpdesk, DTO, old/new-module and command-lifecycle rows illustrate the table format. Their paths, decisions and confidence values are examples, not claims about a repository's actual routes, completed maintenance, or permission to remove memory.

### Invariants And Boundaries

Route-local overviews are durable memory that remains discoverable through local source traversal. They do not replace file-level onboarding, which stays separate and links back to the nearest governing overview. Cross-cutting workflows have a primary local anchor and secondary local mentions; the map also records parent/child overview relationships.

### Todos

The earlier card's instruction to fill verification metadata after a source commit is historical, not a current instruction to add commit stamps. This template contains no verification-metadata fields; the source references below describe its current format.

### Docs References

The checked template and relevant repository-local bootstrap-skill sections define this format without requiring external documentation. No relevant external documentation was found in those inputs.

## Evidence

### Repo-Internal References

- The route map places local overviews without replacing file-level onboarding. [1]
- The map records proposed and deferred routes, moved/deleted-route decisions, cross-cutting anchors, parent/child relationships and developer questions. [2]
- Phase 4B writes the governing route map and records stale, moved or deleted routes in slice maintenance. [3]
- Overview cards and overview waves follow the route-map phase. [4]
- Existing-memory slice maintenance starts from existing memory and considers preservation before removal of moved or deleted route knowledge. [5]

### Cross-Repo References

No sibling repository was consulted for this template. No meaningful cross-repo reference was found in the checked template or relevant bootstrap-skill sections; a work order's boundary-pack field is not itself evidence of a live external boundary.
