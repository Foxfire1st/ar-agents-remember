# mcp/tests/test_explainer_service.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The seat order rather than the bytes: one environment per leaf, a generation that only grows, a build that rolls back to zero effects, an Update that refuses instead of waiting, and a Retire that finishes its receipt.

## Code Commentary

- A send builds one environment and one seat after the lock is released; a repeated request reconciles, and a closed seat is resumed rather than duplicated.
- An Update refuses while the lock is held or the explainer is in a turn, and an Update after a Retire is refused.
- A build faulted before the seat leaves no workspace, no binding and no seat, while a lost create reply reconciles to the same seat.
- A failed Retire stays pending and resumes its original receipt, pruning only grades whose references are gone.
- The recheck after the environment write lets a comparison that moved during the build win over the packet.

## Evidence

- The case `test_a_closed_seat_is_resumed_by_the_send_that_reaches_it` protects a closed seat being resumed by the send that reaches it. [1]
- The case `test_a_build_faulted_before_the_seat_rolls_back_every_effect` protects a faulted pre-seat build leaving zero partials. [3]
- The case `test_failed_retire_stays_pending_and_resumes_original_receipt_and_prunes_gone_grades` protects a failed Retire staying pending and resuming its own receipt. [4]
- The case `test_a_comparison_that_moves_during_the_build_wins_over_the_packet` protects a comparison that moved mid-build winning over the packet. [5]

- The case `test_an_update_refuses_while_the_lock_is_held` protects an Update refusing instead of waiting on a held lock. [2]
