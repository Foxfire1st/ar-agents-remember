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

`ConversationCursorError` (L39-L47) is the typed base; subclasses carry exact wire statuses —
`CursorInvalidError` 400 `cursor-invalid`, `CursorAuthorizationError` 403
`cursor-authorization`, `CursorEpochMismatchError` 409 `bridge-epoch-mismatch`,
`CursorResetRequiredError` 409 `cursor-reset-required`, `CursorConflictError` 400
`cursor-conflict` (L50-L82). Minting (L137-L143) closes a canonical base64url JSON payload with
a truncated HMAC-SHA256 hex signature; `_binding_payload` (L115-L134) records schema version,
purpose, principal, tenant, session, epoch, harness, vendor conversation, project scope,
generation, and position. `_decode` (L146-L169) enforces prefix, signature
(`hmac.compare_digest`), decodability, schema version, and purpose before any payload use;
`_require_binding` (L172-L194) then re-compares every decoded field against the authorized
request context — cross-principal/tenant/session is 403, wrong epoch is 409 with reason
`epoch-mismatch`, wrong harness/vendor/scope is 400. `mint_page_cursor`/`decode_page_cursor`
(L197-L226) carry an ordinal boundary and survive projector restarts (generation `native`);
`mint_event_cursor`/`decode_event_cursor` (L229-L262) bind one projector generation and
sequence; `require_same_generation` (L265-L272) turns a generation change into
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available for this authority. | — | — |

## Repo-Internal References

The strict cursor brands and identity/binding models live in the parent contract module; the
service holds the secret and runs the pre-stream checks; the reviewer ran a 19-vector forgery
battery against this authority (all held).

| Finding | Citations | Source Path |
| --- | --- | --- |
| The purpose-branded token prefixes and root validators define the four non-interchangeable cursor brands. | L74-L93 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| `ActiveConversationRef` and `AuthorizationBinding` carry the identity/caller fields every cursor binds. | L133-L138 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| The service decodes and generation-checks every cursor before any stream exists. | L97-L135 | [service.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/service.py) |
| The routes map dual resume inputs and every cursor error to typed pre-stream statuses. | L106-L118; L85-L89 | [api.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/api.py) |

## Cross-Repo References

No cross-repository implementation participates in this cursor authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the sidecar for the active cursor
  authority — signed purpose-branded tokens, per-wire binding re-checks, the typed cursor error
  family. Verification is blank because the new source file is uncommitted; closeout owns its
  first source stamp.
