# mcp/src/agents_remember/serving/harness_control_models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-01T17:40+02:00 |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
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
`AR_EVIDENCE_METHOD_KEY` (`"arEvidenceMethod"`, L66) is a second reserved `AdapterEvent.raw` key,
disjoint from `AR_EVIDENCE_KEY`: a mapper that already knows its native notification method sets it
beside the `arEvidence` payload. `EvidenceFrame.native_method` (L463-L467) carries it verbatim so a
projector switches on the real method rather than re-guessing meaning from params shape, and
`evidence_frame_json` writes the `nativeMethod` wire key only when the field is non-None
(L620-L621). The field defaults None, so every evidence frame, page, and serialization stays
byte-identical when no method is carried; the bridge, not this module, strips the reserved raw key.

The multiplexing grammar is additive in the same posture. `AdapterSnapshot.
pending_interactions` (L226-L234) is a tuple of `PendingInteraction` for approvals raised on
non-parent (sub-agent) threads — codex sub-agent threads raise their own server→client requests on
the seat's one connection; each entry carries its thread identity in `raw['threadId']` plus the
agent-label evidence the adapter could bind. The singular `pending_interaction` stays the
parent-thread slot for back-compat, and `snapshot_json` adds the plural `pendingInteractions` wire
key beside the untouched singular one (L603-L607), so consumers that predate multiplexing see
exactly the parent entry they always saw. `EvidenceFrame.thread_id` (L471-L477) is the demux key:
codex auto-attaches sub-agent thread listeners to the seat's connection, so one evidence stream
carries many threads and `None` means the parent/session thread (matching pre-multiplexing behavior); Claude
encodes its sidechain join key (`parent_tool_use_id`) inside `raw` instead.
`evidence_frame_json` (L613-L624) serializes `thread_id` as the optional `threadId` wire key only
when it is non-None (L622-L623) — the multiplexed demux key finally crosses the evidence IPC wire;
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The API consumes only the public projections, while private IPC keeps full internal serializers. The
evidence DTOs are consumed by the bridge buffer, the three additive IPC actions, and the
validated client reads. The plural pendings are filled by the codex adapter's
per-thread demux and serialized end-to-end through `snapshot_json` into the control plane.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The daemon submit and reconcile routes select the public raw-free serializers (`public_receipt_json`, `public_reconciliation_json`). | L304-L339 | [harness_control_api.py](agents-remember/mcp/src/agents_remember/serving/harness_control_api.py) |
| Private IPC still serializes full receipts and reconciliation evidence for exact-session peers. | L180-L227 | [harness_control_ipc.py](agents-remember/mcp/src/agents_remember/serving/harness_control_ipc.py) |
| Public route tests seed sensitive-looking raw mappings and prove they do not cross the boundary. | L192-L227; L482-L506 | [test_serving_harness_control_api.py](agents-remember/mcp/tests/test_serving_harness_control_api.py) |
| The bridge diverts `arEvidence` payloads into its bounded deque, stamps the epoch on every evidence page, and extracts `threadId` into `EvidenceFrame.thread_id`. | L204-L288; L495-L610 | [harness_control_bridge.py](agents-remember/mcp/src/agents_remember/serving/harness_control_bridge.py) |
| The three additive IPC actions serialize these evidence/provenance DTOs onto the private socket. | L212-L218; L380-L410 | [harness_control_ipc.py](agents-remember/mcp/src/agents_remember/serving/harness_control_ipc.py) |
| Contract tests pin the evidence round-trips, bounds, no-leak guarantee, continuation, and provenance matrix over these DTOs. | L268-L1460 | [test_harness_control_evidence.py](agents-remember/mcp/tests/test_harness_control_evidence.py) |
| The codex adapter fills the multiplexing grammar: `_sync_pending_snapshot` rebuilds `pending_interactions` with per-thread `threadId`/`agentLabel` evidence and keeps the singular slot the parent's. | L955-L981 | [codex_app_server_adapter.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_adapter.py) |
| The L2E control-plane DTOs and serializers: channel constants, `InterruptResult`, `OperationTimeline{,Item}`, `AssetReference`, `WithdrawalRecovery`, and the typed spool reader. | L113-L122; L255-L263; L385-L443; L1046-L1064 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |
| The interrupt/operation-timeline IPC actions and the submit-asset admission serialize these DTOs over the same private socket. | L220-L225; L275-L325; L458-L500 | [harness_control_ipc.py](agents-remember/mcp/src/agents_remember/serving/harness_control_ipc.py) |
| The authority pages the retained ledger into `OperationTimeline`, captures the pre-tombstone recovery, and extends the idempotence digest over canonical asset identity only when assets ride. | L491-L531; L538-L590; L1130-L1151 | [harness_submission_authority.py](agents-remember/mcp/src/agents_remember/serving/harness_submission_authority.py) |
| Contract tests pin the interrupt/timeline/asset/recovery round-trips, bounds, and validation battery over these DTOs. | L252-L1575 | [test_harness_control_plane.py](agents-remember/mcp/tests/test_harness_control_plane.py) |

