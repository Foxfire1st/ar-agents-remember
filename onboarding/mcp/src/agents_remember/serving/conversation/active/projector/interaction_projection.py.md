# mcp/src/agents_remember/serving/conversation/active/projector/interaction_projection.py

## Governing Overview

[Active projector package overview](overview.md)

## Purpose

Projects parent and multiplexed child pending interactions from current adapter snapshot
authority.

## Code Commentary

### Logic

`InteractionProjection.apply` keeps the singular parent interaction slot and separately projects
every multiplexed pending interaction that carries a thread id. Child requests receive an agent
ref plus adapter-provided label. Slot rotation resolves the evicted interaction; disappearance
resolves each multiplexed id. Resolution keeps the item but marks its phase unknown with an honest
reason because the projector did not observe the answer outcome.

### Conventions

Snapshot authority determines which interactions are pending; the component never invents an
answer.

### Invariants And Boundaries

- The singular parent slot is never double-projected from the multiplexed tuple.
- Concurrent parent requests beyond the oldest remain visible.
- Child labels enrich identity but never replace the thread id.
- Cleared interactions resolve individually.

### Todos

None known.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Snapshot pending-interaction model. [1]


### Cross-Repo References

No meaningful cross-repository references found.
