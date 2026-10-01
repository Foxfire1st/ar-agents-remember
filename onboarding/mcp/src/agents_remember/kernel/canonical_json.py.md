# mcp/src/agents_remember/kernel/canonical_json.py

## Governing Overview

[mcp route overview](../../../overview.md)

## Purpose

One canonical JSON encoder for content-addressed digests: "the same logical value always produces the same
bytes", owned in one place across the tree.

## Code Commentary

### Logic

`CANONICAL_JSON_KWARGS` fixes the encoding: `sort_keys=True`, `separators=(",", ":")`, `ensure_ascii=False`,
`allow_nan=False`. `canonical_json_bytes` encodes a value to canonical UTF-8 JSON; `sha256_digest` returns the
lowercase hex SHA-256 over those bytes; `prefixed_sha256_digest` returns the `sha256:<hex>` form used in receipts
and exports.

`decoded_json` decodes stored canonical JSON text through an `object_pairs_hook` that refuses a duplicate key
(`"duplicate JSON key: <key>"`) instead of applying last-one-wins. `require_mapping` narrows a decoded value to a
mapping with a legible `ValueError`.

### Conventions

This is a kernel primitive because it holds no feature: it decides only separators, key order, Unicode and float
policy, and it refuses the value classes whose encoding would not be reproducible. `allow_nan` is off because NaN
has no single textual spelling, so a digest over it would not identify the value it seals.

### Invariants And Boundaries

- Exactly one owner: there is no second canonical-encoding path in the repository, so a digest computed in two
  places cannot disagree about separators or key order.
- The encoder is used as a pure function; it holds no state, performs no I/O and raises only the JSON encoder's
  own `TypeError`/`ValueError` for an unencodable value.
- Its first consumer is the knowledge substrate (`models/knowledge/digest.py` for the revision seal,
  `memory/knowledge/records.py` for typed columns, `memory/knowledge/schema.py` for the schema fingerprint); the
  module is deliberately placed in `kernel` (rank 1) so `models` (rank 2) and `memory` (rank 12) may both import
  it downward.

### Todos

None recorded. `prefixed_sha256_digest` and `require_mapping` have no consumer inside this leaf's slice and exist
for later leaves (receipt/export and schema-mapping readers).

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The one canonical encoding policy, including the deliberate `allow_nan=False`. [1]
- The byte encoder and the two digest spellings. [2]
- The duplicate-key-refusing decoder a stored typed column is read through. [3]
- The revision seal computed through this encoder. [4]
- The typed-column storage path that reuses this encoder and decoder. [5]
- The schema fingerprint computed through this encoder. [6]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
