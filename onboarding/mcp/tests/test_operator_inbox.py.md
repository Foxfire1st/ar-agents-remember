# mcp/tests/test_operator_inbox.py

| Field                  | Value                                 |
| ---------------------- | ------------------------------------- |
| repository             | agents-remember                       |
| path                   | `mcp/tests/test_operator_inbox.py`    |
| doc_type               | `file-level-onboarding`               |
| lastUpdated            | 2026-07-10T13:03+02:00                |
| lastVerifiedCommitHash |                                       `0d5ce6784930aa4e9006ab4bbf2b788a3296abce`|
| lastVerifiedCommitDate |                                       2026-07-10T22:30:19+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

Focused backend tests for the durable operator/agent inbox record, store, hosted
delivery helper, and MCP payload builders.

## Code Commentary

### 260707-HFX2-L20 Deterministic Concurrency Regression

The in-flight delivery test blocks the paster in a worker thread, consumes the same row, then lets
delivery append from its stale snapshot. It proves the physical log contains pending, consumed, and
late pending records while `current`, polling, and redelivery all continue to expose the consumed
terminal state.

### 260707-HFX2-L13 Transition And Completion-Wake Proof

Store coverage now asserts `advance_rung` stamps `rungTransitionAt` on consecutive transitions.
The end-to-end completion test posts a reviewer turn-report with a stale manager address and proves
the resulting row/owner metadata targets the successor manager, hosted delivery succeeds, and the
paste lands in that manager's session.

### Logic

**260707-HFX2-L15 coverage.** Hosted inbox tests provide a matching harness log, assert
`harness-log-confirmed` durable detail and catalog binding, and prove absence remains unconfirmed
with failure evidence. Fixture rows carry the new optional dispatch provenance without changing
the durable inbox state enum.

