# mcp/src/agents_remember/controlplane/signal_routing.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Routes owner signals through canonical task-document containment and role, resolving only the current
catalog occupant after the structural owner is known.

## Code Commentary

### Logic

`derive_signal_owner` walks exactly one role-appropriate parent edge; decision items route to the
sprint architect. `_current_occupant` delegates current document/staged-replacement precedence to
the shared `current_seat_occupant` selector and translates typed occupancy ambiguity into a routing
error. Progress checks follow the task chain rather than spawn ancestry.
`StructuralRoutingError` belongs to the shared `AgentsRememberError` family; this adapter uses it
only to translate the selector's occupancy ambiguity into the routing boundary's own typed meaning.

Reviewers use the same role at three task altitudes and four review contexts. Their catalog
generation therefore carries a structural-parent document+role stamp. Routing validates that stamp
and targets the exact manager, architect, or orchestrator owner. Only historical unstamped leaf
reviewers retain their deterministic manager owner. Unstamped master and sprint reviewers refuse:
those higher review manifestations require a generation-bound plane stamp and are never inferred.

### Conventions

The returned `RoutedOwner` carries stable role/document identity with optional current
agent/lifecycle correlations.

### Invariants And Boundaries

- Task containment, never spawn ancestry, defines parent routing.
- Missing or ambiguous occupants are not replaced by a global same-role guess.
- Runtime correlations are delivery evidence, not the route key.
- Signal routing does not carry a second implementation of incumbent/heir precedence.
- A polymorphic reviewer routes by its validated generation-bound parent stamp; the shared reviewer
  address never authorizes a first-role or guessed sprint owner.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Current occupant selection is document-and-role scoped and ambiguity-strict. [1]
- Owner routing follows structural role and task containment. [2]
- Reviewer routing validates the altitude-specific parent and limits unstamped migration to historical leaf rows. [3]
- Progress evaluation follows the same task chain. [4]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
