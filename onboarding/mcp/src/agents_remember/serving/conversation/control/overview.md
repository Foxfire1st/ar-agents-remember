# Structured Conversation Control Route Overview

## Purpose

This package owns the exact-session human control and operation-projection surface for structured conversations. Its seventeen route declarations expose exact-turn interrupt and reconciliation, a source-aware live prompt queue, cockpit-only withdrawal and recovery, typed attachment staging/rebind/submission, read-only effective policy, and evidence-bound telemetry. The browser consumes these projections; rendering, composer state, and presentation of accessible descriptions belong to the dashboard.

Control operates over the installed ConversationRuntime and its canonical ControlPlanePort. It consumes the shared submission authority's native writes, operation timeline, asset transport, and pre-tombstone withdrawal payload rather than creating another native queue, process identity, or dispatch authority. Its local ledgers retain bounded replay answers, semantic revisions, cockpit-held content, and recovery state. Active page/stream serving and dormant library list/read/open remain neighboring responsibilities; control is not another conversation-history read port.

The enduring intent is exact identity, truthful uncertainty, source privacy, and bounded ephemeral recovery. Native acknowledgement does not prove terminal settlement; a lost response must not silently become a new operation; an unobserved metric must not become zero; a capability declaration must not become a claim of fresh runtime acceptance. The original L3 designation and later reviewer rulings describe the inherited design intent, not a new delivery receipt.

## Hot Path Summary

Start with api.py for route declarations, request assembly, typed refusals, and outcome-specific statuses. Each handler obtains the runtime and server-side authorization binding through the parent request functions. The authorization resolver uses the TCP peer rather than browser principal/tenant claims. Route operations resolve the running session and verify the expected bridge epoch against the live authority before working in that epoch's channel.

service.py owns the per-runtime service, random control secret, channel stores, session locks, injectable clock, identity construction, timeline pagination, and spool-root convention. Catalog resolution, epoch lookup, live snapshot reads, and timeline reads are offloaded through asyncio.to_thread so their blocking work does not occupy the event loop. ControlRequest groups service, caller binding, session, and claimed epoch; resolved(epoch) produces ControlScope containing the verified epoch. These values express the intended boundary, but adoption is not universal: queue, policy, telemetry, and submit entry points still accept separate arguments, and some operations unpack ControlRequest directly.

refs.py mints and verifies four purpose brands: ar-oqr1. operation, ar-wdr1. withdrawal, ar-wrr1. recovery, and ar-war1. recovery asset. RefBinding groups caller, session, and epoch; RefTarget groups operation identity and optional withdrawal/asset identity. HMAC-SHA256 integrity is checked before JSON decoding, then schema, purpose, principal, tenant, session, and epoch are compared. Tokens contain identity fields, not prompt content; signatures establish integrity, while request authorization and binding checks establish authority.

operations.py owns interrupt replay and settlement. queue_projection.py owns live prompt rows, with previews.py supplying redacted identification copy and content digests. withdrawals.py owns withdrawal/recovery lifecycle; recovery_assembly.py chooses available content and constructs recovery references. attachments.py owns staged operation lifecycle and submit assembly; asset_spool.py owns filesystem mechanics. capabilities.py declares per-harness control and telemetry evidence. policy.py and telemetry.py project read-only facts.

## Construction And Ownership

The API prefix is /api/terminal/{ar_session_id}. The seventeen routes comprise three interrupt routes; queue, withdraw, withdraw-status, withdraw-reconcile, pending recovery discovery, recovery fetch, and recovery acknowledgement; attachment stage, rebind, status, and reconcile; submit; policy; and telemetry. All declare response_model and a responses table, but handlers return constructed JSONResponse objects. Those declarations do not themselves validate the emitted response at runtime.

The shared response contracts live in serving/conversation/response_contract.py. StagedAttachments wraps an operation and receipts; ConversationSubmitted describes the same submit body across its outcome statuses; WithdrawQueueAnswer is the withdrawn/failed answer union. The conversation contract module is separate from the app-level response contract to avoid the documented router/model import cycle. Canonical wire types now live in models/conversations/, including control_wire.py, evidence.py, submissions.py, interrupts.py, attachments.py, and withdrawals.py; the canonical port lives in serving/ports.py. PolicyPart and ConversationPolicyProjection remain local to control/policy.py.

