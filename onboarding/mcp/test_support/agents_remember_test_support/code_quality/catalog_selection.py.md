# mcp/test_support/agents_remember_test_support/code_quality/catalog_selection.py

## Governing Overview

[Quality verification overview](overview.md)

## Purpose

Narrows explicit lifecycle catalog consumer-list edits while retaining consumers removed by the change.

## Code Commentary

### Logic

`changed_catalog_consumers` parses both TOML versions. Only matching outer configuration and matching ordered artifact declarations can narrow selection. Each artifact must retain all fields other than its consumer list. Consumer lists must contain nonempty strings. A changed list contributes the union of old and new consumer paths, so deleting a consumer does not erase its impact.

### Conventions

An empty frozenset represents no changed consumer population. `None` means broader catalog semantics changed or its shape cannot safely narrow. Invalid TOML raises; it is not converted into an empty declaration.

### Invariants And Boundaries

Schema, scope, contract, artifact addition/removal and lifecycle-policy changes retain global invalidation through the caller. This helper returns dependency information; it neither runs tests nor grants certification authority.

### Todos

No source-local TODO is asserted.

## Evidence

### Docs References

No configured external domain source applies.

### Repo-Internal References

- Pure old/new consumer comparison preserves removed consumers and refuses broader narrowing. [1]

### Cross-Repo References

No cross-repository authority is used.
