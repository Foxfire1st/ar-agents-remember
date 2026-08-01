# Structured Conversation Control Route Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| doc_type | `route-local-overview` |
| sourceRoute | `mcp/src/agents_remember/serving/conversation/control/` |
| onboardingRoute | `mcp/src/agents_remember/serving/conversation/control/overview.md` |
| parentOverview | [`conversation/overview.md`](../overview.md) |
| lastUpdated | 2026-08-01T09:10+02:00 |
| lastVerifiedCommitHash |  `e52edaf5b655f495580efd93306afdf922b19b51`|
| lastVerifiedCommitDate |  2026-08-01T11:01:51+02:00|

## What This Area Is

This route is the implemented authoritative human control surface landed by 260718-CHATS-L3: the
exact-session control and operation-projection slice of structured Chats. It fills the previously
behavior-empty `control/` shell with seventeen registered production routes — exact-turn interrupt,
the source-aware operation queue with cockpit-only withdrawal and bounded recovery, typed attachment
stage/rebind/submit, read-only effective policy, and evidence-bound telemetry — consumed by the
browser cockpit without weakening the landed pop-back.

Every wire re-authorizes: the two L0 request dependencies resolve the caller and the runtime,
`expectedBridgeEpoch` is verified against the live submission authority per request, and every opaque
control reference is HMAC-signature-checked and re-bound against the authorized identity before any
lookup. The slice is disjoint from active/library: it invents no second queue, operation ledger, or
process identity, and it is not a third conversation read port. It consumes the closed L2E
control-plane substrate (the epoch-guarded native interrupt write, the paged never-bodies operation
timeline, the asset channel, and the pre-tombstone withdrawal recovery payload) read-only, and it
reads the L3E-preserved terminal-identity fields (`type`, pi `message.stopReason`, codex `turn.id`/
`turn.status`) out of the bounded evidence window for settlement.

## Hot Path Summary

Start with `api.py` for the seventeen routes and the O4 typed-error mapping. `service.py` is the
per-app authority (control secret, bounded per-(session, epoch) ledgers, per-session serialization
locks, the shared session/epoch/identity/timeline/spool seams). `refs.py` is the opaque signed
control-reference authority (four non-interchangeable purpose brands). Then the R-owning modules:
`operations.py` (R1 interrupt ledger + settlement correlation), `queue_projection.py` (R2 never-bodies
queue truth) with `previews.py` (preview/digest transforms), `withdrawals.py` (R3 cockpit-only
withdrawal + bounded recovery) with `recovery_assembly.py`, `attachments.py` (R4 typed lifecycle) with
`asset_spool.py` (the filesystem boundary), `policy.py` (R5 read-only policy), and `telemetry.py`
(R6 evidence-bound telemetry). `capabilities.py` is the control-domain gate every route consults.

## What Belongs Here

| Path | Role |
| --- | --- |
| `api.py` | The seventeen registered routes plus the O4 typed-error mapping and multipart staging. |
| `service.py` | Per-app service: control secret, bounded per-(session, epoch) ledgers, per-session locks, shared seams. |
| `refs.py` | The opaque signed control-reference authority (four purpose brands) and the typed `ControlRefError` family. |
| `capabilities.py` | Control-domain exact-session capability gate; contract-only honesty (no observed-runtime/version demotion since L5F R4). |
| `operations.py` | R1: the exact-turn interrupt ledger, idempotence, and settlement correlation. |
| `queue_projection.py` | R2: the complete never-bodies source-aware prompt-queue projection. |
| `previews.py` | The deterministic preview transform and authority-parity content digest. |
| `withdrawals.py` | R3: cockpit-only atomic withdrawal + bounded authorization-bound recovery. |
| `recovery_assembly.py` | R3: recovery content/digest/asset-ref assembly over the retention record. |
| `attachments.py` | R4: the typed attachment stage/status/reconcile/rebind/submit lifecycle. |
| `asset_spool.py` | R4: the confined staged-bytes filesystem boundary and staged asset types. |
| `policy.py` | R5: the read-only effective-policy projection. |
| `telemetry.py` | R6: evidence-bound telemetry (codex cumulative token usage). |
| `__init__.py` | Package marker. |

