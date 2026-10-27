# mcp/tests/test_mcp_dispatch_concurrency.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Exercises real MCP dispatch concurrency, write ordering and per-call context isolation.

## Code Commentary

The transport test keeps a long synchronous tool blocked while a registered quality poll and a read complete. A cancellation test proves the next synchronous write waits until the first worker drains. Conditional-read cases distinguish strict boolean flags from coercible strings. Concurrent calls keep ContextVars, memo dictionaries, recorded reads and answer-log caller data separate; an async-handler case retains its original event-loop behavior.

### Invariants And Boundaries

Read-only hints are dispatch classification, not sandbox authority or host-wide purity. The tests assert source-defined ordering and transport behavior; a card does not certify their execution on another candidate.

## Evidence


- A poll and read answer before a long synchronous call is released. [1]



- Cancellation drains before the next write and call contexts stay separate. [2]


