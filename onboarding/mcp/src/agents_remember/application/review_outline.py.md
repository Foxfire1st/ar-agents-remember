# mcp/src/agents_remember/application/review_outline.py

## Governing Overview

[application overview](overview.md)

## Purpose

`review_outline` builds the comparison's complete navigation tree — every family with its members and every invariant with its change — from the two derived memory indexes only. It reads no blob, no hunk classification, no roster page and no subject review.

## Code Commentary

`read_review_outline` opens the resolved baseline and candidate index databases and delegates to `_outline`; a missing converted memory (`trees is None`) or an unreadable index yields `unavailable` with the reason, and an unavailable outline never carries a partial tree. `_outline` registers both sides' records once in a shared `RecordChanges`, then walks families and invariants in candidate order followed by baseline-only identities (the catalogue's order). Families carry title, guarantee change and members in the family record's order with `both`/`joined`/`left`; invariants carry a word-cut 120-character statement summary and the intent change. Unknown membership fails the whole outline to `unavailable` with the joined reasons rather than guessing a tree.

## Evidence

- The tree is enumerated without source, roster or subject reads [1]
- Both sides' records are registered once for shared meaning facts [2]
- Members follow the family record's order with join/leave facts [3]
- Summaries cut at 120 characters on word boundaries [4]