## Cross-Repo References

No external repository boundary is implemented by these local protocol models.

| Finding | Citations | Source Path |
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

## Update History

- 2026-08-01T17:40+02:00 — 260731-EFA-L4 markdown repair: a prose line had been hard-wrapped at a ` + ` conjunction, leaving the plus at column zero where markdown reads `+ ` as a list bullet, so a wrapped sentence rendered as a spurious new list item mid-thought. The plus moved to the end of the previous line; the rendered prose is character-for-character unchanged. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 2 cross-file line citations. The daemon
  route row is now L304-L339 of `harness_control_api.py` — the routes were regrouped into
  `_register_submission_routes`, and `api_terminal_submit` (L304-L323) / `api_terminal_reconcile`
  (L325-L339) still wrap their calls in `public_receipt_json` / `public_reconciliation_json`; named
  both serializers in the claim. The no-leak test row was one range starting mid-file; the two
  tests that actually seed a sensitive `raw` mapping and assert it never crosses are
  `test_submit_preserves_whole_message_request_and_vendor_correlation` (L192-L227, seeding
  `VENDOR_AUTH_TOKEN`) and `test_reconcile_keeps_the_same_request_correlation` (L482-L506, seeding
  `vendorThread`/`auth.account`), so the citation is now `L192-L227; L482-L506`. Read all four
  ranges back.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `_TOP_LEVEL_IDENTITY_KEYS` and the `_bounded_identity_scalars` / `_nested_identity_scalars` split.
- 2026-07-27T00:02+02:00 — 260718-CHATS-L7R curator: recorded the evidence-wire demux fix —
  `evidence_frame_json` now emits the optional `threadId` key when `EvidenceFrame.thread_id` is
  set (L622-L623), so the multiplexed demux key crosses the evidence IPC wire; parent frames carry
  no key and the pre-multiplex wire stays byte-identical. Recorded the root cause (a dashboard-side
  projector received every frame thread-less and bound all agent content to the parent) and
  corrected the two body statements that claimed the key was deliberately unserialized.
  Verification metadata stays pinned — the change is uncommitted.
- 2026-07-26T15:36 — 260718-CHATS-L7 curator: documented the multiplexed sub-agent grammar —
  `AdapterSnapshot.pending_interactions` (L226-L234) serialized as the additive
  `pendingInteractions` key in `snapshot_json` (L603-L607) with the singular slot kept as the
  parent-thread entry, and `EvidenceFrame.thread_id` (L471-L477) as the demux key (`None` = parent;
  Claude keeps its join key in `raw`) that `evidence_frame_json` deliberately does not serialize as
  its own wire key. Fixed the stale R1 citations (`native_method` L416-L420 → L463-L467;
  `nativeMethod` L547-L548 → L620-L621) and refreshed the bridge/authority/api/IPC citation ranges
  against the current sources. Verification metadata stays pinned: the L7 change is uncommitted, so
  no commit hash can attest it.
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: R1 — documented the additive native-method
  carry: reserved key `AR_EVIDENCE_METHOD_KEY` (`"arEvidenceMethod"`, L66), the optional
  `EvidenceFrame.native_method` field (L416-L420), and `evidence_frame_json`'s `nativeMethod`
  serialization when present (L547-L548), with the additive/optional invariant. Verification
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
