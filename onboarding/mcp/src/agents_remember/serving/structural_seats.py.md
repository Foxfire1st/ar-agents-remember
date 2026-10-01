# mcp/src/agents_remember/serving/structural_seats.py

## Governing Overview

[Serving overview](overview.md)

## Purpose

Qualifies current structural seats from canonical task-document containment and role. It is the one
resolver used by structural operations and replacement-aware routing.

## Code Commentary

### Logic

`StructuralSeatResolver` reads task topology and catalog bindings, enforces the role's natural
altitude, derives authorized parents/children, and selects exactly one live occupant. Missing,
ambiguous, wrong-level, and out-of-scope cases become typed `StructuralSeatError`s.
`parent_address` and `child_address` derive and authorize the canonical document-and-role pair
without requiring a live occupant; `parent` and `child` layer current-generation resolution on top.
Current selection is delegated to `controlplane.seats.current_seat_occupant`.

`authorize_child` exposes the four reviewer contexts without creating four roles: managers own leaf
and master reviewers, the architect owns the sprint plan reviewer, and the orchestrator owns the
sprint super-exit reviewer. `_reviewer_parent_address` validates the parent stamp against the target
altitude before routing. Only a pre-polymorphic unstamped leaf reviewer retains its one
deterministic manager owner. Unstamped master and sprint reviewers fail closed rather than inventing
an owner for a review manifestation that did not exist in the legacy leaf-only model.
Manager child authorization distinguishes an invalid same-master role from a leaf owned by a
different master. The latter returns the specific outside-manager-scope refusal instead of being
collapsed into the generic child-vocabulary error.

### Conventions

The resolver uses structural task references for identity and runtime ids only as internal catalog
occupant/provenance evidence.

### Invariants And Boundaries

- Exactly one live occupant may satisfy a singular document+role seat.
- Parent and child lookup never escapes the containing sprint/master.
- Spawn ancestry is neither public identity nor a fallback resolver here; topology plus role
  establishes the authorized relation.
- No first-running-role or workspace-global fallback exists.
- An address remains valid while its seat is vacant; occupancy is required only for operations that
  act on a current generation.
- Reviewer is polymorphic by task altitude and generation-bound parent; sprint ownership is never
  guessed from the shared reviewer address.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.


### Repo-Internal References

- The resolver and error family centralize structural qualification. [1]
- Parent/child canonical addresses are derivable through vacancy. [2]
- Reviewer parent resolution validates the plane stamp and permits unstamped migration only for historical leaf rows. [3]
- Task containment resolves real sprint/master/leaf documents. [4]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
