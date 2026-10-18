# Held-queue recovery and bounded-work proofs

[Tests route overview](overview.md)

## Contract

Fault injection covers admission before receipt counting (including a stale zero count), ended text deletion before terminal receipt publication, immutable batch/part recovery, and sender withdrawal racing a live delivery claim. End records are sender-isolated even when a recipient is archived. Waiting text belongs to the workspace and ends when that folder is reclaimed.

The partition tests distinguish accepted-size lower bounds from refused-size upper bounds: equal and variable-length FIFO messages yield minimum admitted partitions under the fixture’s monotone size limit; an exactly admitted batch is one delivery. Crash/replay exactly-once claims use an explicitly deduping fake host keyed by the durable message ID. They are not a real-host deduplication witness.

Bound tests separately count receipt reads and enumerated names across empty, small and large fleets, multiple zero-input cycles, dead recipients and history. The idle-fleet test observes zero `rglob` yields and a per-tick read cap; it does not claim that every enumeration mechanism produces zero names. The native scanner has its own bounded rotating census.

The class also holds the turn-end, rotation and paused-drain cases. `TurnEndDeliveryTests::test_a_turn_end_delivers_what_waits_without_another_message` publishes a turn end and delivers the waiting message with no further send, and the queue forgets the receipt; `::test_a_turn_end_holds_the_message_while_a_permission_still_waits` keeps it held while the prompt is open; `::test_a_failed_drain_writes_one_line_with_the_recipient_and_the_reason` and `HeldQueueRecoveryTests::test_a_ready_drain_that_pauses_writes_one_line_with_the_recipient_and_reason` assert one warning line naming the recipient and the reason; `::test_a_receipt_count_equals_the_messages_its_store_holds` asserts the recounted `heldWaiting`. `HeldSweepBoundsTests::test_a_queued_receipt_past_the_first_slice_is_reached_within_bounded_ticks` reaches a receipt behind 33 and 65 queued ones within `2 + size // 32` ticks while the receipts ahead of the slice stay held. These are the controlled fixture's file and log assertions, not a real-host witness.

## Evidence

- A stale receipt zero does not lose durable admitted text after restart. [1]
- A terminal end survives the deletion-to-publication crash boundary. [2]
- Replayed split work retains its part ID on a deduping host. [3]
- A larger admissible remainder is not chopped by a smaller earlier accepted size. [4]
- Fleet-scale idle ticks cap reads and observe enumeration independently of read counts. [5]
