# mcp/tests/test_knowledge_review_relationship_line.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

No authored line: retractions state what was read, and moved-to sides outside the union stay out.

## Code Commentary

The module owns the shapes the old line search used to follow past the union's page and pins what
the rule-1 display does with them instead: two further revisions each recording a realization
display as a retraction stating that no relationship citing their revision was read; a claim at an
intermediate further revision gets the same retraction; a membership recorded again under another
family revision displays the withdrawn baseline side as its own retraction. No line is read, no
head is established, and no succession, split or merge is stated.

Datasets are built through the rows builder with test-only family/revision/membership constructors
from knowledge_rows_test_support. Those fixture writes provide no canonical write admission guarantee.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- `test_two_further_revisions_that_record_relationships_are_a_retraction_and_never_denied` supplies the current fixture or assertion described above. [11]
- `test_two_unpaired_rows_are_two_absences_and_never_a_unique_head` supplies the current fixture or assertion described above. [12]
- `test_a_further_revision_outside_the_union_states_only_what_was_read` supplies the current fixture or assertion described above. [13]
- `test_a_relationship_at_a_further_revision_outside_the_union_is_not_displayed` supplies the current fixture or assertion described above. [14]
- `test_a_membership_recorded_again_under_another_family_revision_is_a_retraction` supplies the current fixture or assertion described above. [15]
- Fixture construction imports test-only row constructors; it does not call the retired canonical writer. [16]
- RowStore writes text-tree fixture rows without the retired production admission plane. [17]
