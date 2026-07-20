# mcp/src/agents_remember/serving/conversation/control/refs.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/refs.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `0be0099744bf1287805acf0b95072127b70f7104`|
| lastVerifiedCommitDate |  2026-07-20T15:34:11+02:00|
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

Four purpose brands map through `_PREFIX_BY_PURPOSE` (L38): `ar-oqr1.` operationRef (stable
queue-row identity kind/operationId/sequence), `ar-wdr1.` withdrawalRef (caller/session/epoch/
operation-bound withdraw target, adds the withdraw ledger salt), `ar-wrr1.` recoveryRef (opaque
pending-recovery identity, adds the `withdrawRequestId`, never any content), and `ar-war1.`
recoveryAssetRef (one recoverable staged asset's exchange identity). `mint_ref` (L112) canonically
serializes (`_canonical`, L102 — sorted keys, no spaces) the payload, appends the app-scoped-secret
HMAC-SHA256 signature (`_sign`, L108), and base64url-encodes under the brand prefix. `decode_ref`
(L144) splits the prefix, base64-decodes, verifies the signature **before** parsing the payload
(no oracle), then `_check_payload` (L179) re-compares every decoded binding field against the
authorized request context — the actual authorization mechanism. `OperationIdentity` (L74) is the
value-equal (kind, operation_id, sequence) triple carried in operation/withdrawal refs;
`ref_identity` (L204) extracts it. `REF_SCHEMA_VERSION = 1` (L34) rides every payload.

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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The ref authority mirrors the L1 cursor authority's posture and binds the L0 authorization DTO; the
service owns the app-scoped secret this module signs with.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The `AuthorizationBinding` (principal/tenant) re-bound in every payload check. | L1-L40 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| The app-scoped control secret this module signs/verifies with. | L179-L183 | [service.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/service.py) |
| The L1 cursor authority whose signed-purpose-branded posture this mirrors. | L1-L272 | [active/cursor.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/cursor.py) |
| Consumers: the queue projection mints operation/withdrawal refs; withdrawals/attachments decode and re-bind them. | L74-L144 | [queue_projection.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/queue_projection.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the opaque signed
  control-reference authority — four non-interchangeable purpose brands, sign-before-parse decode,
  per-wire binding re-check, and the typed `ControlRefError` family. Verification is blank because
  the new source file is uncommitted; closeout owns its first source stamp.
