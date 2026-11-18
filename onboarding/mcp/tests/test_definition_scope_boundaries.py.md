# mcp/tests/test_definition_scope_boundaries.py

## Governing Overview

[Tests](overview.md)

## Purpose

Checks definition-cache lifetimes at MCP, finite CLI, dashboard dispatch and background quality-worker boundaries.

## Code Commentary

The MCP test invokes a real registered synchronous handler through the common async dispatcher and verifies reuse within a call and disposal between calls. Parameterized finite CLI adapters verify disposal after success and exceptions. A quality worker starts with an isolated context rather than inheriting the starting call.

The dashboard cases cover plain, reload and daemon option dispatch with a substituted dashboard runner serving real HTTP requests. They establish that CLI dispatch does not wrap the server lifetime in a definition scope; they do not launch the real reload or daemon subprocesses.

## Relationships

The counted parser is shared with `test_definition_scope.py`. Production lifetime owners are the MCP server, CLI entry point and quality-run registry.

## Evidence

- MCP dispatch shares a synchronous handler context within one call. [1]
- Finite CLI scopes clear on success and exceptions. [2]
- Dashboard option dispatch leaves server requests outside a process scope. [3]
- A background worker owns a context separate from its starting call. [4]
