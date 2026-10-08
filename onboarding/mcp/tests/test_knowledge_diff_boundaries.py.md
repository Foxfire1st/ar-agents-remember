# mcp/tests/test_knowledge_diff_boundaries.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Pins the bounded comparison response, independent record/source changes and honest unavailable observations.

## Code Commentary

The source declares fifteen test functions. They cover requested-tree expansion, visible unattributed gaps, side-specific realization evidence, display paging with whole-union totals, missing or changed snapshot/selector refusals, payload-field comparisons and separation of record changes from source observations. A read page is not reused as the comparison scope.

Serialized response checks exclude strengthening/harmlessness verdicts, mounted UI state, approval and severity. Paired unavailable/available probe substitutions distinguish an unmade observation from a measured gap. Index-shaped fixtures use test-only RowStore/revision helpers; payload substitution isolates the comparison projection and is not evidence of canonical writer duplicate_identity admission.

The old InventoryFixture/build_inventory_fixture six-case inventory population was removed. No current inventory-walk coverage or production store authoring is attributed to it.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- `test_a_small_display_budget_pages_the_comparison_without_shrinking_its_totals` supplies the current fixture or assertion described above. [26]
- `test_the_record_comparison_reports_exactly_the_payload_field_that_changed` supplies the current fixture or assertion described above. [27]
- `test_a_page_of_a_selection_is_what_the_comparison_displays_not_what_it_selected` supplies the current fixture or assertion described above. [28]
- `test_an_unavailable_observation_is_reported_as_unavailable_and_never_as_a_change_set` supplies the current fixture or assertion described above. [29]
- `test_a_probe_that_measured_the_trees_is_what_makes_a_gap_visible` supplies the current fixture or assertion described above. [30]
- Fixture construction imports test-only row constructors; it does not call the retired canonical writer. [31]
- RowStore inserts index-shaped fixture rows without the retired production admission plane. [32]
