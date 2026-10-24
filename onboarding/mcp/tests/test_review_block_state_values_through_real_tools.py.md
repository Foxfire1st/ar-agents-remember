# mcp/tests/test_review_block_state_values_through_real_tools.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Reaches every state value of the two result blocks — the sync rebinding block and the closeout and integration
receipts — through the real tools (MIK-R74 rule 7): current, moved, no-movement, not-measured, bound and
unmeasured, each with the trees that justify it.

## Code Commentary

### Logic

`_reviewed_closeout()` builds a closeout leaf with converted memory, a seeded memory line and a recorded
review; `_closed_reviewed_leaf()` builds the integrate leaf reviewed and closed out, so a receipt case starts
from a real owner history and a fresh production comparison.

- **Sync.** `test_sync_records_current_when_the_carried_line_leaves_both_trees`,
  `test_sync_records_moved_with_matching_code_on_a_memory_only_carry` and
  `test_sync_records_no_movement_when_the_pair_already_contains_the_line` cover current, moved and
  no-movement; `test_sync_records_not_measured_when_the_carry_fails` keeps a refused carry from producing a
  pair, and `test_sync_records_unmeasured_when_the_memory_capture_faults` stages one fault at the memory-candidate
  capture seam.
- **Closeout receipt.** `test_closeout_receipt_is_moved_when_its_own_memory_commit_differs`,
  `..._when_code_changes_after_review` and `..._for_a_memory_change_with_matching_code` show a receipt reads
  moved when the delivered memory commit or the code differs from what was reviewed.
- **Integration receipt.** `test_integration_receipt_is_bound_when_both_trees_match` requires a bound verdict
  when both trees match the reviewed pair, and `test_integration_receipt_is_moved_when_code_changes_after_review`
  reads moved when late code lands.

### Conventions

Each case lands a real change through the tool and reads the block the tool attaches, rather than calling the
comparison directly.

### Invariants And Boundaries

- A block's state is decided by the trees delivered, not by what the caller says it reviewed.
- A refused carry or a faulted capture reads not-measured or unmeasured; neither is reported as current.

## Evidence

- Sync records current when the carried line leaves both trees. [1]
- A closeout receipt reads moved when the code changes after review. [2]
- An integration receipt is bound when both trees match. [3]
- A memory capture fault records unmeasured. [4]
- Removed-mode behaviour is a named refusal, not a memory-free comparison. [5]
- A differing-byte carry retains the refusal block's original not-measured and non-covering assertions. [6]
- The real owner history is closed and a fresh production comparison taken before closeout, with the original receipt assertions intact. [7]
