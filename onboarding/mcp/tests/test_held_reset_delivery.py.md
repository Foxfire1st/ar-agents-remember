# mcp/tests/test_held_reset_delivery.py

## Governing Overview

[overview](overview.md)

## Purpose

Unit-regression suite exercising durable reset-index scheduling, startup adoption of aged legacy waits, ordered post-reset delivery, generation fencing, and bounded multi-recipient overlap across the real admission, receipt-discovery, and scheduler owners.

## Code Commentary

`HeldResetDeliveryTests` subclasses `RoleToolsTestCase` to drive real launch receipts, held stores, and the fake native host:

- `test_startup_adopts_an_aged_legacy_wait_and_delivers_in_order_at_reset` holds two provider-limited messages without indexing them, ages the held-receipt queue entry past `HELD_QUEUE_MAX_AGE_SECONDS` so `held_queue_receipts` is empty, runs `run_held_reset_scheduler` with an injected clock and sleep starting one second before `RESET`, and asserts that startup adoption enrolls the wait, the scheduler sleeps exactly `1.0` second until reset, delivers both messages in FIFO order within thirty seconds of reset, and clears `index.next_attempt()`.
- `test_an_indexed_wait_survives_a_new_scheduler_and_is_retired_after_ack` holds two provider-limited messages through `hold_at_receipt`, opens a fresh `HeldResetIndex`, verifies the entry is not due one microsecond before `RESET`, delivers it via `deliver_due_pass`, and asserts `ResetPassResult(1, 1, 1)`, retirement from `due_at(RESET)`, and receipt of the held batch.

Two standalone pytest tests verify concurrency and generation safety:

- `test_live_reset_wins_enrollment_and_a_prior_generation_cannot_retire_it` schedules an earlier reset, captures its `ResetEntry`, schedules an extended reset, calls `enroll` with the stale earlier target and `finish` with the stale generation, and asserts the extended live entry remains intact.
- `test_pass_overlaps_distinct_recipients_and_stays_at_the_pool_bound` schedules eight distinct recipients due at `RESET`, runs `deliver_due_pass` on a 2-worker pool with a 2-thread `Barrier`, and asserts every recipient is visited once, concurrent active recipients overlap at 2 and never exceed 2, and `ResetPassResult(8, 8, 8)` is returned.

## Boundaries

These are source-declared unit-regression assertions registered in `unit-regression` (`mcp/tests/test-evidence-lanes.toml`) and tracked in `mcp/tests/evidence-lifecycle.toml`; card prose describes declared assertions rather than a new execution run or live-host throughput measurement.

## Evidence

- `HeldResetDeliveryTests` exercises startup adoption of an aged legacy wait dropped from the 24-hour queue, exact deadline wake, FIFO delivery within thirty seconds, and post-acknowledgement retirement across a fresh scheduler. [1]
- `test_live_reset_wins_enrollment_and_a_prior_generation_cannot_retire_it` verifies that `enroll` preserves live entries and a stale generation cannot retire a newer schedule. [2]
- `test_pass_overlaps_distinct_recipients_and_stays_at_the_pool_bound` verifies concurrent delivery across distinct recipients stays within the configured pool bound with one visit per recipient. [3]
