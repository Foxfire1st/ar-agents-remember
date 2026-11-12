# mcp/src/agents_remember/worktrees/integration/direct_landing/__init__.py

## Governing Overview

[integration overview](../overview.md)

## Purpose

Declares the integration subpackage that owns direct-landing execution and recovery.

## Code Commentary

### Logic

The marker groups direct-landing errors, accepted operation state, execution, and recovery without creating another landing entrypoint.

### Conventions

Public application routing stays above this package; durable evidence and Git reconciliation stay here.

### Invariants And Boundaries

- Direct landing remains journaled and recoverable; no unjournaled compatibility path belongs in this marker.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies to this package marker.

### Repo-Internal References

- The package docstring assigns direct-landing execution and recovery ownership. [1]

### Cross-Repo References

No cross-repository boundary is owned here.
