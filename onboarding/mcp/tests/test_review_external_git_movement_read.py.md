# mcp/tests/test_review_external_git_movement_read.py

## Governing Overview

[mcp tests route overview](overview.md)

## Purpose

**The cases that drive real Git in real enclosures and then read the shipped surfaces for the raw-Git
identity boundary (ICR-R23@v1).** `worktree_sync` is the one route that moves a leaf's declared
identities under measurement; everything else that can move them — `git rebase`, `git cherry-pick`,
`git revert`, a checkout that leaves its declared branch — is ordinary Git and leaves no record behind,
so a reader holding only "a comparison generation was frozen" cannot tell a rewritten branch from an
untouched one.

The module's own docstring states what it reads: the ordinary review read
(`application.knowledge_review.read_knowledge_review`), the closeout preview and apply tools, and the
integration tool. It pins the support matrix the code publishes against the matrix the repository
documents, and it pins the states that must never be flattened into one another — an untouched leaf, an
advanced branch, a rewritten one, a checkout that left its branch, a recorded object that is gone, and a
generation that cannot be read.

**It is a separate module by the seam the production owners already have.** It lives beside
`test_review_sync_movement_read.py` rather than inside it (`:15-19`): that module owns what the *managed*
sync's rebinding renders on the same read, and the two together pass the file-size rail, so the seam is
the managed measurement beside the raw one. The enclosure fixture and the closeout enclosure are the
siblings' own, shared rather than rebuilt, for the same reason.

## Code Commentary

### Logic

**Every case drives the operation rather than a private helper.** The class
`RawGitIdentityBoundaryTests` (`:53-61`) states the defect it protects — the packet's non-conforming
example in its second form, a review whose declared identities a raw operation replaced keeping on
reading as current because no managed sync ran and therefore no rebinding record exists — and each case
performs real Git in the enclosure's own work branch before reading through the shipped entry point.

| Case | Line | The operation it drives |
| --- | --- | --- |
| `test_a_raw_rebase_is_measured_and_the_review_stops_reading_as_current` | `:62` | real `git rebase`, then the shipped read — the one transition an ancestry check can prove |
| `test_a_managed_sync_alone_is_not_reported_as_a_raw_transition` | `:144` | the production sync tool; the control keeping R22's fact and this leaf's fact apart |
| `test_a_worktree_that_left_its_declared_branch_reports_the_switch` | `:204` | a checkout leaving the declared branch, so the comparison cannot be taken at all |
| `test_each_forward_moving_transition_is_exercised_and_reported_as_what_it_is` | `:254` | real `git cherry-pick`, real `git revert`, plus an ordinary commit, each in its own fixture |
| `test_a_rewritten_official_line_replaces_the_recorded_source_base` | `:302` | the declared source branch rewritten while the leaf's own branch is untouched |
| `test_an_untouched_leaf_reports_no_transition_at_all` | `:352` | the control state: the value every ordinary review of an untouched leaf publishes |
| `test_a_missing_recorded_object_is_not_reported_as_a_branch_switch` | `:400` | a recorded object that is gone, which must not be read as a switch |
| `test_a_generation_that_cannot_be_read_is_unavailable_not_absent` | `:448` | an unusable generation, kept apart from "never reviewed" |
| `test_the_documented_matrix_and_the_published_matrix_are_one_table` | `:499` | the rendered production table against the documented section, with unknown names refusing |
| `test_the_movement_validator_refuses_each_false_shape` | `:560` | five forgeries, each departing from exactly one validator clause, against the real published value |
| `test_the_unchanged_value_is_the_one_the_control_state_publishes` | `:634` | the `unchanged` value pinned as the published control |

**Two module-level cases cover the closeout and integration owners.**
`test_the_closeout_and_integration_results_carry_the_boundary_statement` (`:741`) and
`test_a_result_whose_leaf_published_nothing_states_the_absence` (`:801`) are outside the class because
they read tools rather than the review surface, and they pin the half of the boundary that never
refuses.

**The helpers are Git operations, not assertions.** `_delete_loose_object` (`:656`) removes a recorded
object so the missing-object state is reachable; `_rebase_work_branch_onto_a_new_official_commit`
(`:672`), `_cherry_pick_an_official_commit_into_the_work_branch` (`:692`),
`_revert_the_leaves_own_commit` (`:703`) and `_commit_another_leaf_change` (`:712`) perform the four
transitions; `_on_branch` (`:719`) and `_git_ok` (`:730`) are the small guards the others share.

### Conventions

