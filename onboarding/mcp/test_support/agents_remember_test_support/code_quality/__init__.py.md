# mcp/test_support/agents_remember_test_support/code_quality/__init__.py

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

`__init__.py` marks `agents_remember_test_support.code_quality` as the package-local domain
for source-development quality helpers.

## Code Commentary

### Logic

The package currently exposes helper modules by explicit import. It does not
register MCP tools or runtime behavior.

### Invariants And Boundaries

- Code quality helpers are source-development utilities, not installed
  coordinator runtime behavior.
- Runtime MCP dependencies should not grow just because a development helper
  exists in this package.

## Evidence

### Repo-Internal References

- CRAP-Calculator lives in this package. [1]
- The source quality suite wrapper lives in this package. [2]
- Changed-line coverage is diagnostic; its calculator reports affected lines and branch outcomes. [3]
