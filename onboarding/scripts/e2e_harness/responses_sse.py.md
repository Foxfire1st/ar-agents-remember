# responses_sse.py

## Governing Overview

[Ambient Role-Chat E2E Harness](overview.md)

## Purpose

Renders the minimal Responses API server-sent-event sequences used by the deterministic provider.

## Code Commentary

### Logic

Dedicated builders create function-call, tool-search, and assistant-message output items, then append
one standard zero-usage completion event and serialize the event stream with compact JSON.

### Conventions

Wire projection is isolated from fixture state and tool-selection policy. Namespace is emitted only
for a namespaced tool definition.

### Invariants And Boundaries

- Every response has one created event and one completed event.
- Function arguments are compact JSON strings, matching the Responses wire contract.
- This module projects already-made decisions; it never chooses a tool or route.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured; the live Codex consumer validates these fixture frames.

- Each helper emits a bounded created/output/completed SSE sequence. [1]

### Repo-Internal References

- Namespace is conditional while function name and JSON arguments are always present. [2]

### Cross-Repo References

No meaningful cross-repository reference applies.

- The projection has no external repository dependency. [3]
