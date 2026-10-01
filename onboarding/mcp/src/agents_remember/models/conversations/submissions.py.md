# mcp/src/agents_remember/models/conversations/submissions.py

## Governing Overview

[models conversations overview](overview.md)

## Purpose

`models/conversations/submissions.py` (260731-EFA-L9, moved from
`serving/conversation/_models_operations.py`) owns the cockpit queue and submit DTOs:
queue identity, operation queue items/projections, typed submit blocks, and the conversation
submit request.

## Code Commentary

### Logic

`CockpitQueueIdentity` (cit:(["class CockpitQueueIdentity"], mcp/src/agents_remember/models/conversations/submissions.py:16-16)) brands the queue;
`OperationQueueItem` (cit:(["class OperationQueueItem"], mcp/src/agents_remember/models/conversations/submissions.py:23-23)) and `OperationQueueProjection`
(cit:(["class OperationQueueProjection"], mcp/src/agents_remember/models/conversations/submissions.py:44-44)) model the source-aware queue;
`ConversationSubmitRequest` (cit:(["class ConversationSubmitRequest"], mcp/src/agents_remember/models/conversations/submissions.py:71-71)) validates the full
submit semantic product with text/asset composer blocks.

### Invariants And Boundaries

- Only queued cockpit work exposes withdrawal identity; raw drafts exist only in authoritative
  successful withdrawal responses.

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
