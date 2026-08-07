# mcp/src/agents_remember/serving/conversation/control/refs.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/refs.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `b252c42cca200933d5c9c36e26de47a526a569ce`|
| lastVerifiedCommitDate |  2026-08-07T23:58:52+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structured conversation control overview](overview.md)

## Purpose

The opaque signed control-reference authority (R1–R4): every control-domain token is a
purpose-branded, HMAC-signed payload binding the caller authorization (principal/tenant), the
exact AR session and bridge epoch, and the operation identity it names. The four brands are
non-interchangeable; a token minted for one purpose fails validation for any other before any
lookup. Tokens carry no content of any kind — identity fields only, the same posture as the
landed L1 cursor authority.

## Code Commentary

### Logic

Four purpose brands map through cit:([`_PREFIX_BY_PURPOSE`], mcp/src/agents_remember/serving/conversation/control/refs.py:39-44): `ar-oqr1.` operationRef (stable
queue-row identity kind/operationId/sequence), `ar-wdr1.` withdrawalRef (caller/session/epoch/
operation-bound withdraw target, adds the withdraw ledger salt), `ar-wrr1.` recoveryRef (opaque
pending-recovery identity, adds the `withdrawRequestId`, never any content), and `ar-war1.`
recoveryAssetRef (one recoverable staged asset's exchange identity). cit:([`mint_ref`], mcp/src/agents_remember/serving/conversation/control/refs.py:136-161) canonically
serializes (`_canonical` cit:(["def _canonical"], mcp/src/agents_remember/serving/conversation/control/refs.py:103-103) — sorted keys, no spaces) the payload, appends the app-scoped-secret
HMAC-SHA256 signature cit:([`_sign`], mcp/src/agents_remember/serving/conversation/control/refs.py:109-110), and base64url-encodes under the brand prefix. `decode_ref`
cit:(["def decode_ref"], mcp/src/agents_remember/serving/conversation/control/refs.py:164-164) splits the prefix, base64-decodes, verifies the signature **before** parsing the payload
(no oracle), then cit:([`_check_payload`], mcp/src/agents_remember/serving/conversation/control/refs.py:196-218) re-compares every decoded binding field against the
authorized request context — the actual authorization mechanism. cit:([`OperationIdentity`], mcp/src/agents_remember/serving/conversation/control/refs.py:75-91) is the
value-equal (kind, operation_id, sequence) triple carried in operation/withdrawal refs;
cit:([`ref_identity`], mcp/src/agents_remember/serving/conversation/control/refs.py:221-233) extracts it. `REF_SCHEMA_VERSION = 1` cit:(["REF_SCHEMA_VERSION = 1"], mcp/src/agents_remember/serving/conversation/control/refs.py:35-35) rides every payload.

### Conventions

Signature is tamper-evidence; the binding re-check is authorization. Minting/decoding uses only the
service's control secret; a ref never leaves this module carrying content. Cross-purpose reuse is a
typed failure, not a silent mismatch.

### Invariants And Boundaries

- Tokens carry identity only; prompt/asset content never rides a ref.
- The signature is verified before the payload is parsed — no parse-then-check oracle.
- Every decoded field (principal, tenant, session, epoch, identity) is re-bound against the live
  request; possession of a token is never authorization.
- The typed `ControlRefError` family maps one-to-one to the wire: `RefInvalidError` → 400
  `ref-invalid`, `RefAuthorizationError` → 403 `ref-authorization`, `RefEpochMismatchError` → 409
  `bridge-epoch-mismatch`.
- A daemon restart rotates the app-scoped secret, so every prior ref fails loudly (not-found), the
  recovery-as-lease posture.

### Todos

None.

## Docs References

No Domain Documentation source is configured; the ref grammar is repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The ref authority mirrors the L1 cursor authority's posture and binds the L0 authorization DTO; the
service owns the app-scoped secret this module signs with.

| Finding | Anchor | Source |
| --- | --- | --- |
| The `AuthorizationBinding` (principal/tenant) re-bound in every payload check. | "class AuthorizationBinding(WireModel):" | mcp/src/agents_remember/serving/conversation/_models_wire.py:117-117 |
| The app-scoped control secret this module signs/verifies with. | "def secret" | mcp/src/agents_remember/serving/conversation/control/service.py:233-233 |
| The L1 cursor authority whose signed-purpose-branded posture this mirrors. | "CURSOR_SCHEMA_VERSION = 1" | mcp/src/agents_remember/serving/conversation/active/cursor.py:34-34 |
| Consumers: the queue projection mints operation/withdrawal refs; withdrawals/attachments decode and re-bind them. | "async def operation_queue" | mcp/src/agents_remember/serving/conversation/control/queue_projection.py:47-47 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260731-EFA-L2 Current Delta

Ref minting and decoding now take two named halves instead of parallel arguments, and **both sides
take the same pair**:

- **`RefBinding`** (`authorization`, `ar_session_id`, `bridge_epoch`) — what a reference is bound
  TO. A ref is only meaningful re-bound to all three; minting against one of them and verifying
  against another is precisely the confused-deputy problem the branding exists to stop, which is
  why mint and decode take the same binding value rather than three parallel arguments each.
- **`RefTarget`** (`identity`, optional `withdraw_request_id`, optional `asset_id`) — what a
  reference POINTS AT: the operation, and optionally the withdrawal or asset inside it.

The opaque ref format, the signature and the verification failures are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B22 curator: replaced the superseded
  `(L…)` prose citations and the `n/a` table rows with exact anchors and fixer-generated
  ranges; exact non-fixing check returns zero findings.

- 2026-07-31T17:48+02:00 — 260731-EFA-L2 curator: re-derived 3 stale self-citations pushed down by
  this leaf's own `RefBinding`/`RefTarget` dataclasses cit:(["class RefBinding"], mcp/src/agents_remember/serving/conversation/control/refs.py:114-114): `mint_ref` is L136-L161 (was
  L112, now inside `RefBinding`), `_check_payload` is L196-L218 (was L179, mid-`decode_ref`), and
  `OperationIdentity` is L75-L91 (was L74, the blank line above it). Signing, sign-before-parse
  decode and the binding re-check are unchanged. Still stale and left for the next citation pass
  (verified, not repaired here): `decode_ref` is L164-L193 (cited L144) and `REF_SCHEMA_VERSION` is
  L35 (cited L34).
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation. `queue_projection.py`
  is now 152 lines; the two `mint_ref` calls the row names — the `"operation-ref"` mint and the
  `"withdrawal-ref"` mint inside the authorized `CockpitQueueIdentity` — read at L111-L138 (was L74-L144,
  which now covers the revision-bookkeeping/eviction block instead).
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `RefBinding` (what a ref is bound to) and `RefTarget` (what it points at) as the shared mint/decode shape.
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the opaque signed
  control-reference authority — four non-interchangeable purpose brands, sign-before-parse decode,
  per-wire binding re-check, and the typed `ControlRefError` family. Verification is blank because
  the new source file is uncommitted; closeout owns its first source stamp.
