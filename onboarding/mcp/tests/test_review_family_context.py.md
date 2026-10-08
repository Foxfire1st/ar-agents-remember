# mcp/tests/test_review_family_context.py

## Governing Overview

[mcp tests route overview](overview.md)

## Purpose

Pins exact family guarantees, memberships and bounded roster continuation in review context.

## Code Commentary

Recorded family revisions supply their own guarantees and memberships; a successor roster is not inherited. Shared members retain canonical revision identity across contexts, and repeated memberships do not inflate the distinct source population. A member change exposes its family context without declaring a guarantee change or an intent verdict.

The suite distinguishes measured no-family, absent knowledge, no selected subject, one-sided families and ambiguous family lineage. Roster truncation preserves owner counts and its continuation; tokens bind their exact walk, final pages carry only their share, and a multi-page walk terminates without loss. The client route assertions exercise the production adapter.

Family/revision/membership inputs are inserted by test-only knowledge_rows_test_support. Those fixtures do not enforce the former canonical family authoring plane. Current guarantees and roster meanings are read from exact supplied rows by the surviving production readers.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- `test_a_successor_family_revision_is_read_from_its_own_rows_not_inherited` supplies the current fixture or assertion described above. [42]
- `test_a_shared_member_is_one_canonical_revision_referenced_in_two_contexts` supplies the current fixture or assertion described above. [43]
- `test_missing_knowledge_is_the_reviews_refusal_not_an_empty_family_context` supplies the current fixture or assertion described above. [44]
- `test_the_published_cursor_continues_exactly_the_walk_that_minted_it` supplies the current fixture or assertion described above. [45]
- `test_a_roster_walk_larger_than_one_page_terminates_with_a_page_and_no_failure` supplies the current fixture or assertion described above. [46]
- Fixture construction imports test-only row constructors; it does not call the retired canonical writer. [47]
- RowStore inserts index-shaped fixture rows without the retired production admission plane. [48]
