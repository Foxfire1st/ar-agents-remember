# mcp/src/agents_remember/worktrees/integration/lifecycle/generation/__init__.py

## Governing Overview

[Package overview](overview.md)

## Purpose

Describes the lifecycle generation construction and same-generation resume package.

## Code Commentary

### Logic

The initializer contains only the package docstring. `creation` and `resume` are separate concrete owners and are not re-exported here.

### Conventions

Import the needed constructor or resume transition from its actual child module.

### Invariants And Boundaries

Importing this package does not create a journal generation, claim a door, launch a worker or publish a ref.

### Todos

None recorded.

## Evidence

### Docs References

The configured Domain Documentation registry has no entries. This repository-owned contract is established by the source below.

The resolved registry supplies no applicable external Domain Documentation source for this card.

### Repo-Internal References

- The initializer names the package ownership without executing a workflow. [1]

### Cross-Repo References

No cross-repository implementation boundary is owned here.


No separately configured cross-repository source is used for this card.
