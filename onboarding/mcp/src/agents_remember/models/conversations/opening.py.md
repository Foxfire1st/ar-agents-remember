# mcp/src/agents_remember/models/conversations/opening.py

## Governing Overview

[models conversations overview](overview.md)

## Purpose

`models/conversations/opening.py` (260731-EFA-L9, moved from
`serving/conversation/_models_operations.py`) owns `OpenConversationOperation`, the
identity/catalog-proof open operation with phase-matching rollback.

## Code Commentary

### Logic

`OpenConversationOperation` (cit:(["class OpenConversationOperation"], mcp/src/agents_remember/models/conversations/opening.py:16-16)) validates the complete semantic
product: no-launch outcomes carry no spawned identity, and identity-bearing failures require
catalog proof plus the phase-matching rollback state.

### Invariants And Boundaries

- Open identity and catalog proof must agree exactly; do not weaken the bidirectional rollback
  product.

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
