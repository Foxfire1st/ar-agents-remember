# mcp/src/agents_remember/serving/conversation/library/__init__.py

## Governing Overview

[Native conversation library overview](overview.md)

## Purpose

Marks the package that owns dormant native conversation list/read/resume serving.

## Code Commentary

### Logic

Contains only a package docstring; sibling `api.py` owns the route entrypoint.

### Conventions

Keep the marker behavior-free and separate from active exact-session projection.

### Invariants And Boundaries

- Library reads use native history authority, project scope, authorization, and library cursors.
- This marker does not enable a capability or load a vendor dependency.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

No configured domain documentation was available.

### Repo-Internal References

- The sibling router reserves the harness-native conversation-library prefix. [1]

### Cross-Repo References

No meaningful cross-repo references found.

No meaningful cross-repo references found.
