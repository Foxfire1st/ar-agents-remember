# mcp/src/agents_remember/models/conversations/history.py

## Governing Overview

[models conversations overview](overview.md)

## Purpose

`models/conversations/history.py` (260731-EFA-L9, moved from
`serving/conversation/_models_status.py`) owns the dormant native library/page grammar:
page windows, library rows, sub-agent grouping, and the historical page.

## Code Commentary

### Logic

`ConversationPageWindow` (cit:(["class ConversationPageWindow"], mcp/src/agents_remember/models/conversations/history.py:27-27)) carries cursor continuity;
`ConversationLibraryAgentRow` (cit:(["class ConversationLibraryAgentRow"], mcp/src/agents_remember/models/conversations/history.py:48-48)) is one sub-agent conversation
grouped under its parent row; "class ConversationLibraryPage(WireModel):" (cit:(["class ConversationLibraryPage(WireModel):"], mcp/src/agents_remember/models/conversations/history.py:86-86)) carries
`agents_note` — the exact native reason sub-agent conversations are unavailable, never silently
absent; `HistoricalConversationPage` (cit:(["class HistoricalConversationPage"], mcp/src/agents_remember/models/conversations/history.py:95-95)) keeps the
library serializer's meaningful-null `older_cursor`.

### Invariants And Boundaries

- Sub-agent identity is never fabricated; when sub-agent conversations are unavailable,
  `agents_note` must carry the exact native reason.
- Nulls are meaningful on the library wire: fields reached only by the library serializer stay
  required-and-nullable by design.

### Todos

No known follow-up.

## Evidence

### Docs References

No external/domain documentation is configured.

No configured domain documentation was available.

### Repo-Internal References

- The library serializer deliberately keeps nulls on the wire. [1]

### Cross-Repo References

No cross-repository implementation participates.

No meaningful cross-repo references found.
