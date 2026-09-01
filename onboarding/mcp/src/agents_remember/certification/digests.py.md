# mcp/src/agents_remember/certification/digests.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/digests.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T03:11+02:00 |
| lastVerifiedCommitHash | `0506b57a1a80e0b377e9cc3303e1841d3bd4799a`|
| lastVerifiedCommitDate | 2026-09-01T12:17:08+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical JSON bytes use sorted keys, compact separators, UTF-8, and SHA-256. | `content_digest` | mcp/src/agents_remember/certification/digests.py:12-22 |

## Cross-Repo References

No external repository or service is consulted.

| Finding | Anchor | Source |
| --- | --- | --- |
| Digest derivation is local and deterministic. | `content_digest` | mcp/src/agents_remember/certification/digests.py:12-22 |

## Update History

- 2026-09-01T03:11+02:00 — Created for the certification package's canonical digest seam.
  Verification remains closeout-owned until the source candidate is committed.
