# mcp/test_support/agents_remember_test_support/code_quality/catalog_selection.py

## Governing Overview

[Quality verification overview](overview.md)

## Purpose

Narrows explicit lifecycle catalog consumer-list edits while retaining consumers removed by the change.

## Code Commentary

### Logic

`changed_catalog_consumers` reads both catalog versions through `parse_catalog`, the shared catalog reader, so an invalid file raises `EvidenceLifecycleError` with the reader's refusal instead of a bare parse error. Only matching outer configuration and matching ordered artifact declarations can narrow selection. Each artifact must retain all fields other than its consumer list. Consumer lists must contain nonempty strings. A changed list contributes the union of old and new consumer paths, so deleting a consumer does not erase its impact.

### Conventions

An empty frozenset represents no changed consumer population. `None` means broader catalog semantics changed or its shape cannot safely narrow. Invalid TOML raises `EvidenceLifecycleError`, the shared reader's refusal, with the reason a reader has to act on; it is not converted into an empty declaration.

### Invariants And Boundaries

Schema, scope, contract, artifact addition/removal and lifecycle-policy changes retain global invalidation through the caller. This helper returns dependency information; it neither runs tests nor grants certification authority.

### Todos

No source-local TODO is asserted.

## Evidence

### Docs References

No configured external domain source applies.

### Repo-Internal References


- The helper reads both catalog versions through the shared reader and raises its error type, so an invalid catalog is refused by name rather than as a bare parse error. [2]
- Pure old/new consumer comparison preserves removed consumers and refuses broader narrowing. [3]

### Cross-Repo References

No cross-repository authority is used.