_map_typed_error handles epoch mismatch before the broader bridge error family and maps the known typed refusal families to 400 malformed reference, 403 authorization, 404 unknown identity, 409 epoch/conflict, 422 refusal as posed, or 503 composition/control unavailable. Unexpected exceptions are re-raised. The intended O4 boundary is precise mapping of routine typed refusals, not a guarantee that arbitrary failures cannot produce 500.

Outcome bodies must remain distinct from refusal envelopes. Interrupt returns its operation on 200, 202 pending, 422 rejected acknowledgement, or 503 failed settlement. Withdrawal returns its answer on 200 withdrawn, 202 delivery unknown, 404 not found, or 409 dispatch/epoch/request conflict. Submit returns ConversationSubmitted on 200, 202 unknown, or 422 rejected/unsupported. Where outcome tables overwrite shared statuses through dictionary expansion, their models union the outcome and applicable refusal models; otherwise the declaration would erase a body the handler can emit.

One service is cached per ConversationRuntime in a weak-key dictionary. It creates a random 32-byte secret and does not persist it. References therefore cease to validate when that authority is replaced. Channels are keyed by session and epoch and capped at 64 with oldest-channel eviction, refreshed on access. Declared channel limits are 64 interrupts, 64 withdrawals, 32 recoveries, 32 attachment operations, 256 journal entries, 256 submit answers, and 256 queue revision keys. These limits have different reclamation policies and do not imply unlimited replay or recovery retention. Interrupt eviction prefers nonpending records but can remove the oldest pending record under pressure; withdrawal eviction prefers records without an active recovery but can remove the oldest other record. Recovery pressure expires and removes the oldest lease rather than undoing a completed withdrawal. Attachment admission evicts accepted/failed/expired operations and refuses when the store contains only live operations. Submit/journal bookkeeping evicts oldest entries.

Session locking protects interrupt admission/reconciliation and withdrawal admission/reconciliation above the substrate replay cache. It is not applied uniformly to every mutating handler: stage, rebind, submit, and recovery acknowledgement do not acquire this service lock in their local bodies. This observation does not establish absence of lower-layer serialization or guards along their complete call paths. The lock map targets 128 entries by evicting unlocked locks; if every retained lock is held, eviction stops and a new lock can exceed that target. release_session synchronously removes a session's lock and all epoch channels. The inherited session-end wiring limit remains relevant: a bounded production-source search found its control definition but no caller, and this proposal does not certify terminate/retire integration.

The built-in native harness factory dispatches Claude, Codex, Pi and Eve through repository-owned adapters. Their production defaults launch local subprocesses: Claude stream-json, Codex app-server stdio, Pi RPC, and Eve’s local Node runtime before HTTP health checking. Injected transport/runtime factories remain possible; this describes built-in/default adapter architecture, not every configured registry entry or a newly executed launch.

## Invariants And Boundaries

### Exact identity and interrupt truth

Every wire re-resolves authorization and checks the live epoch. A control reference's possession does not authorize its use. Purpose brands are non-interchangeable, minting and decoding use the same binding shape, and withdrawal checks that its operation and withdrawal references name the same operation before consulting the live queue. This is an identity boundary, not encrypted content storage.

Interrupt fingerprints include caller authorization, session, verified epoch, turn id, and request id. Retained identical requests replay the stored answer; a reused id with different fingerprint is a typed conflict. Admission rechecks under the session lock. A client error proven unsent becomes control-unavailable; a possibly sent write records unknown acknowledgement. Reconciliation reuses the original target through the substrate's replay semantics, and pending settlement is observed independently of acknowledgement. InterruptTicket keeps turn, request, fingerprint, and evidence floor attached to one attempt. The API also records developer interrupt provenance on the seat when acknowledgement is not rejected; that provenance is not terminal settlement evidence.

Codex uses the native turn id and correlates completed evidence by exact turn.id and a terminal turn.status. Interrupted, completed, and failed map respectively to interrupted, already-settled, and failed. Pi and Claude use the active AR operation id as the caller's turnId because their control contract does not provide the same native turn identity. The native write receives expected_operation_id for non-Codex harnesses.

