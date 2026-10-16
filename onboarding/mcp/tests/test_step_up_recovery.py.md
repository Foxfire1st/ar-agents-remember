# mcp/tests/test_step_up_recovery.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Step-up retry/archive safety, durable takeover evidence and bounded Git inventory recovery.

## Code Commentary

Both saved retry and history recovery renew predecessor liveness immediately before archive: active turn, permission prompt and unreachable host prevent archive/create, then idle retry succeeds. Registered role_start empty-seat rejection directs the same request/selection while ordinary nonretryable failure still names a new request. Receipt-loss/unconfirmed controls retain known versus unknown applied predecessor. Takeover artifacts restore missing original bytes or refuse changed/symlink/directory/FIFO; write-once/read-only publication checks opened-file regularity. Real disposable Git populations exercise file/byte caps. The hung-child case asserts that the captured child exited by signal (negative return code), incomplete inventory/recovery was retained and a following Reviewer start can acquire the lock. It no longer uses elapsed < 1 as a whole-start performance oracle; the injected per-root inventory timeout remains. These are assertions about a disposable subprocess and fake host, not universal cleanup or latency guarantees.

## Evidence Boundaries

- When executed, these assertions combine actual subprocess/file/registered-tool seams with a fake host; the source distinguishes partial inventory from complete.
- Positive controls preserve same-request recovery after damage restoration, and no-call negative assertions guard host effects.
- No real actor is started or archived, and no atomic remote host lease is asserted.
- Bounded Git subprocess tests are not an exhaustive process/race/resource proof or Dagger certification.

This card describes assertion/support/document source, not a test invocation, independent verdict or publication.

## Evidence

- Source assertion: test_archive_renews_predecessor_read_on_every_recovery. The declaration is not an execution receipt. [1]
- Source assertion: test_retryable_empty_seat_tool_answer_preserves_same_request. The declaration is not an execution receipt. [2]
- Source assertion: test_nonretryable_tool_rejection_keeps_new_request_guidance. The declaration is not an execution receipt. [3]
- Source assertion: test_receipt_loss_uses_durable_applied_destination_in_takeover. The declaration is not an execution receipt. [4]
- Source assertion: test_unconfirmed_prior_destination_does_not_claim_the_configured_base. The declaration is not an execution receipt. [5]
- Source assertion: test_saved_takeover_material_is_restored_or_refused_before_create. The declaration is not an execution receipt. [6]
- Source assertion: test_git_inventory_has_explicit_file_budget. The declaration is not an execution receipt. [7]
- Source assertion: test_git_inventory_caps_bytes_before_serialization. The declaration is not an execution receipt. [8]
- Source assertion: test_takeover_publication_is_write_once_and_checks_the_open_file. The declaration is not an execution receipt. [9]
- The hung-child source case checks signal termination/reaping, durable partial recovery and later lock reuse, not an elapsed whole-start deadline. [10]

