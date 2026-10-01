# mcp/src/agents_remember/models/conversations/stream_events.py

## Governing Overview

[models conversations overview](overview.md)

## Purpose

`models/conversations/stream_events.py` (260731-EFA-L9, moved from
`serving/conversation/_models_status.py`) owns the SSE mutation grammar: append, delta, upsert,
replace-page, status, and explicit gap mutations inside `ConversationEventEnvelope`.

## Code Commentary

### Logic

`AppendItemMutation` (cit:(["class AppendItemMutation"], mcp/src/agents_remember/models/conversations/stream_events.py:19-19)) opens the mutation family;
`GapMutation` (cit:(["class GapMutation"], mcp/src/agents_remember/models/conversations/stream_events.py:67-67)) is the explicit established-stream failure
marker; `ConversationEventEnvelope` (cit:(["class ConversationEventEnvelope"], mcp/src/agents_remember/models/conversations/stream_events.py:88-88)) carries the envelope
with the L4 defaulted `previous_cursor`.

### Invariants And Boundaries

- On an established-stream gap, emit the explicit gap mutation, require repage, and close rather
  than silently resetting.

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
