# mcp/src/agents_remember/memory_quality/style/citations/lean_lex.py

## Governing Overview

[Overview](../../overview.md)

## Purpose

Prepare the physical lines used by the Lean declaration scanner.

## Code Commentary

The lexer masks comments, character literals and string bodies at their original columns. It keeps nesting, physical line positions and documentation-comment kinds so the declaration scanner can distinguish attached documentation from module documentation.

## Relationships

The token inventory also reads the collected ordinary and raw string literals with their source coordinates. Quoted identifier parts remain visible to the name reader.

## Evidence

- `code_lines` produces masked physical lines for the declaration scan. [1]
