# mcp/src/agents_remember/serving/harness_control_bridge.py

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Hosts one exact harness identity, validates adapter handshake/capabilities, exposes one bounded
`HarnessSubmissionAuthority` for prompts, interactions, reconciliation, and model/effort mutations, and publishes
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
state. Per operation, `submissions()` applies that running-state check and returns the epoch-bound
`HarnessSubmissionAuthority`; the authority owns prompt/setter order, interaction responses,
reconciliation, stop, result validation, and ambiguous-send resolution. Submission receipts remain
distinct from terminal completion. Event reduction and transcript retention are bounded. Adapter
failures are classified by the authority: certified pre-send failures can requeue, while a possible
send or incoherent result installs the ambiguity blocker instead of guessing
cit:([`_send_and_settle`], mcp/src/agents_remember/serving/harness_submission_authority.py:700-727).

The evidence buffer is a bounded per-session deque (default 2000 frames, per-frame 32 KiB clip)
fed at the single `_run_events` event-consumption point: when an adapter event carries the reserved
`arEvidence` raw key, `_divert_evidence` cit:([`_divert_evidence`], mcp/src/agents_remember/serving/harness_control_bridge.py:468-489) appends an `EvidenceFrame(sequence, kind,
created_at, clipped payload, native_method, thread_id)` and the redacted event (raw minus BOTH reserved keys,
`{AR_EVIDENCE_KEY, AR_EVIDENCE_METHOD_KEY}` cit:([`AR_EVIDENCE_KEY`, `AR_EVIDENCE_METHOD_KEY`], mcp/src/agents_remember/models/conversations/evidence.py:17-17; mcp/src/agents_remember/models/conversations/evidence.py:26-26) flows to reduce/observe/transcript/publish, so
`snapshot.raw`, catalog `control_raw`, SSE projections, and every existing consumer stay
byte-identical. The out-of-band native method rides this same seam:
when the event also carries `AR_EVIDENCE_METHOD_KEY`, `_divert_evidence` validates it is non-empty
text (else raises) and preserves it on the frame as typed `native_method` cit:([`_divert_evidence`], mcp/src/agents_remember/serving/harness_control_bridge.py:468-489) so the
codex projector switches on the real method, then strips the extra reserved key so the redacted
snapshot stays byte-identical exactly as before. A third stamped field carries the multiplex demux key:
`_evidence_thread_id` cit:([`_evidence_thread_id`], mcp/src/agents_remember/serving/harness_control_bridge.py:491-503) reads the payload's `threadId` verbatim — codex notification
params carry it, parent frames carry the parent thread's id — and `_append_evidence` stamps it as
`thread_id` on every frame cit:([`_append_evidence`], mcp/src/agents_remember/serving/harness_control_bridge.py:505-528); anything present-but-not-non-empty-text degrades to `None`
(the parent/session thread, matching pre-multiplexing behavior) rather than being guessed. `evidence()` pages
the deque domain with count+byte bounds and reports
`latestSequence`, `evictedBeforeSequence`, `truncated`, and `bridgeEpoch`; `native_page()` dispatches
through the structural `NativePageReader` protocol (fail-closed typed where the adapter does not
support it) and stamps the bridge epoch itself — an adapter-minted epoch is refused;
Private IPC `_submission_provenance` reads the epoch-checked batch through the running-checked
authority and its ledger, the sole bridge-to-submission path. The evidence sequence is the adapter event sequence and non-monotonic input
fails visibly.

`native_page` is also optionally per-thread cit:([`native_page`], mcp/src/agents_remember/serving/harness_control_bridge.py:226-271): the additive `thread_id` kwarg is
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
path. Private IPC obtains the running-checked authority from `bridge.submissions()` and pages
`authority.ledger.operation_timeline`, bounded by `MAX_OPERATION_TIMELINE_PAGE` and
`EVIDENCE_PAGE_BYTE_BUDGET`.

### Conventions

The bridge is a lifecycle/state publisher; harness-specific set evidence belongs to the adapter,
ordinary-operation ordering/result validation belongs to `HarnessSubmissionAuthority`, and retained
operation rows plus provenance/timeline reads belong to its `SubmissionLedger`.

### Invariants And Boundaries

- The bridge is control authority; pane content is never used to infer readiness or acceptance.
- Live advertise addresses this exact adapter instance; pre-session cached discovery is owned by a
  separate catalog and is never substituted here.
- A model/effort mutation cannot bypass the authority's serialized ordinary-operation timeline or
  race a prompt accepted through this bridge.
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

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live
domain-documentation pass was available for this update.

No configured domain documentation could be checked.

### Repo-Internal References

The adapter protocol owns vendor-specific setter execution; `HarnessSubmissionAuthority` owns
ordinary-operation order and result validation, while `SubmissionLedger` owns retained rows and
timeline/provenance reads.

- The adapter protocol requires both live setters and supplies explicit unsupported results when no adapter exists. [1]
- The bridge exposes its running, epoch-bound "def submissions(self) -> HarnessSubmissionAuthority:" through `submissions()`. The authority owns ordinary-operation dispatch order and result validation, including "async def set_model(self" and "async def set_effort(self"; the bridge applies the running-state guard before each caller takes the authority. [2]
- The retained `SubmissionLedger` owns provenance and paged operation-timeline reads; private IPC reaches the timeline as `bridge.submissions().ledger.operation_timeline`. [3]
- Private IPC exposes bridge advertise/set actions under the same exact identity. [4]
- The evidence DTOs, reserved keys, clip/window helpers, and structural native-page protocol live in the models module; `AR_EVIDENCE_METHOD_KEY` + `EvidenceFrame.native_method` are the method-carry pair this divert preserves, alongside `EvidenceFrame.thread_id` (the demux key this bridge stamps) plus `AdapterSnapshot.pending_interactions` (the plural multiplexed set). [5]

| The structural interrupt sub-protocol this bridge dispatches against, with identity guards riding the write. | "class InterruptCapableAdapter(Protocol):"; """"Structural native interrupt write; adapters opt in without a base-contract member." | mcp/src/agents_remember/serving/harness_control_adapter.py:91-106; mcp/src/agents_remember/serving/harness_control_bridge.py:273-300 |
| The IPC server dispatches the interrupt and operation-timeline actions to this bridge over the private socket. | `HarnessControlServer`; `_interrupt`; `_operation_timeline` | mcp/src/agents_remember/serving/harness_control_ipc.py:99-412 |
| The validated client drives `interrupt_control`/`read_operation_timeline` with strict response validation against this bridge's stamps. | "def interrupt_control("; "opaque cursor coordinates are invalid in the operation timeline domain"; "def _interrupt_result("; "def _operation_timeline(" | mcp/src/agents_remember/serving/_harness_control_parsing.py:252-252; mcp/src/agents_remember/serving/harness_control_client.py:431-451; mcp/src/agents_remember/serving/harness_control_client.py:454-478; mcp/src/agents_remember/serving/_harness_control_parsing.py:277-277 |


### Cross-Repo References

No external repository boundary is implemented by the bridge.

No meaningful cross-repo references found.

#### Shared Protocol Bridge

The bridge owns adapter lifecycle, exact identity, readiness, correlated immediate/queued/rejected/
unknown receipts, pending interactions, transcript completion, and graceful recovery. It retains
raw vendor detail as evidence without promoting pane diagnostics to authority.

## Submission Authority Delta

The bridge now exposes one epoch-bound authority facade for submit, reconcile, status, withdrawal,
model/effort sets, and exact operation resolution. Direct adapter completion events enter authority
before coalesced snapshot publication, preventing publication latency or loss from stranding the
active operation. Startup failure and graceful stop clean the same authority instance.

## 260731-EFA-L2 Current Delta

**`BridgeLimits`** (`queue=64`, `transcript=1000`, `submission=256`, `subscriber_queue=16`,
`evidence=2000`, `evidence_frame_bytes=32 KiB`; module default `DEFAULT_BRIDGE_LIMITS`) replaces the
six independent bound arguments. The concept: **every bound one control bridge holds itself to,
chosen as one memory budget**. A bridge retains a transcript, an evidence window (capped in frames
AND in bytes per frame), an authority timeline, a submission ledger and a per-subscriber fan-out queue —
they are one decision, how much a single live session may hold, and raising any one alone silently
moves the process's real ceiling somewhere else. The default values are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.
