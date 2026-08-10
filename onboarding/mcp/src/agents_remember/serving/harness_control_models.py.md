# mcp/src/agents_remember/serving/harness_control_models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-02T01:42+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Defines protocol-neutral value objects and JSON projections for one hosted harness control session:
exact identity, handshake, normalized state, prompt and interaction requests, receipts,

reconciliation, transcript entries, and shutdown mode. Deliberately raw-free serializers cover the
daemon's public submit and reconciliation responses. The additive, read-only native evidence family
adds deque-domain and native-domain evidence pages, submission provenance, the reserved `arEvidence`
raw key, byte-bounded clip/window helpers, and the structural `NativePageReader` protocol. The
additive control-plane family adds the `InterruptResult` acknowledgement, the paged never-bodies
`OperationTimeline{,Item}` enumeration, `AssetReference` (runner-local `spool_path` never
serialized), `WithdrawalRecovery`, the additive optional `PromptRequest.assets` and
`WithdrawalResult.recovery` fields, all `*_json` serializers, the
`operation_timeline_item_wire_bytes` budget measurer, and the shared typed `read_asset_bytes` spool
reader. The truncation envelope preserves terminal identity: `clip_evidence_payload` re-carries a
clipped frame's tiny terminal-identity enums (frame `type`, pi `message.stopReason`, codex `turn.id` +
`turn.status`) at their original payload paths via `_preserved_evidence_identity` +
`_bounded_identity_scalar` under the `MAX_PRESERVED_EVIDENCE_SCALAR_CHARS = 256` drop-whole ceiling,
so oversized-frame interrupt settlement stays honest while no other content crosses the clip
boundary. One reserved key `AR_EVIDENCE_METHOD_KEY = "arEvidenceMethod"` and one optional typed
field `EvidenceFrame.native_method` let `evidence_frame_json` serialize the method as `nativeMethod`
only when present, so a diverted notification's native method survives to the projector as typed
metadata instead of being stripped at the bridge. The multiplexed sub-agent grammar adds
`AdapterSnapshot.pending_interactions` (plural, serialized as `pendingInteractions`) for approvals
raised on non-parent threads, and `EvidenceFrame.thread_id` as the demux key that tells the serving
layer which native thread one multiplexed evidence frame belongs to — a demux key
`evidence_frame_json` now carries onto the evidence IPC wire as the optional `threadId` key
(present only when the field is set, so parent-thread frames keep the pre-multiplex wire shape).

## Code Commentary

### Logic

The normalized snapshot keeps control (`starting`, `ready`, `disconnected`, `failed`,
`unsupported`), activity, and acceptance orthogonal while retaining raw vendor detail internally.
Request ids, correlation ids, timestamps, and exact AR/session identity remain explicit.
`receipt_json` and `reconciliation_json` preserve full internal evidence for private IPC and durable
diagnostics. `public_receipt_json` and `public_reconciliation_json` expose only normalized fields and
intentionally omit `raw` from the daemon consumer contract.

The evidence family is purely additive. `AR_EVIDENCE_KEY` (`"arEvidence"`) is the single reserved
`AdapterEvent.raw` key under which mappers place one full native payload; every pre-existing raw key
keeps its exact shape. `EvidenceFrame`/`EvidencePage` carry the deque coordinate domain (adapter
event sequence, `latestSequence`, `evictedBeforeSequence`, `truncated`, `bridgeEpoch`);
`NativeEvidenceFrame`/`NativeEvidencePage` carry the native domain with typed identity
(`nativeId`/`nativeParentId`/`nativeType`) and an opaque `nextCursor`; `SubmissionProvenance{,Batch}`
carry request-id source/state/timestamps/vendor-correlation with an epoch stamp. The two coordinate
domains are disjoint and never mixed. `clip_evidence_payload` bounds one serialized payload to a byte
budget with a visible `…[truncated]` marker envelope; `window_native_evidence_page` + `_native_window_start`
window a full native read into a bounded page whose cursor names the last native id of the previous
page, clipping a single oversized frame so every page makes progress. The runtime-checkable
`NativePageReader` structural protocol lets concrete adapters opt into native paging without editing
`HarnessProtocolAdapter`.

