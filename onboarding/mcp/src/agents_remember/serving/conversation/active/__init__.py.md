# mcp/src/agents_remember/serving/conversation/active/__init__.py

## Governing Overview

[Active conversation serving overview](overview.md)

## Purpose

Marks the package that owns active exact-session structured-conversation serving.

## Code Commentary

### Logic

Contains only a package docstring; route ownership is implemented by sibling `api.py`.

### Conventions

Keep the marker behavior-free and use `api.py` as the route entrypoint.

### Invariants And Boundaries

- Active conversation work is distinct from dormant native library and control routes.
- This marker must not become an import-time registration path.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

No configured domain documentation was available.

### Repo-Internal References

- The sibling router implements the two owned active routes on the exact-session conversation prefix. [1]

### Cross-Repo References

No meaningful cross-repo references found.

No meaningful cross-repo references found.
