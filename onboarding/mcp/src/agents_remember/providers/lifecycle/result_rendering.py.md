# mcp/src/agents_remember/providers/lifecycle/result_rendering.py

## Governing Overview

[Provider Lifecycle Overview](overview.md)

## Purpose

`result_rendering.py` owns text/JSON rendering for provider lifecycle command
results.

## Code Commentary

### Logic

The module renders plain lifecycle result fields, streams captured native
command output without wrapping it, compacts CGC/GrepAI run results into API
payloads, and routes dry-run versus live command rendering.

### Invariants And Boundaries

- Captured command stdout/stderr must be streamable as native output for run
  actions.
- Rendering helpers must not perform lifecycle mutations.
- GrepAI run rendering intentionally mirrors CGC run rendering.

## Evidence

### Repo-Internal References

- The lifecycle CLI delegates result display to this module. [1]
