# mcp/src/agents_remember/serving/harness_submission_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_submission_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-02T01:42+02:00 |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce` |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving overview](overview.md)

## Purpose

The authority owns ordered dispatch, the active operation, adapter invocation, admission, withdrawal,
asset routing, and recovery capture. Its `SubmissionLedger`, under the same lifecycle lock, owns
retained records, tombstones, eviction accounting, provenance, and timeline reads. `respond` is
multiplex-aware: interaction responses match against the parent-thread
singular pending slot OR the plural sub-agent pending tuple, with the active-operation guard kept
parent-only — parent-ness decided by the matched entry's own THREAD, so a concurrent parent
pending riding the plural tuple is guarded exactly like the singular slot.

## Code Commentary

### Construction: two named concepts, not six keywords

`HarnessSubmissionAuthority(adapter, port, limits, *, bridge_epoch=None)`.

- **`BridgeSnapshotPort`** (`clock`, `snapshot`, `set_snapshot`, `publish`) — how a bridge
  sub-component reads, replaces, publishes and timestamps **the one** snapshot. They travel as one
  value because reading through one accessor while replacing through another component's setter
  would publish transitions nobody else sees; the clock rides along because every published
  transition is stamped by the same one.
- **`SubmissionLimits`** (`timeline`, `ledger`, `dispatch_grace_seconds`) — the bounds of one
  authority. They are one bound, not two: the ledger retains settled records the timeline has
  already dropped, so a ledger shorter than its timeline cannot answer for the operations still in
  it. The constructor still refuses non-positive limits and `ledger < timeline` with
  `HarnessControlError`; that refusal is now the reason the two arrive together.

### Admission: `_unsupported_prompt_locked` is the single capability decision point

`submit` decomposes into three locked steps, in order:

1. `_pre_admission_receipt_locked` — the receipt the request is already owed before any record
   exists: the idempotent duplicate receipt (same source **and** payload digest; a different one
   under the same id is `HarnessRequestConflictError`), or the ledger-full `rejected` receipt.
2. `_enrol_prompt_locked` — register the admitted prompt as a queued `OperationRecord` and bind its
   request id, before it reaches the timeline.
3. `_unsupported_prompt_locked` — retire a prompt this hosted harness cannot carry at all. Two
   cases: the snapshot says `control == "unsupported"`, or the request carries assets and the
   adapter is not `AssetSubmitCapable`. The record is still created and marked terminal so the
   ledger can answer for the request id; what it never does is join the dispatch timeline.

That third step is **the** place capability is decided. It runs under the same lock that enrols the
record, against the one adapter the authority was constructed with (`self._adapter` is never
rebound — reconnect for Codex/pi replaces the transport under a fixed adapter, and no adapter in
this tree binds or drops `submit_with_assets` at runtime), so its answer still holds at dispatch.
A refusal here is clean and terminal — an `unsupported` receipt, the session untouched — whereas
refusing at dispatch could only produce an `unknown` ambiguity barrier, because by then the
authority can no longer say whether bytes crossed the wire. Do not add a second capability check
downstream; add to this one.

### Dispatch: `_dispatch_one` decomposed

`_dispatch_one` returns whether the dispatcher should look at the head again immediately rather than
wait for a wake (the head was released, or the claim went stale and the new head is unexamined). It
now reads as four named steps:

- `_dispatchable_head_locked` — the queued head this step may dispatch, or `None`.
- `_preflight_declined` — ask the adapter whether it can take the operation; `True` means stand
  down. A preflight sends no operation bytes, so busy/not-yet-connected simply leaves the record
  queued; an adapter that nonetheless claims it may have sent goes to
  `_unknown_after_preflight_claim`, which installs the ambiguity barrier and flips the snapshot to
  disconnected/unknown/unknown.
- `_claim_head_locked` — re-verify under the lock (timeline head, no active operation, still
  queued, same bridge epoch, snapshot still allows dispatch) and mark it `dispatching`. The
  preflight ran outside the lock, so anything that moved voids the claim.
