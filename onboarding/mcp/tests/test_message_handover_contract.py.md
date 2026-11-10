# mcp/tests/test_message_handover_contract.py

## Governing Overview

[overview](overview.md)

## Purpose

Proves that the held-delivery rule and the full-store (recipient-busy) refusal rule each have exactly one home in the compiled worker capsule, and that a paraphrased duplicate of either rule in the other home is caught.

## Code Commentary

The test compiles the worker orientation capsule from the live `skills/l-01-agent-lifecycles` tree through `routed_admission_for` and `compile_admitted_capsule`, then checks the two homes: the shared block equals `core/every-role.md` byte for byte (recorded with its content digest and emitted once by `shared_block`), and the `reference/message-handover.md` detail reference carries that file's bytes, a non-empty step, and exactly one rendered paragraph pairing "Before sending a handover, read" with its `{{detail:...}}` marker.

`_assert_one_receipt_contract` classifies non-heading paragraphs: the held contract (a paragraph naming both "held" and "queued") must sit once, in the shared block, saying "never resend it", with the `withdraw_held_message_id` sentence in the same section; the refusal contract (a paragraph naming recipient-busy or full-store) must sit once, in the handover reference, whose section holds the record-pending, continue, resend-once, report-the-second-refusal and leave-pending clauses. Two reworded combined sentences are appended to each home in turn and must fail with "multiple semantic homes". The reference also keeps "A receipt or turn-end does not establish semantic acceptance." This is static wording and compilation evidence, not executed message delivery.

## Evidence

- The one-home classifier for the held and refusal contracts [1]
- The compiled capsule carries both homes once and a paraphrased duplicate in either home fails [2]
- The held-delivery home in the shared every-role block [3]
- The full-store refusal home [4]
