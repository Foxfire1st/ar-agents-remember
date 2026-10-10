# mcp/tests/test_knowledge_review_relationship_movement.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose
Checks authored relationship movement and family-declared route sets across exact comparison sides.

## Code Commentary
Synthetic index rows exercise lineage, retractions/additions and authored split/merge edges; a Git rename is labeled inference and does not manufacture an authored edge. A converted-text fixture reads a family's declared routes, one relationship per declared route, while an unread side is never called ungoverned. Removed scalar canonical governing-route writers and helpers are not current fixture owners. Bounded selection omissions are not deletions. These assertions record test intent, not an execution result.

### Logic
**Eleven cases, one distinct user operation each:**

- `test_a_moved_realization_displays_both_recorded_paths_under_one_invariant_identity` — the packet's
  conforming example: one movement, both recorded addresses, one preserved invariant identity, and both
  locations carrying it.
- `test_only_the_after_graph_is_read_so_the_old_association_vanishes` — the packet's non-conforming
  reading measured as a population the after side cannot produce, beside the union that does.
- `test_a_withdrawn_realization_stays_visible_with_its_deleted_file_and_its_identity` — a retraction
  keeps its side, its resolution, its reason and the still-recorded invariant.
- `test_a_record_the_other_selection_did_not_reach_is_not_displayed_as_a_deletion` — present outside
  the selection is its own transition, never `retracted`.
- `test_a_source_rename_is_displayed_as_a_labelled_git_inference` — the inference with its command,
  its similarity word and its "not proof that the invariant moved" sentence.
- `build_no_authored_edge_fixture` + `test_the_same_rename_with_no_authored_edge_is_a_retraction_and_an_addition`
  — the inference never fabricates a movement.
- `test_the_authored_split_and_merge_are_displayed_from_the_candidates_own_edges` — the split names
  every successor, the merge every predecessor, read from the snapshots' predecessor rows.
- `test_a_family_association_reassigned_to_a_new_revision_displays_both_recorded_sides` — a family
  reassignment with the family identity preserved and the member revision moved.
- `test_a_side_that_did_not_resolve_exactly_keeps_its_own_state_and_reason` — `anchor_unresolved` with
  the read's own resolution detail (`path_absent`, `recorded_blob_mismatch` in this fixture).

**The read-back helpers make the assertions about the production payload rather than about internals.**
`review`/`review_of` call the composition, `realization_movements` selects the realization movements
from the payload's `source.relationships`, and `movement_between` finds the movement displaying a given
recorded address pair — so a case states the user-visible fact it protects.

### Invariants And Boundaries
- **The packet's own examples are measured, not asserted** — conforming (one movement, two addresses,
  one identity), non-conforming (the after-only population cannot name the old association) and the
  deletion boundary (a withdrawn realization keeps its file, side and reason).
- **The rename clause is measured on both sides**: a real near-copy rename is displayed as a labelled
  inference, and the same rename with no authored edge is a retraction and an addition.
- **Boundaries.** The reach cases are the sibling modules'; mounting the payload in the browser pane is
  `ICR-R24`'s; the acceptance journey is `ICR-R25`'s.

### Todos
None recorded.

## Evidence

### Repo-Internal References

Every claim on this card is checkable in the uncommitted candidate: the module's own docstring, the
fixture builders, the read-back helpers and the eleven cases.

- `test_a_moved_realization_displays_both_recorded_paths_under_one_invariant_identity` owns the current boundary described above. [12]
- `test_the_same_rename_with_no_authored_edge_is_a_retraction_and_an_addition` owns the current boundary described above. [13]
- `test_a_familys_declared_route_set_is_the_governing_association_read_from_text` owns the current boundary described above. [14]
- `test_each_declared_route_is_one_relationship_and_an_unread_side_is_never_ungoverned` owns the current boundary described above. [15]

- The module's own statement of what it measures and of the near-copy content constant that makes the source movement a rename to Git's own detection. [16]
- The read-back helpers: the composition call and the movement selection from the payload's relationship collection. [17]
- **The packet's conforming example and the non-conforming reading measured beside it.** [18]
- **The withdrawal boundary and the selection boundary: a deleted file keeps its identity and reason, and present-outside-selection is never a deletion.** [19]
- **The labelled rename inference, and the same rename with no authored edge producing a retraction and an addition.** [20]
- The authored split and merge read from the candidate's own predecessor rows. [21]
- **The unresolved anchor keeps its own state and reason.** [22]
- The two exact-scope support modules this case module consumes, registered on both consumer rows of the lifecycle catalog. [23]

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is configured for this file.

No relevant domain documentation was found.

### Cross-Repo References

No cross-repository behavior is exercised in this file.

No applicable cross-repository source was found.
