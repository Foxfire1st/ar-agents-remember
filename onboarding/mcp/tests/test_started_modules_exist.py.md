# mcp/tests/test_started_modules_exist.py

## Governing Overview

[MCP Tests](overview.md)

## Purpose

This architecture test checks Python module launches constructed by shipped package source and the console script targets declared in `mcp/pyproject.toml`.

## Code Commentary

The AST scan resolves literal or module-constant targets in interpreter argument sequences, including separately declared commands and recognized generated argument text. It reports unresolved forms unless their file and reason are declared. Declared forms must still appear and known module destinations are checked on disk. Git commands, development scripts, test support and prose examples are outside the product launch census.

## Relationships

The console check follows a named function or re-export to its defining module, using the original imported name for aliases and tracking file and symbol pairs to detect cycles. Both checks inspect files without importing their targets.

## Evidence

- The package scan reports missing module files and undeclared unresolved forms. [1]
- The console check resolves each declaration to a module file and a function definition, following re-exports. [2]
