# mcp/tests/test_memory_review_lane.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Keeps a product task-document's memory review in its own lane: a memory record answers through the Curator
lane without reopening code that already passed, a memory baseline after a code pass is independent and
persisted, and a memory record binds memory bytes rather than code bytes. Generic task mutations can neither
author nor erase the lane, and an invalid kind or an incomplete count fails closed.

## Code Commentary

### Logic

`launch_world` from `paseo_launch_test_support` provides the launch fixture, `_memory_config()` builds the
memory-side configuration, and the cases drive `task_doc_route_review`, `task_doc_tools`, `task_review_step_up`,
`route_review`, `launch_review_read` and the review history.

- **Independent lane.** `test_memory_record_answer_uses_curator_lane_without_reopening_passed_code` and
  `test_memory_baseline_after_code_pass_is_independent_and_persisted` keep the memory answer and its baseline
  independent of the code pass.
- **What is bound.** `test_memory_record_only_binds_memory_bytes_not_code_bytes` binds memory bytes only, and
  `test_memory_lane_strict_reader_and_launch_only_diagnostic_preserve_raw_state` keeps the strict reader and
  the launch-only diagnostic from rewriting state.
- **Who may write.** `test_memory_lane_cannot_be_authored_or_erased_by_generic_task_mutations` and
  `test_memory_candidate_authority_uses_contract_or_configured_fallback_only` bound the lane to the contract or
  the configured fallback, and `test_memory_kind_cannot_publish_code_route_evidence` stops a memory record
  publishing code-route evidence.
- **Counting.** `test_product_memory_threshold_own_limits_approval_and_shrinking_list` gives the memory
  threshold its own limits and approval, `test_legacy_mixed_code_records_are_not_migrated_into_curator_count`
  keeps mixed legacy records out of the curator count, and
  `test_invalid_kinds_and_incomplete_memory_count_fail_closed` fails closed.

### Conventions

The launch-world step-up case asserts on the review record its launch persisted; the task-document cases
read the review state back from the document they wrote; the pure model and authority cases judge
documents built in memory, without a launch world or a persisted review.

### Invariants And Boundaries

- A memory review never reopens a passed code record, and the code lane never writes the memory lane.
- An unknown kind or an incomplete count refuses; it is not defaulted.

## Evidence

- A memory record answers through the Curator lane without reopening passed code. [1]
- A memory baseline after a code pass is independent and persisted. [2]
- A memory record binds memory bytes, not code bytes. [3]
- The strict reader and launch-only diagnostic preserve raw state. [4]
- The memory lane cannot be authored or erased by generic task mutations. [5]
- Memory candidate authority comes from the contract or the configured fallback only. [6]
- A memory kind cannot publish code-route evidence. [7]
- The product memory threshold has its own limits, approval and shrinking list. [8]

- Source assertion: test_legacy_mixed_code_records_are_not_migrated_into_curator_count. The declaration is not an execution receipt — `test_legacy_mixed_code_records_are_not_migrated_into_curator_count` in mcp/tests/test_memory_review_lane.py. [9]
- Source assertion: test_invalid_kinds_and_incomplete_memory_count_fail_closed. The declaration is not an execution receipt — `test_invalid_kinds_and_incomplete_memory_count_fail_closed` in mcp/tests/test_memory_review_lane.py. [10]
