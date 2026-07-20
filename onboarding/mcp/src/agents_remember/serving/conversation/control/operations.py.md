# mcp/src/agents_remember/serving/conversation/control/operations.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/operations.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `0be0099744bf1287805acf0b95072127b70f7104`|
| lastVerifiedCommitDate |  2026-07-20T15:34:11+02:00|
| governingOverview | `overview.md` |

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

`InterruptRecord` (L65) is the immutable ledger row (fingerprint, ack, settlement, revision, the
recorded evidence floor); `InterruptAnswer` (L83) is its projection payload. `interrupt` (L87)
serializes on the service's per-session lock, gates on the control capability, admits under the
fingerprint (identical replay returns the stored projection with no second native write; a reused id
with a different tuple is `request-conflict`), then `_drive_interrupt` (L192) performs the L2E
epoch-guarded native write and `_apply_interrupt_result` (L248) records the acknowledgement.
`interrupt_status` (L147) re-observes settlement; `_redrive_unknown` (L273) re-drives a lost
`may_have_sent` response through the substrate's replay-once cache (one native write total).
`_observe_settlement` (L304) correlates the terminal native event: `_codex_terminal_outcome` (L325)
reads the completion surface on event kind `"completed"` against `_CODEX_TERMINAL_STATUSES` (L59);
`_pi_terminal_outcome` (L357) + `_pi_stop_reason` (L383) read pi's `stopReason` from the evidence
buffer. The **Finding 1 fix** lives at the `_pi_stop_reason` frame filter (L398-L399): it matches
`frame.raw.get("type") == "message_end"` (payload type) instead of the old `frame.kind ==
"pi:message_end"` (event kind), so BOTH the content-less (`pi:message_end`) and content-ful
(`transcript`) message_end classes contribute their `stopReason` — without this an accepted abort
whose turn finished naturally with text stalled `pending` forever. The **Finding 2** class (a
`message_end` frame over the 32 KiB evidence clip) is closed by the L3E substrate fix (the truncation
envelope now preserves `type` + `message.stopReason`), which this evidence read consumes unchanged.
`_pi_terminal_outcome` returns `None` (L374-L375 → stays `pending`) when no `stopReason` is
recoverable; the latest-wins scan (L404-L406) settles on the most recent visible reason. `_store`
(L413), `_projection` (L427), `_as_record` (L444), and `interrupt_http_status` (L449) are the ledger
plumbing and the O4 status map.

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

## Docs References

No Domain Documentation source is configured; the interrupt contract is repository-owned.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The native write and its replay cache belong to the L2E substrate; the pi/codex terminal frame
shapes come from the vendor mappers; the L3E envelope preservation is what the pi settlement reads.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The L2E epoch-guarded native interrupt write and replay-once cache. | L1-L120 | [harness_control_bridge.py](agents-remember/mcp/src/agents_remember/serving/harness_control_bridge.py) |
| The pi mapper's two message_end emission classes (`pi:message_end` content-less L237, `transcript` content-ful L241). | L131-L302 | [pi_rpc_events.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_events.py) |
| The L3E truncation-envelope identity preservation (`type` + `message.stopReason`) this read consumes. | L569-L667 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |
| The service seams (per-session lock, epoch verify, identity, timeline) this ledger composes. | L168-L266 | [service.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/service.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the exact-turn interrupt
  ledger — fingerprint idempotence, per-session serialization above the L2E replay cache, ack≠settle
  semantics, and the settlement correlation carrying the round-3 Finding 1 payload-type fix over the
  closed L3E evidence-envelope preservation (Finding 2 class). Verification is blank because the new
  source file is uncommitted; closeout owns its first source stamp.
