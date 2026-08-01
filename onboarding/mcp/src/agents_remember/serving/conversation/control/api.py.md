# mcp/src/agents_remember/serving/conversation/control/api.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/api.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-01T09:28+02:00 |
| lastVerifiedCommitHash |  `e52edaf5b655f495580efd93306afdf922b19b51`|
| lastVerifiedCommitDate |  2026-08-01T11:01:51+02:00|
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

### 260731-EFA-L4 Current Delta — All Seventeen Routes Declare Their Contract

Every route now names a `response_model`, and — because `_map_typed_error` is the one mapper for
this whole surface — **one shared `CONTROL_RESPONSES` table is the complete refusal surface of
all seventeen**: 400, 403, 404, 409 (`BridgeEpochMismatchRefusal | StatusRefusal`), 422 and 503.
Declaring only the success model would have been a half-declaration.

Most routes declare the model `_dump` already serialized (`InterruptOperation`,
`OperationQueueProjection`, `WithdrawalOperationProjection`, `PendingWithdrawalRecoveryList`,
`WithdrawalRecovery`, `AttachmentOperationProjection`, `ConversationPolicyProjection`,
`ConversationTelemetry`). Four routes needed more:

- **`/conversation/attachments` and `/attachments/rebind`** (L482, L531) declare
  `StagedAttachments` — a model that did not exist, because that body (`operation` + `receipts`)
  is assembled at the route.
- **`/operation-queue/withdraw`** (L280) declares `WithdrawQueueAnswer`
  (`WithdrawnQueueResponse | FailedWithdrawalResponse`) plus `WITHDRAW_OUTCOME_RESPONSES`:
  `withdraw_http_status` reads which of the two was built to pick the status, so a **failed
  withdrawal is still this route's own answer** on 202/404/409, not an error body.
- **The three interrupt routes** (L151, L184, L218) add `INTERRUPT_OUTCOME_RESPONSES` for the
  same reason: `interrupt_http_status` picks 200/202/422/503 off the operation's OWN
  `acknowledgement`/`settlement`, so those statuses carry an `InterruptOperation`. Declaring
  them as refusals — which the shared table alone would have done — was wrong, and the
  conformance suite caught it on the real 422.
- **`/conversation/submit`** (L635) declares `ConversationSubmitted` for **one body shape across
  three statuses**: `acceptance` picks 200, 202 (`unknown`) or 422 (`rejected`/`unsupported`).
  Its 422 entry must UNION `CONTROL_RESPONSES[422]`, because `responses={**a, **b}` is a dict
  merge — a bare `{422: ConversationSubmitted}` would have DELETED the shared refusal rather
  than joining it, and `_map_typed_error` reaches this route's 422 too
  (`CapabilityRefusedError` and `OperationRejectedError` both carry `http_status = 422`).

Nothing validates at runtime: every handler returns a `JSONResponse`, so FastAPI never reaches
`serialize_response`. `mcp/tests/test_serving_response_conformance.py` drives each route and
validates the real body — and it validates in **alias form only** (`by_name=False`), which is
what pins these bodies to camelCase rather than merely to the right field set.

This entry supersedes any earlier description in this sidecar that conflicts with the current
source behavior above; verification metadata stays pinned to the pre-commit source history until
closeout.

### Logic

The `router` (L75-L78) mounts at `/api/terminal/{ar_session_id}` with the structured-control tag. The
seventeen routes: interrupt (L151), interrupt-status (L184), interrupt-reconcile (L218) [R1];
`GET /operation-queue` (L252), withdraw (L280), withdraw-status (L314), withdraw-reconcile (L346),
`GET .../pending-withdrawal-recoveries` (L378), withdraw-recovery (L406), withdraw-recovery-ack
(L436) [R2/R3]; attachments (L482), attachments/rebind (L531), `GET .../attachments/{request_id}/
status` (L567), attachments/{request_id}/reconcile (L598), submit (L635) [R4]; `GET .../conversation/
policy` (L685) [R5]; `GET .../conversation/telemetry` (L711) [R6]. Each handler invokes the two L0
dependencies (`get_conversation_runtime`, `resolve_conversation_authorization`), gets the per-app
service via `conversation_control_service`, and delegates to the owning module (operations,
withdrawals, attachments, policy, telemetry, queue_projection). `_map_typed_error` (L124) maps the
`_TYPED_ERRORS` tuple (L80-L88 — AuthorityError, ConversationCompositionError,
HarnessBridgeEpochMismatchError, HarnessControlError, ControlRefError, ControlOperationError,
SessionResolutionError) to the serving status idiom via `_error` (L117); `_dump` (L144) serializes
wire models with `exclude_none=True`. Multipart staging parses through `_parse_uploads` (L737-L748),
`_parse_metadata_array` (L751), and `_upload_for` (L765-L786) with the `MAX_SUBMIT_ASSET_BYTES`
bounded read. The request bodies
`InterruptBody`/`WithdrawStatusBody`/`RecoveryFetchBody`/`RecoveryAckBody`/`RebindBody` (L93-L114) are
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
- **`CONTROL_RESPONSES` is only as complete as `_map_typed_error`.** A status added to that
  mapper without being added to the table leaves seventeen routes emitting an undeclared shape.
