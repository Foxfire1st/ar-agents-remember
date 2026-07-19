# mcp/src/agents_remember/serving/harness_control_bridge.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_bridge.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T00:08+02:00 |
| lastVerifiedCommitHash | `22562e0f2161c2d980385a462275dc370deb72eb` |
| lastVerifiedCommitDate | 2026-07-20T00:45:01+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Hosts one exact harness identity, validates adapter handshake/capabilities, serializes prompts,
interactions, reconciliation, and model/effort mutations through one bounded queue, and publishes
normalized snapshots/transcripts. 260718-CHATS-L0E adds a bounded per-session native evidence
buffer beside the untouched transcript path, plus deque-domain/native-domain evidence page reads
and the submission-provenance batch read. 260718-CHATS-L2E adds the epoch-guarded native
`interrupt` write dispatch (bridge-stamped epoch, adapter-mint epoch refused, settlement untouched)
and the `operation_timeline` read delegation.

## Code Commentary

### Logic

Start refuses identity, protocol, readiness, or capability mismatches and force-cleans a rejected
adapter. `advertise` reads the already-running exact adapter instance and refuses outside running
state. `set_model` and `set_effort` require that same running bridge and delegate to the command queue
as prompt submission, interaction response, reconciliation, and stop. Submission receipts remain
distinct from terminal completion; reconciliation and explicit unknown resolution handle ambiguous
sends. Event reduction and transcript retention are bounded. Unexpected queue failures publish a
loud failed state, resolve active callers, and drain queued commands.

The L0E evidence buffer is a bounded per-session deque (default 2000 frames, per-frame 32 KiB clip)
fed at the single `_run_events` event-consumption point: when an adapter event carries the reserved
`arEvidence` raw key, `_divert_evidence` appends an `EvidenceFrame(sequence, kind, created_at,
clipped payload)` and the redacted event (raw minus `arEvidence`) flows to reduce/observe/transcript/
publish, so `snapshot.raw`, catalog `control_raw`, SSE projections, and every existing consumer stay
byte-identical. `evidence()` pages the deque domain with count+byte bounds and reports
`latestSequence`, `evictedBeforeSequence`, `truncated`, and `bridgeEpoch`; `native_page()` dispatches
through the structural `NativePageReader` protocol (fail-closed typed where the adapter does not
support it) and stamps the bridge epoch itself — an adapter-minted epoch is refused;
`submission_provenance()` delegates the epoch-checked batch to the command queue, the sole
bridge→authority path. The evidence sequence is the adapter event sequence and non-monotonic input
fails visibly.

The L2E `interrupt` dispatch is a single native write, never a queue entry: `_require_epoch`
compares the caller's expected epoch with the authority's and raises
`HarnessBridgeEpochMismatchError` on mismatch, `_require_running` gates lifecycle, and a structural
`isinstance(adapter, InterruptCapableAdapter)` check refuses unsupported harnesses typed, naming
the adapter type. The adapter returns an `InterruptResult`; a non-empty adapter-minted
`bridge_epoch` is refused and the bridge stamps its own epoch via `replace`. Settlement is
deliberately untouched — the interrupted operation still settles through the landed completion
path. `operation_timeline` delegates the epoch-checked paged read to the command queue under
`_require_running`, bounded by `MAX_OPERATION_TIMELINE_PAGE` and `EVIDENCE_PAGE_BYTE_BUDGET`.

### Conventions

The bridge is a lifecycle/state publisher; harness-specific set evidence belongs to the adapter and
generic evidence validation/ordering belongs to the queue.

### Invariants And Boundaries

- The bridge is control authority; pane content is never used to infer readiness or acceptance.
- Live advertise addresses this exact adapter instance; pre-session cached discovery is owned by a
  separate catalog and is never substituted here.
- A model/effort mutation cannot bypass the serialized queue or race a prompt accepted through this
  bridge.
- No automatic resend follows a disconnect after a possible send.
- Unsupported receipts use the bounded submission ledger and remain explicitly unsupported.
- The evidence buffer is evidence, not authority: it is a hot window with an explicit frame-count
  bound and an honest eviction floor on every page; deep history stays with the native read APIs.
- Evidence never rides the shared raw merge: the reserved key is diverted at the one consumption
  point and only the redacted event reaches reduction, the authority, the transcript, and
  subscribers.
- The bridge alone stamps `bridgeEpoch` on evidence responses; adapters never mint it.
- The interrupt write is epoch-guarded, bridge-stamped, and adapter-mint-epoch-refused; it never
  enters the prompt FIFO and never settles the operation — settlement stays with the landed
  completion path.
- A harness without the structural `InterruptCapableAdapter` seam is refused typed with the
  adapter named; the fail-closed posture is bridge-side (claude needs no edits).

