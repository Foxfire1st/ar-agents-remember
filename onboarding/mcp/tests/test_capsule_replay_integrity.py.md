# mcp/tests/test_capsule_replay_integrity.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Replay and delayed held-seat integrity of frozen instruction detail artifacts.

## Code Commentary

Builds two frozen details through real launch composition and checks every saved revision, missing/symlink/directory/FIFO refusal, canonical report-folder rebound and malformed reference refusal while allowing detail-free legacy receipts. Saved-start replay reaches a fake host seam with good bytes, then refuses missing detail before any call. Held opening similarly rejects changed detail and leaves the waiting claim recoverable.

## Evidence Boundaries

- The source assertions bind frozen bytes and canonical report access without regenerating from mutable current corpus.
- Positive controls reach a deliberately stopping fake-host boundary; negative controls assert no call and recoverable receipt/queue state.
- No native agent is created, opened or consumed by a model.
- Regular-open/canonical checks are bounded to the tested paths; there is no universal filesystem race proof or authority to silently repair corrupted frozen bytes.

This card describes assertion/support/document source, not a test invocation, independent verdict or publication.

## Evidence

- Source assertion: test_replay_checks_every_frozen_revision_without_reading_the_current_corpus. The declaration is not an execution receipt. [1]
- Source assertion: test_replay_refuses_missing_or_nonregular_detail_targets. The declaration is not an execution receipt. [2]
- Source assertion: test_replay_refuses_a_rebound_report_folder_even_when_detail_bytes_are_unchanged. The declaration is not an execution receipt. [3]
- Source assertion: test_replay_refuses_incomplete_detail_references_instead_of_skipping_them. The declaration is not an execution receipt. [4]
- Source assertion: test_saved_start_replay_refuses_missing_details_before_the_host_call. The declaration is not an execution receipt. [5]
- Source assertion: test_held_opening_refuses_changed_details_and_preserves_waiting_messages. The declaration is not an execution receipt. [6]
