# mcp/src/agents_remember/models/lifecycles/preparation_state.py

## Governing Overview

[Owning overview](overview.md)

## Purpose

Typed selected private preparation intents and outputs.

## Code Commentary

### Logic

Selected preparations form an ordered prefix of at most two legs, code followed by memory content. Every leg retains its exact accepted intent. The last selected leg can have no prepared output. A later leg requires the preceding selected output.

The preparation binds the leg order, operation owner and certification. The journal reader accepts old command-bearing records and removes their commands during validation.

### Conventions

Use the named source owners directly. The source is present in the landed IAS baseline. This preparation pass updates its description; review of an uncommitted candidate does not establish final publication proof.

### Invariants And Boundaries

The documented types and paths do not themselves establish execution, certification, delivery or acceptance. Those claims require the corresponding owning runtime evidence.

### Todos

No source-local TODO is asserted here.

## Evidence

### Docs References

No configured domain documentation applies.

### Repo-Internal References

- Selection is an ordered prefix of code and memory content. Each prior leg requires an output and the last selected leg may omit one. [1]


- `OperationPreparationState` owns the corresponding behavior described above. [4]
- `validate_preparation_owner` owns the corresponding behavior described above. [5]



### Cross-Repo References

No cross-repository source is needed for this card.
