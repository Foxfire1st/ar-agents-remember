# mcp/tests/test_knowledge_review_revision_selection.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

Pins revision-head selection without guessed winners: heads from retained revisions, never from order or presence.

## Code Commentary

The cases drive the real two-snapshot comparison over real snapshot pairs built through the
text-backed builder, then run the exact head-selection function the review adapter calls. A unique
single retained revision per side compares head to head; a known-empty side stays a one-sided
addition or removal with the nonempty side's head recorded (ICR-R06@v1); heads are the retained
population in sorted order, so collection order selects nothing; and the review pane renders the
selected head pair's own recorded statements. The multi-revision cases are removed and named, not
asserted: one side retaining several revisions is not a shape a text tree can express (rule 3).

Fixture construction uses test-only RowStore and revision containers, not a validating production
writer. The void case's empty side is an empty built file — an empty side cannot be authored as a
text revision.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References


- test_a_single_retained_revision_pair_compares_head_to_head supplies the current revision-selection assertion; no historical multi-revision measurement is claimed. [16]


- test_a_known_empty_after_side_stays_a_removal_with_the_before_head_recorded supplies the current revision-selection assertion; no historical multi-revision measurement is claimed. [17]


- test_heads_are_the_retained_population_in_sorted_order supplies the current revision-selection assertion; no historical multi-revision measurement is claimed. [18]


- `test_the_review_pane_renders_the_selected_head_pairs_own_statements` supplies the current fixture or assertion described above. [20]


- Fixture construction imports test-only row constructors; it does not call the retired canonical writer. [21]


- Test-only RowStore mutates a text tree and rebuilds its derived index; fixture authoring is not shipped write admission. [22]


- _select runs select_subject_revisions over the comparison page items and the fixture identity seed. [23]
- The module's own lane declaration, which is what makes the classification its own rather than a budget convenience. [24]
- STATEMENTS supplies the fixed statement strings used by the revision fixtures. [25]
- _select runs the adapter-owned head selection over one comparison union and requires an available selection. [26]
- The known-empty side: a removal under the R06 contract with the before head recorded and the after side absent. [30]
- The pane case: the served payload records the compared head pair and renders the heads' own recorded statements as `present`. [33]
- The evidence-lane catalogue registers test_knowledge_review_revision_selection.py. [34]
