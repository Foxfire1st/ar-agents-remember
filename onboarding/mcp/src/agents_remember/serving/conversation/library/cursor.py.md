# mcp/src/agents_remember/serving/conversation/library/cursor.py

## Governing Overview

[Native conversation library overview](overview.md)

## Purpose

The one mint/verify boundary for every library opaque token — list cursors, read cursors,
conversation keys, and server-private native resume targets — plus the identity digests and
content-derived catalog generations those tokens bind.

## Code Commentary

### Logic

`LibraryCursorAuthority` holds one random per-application HMAC-SHA256 signing key (minted by
`mint_signing_key`, never persisted). Every token is a purpose-branded base64url JSON payload
closed by a MAC over the canonical serialized body: list/read cursors carry a
`LibraryCursorBinding` (scope, purpose, generation, schema version) plus the native position;
conversation keys carry a `LibraryKeyBinding` plus the vendor identity; resume targets add the
launch material and stay server-private. `identity_digest` is the server-issued stale-open check
token recomputed from native identity; `catalog_generation` folds one native catalog signature
into a positive wire integer, so the generation changes exactly when the store observable
changes without any server-side counter or index.

### Conventions

Verification is fail-closed at every step: wrong purpose prefix, undecodable envelope,
unsupported schema version, bad MAC, invalid binding model, or wrong cursor purpose each raise
`InvalidLibraryCursorError`. A server restart invalidates outstanding tokens honestly; the
caller re-lists from native authority.

### Invariants And Boundaries

- Possession of a token is never authorization: services re-resolve the caller binding and
  re-check scope, purpose, and generation on every call (design section 6.8).
- Resume targets must never appear on any wire model, log, or diagnostic; review O1 records
  that the purpose prefix itself is not MAC-covered, accepted hardening while targets stay
  server-private.
- Native cursor positions are text-or-integer only (bools rejected); read positions must name
  an ordinal above the first item where the port requires it.
- The signing key is per app lifetime and at least 32 bytes; no token content is authoritative
  beyond the local operator posture it is issued to.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured for this internal token authority.

No configured domain documentation was available.

### Repo-Internal References

The cursor suite round-trips every token family and probes tamper, wrong-purpose, and garbage
rejection; the contract module owns the branded token types this authority mints.

- The cursor authority signs and validates purpose-bound list/read coordinates and native identities. [1]
- The cursor authority signs and validates purpose-bound list/read coordinates and native identities. [2]
- Identity digests are stable and scope/vendor-sensitive; catalog generations are content-derived and positive. [3]
- The purpose-branded token types and binding models are declared in the parent contract. [4]

### Cross-Repo References

No meaningful cross-repo boundary exists for this local token authority.

No meaningful cross-repo references found.
