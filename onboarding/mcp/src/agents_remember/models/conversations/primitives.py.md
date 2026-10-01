# mcp/src/agents_remember/models/conversations/primitives.py

## Governing Overview

[models conversations overview](overview.md)

## Purpose

`models/conversations/primitives.py` is the lowest layer of the responsibility-owned
conversation wire models (260731-EFA-L9 R1): strict immutable wire configuration and the opaque
purpose-branded token root every cursor/operation identity derives from.

## Code Commentary

### Logic

`WireModel` (cit:(["class WireModel"], mcp/src/agents_remember/models/conversations/primitives.py:15-15)) makes public DTOs immutable, camel-case on the wire, and
closed to unknown fields. `_OpaqueToken` (cit:(["class _OpaqueToken"], mcp/src/agents_remember/models/conversations/primitives.py:26-26)) is the branded
`RootModel[str]` base; `OperationFingerprint` (cit:(["class OperationFingerprint"], mcp/src/agents_remember/models/conversations/primitives.py:44-44)) is its
SHA-256 operation-identity specialization.

### Conventions

- Purpose-prefixed opaque types keep active-page, active-event, library-list, library-read,
  library-key, private native-resume, and operation identities non-interchangeable.

### Invariants And Boundaries

- This module must not import any sibling conversation module (it is the layer bottom); the armed
  layering rail and resolved-forward-reference architecture test preserve that boundary without a
  task/date snapshot.

### Todos

No known follow-up.

## Evidence

### Docs References

No external/domain documentation is configured.

No configured domain documentation was available.

### Repo-Internal References

### Cross-Repo References

No cross-repository implementation participates.

No meaningful cross-repo references found.
