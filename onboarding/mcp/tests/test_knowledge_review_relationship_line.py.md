# mcp/tests/test_knowledge_review_relationship_line.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose
Pins relationship disclosure across a selected subject's complete retained successor line.

## Code Commentary
A split or multi-head line displays relationships actually recorded in that line without claiming a unique head or denying displayed evidence. A line recording no relationships states only what was read. Intermediate descendants and memberships moved to an unselected family revision remain visible.

Datasets are copied from the shared fixture and extended with test-only family/revision/membership constructors from knowledge_rows_test_support. Production review readers perform line/head selection and disclosure; those fixture inserts provide no canonical write admission guarantee.

### Logic
**Five cases, one distinct user operation each:**

- `test_a_split_line_that_records_relationships_names_them_and_never_denies` — the round-2 F1 fix: the
  lineage sentence names both successors, the rows recorded on them are displayed as their own
  movements, and no denial clause is emitted.
- `test_a_multi_head_line_with_relationships_never_claims_a_unique_head` — the round-3 F5 fix: a
  multi-ended line has no head, so neither row's sentence may say "uniquely established head"; each
  names the line that was read and the revision it records.
- `test_a_split_line_that_records_nothing_states_only_what_was_read` — the negative is complete over
  the revisions that were read, and nothing more is claimed.
- `test_a_relationship_on_an_intermediate_descendant_is_displayed` — the round-2 F3 fix: the whole line
  is read, not just its head.
- `test_a_membership_moved_onto_an_unselected_family_revision_is_displayed` — the family side is read
  through the family-revision owner, so the new side is displayed with its pairing basis.

### Invariants And Boundaries
- **The whole authored line is read**, so a relationship at an intermediate descendant is displayed and
  a stated negative is complete over the revisions that were read.
- **A head is named only where one exists**: a multi-ended or cyclic line has none, so no sentence may
  claim one, and the row's basis sentence names the line it read and the revision it records.
- **No sentence denies what the same payload displays**, and the family side is read through the owner
  keyed by the family revision, so no sibling member is mis-named.
- **Boundaries.** The ruling's member-head and multi-head *reach* cases live in the reach module; this
  module owns the authored-line consequences; browser mounting is `ICR-R24`'s and the acceptance
  journey `ICR-R25`'s.

### Todos
None recorded.

## Evidence

### Repo-Internal References

Every claim on this card is checkable in the uncommitted candidate: the module's own docstring, the
three fixture builders and the five cases.

- `test_a_split_line_that_records_relationships_names_them_and_never_denies` supplies the current fixture or assertion described above. [11]
- `test_a_multi_head_line_with_relationships_never_claims_a_unique_head` supplies the current fixture or assertion described above. [12]
- `test_a_relationship_on_an_intermediate_descendant_is_displayed` supplies the current fixture or assertion described above. [13]
- `test_a_membership_moved_onto_an_unselected_family_revision_is_displayed` supplies the current fixture or assertion described above. [14]
- Fixture construction imports test-only row constructors; it does not call the retired canonical writer. [15]
- RowStore inserts index-shaped fixture rows without the retired production admission plane. [16]

- The module's own statement of the three shapes it owns and of the read-back the cases use. [17]
- The fixtures that author an intermediate descendant, a split with relationships on both successors, and a membership moved onto a successor family revision. [18]
- **The split line that names its recorded relationships and never denies them (round-2 F1).** [19]
- **The multi-ended line that never claims a unique head (round-3 F5).** [20]
- The split that records nothing: only what was read is claimed. [21]
- **The relationship recorded on an intermediate descendant is displayed (round-2 F3).** [22]
- The membership moved onto an unselected successor family revision, read through the family-revision owner. [23]
- The display sentences these cases pin, and the pairing bases the head rule chooses between. [24]
- The whole-line read and the head rule the cases measure. [25]
- The sibling case module this one imports its builders from, and the reach fixture it reuses. [26]

### Docs References

No Domain Documentation source is configured for this slice.

### Cross-Repo References

No cross-repository behavior is exercised in this file.

No applicable cross-repository source was found.
