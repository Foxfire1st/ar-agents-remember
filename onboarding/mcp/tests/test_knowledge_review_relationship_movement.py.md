# mcp/tests/test_knowledge_review_relationship_movement.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The reviewer's relationship union and display: retractions, additions and recorded sides — never a succession the author did not record.

## Code Commentary

The fixture keeps reader cases a text tree cannot author, calling the actual composition with
explicit test-only row inputs; public resolution is covered by the converted-tree suite. A removed
claim and a new claim display as a retraction and an addition; an intentionally after-only extraction omits the old association, whereas the actual payload union retains it as a retraction; a withdrawn realization stays visible with its deleted file and its
identity; a source rename is never a recorded movement and carries no inference; an authored merge
revision displays as an addition citing its own revision; a family association reassigned to a new
revision displays both recorded sides. A converted-text fixture reads a family's declared routes —
one relationship per declared route — while an unread side is never called ungoverned. Bounded
selection omissions are not deletions. These assertions record test intent, not an execution result.

## Evidence

### Repo-Internal References


- Historical target names the former moved-realization test. Current test_a_removed_claim_and_a_new_claim_display_as_a_retraction_and_an_addition asserts separate unpaired retraction/addition under the retained invariant identity, not one movement carrying both addresses. [12]


- `test_the_same_rename_with_no_authored_edge_is_a_retraction_and_an_addition` owns the current boundary described above. [13]
- `test_a_familys_declared_route_set_is_the_governing_association_read_from_text` owns the current boundary described above. [14]
- `test_each_declared_route_is_one_relationship_and_an_unread_side_is_never_ungoverned` owns the current boundary described above. [15]
