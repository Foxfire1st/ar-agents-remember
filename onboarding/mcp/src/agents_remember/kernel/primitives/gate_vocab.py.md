# mcp/src/agents_remember/kernel/primitives/gate_vocab.py

## Governing Overview

[kernel primitives overview](overview.md)

## Purpose

`kernel/primitives/gate_vocab.py` is the gate vocabulary for policy and records (kernel-owned,
260731-EFA-L9). Kernel is below models: the wire layer re-exports these names from here rather
than defining them, and the control-plane records import them through models.

## Code Commentary

### Logic

The module defines the `GateKind` literal vocabulary and `coerce_gate_kind`
(cit:([`coerce_gate_kind`], mcp/src/agents_remember/kernel/primitives/gate_vocab.py:45-45)), which validates raw gate-kind strings with a typed
error for unknown values.

### Invariants And Boundaries

- One declaration per gate-kind member: models re-export, records import through models, and
  nobody re-types the literal.

### Todos

No known follow-up.

## Evidence

### Docs References

No external/domain documentation is configured.

No configured domain documentation was available.

### Repo-Internal References

- Structural gate models import the producer-owned vocabulary from kernel. [1]
- Gate kind coercion is the production vocabulary boundary. [2]

### Cross-Repo References

No cross-repository implementation participates.

No meaningful cross-repo references found.
