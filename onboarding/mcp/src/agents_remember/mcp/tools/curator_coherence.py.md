# mcp/src/agents_remember/mcp/tools/curator_coherence.py

## Governing Overview

[MCP tool-adapter overview](overview.md)

## Purpose

Provides the one payload adapter between the public `curator_coherence` registration and its
configured application boundary.

## Code Commentary

### Logic

`curator_coherence_payload` delegates the typed request to `curator_coherence_tool` and passes the
result through the common `_tool_payload` response-model conformance boundary.

### Conventions

Adapters in this route contain no lifecycle policy. Public schema, configured admission, and
publication semantics remain in their dedicated owners.

### Invariants And Boundaries

- The adapter does not add action aliases, filename fallbacks, or alternate response shapes.
- Tool-response conformance is applied exactly once through the shared helper.

### Todos

None recorded.

## Evidence

### Docs References

No configured external documentation applies.

This adapter is repository-internal.

### Repo-Internal References

- The adapter delegates one request and validates one named public result. [1]

### Cross-Repo References

No meaningful cross-repository reference applies.

No cross-repository boundary is introduced.
