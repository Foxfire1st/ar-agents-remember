# mcp/src/agents_remember/certification/digests.py

## Governing Overview

[Certification overview](overview.md)

## Purpose

Defines the single canonical content-digest function used to bind registries, plans, rails, and
terminal manifests to exact JSON-compatible contract bytes.

## Code Commentary

### Logic

`content_digest` converts Pydantic contracts to JSON-mode data, serializes with sorted keys and
compact stable separators, encodes UTF-8, and returns the SHA-256 hexadecimal digest.

### Conventions

Callers build the semantic payload; this owner supplies only canonical byte serialization and
hashing.

### Invariants And Boundaries

- All certification content digests use the same serialization rule.
- Mapping insertion order and presentation whitespace cannot affect the digest.
- The helper does not normalize semantic text or repair malformed values.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

No configured domain documentation could be checked.

### Repo-Internal References

- Canonical JSON bytes use sorted keys, compact separators, UTF-8, and SHA-256. [1]

### Cross-Repo References

No external repository or service is consulted.

- Digest derivation is local and deterministic. [2]
