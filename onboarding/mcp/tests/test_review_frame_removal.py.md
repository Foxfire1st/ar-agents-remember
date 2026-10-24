# mcp/tests/test_review_frame_removal.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The developer's removal of retained revisions is one store act: it deletes and receipts, never reissues the number, and refuses the pinned agreed revision.

## Code Commentary

- A chosen revision is deleted and receipted, and its number is never issued again; a second removal of the same number refuses with the first receipt still explaining it.
- The pinned agreed revision is refused even inside a batch and still reads when its neighbours go.
- A revision a retained revision's lineage names is refused, and what remains still reads: manifest, binding, parent chain, served asset and ready pointer.
- Retention has no count bound while the per-revision byte ceiling still refuses one revision, and a removal under a held lock answers a typed refusal instead of hanging.

## Evidence

- The case `test_a_chosen_revision_is_removed_receipted_and_its_number_is_never_reissued` protects a removed revision being receipted and its number never reissued. [1]
- The case `test_the_pinned_agreed_revision_is_never_removed_and_still_reads` protects the pinned agreed revision being refused and still readable. [2]
- The case `test_a_revision_a_retained_lineage_names_is_refused` protects a revision a retained lineage names being refused. [3]
- The case `test_retention_and_the_per_revision_ceiling_still_hold_after_a_removal` protects retention and the per-revision ceiling holding after a removal. [4]
- The case `test_a_removal_under_a_held_lock_refuses_instead_of_waiting` protects a removal refusing under a held lock rather than waiting. [5]
