# mcp/tests/test_definition_scope_boundaries.py

## Governing Overview

[Tests](overview.md)

## Purpose

Checks definition-cache lifetimes at MCP, finite CLI, dashboard dispatch and background quality-worker boundaries.

## Code Commentary

A native call shares Python definitions and exact TypeScript anchor inputs inside its request. The detached quality worker repeats those parses inside its own scopes. Journal cases check caller-owned copies and a new read when the witness moves. The dashboard runner checks reuse across two requests through the process owners.

The MCP test invokes a real registered synchronous handler through the common async dispatcher and verifies reuse within a call and disposal between calls. Parameterized finite CLI adapters verify disposal after success and exceptions. A quality worker starts with an isolated context rather than inheriting the starting call.

The dashboard cases cover plain, reload and daemon option dispatch with a substituted dashboard runner serving real HTTP requests. They establish that CLI dispatch does not wrap the server lifetime in a definition scope; they do not launch the real reload or daemon subprocesses.

## Relationships

The counted parser is shared with `test_definition_scope.py`. Production lifetime owners are the MCP server, CLI entry point and quality-run registry.

## Evidence


- The registered synchronous handler reuses its Python definition and TypeScript anchor memo within one native call. The next call parses the inputs again. [1]

- Finite CLI scopes clear on success and exceptions. [2]
- Dashboard option dispatch leaves server requests outside a process scope. [3]

- A detached quality worker reparses the named definitions and anchors in its own context. [4]