Claude observes the first completed result frame after the recorded evidence floor, relying on the documented single-active-turn ordering. An adapter-attributed arTerminalOutcome stamp has precedence: cancelled means interrupted, completed means already-settled, and failed stays failed. For unstamped older/foreign evidence, native success/is_error and terminal_reason classify the result; an error-shaped result without accepted-interrupt correlation remains failed. Pi requires the corresponding prompt timeline row to leave queued/dispatching/unknown and reads the latest message_end message.stopReason after the evidence floor; aborted means interrupted, error means failed, and another nonempty reason means already-settled.

The evidence clip preserves bounded identity/status scalars at their original paths: type, subtype, terminal_reason, arTerminalOutcome, message.stopReason, and turn.id/status. Absent, non-string, or overlength scalars are omitted rather than invented or truncated. Interrupt settlement must consume this preserved evidence identity rather than depend on complete transcript bodies. The inherited 64 KiB IPC-cap escalation remains a historical reason for this seam, not a freshly reproduced measurement.

Eve now has a supported interrupt capability declaration with pinned fixture provenance. However, this control ledger's settlement dispatcher selects Codex, Claude, or the Pi observer for every other harness. Thus Eve falls through to the Pi-shaped observer here; this package does not establish how its advertised native turn.cancelled evidence becomes a completed control-ledger settlement. Keep that named discrepancy visible rather than inventing an Eve-specific observer or claiming a fresh successful path.

### Queue privacy and withdrawal

The queue pages the complete retained operation timeline, then projects prompt rows only in queued, dispatching, or unknown state. Completeness means the retained live prompt projection, not all historical operations or setter rows. Kind/source/phase/order come from the substrate. Only queued cockpit rows receive cockpit withdrawal identity, a redacted preview, and a held-content digest. The OperationQueueItem validator requires withdrawable and cockpit identity presence to agree exactly with source=cockpit and phase=queued; terminal/durable prompt bodies are not fields on this projection.

The accepted setter exclusion remains: set-model/set-effort have no submission source in this contract and cannot be represented without inventing one. Their kind vocabulary remains in the DTO, while the production projection skips them; future SC1 admission was the recorded historical option, not functionality added here.

Preview content comes only from this service's submit journal. An otherwise withdrawable row absent from that journal reports an empty preview, false truncation, and digest-of-empty. This means the daemon holds no preview content, not that the original prompt or user's draft was empty. previews.py removes selected control characters, collapses whitespace, applies secret redaction, and cuts identification copy at 96 grapheme-ish clusters. Its stdlib clustering is an approximation, not a complete Unicode segmentation contract. Digest construction hashes exact text alone or canonical text plus sorted asset identity when assets are present; previews are never recovery authority.

Queue-row revisions change with phase/source/withdrawability, and the projection revision changes with the assembled row key. The 256-key revision map performs oldest-key eviction without checking settlement. An evicted row starts at revision 1 if seen again. The historical claim that this eviction can only touch settled operations and is invisible to live rows is stronger than the implemented predicate.

Withdrawal verifies both references and the exact retained kind/id/sequence, requires a cockpit source and queued state locally, then asks the shared submission authority to linearize the queued-to-dispatching race. That authority checks epoch and source under its lock, returns not-withdrawable after dispatch begins, and captures text/assets before marking the record withdrawn. Its already-withdrawn replay contains no recovery body. WithdrawalTicket keeps verified epoch, operation identity, caller operation ref, fingerprint, and withdraw request id together across successful, failed, and unknown records.

Lost withdrawal responses remain unknown and reconcile under the same withdrawRequestId. Successful initial responses may carry recovery content. Discovery exposes opaque identities and expiry, while status/reconcile expose operation projections without recovery bodies. Fetch verifies the recovery reference against caller/session/epoch and requires an unacknowledged record with retained text. recovery_assembly chooses substrate text first, then journal text if available; without either it supplies an empty response representation rather than fabricating content. It constructs the digest from selected text and available substrate asset identities, or from the journal/empty marker when text is absent. These assembly functions do not implement the previously claimed comparison of substrate payload against journal content.

Recovery and staging use 900-second leases. Recovery expiry is processed by invoked sweeps, not demonstrated here as a background timer. Recovery pressure can end retention earlier. Acknowledgement clears RecoveryRecord.text and advances recovery/withdrawal revisions; keep-current-draft also deletes recoverable asset bytes. Expiry clears that recovery text and deletes recoverable bytes. Replayed withdrawal answers suppress recovery text/assets once the withdrawal state is acknowledged or expired. These are fetchability and lifecycle predicates, not proof that all raw-content copies have been erased: the stored withdrawal response contains its assembled recovery, and the cockpit journal retains its own bounded text entry. replace-current-draft acknowledgement does not itself delete recoverable bytes. Preserve bounded recovery as intent without describing universal immediate disposal.

