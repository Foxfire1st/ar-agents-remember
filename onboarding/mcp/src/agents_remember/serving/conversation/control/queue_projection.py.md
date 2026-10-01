# mcp/src/agents_remember/serving/conversation/control/queue_projection.py

## Governing Overview

[Structured conversation control overview](overview.md)

## Purpose

R2: the complete retained live prompt-queue projection over the L2E operation-timeline — every
retained prompt operation across all three sources with exact source/kind/phase/order truth, and
never a body. Terminal and durable rows expose identity fields only; only queued cockpit rows carry
the caller-bound withdrawalRef, the redacted identification preview, and the content digest.

## Code Commentary

### Logic

cit:([`operation_queue`], mcp/src/agents_remember/serving/conversation/control/queue_projection.py:47-78) pages the service's full timeline to union completeness through
`latestSequence`, filters to retained prompt rows, and projects each through cit:([`_queue_row`], mcp/src/agents_remember/serving/conversation/control/queue_projection.py:81-149).
Only rows whose `source == "cockpit"` and phase is queued mint a `CockpitQueueIdentity`: the
caller-bound `withdrawalRef`/`operationRef` (via `mint_ref` on the row `OperationIdentity`), the
`redacted_preview`, and the `payload_digest`. Preview and digest come from this authority's own
submit journal; a row the journal does not hold (submitted outside the typed L3 submit) honestly
reports empty held content — `redactedPreview: ""` and `_EMPTY_DIGEST` (the digest of empty),
identification copy never fabricated. cit:([`_LIVE_ROW_STATES`], mcp/src/agents_remember/serving/conversation/control/queue_projection.py:47-47) is `queued|dispatching|unknown`.
Set-model/set-effort control operations (substrate `source=None`) are **not** projected — the SC1
`OperationQueueItem` validator cannot represent them without inventing a source or forcing a
withdrawable cockpit block on a row the authority cannot withdraw — so the projection covers the
complete **prompt** queue they interleave with. Row and projection revisions are semantic and
monotonic (stable on no-change reads, bump on set/phase changes). Since 260718-CHATS-L5F R5 the
per-channel `channel.queue_rows` revision store is bounded: after writing a row, `_queue_row`
`move_to_end`s it and then evicts oldest keys while the store exceeds
`MAX_QUEUE_ROWS_PER_CHANNEL` with `popitem(last=False)`. An evicted key restarts at
revision 1 only if its `(kind, operation_id, sequence)` operation ever reappears; a settled
operation never reappears, so the bound is invisible to any live row and closes the prior
unbounded-`queue_rows` leak (the former L3 precision-note Todo).

### Conventions

The never-bodies rule and the "only queued cockpit rows are withdrawable" rule are enforced by the
SC1 `OperationQueueItem` contract validator, not just by this code. The projection never lies about
withdrawability: it would rather exclude a row the authority cannot withdraw than mint a false
cockpit block.

### Invariants And Boundaries

- Terminal/durable/non-cockpit prompt bodies never serialize; only queued cockpit rows expose a ref,
  preview, and digest.
- Empty-held preview/digest is the truthful statement "the daemon holds no content for this row",
  distinct from an empty draft by the digest-of-empty marker; recovery at withdraw is unaffected
  (the substrate's own payload carries the body).
- Setter rows stay visible in the contract grammar for a future SC1 ruling but are excluded from the
  projection (reviewer ACCEPTED; the SC1 admission is the recorded fallback).
- Union completeness is the join of pages through `latestSequence`; an epoch flip fails typed at the
  validated client.
- The `channel.queue_rows` revision store is bounded-by-construction at `MAX_QUEUE_ROWS_PER_CHANNEL`
  with oldest-first eviction; the bound only ever drops a key whose operation has settled and cannot
  reappear, so a live queued/dispatching row is never lost to eviction.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured; the queue contract is repository-owned.

No configured domain documentation was available.

### Repo-Internal References

The privacy grammar and setter-mint reality live in the contract and the authority; the timeline and
preview/digest transforms are the substrate and sibling module this projection composes.

- The `OperationQueueItem`/`CockpitQueueIdentity` privacy validator (source ∈ {cockpit,terminal,durable}; withdrawable cockpit block rule). [1]
- The authority-internal setter mint with no submission source (`source=None`). [2]
- The full-timeline paging seam and the submit journal this projection reads. [3]
- The payload digest and redacted preview are deterministic transforms. [4]
- The queue projection precomputes the empty-content digest. [5]
- Authorized cockpit rows use stored content or the empty fallback, then mint operation and withdrawal refs. [6]

### Cross-Repo References

No meaningful cross-repo references found.

No meaningful cross-repo references found.

## 260731-EFA-L2 Current Delta

The row builder now takes one `ControlScope` (service + authorization + session id + **verified**
epoch — see [service.py](service.py.md)) instead of four parallel arguments, and mints refs with
`RefBinding(authorization, ar_session_id, epoch)` + `RefTarget(identity=…)` instead of four keyword
arguments to `mint_ref`. The projected queue rows are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.
