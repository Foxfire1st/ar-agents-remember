# mcp/src/agents_remember/serving/conversation/control/queue_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/queue_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash |  `a3e43cb0877c18b9d2b0e6ada4eb5719a01f251f`|
| lastVerifiedCommitDate |  2026-08-06T05:49:07+02:00|
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

cit:([`operation_queue`], mcp/src/agents_remember/serving/conversation/control/queue_projection.py:47-78) pages the service's full timeline to union completeness through
`latestSequence`, filters to retained prompt rows, and projects each through cit:([`_queue_row`], mcp/src/agents_remember/serving/conversation/control/queue_projection.py:81-149).
Only rows whose `source == "cockpit"` and phase is queued mint a `CockpitQueueIdentity`: the
caller-bound `withdrawalRef`/`operationRef` (via `mint_ref` on the row `OperationIdentity`), the
`redacted_preview`, and the `payload_digest`. Preview and digest come from this authority's own
submit journal; a row the journal does not hold (submitted outside the typed L3 submit) honestly
reports empty held content — `redactedPreview: ""` and `_EMPTY_DIGEST` (the digest of empty),
identification copy never fabricated. cit:([`_LIVE_ROW_STATES`], mcp/src/agents_remember/serving/conversation/control/queue_projection.py:43-43) is `queued|dispatching|unknown`.
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

## Docs References

No Domain Documentation source is configured; the queue contract is repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The privacy grammar and setter-mint reality live in the contract and the authority; the timeline and
preview/digest transforms are the substrate and sibling module this projection composes.

| Finding | Anchor | Source |
| --- | --- | --- |
| The `OperationQueueItem`/`CockpitQueueIdentity` privacy validator (source ∈ {cockpit,terminal,durable}; withdrawable cockpit block rule). | `CockpitQueueIdentity`; `OperationQueueItem` | mcp/src/agents_remember/serving/conversation/models.py:963-967; mcp/src/agents_remember/serving/conversation/models.py:970-988 |
| The authority-internal setter mint with no submission source (`source=None`). | `_admit_setter` | mcp/src/agents_remember/serving/harness_submission_authority.py:561-594 |
| The full-timeline paging seam and the submit journal this projection reads. | `read_full_timeline`; `ControlChannel` | mcp/src/agents_remember/serving/conversation/control/service.py:199-219; mcp/src/agents_remember/serving/conversation/control/service.py:320-341 |
| The payload digest and redacted preview are deterministic transforms. | "def payload_digest("; "return f\"sha256:{sha256(text.encode('utf-8')).hexdigest()}\""; "return f\"sha256:{sha256(canonical.encode('utf-8')).hexdigest()}\""; "def redacted_preview("; "redacted = str(redact_secrets(collapsed))"; "return redacted, False"; "return \"\".join(clusters[:MAX_PREVIEW_CLUSTERS]), True" | mcp/src/agents_remember/serving/conversation/control/previews.py:28-28; mcp/src/agents_remember/serving/conversation/control/previews.py:32-32; mcp/src/agents_remember/serving/conversation/control/previews.py:48-48; mcp/src/agents_remember/serving/conversation/control/previews.py:51-51; mcp/src/agents_remember/serving/conversation/control/previews.py:58-58; mcp/src/agents_remember/serving/conversation/control/previews.py:61-62 |
| The queue projection precomputes the empty-content digest. | "_EMPTY_DIGEST = payload_digest(\"\")" | mcp/src/agents_remember/serving/conversation/control/queue_projection.py:44-44 |
| Authorized cockpit rows use stored content or the empty fallback, then mint operation and withdrawal refs. | "preview, truncated = redacted_preview(journal.text)"; "digest = journal.content_digest"; "preview, truncated, digest = \"\", False, _EMPTY_DIGEST"; "operation_ref = mint_ref( service.secret, \"operation-ref\", RefBinding(authorization, ar_session_id, epoch), RefTarget(identity=identity),"; "withdrawal_ref=mint_ref( service.secret, \"withdrawal-ref\", RefBinding(authorization, ar_session_id, epoch), RefTarget(identity=identity)," | mcp/src/agents_remember/serving/conversation/control/queue_projection.py:111-115; mcp/src/agents_remember/serving/conversation/control/queue_projection.py:121-122; mcp/src/agents_remember/serving/conversation/control/queue_projection.py:127-127; mcp/src/agents_remember/serving/conversation/control/queue_projection.py:129-133 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260731-EFA-L2 Current Delta

The row builder now takes one `ControlScope` (service + authorization + session id + **verified**
epoch — see [service.py](service.py.md)) instead of four parallel arguments, and mints refs with
`RefBinding(authorization, ar_session_id, epoch)` + `RefTarget(identity=…)` instead of four keyword
arguments to `mint_ref`. The projected queue rows are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-05T19:58+02:00 — No content impact: 260731-EFA-L16 made `ConversationControlService.resolve_entry` async (event-loop offload of the lock-taking catalog read), so this module's one call site (`operation_queue`) gained only the matching `await` — a one-for-one line replacement; no projection logic, wire shape, or error mapping changed, and this card names neither the seam's signature nor the call shape.
- 2026-08-04T11:43:39+02:00 — 260731-EFA-L6 S18-B03 curator: deduplicated the shared queue-model source
  reference while retaining both exact privacy-validator anchors; split preview/digest definitions,
  empty fallback, and authorized queue-row use into their operative owners.

- 2026-08-02T16:44:12+02:00 — 260731-EFA-L6 W1-B05 curator: anchored 4 citation items; scoped citation check now passes.

- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived the L3-vintage self-citations, which
  were written seven lines short of the current import block. `_LIVE_ROW_STATES` L36 -> L43,
  `operation_queue` L40 -> L47-L78, `_queue_row` L74 -> L81-L149 (the last two now span the whole
  function instead of naming its `def` line); `_EMPTY_DIGEST` L43 -> L44, which otherwise collided
  with the corrected `_LIVE_ROW_STATES` line. The L5F-vintage bound citations (`channel.queue_rows`
  write L104, `move_to_end` L108, the eviction loop L109-L110) were re-read and are still exact.
  No prose claim changed; the timeline paging the first sentence names now happens inside
  `ConversationControlService.read_full_timeline`, which still unions pages through `latestSequence`.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded the `ControlScope` and `RefBinding`/`RefTarget` call shapes.
- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: R5 bound — documented the new
  `MAX_QUEUE_ROWS_PER_CHANNEL=256` cap on `channel.queue_rows` with oldest-first `popitem` eviction
  in `_queue_row`; an evicted key restarts at revision 1 only if a settled operation reappears (it
  never does), so the bound is invisible to live rows and closes the prior unbounded-`queue_rows`
  precision-note Todo. Change uncommitted; closeout re-stamps verification.
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the source-aware queue
  projection — complete never-bodies prompt-queue truth, cockpit-only withdrawal refs/previews/
  digests, journal-backed empty-held honesty, and the accepted setter-row exclusion. Verification is
  blank because the new source file is uncommitted; closeout owns its first source stamp.
