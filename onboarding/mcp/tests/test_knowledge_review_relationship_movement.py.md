# mcp/tests/test_knowledge_review_relationship_movement.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The movement and relationship evolution case module (`ICR-R08@v1`): **the recorded before/after
relationship union, exercised through actual store operations**. Every population and every movement is
produced by the store's own operations over the shared two-snapshot fixture — a realization the author
moved from one path onto a successor revision's path, a realization withdrawn with its invariant still
recorded, an authored split and an authored merge, a family membership whose family and member
revisions moved, and a governing route each snapshot records separately — and then read back through
the production composition (`read_knowledge_review`) on a real leaf enclosure with a real Git worktree.
Nothing here hand-writes a payload the composition is then claimed to render.

The module docstring states the load-bearing properties, one case each, and they are exactly the
packet's Required Behavior, Failure And Recovery Behavior and boundary examples.

## Code Commentary

### Logic

**The fixture is the shared diff fixture plus the source-endpoint enclosure, extended through the
store's own operations.** `build_movement_fixture` builds the two datasets through
`build_endpoint_fixture` (the shipped fixture builder the source-endpoint module owns) and then authors
the populations this leaf needs with the public store operations: `author_claim` inserts a realization
claim and its anchor, `remove_claim` removes one through the store's own removal operation,
`author_revision` creates a successor revision, `_reassign_family` moves a membership onto a new family
revision, and `_author_route`/`_govern` record a governing route at each snapshot's own scope. The
candidate's moved content is deliberately a near-copy of the baseline file the withdrawn claim recorded,
because that is what makes the source movement a *rename* to Git's own similarity detection — and
therefore what makes the packet's rename clause measurable rather than asserted.

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
- `test_a_governing_route_reassignment_displays_both_recorded_routes` — both recorded routes.
- `test_an_identity_with_no_route_is_displayed_as_ungoverned_and_never_as_the_root` — the ungoverned
  state with `route_id=None` and its own sentence.
- `test_a_side_that_did_not_resolve_exactly_keeps_its_own_state_and_reason` — `anchor_unresolved` with
  the read's own resolution detail (`path_absent`, `recorded_blob_mismatch` in this fixture).

**The read-back helpers make the assertions about the production payload rather than about internals.**
`review`/`review_of` call the composition, `realization_movements` selects the realization movements
from the payload's `source.relationships`, and `movement_between` finds the movement displaying a given
recorded address pair — so a case states the user-visible fact it protects.

### Conventions

One behavior boundary per module per the test-split rule: this module owns the packet's own cases; the
reach cases the master's ruling added live in `test_knowledge_review_relationship_reach.py` and the
authored-line cases in `test_knowledge_review_relationship_line.py`, and both import this module's
builders rather than duplicating them. Imports go through the composition
(`read_knowledge_review`) and the public store operations; the support imports
(`diff_scope_test_support`, `read_scope_test_support`) are the two exact-scope consumers
`mcp/tests/evidence-lifecycle.toml` registers, and the module has its own lane row in
`mcp/tests/test-evidence-lanes.toml`. `pytestmark = pytest.mark.evidence_unit` puts it in the ordinary
unit lane.

### Invariants And Boundaries

- **No case trusts a constructed payload.** Every population is authored through the shipped store
  operations and read back through the production composition over a real worktree.
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

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

Every claim on this card is checkable in the uncommitted candidate: the module's own docstring, the
fixture builders, the read-back helpers and the eleven cases.

- The module's own statement of what it measures and of the near-copy content constant that makes the source movement a rename to Git's own detection. [1]
- The two-snapshot fixture and the movement populations authored through the public store operations. [2]
- The route authoring at each snapshot's own scope, and the merge predecessors read from the candidate's rows. [3]
- The read-back helpers: the composition call and the movement selection from the payload's relationship collection. [4]
- **The packet's conforming example and the non-conforming reading measured beside it.** [5]
- **The withdrawal boundary and the selection boundary: a deleted file keeps its identity and reason, and present-outside-selection is never a deletion.** [6]
- **The labelled rename inference, and the same rename with no authored edge producing a retraction and an addition.** [7]
- The authored split and merge read from the candidate's own predecessor rows. [8]
- The family reassignment, the route reassignment and the ungoverned identity. [9]
- **The unresolved anchor keeps its own state and reason.** [10]
- The two exact-scope support modules this case module consumes, registered on both consumer rows of the lifecycle catalog. [11]

### Cross-Repo References

No cross-repository behavior is exercised in this file.

No applicable cross-repository source was found.
