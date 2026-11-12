# mcp/tests/test_explainer_moved_watcher.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The watch around the moved measurement: the native turn-end loop publishes the notice, an actual Worker id resolves to its leaf while an unrelated seat passes by, and an old notice stops being authoritative.

## Code Commentary

- A Worker's ended turn publishes the moved notice on the in-process channel with no page reopened, no message sent, and no comparison pin or record written.
- An actual native Worker id maps to its leaf's environment; a seat of no watched leaf triggers nothing.
- An Update, a Retire or a new generation clears the old notice, and a reconnect within the cooldown cannot replay it.

## Evidence

- The case `test_the_native_turn_end_loop_runs_the_workers_turn_end_without_writes_or_messages` protects the native loop publishing a notice with no write, message or pin. [1]
- The case `test_a_worker_turn_end_captures_through_the_watch_and_an_unrelated_seat_is_ignored` protects a real Worker id resolving to its leaf while an unrelated seat is ignored. [2]
- The case `test_update_retire_and_a_new_generation_clear_the_old_moved_notice` protects an old moved notice ceasing to be authoritative after an Update, a Retire or a new generation. [3]
