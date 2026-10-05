# mcp/tests/test_route_index_memory_scope.py

## Governing Overview

[Route overview](overview.md)

## Purpose and current source account

The scoped fixture refreshes only the leaf overview index while rereading configured official roots for authority. Forged leaf scope pointing at official onboarding, direct official scope and contractless refresh all refuse. This exercises memory write fencing in a disposable fixture, not an official-memory mutation.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]
