# mcp/src/agents_remember/mcp/registration/orchestration.py

## Governing Overview

[registration route overview](overview.md)

## Purpose

Registers agent-facing parent and child whole-message tools over structural seat relationships.

## Code Commentary

### Logic

`message_parent` derives the target entirely from the ambient caller. `message_child` accepts only
a canonical child task document, role, and message content. Both delegate persistence, authorization,
current-occupant resolution, and delivery to the structural application boundary.
The content fields after `role` are keyword-only in Python. FastMCP keeps the same named JSON fields,
while Ruff's positional-argument rule can enforce the implementation signature without changing the
published tool schema.

### Conventions

Runtime, lifecycle, inbox-row, gate, and adapter ids are absent from requests and responses.

### Invariants And Boundaries

- Ordinary traffic is re-resolved after replacement.
- Dispatch briefs and state signals are plane-owned, not model-posted through these tools.
- A child target must be an authorized direct structural relation.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Parent messaging has no caller-supplied target identity. [1]
- Child messaging accepts only structural target and content. [2]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
