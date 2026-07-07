# mcp/tests/test_operator_inbox.py

| Field                  | Value                                 |
| ---------------------- | ------------------------------------- |
| repository             | agents-remember                       |
| path                   | `mcp/tests/test_operator_inbox.py`    |
| doc_type               | `file-level-onboarding`               |
| lastUpdated            | 2026-07-07T22:15+02:00                |
| lastVerifiedCommitHash |                                       `551695279f403ab19c0eba4ce6f6cfde6a8bb1f5`|
| lastVerifiedCommitDate |                                       2026-07-07T20:09:01+02:00|
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
