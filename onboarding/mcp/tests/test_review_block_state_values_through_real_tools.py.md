# mcp/tests/test_review_block_state_values_through_real_tools.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R74 rule 7: every reachable state value of the two result blocks, through the real tools.** The receipt block (`final_output_receipt`) via `worktree_closeout_apply` and `worktree_integrate`; the rebinding block (`review_rebinding`) via `worktree_sync`. Each case builds its reviewed leaf the way the existing result-block cases do — the product records the comparison itself — and asserts the exact channel matches and verdict the real tool attaches.

## Code Commentary

Ruling 814778 narrowed the v2 receipt to measured values only (`bound`/`moved`); a delivery without a memory commit writes no receipt. The rebinding keeps its `unmeasured` match and verdict with a staged-fault case, and a memory-disabled leaf records no tree comparison at all. Both blocks compare trees, never branch history: a rebase ending in the same tree reads as the same.

## Evidence

- Sync records current when the line leaves both trees [1]
- Closeout receipt is moved when code changes after review [2]
- Integration receipt is bound when both trees match [3]
- Memory capture fault records unmeasured [4]
- A memory-disabled leaf records no comparison [5]
