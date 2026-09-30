# mcp/tests/test_review_external_git_movement_read.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_review_external_git_movement_read.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:35:02+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076` |
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `mcp/tests/overview.md` |

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
manifests govern; `LIFECYCLE_CONTRACT_COUNT` and `LIFECYCLE_ARTIFACT_COUNT` are unchanged by the
registration, while `LIFECYCLE_CATALOG_SHA256` is re-pinned deliberately because the catalog bytes moved.

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

## Docs References

No configured domain documentation could be checked for this module. The resolved memory layer's
`system/sources.md` carries no `Domain Documentation` category, so no documentation row is recorded
here. The one document these cases read is a repository file rather than an external source:
`docs/reference/worktrees-c09.md`, whose `## Raw Git Identity Boundary` section the matrix case asserts
against, and that assertion is filed under Repo-Internal References.

## Repo-Internal References

Every claim on this card is checkable in the module's own cases, in the fixtures it borrows from its
siblings, and in the manifests that govern its population. The three details a reader should carry:
**every case drives real Git and then reads a shipped entry point**; **the states that look similar each
have their own case**; and **the documented matrix is asserted to be the published one**, so the two
cannot drift apart silently.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of what it drives, what it reads, and why it is a separate module from the managed-sync cases.** | "It lives beside"; "rather than inside it" | mcp/tests/test_review_external_git_movement_read.py:15-19 |
| **The sibling fixture this module shares rather than rebuilds.** | `ReviewSyncFixture` | mcp/tests/test_review_sync_rebinding.py:102-378 |
| **The shipped review read these cases drive.** | `read_knowledge_review` | mcp/src/agents_remember/application/knowledge_review.py:227-254 |
| **The class whose docstring states the defect it protects: the packet's non-conforming example in its second form.** | `RawGitIdentityBoundaryTests` | mcp/tests/test_review_external_git_movement_read.py:56-656 |
| **The case that drives a real rebase and proves the review stops reading as current.** | `test_a_raw_rebase_is_measured_and_the_review_stops_reading_as_current` | mcp/tests/test_review_external_git_movement_read.py:65-145 |
| **The control that keeps R22's managed-sync fact and this leaf's raw-Git fact apart.** | `test_a_managed_sync_alone_is_not_reported_as_a_raw_transition` | mcp/tests/test_review_external_git_movement_read.py:147-205 |
| The case where the worktree left its declared branch and the comparison cannot be taken at all. | `test_a_worktree_that_left_its_declared_branch_reports_the_switch` | mcp/tests/test_review_external_git_movement_read.py:207-255 |
| The cherry-pick, revert and ordinary-commit case, each in its own fixture. | `test_each_forward_moving_transition_is_exercised_and_reported_as_what_it_is` | mcp/tests/test_review_external_git_movement_read.py:257-303 |
| The case where the declared source branch is rewritten while the leaf's own branch is untouched. | `test_a_rewritten_official_line_replaces_the_recorded_source_base` | mcp/tests/test_review_external_git_movement_read.py:305-353 |
| **The control state: the value an ordinary review of an untouched leaf publishes.** | `test_an_untouched_leaf_reports_no_transition_at_all` | mcp/tests/test_review_external_git_movement_read.py:355-401 |
| **The pair that keeps a missing recorded object apart from a branch switch.** | `test_a_missing_recorded_object_is_not_reported_as_a_branch_switch` | mcp/tests/test_review_external_git_movement_read.py:403-449 |
| **The pair that keeps an unusable generation apart from "never reviewed".** | `test_a_generation_that_cannot_be_read_is_unavailable_not_absent` | mcp/tests/test_review_external_git_movement_read.py:451-500 |
| **The case that asserts the documented matrix is the rendered production table, with unknown names refusing.** | `test_the_documented_matrix_and_the_published_matrix_are_one_table` | mcp/tests/test_review_external_git_movement_read.py:502-561 |
| **The five validator forgeries, one departing from each clause, against the real published value.** | `test_the_movement_validator_refuses_each_false_shape` | mcp/tests/test_review_external_git_movement_read.py:563-635 |
| **The case that pins the `unchanged` value as the published control.** | `test_the_unchanged_value_is_the_one_the_control_state_publishes` | mcp/tests/test_review_external_git_movement_read.py:637-656 |
| The helper that removes a recorded object so the missing-object state is reachable. | `_delete_loose_object` | mcp/tests/test_review_external_git_movement_read.py:659-672 |
| The helpers that perform the four transitions, each a Git operation rather than an assertion. | `_rebase_work_branch_onto_a_new_official_commit`; `_revert_the_leaves_own_commit` | mcp/tests/test_review_external_git_movement_read.py:675-692; mcp/tests/test_review_external_git_movement_read.py:706-712 |
| The small shared guards the transition helpers are built on. | `_on_branch`; `_git_ok` | mcp/tests/test_review_external_git_movement_read.py:722-730; mcp/tests/test_review_external_git_movement_read.py:733-741 |
| **The module-level case that pins the closeout, closeout-apply and integration results carrying the statement.** | `test_the_closeout_and_integration_results_carry_the_boundary_statement` | mcp/tests/test_review_external_git_movement_read.py:744-801 |
| **The module-level case that pins the absence a leaf which published nothing reports.** | `test_a_result_whose_leaf_published_nothing_states_the_absence` | mcp/tests/test_review_external_git_movement_read.py:804-830 |
| **The lane registration that makes these cases part of the governed `integration` population.** | "mcp/tests/test_review_external_git_movement_read.py" | mcp/tests/test-evidence-lanes.toml:362-362 |
| **A lifecycle consumer row that names this module, so the artifact census still counts it.** | "mcp/tests/test_review_external_git_movement_read.py" | mcp/tests/evidence-lifecycle.toml:765-770; mcp/tests/evidence-lifecycle.toml:1337-1337; mcp/tests/evidence-lifecycle.toml:1468-1468; mcp/tests/evidence-lifecycle.toml:771-771 |
| The re-pinned catalog digest that owns the lifecycle manifest's exact bytes. | `LIFECYCLE_CATALOG_SHA256` | mcp/tests/test_dependency_ownership_ast_helpers.py:46-46 |
| **The documented section the matrix case asserts against, generated from the production table.** | "Raw Git Identity Boundary" | docs/reference/worktrees-c09.md:113-148 |
| The sibling module that owns the managed-sync half of the same read, whose fixture this module shares. | `LiveReviewMovementTests` | mcp/tests/test_review_sync_movement_read.py:40-327 |

