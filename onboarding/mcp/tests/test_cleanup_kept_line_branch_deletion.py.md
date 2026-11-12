# mcp/tests/test_cleanup_kept_line_branch_deletion.py

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Kept-line branch deletion through to the deleted branches.

## Code Commentary

MIK-R82 rule 5 with the assignment scope-boundaries ruling: a work branch whose tip is reachable from the landing line or the default line is deleted even where its master's line does not hold the tip. The kept-line test runs through to the deleted branches; the refused real run is kept as its limit.

## Evidence

- Kept-line branch deletion to the deleted branches is pinned. [1]
