# mcp/tests/test_review_family_member_sources.py

## Governing Overview

[mcp tests route overview](overview.md)

## Purpose

Pins each family member's recorded source locator and the range resolved in its exact selected Git blob.

## Code Commentary

The fixture inserts realization rows through test-only knowledge_rows_test_support and creates real source commits. Production read_family_roster and its side-selected anchor resolver supply the output. Construction through the test namespace is not a production realization write or admission check.

Assertions preserve per-member role/rationale and distinguish symbol/range resolution, whole-file locators, missing or stale locators and ranges beyond the recorded blob. A symbol defined twice carries both defining ranges. Changing a file can preserve an unchanged attributed range on both sides; the existing source fields retain their wire values beside the structured locator fields. No range is inferred by parsing a detail sentence.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- `test_two_members_in_one_file_carry_their_own_locators_ranges_and_rationale` supplies the current fixture or assertion described above. [15]
- `test_a_changed_file_keeps_its_unchanged_attributed_range_on_each_side` supplies the current fixture or assertion described above. [16]
- `test_an_unresolved_locator_is_stated_with_its_recorded_locator_and_no_range` supplies the current fixture or assertion described above. [17]
- `test_a_symbol_defined_twice_carries_every_defining_range` supplies the current fixture or assertion described above. [18]
- `test_the_existing_source_fields_keep_their_published_values` supplies the current fixture or assertion described above. [19]
- Fixture construction imports test-only row constructors; it does not call the retired canonical writer. [20]
- RowStore inserts index-shaped fixture rows without the retired production admission plane. [21]
