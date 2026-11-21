# mcp/src/agents_remember/worktrees/queue/closeout_queue.py

## Governing Overview

[overview](overview.md)

## Purpose

Owns sprint-scoped status and rebuild for the disposable closeout projection. A retained helper
checks the exact first-ready waiting generation when explicitly invoked.

## Code Commentary

### Logic

`closeout_queue_tool` structurally authorizes the sprint caller and serves effective status or an
idempotent rebuild. The retained `require_first_ready_generation` compares the named waiting
generation with the first ready member of the exact current projection. Ordinary synchronous
closeout calls its transaction owner directly. Candidate construction, source census, member
readiness and publication effects delegate to the projection modules.

### Conventions

Judgment and priority are read from canonical sources during projection construction. Equal
effective priority uses graph declaration order and then leaf identity. A graph-less
atomic-sequential sprint remains valid; its waiting reasons observe this contract's own strict
activation snapshot rather than electing a series from contract presence, and a sibling master's
selection is never one of them.

### Invariants And Boundaries

- Only status and rebuild are public queue actions.
- The retained first-ready helper succeeds only for the deterministic first-ready waiting generation.
- Task edits and door controls remain canonical even when rebuild fails.
- Closeout and integration output belongs to their synchronous transaction owners. Direct-landing controls belong to its generation.
- There is no persistent blocker, release, abort, declared-candidate, or queue-owned grade action.
- Activation is read-only input to projection; this facade cannot select, pause, activate, or vacate
  a master.

### Todos

Activation-related claims are reconciled to the frozen projection behavior. Verification metadata
remains closeout-owned.

## Evidence

### Docs References

No configured Domain Documentation source applies; queue doctrine is repository-internal.

### Repo-Internal References

- The facade serves status and idempotent rebuild. [1]

- The retained helper checks the exact first-ready waiting generation of a current projection. [2]


### Cross-Repo References

No external repository owns this queue.

## Integration-Authority Boundary

Task-derived integration refs are mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## Status/Rebuild Facade

The command processor offers sprint-scoped `status` and idempotent `rebuild`. The retained internal
first-ready comparison reads the projection. It offers neither scheduling mutation nor transaction
approval. Task authoring remains with its canonical owner.

## Activation Projection Boundary

The facade serves status and rebuild. For graph-less atomic work,
projection helpers derive active/reconciling/paused/vacant waiting reasons from the exact selector
snapshot. Contract presence is not a lane owner, selector corruption makes only the affected
projection invalid-empty, and no queue action mutates activation or operation lifecycle.


## Projection Access

Projection access recognizes the exact sprint planning actors — the sprint document's `architect` or `orchestrator` — and the commanded manager set; any other caller is refused with `closeout-projection-caller-refused`. Queue authorization does not subordinate task authoring or infer managers from unrelated topology.

- The sprint planning actors are the sprint document's architect and orchestrator. [3]