- **Outcome statuses are success shapes, and spreading tables must union.** An acknowledged-but-
  unsettled interrupt, a not-withdrawable withdrawal, and a `202`/`422` submit are answers with
  their own bodies; and since `responses={**a, **b}` overwrites rather than joins, every entry
  that overlaps a shared status has to carry the shared refusal model too.

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
| Operation, queue, withdrawal, recovery, attachment, and telemetry wire products (`OpenConversationOperation` through `ConversationTelemetry`). | L831-L1262 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| The read-only effective-policy wire models (`PolicyPart`, `ConversationPolicyProjection`) and the `conversation_policy` projector behind `GET .../conversation/policy`. | L36-L101 | [policy.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/policy.py) |
| The two L0 request dependencies every handler consumes. | L21-L36 | [dependencies.py](agents-remember/mcp/src/agents_remember/serving/conversation/dependencies.py) |
| The foundation regression pins the exact seventeen owned routes (GET-only on policy/telemetry/queue/pending). | L54-L82 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |
| The shared `CONTROL_RESPONSES` table plus the two outcome tables and the three route-assembled models these routes declare. | `CONTROL_RESPONSES`; `INTERRUPT_OUTCOME_RESPONSES`; `WITHDRAW_OUTCOME_RESPONSES`; `StagedAttachments`; `ConversationSubmitted` | [../response_contract.py](../response_contract.py.md) |
| The two 422-carrying control errors that force `/conversation/submit`'s 422 to union the shared refusal with the success model. | `CapabilityRefusedError`; `OperationRejectedError` | [service.py](service.py.md) |
| The suite that enforces the declarations, drives all seventeen routes, and validates in alias form only (`by_name=False`) so camelCase is pinned. | `validate_wire`; `test_serving_response_conformance` | [test_serving_response_conformance.py](agents-remember/mcp/tests/test_serving_response_conformance.py) |

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

- 2026-08-01T09:28+02:00 — 260731-EFA-L4 curator: recorded the seventeen `response_model`
  declarations and the shared `CONTROL_RESPONSES` table (complete because `_map_typed_error` is
  the one mapper), plus the four routes that needed more than the model `_dump` already
  serialized: `StagedAttachments` for the two route-assembled attachment bodies,
  `WithdrawQueueAnswer` + `WITHDRAW_OUTCOME_RESPONSES` on withdraw, `INTERRUPT_OUTCOME_RESPONSES`
  on the interrupt trio (where 200/202/422/503 carry an `InterruptOperation`, not a refusal —
  the conformance suite caught the wrong declaration on the real 422), and
  `ConversationSubmitted` on submit, whose 422 must union `CONTROL_RESPONSES[422]` because
  `{**a, **b}` is a dict merge and `CapabilityRefusedError`/`OperationRejectedError` both reach
  it. Added the two matching invariants. Re-derived **25** in-file citations that the added
  decorator blocks shifted — all seventeen route lines (interrupt L131→L151 through telemetry
  L612→L711), `router` L58-L61→L75-L78, `_TYPED_ERRORS` L61→L80-L88, `_error` L100→L117,
  `_map_typed_error` L107→L124, `_dump` L127→L144, `_parse_uploads` L634-L645→L737-L748,
  `_parse_metadata_array` L648→L751, `_upload_for` L662-L683→L765-L786, and the request bodies
  L76-L95→L93-L114 — plus the `models.py` control wire block L811-L1242→L831-L1262, shifted by
  the twenty comment lines that leaf added to that file. Verification metadata pinned until
  closeout stamps the L4 commit.

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
