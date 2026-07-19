# mcp/src/agents_remember/serving/harness_control_models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T00:08+02:00 |
| lastVerifiedCommitHash | `22562e0f2161c2d980385a462275dc370deb72eb` |
| lastVerifiedCommitDate | 2026-07-20T00:45:01+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Defines protocol-neutral value objects and JSON projections for one hosted harness control session:
exact identity, handshake, normalized state, prompt and interaction requests, receipts,
reconciliation, transcript entries, and shutdown mode. L4 adds deliberately raw-free serializers
for the daemon's public submit and reconciliation responses. 260718-CHATS-L0E adds the additive,
read-only native evidence family: deque-domain and native-domain evidence pages, submission
provenance, the reserved `arEvidence` raw key, byte-bounded clip/window helpers, and the structural
`NativePageReader` protocol. 260718-CHATS-L2E adds the additive control-plane family: the
`InterruptResult` acknowledgement, the paged never-bodies `OperationTimeline{,Item}` enumeration,
`AssetReference` (runner-local `spool_path` never serialized), `WithdrawalRecovery`, the additive
optional `PromptRequest.assets` and `WithdrawalResult.recovery` fields, all `*_json` serializers,
the `operation_timeline_item_wire_bytes` budget measurer, and the shared typed `read_asset_bytes`
spool reader.

## Code Commentary

### Logic

The normalized snapshot keeps control (`starting`, `ready`, `disconnected`, `failed`,
`unsupported`), activity, and acceptance orthogonal while retaining raw vendor detail internally.
Request ids, correlation ids, timestamps, and exact AR/session identity remain explicit.
`receipt_json` and `reconciliation_json` preserve full internal evidence for private IPC and durable
diagnostics. `public_receipt_json` and `public_reconciliation_json` expose only normalized fields and
intentionally omit `raw` from the daemon consumer contract.

The L0E evidence family is purely additive. `AR_EVIDENCE_KEY` (`"arEvidence"`) is the single reserved
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

The L2E control-plane family is purely additive as well. `MAX_OPERATION_TIMELINE_PAGE = 256` (the
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

### Conventions

Internal serializers preserve additive vendor evidence; public serializers are separate named
functions rather than an exclusion flag so callers cannot accidentally leak the private mapping.
Wire names are camel-case.

### Invariants And Boundaries

- Models carry protocol state; tmux pane text and terminal logs are diagnostic, not authoritative.
- Additive raw event detail is retained without guessing semantics for unknown event kinds.
- Disconnect-after-possible-send remains unknown and must be reconciled, never blindly resent.
- Public receipt/reconciliation responses retain normalized correlation and detail but never `raw`.
- The evidence family is additive and read-only: no existing DTO or serializer changes shape or
  semantics, and unknown native shapes cross as unknown-vendor evidence with raw preserved and
  semantics never guessed.
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

### Todos

None known for the L4 public serialization boundary.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The API consumes only the public projections, while private IPC keeps full internal serializers. The
L0E evidence DTOs are consumed by the bridge buffer, the three additive IPC actions, and the
validated client reads.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The daemon submit and reconcile routes select the public raw-free serializers. | L173-L210 | [harness_control_api.py](agents-remember/mcp/src/agents_remember/serving/harness_control_api.py) |
| Private IPC still serializes full receipts and reconciliation evidence for exact-session peers. | L180-L227 | [harness_control_ipc.py](agents-remember/mcp/src/agents_remember/serving/harness_control_ipc.py) |
| Public route tests seed sensitive-looking raw mappings and prove they do not cross the boundary. | L166-L219 | [test_serving_harness_control_api.py](agents-remember/mcp/tests/test_serving_harness_control_api.py) |
| The bridge diverts `arEvidence` payloads into its bounded deque and stamps the epoch on every evidence page. | L93; L176-L240; L445-L530 | [harness_control_bridge.py](agents-remember/mcp/src/agents_remember/serving/harness_control_bridge.py) |
| The three additive IPC actions serialize these evidence/provenance DTOs onto the private socket. | L206-L211; L381-L410 | [harness_control_ipc.py](agents-remember/mcp/src/agents_remember/serving/harness_control_ipc.py) |
| Contract tests pin the evidence round-trips, bounds, no-leak guarantee, continuation, and provenance matrix over these DTOs. | L268-L1460 | [test_harness_control_evidence.py](agents-remember/mcp/tests/test_harness_control_evidence.py) |
| The L2E control-plane DTOs and serializers: channel constants, `InterruptResult`, `OperationTimeline{,Item}`, `AssetReference`, `WithdrawalRecovery`, and the typed spool reader. | L75-L88; L184-L204; L314-L366; L768-L830 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |
| The interrupt/operation-timeline IPC actions and the submit-asset admission serialize these DTOs over the same private socket. | L212-L215; L231-L325; L449-L490 | [harness_control_ipc.py](agents-remember/mcp/src/agents_remember/serving/harness_control_ipc.py) |
| The authority pages the retained ledger into `OperationTimeline`, captures the pre-tombstone recovery, and extends the idempotence digest over canonical asset identity only when assets ride. | L436-L485; L515-L531; L1053-L1073 | [harness_submission_authority.py](agents-remember/mcp/src/agents_remember/serving/harness_submission_authority.py) |
| Contract tests pin the interrupt/timeline/asset/recovery round-trips, bounds, and validation battery over these DTOs. | L252-L1575 | [test_harness_control_plane.py](agents-remember/mcp/tests/test_harness_control_plane.py) |

## Cross-Repo References

No external repository boundary is implemented by these local protocol models.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260715-FEUI-L5 Submission Authority Delta

The normalized model now carries bridge epoch on prompts, receipts, and reconciliation; defines full
operation references, authority/status/batch/withdraw/event records; and separates private internal
serialization from raw-free public lifecycle projection. The public alphabet is intentionally
smaller than vendor evidence and sufficient for monotonic cockpit rendering.

## Update History

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