### Attachments and submission

Staging is ephemeral transport, not conversation persistence. The API reads each upload up to MAX_SUBMIT_ASSET_BYTES+1, validates positional metadata, and requires a declared image/file/resource kind; stage requires 1..4 uploads and a safe request component. stage_one refuses a kind whose declared capability is not supported and checks MIME, nonempty bounded bytes, required description where applicable, and nonempty name. Supported image declarations use the shared MIME/count/byte limits; file/resource staging remains unavailable. Codex and Pi images are declared supported; Claude image staging remains unverified; Eve attachment kinds are unavailable.

Spool paths are constructed beneath the session endpoint's assets directory and resolved for containment. Request components reject empty values, over-255-byte values, slash, NUL, and dot segments. The implementation sets the request directory to 0700 and files to 0600; it does not establish that every ancestor directory receives those permissions. Each asset gets a generated identity and a digest. Rebind verifies recoverable bytes against digest and size, then atomically moves them to a fresh staged identity and preserves name, MIME, description, and provenance. A supplied description is retained; otherwise the explicit filename/MIME description is the truthful accessibility fallback.

Stage fingerprints bind caller/session/epoch/request/content. Submit requires nonempty composed text, accepts only disposition next, and uses source cockpit through the shared FIFO submission port. Asset blocks must name an existing unconsumed asset and match its receipt's kind, name, MIME, digest, alt, and alt provenance before dispatch. Retained submit fingerprints reject changed content and replay identical answers. Accepted/queued/unknown outcomes consume selected assets; rejected/unsupported do not. Unknown remains represented as unknown rather than triggering a replacement upload. SubmittedContent keeps body, receipt, composed text, and selected assets attached to one submission, and nonterminal admission records the bounded cockpit journal.

Attachment reconciliation advances from the retained timeline. A queued row can become dispatching; rejection/unsupported becomes failed; an absent or delivered row can mark a previously queued/dispatching operation accepted and delete its bytes, relying on the substrate's terminal-only eviction contract. A withdrawn row is left to recovery lifecycle, and unknown is not treated as delivered. Withdrawal marks retained assets recoverable under the recovery lease and resets their one-use consumption for exchange. Rebind records the exchange and replays it only for the same target request; a different target conflicts. Staged expiry deletes bytes during attachment sweeps. Recoverable deletion is owned by the withdrawal/recovery paths. Local attachment status resolves authorization at the API boundary but does not compare a stored caller fingerprint again; this does not negate the parent single-operator authorization contract.

### Capability, policy, and telemetry honesty

The inherited 2026-07-21/L5F R4 ruling remains: contract evidence is the gate, never observed runtime/helper version equality. Current control and telemetry dispatch select per-harness declaration factories and explicitly discard the snapshot for capability selection. Fixture ids, captured versions, and observed times are provenance constants, not live probes performed on every request. The implementation does not dynamically rerun contract verification here. Interrupt and asset staging enforce their relevant supported capability; other routes project evidence or enforce their own identity/lifecycle rules rather than all consulting one universal capability gate.

Interrupt is declared supported for Codex, Claude, Pi, and Eve. Claude's earlier never-probed control statement now applies to its unverified image/policy and telemetry declarations, not interrupt. Steer and follow-up remain unavailable as ordinary submit actions. Renderer controls must use the owning capability evidence rather than infer support from fixture existence. The active page now delegates interrupt to control.interrupt_capability_for, so the historical warning that L1 always hides interrupt is obsolete. Other active-page attachment/policy/telemetry declarations can retain conservative states; Eve also delegates telemetry and declares policy evidence. Identity digests remain service-domain values: consumers should correlate identity fields rather than assume digest equality across active/library/control authorities.

Policy is GET-only here. It separates the AR local single-operator/canonical-scope posture from harness-mode evidence, with origin, observation, freshness, and capability reason. Claude can expose permissionMode while remaining policy-read unverified; Codex has no public adapter-private approval/sandbox value; Pi's policy capability is unavailable. Eve policy_read is declared supported, but _harness_mode has no Eve-specific branch and currently emits the generic Pi-origin label with no value. That is a named projection mismatch, not evidence of an Eve permission mode. Reading capability evidence does not authorize a policy mutation.

