# mcp/src/agents_remember/memory_quality/style/citations/lean_aliases.py

## Governing Overview

[Memory quality](../../overview.md)

## Purpose

Read the names and target of a Lean `alias` header for symbol anchoring.

## Code Commentary

The header accepts `alias name := target` and a bracketed pair such as `alias ⟨left, right⟩ := target`. A bracketed `_` slot contributes no name. The parser keeps its position across masked physical lines and returns the names once it reads the target identifier.

## Relationships

The [declaration scanner](lean_declarations.py.md) supplies the masked lines and uses the completed header to bind each returned name in scope.

## Evidence

- The header reads a simple binder or a bracketed pair and completes at the target identifier. [1]
