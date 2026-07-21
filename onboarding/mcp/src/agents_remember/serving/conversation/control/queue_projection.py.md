# mcp/src/agents_remember/serving/conversation/control/queue_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/queue_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash |  `38c3fd81bdf851dce96e9b2b14e2bff741e7b383`|
| lastVerifiedCommitDate |  2026-07-21T11:31:07+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structured conversation control overview](overview.md)

## Purpose

R2: the complete retained live prompt-queue projection over the L2E operation-timeline — every
retained prompt operation across all three sources with exact source/kind/phase/order truth, and
never a body. Terminal and durable rows expose identity fields only; only queued cockpit rows carry
the caller-bound withdrawalRef, the redacted identification preview, and the content digest.

## Code Commentary

### Logic

`operation_queue` (L40) pages the service's full timeline to union completeness through
`latestSequence`, filters to retained prompt rows, and projects each through `_queue_row` (L74).
Only rows whose `source == "cockpit"` and phase is queued mint a `CockpitQueueIdentity`: the
caller-bound `withdrawalRef`/`operationRef` (via `mint_ref` on the row `OperationIdentity`), the
`redacted_preview`, and the `payload_digest`. Preview and digest come from this authority's own
submit journal; a row the journal does not hold (submitted outside the typed L3 submit) honestly
reports empty held content — `redactedPreview: ""` and `_EMPTY_DIGEST` (L37, the digest of empty),
identification copy never fabricated. `_LIVE_ROW_STATES` (L36) is `queued|dispatching|unknown`.
Set-model/set-effort control operations (substrate `source=None`) are **not** projected — the SC1
`OperationQueueItem` validator cannot represent them without inventing a source or forcing a
withdrawable cockpit block on a row the authority cannot withdraw — so the projection covers the
complete **prompt** queue they interleave with. Row and projection revisions are semantic and
monotonic (stable on no-change reads, bump on set/phase changes). Since 260718-CHATS-L5F R5 the
per-channel `channel.queue_rows` revision store is bounded: after writing a row (L97) `_queue_row`
`move_to_end`s it (L101) and then evicts oldest keys while the store exceeds
`MAX_QUEUE_ROWS_PER_CHANNEL` (L102-L103, `popitem(last=False)`). An evicted key restarts at
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

## Docs References

No Domain Documentation source is configured; the queue contract is repository-owned.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The privacy grammar and setter-mint reality live in the contract and the authority; the timeline and
preview/digest transforms are the substrate and sibling module this projection composes.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The `OperationQueueItem`/`CockpitQueueIdentity` privacy validator (source ∈ {cockpit,terminal,durable}; withdrawable cockpit block rule). | L931-L949 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| The authority-internal setter mint with no submission source (`source=None`). | L541-L543 | [harness_submission_authority.py](agents-remember/mcp/src/agents_remember/serving/harness_submission_authority.py) |
| The full-timeline paging seam and the submit journal this projection reads. | L236-L266 | [service.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/service.py) |
| The preview/digest transforms and the ref mint used on cockpit rows. | L28-L64 | [previews.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/previews.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: R5 bound — documented the new
  `MAX_QUEUE_ROWS_PER_CHANNEL=256` cap on `channel.queue_rows` with oldest-first `popitem` eviction
  in `_queue_row`; an evicted key restarts at revision 1 only if a settled operation reappears (it
  never does), so the bound is invisible to live rows and closes the prior unbounded-`queue_rows`
  precision-note Todo. Change uncommitted; closeout re-stamps verification.
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the source-aware queue
  projection — complete never-bodies prompt-queue truth, cockpit-only withdrawal refs/previews/
  digests, journal-backed empty-held honesty, and the accepted setter-row exclusion. Verification is
  blank because the new source file is uncommitted; closeout owns its first source stamp.
