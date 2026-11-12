# mcp/src/agents_remember/mcp/__main__.py

## Governing Overview

[Governing route overview](../../../overview.md)

## Purpose

Provides the Python module entrypoint for the MCP server.

## Code Commentary

### Logic

Imports main from the sibling server module. Direct module execution calls main and raises SystemExit with its return value.

### Conventions

Argument parsing and server composition belong to the imported main function.

### Invariants And Boundaries

The call to main is guarded by the __main__ name check.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation is configured. This card describes repository source only.

### Repo-Internal References

These constructs establish the behavior described above.

- Guarded delegation to the server entrypoint [1]

### Cross-Repo References

No cross-repository behavior is implemented in this file.
