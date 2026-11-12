# mcp/src/agents_remember/models/knowledge/review_outline.py

## Governing Overview

[models overview](../overview.md)

## Purpose

`models/knowledge/review_outline.py` fixes the index-only navigation outline of a review comparison: every family with its members and every invariant with its change, in an `outlined` tree or an `unavailable` reason that never carries a partial tree.

## Code Commentary

### Recorded reviewer judgments

Every family, member and invariant outline row carries a required ReviewOutlineMeaning. Its steps/none/unavailable state is distinct from OutlineChange; labels are present only for steps and retain authored attempt order. This is display of recorded history, not a label inferred from the change enum, guarantee or member data. An unavailable whole outline still carries no partial tree.

- Every family, member and invariant outline row carries a required ReviewOutlineMeaning. [5]

`OutlineChange` is the five-way meaning vocabulary (added, removed, changed, unchanged, unknown). `ReviewOutlineMember` pairs the review-opening `selector_id` with the record id and `both`/`joined`/`left`; `ReviewOutlineFamily` adds title, change and authored-order members; `ReviewOutlineInvariant` adds the 120-character statement summary. `ReviewOutline` is `outlined` with the two lists or `unavailable` with a non-empty detail, enforced by `_unavailable_lists_nothing` so a failure carries its reason and never a half tree.

## Evidence

- Members pair selector identity with join/leave membership [1]

- Families carry title, change and ordered members [2]
- The tree is outlined content or an unavailable reason [3]
- An unavailable outline never carries a partial tree [4]
