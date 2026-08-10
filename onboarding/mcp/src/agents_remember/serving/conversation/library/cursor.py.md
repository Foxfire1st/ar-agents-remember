# mcp/src/agents_remember/serving/conversation/library/cursor.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/cursor.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate |  2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured for this internal token authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The cursor suite round-trips every token family and probes tamper, wrong-purpose, and garbage
rejection; the contract module owns the branded token types this authority mints.

| Finding | Anchor | Source |
| --- | --- | --- |
| List/read cursors round-trip and reject tampering and wrong-purpose use. | `test_list_cursor_round_trip_and_tamper_rejection`, `test_read_cursor_round_trip_and_wrong_purpose_rejection` | mcp/tests/test_conversation_library_cursor.py:37-50; mcp/tests/test_conversation_library_cursor.py:53-66 |
| Conversation keys and resume targets round-trip and reject garbage/foreign signatures. | `test_conversation_key_round_trip_and_garbage_rejection`, `test_resume_target_round_trip_and_garbage_rejection` | mcp/tests/test_conversation_library_cursor.py:77-90; mcp/tests/test_conversation_library_cursor.py:93-110 |
| Identity digests are stable and scope/vendor-sensitive; catalog generations are content-derived and positive. | `identity_digest`, `catalog_generation` | mcp/src/agents_remember/serving/conversation/library/cursor.py:72-87; mcp/src/agents_remember/serving/conversation/library/cursor.py:89-98 |
| The purpose-branded token types and binding models are declared in the parent contract. | "class LibraryCursorBinding(WireModel):", "class LibraryKeyBinding(WireModel):" | mcp/src/agents_remember/models/conversations/cursors.py:54-54; mcp/src/agents_remember/models/conversations/cursors.py:61-61 |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local token authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T16:44:57+02:00 — L6 W1-B02 curator: repaired 4 repository-internal citations for cursor tests, digest/generation methods, and parent binding models.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the signed cursor/key authority
  sidecar. Verification is blank until closeout commits and stamps the new source.
