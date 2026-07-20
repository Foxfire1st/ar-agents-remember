# Structured Conversation Control Route Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| doc_type | `route-local-overview` |
| sourceRoute | `mcp/src/agents_remember/serving/conversation/control/` |
| onboardingRoute | `mcp/src/agents_remember/serving/conversation/control/overview.md` |
| parentOverview | [`conversation/overview.md`](../overview.md) |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `0be0099744bf1287805acf0b95072127b70f7104`|
| lastVerifiedCommitDate |  2026-07-20T15:34:11+02:00|

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
| `capabilities.py` | Control-domain exact-session capability gate with observed-runtime demotion. |
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
5. Capability gating is fixture/evidence-bound and demotes on observed runtime/helper mismatch; a
   refused capability fails typed (422) before any native call.

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
| `capabilities.py` | capability gate | Features enable only from fixture evidence; a version mismatch demotes and the action stays off. | covered |

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
| The operation/queue/withdrawal/recovery/attachment/policy/telemetry wire products and privacy validators. | L786-L1250 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| The L2E control-plane reads (interrupt write, operation timeline, asset channel) this slice consumes. | L270-L360 | [harness_control_client.py](agents-remember/mcp/src/agents_remember/serving/harness_control_client.py) |
| The L3E truncation-envelope terminal-identity preservation the pi settlement reads. | L569-L667 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |
| The authority setter mint with no submission source (setter-row exclusion basis). | L541-L543 | [harness_submission_authority.py](agents-remember/mcp/src/agents_remember/serving/harness_submission_authority.py) |
| The stale-but-fail-closed L1 page-level control/telemetry capability view (L4 gates on the L3 module instead). | L152-L165 | [active/capabilities.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/capabilities.py) |
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

- Claude's control/telemetry surface stays `unverified` on this machine (installed 2.1.214 ≠ locked
  2.1.211) until a real installed 2.1.211 session crosses the production seam; the wire carries the
  exact reason.
- Only codex cumulative token usage is a landed supported metric; cost/context/rateLimits/compaction
  for codex and every claude/pi metric stay visibly unverified/unavailable until installed-runtime
  fixtures observe them through the production seam.

## Update History

- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the governing overview for the
  implemented authoritative control slice — the seventeen registered routes, the opaque signed
  reference authority, the per-app service with bounded ledgers and per-session locks, the R1–R6
  owning modules over the closed L2E/L3E substrate, and the durable L4-facing reviewer rulings
  (setter-row exclusion, empty-held preview, pi turnId, stale L1 capability gate, domain-scoped
  digests). Verification is blank because the new source route is uncommitted; closeout owns its
  first source stamp.