## What Does Not Belong Here

| Nearby Thing | Belongs Instead In |
| --- | --- |
| Strict wire grammar, cursor brands, canonical vocabulary, queue/attachment/telemetry DTOs | `mcp/src/agents_remember/serving/conversation/models.py` (the parent contract route). |
| Runtime composition, authorization ruling, request dependencies, child-router mounting | `mcp/src/agents_remember/serving/conversation/` (L0; consumed, never edited). |
| Active conversation page/stream serving | `mcp/src/agents_remember/serving/conversation/active/` (the L1 leaf). |
| Dormant native list/read/exact open | `mcp/src/agents_remember/serving/conversation/library/` (the L2 leaf). |
| The native interrupt write, operation timeline, asset channel, evidence clip, and recovery payload | `serving/harness_*` (L2E/L0E/L3E substrate; consumed read-only). |
| Browser rendering, composer state, alt-text presentation | `dashboard/src/` (the L4 renderer). |

## Structures Found Here

- Seventeen FastAPI routes on the L9 prefix `/api/terminal/{ar_session_id}` with every typed refusal
  mapped subclass-before-base to one precise HTTP status (no raw 500 for routine refusals — the O4
  idiom), and multipart attachment staging behind a bounded read.
- Four purpose-branded HMAC-SHA256-signed control references (`ar-oqr1.` operation, `ar-wdr1.`
  withdrawal, `ar-wrr1.` recovery, `ar-war1.` recovery-asset), non-interchangeable, carrying identity
  only — never content; the app-scoped random secret is never persisted, and the per-wire binding
  re-check is the real authorization mechanism.
- A per-app service holding bounded per-(session, epoch) ledgers (64 interrupts / 64 withdrawals /
  32 recoveries / 32 attachment-ops / 256 journal / 256 submits per channel; 64 channels/app) with
  named eviction, per-session serialization locks above the L2E replay cache, and an injectable clock.
- An interrupt ledger with fingerprint idempotence, monotonic semantic revisions, and settlement
  correlation over the evidence/completion surface (codex `turn/completed`; pi operation-settle +
  `stopReason` read from the L3E-preserved evidence identity).
- A never-bodies queue projection (validator-enforced) exposing withdrawal refs/previews/digests only
  on queued cockpit rows; a bounded 900 s authorization-bound recovery lease with opaque discovery,
  authenticated fetch, ack-disposal, and expiry; a typed attachment lifecycle with one-use assets in
  a confined 0700/0600 spool; a read-only policy projection with no mutation surface; and
  evidence-bound telemetry with absent-not-zero missing data.

## Operating Model

1. Each handler invokes the two L0 dependencies, gets the per-app control service, and verifies the
   expected bridge epoch against the live submission authority before any state work.
2. Mutating routes serialize on the service's per-session lock (above the L2E replay cache) and admit
   under a request fingerprint; identical replays return the stored answer with no second native
   write, and a reused id with a different tuple is `request-conflict`.
3. The R-owning module consumes the L2E substrate reads (interrupt write, operation timeline, asset
   channel, recovery payload) — never reimplementing them — and records the semantic-revisioned
   result in its bounded ledger.
4. Every opaque reference is re-bound against the authorized identity on the wire; possession is never
   authorization, and the source rule is the backstop behind the signature.
5. Capability gating is fixture/evidence-bound and, since L5F R4, demotes only on a failed or
   never-run contract verification — never on an observed runtime/helper version comparison (the
   observed version is informational evidence only); a refused capability fails typed (422) before
   any native call.

## Main Flows

### Exact-turn interrupt (R1)

