# mcp/tests/test_review_block_state_values_through_real_tools.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**Selected receipt and rebinding state values through the real tools.** The receipt block
(`final_output_receipt`) is exercised via `worktree_closeout_apply` and `worktree_integrate`;
the rebinding block (`review_rebinding`) via `worktree_sync`. Each case builds its reviewed
leaf through the existing result-block fixture and asserts its own selected match/verdict
fields. Bound cases assert both channels; moved-code receipt cases assert the code mismatch
and moved verdict without a memory-match assertion. This module does not cover every valid
outcome: no-comparison and not-recorded outcomes remain outside this selected population.

## Code Commentary

Ruling 814778 narrowed the v2 receipt to measured values only (`bound`/`moved`); a delivery without a memory commit writes no receipt. The rebinding keeps its `unmeasured` match and verdict with a staged-fault case. The removed memory-disabled mode has no comparison case here; its named refusal boundary is held by `test_memory_opt_out_refused_start.py` and `test_memory_opt_out_refused_routes.py`. Both blocks compare trees, never branch history: a rebase ending in the same tree reads as the same.

The integration receipt fixtures write `knowledge/layout.json` in canonical text.
Their shared `_integrate_without_item_judgment` helper stubs only
`closeout_external.leaf_gate_refusal`: uncovered scaffold worklist items are outside
these receipt cases. The knowledge validator and real integration tool still run,
and bound/moved receipt assertions remain unchanged. These cases are not proof of
worklist-item judgment acceptance.

The refused-carry case parks `SAME = 1` while the landed line holds `SAME = 2`; it invokes the public sync tool and keeps the original assertions that `review_rebinding.state` is `not-measured` and `covers_resolved_pair` is false. The different-byte scenario is deliberate: the separately owned parked-candidate case exercises an identical-byte successful carry and asserts a `current` rebinding block. A refused sync is not upgraded to current, and branch movement alone is not tree mismatch. Source assertions describe the cases; execution receipts remain separately owned.


## MIK-R46 R8: compare the closed history before closeout

`_closed_reviewed_leaf` retains the initial real review-tree capture, then closes LEAF-C's owner history through `close_owner_history`. It takes another production `live_review_trees` comparison using a fresh code capture and requires a real `ReviewTrees` before `close_out_leaf`. The reviewed memory now includes the closed history that closeout delivers; no fabricated receipt or relaxed bound/moved assertion replaces that comparison. The separately documented item-gate fixture seam and selected-outcome limits remain.


## Evidence

### Current Source-Inspection References

- Sync records current when the line leaves both trees [1]
- Closeout receipt is moved when code changes after review [2]
- Integration receipt is bound when both trees match [3]
- Memory capture fault records unmeasured [4]
- Removed-mode behavior is a named refusal, not a memory-free comparison. [5]
- A differing-byte carry retains the refusal block's original not-measured and non-covering assertions. Receipt fixtures retain canonical layout and real receipt assertions while sharing the explicit items-judgment seam. [6]

- Close the real owner history and take a fresh production comparison before closeout; original receipt assertions remain. [7]