- `_send_and_settle` — issue the claimed operation via `_invoke_adapter` and apply what came back.
  Every failure mode turns on what the adapter can certify: busy, or a disconnect proven pre-write,
  requeues safely; a disconnect that may have sent, any other exception, and an incoherent result
  all install the ambiguity barrier instead of guessing which side of the wire the bytes are on.

Receipt/result application is likewise split into `_verified_prompt_receipt` (read the adapter's
result as a receipt for exactly this operation, or a control error), `_accept_prompt_locked`,
`_complete_delivered_locked`, `_apply_prompt_receipt_locked` and `_apply_set_result_locked` — the
last two returning whether the head was released.

### Logic

`HarnessSubmissionAuthority` stores one ordered timeline for prompts, model sets, and effort sets.
Prompt FIFO lives here; adapters are dispatch-now transports and may not create a second hidden
queue. Admission checks epoch plus `(request id, source, payload digest)` idempotency, runs async
native preflight, then claims under the lifecycle lock. Each native operation receives the full
`ControlOperationRef` (`bridge epoch`, monotonic sequence, id, kind). Queued withdrawal and dispatch
claim are atomic competitors. Adapter completion is exact-ref and may arrive before the dispatch
receipt; such definitive completion dominates a later unknown observation. Response operations use
a bypass lane but share each adapter's write lock. Status/withdrawal read only normalized state and
never wait on vendor I/O while holding the lifecycle lock.