## Cross-Repo References

No cross-repository behavior is implemented or exercised in this module. Every repository it drives is a
temporary enclosure this same repository's own fixture created under a temporary directory, and every
operation it performs is a local Git subprocess inside that enclosure. No remote, credential, network or
external system is involved, and no cited range proves a repository or external-system boundary, so no
cross-repo reference row is recorded here.

## Update History
- 2026-09-30T22:35:02+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): No content impact: citation repair only; this document's own source is unchanged by MIK-L33. Rows citing MIK-L33's changed sources (`knowledge_review.py`, `test-evidence-lanes.toml`) moved with the leaf's inserted lines: 1 row(s) re-pointed by the installed fixer (its generated bullets kept); 1 passing row(s) normalised by the fixer. No claim wording changed, and no verification stamp was advanced.
- 2026-09-30T20:31:36+00:00: Generated citation repair: "mcp/tests/test_review_external_git_movement_read.py" repointed to mcp/tests/test-evidence-lanes.toml:362-362. No content impact: mechanical anchor-range projection bound to citation source snapshot 8b6fd4477f4e6588d3a971c6b77ff9a95df2a0849774b3a5c948b24cd8c436b5; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T05:58:11+02:00 — 260928-MIK-L05 curator (uncommitted change set on `ar/260928-mik-l05`, code base `31d761a241055d67b85ef3908033856b78a86a57` plus the staged and unstaged delta): No content impact: citation-only repair. This card's source is unchanged. Rows citing `mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test-evidence-lanes.toml` were re-pointed to the lines MIK-R05 moved, by the installed fixer or by the exact line shift where it declined (each such row byte-identical to memory HEAD, its anchors checked in the base and the shifted ranges); no claim was reworded.
- 2026-09-30T03:51:02+00:00: Generated citation repair: "mcp/tests/test_review_external_git_movement_read.py" repointed to mcp/tests/test-evidence-lanes.toml:356-356. No content impact: mechanical anchor-range projection bound to citation source snapshot 778874e9f7067e0c11ceadc4ef5d81e0b76e5e12eb31479c7b3ae9bc268513ab; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`evidence-lifecycle.toml`, `test-evidence-lanes.toml`, `test_dependency_ownership_ast_helpers.py`) were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact base-to-working line map; no claim wording changed. No verification stamp was advanced.
- 2026-09-29T12:08:03+00:00: Generated citation repair: "mcp/tests/test_review_external_git_movement_read.py" repointed to mcp/tests/test-evidence-lanes.toml:342-342. No content impact: mechanical anchor-range projection bound to citation source snapshot 75677f16e5ed8ed01a37a3496ecf058f05e2f85f804720849cd36afc05309a98; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-28T23:41:23+02:00 — 260921-ICR-L57 curator (uncommitted candidate tree `a0358351a0f6b5157f7abc2255a0a6e46066ae6b` over code base `69883386d36d7cdb7faeed5bdf275ddd66d87aea`): No content impact: re-pointed 5 citations into `mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test-evidence-lanes.toml` through the exact base-to-candidate line map after this leaf's behaviour-preserving splits and catalog/lane/pin repairs; each moved range cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T23:11:42+02:00 — 260921-ICR-L56 curator (candidate tree `0dabc51f68b613546ec971657726b97828afb69a` over code base `ae2fd5c864aa2609ae45b5c7dbbaa693569aefc6`): No content impact: re-pointed 1 citation into `test-evidence-lanes.toml` after this leaf inserted the `mcp/tests/test_read_anchor_memo.py` row at `:173`; each moved row cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T20:07:41+02:00 — 260921-ICR-L55 curator: No content impact: re-pointed 1 citation into `test-evidence-lanes.toml` after this leaf inserted the `mcp/tests/test_notes_listing.py` row at `:162` (candidate tree `c77a4346480db6674dd760f974e8b24079d8f755` over code base `e66f1f3894116e0bb37b49f178d8bfcb130a7e28`). Each moved row cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T17:08:17+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test-evidence-lanes.toml`) were re-pointed through the exact base-to-candidate line map; each moved row cites the same line content it cited at base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T16:25:39+02:00 — 260921-ICR-L42 curator: No content impact: re-pointed this card's citations into `test-evidence-lanes.toml` after this leaf's line insertions (candidate tree `27409ea9f3320689c28c6a810c9a88afa288bbba` over code base `55c62237132eaa56b0df28ae5a8420a8dc05303d`). Each moved row cites the same line content it cited at base. Wording is unchanged, and no stamp was advanced.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "mcp/tests/test_review_external_git_movement_read.py" repointed to mcp/tests/test-evidence-lanes.toml:309-309. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **citation pass — the rows this leaf's own line movement displaced were re-anchored from each row's own finding message.** Every flagged range was repointed or widened to the lines that actually carry the anchor at this candidate, using the memory-quality checklist's own per-row message as the ground truth rather than adding a delta to an old number; the repair was applied row-scoped by the cited-range string, so duplicate rows were each corrected. No claim was re-worded to fit a stale pointer, no anchor or range was dropped to silence a finding, and the two legacy mechanical-projection bullets on rows this pass re-read were retired with this entry as their dated disposition, and no new projection bullet was written. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base `63b476297708f779de8ed5c0bf3555b9d1de70c2`): **citation re-anchoring and history only; no claim wording changed and no row deleted.** This leaf's change set moved the lines several of this card's rows cite — `mcp/src/agents_remember/application/knowledge_curator_ingest.py` grew 3587 → 3861 while `mcp/tests/test-evidence-lanes.toml` gained one `unit-regression` row and `mcp/tests/evidence-lifecycle.toml` gained two consumer rows, each shifting every row below it — so every affected range was re-derived against the candidate's own bytes rather than shifted by a remembered delta and re-anchored to the construct it names. Nothing in the body above was deleted to clear a finding, and no verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-23T19:50:00+02:00 — 260921-ICR-L23 curator (uncommitted change set on `ar/260921-icr-l23`, base `473ad8242bb4c22bdabed5d5253767350381eb3e`): created this one-to-one card for the module this leaf's fix round extracted as **the raw-Git half of the review-boundary cases**, split out of `test_review_sync_movement_read.py` along the seam the production owners already have — the managed measurement beside the raw one — because the two together pass the file-size rail. It records what a reader has to act on: every case performs real Git in a real enclosure and then reads a shipped entry point (the ordinary review read, the closeout preview and apply tools, the integration tool), so no prebuilt payload or injected resolution stands in for the operation; the states that look similar each have their own case, with a missing recorded object kept apart from a branch switch and an unreadable generation kept apart from "never reviewed"; the documented matrix is asserted to be the rendered production table rather than a transcription beside it; and the validator's clauses are pinned one forgery each against the real published value. The enumeration fixture and the closeout enclosure are the siblings' own (`test_review_sync_rebinding`, `test_review_final_output_receipt`), shared rather than rebuilt. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` name this leaf's recorded base `473ad8242bb4c22bdabed5d5253767350381eb3e` because every construct cited here exists only in this leaf's uncommitted working tree — the file itself is untracked at that commit — so no commit contains the content a stamp would claim to have verified; what was actually read is that working tree (base commit plus the leaf's working-tree delta), and the governing overview is `mcp/tests/overview.md`.
