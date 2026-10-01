# mcp/tests/test_knowledge_review_attributed_source_content.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

Production-composition evidence for the **attributed unchanged** admission of the review's
source-content route (ICR-R03@v1 under the 2026-09-28 admission ruling): an unchanged file that a
realization recorded in the *same comparison's* knowledge links opens at that comparison's exact
endpoints, and every other unchanged path is still refused. The general confinement case for
arbitrary unchanged paths stays in the sibling `test_knowledge_review_source_content.py` and is kept.

Cases run through the real leaf enclosure and worktree, the real review route's inventory, the real
capture, the real comparison freeze and the real expansion route wired to the real application owner.
Bytes are compared against subprocess Git, never against the owner under test.

## Code Commentary

### Logic

**Fixture and helpers.** `attributed_fixture` builds a fresh live enclosure **with** both knowledge
halves (`build_endpoint_fixture` from the R01 source-endpoint suite); the sibling content suite builds
its own with `datasets=False`. Three paths from `read_scope_test_support` name the populations:
`ATTRIBUTED_PATH` (linked on both snapshots), `BEFORE_ONLY_PATH` (linked only by the before snapshot)
and `UNRELATED_PATH` (linked by neither). `_freeze` publishes the current comparison as a generation;
`_attributed` validates a served body with `ReviewSourceExpansion.model_validate` and asserts
`attributed_unchanged` / `unchanged` / `requested_generation`; `_refused` asserts a 400
`source_content_unresolved` naming the path. The listing, expansion and Git-observation helpers are
imported from the sibling content suite.

**The ten cases:**

| Case | Property |
| --- | --- |
| `test_an_unchanged_path_a_recorded_realization_links_opens_as_context_without_counting` | both-snapshot and before-only links admit; each side is the pair's own blob; re-listing gives the same entries and `listed_total` |
| `test_an_unchanged_path_no_recorded_realization_links_is_still_refused` | an unlinked unchanged path refuses, naming both snapshots' answers |
| `test_a_path_linked_only_in_another_comparison_is_refused_for_this_one` | an earlier generation's link does not admit the path into the current pair; the earlier pair still opens it from its own record |
| `test_after_the_live_tree_moves_the_listed_pair_keeps_its_exact_attributed_bytes` | the frozen pair serves its historical bytes; an unrecorded superseded pair refuses rather than using current knowledge; the rewritten path becomes an ordinary change |
| `test_a_closed_leaf_opens_its_attributed_path_from_the_retained_generation` | with the worktree group removed, the retained generation admits exactly the same paths |
| `test_a_padded_spelling_is_never_admitted_as_attributed_context` | four whitespace paddings of a linked, an unlinked and a changed path all refuse (L43-R1-F1) |
| `test_a_selection_bound_below_the_scope_cannot_refuse_a_linked_path` | with `SELECTION_ITEM_LIMIT=1` the scope read refuses, yet the linked path still opens (L43-R1-F2) |
| `test_an_unreadable_snapshot_leaves_the_link_undetermined_rather_than_absent` | a corrupt after half: a before-linked path still opens, and its admission detail starts "a realization or proof recorded for the path" (ruling Q1's wording, MIK-L31); an unlinked path refuses as undetermined, never with the established-negative sentence, and the damaged half's remedy is still "restore or repair" (L43-R1-F2) |
| `test_never_initialized_knowledge_asks_to_initialize_it` | with no knowledge halves at all (`datasets=False`), the link stays undetermined and the next action starts "initialize this leaf's knowledge", never "restore or repair" (MIK-R31 rule 6, ICR-L43 review R2 O1) |
| `test_a_tree_index_links_a_path_its_proof_entry_is_anchored_at` | an in-memory `ix_entry` with one proof links exactly its path; an index without `ix_entry` (a dataset) links none (MIK-R31 rule 5, ruling Q1) |

### Conventions

`pytestmark = pytest.mark.evidence_unit`. The module is registered in the `unit-regression` lane of
`mcp/tests/test-evidence-lanes.toml` and as a consumer of the `read_scope_test_support.py` artifact in
`mcp/tests/evidence-lifecycle.toml`; an unregistered test module fails the lane-manifest check. Each case
builds its own enclosure under `tmp_path`, and damage (copied halves, a corrupt half, a removed worktree
group) is applied to real artifacts.

### Invariants And Boundaries

- **Production composition only.** No prebuilt expansion or hand-assembled resolution is injected.
- **The inventory is never widened.** The first case asserts re-listing equality after attributed reads.
- **Comparison isolation.** The cross-comparison and moved-tree cases are the falsifiers for current
  knowledge standing in for a superseded comparison's knowledge; the worker's mutation runs broke them.
- **Undetermined is asserted as not absent** by string: `_NOT_LINKED` must not appear in the
  undetermined refusal.
- **Never initialized is asserted as not damaged**: its next action never says "restore or repair".
- The route-level proof admission (review F12) lives in `test_review_git_trees.py`; the unit case here covers the
  dataset side (no `ix_entry`).

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries).

No configured domain documentation could be checked.

### Repo-Internal References

- **The module's own statement of the admitted population and one case per property.** [1]
- The lane marker, the three population paths and the two refusal constants. [2]
- Fixture and helpers: fresh enclosure with knowledge halves, freeze, refusal and attributed assertions. [3]
- **Attributed admission without counting, and the unlinked refusal.** [4]
- **Comparison isolation and historical bytes.** [5]
- **The two review-fix cases: exact spelling, and a link scope size cannot fail or an unread half cannot negate.** [6]
- **The MIK-L31 cases: the never-initialized remedy, and a proof entry's path linked in a tree index but not in a dataset.** [7]
- The population paths the fixture's knowledge links. [8]
- The lane row and the read-scope consumer row this module adds. [9]
- The owners under test. [10]

### Cross-Repo References

No cross-repository behavior is measured in this file.

No meaningful cross-repo references found.