The multiplex-aware cit:([`respond`], mcp/src/agents_remember/serving/harness_submission_authority.py:300-356) resolves an interaction response against TWO pending sets: the singular
`snapshot.pending_interaction` (the parent thread's OLDEST pending) and the plural
`snapshot.pending_interactions` (multiplexed entries, including concurrent parent-thread pendings
beyond the oldest — the adapter keeps a per-thread pending map). A response matching
neither raises the same typed `HarnessInteractionNotPendingError` as before — the not-pending
contract is unchanged, only the match set widened. Parent-ness is decided by the matched entry's
own thread, not by which slot carries it: a singular-slot match is parent, and a tuple
entry whose `raw.threadId` equals the snapshot's `vendor_session_id` is parent too, so a concurrent
parent pending riding the tuple gets the "active ordinary operation" guard exactly like
the singular slot. Genuinely foreign (sub-agent) pendings own no parent operation, so their
responses cross to the adapter with `operation=None` via
cit:([`respond`, "replace(response, operation=operation)"], mcp/src/agents_remember/serving/harness_submission_authority.py:300-356)
instead of being refused for lacking an active record. The `_responded_interactions` dedupe and the
post-response identity check apply uniformly to both classes in that response path.

Retention is bounded (timeline 64, duplicate/terminal ledger 256 by the configured defaults): live,
active, and unknown rows are never evicted; terminal rows discard full prompt text while retaining
identity/digest truth. Full-ref completion dedupe prevents a reused request id or stale adapter event
from releasing a successor. Certified pre-dispatch busy may requeue safely; possible-first-byte
loss remains unknown and blocks later ordered work until exact resolution.

The `provenance(expected_bridge_epoch, request_ids)` read is a batch over those same
records: epoch-checked before disclosure, 1..64 unique request ids, and never origin-filtered —
each found id reports its exact `source` (`cockpit`/`terminal`/`durable`), `state`, submitted/
updated/accepted timestamps, and vendor correlation from the record; unknown ids answer an honest
`not-found` rather than a guessed row. The read holds the lifecycle lock only over normalized
record fields and mutates nothing.

The `operation_timeline(expected_bridge_epoch, *, after_sequence, limit, byte_budget)` read pages
those same records under the lifecycle lock: epoch-checked, positive limit/byte budget, items in
sequence order strictly after `afterSequence`, the greedy loop bounded by both
   `MAX_OPERATION_TIMELINE_PAGE` and the shared `EVIDENCE_PAGE_BYTE_BUDGET` (an oversized first item
   still makes progress; identity is never clipped), and every page carrying `latestSequence` (the
   mint counter), `evictedBeforeSequence` (tracked additively at the sole `SubmissionLedger.make_room`
   eviction site), `truncated`, and `bridgeEpoch`. Completeness is the union of pages through
`latestSequence`. The asset channel extends admission: `_payload_digest` covers canonical asset
identity only when assets are present (asset-free digests stay byte-identical), a non-
`AssetSubmitCapable` adapter receives an `unsupported` terminal receipt with the exact reason
before any dispatch (`_unsupported_prompt_locked`), and `_invoke_adapter` routes asset requests to
`submit_with_assets`. The old defensive re-check there — a `HarnessControlError("asset submission
dispatch reached a non-capable adapter")` — is now literally `assert isinstance(capable,
AssetSubmitCapable)`, because it was always the assert class: it can only fire if the admission gate
above it stopped deciding. `OperationRecord.assets` clears at exactly the tombstone moment text clears.
Withdrawal captures `WithdrawalRecovery(text, assets)` at the true queued → withdrawn transition
immediately before `_mark_terminal`, so the exact body crosses once inside the already
`cockpit_only` response and idempotent replays carry `recovery=None`. `_receipt` adds raw
`assetIds` only for asset-carrying records; asset-free receipts keep `raw={}` byte-identical.

### Invariants And Boundaries

- There is exactly one prompt/setter authority per bridge generation. Native queues and browser
  optimistic queues are not co-authorities.
- A request id is idempotent only for the same source and payload digest; conflicting reuse is 409.
- Epoch mismatch is rejected before mutation or lifecycle disclosure.
- Withdrawal can succeed only while the row is authoritatively queued; dispatching/delivered work
  cannot be pulled back by inference.
- Completion must carry the full operation ref. Id-only or FIFO completion is forbidden.
- Public status is cockpit-only, raw-free, and bounded; private authority may retain internal
  correlation but not unbounded terminal text.
- The provenance batch discloses submission source only to the exact-session daemon peer over the
  private socket; it is a read, never a mutation channel, and never infers a source the record
  does not carry.
- The operation timeline never carries bodies — identity/source/kind/sequence/state/timestamps,
  digest-presence, and vendor correlation only; completeness is the union of pages through
  `latestSequence`, and the eviction floor disclosed on every page is tracked at the sole
  `SubmissionLedger.make_room` site so no retained row is ever hidden.
- The recovery payload crosses exactly once, at the true queued → withdrawn transition before the
  tombstone fires; replays carry none, and the tombstone timing/class, `cockpit_only` hardcode,
  and epoch verification stay byte-preserved.
- The idempotence digest covers canonical asset identity only when assets are present; asset-free
  submissions keep byte-identical digests, and same-text-with-asset conflicts instead of silently
  deduping.
- Asset submissions on a non-capable adapter fail closed with an `unsupported` terminal receipt —
  never guessed, never dispatched; bounded daemon-side recovery retention is not this authority's
  obligation. `_unsupported_prompt_locked` is the ONE place that decision is made; `_invoke_adapter`
  only asserts it, and must not grow a second runtime check.
- An interaction response must match a CURRENTLY pending entry — the singular parent slot or the
  plural multiplexed tuple; anything else is the same typed not-pending error as
  before multiplexing, and the already-responded dedupe covers both classes.
- The active-operation guard in `respond` is parent-only BY ENTRY THREAD: parent-ness is the
  singular slot match OR a tuple entry whose `raw.threadId` is the session's vendor thread (a
  concurrent parent pending riding the tuple is guarded exactly like the singular slot); genuinely
  foreign sub-agent pendings own no parent operation, so their responses carry `operation=None` to
  the adapter rather than inventing or borrowing an operation ref.

### Todos

None known.

## Docs References

