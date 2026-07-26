# mcp/src/agents_remember/serving/harness_control_bridge.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_bridge.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:34 |
| lastVerifiedCommitHash | `4e5fbcf872bbc1ec2566a6ccb17276a6bad80c7f` |
| lastVerifiedCommitDate | 2026-07-26T18:40:37+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Hosts one exact harness identity, validates adapter handshake/capabilities, serializes prompts,
interactions, reconciliation, and model/effort mutations through one bounded queue, and publishes
normalized snapshots/transcripts. A bounded per-session native evidence buffer sits beside the
untouched transcript path, plus deque-domain/native-domain evidence page reads and the
submission-provenance batch read. The epoch-guarded native `interrupt` write dispatch
(bridge-stamped epoch, adapter-mint epoch refused, settlement untouched) and the
`operation_timeline` read delegation are also served here. A diverted notification's native method
is threaded onto the evidence frame as typed `native_method` and its reserved raw key stripped so
the redacted snapshot stays byte-identical. Each evidence frame is stamped with the multiplex demux
key `thread_id` extracted from the payload's `threadId`, and `native_page` is optionally per-thread
for multiplexed adapters.

## Code Commentary

### Logic

Start refuses identity, protocol, readiness, or capability mismatches and force-cleans a rejected
adapter. `advertise` reads the already-running exact adapter instance and refuses outside running
state. `set_model` and `set_effort` require that same running bridge and delegate to the command queue
as prompt submission, interaction response, reconciliation, and stop. Submission receipts remain
distinct from terminal completion; reconciliation and explicit unknown resolution handle ambiguous
sends. Event reduction and transcript retention are bounded. Unexpected queue failures publish a
loud failed state, resolve active callers, and drain queued commands.

The evidence buffer is a bounded per-session deque (default 2000 frames, per-frame 32 KiB clip)
fed at the single `_run_events` event-consumption point: when an adapter event carries the reserved
`arEvidence` raw key, `_divert_evidence` (L521-L544) appends an `EvidenceFrame(sequence, kind,
created_at, clipped payload, native_method, thread_id)` and the redacted event (raw minus BOTH reserved keys,
`{AR_EVIDENCE_KEY, AR_EVIDENCE_METHOD_KEY}` at L540) flows to reduce/observe/transcript/publish, so
`snapshot.raw`, catalog `control_raw`, SSE projections, and every existing consumer stay
byte-identical. The out-of-band native method rides this same seam:
when the event also carries `AR_EVIDENCE_METHOD_KEY`, `_divert_evidence` validates it is non-empty
text (L532-L536, else raises) and preserves it on the frame as typed `native_method` (L537-L539) so the
codex projector switches on the real method, then strips the extra reserved key so the redacted
snapshot stays byte-identical exactly as before. A third stamped field carries the multiplex demux key:
`_evidence_thread_id` (L546-L558) reads the payload's `threadId` verbatim — codex notification
params carry it, parent frames carry the parent thread's id — and `_append_evidence` stamps it as
`thread_id` on every frame (L581); anything present-but-not-non-empty-text degrades to `None`
(the parent/session thread, matching pre-multiplexing behavior) rather than being guessed. `evidence()` pages
the deque domain with count+byte bounds and reports
`latestSequence`, `evictedBeforeSequence`, `truncated`, and `bridgeEpoch`; `native_page()` dispatches
through the structural `NativePageReader` protocol (fail-closed typed where the adapter does not
support it) and stamps the bridge epoch itself — an adapter-minted epoch is refused;
`submission_provenance()` delegates the epoch-checked batch to the command queue, the sole
bridge→authority path. The evidence sequence is the adapter event sequence and non-monotonic input
fails visibly.

