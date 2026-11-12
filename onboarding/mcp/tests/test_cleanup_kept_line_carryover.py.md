# mcp/tests/test_cleanup_kept_line_carryover.py

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Kept-line carryover: no recovery leaf where both tips sit on a kept line.

## Code Commentary

MIK-R82 rule 5: an integrated leaf whose ledger shows no carryover is still refused where a tip sits on neither kept line, and finishes without a recovery leaf where both tips sit on one. The branch check takes the same proof.

## Evidence


- Kept-line carryover and refusal cases are pinned. [1]