No Domain Documentation source is configured for this repository; the authority protocol is
repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Locks, idempotent admission, dispatch/withdraw, exact completion, the recovery capture, and the entry-thread multiplexed respond. | `HarnessSubmissionAuthority` | mcp/src/agents_remember/serving/harness_submission_authority.py:116-1023 |
| The records, the retention and the timeline read named in the old single-row claim are no longer in this module: 260731-EFA-L6 split `OperationRecord` and `SubmissionLedger` into their own file, which is where enrolment, eviction (`make_room`) and `operation_timeline` now live. | `OperationRecord`; `SubmissionLedger` | mcp/src/agents_remember/serving/harness_submission_ledger.py:57-252; mcp/src/agents_remember/serving/harness_submission_ledger.py:255-437 |
| The bridge wires direct adapter events here before coalesced publication. | `_run_events` | mcp/src/agents_remember/serving/harness_control_bridge.py:415-458 |
| The API registers the submission-ledger routes. | `_register_submission_ledger_routes` | mcp/src/agents_remember/serving/harness_control_api.py:301-339 |
| The API exposes the submission-authority route. | `api_submission_authority` | mcp/src/agents_remember/serving/harness_control_api.py:306-316 |
| The status serializer produces the raw-free submission batch. | `submission_status_batch_json` | mcp/src/agents_remember/serving/harness_control_models.py:987-991 |
| The status wire model carries the raw-free batch projection. | `SubmissionStatusBatchWire` | mcp/src/agents_remember/serving/response_contract.py:952-956 |
| The public receipt wire preserves the raw-free response shape. | `PublicReceiptWire` | mcp/src/agents_remember/serving/response_contract.py:986-995 |
| Dedicated tests exercise races, early completion, full-ref reuse, bounds, privacy, and epochs. | `HarnessSubmissionAuthorityTests`; `SubmissionLedgerTests` | mcp/tests/test_harness_submission_authority.py:230-755; mcp/tests/test_harness_submission_authority.py:758-926 |
| The evidence contract suite exercises provenance end-to-end through bridge → authority → IPC → validated client, including all three sources, not-found, epoch mismatch, and the 1..64 unique-id bound. | `test_submission_provenance_all_sources_epoch_and_bounds` | mcp/tests/test_harness_control_evidence_ipc.py:229-312 |
| The control-plane contract suite exercises the timeline enumeration (all sources/kinds, paged union, eviction floor, 256-record budget edge), the asset channel (capability gate, digest conflict/dedupe, receipt `assetIds`), and the first-vs-replay recovery through this authority. | `OperationTimelineTests`; `AssetChannelTests`; `AssetNativeConstructionTests`; "class WithdrawalRecoveryTests(unittest.IsolatedAsyncioTestCase):" | mcp/tests/test_harness_control_plane_assets.py:249-483; mcp/tests/test_harness_control_plane_channels.py:52-318; mcp/tests/test_harness_control_plane_channels.py:321-481; mcp/tests/test_harness_control_plane_recovery.py:32-32 |
| The common conformance suite pins the multiplexed respond: respond-without-parent-operation for agent entries, the entry-thread operation guard for concurrent parent tuple entries, and the plural pending serialization round-trips. | `test_subagent_pending_interaction_responds_without_parent_operation`; `test_parent_thread_tuple_entry_gets_the_operation_guard`; `test_multiplexed_pending_interactions_serialize_through_every_surface` | mcp/tests/test_harness_control_conformance_1.py:437-491; mcp/tests/test_harness_control_conformance_1.py:493-551; mcp/tests/test_harness_control_conformance_1.py:553-612 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| The authority is internal to agents-remember's hosted-control bridge. | — | — |

## Queued Receipt Grace Delta

Submission authority now returns an honest queued receipt after a bounded dispatch-acceptance grace when a healthy native echo has not yet arrived. Later lifecycle evidence upgrades the state; a receipt alone is never treated as a completed turn.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Multiplex-Aware Respond Delta

`respond` now matches an interaction response against the union of the parent-thread singular pending and the multiplexed plural pending tuple. The active-operation guard became parent-only: sub-agent entries own no parent operation and cross with `operation=None`. Not-pending, already-responded, and post-response identity checks are unchanged and apply to both classes.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-04T15:32:44+02:00 — 260731-EFA-L6 S18-B08 curator: rebound the operation-none and dedupe/identity claim to the complete `respond` body, including the operative adapter replacement.