### Todos

None known for the L4 bridge seam.

## Docs References

No Domain Documentation source is configured for this repository, so no live
domain-documentation pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The protocol owns vendor-specific setters; the queue owns order and result validation.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The adapter protocol requires both live setters and supplies explicit unsupported results when no adapter exists. | L33-L79; L151-L180 | [harness_control_adapter.py](agents-remember/mcp/src/agents_remember/serving/harness_control_adapter.py) |
| The queue facade serializes both setters and the timeline read through the authority. | L93-L197 | [harness_control_queue.py](agents-remember/mcp/src/agents_remember/serving/harness_control_queue.py) |
| Private IPC exposes bridge advertise/set actions under the same exact identity. | L150-L170; L220-L229 | [harness_control_ipc.py](agents-remember/mcp/src/agents_remember/serving/harness_control_ipc.py) |
| The evidence DTOs, reserved key, clip/window helpers, and structural native-page protocol live in the models module. | L57-L72; L385-L470; L569-L660 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |
| Contract tests pin diversion no-leak, buffer bounds, continuation, epoch mismatch, and the provenance delegation through this bridge. | L268-L791 | [test_harness_control_evidence.py](agents-remember/mcp/tests/test_harness_control_evidence.py) |
| The structural interrupt sub-protocol this bridge dispatches against, with identity guards riding the write. | L92-L115 | [harness_control_adapter.py](agents-remember/mcp/src/agents_remember/serving/harness_control_adapter.py) |
| The IPC server dispatches the interrupt and operation-timeline actions to this bridge over the private socket. | L212-L215; L302-L325 | [harness_control_ipc.py](agents-remember/mcp/src/agents_remember/serving/harness_control_ipc.py) |
| The validated client drives `interrupt_control`/`read_operation_timeline` with strict response validation against this bridge's stamps. | L398-L450 | [harness_control_client.py](agents-remember/mcp/src/agents_remember/serving/harness_control_client.py) |
| Contract tests pin the epoch guard, structural refusal naming the adapter, adapter-mint-epoch refusal, and the bridge-stamped epoch. | L252-L346 | [test_harness_control_plane.py](agents-remember/mcp/tests/test_harness_control_plane.py) |

## Cross-Repo References

No external repository boundary is implemented by the bridge.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

### 260713-PHA-L5 Shared Protocol Bridge

The bridge owns adapter lifecycle, exact identity, readiness, correlated immediate/queued/rejected/
unknown receipts, pending interactions, transcript completion, and graceful recovery. It retains
raw vendor detail as evidence without promoting pane diagnostics to authority.

## 260715-FEUI-L5 Submission Authority Delta

The bridge now exposes one epoch-bound authority facade for submit, reconcile, status, withdrawal,
model/effort sets, and exact operation resolution. Direct adapter completion events enter authority
before coalesced snapshot publication, preventing publication latency or loss from stranding the
active operation. Startup failure and graceful stop clean the same authority instance.

## Update History

- 2026-07-20T00:08+02:00 — 260718-CHATS-L2E curator: documented the epoch-guarded native
  `interrupt` dispatch (`_require_epoch` mismatch typed, structural `InterruptCapableAdapter`
  refusal naming the adapter, adapter-mint-epoch refusal, bridge-stamped epoch, settlement
  untouched on the landed completion path) and the `operation_timeline` read delegation; refreshed
  the adapter/queue/models/IPC citation ranges for the shifted sources (the queue row's pre-facade
  ranges were legacy-stale and now cite the current facade). Verification metadata stays pinned
  until closeout stamps the candidate commit.
- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: documented the bounded per-session evidence
  deque with reserved-key diversion at `_run_events` (redacted event to every existing consumer),
  the deque-domain `evidence()` page with eviction-floor honesty, the structural `native_page()`
  dispatch with bridge-stamped epoch, and the `submission_provenance()` delegation. Verification
  metadata stays pinned until closeout stamps the candidate commit.
- 2026-07-17T21:39+02:00 — FEUI-L5: documented the sole authority facade, exact operation routing,
  event-before-publish completion, and lifecycle cleanup.

- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: documented exact-running-adapter advertise
  beside the already ordered set, submit, and reconcile operations while keeping pre-session cache
  ownership separate.
- 2026-07-16T01:19+02:00 — 260714-ACPUI-L3 curator: documented bridge-level model/effort methods,
  their shared command ordering with prompts and interactions, and the adapter/queue ownership split.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: documented cross-adapter bridge lifecycle and receipt semantics.

- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator pass: created onboarding for the one-adapter
  bridge, handshake gate, ordered inputs, ambiguous-send recovery, and bounded lifecycle behavior.
