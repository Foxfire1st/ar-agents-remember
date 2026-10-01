# mcp/src/agents_remember/models/conversations/interrupts.py

## Governing Overview

[models conversations overview](overview.md)

## Purpose

`models/conversations/interrupts.py` (260731-EFA-L9, moved from
`serving/conversation/_models_operations.py`) owns `InterruptOperation`, the exact-turn interrupt
request DTO.

## Code Commentary

### Logic

`InterruptOperation` (cit:(["class InterruptOperation"], mcp/src/agents_remember/models/conversations/interrupts.py:12-12)) validates the interrupt semantic product
used by the control child's exact-turn interrupt routes.

### Invariants And Boundaries

- Acknowledgement never equals settlement; the operation carries the exact target identity.

### Todos

No known follow-up.

## Evidence

### Docs References

No external/domain documentation is configured.

No configured domain documentation was available.

### Repo-Internal References

### Cross-Repo References

No cross-repository implementation participates.

No meaningful cross-repo references found.
