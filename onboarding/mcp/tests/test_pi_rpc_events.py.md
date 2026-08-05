# mcp/tests/test_pi_rpc_events.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_pi_rpc_events.py`          |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T15:32+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Behavioural tests for the Pi RPC event mapper (`serving.pi_rpc_events.PiRpcEventMapper`).

The mapper is the **only** thing that decides what one Pi wire frame *means* to the bridge:
whether it republishes the snapshot, appends a durable transcript entry, or crosses as
evidence only. **Nothing downstream can recover a frame the mapper classified wrongly**, so
these drive real frames through `translate` and assert the classification, the snapshot it
leaves behind, and the queue arithmetic that decides whether the seat is accepting input.

## Tests

- `test_a_fire_and_forget_extension_ui_call_becomes_one_transcript_entry` — a
  `notify`/`setStatus`-class call is durable content, exactly once.
- `test_a_dialog_extension_ui_call_blocks_the_seat_instead` — a dialog is a *block*, not a
  transcript entry: the seat is waiting for a human reply.
- `test_an_unsupported_extension_ui_method_is_refused` — an unknown method is refused, not
  guessed at.
- `test_a_queue_update_with_work_pending_marks_the_seat_running_and_queued`.
- `test_an_empty_queue_update_leaves_the_current_activity_alone` — an empty queue is not
  evidence the turn ended.
- `test_a_queue_update_without_both_arrays_is_refused` — a partial frame is a refusal, not a
  zero.

## Method

Plain pytest with a `mapper` fixture. `_state(**overrides)` builds a `PiSessionState`
(`session_id`, `session_file`, `is_streaming`, `is_compacting`, `pending_message_count`,
`thinking_level`, `model_key`, `raw`) so each test states only the field it is about.

The dialog / fire-and-forget split this module relies on is the same split recorded in
`fixtures/pi_rpc/0.80.7-capabilities.json` and **measured** against a live Pi by
`_pi_rpc_capabilities.py` — the mapper's vocabulary is not an assumption.

## Invariants And Boundaries

- Classification is one-way: a frame appended as a transcript entry cannot later be
  reclassified as evidence.
- A malformed queue frame is refused (`HarnessControlError`), never read as an empty queue —
  an empty queue would falsely mark the seat as accepting input.
- The mapper never invents state: the snapshot it leaves is derived from the frame plus the
  prior state.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The mapper under test. | `PiRpcEventMapper` | mcp/src/agents_remember/serving/pi_rpc_events.py:55-358 |
| `PiSessionState` and the parser that builds it. | `PiSessionState` | mcp/src/agents_remember/serving/pi_rpc_protocol.py:37-48 |
| The measured dialog / fire-and-forget vocabulary. | `fireAndForgetMethods` | mcp/tests/fixtures/pi_rpc/0.80.7-capabilities.json:43-43 |
| The adapter suite that consumes these classifications. | `PiRpcAdapterTests` | mcp/tests/test_pi_rpc_adapter.py:550-1124 |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B22 curator: replaced the `n/a` table rows with
  exact anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new Pi RPC
  event-mapper suite. Verification metadata is pinned to the leaf's reformat commit until
  closeout stamps the code commit.