The control-plane family is purely additive as well. `MAX_OPERATION_TIMELINE_PAGE = 256` (the
retained ledger's own bound), `MAX_SUBMIT_ASSETS = 4`, `MAX_SUBMIT_ASSET_BYTES = 5 MiB`, the
`SUBMIT_ASSET_MIME_TYPES` image allow-list, and the `InterruptAcknowledgement` literal fix the
channel bounds and vocabulary. `InterruptResult` carries the acknowledgement, a bridge-stamped
epoch, the operation ref, vendor correlation, and raw boundary evidence — settlement stays with the
completion path, never this DTO. `OperationTimelineItem` exposes exactly ten identity keys
(operationId, kind, source|None, state, sequence, submittedAt, updatedAt, acceptedAt,
payloadDigestPresent, vendorCorrelationId) — never bodies, never setter values;
`OperationTimeline` adds `bridgeEpoch`, `latestSequence`, `evictedBeforeSequence`, `truncated`, and
the page items, and `operation_timeline_item_wire_bytes` measures one item against the shared
`EVIDENCE_PAGE_BYTE_BUDGET`. `AssetReference` is the verified staged-asset identity; its
`spool_path` is runner-local and `asset_reference_json` never serializes it. `WithdrawalRecovery`
carries the exact pre-tombstone body; `withdrawal_result_json` appends the `recovery` key only when
it is non-None, so replayed withdrawals stay byte-identical to before. `read_asset_bytes` is the
shared typed read+digest helper both the IPC admission and the native constructors use.

The clip-envelope identity preservation is additive and settlement-facing. `clip_evidence_payload`'s
unclipped path (payload already within `max_bytes`) is byte-unchanged — the full native frame is
still returned verbatim. When a frame IS clipped, the envelope now merges
`_preserved_evidence_identity(payload)` (computed once, spread into the truncation-notice dict
inside the preview shrink loop) at the frame's ORIGINAL payload paths: the top-level frame `type`
(pi `message_end`), `message.stopReason` as `{"message": {"stopReason": <str>}}` (the pi terminal
enum), and codex `turn.id` + `turn.status` as `{"turn": {"id": <str>, "status": <str>}}`. Only tiny
scalar identity/status enums cross — never message `role`/`content`, turn `items`/`error`, or any
other body. Each scalar routes through `_bounded_identity_scalar`, an isinstance-guarded allowlist
that preserves a value only when it is a `str` with `len <= MAX_PRESERVED_EVIDENCE_SCALAR_CHARS`
(256); an absent, non-string, or over-length value is dropped WHOLE — never invented, never
truncated (a partial id/status could mis-correlate at settlement). This closes the oversized-frame
settlement gap: a frame above the 32 KiB evidence budget previously kept only
`{arEvidenceTruncated, originalBytes, preview}`, so pi settlement stalled `pending` forever and
codex settlement re-stalled; the preserved enums let the unchanged settlement readers decide
honestly on the clipped frame — `_pi_stop_reason` matches `frame.raw["type"] == "message_end"` then
reads `message.stopReason`, and `_codex_terminal_outcome` correlates `frame.raw["turn"]["id"] ==
turn_id` BEFORE taking `turn["status"]`, so BOTH `turn.id` and `turn.status` must survive together
or the frame is skipped. `turn.id` is preserved beyond the master decision's literal `turn.status`
precisely because the codex consumer correlates on it first; a status-only envelope would be
unmatchable and re-stall.

The native-method carry is additive metadata on the same evidence frame.
`AR_EVIDENCE_METHOD_KEY` (`"arEvidenceMethod"`) is a second reserved `AdapterEvent.raw` key,
disjoint from `AR_EVIDENCE_KEY`: a mapper that already knows its native notification method sets it
beside the `arEvidence` payload. `EvidenceFrame.native_method` carries it verbatim so a
projector switches on the real method rather than re-guessing meaning from params shape, and
`evidence_frame_json` writes the `nativeMethod` wire key only when the field is non-None.
The field defaults None, so every evidence frame, page, and serialization stays
byte-identical when no method is carried; the bridge, not this module, strips the reserved raw key.

The multiplexing grammar is additive in the same posture. `AdapterSnapshot.
pending_interactions` is a tuple of `PendingInteraction` for approvals raised on
non-parent (sub-agent) threads — codex sub-agent threads raise their own server→client requests on
the seat's one connection; each entry carries its thread identity in `raw['threadId']` plus the
agent-label evidence the adapter could bind. The singular `pending_interaction` stays the
parent-thread slot for back-compat, and `snapshot_json` adds the plural `pendingInteractions` wire
key beside the untouched singular one, so consumers that predate multiplexing see
exactly the parent entry they always saw. `EvidenceFrame.thread_id` is the demux key:
codex auto-attaches sub-agent thread listeners to the seat's connection, so one evidence stream
carries many threads and `None` means the parent/session thread (matching pre-multiplexing behavior); Claude
encodes its sidechain join key (`parent_tool_use_id`) inside `raw` instead.
`evidence_frame_json` serializes `thread_id` as the optional `threadId` wire key only
when it is non-None — the multiplexed demux key finally crosses the evidence IPC wire;
parent frames carry no key, so the pre-multiplex wire shape stays byte-identical. (The recorded
root cause of the earlier in-process-only gap: a dashboard-side projector received every evidence
frame as thread-less and bound all agent content to the parent conversation.)

The 256-char ceiling is a fail-safe, not a formatting bound. Every preserved field is a protocol
enum (pi `stopReason`, codex turn `status`), a frame-type name, or a vendor turn id — a handful of
characters in every legitimate shape — so 256 is orders of magnitude above any real value while four
maxed scalars stay ≈1 KB, trivially inside both the 32 KiB evidence budget and the native
windower's `budget//2` page. Dropping an over-length scalar whole keeps a malformed giant scalar
from making the truncation envelope exceed its own byte budget: without the bound, such a frame
makes the envelope exceed `max_bytes` at every preview size and `clip_evidence_payload` RAISES after
64 preview halvings instead of clipping — session-fatal in the bridge `_run_events` loop
(`control="failed"`, the event loop terminates) and a persistent failure in the native page
windower. With the bound the envelope degrades to the pre-identity total clip for that one field,
never raising for any wire-reachable frame.

### Conventions

Internal serializers preserve additive vendor evidence; public serializers are separate named
functions rather than an exclusion flag so callers cannot accidentally leak the private mapping.
Wire names are camel-case. The multiplexed forms follow the same additive convention: the plural
tuple defaults empty and the demux key defaults `None`, so a single-thread harness serializes
byte-identically to before.

### Invariants And Boundaries

- Models carry protocol state; tmux pane text and terminal logs are diagnostic, not authoritative.
- Additive raw event detail is retained without guessing semantics for unknown event kinds.
- Disconnect-after-possible-send remains unknown and must be reconciled, never blindly resent.
- Public receipt/reconciliation responses retain normalized correlation and detail but never `raw`.
- The evidence family is additive and read-only: no existing DTO or serializer changes shape or
  semantics, and unknown native shapes cross as unknown-vendor evidence with raw preserved and
  semantics never guessed.
- `EvidenceFrame.native_method` is an optional discriminator hint, never authority: it defaults
  None, `nativeMethod` serializes only when present, and the reserved `AR_EVIDENCE_METHOD_KEY` is a
  raw-key convention the bridge diverts — this module never reads or promotes it from a snapshot.
- Evidence frames are evidence, not authority; deep history stays with the native read APIs.
- Deque-sequence and native-cursor coordinates are disjoint domains; `bridgeEpoch` rides every
  evidence response so a mid-paging bridge restart fails detectably.
- The control-plane family is additive-only: existing DTOs change shape only through optional
  fields with empty/None defaults (`PromptRequest.assets`, `WithdrawalResult.recovery`), and
  `withdrawal_result_json` omits the `recovery` key entirely when it is None.
- Timeline items never carry bodies: identity, source, kind, sequence, state, timestamps, and a
  digest-presence boolean only — no prompt text, no setter values.
- `AssetReference.spool_path` is runner-local and never serialized onto the wire.
- The interrupt acknowledgement is never settlement; the operation still settles through the
  landed completion path.
- The clip envelope preserves ONLY the four terminal-identity scalars (`type`,
  `message.stopReason`, `turn.id`, `turn.status`) at their original payload paths; no message text,
  content blocks, turn items, or other body ever crosses the clip boundary (proven by byte-level
  exact key-sets plus a tail-leak sentinel).
- Preserved scalars are drop-whole bounded at `MAX_PRESERVED_EVIDENCE_SCALAR_CHARS = 256`:
  absent/non-string/over-length stays absent — never invented, never truncated — and the truncation
  envelope never collapses into a raise for any wire-reachable frame.
- The preserved paths are a settlement contract: the `_pi_stop_reason` and
  `_codex_terminal_outcome` settlement readers read exactly these paths, and the codex reader correlates `turn.id`
  before `turn.status`, so both must survive together or the frame is skipped.
- The unclipped clip path is byte-identical to the pre-preservation behavior; identity preservation affects only the
  clipped truncation envelope, and the no-leak guarantee is untouched (the change is
  buffer-copy-only, `reduce_adapter_event` still never reads adapter snapshot raw).
- The multiplexing grammar is back-compat by construction: the singular `pending_interaction`
  slot stays the parent-thread entry, the plural `pending_interactions` defaults to the empty tuple
  and is serialized as the additive `pendingInteractions` key only, and `EvidenceFrame.thread_id`
  defaults `None` = the parent/session thread — parent-thread frames keep the exact pre-multiplex
  wire shape, and agent frames carry only the one additive optional `threadId` key.
- `thread_id` is a demux key, never authority: this module carries it verbatim (the bridge extracts
  it from diverted raw evidence), `evidence_frame_json` emits it as the additive optional
  `threadId` wire key only when present, and a missing/`None` value always reads as the parent
  thread — no consumer may invent a thread.

### Todos

None known for the public serialization boundary.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The API consumes only the public projections, while private IPC keeps full internal serializers. The
evidence DTOs are consumed by the bridge buffer, the three additive IPC actions, and the
validated client reads. The plural pendings are filled by the codex adapter's
per-thread demux and serialized end-to-end through `snapshot_json` into the control plane.

| Finding | Anchor | Source |
| --- | --- | --- |
| The daemon submit route selects the public raw-free receipt serializer. | `api_terminal_submit`; "public_receipt_json(" | mcp/src/agents_remember/serving/harness_control_api.py:370-403 |
| The daemon reconcile route selects the public raw-free reconciliation serializer. | `api_terminal_reconcile`; "public_reconciliation_json(" | mcp/src/agents_remember/serving/harness_control_api.py:405-423 |
| Private IPC still serializes full receipt evidence for exact-session peers. | `_submit` | mcp/src/agents_remember/serving/harness_control_ipc.py:229-248 |
| Private IPC still serializes full reconciliation evidence for exact-session peers. | `_reconcile` | mcp/src/agents_remember/serving/harness_control_ipc.py:221-227 |
| Public route tests seed sensitive-looking raw mappings and prove they do not cross the boundary. | `test_submit_preserves_whole_message_request_and_vendor_correlation`; `test_reconcile_keeps_the_same_request_correlation` | mcp/tests/test_serving_harness_control_api.py:192-227; mcp/tests/test_serving_harness_control_api.py:482-506 |
| The bridge diverts `arEvidence` payloads into its bounded deque and stamps typed thread identity onto each frame. | `_divert_evidence`; `_evidence_thread_id`; `_append_evidence` | mcp/src/agents_remember/serving/harness_control_bridge.py:468-489; mcp/src/agents_remember/serving/harness_control_bridge.py:505-528; mcp/src/agents_remember/serving/harness_control_bridge.py:491-503 |
| The three additive IPC actions serialize these evidence/provenance DTOs onto the private socket. | `_evidence`; `_evidence_native_page`; `_submission_provenance` | mcp/src/agents_remember/serving/harness_control_ipc.py:377-383; mcp/src/agents_remember/serving/harness_control_ipc.py:385-397; mcp/src/agents_remember/serving/harness_control_ipc.py:399-405 |
| The evidence contract tests cover reserved-key privacy, epoch/paging, thread-id wire round-trip, provenance bounds, and fail-closed native-page continuation. | `test_reserved_key_round_trip_and_no_leak`; `test_evidence_action_round_trip_with_epoch_and_paging`; `test_evidence_thread_id_round_trips_over_ipc`; `test_submission_provenance_all_sources_epoch_and_bounds`; `test_native_page_continuation_no_overlap_no_gap_and_fail_closed_cursor` | mcp/tests/test_harness_control_evidence.py:361-409; mcp/tests/test_harness_control_evidence_ipc.py:57-89; mcp/tests/test_harness_control_evidence_ipc.py:91-117; mcp/tests/test_harness_control_evidence_ipc.py:229-312; mcp/tests/test_harness_control_evidence_ipc.py:393-439 |
| The codex adapter's `_sync_pending_snapshot` preserves the parent pending interaction and adds raw `threadId` plus `agentLabel` for non-parent entries. | `_sync_pending_snapshot` | mcp/src/agents_remember/serving/codex_app_server_adapter.py:910-922 |
| The L2E control-plane models define interrupt/timeline/asset/recovery DTOs and their serializers, the timeline wire-byte measurer, and `read_asset_bytes`. | `InterruptResult`; `OperationTimeline`; `OperationTimelineItem`; `AssetReference`; `WithdrawalRecovery`; `interrupt_result_json`; `operation_timeline_json`; `operation_timeline_item_wire_bytes`; `asset_reference_json`; `withdrawal_result_json`; `read_asset_bytes` | mcp/src/agents_remember/models/conversations/control_wire.py:154-162; mcp/src/agents_remember/models/conversations/control_wire.py:210-215; mcp/src/agents_remember/models/conversations/control_wire.py:228-237; mcp/src/agents_remember/models/conversations/control_wire.py:240-253; mcp/src/agents_remember/models/conversations/control_wire.py:256-264; mcp/src/agents_remember/models/conversations/control_wire.py:372-383; mcp/src/agents_remember/models/conversations/control_wire.py:386-394; mcp/src/agents_remember/models/conversations/control_wire.py:404-412; mcp/src/agents_remember/models/conversations/control_wire.py:430-437; mcp/src/agents_remember/models/conversations/control_wire.py:440-441; mcp/src/agents_remember/models/conversations/control_wire.py:444-451 |
| The interrupt and operation-timeline IPC actions serialize these DTOs over the same private socket. | `_interrupt`; `_operation_timeline` | mcp/src/agents_remember/serving/harness_control_ipc.py:306-313; mcp/src/agents_remember/serving/harness_control_ipc.py:315-326 |
| The submit-asset admission validates staged-asset claims before dispatch. | `_submit_asset_schema` | mcp/src/agents_remember/serving/harness_control_ipc.py:485-506 |
| The authority captures the pre-tombstone recovery on withdraw and extends the idempotence digest over canonical asset identity only when assets ride. | `withdraw`; `_payload_digest` | mcp/src/agents_remember/serving/harness_submission_authority.py:452-498; mcp/src/agents_remember/serving/harness_submission_authority.py:987-1008 |
| Paging the retained ledger into `OperationTimeline` moved OUT of the authority in 260731-EFA-L6: `OperationRecord` and `SubmissionLedger` now live in their own module, and the never-bodies paging is `SubmissionLedger.operation_timeline`. | `OperationRecord`; `SubmissionLedger`; `operation_timeline` | mcp/src/agents_remember/serving/harness_submission_ledger.py:57-252; mcp/src/agents_remember/serving/harness_submission_ledger.py:255-437 |
| Contract tests pin the interrupt/timeline/asset/recovery round-trips, bounds, and validation battery over these DTOs. | `InterruptBridgeTests`; `OperationTimelineTests`; `AssetNativeConstructionTests` | mcp/tests/test_harness_control_plane.py:289-376; mcp/tests/test_harness_control_plane_assets.py:249-483; mcp/tests/test_harness_control_plane_channels.py:321-481 |

## Cross-Repo References

No external repository boundary is implemented by these local protocol models.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Submission Authority Delta

The normalized model now carries bridge epoch on prompts, receipts, and reconciliation; defines full
operation references, authority/status/batch/withdraw/event records; and separates private internal
serialization from raw-free public lifecycle projection. The public alphabet is intentionally
smaller than vendor evidence and sufficient for monotonic cockpit rendering.

## Structured Pending Interaction Delta

Control models now carry structured pending-interaction pages, per-question options, and multi-select semantics alongside the compatibility prompt/choice view. The normalized model lets direct and gate-mediated responders submit one authoritative answers map.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260731-EFA-L2 Current Delta

The settlement identity/status reads were decomposed and their key set named:

- `_TOP_LEVEL_IDENTITY_KEYS` = `("type", "subtype", "terminal_reason", AR_TERMINAL_OUTCOME_KEY)` —
  the identity/status enums the settlement reads take straight off the frame root.
- `_bounded_identity_scalars(source, keys)` — the subset of `keys` present in `source` as bounded
  scalars, kept at their own names.
- `_nested_identity_scalars(source, path, keys)` — one nested object's surviving identity scalars,
  rebuilt at `path`.

What survives the bounded projection is unchanged; the rule is now stated once rather than repeated
per nesting level.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260731-EFA-L9 Change

The shared evidence and control-wire contracts moved to `models/conversations/evidence.py` and
`models/conversations/control_wire.py` (R2/R8); this module now holds the control-plane-only set
(278 lines) — `CONTROL_PROTOCOL_VERSION`, terminal/transcript/adapter vocabulary,
`TerminalResult`, `AdapterHandshake`, `PromptRequest`, `InteractionResponse`, submission
status/lookup records, and their JSON projections. L11 will move the control-only set to
`harness_control/`; no forwarding shim exists, and conversation modules import the shared names
from `models.conversations`.

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: recorded the control-only scope after the
  shared contracts moved to models; the L9 change section above documents the split. Verification
  metadata pinned until closeout stamps the L9 code commit.
- 2026-08-04T11:34:10+02:00 — 260731-EFA-L6 S18-B12 curator: restored route-handler/serializer ownership, expanded the evidence-contract test matrix, split pending-interaction producers, and widened the L2E DTO/serializer coverage; the scoped fixer will generate citation ranges.
- 2026-08-02T01:42+02:00 — 260731-EFA-L6 debt this leaf created, now cleared: three L6 workers split six oversized `serving/` classes while this memory tree was being edited, and every line range in this document that pointed into them went out of bounds the instant the sources shrank (`citation_range_out_of_bounds`). Ranges were re-derived by READING the cited construct at its current location, never by scaling or subtracting a delta — the splits moved code between files rather than shifting it uniformly. Where a construct left the file the row names, the Source Path moved with the range into its own row rather than being silently re-pointed. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T17:40+02:00 — 260731-EFA-L4 markdown repair: a prose line had been hard-wrapped at a ` + ` conjunction, leaving the plus at column zero where markdown reads `+ ` as a list bullet, so a wrapped sentence rendered as a spurious new list item mid-thought. The plus moved to the end of the previous line; the rendered prose is character-for-character unchanged. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: recorded that `_register_submission_routes` delegates submission writes to `_register_submission_write_routes`; the public submit and reconcile serializers and the two raw-free route tests remain the source owners.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `_TOP_LEVEL_IDENTITY_KEYS` and the `_bounded_identity_scalars` / `_nested_identity_scalars` split.
- 2026-07-27T00:02+02:00 — 260718-CHATS-L7R curator: recorded the evidence-wire demux fix —
  `evidence_frame_json` now emits the optional `threadId` key when `EvidenceFrame.thread_id` is
  set, so the multiplexed demux key crosses the evidence IPC wire; parent frames carry
  no key and the pre-multiplex wire stays byte-identical. Recorded the root cause (a dashboard-side
  projector received every frame thread-less and bound all agent content to the parent) and
  corrected the two body statements that claimed the key was deliberately unserialized.
  Verification metadata stays pinned — the change is uncommitted.
- 2026-07-26T15:36+02:00 — 260718-CHATS-L7 curator: the earlier pre-fix note is historical only; at that point `evidence_frame_json` did not serialize the demux key, while the later correction and current source emit optional `threadId` when `EvidenceFrame.thread_id` is present.
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: R1 — documented the additive native-method
  carry: reserved key `AR_EVIDENCE_METHOD_KEY` (`"arEvidenceMethod"`), the optional
  `EvidenceFrame.native_method` field, and `evidence_frame_json`'s `nativeMethod`
  serialization when present, with the additive/optional invariant. Verification
  metadata stays pinned to the last committed source until closeout stamps the candidate commit.
- 2026-07-20T15:10+02:00 — 260718-CHATS-L3E curator: documented the clip-envelope terminal-identity
  preservation — `clip_evidence_payload` now re-carries `type`/`message.stopReason`/`turn.id`/
  `turn.status` at their original payload paths (`_preserved_evidence_identity` +
  `_bounded_identity_scalar`, drop-whole bounded at `MAX_PRESERVED_EVIDENCE_SCALAR_CHARS = 256`) so
  oversized-frame interrupt settlement stays honest for the unchanged L3 `_pi_stop_reason`/
  `_codex_terminal_outcome` readers, with no content crossing the boundary and the giant-scalar
  envelope-collapse raise (session-fatal in the bridge loop) fail-safed. Verification metadata stays
  pinned to the last committed source until closeout stamps the candidate commit.
- 2026-07-20T00:08+02:00 — 260718-CHATS-L2E curator: documented the additive control-plane
  family — `InterruptResult`, paged never-bodies `OperationTimeline{,Item}` with the shared
  budget measurer, `AssetReference` (runner-local `spool_path` never serialized),
  `WithdrawalRecovery` (key omitted on replay), the additive `PromptRequest.assets`/
  `WithdrawalResult.recovery` optionals, the channel constants, and the typed `read_asset_bytes`
  helper; refreshed the bridge/IPC citation ranges for the shifted sources. Verification metadata
  stays pinned to the last committed source until closeout stamps the candidate commit.
- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: documented the additive native evidence
  family — the reserved `arEvidence` raw key, deque-domain `EvidenceFrame`/`EvidencePage`,
  native-domain `NativeEvidenceFrame`/`NativeEvidencePage` with typed identity and opaque
  continuation, `SubmissionProvenance{,Batch}`, the structural `NativePageReader` protocol, and the
  byte-bounded clip/window helpers. Verification metadata stays pinned to the last committed source
  until closeout stamps the candidate commit.
- 2026-07-17T21:39+02:00 — FEUI-L5: added generation-bound submit records, full operation refs,
  normalized status/withdraw DTOs, and explicit public/private serialization boundaries.

- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: documented the explicit public receipt and
  reconciliation serializers that preserve normalized evidence while omitting adapter-private raw.
- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator pass: created onboarding for the normalized
  control models, identity/correlation state, raw vendor detail, and R11 draft ownership.
