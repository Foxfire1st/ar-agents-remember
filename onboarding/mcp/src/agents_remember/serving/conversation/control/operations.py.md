# mcp/src/agents_remember/serving/conversation/control/operations.py

## Governing Overview

[Structured conversation control overview](overview.md)

## Purpose

R1: the exact-turn interrupt operation ledger. One idempotent interrupt authority per (session,
epoch) channel, keyed by authenticated caller + `(bridgeEpoch, turnId, requestId)` with an immutable
request fingerprint and a monotonic semantic revision. Acknowledgement (`requested → accepted |
unknown | rejected`) is the native interrupt write's answer; settlement (`pending → interrupted |
already-settled | failed`) is the correlated terminal native event. Acknowledgement is never
settlement.

## Code Commentary

### Logic

cit:([`InterruptRecord`], mcp/src/agents_remember/serving/conversation/control/operations.py:72-87) is the immutable ledger row (fingerprint, ack, settlement, revision, the
recorded evidence floor); cit:([`InterruptAnswer`], mcp/src/agents_remember/serving/conversation/control/operations.py:96-98) is its projection payload. cit:([`interrupt`], mcp/src/agents_remember/serving/conversation/control/operations.py:95-156)
serializes on the service's per-session lock, gates on the control capability, admits under the
fingerprint (identical replay returns the stored projection with no second native write; a reused id
with a different tuple is `request-conflict`), then cit:([`_drive_interrupt`], mcp/src/agents_remember/serving/conversation/control/operations.py:219-270) performs the L2E
epoch-guarded native write and cit:([`_apply_interrupt_result`], mcp/src/agents_remember/serving/conversation/control/operations.py:273-295) records the acknowledgement.
cit:([`interrupt_status`], mcp/src/agents_remember/serving/conversation/control/operations.py:159-201) re-observes settlement; cit:([`_redrive_unknown`], mcp/src/agents_remember/serving/conversation/control/operations.py:298-326) re-drives a lost
`may_have_sent` response through the substrate's replay-once cache (one native write total).
cit:([`_observe_settlement`], mcp/src/agents_remember/serving/conversation/control/operations.py:329-351) correlates the terminal native event: cit:([`_codex_terminal_outcome`], mcp/src/agents_remember/serving/conversation/control/operations.py:354-383)
reads the completion surface on event kind `"completed"` against cit:([`_CODEX_TERMINAL_STATUSES`], mcp/src/agents_remember/serving/conversation/control/operations.py:72-72);
cit:([`_pi_terminal_outcome`], mcp/src/agents_remember/serving/conversation/control/operations.py:452-481) + cit:([`_pi_stop_reason`], mcp/src/agents_remember/serving/conversation/control/operations.py:484-511) read pi's `stopReason` from the evidence
buffer. The **Finding 1 fix** lives at the `_pi_stop_reason` frame filter cit:([`_pi_stop_reason`], mcp/src/agents_remember/serving/conversation/control/operations.py:484-511): it matches
`frame.raw.get("type") == "message_end"` (payload type) instead of the old `frame.kind ==
"pi:message_end"` (event kind), so BOTH the content-less (`pi:message_end`) and content-ful
(`transcript`) message_end classes contribute their `stopReason` — without this an accepted abort
whose turn finished naturally with text stalled `pending` forever. The **Finding 2** class (a
`message_end` frame over the 32 KiB evidence clip) is closed by the L3E substrate fix (the truncation
envelope now preserves `type` + `message.stopReason`), which this evidence read consumes unchanged.
`_pi_terminal_outcome` returns `None` (cit:([`_pi_terminal_outcome`], mcp/src/agents_remember/serving/conversation/control/operations.py:452-481) — stays `pending`) when no `stopReason` is
recoverable; the latest-wins scan cit:([`_pi_stop_reason`], mcp/src/agents_remember/serving/conversation/control/operations.py:484-511) settles on the most recent visible reason. `_store`
cit:([`_store`], mcp/src/agents_remember/serving/conversation/control/operations.py:514-525), cit:([`_projection`], mcp/src/agents_remember/serving/conversation/control/operations.py:528-544), cit:([`_as_record`], mcp/src/agents_remember/serving/conversation/control/operations.py:554-556), and `interrupt_http_status`
cit:([`interrupt_http_status`], mcp/src/agents_remember/serving/conversation/control/operations.py:552-561) are the ledger plumbing and the O4 status map.

### Conventions

For pi (no native turn identity) the caller's `turnId` names the exact active AR operation id, which
the substrate guards pre-write (the L4-facing note below). Settlement is conservative: pi requires
the operation settle **plus** an `aborted`/`stop` `stopReason` — an order-only correlation could
overclaim `interrupted` on a natural completion.

### Invariants And Boundaries

- Acknowledgement ≠ settlement: an `accepted` interrupt returns 202 `pending` and settles only when
  the exact turn's terminal evidence crosses.
- Identical `(bridgeEpoch, turnId, requestId)` replay is idempotent — same projection, no second
  native write; a reused id with a different tuple is `409 request-conflict`.
- Every same-session interrupt serializes on the per-session lock above the L2E replay cache.
- A pre-write failure is `503 control-unavailable` with no phantom record; the guard battery
  (codex no-active/turn-mismatch, pi stale identity) settles `rejected`/`failed` as 422 with zero
  native writes.
- No PTY Esc / paste / native-queue substitution anywhere (source-scanned by the API suite).
- The settlement correlation reads only fields the L3E envelope preserves within the clip budget, so
  it stays under the 64 KiB IPC cap (the transcript-read seam that L3's fix-round-2 proved a dead
  end is not used here).

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured; the interrupt contract is repository-owned.

No configured domain documentation was available.

### Repo-Internal References

The native write and its replay cache belong to the L2E substrate; the pi/codex terminal frame
shapes come from the vendor mappers; the L3E envelope preservation is what the pi settlement reads.

- The L2E epoch-guarded native interrupt write and replay-once cache. [1]
- The pi mapper's two message_end emission classes (`pi:message_end` content-less, `transcript` content-ful). [2]
- The L3E truncation-envelope identity preservation (`type` + `message.stopReason`) this read consumes. [3]
- The service seams (per-session lock, epoch verify, identity, timeline) this ledger composes. [4]

### Cross-Repo References

No meaningful cross-repo references found.

No meaningful cross-repo references found.

## 260718-CHATS-L5I Current Delta

The control operation layer now accepts structured interaction answers and exact-turn interrupt operations through the same authorized session/epoch boundary. It separates an acknowledgement from terminal settlement and keeps the operation ledger authoritative for later reconciliation.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260731-EFA-L2 Current Delta

**`InterruptTicket`** (`turn_id`, `request_id`, `fingerprint`, `evidence_floor`) is now the single
value the interrupt path carries: the exact turn being interrupted and the request that is
interrupting it. The turn, the caller's request id, the fingerprint that makes the request
idempotent and the evidence floor the settlement is observed from are one attempt — a record
stamped with one attempt's fingerprint but another's evidence floor would settle against the wrong
turn.

`_claude_result_settlement(frame)` is now a named reader: it reads one Claude result frame as a
settlement. The settlement outcomes themselves are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.
