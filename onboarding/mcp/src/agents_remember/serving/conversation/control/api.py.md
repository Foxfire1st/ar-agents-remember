# mcp/src/agents_remember/serving/conversation/control/api.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/api.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `0be0099744bf1287805acf0b95072127b70f7104`|
| lastVerifiedCommitDate |  2026-07-20T15:34:11+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structured conversation control overview](overview.md)

## Purpose

The authoritative human control surface for structured Chats: the seventeen registered production
routes on the `/api/terminal/{ar_session_id}` prefix covering exact-turn interrupt, the source-aware
operation queue with cockpit-only withdrawal and bounded recovery, typed attachment stage/rebind/
submit, read-only effective policy, and evidence-bound telemetry. Every wire resolves the caller
through the L0 authorization dependency, compares `expectedBridgeEpoch` against the live submission
authority, and maps every typed refusal to the serving status idiom — raw 500s are never a routine
refusal path (L0 reviewer obligation O4).

## Code Commentary

### Logic

The `router` (L57) mounts at `/api/terminal/{ar_session_id}` with the structured-control tag. The
seventeen routes: interrupt (L129), interrupt-status (L156), interrupt-reconcile (L184) [R1];
`GET /operation-queue` (L212), withdraw (L234), withdraw-status (L262), withdraw-reconcile (L288),
`GET .../pending-withdrawal-recoveries` (L314), withdraw-recovery (L336), withdraw-recovery-ack
(L360) [R2/R3]; attachments (L385), attachments/rebind (L429), `GET .../attachments/{request_id}/
status` (L459), attachments/{request_id}/reconcile (L484), submit (L509) [R4]; `GET .../conversation/
policy` (L548) [R5]; `GET .../conversation/telemetry` (L570) [R6]. Each handler invokes the two L0
dependencies (`get_conversation_runtime`, `resolve_conversation_authorization`), gets the per-app
service via `conversation_control_service`, and delegates to the owning module (operations,
withdrawals, attachments, policy, telemetry, queue_projection). `_map_typed_error` (L105) maps the
`_TYPED_ERRORS` tuple (L61 — AuthorityError, ConversationCompositionError,
HarnessBridgeEpochMismatchError, HarnessControlError, ControlRefError, ControlOperationError,
SessionResolutionError) to the serving status idiom via `_error` (L98); `_dump` (L125) serializes
wire models. Multipart staging parses through `_parse_uploads` (L592), `_parse_metadata_array`
(L608), and `_upload_for` (L626) with the `MAX_SUBMIT_ASSET_BYTES` bounded read. The request bodies
`InterruptBody`/`WithdrawStatusBody`/`RecoveryFetchBody`/`RecoveryAckBody`/`RebindBody` (L74-L93) are
strict wire models.

### Conventions

This module composes the existing native submission/control authority; it invents no second queue,
operation ledger, or process identity. It is the HTTP boundary only — all state and policy live in
the owning control modules. Exact AR session and bridge epoch remain mandatory authority on every
wire.

### Invariants And Boundaries

- O4 per-route typed-error mapping on all seventeen routes: no raw 500 on any routine refusal
  (subclass-before-base mapping).
- Policy/telemetry/queue/pending are GET-only; the mutating routes are POST; no mutation surface
  exists on policy (405 on PATCH/PUT/DELETE).
- Every wire verifies `expectedBridgeEpoch` against the LIVE authority; the L0 dependencies are the
  only caller/runtime resolution seam.
- Authoritative pop-back is queue withdrawal recovery, not client-side draft reconstruction; the
  control routes are not a third conversation read port.

### Todos

None. (The route shell was filled by 260718-CHATS-L3; the seventeen routes are pinned by the
foundation suite.)

## Docs References

No Domain Documentation source is configured for this internal route boundary.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

Each route delegates to an owning control module; the wire products are the SC1 contract; the
foundation suite pins the exact seventeen routes.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The owning modules each route delegates to (operations/queue/withdrawals/attachments/policy/telemetry). | L87-L570 | [operations.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/operations.py) |
| Operation, queue, withdrawal, recovery, attachment, policy, and telemetry wire products. | L786-L1250 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| The two L0 request dependencies every handler consumes. | L21-L36 | [dependencies.py](agents-remember/mcp/src/agents_remember/serving/conversation/dependencies.py) |
| The foundation regression pins the exact seventeen owned routes (GET-only on policy/telemetry/queue/pending). | L54-L82 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local route surface.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: replaced the behavior-empty route-shell
  description with the filled reality — the seventeen registered production routes, per-handler L0
  dependency + live-epoch verification, O4 typed-error mapping across the `_TYPED_ERRORS` tuple, and
  multipart attachment staging — and repointed the governing overview to the new `control/overview.md`
  pillar. Verification stays pinned at the L3E base until L3 closeout stamps the candidate commit.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the structured-control route-shell
  sidecar. Verification is blank until closeout commits and stamps the new source.