1. Authorization + epoch verification; capability gate refuses claude/unsupported before any native
   call.
2. The native write's answer is the acknowledgement (`accepted`/`unknown`/`rejected`); settlement
   lands only when the exact turn's terminal evidence crosses (`interrupted`/`already-settled`/
   `failed`). A lost ack records `unknown` and reconciles through the same id with one native write.

### Source-aware queue truth and cockpit-only withdrawal recovery (R2/R3)

1. The projection pages the L2E timeline to union completeness and projects every retained prompt row
   with never-bodies truth; only queued cockpit rows carry a withdrawal ref/preview/digest.
2. A successful withdrawal retains the exact body in a bounded, authorization-bound, 900 s recovery
   lease; fresh tabs discover opaque pending-recovery identities and fetch exact text/assets only
   while authenticated and unacknowledged; ack disposes the body; expiry deletes text and bytes.

### Typed attachments (R4)

1. Stage binds each asset to caller/session/epoch/request/kind with fixture-backed limits into the
   confined spool; submit consumes one-use assets through the L2E asset channel; a tampered block
   refuses pre-dispatch.
2. Withdrawal marks assets recoverable under the same lease; rebind atomically exchanges one
   authorized recovery asset for a fresh one-use staged asset; unknown is retained, never re-uploaded.

## Load-Bearing Files

| File | Role | Why It Matters | Onboarding |
| --- | --- | --- | --- |
| `api.py` | route/mapping authority | Keeps every typed refusal on its precise HTTP status; a raw 500 here violates the O4 contract. | covered |
| `service.py` | serving authority | The one boundary for the control secret, bounded ledgers, per-session locks, and the shared seams. | covered |
| `refs.py` | reference authority | Every opaque token's mint/verify boundary; cross-purpose/cross-session/tamper fails closed before any lookup. | covered |
| `operations.py` | interrupt authority | Ack≠settlement and the settlement correlation that must read the L3E-preserved identity, not the clipped body. | covered |
| `withdrawals.py` | withdrawal authority | Preserves the landed cockpit-only atomicity and bounds recovery to an expiring, authenticated lease. | covered |
| `attachments.py` | attachment authority | One-use exact-receipt assets, timeline-driven lifecycle, and recoverable-under-lease rebind. | covered |
| `queue_projection.py` | queue authority | Never-bodies truth; withdrawability is validator-enforced, never fabricated. | covered |
| `capabilities.py` | capability gate | Features enable only from fixture evidence; an un-probed contract stays `unverified` and the action stays off (contract-only gate, no version demotion since L5F R4). | covered |

## Local Invariants And Traps

- Possession of a control reference is never authorization: every wire re-resolves the caller and
  re-binds every decoded ref field; the signature is verified before the payload is parsed.
