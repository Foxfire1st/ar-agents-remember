# mcp/src/agents_remember/memory_quality/style/citations/lean_scopes.py

## Governing Overview

[Overview](../../overview.md)

## Purpose

Track the scope frames that determine a declaration's full Lean name.

## Code Commentary

Namespace frames supply name components. Section frames may carry a name, and mutual groups track member indentation. Possible interpretations of an unclassified scope token leave several stacks. The scanner retains lawful bare and named exits, then checks whether the remaining stacks agree on a declaration's namespace.

## Relationships

This lets the declaration scanner preserve verified names before an uncertain exit and resume emitting verified names when the namespace projections agree.

## Evidence

- `Scopes.close` updates the retained scope stacks for an exit. [1]
