# mcp/src/agents_remember/serving/conversation/control/api.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/api.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |  2026-07-31T19:28:50+02:00|
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

The `router` (L58-L61) mounts at `/api/terminal/{ar_session_id}` with the structured-control tag. The
seventeen routes: interrupt (L131), interrupt-status (L160), interrupt-reconcile (L190) [R1];
`GET /operation-queue` (L220), withdraw (L242), withdraw-status (L272), withdraw-reconcile (L300),
`GET .../pending-withdrawal-recoveries` (L328), withdraw-recovery (L352), withdraw-recovery-ack
(L378) [R2/R3]; attachments (L420), attachments/rebind (L465), `GET .../attachments/{request_id}/
status` (L497), attachments/{request_id}/reconcile (L524), submit (L551) [R4]; `GET .../conversation/
policy` (L590) [R5]; `GET .../conversation/telemetry` (L612) [R6]. Each handler invokes the two L0
dependencies (`get_conversation_runtime`, `resolve_conversation_authorization`), gets the per-app
service via `conversation_control_service`, and delegates to the owning module (operations,
withdrawals, attachments, policy, telemetry, queue_projection). `_map_typed_error` (L107) maps the
`_TYPED_ERRORS` tuple (L61 — AuthorityError, ConversationCompositionError,
HarnessBridgeEpochMismatchError, HarnessControlError, ControlRefError, ControlOperationError,
SessionResolutionError) to the serving status idiom via `_error` (L100); `_dump` (L127) serializes
wire models. Multipart staging parses through `_parse_uploads` (L634-L645), `_parse_metadata_array`
(L648), and `_upload_for` (L662-L683) with the `MAX_SUBMIT_ASSET_BYTES` bounded read. The request bodies
`InterruptBody`/`WithdrawStatusBody`/`RecoveryFetchBody`/`RecoveryAckBody`/`RebindBody` (L76-L95) are
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
| The three interrupt routes delegate to the operations ledger's whole public surface: `interrupt`, `interrupt_status`, and the `interrupt_http_status` mapping. | L95-L201; L552-L564 | [operations.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/operations.py) |
| Operation, queue, withdrawal, recovery, attachment, and telemetry wire products (`OpenConversationOperation` through `ConversationTelemetry`). | L811-L1242 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| The read-only effective-policy wire models (`PolicyPart`, `ConversationPolicyProjection`) and the `conversation_policy` projector behind `GET .../conversation/policy`. | L36-L101 | [policy.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/policy.py) |
| The two L0 request dependencies every handler consumes. | L21-L36 | [dependencies.py](agents-remember/mcp/src/agents_remember/serving/conversation/dependencies.py) |
| The foundation regression pins the exact seventeen owned routes (GET-only on policy/telemetry/queue/pending). | L54-L82 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local route surface.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260731-EFA-L2 Current Delta

**`StageAttachmentsForm`** replaces the loose multipart parameters of the attachment-staging route:
the request id, the metadata array and the uploaded assets are one upload — the metadata is
positionally matched against the assets, and both are only meaningful under the request id that
makes the staging idempotent. It is a `BaseModel` with `populate_by_name`, so `requestId` stays the
wire name.

Every route in this module now builds one `ControlRequest(service=conversation_control_service(
runtime), authorization=…, ar_session_id=…, expected_bridge_epoch=…)` and passes it to the control
layer, instead of repeating the same four arguments at each call. See
[service.py](service.py.md) for why the four are one scope (and why `ControlScope` — the same
request narrowed to the *verified* epoch — is a separate type). The paths, payloads and status
codes are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived 3 stale self-citations. `router` cited
  the single line L59; the `APIRouter(...)` construct with its prefix and tag is L58-L61. The two
  multipart helpers moved to the end of the module behind the route block: `_parse_uploads` L592 →
  L634-L645 and `_upload_for` L626 → L662-L683 (`_parse_metadata_array` L648 was already correct,
  as were all seventeen route line numbers).
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 2 cross-file line citations and rewrote
  both claims. The `operations.py` row cited L87-L570 against a 564-line file and claimed six owning
  modules while linking only one; `operations.py` is the interrupt ledger alone, so the claim now
  names its actual public surface — `interrupt` (L95-L156), `interrupt_status` (L159-L201) and
  `interrupt_http_status` (L552-L561) with `__all__` on L564 — cited L95-L201; L552-L564. The
  `models.py` row cited L786-L1250 and listed "policy" among the wire products, but no policy model
  lives in `models.py`; the control wire block is now L811-L1242 (`OpenConversationOperation`
  through `ConversationTelemetry`, stopping before `RuntimeFixtureObservation`) and "policy" was
  dropped from that claim. Added one row pointing the policy products at their real home,
  `control/policy.py` L36-L101 (`PolicyPart`, `ConversationPolicyProjection`,
  `conversation_policy`).
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `StageAttachmentsForm` as the one multipart staging body (wire alias `requestId` preserved).
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: replaced the behavior-empty route-shell
  description with the filled reality — the seventeen registered production routes, per-handler L0
  dependency + live-epoch verification, O4 typed-error mapping across the `_TYPED_ERRORS` tuple, and
  multipart attachment staging — and repointed the governing overview to the new `control/overview.md`
  pillar. Verification stays pinned at the L3E base until L3 closeout stamps the candidate commit.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the structured-control route-shell
  sidecar. Verification is blank until closeout commits and stamps the new source.