- 2026-08-02T01:42+02:00 — 260731-EFA-L6 deleted-source cleanup. `serving/harness_control_queue.py` was deleted outright by the L6 class-split work (a pure forwarding facade), and its mirrored sidecar was removed with it. **Curator's judgement, stated rather than assumed: the card had no subject left.** Every invariant it carried was either the facade's own NON-behavior ("cannot enqueue work behind the authority", "holds no facade state, mutates nothing") or was explicitly attributed to `harness_submission_authority.py`, so nothing moved with the deletion and no knowledge needed rehoming — which is also why no replacement card was manufactured. Present-tense claims that `HarnessControlQueue` "is a facade" were corrected here to say it no longer exists; dated history entries naming it are preserved verbatim. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T01:42+02:00 — 260731-EFA-L6 debt this leaf created, now cleared: three L6 workers split six oversized `serving/` classes while this memory tree was being edited, and every line range in this document that pointed into them went out of bounds the instant the sources shrank (`citation_range_out_of_bounds`). Ranges were re-derived by READING the cited construct at its current location, never by scaling or subtracting a delta — the splits moved code between files rather than shifting it uniformly. Where a construct left the file the row names, the Source Path moved with the range into its own row rather than being silently re-pointed. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded the `BridgeSnapshotPort` / `SubmissionLimits`
  constructor concepts, the three-step locked admission (`_pre_admission_receipt_locked`,
  `_enrol_prompt_locked`, `_unsupported_prompt_locked` as the single capability decision point),
  the four-step `_dispatch_one` decomposition, and the reduction of the dispatch-side capability
  re-check to an assert. Verification metadata stays pinned until closeout.
- 2026-07-26T21:59+02:00 — 260718-CHATS-L7R curator: recorded the entry-thread parent guard in
  `respond`: parent-ness is no longer which SLOT carries the entry (concurrent parent pendings
  beyond the singular slot's oldest ride the plural tuple now that the adapter keeps a per-thread
  pending map) — a tuple entry whose `raw.threadId` is the session's vendor thread gets the
  active-operation guard exactly like the singular slot, while genuinely foreign agent entries
  still cross with `operation=None`. Re-anchored the respond behavior to cit:([`respond`], mcp/src/agents_remember/serving/harness_submission_authority.py:300-356) and added the
  conformance-suite row. Verification metadata stays pinned to the pre-commit source history until
  closeout (the change is uncommitted).
- 2026-07-26T15:34 — 260718-CHATS-L7 curator: documented the multiplex-aware `respond` — match
  against singular parent pending OR plural sub-agent tuple, parent-only active-operation guard,
  `operation=None` for sub-agent responses, unchanged not-pending/dedupe/identity checks — in
  Purpose, Logic, and Invariants. Verification metadata stays pinned to the pre-commit source
  history until closeout (the L7 change is uncommitted).
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-20T00:08+02:00 — 260718-CHATS-L2E curator: documented the paged never-bodies
  `operation_timeline` enumeration (count+budget greedy loop, `latestSequence`, the eviction floor
  tracked at the sole pop site, epoch-checked), the pre-tombstone `WithdrawalRecovery` capture at
  the true transition only, and the asset channel (capability gate with `unsupported` receipt,
  `submit_with_assets` dispatch routing, asset-conditional digest extension, additive receipt
  `assetIds`, assets tombstoned with text). Verification metadata stays pinned until closeout
  stamps the candidate commit.
- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: documented the additive read-only
  `provenance` batch — epoch-checked disclosure of exact source/state/timestamps/vendor-correlation
  for all three submission sources from the existing records, 1..64 unique ids, honest not-found,
  and no mutation surface. Verification metadata stays pinned until closeout stamps the candidate
  commit.
- 2026-07-17T21:39+02:00 — Created for 260715-FEUI-L5 after canonical review PASS; documented the
  sole epoch-bound prompt/setter timeline, atomic dispatch/withdrawal, full operation references,
  early-completion dominance, safe-retry certificate boundary, bounded privacy-aware retention, and
  the removal of adapter/native queue authority. Verification metadata remains pinned to the leaf
  base until closeout stamps the code commit.
