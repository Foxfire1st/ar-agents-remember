# mcp/src/agents_remember/serving/harness_submission_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_submission_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T00:08+02:00 |
| lastVerifiedCommitHash | `22562e0f2161c2d980385a462275dc370deb72eb` |
| lastVerifiedCommitDate | 2026-07-20T00:45:01+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving overview](overview.md)

## Purpose

Owns the FEUI-L5 authoritative, epoch-bound prompt/setter timeline for one live harness bridge. It
is the only component allowed to admit queued prompts, linearize withdrawal against dispatch, bind
exact adapter operations, and retain normalized lifecycle truth. 260718-CHATS-L0E adds one
additive read-only provenance batch over its existing per-operation records. 260718-CHATS-L2E adds
the paged never-bodies `operation_timeline` enumeration over the same retained ledger (with the
eviction floor tracked at the sole pop site), the pre-tombstone withdrawal-recovery capture, and
the asset-carrying submit channel (capability gate, dispatch routing, additive digest extension,
and receipt `assetIds` evidence).

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

Retention is bounded (timeline 64, duplicate/terminal ledger 256 by the configured defaults): live,
active, and unknown rows are never evicted; terminal rows discard full prompt text while retaining
identity/digest truth. Full-ref completion dedupe prevents a reused request id or stale adapter event
from releasing a successor. Certified pre-dispatch busy may requeue safely; possible-first-byte
loss remains unknown and blocks later ordered work until exact resolution.

L0E's `provenance(expected_bridge_epoch, request_ids)` is a read-only batch over those same
records: epoch-checked before disclosure, 1..64 unique request ids, and never origin-filtered —
each found id reports its exact `source` (`cockpit`/`terminal`/`durable`), `state`, submitted/
updated/accepted timestamps, and vendor correlation from the record; unknown ids answer an honest
`not-found` rather than a guessed row. The read holds the lifecycle lock only over normalized
record fields and mutates nothing.

L2E's `operation_timeline(expected_bridge_epoch, *, after_sequence, limit, byte_budget)` pages
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
behind the admit gate is a loud invariant, never reachable — the reviewer accepted it as the
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
  never guessed, never dispatched; daemon-side bounded recovery retention is L3's obligation, not
  this authority's.

### Todos

None for FEUI-L5 after review round 6 PASS.

## Docs References

No Domain Documentation source is configured for this repository; the authority protocol is
repository-owned.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Records, locks, idempotent admission, dispatch/withdraw, exact completion, retention, the timeline read, and the recovery capture. | L56-L1098 | [harness_submission_authority.py](harness_submission_authority.py) |
| The queue module is now only a compatibility facade over this authority. | — | [harness_control_queue.py](harness_control_queue.py) |
| The bridge wires direct adapter events here before coalesced publication. | — | [harness_control_bridge.py](harness_control_bridge.py) |
| The API exposes raw-free authority/status/withdrawal projections. | — | [harness_control_api.py](harness_control_api.py) |
| Dedicated tests exercise races, early completion, full-ref reuse, bounds, privacy, and epochs. | — | [../../../tests/test_harness_submission_authority.py](../../../tests/test_harness_submission_authority.py) |
| The evidence contract suite exercises the provenance batch end-to-end through bridge → queue → authority → IPC → validated client, including all three sources, not-found, epoch mismatch, and the 1..64 uniqueness bound. | L463-L791 | [test_harness_control_evidence.py](../../../tests/test_harness_control_evidence.py) |
| The control-plane contract suite exercises the timeline enumeration (all sources/kinds, paged union, eviction floor, 256-record budget edge), the asset channel (capability gate, digest conflict/dedupe, receipt `assetIds`), and the first-vs-replay recovery through this authority. | L773-L1010; L1175-L1268; L1397-L1473 | [test_harness_control_plane.py](../../../tests/test_harness_control_plane.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The authority is internal to agents-remember's hosted-control bridge. | — | — |

## Update History

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
