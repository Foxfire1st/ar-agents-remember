# mcp/tests/test_knowledge_review_relationship_line.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

Pins relationship disclosure across a selected subject's complete retained successor line.

## Code Commentary

A split or multi-head line displays relationships actually recorded in that line without claiming a unique head or denying displayed evidence. A line recording no relationships states only what was read. Intermediate descendants and memberships moved to an unselected family revision remain visible.

Datasets are copied from the shared fixture and extended with test-only family/revision/membership constructors from knowledge_rows_test_support. Production review readers perform line/head selection and disclosure; those fixture inserts provide no canonical write admission guarantee.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- `test_a_split_line_that_records_relationships_names_them_and_never_denies` supplies the current fixture or assertion described above. [11]
- `test_a_multi_head_line_with_relationships_never_claims_a_unique_head` supplies the current fixture or assertion described above. [12]
- `test_a_relationship_on_an_intermediate_descendant_is_displayed` supplies the current fixture or assertion described above. [13]
- `test_a_membership_moved_onto_an_unselected_family_revision_is_displayed` supplies the current fixture or assertion described above. [14]
- Fixture construction imports test-only row constructors; it does not call the retired canonical writer. [15]
- RowStore inserts index-shaped fixture rows without the retired production admission plane. [16]
