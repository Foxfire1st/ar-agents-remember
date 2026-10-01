# mcp/src/agents_remember/worktrees/queue/closeout_queue.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Owns the sprint-scoped status/rebuild facade and the exact first-ready waiting-generation admission
check for the disposable closeout projection.

## Code Commentary

### Logic

`closeout_queue_tool` structurally authorizes the sprint caller and serves effective status or an
idempotent rebuild. `require_first_ready_generation` is called only while its caller holds the
short task/door publication mutex; it rechecks the exact current projection and admits only the
named first-ready waiting generation. All candidate construction, source census, member readiness,
and publication effects delegate to the projection modules.

### Conventions

Judgment and priority are read from canonical sources during projection construction. Equal
effective priority uses graph declaration order and then leaf identity. A graph-less
atomic-sequential sprint remains valid; its waiting reasons observe this contract's own strict
activation snapshot rather than electing a series from contract presence, and a sibling master's
selection is never one of them.

### Invariants And Boundaries

- Only status and rebuild are public queue actions.
- Only the deterministic first-ready waiting generation passes the claim-admission fence.
- Task edits and door controls remain canonical even when rebuild fails.
- In-flight records, commits, certification, integration, and lifecycle controls are journal-owned.
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
- Claim admission requires the exact first-ready waiting generation. [2]

### Cross-Repo References

No external repository owns this queue.

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## 260821-CLIVE Status/Rebuild Facade

The command processor is reduced to sprint-scoped `status` and idempotent `rebuild`, plus
`require_first_ready_generation` for the short claim admission fence. That fence runs while the
caller holds the task/door CAS and requires the exact first ready waiting generation. Declare,
grade, claim, certify, block, release, abort, and integration-completion mutations are removed. Task
authoring is never gated by this facade.

## IAS Activation Projection Boundary

The facade remains status/rebuild plus first-ready admission. For graph-less atomic work,
projection helpers derive active/reconciling/paused/vacant waiting reasons from the exact selector
snapshot. Contract presence is not a lane owner, selector corruption makes only the affected
projection invalid-empty, and no queue action mutates activation or operation lifecycle.


## PDLS Reconciliation

Projection access now recognizes the exact sprint planning actor and commanded manager set; queue authorization no longer subordinates task authoring or infers managers from unrelated topology.

This change preserves the file's existing authority boundary. No threshold exception, silent
fallback, or compatibility reader was added.