Codex cumulative token usage is the only metric emitted by this implementation. Its supported/partial capability plus evidence is necessary, and the latest retained frame containing a tokenUsage mapping supplies input/output/cached counts from total. The reader does not independently test a native notification type before selecting that mapping. Missing frame/total data produces absence; missing or noninteger counts stay absent, including booleans. Metric evidence carries unit, conversation scope, origin label, observation, exact precision, captured runtime/helper/fixture provenance, and freshness (15 seconds or less is fresh; malformed time is unknown). Other Codex context/cost/rate-limit/compaction fields and all Claude/Pi fields remain unavailable or unverified according to their declarations; Eve declares every metric unavailable.

## Historical And Verification Limits

This proposal is based on source inspection at the stated checkout and full reading of the supplied card. It supplies no test result, installed-runtime probe, route execution, delivery certification, or acceptance receipt. Historical fixture descriptions in capability constants are observed source declarations, not independently refreshed observations.

Retain the named L3/L2E/L0E/L3E design limits: native identity and replay authority belong to the substrate; acknowledgement is not settlement; terminal evidence is bounded; Pi/Claude turnId denotes the AR operation; setter rows remain excluded pending a different SC1 admission; journal-absent preview is empty held content; recovery is ephemeral and daemon-scoped; unknown outcomes require reconciliation rather than replacement ids; and control references lose validity when their secret-owning authority changes. The historical landed-pop-back preservation claim is inherited intent, not a new proof from this control inspection.

The L3 fix-round-2 transcript/64 KiB IPC escalation, L5F reviewer ACCEPTED setter and empty-held-preview rulings, L5F R5 accepted-bounding/session-end-hook limitation, L4 renderer capability and digest rulings, and L16 2026-08-05 ABBA/catalog-lock incident remain named historical context. Their original reviewer decisions, incident measurements, sidecar wiring notes, and installed delivery witnesses were not independently adjudicated here. Current code confirms the asynchronous offload and local predicates, while the strict lock-cap, settled-only queue eviction, universal serialization, journal-cross-check, and complete content-disposal claims require the narrower descriptions above.

The EFA-L4 route-conformance suite is recorded as retired. Its inherited reach was 404 on all seventeen routes, 403 on one, and reachable success bodies with a live bridge. Most typed bridge-failure legs at 400/409/422/503 were declared but undriven because the fixture did not model stale epochs or mid-write socket death. The historical real-422 conformance finding explains the outcome/refusal unions. Those figures and declarations do not establish a current pass, and no test population was examined or executed for this proposal. The card's operations, queue, attachment, real-socket, foundation-route, and on-disk spool verification expectations remain historical review guidance rather than completed checks.

The L5I normalized question-pages/exact-answers-map intent belongs to adjacent interaction machinery. Claude protocol parsing retains header, exact question text, options/descriptions, and multi-select; answer validation requires a JSON string-to-string map with exactly the expected question texts. hosted_interactions carries pages into gates and sends decisions through the shared interaction client. Invalid decisions reopen immediately with visible failure evidence. Delivery proven unsent can retain the decision for bounded retries (three attempts); possible delivery reopens with unknown delivery evidence rather than risking a second answer. The lifecycle-free harness-control response path checks epoch and serializes an answers map through the same client. These are not extra routes owned by control/api.py, and the card's blanket failed-decision-immediately-reopens wording needs this retry exception.

The inherited registry statements—no cross-repository implementation evidence, no allowed neighboring repository, and no configured Domain Documentation—were not revalidated against memory settings because this adjudication was restricted to the checkout and supplied card. They remain inherited scope/configuration limits, not fresh registry findings. Original numbered references, coverage/status/route metadata, sidecars, and excluded tables remain parent-owned; this body proposes no replacement lifecycle status. No sync or publication was performed.

## Retained Route And Coverage Metadata