- Acknowledgement is never settlement (R1). An `accepted` interrupt settles only on the exact turn's
  terminal evidence; the settlement correlation must read the L3E-preserved `type`/`message.stopReason`
  from the evidence envelope (the transcript-read seam is defeated by the 64 KiB IPC cap — proven in
  L3's fix-round-2 escalation).
- Never-bodies queue projection is validator-enforced: terminal/durable prompt bodies cannot cross,
  and only queued cockpit rows are withdrawable.
- **Setter rows are excluded from the queue projection (reviewer ACCEPTED).** Set-model/set-effort
  operations are authority-minted with `source=None` and cannot be withdrawn; the SC1
  `OperationQueueItem` validator cannot represent them without inventing a source or lying about
  withdrawability, so the projection covers the complete **prompt** queue and setters stay in the
  contract grammar for a future SC1 admission (the recorded fallback).
- **Empty-held preview semantics (reviewer ACCEPTED).** A cockpit row the submit journal does not hold
  reports `redactedPreview: ""` and the digest-of-empty marker — the truthful "the daemon holds no
  content", distinct from an empty draft, never fabricated; recovery at withdraw still carries the
  body from the substrate payload.
- Recovery is a bounded lease, not durable storage: acknowledgement disposes raw content, expiry
  deletes text and bytes, and daemon restart invalidates every reference loudly (the app-scoped-secret
  posture).
- Staged assets are one-use, exact-receipt-matched, and confined (0700/0600, resolve-and-verify);
  `unknown` is retained, never re-uploaded under a new id.
- No PTY Esc / paste / native-queue substitution exists anywhere in the control modules (source-
  scanned); policy is GET-only with no mutation surface.
- 260718-CHATS-L5F R5 bounds the per-session control structures: `service._locks` is a bounded
  `OrderedDict` (`MAX_SESSION_LOCKS_PER_APP=128`, evicting the oldest UNLOCKED lock so a held lock is
  never dropped) with an explicit `release_session` (drops the lock + every epoch channel on session
  end), and `queue_projection.queue_rows` is capped at `MAX_QUEUE_ROWS_PER_CHANNEL=256` with oldest-key
  eviction (closing the old unbounded-`queue_rows` L3 Todo; eviction only ever touches settled
  operations, invisible to live rows). Honest posture (reviewer F1 accepted-bounding): the sync
  `release_session` is unit-tested but NOT wired into the terminate/retire endpoints this leaf — the
  monotonic `_locks` leak is closed by bounding, not by an explicit session-end hook; the wiring locus
  (expose the ConversationRuntime and call `release_session` after `catalog.mark_terminated`) is
  recorded in the `service.py` sidecar.
- Since 260718-CHATS-L5F R4 (developer ruling 2026-07-21) THE CONTRACT IS THE ONLY GATE: no
  version-string comparison demotes any control/telemetry capability; the observed runtime/helper
  version is informational evidence only.

## L4-Facing Register (durable reviewer rulings the renderer must carry)

- **Pi `turnId` names the exact AR operation id, not a native turn id (ruling 3).** Pi has no native
  turn identity (L2E deviation 6), so for pi the caller supplies the active AR operation id (from the
  dispatching queue row or item correlation), which the substrate guards pre-write; for codex `turnId`
  names the native turn id.
- **Control affordances must gate on the L3 routes' own capability evidence, not the stale L1 page
  view (ruling 6).** `active/capabilities.py` still reports controls/telemetry as `unverified` ("the
  L3 control leaf owns the gate") — true from L1's pre-L2E evidence but stale now; it is fail-closed
  (disables, never enables). L4 must gate on the L3 routes' `control/capabilities.py` evidence, or a
  later leaf refreshes the L1 view. Hiding a landed feature on the stale view is the failure to avoid.
- **Identity digests are domain-scoped (precision note 4).** L1/L2/L3 services each hold their own app
  secret, so L4 must match conversations by identity fields, never by digest equality across services.

## Repo-Internal References

The parent contract route supplies the wire grammar and composition seams; the L2E/L0E/L3E substrate
supplies the native writes, timeline, asset channel, evidence window, and recovery payload; the
foundation and four+installed suites pin the slice.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The two L0 request dependencies are the only caller/runtime consumption seam the handlers use. | L21-L36 | [dependencies.py](agents-remember/mcp/src/agents_remember/serving/conversation/dependencies.py) |
| The operation/queue/withdrawal/recovery/attachment/telemetry wire products this route imports, the `protect_queue_source_privacy` validator, and the content-free `operation_fingerprint`. Policy products (`PolicyPart`, `ConversationPolicyProjection`) are route-local in `control/policy.py`, not here. | L935-L1262; L1285-L1302 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| The seventeen route declarations: one shared refusal table plus the two outcome tables, and the submit route's own 202/422 entries. `_map_typed_error` is the single mapper that makes one table the complete refusal surface. | L124-L150; L151-L789 | [control/api.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/api.py) |
| `CONTROL_RESPONSES` (six statuses), `INTERRUPT_OUTCOME_RESPONSES` and `WITHDRAW_OUTCOME_RESPONSES` — the outcome tables whose bodies are the operation, not a refusal — plus `StagedAttachments`/`ConversationSubmitted`/`WithdrawQueueAnswer`. | L57-L90; L95-L112; L140-L177 | [conversation/response_contract.py](agents-remember/mcp/src/agents_remember/serving/conversation/response_contract.py) |
| The L2E control-plane reads (interrupt write, operation timeline, asset channel) this slice consumes. | L270-L360 | [harness_control_client.py](agents-remember/mcp/src/agents_remember/serving/harness_control_client.py) |
| The L3E truncation-envelope terminal-identity preservation the pi settlement reads. | L569-L667 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |
| The authority setter mint with no submission source (setter-row exclusion basis). | L541-L543 | [harness_submission_authority.py](agents-remember/mcp/src/agents_remember/serving/harness_submission_authority.py) |
| The stale-but-fail-closed L1 page-level control/telemetry capability view (L4 gates on the L3 module instead). | L154-L167 | [active/capabilities.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/capabilities.py) |
| The foundation pin asserts exactly the seventeen owned control routes (GET-only on policy/telemetry/queue/pending). | L54-L82 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |
| The four focused suites + the opt-in installed suite cover interrupt, queue/withdrawal/recovery, attachments/policy/telemetry, the real-wire routes, and the live proof. | L1-L8 | [mcp/tests overview](../../../../../tests/overview.md) |

## Cross-Repo References

No cross-repository implementation participates in this route. All three harnesses are local
subprocesses reached through this repository's own adapters, and the resolved memory policy allows no
neighboring repository.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant cross-repo evidence found. | — | — |

## Docs References

The resolved `Domain Documentation` registry has no entries. This route therefore uses the
repository-owned contract, the L2E/L0E/L3E substrate, fixtures, and tests as its direct evidence and
does not fabricate an external citation.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available for this control gate. | — | — |

## File-Level Onboarding Map

| Source File | Onboarding File | Status | Reason |
| --- | --- | --- | --- |
| `__init__.py` | [`__init__.py.md`](__init__.py.md) | covered | Control route package marker. |
| `api.py` | [`api.py.md`](api.py.md) | covered | The seventeen registered routes and the O4 mapping. |
| `service.py` | [`service.py.md`](service.py.md) | covered | Per-app control service authority. |
| `refs.py` | [`refs.py.md`](refs.py.md) | covered | Opaque signed control-reference authority. |
| `capabilities.py` | [`capabilities.py.md`](capabilities.py.md) | covered | Control-domain capability gate. |
| `operations.py` | [`operations.py.md`](operations.py.md) | covered | Exact-turn interrupt ledger (R1). |
| `queue_projection.py` | [`queue_projection.py.md`](queue_projection.py.md) | covered | Source-aware queue projection (R2). |
| `previews.py` | [`previews.py.md`](previews.py.md) | covered | Preview/digest transforms. |
| `withdrawals.py` | [`withdrawals.py.md`](withdrawals.py.md) | covered | Cockpit-only withdrawal + bounded recovery (R3). |
| `recovery_assembly.py` | [`recovery_assembly.py.md`](recovery_assembly.py.md) | covered | Recovery content/digest/ref assembly (R3). |
| `attachments.py` | [`attachments.py.md`](attachments.py.md) | covered | Typed attachment lifecycle (R4). |
| `asset_spool.py` | [`asset_spool.py.md`](asset_spool.py.md) | covered | Confined staged-bytes filesystem boundary (R4). |
| `policy.py` | [`policy.py.md`](policy.py.md) | covered | Read-only effective-policy projection (R5). |
| `telemetry.py` | [`telemetry.py.md`](telemetry.py.md) | covered | Evidence-bound telemetry (R6). |

## Child Overviews

None. The fourteen modules form one coherent control slice; there are no child routes.

## How To Use This Area

Read this overview and the exact file sidecar first. Route/error-mapping changes require the
production-route suite over a real socket and the foundation route pin; interrupt-settlement changes
require the operations suite (including the pi content-ful and oversized/clipped regressions); queue/
withdrawal/recovery changes require the queue suite; attachment changes require the attachments suite
plus on-disk spool proofs. Never mint a control reference that carries content, never fabricate a
preview/digest for content the daemon does not hold, and never infer capability from fixture
existence. The interrupt settlement must read the L3E-preserved evidence identity, not the clipped
body.

## Needs Verification

- Claude's control/telemetry surface stays `unverified` with a NEVER-PROBED contract reason
  ("control contract not yet probed through a captured production fixture … never a version gate"),
  no longer a version-mismatch reason (L5F R4 removed the version gate); the wire carries the exact
  contract reason.
- Only codex cumulative token usage is a landed supported metric; cost/context/rateLimits/compaction
  for codex and every claude/pi metric stay visibly unverified/unavailable until installed-runtime
  fixtures observe them through the production seam.

## 260718-CHATS-L5I Current Route Impact

The control child now carries normalized question pages and an exact answers map through both gate-mediated and lifecycle-free response paths. Native Claude interrupt joins the existing exact-turn control ledger with an explicit acknowledgement/settlement split; a failed adapter decision reopens with visible failure evidence rather than masquerading as approval.

Route indexes are intentionally not regenerated during this partitioned curator pass; the manager will run the single aggregate refresh after all curator ownership is complete. Existing verification metadata remains pre-commit.

## 260731-EFA-L2 — The Re-Authorization Rule Became A Type

Everything asserted above about re-authorization still holds, and the route's boundaries are
unchanged. What changed is that the rule is now carried by the type system instead of by four
arguments repeated at every layer, and **the two most dangerous confusions in this route are now
hard to express.**

**`ControlRequest` → `ControlScope` (`service.py`).** `ControlRequest` is one authorized request's
scope: `service`, `authorization`, `ar_session_id`, `expected_bridge_epoch`. Nothing in this package
may act on a session without all four — the service owns the per-`(session, epoch)` channel, the
authorization binding is what every operation fingerprint is computed against, and the session id
plus the caller's *expected* epoch are what the epoch check verifies. `request.resolved(epoch)`
narrows it to a `ControlScope` carrying **the epoch the service actually verified, not the one the
caller believed.** Refs are minted and decoded against the verified epoch, so carrying the claimed
epoch past the check would let a stale client mint refs for an epoch that no longer exists. The
entry points take `ControlRequest`; everything downstream of the epoch check takes `ControlScope`.
Do not add a function that takes a raw `expected_bridge_epoch` past that boundary.

**`RefBinding` / `RefTarget` (`refs.py`).** A ref is only meaningful re-bound to all three of
caller, session and exact bridge epoch — `RefBinding(authorization, ar_session_id, bridge_epoch)` —
and `RefTarget(identity, withdraw_request_id=, asset_id=)` is what it points at. `mint_ref` and the
decode path take **the same binding value**, rather than three parallel arguments each. Minting
against one binding and verifying against another is exactly the confused-deputy the purpose brands
exist to stop; passing one value makes the two sides provably identical. The four non-interchangeable
purpose brands are unchanged.

**One attempt, one record.** `WithdrawalTicket` (`withdrawals.py`) carries the five facts every
record this module builds — settled, failed or unknown — is stamped with: the bound epoch, the
operation identity, the caller's opaque operation ref, the idempotency fingerprint, and the withdraw
request id. Its reason for existing is precise: it keeps a *failure* record from being stamped with
a different operation's identity than the attempt it describes. `InterruptTicket` (`operations.py`)
and `SubmittedContent` (`attachments.py`) play the same role for their operations, and
`StageAttachmentsForm` (`api.py`) carries one multipart stage form.

No route was added or removed; the seventeen routes, the typed-error mapping, the bounded ledgers,
the never-bodies queue rule and the cockpit-only withdrawal restriction are all as described above.

## 260731-EFA-L4 — Seventeen Declarations, And The Distinction Between An Outcome And A Refusal

No route was added or removed; the ref authority, bounded ledgers, never-bodies queue rule,
cockpit-only withdrawal restriction and capability gate are all unchanged. All seventeen routes now
declare a `response_model` and a `responses` table.

**One shared refusal table covers all seventeen, and that is a claim about the code, not a
convenience.** `_map_typed_error` is the single place a typed error becomes a status here, and it
maps the whole family onto exactly six: 400 (a malformed operation/recovery/asset ref), 403
(authorization), 404 (unknown session or operation), 409 (stale epoch or a typed conflict), 422
(rejected as posed), 503 (composition or bridge unavailable). `CONTROL_RESPONSES` is that mapper
transcribed. If a later leaf adds a seventh status to `_map_typed_error` and not to the table, the
declaration becomes a lie that nothing about the mapper itself will catch.

**Where this route is unusual: three of its statuses are not refusals at all.** The interrupt trio,
the withdrawal route and submit each choose their status from the operation they built, and the body
on those statuses is the operation:

| Route(s) | Status chosen by | Statuses carrying a NON-refusal body |
| --- | --- | --- |
| `interrupt` / `interrupt-status` / `interrupt-reconcile` | `operations.interrupt_http_status`, off the operation's own `acknowledgement`/`settlement` | 202, 422, 503 carry `InterruptOperation` |
| `operation-queue/withdraw` | `withdrawals.withdraw_http_status`, off which answer it built | 202, 404, 409 carry `WithdrawQueueAnswer` (withdrawn **or** failed) |
| `conversation/submit` | `acceptance` (`unknown` → 202, `rejected`/`unsupported` → 422) | 200, 202, 422 all carry the SAME `ConversationSubmitted` body |

An acknowledged-but-unsettled interrupt on 202 and a failed withdrawal on 409 are this route's own
answers, not error envelopes. Declaring them through the shared refusal table alone would have been
wrong, **and the conformance suite caught exactly that on a real 422 from the interrupt route.**

**The merge trap.** These outcome tables are spread as `{**CONTROL_RESPONSES, **OUTCOME}`, and
`{**a, **b}` is a dict merge — a bare `{422: InterruptOperation}` would DELETE the shared refusal
entry rather than join it, declaring a model the route cannot produce on a status it genuinely
answers with a refusal (`_map_typed_error` reaches 422 through `CapabilityRefusedError` and
`OperationRejectedError`). Every overlapping entry therefore unions both members. The same shape is
required of any future outcome table here.

Three bodies on this surface are assembled at the route and had no model at all before this leaf:
`StagedAttachments` (stage and rebind) and `ConversationSubmitted` (submit). They are declared in
`conversation/response_contract.py`, which is split from the app-level contract module for an
import-cycle reason (see `../overview.md`).

**What is and is not enforced.** Every handler here returns a `JSONResponse` it built itself, so
FastAPI validates none of these declarations at runtime — undoing them would fail no request.
`mcp/tests/test_serving_response_conformance.py` is the enforcement: it drives the real routes and
validates the returned body against the model declared for the status that came back. Its ledger is
honest about the reach: the 404 (no such seat) is driven on all seventeen, the 403 on one, and every
reachable success shape off a live bridge — while the typed-bridge-failure legs (400/409/422/503 on
most routes) stay declared-and-undriven with a reason, because the bridge fixture models the harness
edge rather than a stale epoch or a socket that dies mid-write.

## Update History

- 2026-08-01T09:10+02:00 — 260731-EFA-L4 curator: recorded the seventeen route declarations and,
  more importantly, the distinction the declarations had to encode — three of this route's statuses
  carry the operation itself and not a refusal (202/422/503 on the interrupt trio, 202/404/409 on
  withdraw, 200/202/422 all on submit), so the shared refusal table alone was a wrong declaration
  and the conformance suite caught it on a real 422. Recorded that `_map_typed_error` being the
  single mapper is what makes one six-status table the COMPLETE refusal surface of all seventeen,
  and the `{**a, **b}`-is-a-merge trap every outcome table works around. Stated the enforcement
  boundary: every handler returns a `JSONResponse` it built, so FastAPI validates nothing here and
  the declarations mean only what `test_serving_response_conformance.py` drives. Repaired 2 line
  citations in the `models.py` row, both moved +20 by the parent's field-default edits: L915-L1242 →
  L935-L1262 (`InterruptOperation` → `ConversationTelemetry`) and L1265-L1282 → L1285-L1302
  (`operation_fingerprint`). Added 2 reference rows (`control/api.py` declarations,
  `conversation/response_contract.py` tables); all ranges read back. Verification metadata pinned
  until closeout stamps the L4 commit.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired the `models.py` citation and narrowed
  the claim, which was partly false. The span is now L915-L1242 (`InterruptOperation` through
  `ConversationTelemetry`) plus L1265-L1282 (`operation_fingerprint`) — verified against what the
  route's own modules import: `operations.py` takes `InterruptOperation`/`OperationFingerprint`,
  `queue_projection.py` takes the three queue models (the privacy validator is
  `OperationQueueItem.protect_queue_source_privacy` at L961-L968), `withdrawals.py` +
  `recovery_assembly.py` take the withdrawal/recovery set, `attachments.py` the submit/receipt
  set, `telemetry.py` the metric set. **Dropped "policy" from the claim**: `models.py` defines no
  policy wire product — `PolicyPart` and `ConversationPolicyProjection` are declared in
  `control/policy.py` and only borrow `FeatureCapability`/`CapabilityEvidence` from `models.py`.
  The old start at L786 also over-reached into `ConversationLibraryPageScope`, which this route
  does not touch.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2: the re-authorization contract became structural —
  `ControlRequest` carries the four facts no operation may proceed without, `ControlScope` carries
  the **verified** epoch past the check, and `RefBinding`/`RefTarget` make mint and decode share one
  binding value. `WithdrawalTicket`/`InterruptTicket`/`SubmittedContent`/`StageAttachmentsForm` bind
  one attempt's facts together. No route, error mapping or authorization rule changed. Verification
  metadata pinned until closeout stamps the L2 commit.
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: updated the route body for the current backend/shared behavior; aggregate route-index generation remains manager-owned.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: recorded the half-time functional truths for
  the control route. R4 version-gate REMOVAL (developer ruling 2026-07-21) — corrected the now-false
  "version mismatch demotes" capability-gate language to the contract-only gate; claude control/
  telemetry is `unverified` for a never-probed contract reason, not an installed-vs-locked version
  reason. R5 — `_locks` is a bounded `OrderedDict` (128, idle-first eviction, held lock never
  dropped) with `release_session`, and `queue_rows` is capped (256, oldest-evicted), closing the old
  unbounded-`queue_rows` Todo; `release_session` is unwired from terminate/retire (F1
  accepted-bounding, wiring locus recorded). Routes, ref authority, and ledger contract unchanged.
  Verification stays pinned until L5F closeout stamps the candidate commit.
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the governing overview for the
  implemented authoritative control slice — the seventeen registered routes, the opaque signed
  reference authority, the per-app service with bounded ledgers and per-session locks, the R1–R6
  owning modules over the closed L2E/L3E substrate, and the durable L4-facing reviewer rulings
  (setter-row exclusion, empty-held preview, pi turnId, stale L1 capability gate, domain-scoped
  digests). Verification is blank because the new source route is uncommitted; closeout owns its
  first source stamp.
