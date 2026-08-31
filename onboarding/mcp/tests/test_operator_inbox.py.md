# mcp/tests/test_operator_inbox.py

| Field                  | Value                                 |
| ---------------------- | ------------------------------------- |
| repository             | agents-remember                       |
| path                   | `mcp/tests/test_operator_inbox.py`    |
| doc_type               | `file-level-onboarding`               |
| lastUpdated            | 2026-07-10T13:03+02:00                |
| lastVerifiedCommitHash |                                       `f2b7c648f540efb9d64ceea22e11e651cb5cc914`|
| lastVerifiedCommitDate |                                       2026-08-31T15:32:32+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

Record, store, tool, and delivery regression suite for durable operator-inbox communication.

## Code Commentary

L23 covers `transition_many` folding in order, appending only real changes, retaining the latest row for no-op transitions, and refusing missing entries.

### Logic

The suite covers append-only snapshots, mailbox validation, legacy parsing, idempotent attribution, backoff/compaction, role-address resolution, decision relay, replacement-safe manager/architect delivery, and hosted delivery races. Current subjects and owners carry task-document identity where durable work is addressed.

### Conventions

Test-only evidence uses deterministic fakes/fixtures and exercises the registered or owning seam directly.

### Invariants And Boundaries

Durable rows preserve attribution and delivery evidence; public structural messaging never asks the model for the current occupant id; unresolved or ambiguous owners fail closed.

## Docs References

No Domain Documentation source is configured for this repository-local regression contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Current suite declaration anchoring this card. | `_TaskHierarchy` | mcp/tests/test_operator_inbox.py:69-69 |

## Cross-Repo References

No cross-repository implementation source governs this test module.

## Update History

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — Reconciled `test_operator_inbox.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T16:44:03+02:00 — W1-B07 curator: repaired 5 repository-reference citations (5/5 anchored and sourced; scoped citation check clean).
- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: the whole suite moved to the parameter-object
  form of the inbox seams, so the Conventions section was rewritten to name them instead of
  attesting past them: `create_operator_inbox_entry` and `operator_inbox_post_payload` now take
  `InboxMessage`/`InboxAddress`/`InboxRouting`/`InboxPoster` (and `HostedDelivery` for the
  hosted push, with `HostedDelivery(enabled=False)` replacing `deliver_to_hosted=False`),
  `OperatorInboxStore.record_delivery` takes a `DeliveryAttempt` whose field is `detail` rather
  than the old `delivery_detail` keyword, `deliver_inbox_entry` takes `InboxDeliveryLog`
  (carrying the stale `current` snapshot as `floor=RedeliveryFloor(...)` and the timestamp as
  `at=`) plus `sessions=HostedSessionRuntime(...)`, `TerminalHost` takes `TerminalHostSeams`,
  and the `submit_control_prompt` doubles now receive a positional `submission` object instead
  of `**kwargs`. The shifted call sites invalidated all four own-file reference ranges, which
  were re-verified against the current class boundaries and re-anchored (L22-L74 to L52-L153;
  L77-L163 to L155-L276; L220-L290 to L277-L438; L166-L220 to L440-L673), and a fifth row was
  added for the delivery suite at L675-L901. No test case was added, removed, or renamed and no
  assertion changed.

- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented the exact additive inbox compatibility regression
  and negative allowlist proof.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.

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