`native_page` is also optionally per-thread (L209-L254): the additive `thread_id` kwarg is
forwarded to `adapter.read_native_page` only when present, so the structural `NativePageReader`
protocol and every single-thread adapter keep their exact signature; an adapter that rejects the
additive kwarg (`TypeError`) surfaces a typed `HarnessControlError` naming the adapter and stating
it does not support per-thread native pages — never a silent fallback to the wrong thread. The
bridge-stamped epoch discipline is unchanged on both paths.

The `interrupt` dispatch is a single native write, never a queue entry: `_require_epoch`
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
- Evidence never rides the shared raw merge: the reserved key(s) are diverted at the one
  consumption point and only the redacted event reaches reduction, the authority, the transcript,
  and subscribers.
- The native method rides the same divert-and-strip discipline as the payload: it is preserved
  onto the frame as typed `native_method` and its reserved raw key removed from the republished
  event, so the byte-identical snapshot guarantee holds; a present-but-non-string or empty method
  fails visibly rather than being silently carried.
- The bridge alone stamps `bridgeEpoch` on evidence responses; adapters never mint it.
- The interrupt write is epoch-guarded, bridge-stamped, and adapter-mint-epoch-refused; it never
  enters the prompt FIFO and never settles the operation — settlement stays with the landed
  completion path.
- A harness without the structural `InterruptCapableAdapter` seam is refused typed with the
  adapter named; the fail-closed posture is bridge-side (claude needs no edits).
- The evidence `thread_id` is extracted, never inferred: a missing or malformed
  (non-text) `threadId` degrades to `None` = the parent/session thread, and only a consumer that
  knows the session thread (the projector's identity) may classify frames further.
- `native_page(thread_id=…)` is forwarded only when set; an adapter without the additive kwarg is
  refused typed ("does not support per-thread native pages"), so a per-thread read can never
  silently return the parent thread's page.

### Todos

None known for the bridge seam.

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
| The evidence DTOs, reserved keys, clip/window helpers, and structural native-page protocol live in the models module; `AR_EVIDENCE_METHOD_KEY` + `EvidenceFrame.native_method` are the method-carry pair this divert preserves, alongside `EvidenceFrame.thread_id` (the demux key this bridge stamps) plus `AdapterSnapshot.pending_interactions` (the plural multiplexed set). | L57-L76; L217-L227; L456-L478; L534-L544; L770-L790 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |
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

### Shared Protocol Bridge

The bridge owns adapter lifecycle, exact identity, readiness, correlated immediate/queued/rejected/
unknown receipts, pending interactions, transcript completion, and graceful recovery. It retains
raw vendor detail as evidence without promoting pane diagnostics to authority.

## Submission Authority Delta

The bridge now exposes one epoch-bound authority facade for submit, reconcile, status, withdrawal,
model/effort sets, and exact operation resolution. Direct adapter completion events enter authority
before coalesced snapshot publication, preventing publication latency or loss from stranding the
active operation. Startup failure and graceful stop clean the same authority instance.

## Update History

- 2026-07-26T15:34 — 260718-CHATS-L7 curator: documented the multiplex demux key — `_evidence_thread_id`
  extracts `threadId` verbatim (missing/malformed degrades to `None` = parent, never guessed) and
  `_append_evidence` stamps it as `EvidenceFrame.thread_id` — and the additive per-thread
  `native_page(thread_id=…)` forwarding (present-only forwarding, `TypeError` refused typed naming
  the adapter, bridge-stamped epoch unchanged). Refreshed the `_divert_evidence` line ranges
  (L521-L544, validation L532-L536) and the models citation ranges for the L7-shifted source.
  Verification metadata stays pinned until closeout stamps the candidate commit.
- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: R1 — documented `_divert_evidence`'s
  native-method thread: the diverted event's `AR_EVIDENCE_METHOD_KEY` is validated non-empty text,
  preserved onto the frame as typed `native_method`, and its reserved key stripped alongside
  `AR_EVIDENCE_KEY` so the redacted snapshot stays byte-identical; refreshed the divert line ranges
  and the models citation. Verification metadata stays pinned until closeout stamps the candidate
  commit.
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
