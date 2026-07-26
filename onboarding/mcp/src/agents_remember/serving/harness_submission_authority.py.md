# mcp/src/agents_remember/serving/harness_submission_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_submission_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T21:59+02:00 |
| lastVerifiedCommitHash | `a401e3dba0bc6e9723451edbfdefb8d77c42945d` |
| lastVerifiedCommitDate | 2026-07-27T00:27:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving overview](overview.md)

## Purpose

Owns the authoritative, epoch-bound prompt/setter timeline for one live harness bridge. It is the
only component allowed to admit queued prompts, linearize withdrawal against dispatch, bind exact
adapter operations, and retain normalized lifecycle truth. One additive read-only provenance batch
rides over its existing per-operation records. The paged never-bodies `operation_timeline`
enumeration runs over the same retained ledger (with the eviction floor tracked at the sole pop
site), alongside the pre-tombstone withdrawal-recovery capture and the asset-carrying submit
channel (capability gate, dispatch routing, additive digest extension, and receipt `assetIds`
evidence). `respond` is multiplex-aware: interaction responses match against the parent-thread
singular pending slot OR the plural sub-agent pending tuple, with the active-operation guard kept
parent-only — parent-ness decided by the matched entry's own THREAD, so a concurrent parent
pending riding the plural tuple is guarded exactly like the singular slot.

## Code Commentary

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

The multiplex-aware `respond` (L276-L334) resolves an interaction response against TWO pending sets: the singular
`snapshot.pending_interaction` (the parent thread's OLDEST pending) and the plural
`snapshot.pending_interactions` (multiplexed entries, including concurrent parent-thread pendings
beyond the oldest — the adapter keeps a per-thread pending map). A response matching
neither raises the same typed `HarnessInteractionNotPendingError` as before — the not-pending
contract is unchanged, only the match set widened. Parent-ness is decided by the matched entry's
own thread, not by which slot carries it (L287-L301): a singular-slot match is parent, and a tuple
entry whose `raw.threadId` equals the snapshot's `vendor_session_id` is parent too, so a concurrent
parent pending riding the tuple gets the "active ordinary operation" guard (L306-L311) exactly like
the singular slot. Genuinely foreign (sub-agent) pendings own no parent operation, so their
responses cross to the adapter with `operation=None` (`replace(response, operation=operation)` at
L319) instead of being refused for lacking an active record. The `_responded_interactions` dedupe
and the post-response identity check apply uniformly to both classes.

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
mint counter), `evictedBeforeSequence` (tracked additively in `_make_ledger_room` at the sole
`_records.pop` site), `truncated`, and `bridgeEpoch`. Completeness is the union of pages through
`latestSequence`. The asset channel extends admission: `_payload_digest` covers canonical asset
identity only when assets are present (asset-free digests stay byte-identical), a non-
`AssetSubmitCapable` adapter receives an `unsupported` terminal receipt with the exact reason
before any dispatch, and the dispatcher routes asset requests to `submit_with_assets` (the raise
behind the admit gate is a loud invariant, never reachable — it stands as the
assert class). `_OperationRecord.assets` clears at exactly the tombstone moment text clears.
Withdrawal captures `WithdrawalRecovery(text, assets)` at the true queued → withdrawn transition
immediately before `_mark_terminal`, so the exact body crosses once inside the already
`cockpit_only` response and idempotent replays carry `recovery=None`. `_receipt` adds raw
`assetIds` only for asset-carrying records; asset-free receipts keep `raw={}` byte-identical.

### Invariants And Boundaries

- There is exactly one prompt/setter authority per bridge generation. Native queues, browser
  optimistic queues, and the legacy queue facade are not co-authorities.
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
  `_records.pop` site so no retained row is ever hidden.
- The recovery payload crosses exactly once, at the true queued → withdrawn transition before the
  tombstone fires; replays carry none, and the tombstone timing/class, `cockpit_only` hardcode,
  and epoch verification stay byte-preserved.
- The idempotence digest covers canonical asset identity only when assets are present; asset-free
  submissions keep byte-identical digests, and same-text-with-asset conflicts instead of silently
  deduping.
- Asset submissions on a non-capable adapter fail closed with an `unsupported` terminal receipt —
  never guessed, never dispatched; bounded daemon-side recovery retention is not this authority's
  obligation.
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Records, locks, idempotent admission, dispatch/withdraw, exact completion, retention, the timeline read, the recovery capture, and the entry-thread multiplexed respond. | L56-L1186 | [harness_submission_authority.py](harness_submission_authority.py) |
| The queue module is now only a compatibility facade over this authority. | — | [harness_control_queue.py](harness_control_queue.py) |
| The bridge wires direct adapter events here before coalesced publication. | — | [harness_control_bridge.py](harness_control_bridge.py) |
| The API exposes raw-free authority/status/withdrawal projections. | — | [harness_control_api.py](harness_control_api.py) |
| Dedicated tests exercise races, early completion, full-ref reuse, bounds, privacy, and epochs. | — | [../../../tests/test_harness_submission_authority.py](../../../tests/test_harness_submission_authority.py) |
| The evidence contract suite exercises the provenance batch end-to-end through bridge → queue → authority → IPC → validated client, including all three sources, not-found, epoch mismatch, and the 1..64 uniqueness bound. | L463-L791 | [test_harness_control_evidence.py](../../../tests/test_harness_control_evidence.py) |
| The control-plane contract suite exercises the timeline enumeration (all sources/kinds, paged union, eviction floor, 256-record budget edge), the asset channel (capability gate, digest conflict/dedupe, receipt `assetIds`), and the first-vs-replay recovery through this authority. | L773-L1010; L1175-L1268; L1397-L1473 | [test_harness_control_plane.py](../../../tests/test_harness_control_plane.py) |
| The common conformance suite pins the multiplexed respond: respond-without-parent-operation for agent entries, the entry-thread operation guard for concurrent parent tuple entries, and the plural pending serialization round-trips. | L752-L928 | [test_harness_control.py](../../../tests/test_harness_control.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The authority is internal to agents-remember's hosted-control bridge. | — | — |

## Queued Receipt Grace Delta

Submission authority now returns an honest queued receipt after a bounded dispatch-acceptance grace when a healthy native echo has not yet arrived. Later lifecycle evidence upgrades the state; a receipt alone is never treated as a completed turn.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Multiplex-Aware Respond Delta

`respond` now matches an interaction response against the union of the parent-thread singular pending and the multiplexed plural pending tuple. The active-operation guard became parent-only: sub-agent entries own no parent operation and cross with `operation=None`. Not-pending, already-responded, and post-response identity checks are unchanged and apply to both classes.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-07-26T21:59+02:00 — 260718-CHATS-L7R curator: recorded the entry-thread parent guard in
  `respond`: parent-ness is no longer which SLOT carries the entry (concurrent parent pendings
  beyond the singular slot's oldest ride the plural tuple now that the adapter keeps a per-thread
  pending map) — a tuple entry whose `raw.threadId` is the session's vendor thread gets the
  active-operation guard exactly like the singular slot, while genuinely foreign agent entries
  still cross with `operation=None`. Re-anchored the respond citations (L276-L334; guard
  L306-L311; `replace(response, …)` L319) and the whole-file row (L56-L1186), and added the
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
