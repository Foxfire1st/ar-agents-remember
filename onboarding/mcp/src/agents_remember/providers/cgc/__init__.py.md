# mcp/src/agents_remember/providers/cgc/__init__.py

## Governing Overview

[CodeGraphContext Provider Overview](overview.md)

## Purpose

This package marker establishes `providers.cgc` as the provider-owned home for
CodeGraphContext setup, context, and lifecycle modules.

## Code Commentary

### Logic

The file intentionally exports no runtime behavior. Callers import concrete
modules such as `providers.cgc.setup`, `providers.cgc.context`, or
`providers.cgc.lifecycle`.

### Invariants And Boundaries

- Do not add provider orchestration to this marker file.
- Keep provider behavior in the named child modules.

## Evidence

### Repo-Internal References

- The package overview describes the provider-owned CGC route. [1]
