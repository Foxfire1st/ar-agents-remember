# mcp/tests/test_review_subject_catalogue.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

Pins the union, presence, totals, bounded loading and reviewability of a complete subject catalogue.

## Code Commentary

The shared diff fixture is extended through the text-backed builder for retired and added whole invariants: populations that differ from the shared fixture carry whole extra invariants built into the side that records them. Every identity a case asserts against is the projection's own UUID for the text it wrote. It is not a shipped operation or proof of production append-only admission.

Production catalogue/entry/review composition checks kind grouping including before-only identities, one-sided statements, family listing without a statement side, every offered row's reviewability and the currently reviewable recorded subjects. The bare identity with no authored content and its old reason-carrying refusal are removed historical fixture shapes, not current executable coverage. Neighbour reviews remain accessible. Entry totals describe the whole catalogue, an empty catalogue coexists with a measured source inventory, and bounded loading is protected by comparison bindings patched to raise. Browser traversal and relationship/roster paging belong to their separate owners.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- `test_the_catalogue_stays_kind_grouped_when_retired_subjects_exist` supplies the current fixture or assertion described above. [10]
- `test_every_catalogue_row_opens_through_the_normal_review` supplies the current fixture or assertion described above. [11]
The former `test_a_recorded_but_unselectable_subject_is_listed_and_its_open_carries_the_reason`
was removed with the unselectable bare-identity fixture shape. Its historical name is retained here as
a withdrawal disclosure, not a current assertion or a renamed guarantee.
- `test_zero_subjects_is_a_valid_catalogue_beside_the_source_inventory` supplies the current fixture or assertion described above. [13]
- `test_catalogue_loading_runs_no_comparison` supplies the current fixture or assertion described above. [14]
- Fixture construction imports test-only row constructors; it does not call the retired canonical writer. [15]
- RowStore writes text-tree fixture rows without the retired production admission plane. [16]
