# mcp/tests/test_operator_inbox.py

| Field                  | Value                                 |
| ---------------------- | ------------------------------------- |
| repository             | agents-remember                       |
| path                   | `mcp/tests/test_operator_inbox.py`    |
| doc_type               | `file-level-onboarding`               |
| lastUpdated            | 2026-07-08T04:25+02:00                |
| lastVerifiedCommitHash |                                       `1f8121ef5132a1be6a3d5b0829935d73c4556ff2`|
| lastVerifiedCommitDate |                                       2026-07-08T04:09:43+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

Focused backend tests for the durable operator/agent inbox record, store, hosted
delivery helper, and MCP payload builders.

## Code Commentary

### Logic

`OperatorInboxRecordTests` covers pure create/consume snapshots, address
validation, and schema alias round-trip. `OperatorInboxStoreTests` verifies
pending filtering by lifecycle, agent, recipient role, and combined keys; delivery metadata snapshots;
the lower-level store consume path appends a
consumed snapshot and repeated consume calls are idempotent. Task 23/24 adds the public payload
semantics: `operator_inbox_consume_payload` returns the consumed entry and then physically deletes the
throwaway pending row from the public inbox log. `OperatorInboxToolTests` patches `_store` to an in-memory temp
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
| Tool tests cover post, poll, consume payload deletion, and no-address poll validation. | L166-L220 | [test_operator_inbox.py](agents-remember/mcp/tests/test_operator_inbox.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Update History

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
- 2026-06-25T13:20+02:00 — Task 23/24: added coverage that the public consume payload deletes throwaway pending inbox entries after returning them.
- 2026-06-23T13:44+02:00 — Created for task 10 backend inbox: focused tests for record snapshots, store filtering/idempotent consume, and payload builders. Verification metadata pinned until closeout stamps the task-10 code commit.
