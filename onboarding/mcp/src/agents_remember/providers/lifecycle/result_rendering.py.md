# mcp/src/agents_remember/providers/lifecycle/result_rendering.py

## Governing Overview

[Provider Lifecycle Overview](overview.md)

## Purpose

`result_rendering.py` retains text/JSON rendering helpers for provider lifecycle result data.
The lifecycle CLI caller was removed; these definitions do not establish an active CLI.

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