The module imports the shipped entry points it reads (`:30-42`) — `worktree_tools`,
`read_knowledge_review`, the generation owner's manifest reader, the matrix, its renderer, the named
lookup and the unsupported list, and the published value — and it imports its fixtures from the
siblings rather than rebuilding them (`:44-50`): `_closeout`, `_freeze_review`, `_publish_dataset` and
`_review_closeout_fixture` from `test_review_final_output_receipt`, and `NEWLINE`, `ReviewSyncFixture`,
`commit_file` and `git` from `test_review_sync_rebinding`. `pytest` and `unittest` are both used, and
`ValidationError` is imported for the validator forgeries.

The module is registered as a member of the `integration` lane in `mcp/tests/test-evidence-lanes.toml`
and as a consumer in `mcp/tests/evidence-lifecycle.toml`, so its cases are part of the population those
manifests govern.

### Invariants And Boundaries

- **No prebuilt payload and no injected resolution.** Every case reaches the boundary through a real Git
  operation in a real enclosure and then reads the shipped entry point; a case that asserted a
  hand-built payload would prove nothing about the operation.
- **States that look similar must not be flattened.** A missing recorded object is not a branch switch,
  an unreadable generation is not "no generation", and an advanced branch is not a replaced one: each
  has a named case, and `test_a_missing_recorded_object_is_not_reported_as_a_branch_switch` and
  `test_a_generation_that_cannot_be_read_is_unavailable_not_absent` are the pairs that keep them apart.
- **The documented matrix and the published matrix are one table.** `render_git_transition_support()`'s
  output must be a substring of `docs/reference/worktrees-c09.md`, so the document is generated from the
  production table rather than transcribed beside it.
- **The validator's clauses are pinned one forgery each, with the real value as the accepted control**,
  so a clause that stopped refusing would be noticed rather than inferred.
- **Boundary: the module owns the seams it does not cross.** The managed-sync rebinding's own rendering
  stays in `test_review_sync_movement_read.py`; this module takes the raw-Git half only, and shares the
  fixture rather than duplicating it.

### Todos

None recorded.

## Evidence

### Docs References

No configured domain documentation could be checked for this module. The resolved memory layer's
`system/sources.md` carries no `Domain Documentation` category, so no documentation row is recorded
here. The one document these cases read is a repository file rather than an external source:
`docs/reference/worktrees-c09.md`, whose `## Raw Git Identity Boundary` section the matrix case asserts
against, and that assertion is filed under Repo-Internal References.

### Repo-Internal References

Every claim on this card is checkable in the module's own cases, in the fixtures it borrows from its
siblings, and in the manifests that govern its population. The three details a reader should carry:
**every case drives real Git and then reads a shipped entry point**; **the states that look similar each
have their own case**; and **the documented matrix is asserted to be the published one**, so the two
cannot drift apart silently.

- **The module's own statement of what it drives, what it reads, and why it is a separate module from the managed-sync cases.** [1]
- **The sibling fixture this module shares rather than rebuilds.** [2]
- **The shipped review read these cases drive.** [3]
- **The class whose docstring states the defect it protects: the packet's non-conforming example in its second form.** [4]
- **The case that drives a real rebase and proves the review stops reading as current.** [5]
- **The control that keeps R22's managed-sync fact and this leaf's raw-Git fact apart.** [6]
- The case where the worktree left its declared branch and the comparison cannot be taken at all. [7]
- The cherry-pick, revert and ordinary-commit case, each in its own fixture. [8]
- The case where the declared source branch is rewritten while the leaf's own branch is untouched. [9]
- **The control state: the value an ordinary review of an untouched leaf publishes.** [10]
- **The pair that keeps a missing recorded object apart from a branch switch.** [11]
- **The pair that keeps an unusable generation apart from "never reviewed".** [12]
- **The case that asserts the documented matrix is the rendered production table, with unknown names refusing.** [13]
- **The five validator forgeries, one departing from each clause, against the real published value.** [14]
- **The case that pins the `unchanged` value as the published control.** [15]
- The helper that removes a recorded object so the missing-object state is reachable. [16]
- The helpers that perform the four transitions, each a Git operation rather than an assertion. [17]
- The small shared guards the transition helpers are built on. [18]
- **The module-level case that pins the closeout, closeout-apply and integration results carrying the statement.** [19]
- **The module-level case that pins the absence a leaf which published nothing reports.** [20]
- **The lane registration that makes these cases part of the governed `integration` population.** [21]
- **A lifecycle consumer row that names this module, so the artifact census still counts it.** [22]
- **The documented section the matrix case asserts against, generated from the production table.** [24]
- The sibling module that owns the managed-sync half of the same read, whose fixture this module shares. [25]

### Cross-Repo References

No cross-repository behavior is implemented or exercised in this module. Every repository it drives is a
temporary enclosure this same repository's own fixture created under a temporary directory, and every
operation it performs is a local Git subprocess inside that enclosure. No remote, credential, network or
external system is involved, and no cited range proves a repository or external-system boundary, so no
cross-repo reference row is recorded here.
