# route-local-overview-card-template.md

## Purpose

This template defines the overview card used as a scoped work order before a route-local overview worker writes durable memory.

## Code Commentary

### Logic

The overview card records route metadata, why the overview exists, governed paths, what the overview must explain, required inputs, backlinks, downlinks, and open questions.

### Conventions

Overview cards are generated before overview waves. They constrain workers so route-local overview creation does not become broad repo rediscovery.

### Invariants And Boundaries

An overview card is a promotion artifact, not durable source onboarding. The durable output is the route-local `overview.md` produced from it.

### Todos

Fill verification metadata after the source file is committed.

### Docs References

No external documentation is needed for this repository-local template.

No relevant external documentation found.

## Evidence

### Repo-Internal References

- The overview card template records route metadata, governed paths, required explanation topics, inputs, links, and open questions. [1]
- `c-03-repo-bootstrap` skill Phase 4C writes overview cards for each selected governing route before route-local overview waves. [2]

### Cross-Repo References

No sibling repository evidence is needed for this template.

No meaningful cross-repo references found.
