# mcp/src/agents_remember/providers/grepai/__init__.py

## Governing Overview

[GrepAI Provider Overview](overview.md)

## Purpose

This package marker establishes `providers.grepai` as the provider-owned home
for GrepAI setup, context, and lifecycle modules.

## Code Commentary

### Logic

The file intentionally exports no runtime behavior. Callers import concrete
modules such as `providers.grepai.setup`, `providers.grepai.context`, or
`providers.grepai.lifecycle`.

### Invariants And Boundaries

- GrepAI implementation remains under this package and stays Docker-owned.
- Do not add provider orchestration to this marker file.

## Evidence

### Repo-Internal References

- The package overview describes the provider-owned GrepAI route. [1]
