# mcp/tests/test_review_result_blocks_through_real_tools.py

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Tests for the review result blocks through real tools.

## Code Commentary

The sync case checks the moved pair's rebinding through the real sync tool. The
integration case writes a canonical converted-memory layout and checks the
delivered receipt through the real integrate tool.

`_integrate_without_item_judgment` replaces only the worklist-items judgment
(`closeout_external.leaf_gate_refusal`) while the validator and receipt assertions
run for real. It is shared with the block-state cases. Their disposable scaffold
hunks do not establish invariant coverage, and this receipt-focused seam is not
evidence that an uncovered leaf passes the real worklist gate.

## Evidence

- The helper stubs only item judgment; the integration case still checks the delivered receipt through the real tool. [2]


- Real sync rebinding and delivered integration receipt are checked in this module; item judgment is explicitly substituted for the receipt case. [1]
