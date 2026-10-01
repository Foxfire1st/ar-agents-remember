# mcp/src/agents_remember/application/structural/outcomes.py

## Governing Overview

[Structural application services](overview.md)

## Purpose

Defines the stable caller-facing structural outcome and its runtime-id-free payload projection.

## Code Commentary

### Logic

`StructuralOutcome` carries operation status, canonical task document, role, optional detail, and
delivery state. `structural_payload` serializes only populated public fields and deliberately has
no occupant/session coordinate.

### Conventions

Structural application modules construct this typed value instead of independently rebuilding
response dictionaries.

### Invariants And Boundaries

- Public work identity is task document plus role.
- Runtime session, lifecycle, inbox-owner, and lock identities have no field in this type.
- Optional fields are omitted rather than emitted as invented evidence.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

- The outcome vocabulary contains no runtime occupant identifier. [1]

### Repo-Internal References

- The single structural payload projector emits stable work identity and delivery state. [2]

### Cross-Repo References

No cross-repository dependency governs this unit.
