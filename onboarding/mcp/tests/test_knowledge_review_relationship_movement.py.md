# mcp/tests/test_knowledge_review_relationship_movement.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

Checks authored relationship movement and family-declared route sets across exact comparison sides.

## Code Commentary

Synthetic index rows exercise lineage, retractions/additions and authored split/merge edges; a Git rename is labeled inference and does not manufacture an authored edge. A converted-text fixture reads a family's declared routes, one relationship per declared route, while an unread side is never called ungoverned. Removed scalar canonical governing-route writers and helpers are not current fixture owners. Bounded selection omissions are not deletions. These assertions record test intent, not an execution result.

## Evidence

### Repo-Internal References

- `test_a_moved_realization_displays_both_recorded_paths_under_one_invariant_identity` owns the current boundary described above. [12]
- `test_the_same_rename_with_no_authored_edge_is_a_retraction_and_an_addition` owns the current boundary described above. [13]
- `test_a_familys_declared_route_set_is_the_governing_association_read_from_text` owns the current boundary described above. [14]
- `test_each_declared_route_is_one_relationship_and_an_unread_side_is_never_ungoverned` owns the current boundary described above. [15]
