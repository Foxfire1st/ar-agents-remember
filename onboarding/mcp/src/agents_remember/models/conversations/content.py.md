# mcp/src/agents_remember/models/conversations/content.py

## Governing Overview

[models conversations overview](overview.md)

## Purpose

`models/conversations/content.py` (moved by 260731-EFA-L9 from
`serving/conversation/_models_blocks.py`) owns the typed content blocks, choices, correlation,
sub-agent reference, and conversation-item grammar of the wire contract.

## Code Commentary

### Logic

The typed block family starts at `MarkdownBlock` (cit:(["class MarkdownBlock"], mcp/src/agents_remember/models/conversations/content.py:25-25)) and includes text,
thinking, code, tool-input/output, diff, image-reference, file-reference, and vendor blocks;
`ConversationCorrelation` (cit:(["class ConversationCorrelation"], mcp/src/agents_remember/models/conversations/content.py:127-127)) carries the correlation product;
`ConversationAgentRef` (cit:(["class ConversationAgentRef"], mcp/src/agents_remember/models/conversations/content.py:139-139)) is the evidence-bound sub-agent
reference; `ConversationItem` (cit:(["class ConversationItem"], mcp/src/agents_remember/models/conversations/content.py:160-160)) is the item root with stable ids,
monotonic revisions/ordinals, typed blocks, provenance, and the additive per-item `agent`.

### Invariants And Boundaries

- Sub-agent identity is never fabricated: unresolved identity renders as `agent <short-id>`.
- Unknown-vendor blocks preserve raw input without guessing semantics.

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
