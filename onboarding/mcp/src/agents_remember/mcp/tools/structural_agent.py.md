# mcp/src/agents_remember/mcp/tools/structural_agent.py

## Governing Overview

[MCP tools overview](overview.md)

## Purpose

Build only the retained structural dispatch answer.

## Code Commentary

The thin `dispatch_agent_payload` adapter forwards a typed DispatchAgentRequest and a
StructuralAgentRuntime constructed from private overrides to the application dispatcher,
then crosses `_tool_payload` once. Parent/child messaging, rename and retire adapters are
removed. Native role_message is owned elsewhere, not an alias or a leaf-ref compatibility
shim here. Public dispatch identity is the canonical task document and role; private runtime
correlation and authorization remain application/plane responsibilities.

## Current model evidence

- Current source section contains excerpt `from agents_remember.application.structural.agent_tools import (`; DTO/control ownership is not execution acceptance. [3]

## Historical superseded account (non-operative)

Prior removed-tool/current-roster claims below are preserved provenance, not current
registration, runtime capability or execution evidence.



Adapts strict structural request DTOs to application services for dispatch, parent/child messaging,
retirement, and rename. It replaces the removed public leaf/exact-id addressing adapter.

## Code Commentary

### Logic

Each payload function builds one structural runtime, receives its operation-specific typed request,
invokes the corresponding application tool, and validates an operation-specific structural response.

### Conventions

This module is intentionally thin; authorization and lifecycle behavior stay in the application
and serving layers.

### Invariants And Boundaries

- Do not accept runtime ids through `overrides` or request fields.
- Do not restore the deleted leaf-ref compatibility tool.
- Keep one payload adapter per public operation for registry introspection.

### Todos

None.

## Evidence

### Docs References


### Repo-Internal References

- Six payload adapters expose the structural agent operation family. [1]
- The application service owns authorization and mutation. [2]

### Cross-Repo References
