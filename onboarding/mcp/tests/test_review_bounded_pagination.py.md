# mcp/tests/test_review_bounded_pagination.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

Pins bounded review-record and matrix walks, exact continuation scope and entry-read laziness.

## Code Commentary

Eight test functions cover a complete one-page comparison, long walks without duplication/loss, partitioned item windows, the matrix walk named by the records collection, foreign/snapshot-mismatched records cursors, a moved generation requiring fresh selection, transport page bounds and the entry read's refusal to fetch record pages.

The fixture copies shared index-shaped populations and adds realization rows through test-only knowledge_rows_test_support. Production review/page composition is read back; fixture authoring names are not shipped storage admission. The deleted remainder-test population and former twelve-case coverage account are historical, not assertions supplied by this module.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- `test_every_page_of_a_large_comparison_is_reachable_without_duplicate_or_loss` supplies the current fixture or assertion described above. [21]
- `test_the_records_collection_states_the_matrix_walk_and_the_bound_it_applied` supplies the current fixture or assertion described above. [22]
- `test_a_cursor_from_a_moved_generation_is_refused_with_a_new_generation_action` supplies the current fixture or assertion described above. [23]
- `test_the_entry_read_populates_the_button_without_fetching_record_pages` supplies the current fixture or assertion described above. [24]
- Fixture construction imports test-only row constructors; it does not call the retired canonical writer. [25]
- RowStore inserts index-shaped fixture rows without the retired production admission plane. [26]
