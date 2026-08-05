# mcp/src/agents_remember/serving/conversation/control/operations.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/operations.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`|
| lastVerifiedCommitDate |  2026-08-05T12:41:24+02:00|
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

cit:([`InterruptRecord`], mcp/src/agents_remember/serving/conversation/control/operations.py:72-87) is the immutable ledger row (fingerprint, ack, settlement, revision, the
recorded evidence floor); cit:([`InterruptAnswer`], mcp/src/agents_remember/serving/conversation/control/operations.py:90-92) is its projection payload. cit:([`interrupt`], mcp/src/agents_remember/serving/conversation/control/operations.py:95-156)
serializes on the service's per-session lock, gates on the control capability, admits under the
fingerprint (identical replay returns the stored projection with no second native write; a reused id
with a different tuple is `request-conflict`), then cit:([`_drive_interrupt`], mcp/src/agents_remember/serving/conversation/control/operations.py:219-270) performs the L2E
epoch-guarded native write and cit:([`_apply_interrupt_result`], mcp/src/agents_remember/serving/conversation/control/operations.py:273-295) records the acknowledgement.
cit:([`interrupt_status`], mcp/src/agents_remember/serving/conversation/control/operations.py:159-201) re-observes settlement; cit:([`_redrive_unknown`], mcp/src/agents_remember/serving/conversation/control/operations.py:298-326) re-drives a lost
`may_have_sent` response through the substrate's replay-once cache (one native write total).
cit:([`_observe_settlement`], mcp/src/agents_remember/serving/conversation/control/operations.py:329-351) correlates the terminal native event: cit:([`_codex_terminal_outcome`], mcp/src/agents_remember/serving/conversation/control/operations.py:354-383)
reads the completion surface on event kind `"completed"` against cit:([`_CODEX_TERMINAL_STATUSES`], mcp/src/agents_remember/serving/conversation/control/operations.py:66-66);
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
cit:([`_store`], mcp/src/agents_remember/serving/conversation/control/operations.py:514-525), cit:([`_projection`], mcp/src/agents_remember/serving/conversation/control/operations.py:528-544), cit:([`_as_record`], mcp/src/agents_remember/serving/conversation/control/operations.py:547-549), and `interrupt_http_status`
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

## Docs References

No Domain Documentation source is configured; the interrupt contract is repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The native write and its replay cache belong to the L2E substrate; the pi/codex terminal frame
shapes come from the vendor mappers; the L3E envelope preservation is what the pi settlement reads.

| Finding | Anchor | Source |
| --- | --- | --- |
| The L2E epoch-guarded native interrupt write and replay-once cache. | "One native interrupt write, epoch-guarded and bridge-stamped."; `InterruptCapableAdapter` | mcp/src/agents_remember/serving/harness_control_bridge.py:273-300; mcp/src/agents_remember/serving/harness_control_adapter.py:91-106 |
| The pi mapper's two message_end emission classes (`pi:message_end` content-less L237, `transcript` content-ful L241). | `transcript` | mcp/src/agents_remember/serving/pi_rpc_events.py:302-302 |
| The L3E truncation-envelope identity preservation (`type` + `message.stopReason`) this read consumes. | `_preserved_evidence_identity`, `clip_evidence_payload` | mcp/src/agents_remember/serving/harness_control_models.py:727-754; mcp/src/agents_remember/serving/harness_control_models.py:786-838 |
| The service seams (per-session lock, epoch verify, identity, timeline) this ledger composes. | `session_lock`, `verify_epoch`, `build_identity`, `read_full_timeline` | mcp/src/agents_remember/serving/conversation/control/service.py:252-262; mcp/src/agents_remember/serving/conversation/control/service.py:294-298; mcp/src/agents_remember/serving/conversation/control/service.py:308-318; mcp/src/agents_remember/serving/conversation/control/service.py:320-341 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

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

## Update History

- 2026-08-03T03:06:44+02:00 — W3-B04 curator: curated 3 table citations and 8 prose citations (11 total), supplying exact anchors and paths; the scoped fixer generated all final extents.
- 2026-07-31T18:05+02:00 — 260731-EFA-L2 curator: re-derived 19 stale self-citations after the
  `InterruptTicket` extraction and the `_claude_terminal_outcome`/`_claude_result_settlement` pair
  landed between the codex and pi readers, which pushed the whole back half of the file down ~100
  lines. Single-line def citations were also widened to the whole construct the sentence describes:
  `InterruptRecord` L66→L72-L87, `InterruptAnswer` L83→L90-L92, `interrupt` L87→L95-L156,
  `interrupt_status` L147→L159-L201, `_drive_interrupt` L197→L219-L270,
  `_apply_interrupt_result` L248→L273-L295, `_redrive_unknown` L273→L298-L326,
  `_observe_settlement` L322→L329-L351, `_codex_terminal_outcome` L325→L354-L383,
  `_CODEX_TERMINAL_STATUSES` L59→L66, `_pi_terminal_outcome` L357→L452-L481 (its `None` return
  L393-L393→L475-L476), `_pi_stop_reason` L383→L484-L511 with the Finding-1 payload-type frame
  filter L431-L432→L500-L501 and the latest-wins scan L437-L439→L505-L507, `_store` L413→L514-L525,
  `_projection` L427→L528-L544, `_as_record` L479→L547-L549, and `interrupt_http_status`
  L484→L552-L561. No claim text changed; every range was read back against the current source.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation. The epoch-guarded
  native write is `HarnessControlBridge.interrupt` cit:([`interrupt`], mcp/src/agents_remember/serving/harness_control_bridge.py:273-300),
  which calls `_require_epoch` first cit:([`_require_epoch`], mcp/src/agents_remember/serving/harness_control_bridge.py:302-305)
  and re-stamps the result with the queue's bridge epoch. The row's second half — the replay-once
  cache — is contracted on the `InterruptCapableAdapter` protocol cit:([`InterruptCapableAdapter`], mcp/src/agents_remember/serving/harness_control_adapter.py:91-106),
  where a repeat naming the same (expected, active) pair replays the first acknowledgement with no
  second write. No claim text changed.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `InterruptTicket` and the `_claude_result_settlement` reader.
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the exact-turn interrupt
  ledger — fingerprint idempotence, per-session serialization above the L2E replay cache, ack≠settle
  semantics, and the settlement correlation carrying the round-3 Finding 1 payload-type fix over the
  closed L3E evidence-envelope preservation (Finding 2 class). Verification is blank because the new
  source file is uncommitted; closeout owns its first source stamp.
