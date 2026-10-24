# mcp/tests/test_held_queue.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Fault-injection proofs for the held-message queue (MIK-R100 rules 4a/4b): the queue survives restarts, crashes,
withdrawals, host limits and fleet size with every end recorded, a split batch keeps its part id on a deduping
host, and a turn end reported by the host delivers what waits without another message.

## Code Commentary

### Logic

`read_receipt` reads a recipient's store; `hold_open_worker()`, `end_turn()`, `drain_all()` and `open_worker()`
drive one recipient through a permission-pinned turn and its end, and `craft_recipient()` builds a recipient
without launching anything so a fleet can be sized.

- **Recovery.** `HeldQueueRecoveryTests` proves a restart after store admission delivers without a retry, a
  failed end record is staged and written by a later flush, a recovery reuses its batch id, and a restart with a
  stale zero counter still delivers.
- **Terminal ends.** `test_a_stop_after_store_deletion_still_records_its_terminal_end` covers the
  deletion-to-publication crash boundary, and an archived recipient still answers the sender its outcome.
- **Parts.** `test_six_messages_split_into_the_minimum_three_deliveries`,
  `test_variable_lengths_split_into_the_minimum_two_deliveries`,
  `test_an_oversized_batch_splits_into_admitted_deliveries_in_order`,
  `test_a_batch_exactly_at_the_limit_goes_in_one_delivery` and
  `test_an_interrupted_multi_part_delivery_resumes_without_loss_or_duplication` keep splitting minimal, ordered
  and resumable, with `test_a_split_recovery_keeps_the_part_id_on_a_deduping_host` keeping the part id.
- **Withdrawals.** `test_a_withdrawal_during_a_live_claim_is_refused_and_sends_nothing_new` and
  `test_a_withdrawal_racing_a_delivery_has_one_winner` give a race one winner.
- **Ordering.** `test_a_queue_with_a_host_unreachable_row_behind_an_ordinary_one_drains` ends a part before a row
  the host may already hold, and `test_a_ready_drain_that_pauses_writes_one_line_with_the_recipient_and_reason`
  writes one line with the recipient and reason.
- **Bounds.** `HeldSweepBoundsTests` keeps per-tick work bounded at any fleet size: a queued receipt past the
  first slice is reached within bounded ticks, an idle fleet's reads stay bounded at two sizes, zero input does
  no drain work, a small fleet drains in one tick, a large backlog rotates under the cap with dead and history
  recipients counted, and removing a working folder reclaims the store and terminates cleanly.
- **Turn end.** `TurnEndDeliveryTests` parses an unchanged publication once across ticks, delivers on the host's
  own turn-end record, holds while a permission still waits, writes one line on a failed drain, and keeps a
  receipt count equal to the messages its store holds.

### Conventions

Each case injects one fault at a named seam (store, end record, host, withdrawal race) and asserts the recorded
end, so a lost message shows up as a missing or duplicated record.

### Invariants And Boundaries

- A message is delivered once: a split, a recovery and a deduping host all keep the same id.
- Work per tick is bounded by a rotating slice, not by the fleet's size.

## Evidence

- A stale receipt zero does not lose durable admitted text after a restart. [1]
- A terminal end survives the deletion-to-publication crash boundary. [2]
- Replayed split work retains its part id on a deduping host. [3]
- A larger admissible remainder is not chopped by a smaller earlier accepted size. [4]
- Fleet-scale idle ticks cap reads and observe enumeration independently of read counts. [5]
