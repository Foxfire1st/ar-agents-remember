# mcp/src/agents_remember/serving/harness_submission_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_submission_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T09:15+02:00 |
| lastVerifiedCommitHash | `ca9dd05a295ef5f24c479e2231fdcd174b372e04` |
| lastVerifiedCommitDate | 2026-07-19T10:04:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving overview](overview.md)

## Purpose

Owns the FEUI-L5 authoritative, epoch-bound prompt/setter timeline for one live harness bridge. It
is the only component allowed to admit queued prompts, linearize withdrawal against dispatch, bind
exact adapter operations, and retain normalized lifecycle truth. 260718-CHATS-L0E adds one
additive read-only provenance batch over its existing per-operation records.

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
| Records, locks, idempotent admission, dispatch/withdraw, exact completion, and retention. | L56-L926 | [harness_submission_authority.py](harness_submission_authority.py) |
| The queue module is now only a compatibility facade over this authority. | — | [harness_control_queue.py](harness_control_queue.py) |
| The bridge wires direct adapter events here before coalesced publication. | — | [harness_control_bridge.py](harness_control_bridge.py) |
| The API exposes raw-free authority/status/withdrawal projections. | — | [harness_control_api.py](harness_control_api.py) |
| Dedicated tests exercise races, early completion, full-ref reuse, bounds, privacy, and epochs. | — | [../../../tests/test_harness_submission_authority.py](../../../tests/test_harness_submission_authority.py) |
| The evidence contract suite exercises the provenance batch end-to-end through bridge → queue → authority → IPC → validated client, including all three sources, not-found, epoch mismatch, and the 1..64 uniqueness bound. | L463-L791 | [test_harness_control_evidence.py](../../../tests/test_harness_control_evidence.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The authority is internal to agents-remember's hosted-control bridge. | — | — |

## Update History

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
