# mcp/tests/test_review_final_output_receipt.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Pins final-output receipts bound to retained code and memory tree comparisons.

## Code Commentary

TreeReceiptFixture creates real temporary code/memory Git repositories, captures their two-tree comparison through the existing owners and passes committed results to receipt attachment/read functions. It calls receipt owners directly; it does not perform the former end-to-end canonical dataset freeze, closeout or integration journeys.

Six current test functions assert both delivered-tree matches and result keys, moved/absent memory or code coverage, unavailable/corrupt comparison handling without blocking an already completed result, forged source binding and leaf scoping, immutable previous receipts labelled by a successor, and readable historical v1 receipts with an explicit lack of memory-tree proof. The former eleven-journey/module-node account is removed coverage. No receipt here supplies semantic acceptance.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- `TreeReceiptFixture` supplies the current fixture or assertion described above. [19]
- `test_receipts_bind_both_delivered_trees_and_keep_both_result_keys` supplies the current fixture or assertion described above. [20]
- `test_memory_movement_and_absent_memory_never_claim_delivered_coverage` supplies the current fixture or assertion described above. [21]
- `test_source_forgery_is_refused_and_receipts_are_leaf_scoped` supplies the current fixture or assertion described above. [22]
- `test_historical_v1_receipt_remains_readable_without_claiming_memory_tree_proof` supplies the current fixture or assertion described above. [23]
