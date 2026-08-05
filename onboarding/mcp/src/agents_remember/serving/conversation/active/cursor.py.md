# mcp/src/agents_remember/serving/conversation/active/cursor.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/cursor.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T17:35+02:00 |
| lastVerifiedCommitHash | `41b2fd6452ee572799fa10c4f9c820ab549ec3d2`|
| lastVerifiedCommitDate | 2026-07-19T19:12:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active conversation serving overview](overview.md)

## Purpose

The active page/event cursor authority (leaf R4): HMAC-signed, purpose-branded opaque tokens
binding the caller authorization (principal/tenant), the exact AR session and bridge epoch, the
native conversation identity, the projector generation (event cursors), the cursor schema
version, and the page/event purpose — plus the typed cursor error family the routes map to
precise HTTP statuses.

## Code Commentary

### Logic

cit:([`ConversationCursorError`], mcp/src/agents_remember/serving/conversation/active/cursor.py:39-47) is the typed base; subclasses carry exact wire statuses —
`CursorInvalidError` 400 `cursor-invalid`, `CursorAuthorizationError` 403
`cursor-authorization`, `CursorEpochMismatchError` 409 `bridge-epoch-mismatch`,
`CursorResetRequiredError` 409 `cursor-reset-required`, `CursorConflictError` 400
`cursor-conflict` cit:([`CursorInvalidError`, `CursorAuthorizationError`, `CursorEpochMismatchError`, `CursorResetRequiredError`, `CursorConflictError`], mcp/src/agents_remember/serving/conversation/active/cursor.py:50-54; mcp/src/agents_remember/serving/conversation/active/cursor.py:57-61; mcp/src/agents_remember/serving/conversation/active/cursor.py:64-68; mcp/src/agents_remember/serving/conversation/active/cursor.py:71-75; mcp/src/agents_remember/serving/conversation/active/cursor.py:78-82). Minting cit:([`mint_page_cursor`, `mint_event_cursor`], mcp/src/agents_remember/serving/conversation/active/cursor.py:197-212; mcp/src/agents_remember/serving/conversation/active/cursor.py:229-245) closes a canonical base64url JSON payload with
a truncated HMAC-SHA256 hex signature; cit:([`_binding_payload`], mcp/src/agents_remember/serving/conversation/active/cursor.py:115-134) records schema version,
purpose, principal, tenant, session, epoch, harness, vendor conversation, project scope,
generation, and position. cit:([`_decode`], mcp/src/agents_remember/serving/conversation/active/cursor.py:146-169) enforces prefix, signature
(`hmac.compare_digest`), decodability, schema version, and purpose before any payload use;
cit:([`_require_binding`], mcp/src/agents_remember/serving/conversation/active/cursor.py:172-194) then re-compares every decoded field against the authorized
request context — cross-principal/tenant/session is 403, wrong epoch is 409 with reason
`epoch-mismatch`, wrong harness/vendor/scope is 400. cit:([`mint_page_cursor`, `decode_page_cursor`], mcp/src/agents_remember/serving/conversation/active/cursor.py:197-212; mcp/src/agents_remember/serving/conversation/active/cursor.py:215-226) carry an ordinal boundary and survive projector restarts (generation `native`);
`mint_event_cursor`/cit:([`decode_event_cursor`], mcp/src/agents_remember/serving/conversation/active/cursor.py:248-262) bind one projector generation and
sequence; cit:([`require_same_generation`], mcp/src/agents_remember/serving/conversation/active/cursor.py:265-272) turns a generation change into
`cursor-reset-required` with reason `generation-changed`.

### Conventions

The signature is tamper-evidence minted with an app-scoped secret held by the active service;
the *binding checks* are the actual authorization mechanism — possession of a cursor is never
authorization. Pre-stream failures are typed HTTP errors; established-stream continuity failures
are gap events, never HTTP resets.

### Invariants And Boundaries

- The four cursor brands in `conversation.models` are non-interchangeable: a token minted for
  one purpose fails validation for any other before any lookup happens.
- Every decoded field is re-compared against the authorized request context on every wire.
- The signing secret is per-app random and never persisted; a daemon restart invalidates old
  generations loudly through the reset path (worker Confidence Register 1).
- Page cursors name ordinal boundaries, event cursors name (generation, sequence); the two
  never mix.

### Todos

None.

## Docs References

The resolved `Domain Documentation` registry has no entries. The cursor grammar is the
repository-owned strict wire contract cited below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available for this authority. | — | — |

## Repo-Internal References

The strict cursor brands and identity/binding models live in the parent contract module; the
service holds the secret and runs the pre-stream checks; the reviewer ran a 19-vector forgery
battery against this authority (all held).

| Finding | Anchor | Source |
| --- | --- | --- |
| The purpose-branded token prefixes and root validators define the four non-interchangeable cursor brands. | `ActivePageCursor`, `ActiveEventCursor`, `LibraryListCursor`, `LibraryReadCursor` | mcp/src/agents_remember/serving/conversation/models.py:84-85; mcp/src/agents_remember/serving/conversation/models.py:88-89; mcp/src/agents_remember/serving/conversation/models.py:92-93; mcp/src/agents_remember/serving/conversation/models.py:96-97 |
| `ActiveConversationRef` and `AuthorizationBinding` carry the identity/caller fields every cursor binds. | `ActiveConversationRef`, `AuthorizationBinding` | mcp/src/agents_remember/serving/conversation/models.py:129-131; mcp/src/agents_remember/serving/conversation/models.py:134-136 |
| The service decodes and generation-checks every cursor before any stream exists. | "before_ordinal = decode_page_cursor(", "decoded = decode_event_cursor(", "require_same_generation(decoded" | mcp/src/agents_remember/serving/conversation/active/service.py:94-94; mcp/src/agents_remember/serving/conversation/active/service.py:114-115 |
| The routes map dual resume inputs and every cursor error to typed pre-stream statuses. | `_map_typed_error`, `_resume_cursor` | mcp/src/agents_remember/serving/conversation/active/api.py:77-99; mcp/src/agents_remember/serving/conversation/active/api.py:111-123 |

## Cross-Repo References

No cross-repository implementation participates in this cursor authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-02T21:14+02:00 — W2-B03 curator: resolved 11 initial citation findings (4 anchor, 3 prose, 4 source); scoped recheck PASS (0 findings). Verification metadata unchanged.

- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the sidecar for the active cursor
  authority — signed purpose-branded tokens, per-wire binding re-checks, the typed cursor error
  family. Verification is blank because the new source file is uncommitted; closeout owns its
  first source stamp.
