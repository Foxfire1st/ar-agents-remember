# mcp/tests/test_knowledge_review_revision_selection.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

Pins revision-head selection without guessed winners: heads from retained revisions, never from order or presence.

## Code Commentary

The cases drive the real two-snapshot comparison over real snapshot pairs built through the
text-backed builder, then run the exact head-selection function the review adapter calls. The three tests cover a
single retained revision per side comparing head to head, a known-empty after side remaining a
removal with the before head recorded (ICR-R06@v1), and the review pane rendering the selected
head pair's own recorded statements. They do not measure sorted multi-revision populations or
multi-revision selection; the fixture requires exactly one revision per side (rule 3).

Fixture construction uses test-only RowStore and revision containers, not a validating production
writer. The void case's empty side is an empty built file — an empty side cannot be authored as a
text revision.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References








- `test_the_review_pane_renders_the_selected_head_pairs_own_statements` supplies the current fixture or assertion described above. [20]


- Fixture construction imports test-only row constructors; it does not call the retired canonical writer. [21]


- Test-only RowStore mutates a text tree and rebuilds its derived index; fixture authoring is not shipped write admission. [22]


- The module's own lane declaration, which is what makes the classification its own rather than a budget convenience. [24]
- STATEMENTS supplies the fixed statement strings used by the revision fixtures. [25]
- _select runs the adapter-owned head selection over one comparison union and requires an available selection. [26]
- The known-empty side: a removal under the R06 contract with the before head recorded and the after side absent. [30]
- The pane case: the served payload records the compared head pair and renders the heads' own recorded statements as `present`. [33]
- The evidence-lane catalogue registers test_knowledge_review_revision_selection.py. [34]

- The single retained revision pair compares head to head and records that revision as the sole head on both sides. [16]
- A known-empty after side produces a removal with the before revision recorded, no after revision and no after heads. [17]
- _select calls select_subject_revisions with the comparison page items and fixture identity seed, requires an available selection and returns it. [23]
