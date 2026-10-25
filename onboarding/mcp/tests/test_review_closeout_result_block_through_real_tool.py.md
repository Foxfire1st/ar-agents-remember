# mcp/tests/test_review_closeout_result_block_through_real_tool.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Holds the one result block the real `worktree_closeout_apply` tool attaches (ICR-R21, ICR-R23): the
delivered receipt together with the boundary statement. It drives the tool rather than a helper, so the block
a caller receives is the one production builds.

## Code Commentary

### Logic

`test_the_real_closeout_apply_attaches_the_delivered_receipt_and_the_boundary_statement` builds a memory
fixture, calls the registered `worktree_closeout_apply`, and checks the answer carries both the delivered
receipt and the boundary statement produced by `review_tree_comparison` and
`worktrees.modules.future_code_candidate`.

### Conventions

The case goes through the tool surface with the real worktree modules bound, so a change in the attached block
is visible where a caller reads it.

### Invariants And Boundaries

- The closeout result is one block: a delivered receipt plus a boundary statement, not two separate answers.

## Evidence


- The file realizes its current contract at the corrected candidate. [1]