These inherited tables are retained verbatim for navigation and custody. Their status/coverage cells are not a new lifecycle, test, or acceptance verdict.

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/serving/conversation/control/` |
| onboardingRoute | `mcp/src/agents_remember/serving/conversation/control/overview.md` |
| parentOverview | [`conversation/overview.md`](../overview.md) |

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

## Evidence
- Retained reference account (no fresh execution or acceptance inferred): `get_conversation_runtime` is the runtime dependency entry. [1]
- Retained reference account (no fresh execution or acceptance inferred): The authorization dependency resolves that runtime and delegates peer authorization to its bound resolver. [2]
- Retained reference account (no fresh execution or acceptance inferred): The conversation models define `protect_queue_source_privacy`. [3]
- Retained reference account (no fresh execution or acceptance inferred): `operation_fingerprint` hashes the canonical operation identity without retaining raw request content. [4]
- Retained reference account (no fresh execution or acceptance inferred): `PolicyPart` is declared in the route-local `control/policy.py`. [5]
- Retained reference account (no fresh execution or acceptance inferred): `ConversationPolicyProjection` is declared in the route-local `control/policy.py`. [6]
- Retained reference account (no fresh execution or acceptance inferred): `_map_typed_error` is the control API error-mapping entry. [7]
- Retained reference account (no fresh execution or acceptance inferred): `CONTROL_RESPONSES` is the six-status shared refusal table for the control surface. [8]
- Retained reference account (no fresh execution or acceptance inferred): `INTERRUPT_OUTCOME_RESPONSES` declares the interrupt outcome response table. [9]
- Retained reference account (no fresh execution or acceptance inferred): `WITHDRAW_OUTCOME_RESPONSES` declares the withdrawal outcome response table. [10]
- Retained reference account (no fresh execution or acceptance inferred): The control client sends the epoch-guarded interrupt write. [11]
- Retained reference account (no fresh execution or acceptance inferred): The control client validates paged operation-timeline reads before returning them. [12]
- Retained reference account (no fresh execution or acceptance inferred): The control client validates the additive asset channel on prompt submission. [13]
- Retained reference account (no fresh execution or acceptance inferred): `clip_evidence_payload` is the truncation-envelope entry. [14]
- Retained reference account (no fresh execution or acceptance inferred): Pi settlement reads the preserved terminal identity through its stop-reason reader. [15]
- Retained reference account (no fresh execution or acceptance inferred): `HarnessSubmissionAuthority` owns setter and prompt admission/dispatch on the shared authority. [16]
- Retained reference account (no fresh execution or acceptance inferred): `capabilities_for` is the active capability-view entry. [17]

- Seventeen route declarations use the terminal-session prefix and explicit response contracts; handlers construct JSONResponse bodies. [18]
- Known typed refusals preserve epoch-subclass precedence and six shared statuses; outcome tables retain refusal unions. [19]
- Server-side authorization derives from the request TCP peer, not browser identity claims. [20]
- Verified scopes, channel limits, conditional lock eviction, explicit release, and blocking-read offload are separate predicates. [21]
- Signed purpose brands contain identity and verify integrity before decoding and rebinding. [22]
- Interrupt replay/conflict and lost-ack handling remain separate from harness-specific settlement; Eve reaches the non-Claude/non-Codex branch. [23]
- Evidence clipping preserves exact bounded terminal scalars, including Claude correlation classification. [24]
- Queue projects only live prompt states; revision-key eviction has no settled-state predicate; absent journal yields empty held-content preview. [25]
- DTO validation restricts cockpit identity and withdrawability to queued cockpit rows. [26]
- Withdrawal checks live exact identity/source/state; shared authority captures content once before the terminal transition. [27]
- Recovery chooses substrate text then journal; assembly does not compare their contents. [28]
- Ack/expiry clear recovery-record text and conditionally dispose assets; retained replay response is suppressed rather than erased. [29]
- Stage/rebind/submit enforce local lifecycle and receipt predicates; terminal-only eviction is a substrate dependency. [30]
- Spool mechanics confine paths, set request-directory/file modes, verify bytes, and preserve accessible descriptions during exchange. [31]
- Claude and Eve interrupt declarations are supported; version snapshots do not select capability state. [32]
- Active-page interrupt delegates to the control authority. [33]
- Policy has no Eve-specific mode branch despite supported Eve policy capability. [34]
- Codex metric emission selects tokenUsage mappings and retains absent counts; provenance comes from capability evidence. [35]
- Adjacent question-answer validation requires exact keys; interaction delivery retries only proven-unsent failures before reopening. [36]

- The repository’s built-in adapter defaults launch local Claude, Codex, Pi and Eve subprocesses; injected factories and configured-registry scope remain distinct. [37]
