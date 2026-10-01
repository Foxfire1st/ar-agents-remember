# mcp/src/agents_remember/worktrees/integration/master_review_gate.py

## Governing Overview

[Integration overview](overview.md)

## Purpose

Projects master route-review currentness into the integration refusal boundary. The gate is
deliberately absent from atomic child closeout and is required for the single master-to-parent
publication edge.

## Code Commentary

### Logic

`master_route_review_block` adapts the typed currentness refusal into the integration result shape;
`master_route_review_refusal` produces the stable refusal payload and next action. The helpers retain
the canonical candidate, master scope and review evidence in the returned diagnostic so callers can
repair the exact stale edge. They do not perform publication or create a second review authority.

### Conventions

Refusals are typed, deterministic and actionable. Atomic child and non-integration paths remain
deferred or not-applicable; only the master integration seam consumes this gate.

### Invariants And Boundaries

- The gate is evaluated at the master-to-parent integration boundary, including the lock-time
  publication recheck.
- A missing, stale, mismatched or status-only master review blocks publication.
- The module projects refusal state; scope resolution and Git mutation remain owned by their callers.

### Todos

None.

## Evidence

### Docs References

No relevant domain documentation was configured for this repository-internal integration gate.

No external documentation source was configured for this source-owned gate.

### Repo-Internal References

- Typed blocked-integration payload projection. The former `master_route_review_block` / `master_route_review_refusal` pair is gone from this module; the refusal projection now lives in `worktrees/route_review.py` as `route_review_refusal_projection` / `route_review_refusal_fields`. [1]
- Preflight and lock-time publication paths consume the gate. [2]

### Cross-Repo References

No meaningful cross-repo implementation reference is required for this gate card. The coordination
requirement is tracked in the task report and governs this preparation without serving as a source
citation here.

## Source File Binding

The active binding for this card is the exact current source-file bytes: SHA-256
`dd51ab6200088274352370fc8830b1d05df291feb43f5a46f19ccd3b163efff4` (`3248` bytes,
`102` lines). The immutable v3 manifest records the same path bytes. The source remains an
uncommitted preparation candidate, so verification metadata remains closeout-owned.

## Historical Candidate Binding

The predecessor v2 cumulative candidate tree was `96b94b2a1c8e57a7a37b19b08cda33db93fe81b6`,
with this file's SHA-256 recorded as
`dd51ab6200088274352370fc8830b1d05df291feb43f5a46f19ccd3b163efff4`. That whole-tree identity
is retained as historical composition evidence and is not the active identity for this card.
