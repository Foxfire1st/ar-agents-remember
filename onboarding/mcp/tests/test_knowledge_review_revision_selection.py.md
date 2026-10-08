# mcp/tests/test_knowledge_review_revision_selection.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

Pins revision-head selection without guessed winners, including explicitly damaged fixture graphs.

## Code Commentary

A unique successor chain defaults to the before head and after head, while an intermediate revision remains explicitly selectable. Forks name competing heads and choose no pair. A known-empty after side preserves a removal with its before revision. Heads come from successor edges rather than sorted identity strings, and the review pane renders the selected pair's own statements.

Fixture construction uses test-only RowStore and revision containers, not a validating production writer. Cycle and dangling-edge cases deliberately alter their scratch dataset to exercise reader refusal; the reason for that SQL is controlled corrupt read input, not proof that a shipped admission layer prevented the graph. Cyclic or missing predecessor evidence remains unresolved and names no guessed pair.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- `test_a_unique_chain_defaults_to_the_first_before_head_versus_the_last_after_head` supplies the current fixture or assertion described above. [16]
- `test_an_intermediate_revision_stays_selectable_history` supplies the current fixture or assertion described above. [17]
- `test_a_successor_cycle_is_unresolved_and_names_no_pair` supplies the current fixture or assertion described above. [18]
- `test_a_dangling_authored_edge_is_unresolved_and_names_the_missing_revision` supplies the current fixture or assertion described above. [19]
- `test_the_review_pane_renders_the_selected_head_pairs_own_statements` supplies the current fixture or assertion described above. [20]
- Fixture construction imports test-only row constructors; it does not call the retired canonical writer. [21]
- RowStore inserts index-shaped fixture rows without the retired production admission plane. [22]
