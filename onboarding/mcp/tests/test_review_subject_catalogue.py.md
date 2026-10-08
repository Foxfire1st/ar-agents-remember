# mcp/tests/test_review_subject_catalogue.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

Pins the union, presence, totals, bounded loading and reviewability of a complete subject catalogue.

## Code Commentary

The shared diff fixture is copied and extended for retired, added and bare identities. RowStore and revision constructors come from test-only knowledge_rows_test_support; `_insert_bare_identity` inserts fixture identity rows. It is not a shipped batch insert_invariant_identity operation or proof of production append-only admission.

Production catalogue/entry/review composition checks kind grouping including before-only identities, one-sided statements, family listing without a statement side, every offered row's reviewability and a reason-carrying refusal for an unselectable bare identity. Neighbour reviews remain accessible. Entry totals describe the whole catalogue, an empty catalogue coexists with a measured source inventory, and bounded loading is protected by comparison bindings patched to raise. Browser traversal and relationship/roster paging belong to their separate owners.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- `test_the_catalogue_stays_kind_grouped_when_retired_subjects_exist` supplies the current fixture or assertion described above. [10]
- `test_every_catalogue_row_opens_through_the_normal_review` supplies the current fixture or assertion described above. [11]
- `test_a_recorded_but_unselectable_subject_is_listed_and_its_open_carries_the_reason` supplies the current fixture or assertion described above. [12]
- `test_zero_subjects_is_a_valid_catalogue_beside_the_source_inventory` supplies the current fixture or assertion described above. [13]
- `test_catalogue_loading_runs_no_comparison` supplies the current fixture or assertion described above. [14]
- Fixture construction imports test-only row constructors; it does not call the retired canonical writer. [15]
- RowStore inserts index-shaped fixture rows without the retired production admission plane. [16]
