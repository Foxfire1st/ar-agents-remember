# mcp/src/agents_remember/models/conversations/status.py

## Governing Overview

[models conversations overview](overview.md)

## Purpose

`models/conversations/status.py` (260731-EFA-L9, moved from
`serving/conversation/_models_status.py`) owns the canonical evidence-to-turn-state vocabulary:
waiting and terminal cross-products validate against exact evidence.

## Code Commentary

### Logic

`StatusFreshness` (cit:(["class StatusFreshness"], mcp/src/agents_remember/models/conversations/status.py:55-55)) carries evidence freshness with the L4
defaulted-nullable fields; `ConversationTurnStatus` (cit:(["class ConversationTurnStatus"], mcp/src/agents_remember/models/conversations/status.py:87-87)) validates waiting/terminal
cross-products; `ConversationStatusEvidence` (cit:(["class ConversationStatusEvidence"], mcp/src/agents_remember/models/conversations/status.py:132-132)) and
"class ConversationStatus(WireModel):" (cit:(["class ConversationStatus(WireModel):"], mcp/src/agents_remember/models/conversations/status.py:137-137)) fix the evidence classification —
unknown evidence cannot establish `ready`.

### Invariants And Boundaries

- `ready` cannot be derived from unknown evidence; waiting and terminal states retain matching
  evidence products.
- A model must validate its own emitted body: fields reached by `exclude_none=True` serializers
  must be nullable AND defaulted.

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