`OperatorInboxRecordTests` covers pure create/consume snapshots, address
validation, and schema alias round-trip. `OperatorInboxStoreTests` verifies
pending filtering by lifecycle, agent, recipient role, and combined keys; delivery metadata snapshots;
the lower-level store consume path appends a
consumed snapshot and repeated consume calls are idempotent. `operator_inbox_consume_payload` returns
the consumed entry and retains that terminal snapshot until compaction. `OperatorInboxToolTests` patches `_store` to an in-memory temp
store and drives the real post, poll, and consume payload builders. `OperatorInboxDeliveryTests`
drives `deliver_inbox_entry` against a temp store + a fake catalog/host: one case pushes a
verified paste (state `delivered`) and — since 260703-L18 (finding 3, pinning the friction
F-A confirm seam) — a second case pushes an UNVERIFIED paste
(`PasteResult(delivered=False, capture="claude> (booting)")`) and asserts the recorded
`deliveryState` is `unconfirmed` with a `deliveryDetail` that — since 260707-HFX-L3 — contains
"paste was not capture-verified" AND the pane capture itself (the durable row is the forensic
record a re-briefing operator reads, never a bare "not echoed"). A third case
(`test_unverified_delivery_with_empty_capture_still_records_a_loud_detail`) pushes an
empty-capture failure (a vanished session) and asserts the dedicated wording
"paste was not capture-verified (empty pane capture)". The unverified cases are the regression:
they FAIL if `serving/inbox_delivery.py`'s delivered/unconfirmed branch is ever collapsed to
always-`delivered` or its detail drops the capture evidence.
`OperatorInboxToolTests` (260707-HFX-L12) gains two round-trip tests pinning the ratified R9
decision-item relay's operator-inbox schema representability:
`test_decision_item_relay_round_trip_between_orchestrator_and_architect` drives
`operator_inbox_post_payload`/`operator_inbox_poll_payload` for the exact doctrine-mandated call
shape — orchestrator posts `messageKind="decision-item"` to `recipient_role="architect"`, the
architect polls and receives it, then posts `messageKind="decision-ruling"` back to
`recipient_role="orchestrator"` — asserting both posts and the poll succeed at the real tool-payload
seam, not the raw pydantic model. `test_plain_message_addressed_to_architect_and_curator_succeeds`
pins that a plain `"message"` kind addressed to each of the two new `AgentRole` values succeeds.
Both tests are the regression for `controlplane/operator_inbox_records.py`'s `AgentRole`/
`InboxMessageKind` Literal extension: before that fix both raised `ValidationError` (`recipientRole`
rejecting `'architect'`, `messageKind` rejecting `'decision-item'`) — this is the exact live repro
the master-exit adversarial review's Finding 1 (BLOCK) named, and these tests are the proof it is
closed, not just the schema edit in isolation.
`OperatorInboxStoreTests` (260707-HFX2-L1, R1/R3) gains ack/backoff/redelivery/escalation coverage
for the new `attemptCount`/`lastAttemptAt`/`nextAttemptAt`/`escalatedAt` fields on
`OperatorInboxEntry`: `test_record_delivery_bumps_attempt_and_schedules_next_attempt` pins that
`record_delivery` bumps `attemptCount` and stamps a further-out `nextAttemptAt` on EVERY delivery
attempt — including a confirmed `delivered` paste — because consume=ack is the only terminal
outcome, `delivered` is never terminal. HFX2-L9 strengthens that assertion so the first stamped
`nextAttemptAt` is at least 900 seconds after `lastAttemptAt`, proving first send is treated as
in-flight for the redelivery floor. `test_record_delivery_clears_schedule_only_via_consume`
pins the corollary: only `consume` (never another `record_delivery` call) transitions the entry to
the `consumed` state. `test_list_redeliverable_returns_pending_rows_past_backoff` and
`test_list_redeliverable_excludes_consumed_rows` cover the store-level redelivery query the L2
sweep will use — a pending row past its backoff schedule is redeliverable, a consumed row never is.
`test_mark_escalated_stamps_the_reserved_field` pins that `mark_escalated` stamps `escalatedAt`
(the field this leaf only RESERVES for a future escalation-ladder leaf to set on its own trigger).
260707-HFX2-L4 (R1/R2) adds `test_advance_rung_stamps_rung_and_reanchors_escalated_at` — the
ladder's own transition: `advance_rung` sets BOTH `rung` and re-anchors `escalatedAt` to the new
`now` in the SAME snapshot, asserted across two successive transitions (rung 1 then rung 2, each
re-anchoring `escalatedAt` to its own call's `now`) so a stale prior anchor can never leak into the
next rung's SLA check. `test_advance_rung_unknown_entry_raises` pins the `KeyError` on an entry id
the store has never seen.
HFX2-L8 adds `test_ladder_resolved_is_terminal_without_ack` and
`test_compaction_prunes_ladder_resolved_rows`: a row can become durable
`state="ladder-resolved"` without being an ack/consume, redelivery queries exclude it, and
compaction prunes it while still preserving live pending rows.
`test_compaction_never_removes_a_pending_unacked_row_regardless_of_age` is the R1 regression proper:
an unacked row survives `store.compact()` even when it is far past the retention TTL, exercised
against the real post-time compaction path (`operator_inbox_post_payload` calls `store.compact()`
immediately after append) — this is the test that FAILS if `_keep_inbox_entry` is ever changed to
prune pending rows by age instead of by consumed state.
`test_compaction_still_prunes_a_stale_consumed_row` is the paired control: a `consumed` row past
the TTL is still pruned, proving the fix is a targeted pending-row exemption, not a blanket
compaction disable.

### Conventions

Tests mirror the gate control-plane test style: temporary directories, patched
store factories for payload-builder tests, and direct assertions on modeled
payload dictionaries.

### Invariants And Boundaries

- A mailbox post/poll must include `lifecycle_id`, `agent_id`, or `recipient_role`.
- Store-level consume preserves an auditable snapshot for direct store users, while the public MCP consume
  payload deletes the throwaway pending row after returning it.
- Tool tests exercise payload builders, not FastMCP transport.

### Todos

None.

## Docs References

No relevant external documentation found after checking the in-repo design docs
listed as Domain Documentation.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Record tests cover create/consume purity, required addressing, and schema alias round-trip. | L22-L74 | [test_operator_inbox.py](agents-remember/mcp/tests/test_operator_inbox.py) |
| Store tests cover lifecycle/agent filters, idempotent consume, missing entry, and missing address errors. | L77-L163 | [test_operator_inbox.py](agents-remember/mcp/tests/test_operator_inbox.py) |
| Store tests (R1/R3 plus HFX2-L8/L9) cover attempt/backoff stamping, the 900-second first-send floor, redeliverable filtering, escalation stamping, ladder-resolved terminal state, and compaction pruning for terminal rows while preserving pending rows. | L220-L290 | [test_operator_inbox.py](agents-remember/mcp/tests/test_operator_inbox.py) |
| Tool tests cover post, poll, durable consume payloads, and no-address poll validation. | L166-L220 | [test_operator_inbox.py](agents-remember/mcp/tests/test_operator_inbox.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Update History

- 2026-07-10T22:18+02:00 — 260707-HFX2-L20: added deterministic consume-during-delivery coverage
  and updated consume assertions for durable terminal snapshots.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: moved hosted inbox assertions from pane echo to bound
  harness-log evidence and persisted binding provenance. Verification metadata remains pinned
  until closeout stamps the eventual L15 code commit.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 round 2: pinned redundant rung stamps and the exact
  stale-manager reviewer-completion wake path. Verification metadata remains pinned until closeout
  stamps the eventual L13 code commit.

- 2026-07-09T11:19+02:00 — 260707-HFX2-L9: strengthened
  `test_record_delivery_bumps_attempt_and_schedules_next_attempt` to assert the first delivered row
  schedules `nextAttemptAt` at least 900 seconds out. Verification metadata pinned until closeout
  stamps the 260707-HFX2-L9 commit.
- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 (dead-seat storm, R1/R3): added regressions for
  `mark_ladder_resolved` as a terminal non-ack state and compaction pruning ladder-resolved rows
  while preserving live pending rows. Verification metadata pinned until closeout stamps the
  260707-HFX2-L8 commit.
- 2026-07-08T23:15+02:00 — 260707-HFX2-L4 (escalation ladder, R1/R2): added
  `test_advance_rung_stamps_rung_and_reanchors_escalated_at` (two successive rung transitions each
  re-anchor `escalatedAt` to their own call's `now`) and `test_advance_rung_unknown_entry_raises`
  (`KeyError` on an unknown entry id) — coverage for the new `OperatorInboxStore.advance_rung`
  method. Verification metadata pinned until closeout stamps the 260707-HFX2-L4 commit.
- 2026-07-08T16:15+02:00 — 260707-HFX2-L1 (curator delta round 2, closeout-preview gap): added
  coverage for `OperatorInboxStoreTests`' six new R1/R3 tests — `record_delivery` attempt/backoff
  stamping (every attempt, including a confirmed `delivered` paste, bumps `attemptCount` and
  reschedules `nextAttemptAt`, since consume=ack is the only terminal outcome), `list_redeliverable`
  filtering, `mark_escalated` field stamping, and the paired
  never-prune-pending-vs-still-prunes-consumed compaction regression proving the R1 retention fix
  is a targeted pending-row exemption. Verification metadata pinned until closeout stamps the
  260707-HFX2-L1 commit.
- 2026-07-08T04:25+02:00 — 260707-HFX-L12 (operator-inbox relay schema, master-exit fix leaf):
  added `test_decision_item_relay_round_trip_between_orchestrator_and_architect` and
  `test_plain_message_addressed_to_architect_and_curator_succeeds` to `OperatorInboxToolTests` —
  the regression pinning the master-exit-review-mandated `AgentRole`/`InboxMessageKind` Literal
  extension (`architect`/`curator` roles; `decision-item`/`decision-ruling` kinds) via the real
  tool-payload seam. Verification metadata pinned until closeout stamps the HFX-L12 commit.
- 2026-07-07T22:15+02:00 — 260707-HFX-L3 (capture-verified delivery): the unverified-push case now
  asserts the durable `deliveryDetail` carries the pane capture ("paste was not capture-verified"
  + the capture text, replacing the bare "paste was not echoed" truth), and the new
  `test_unverified_delivery_with_empty_capture_still_records_a_loud_detail` pins the
  empty-capture wording. Verification metadata pinned until closeout stamps the HFX-L3 commit.
- 2026-07-07T18:40+02:00 — 260703-L18 (review fix batch, finding 3, test-only): added
  `test_deliver_inbox_entry_records_unconfirmed_when_paste_is_not_echoed` — pins the
  delivered-vs-unconfirmed distinction in `serving/inbox_delivery.py` so an un-echoed paste records
  `unconfirmed`, and the suite FAILS if that branch collapses to always-`delivered` (verified by
  mutation). Verification metadata pinned until closeout stamps the L18 commit.
- 2026-07-04T12:31+02:00 - L3: expanded inbox coverage for role addressing,
  delivery-state snapshots, hosted-session push, and role/message response
  metadata. Verification metadata pinned until closeout stamps the L3 commit.
- 2026-06-25T13:20+02:00 — Task 23/24 historical behavior: added coverage that public consume deleted
  the throwaway row after returning it; superseded by HFX2-L20's durable terminal snapshot.
- 2026-06-23T13:44+02:00 — Created for task 10 backend inbox: focused tests for record snapshots, store filtering/idempotent consume, and payload builders. Verification metadata pinned until closeout stamps the task-10 code commit.
