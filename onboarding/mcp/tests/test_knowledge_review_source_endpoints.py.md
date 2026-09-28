# mcp/tests/test_knowledge_review_source_endpoints.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_review_source_endpoints.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-26T01:00+02:00 |
| lastVerifiedCommitHash | `eda947325ccbe0791973953265278597e968a34a` |
| lastVerifiedCommitDate | 2026-09-28T18:11:05+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The **production-composition evidence for `ICR-R01@v1`**: the exact source endpoints a live curator
review binds, measured through the operations the dashboard really calls. Every case builds a real
enclosure contract on disk, a real linked Git worktree with staged, unstaged and eligible untracked
content, the real `read_knowledge_review`/`resolve_review_candidate` resolution, the real capture owner
and the real comparison. Nothing here injects a preconstructed resolution, a fake index or a
hand-built payload — which is what the packet's own evidence class requires, since "tests that merely
mirror implementation or assert returned prebuilt payloads are insufficient for production-composition
claims".

The load-bearing properties, one case each:

- the resolution binds the contract's **recorded base commit** on one side and the **captured add-all
  candidate tree** on the other, and leaves the real Git index byte-identical;
- the rendered review publishes those two ids and reaches the *whole* candidate — a `HEAD`-to-unstaged
  range would silently miss an eligible untracked file, which is the packet's non-conforming example;
- a capture input that moves before publication is refused **by name** (the exact side, plus the two
  identities it compared) instead of being published as the candidate's comparison;
- the capture owner's own mid-capture head check arrives as that same named refusal;
- a committed change-set range binds the two **recorded** commits, and a later commit on the branch
  does not move it; and
- a committed range nothing has recorded yet is refused by name while the working view stays available
  and labelled — so "what is not committed yet" is never published as what landed, and an unrecorded
  **memory** half empties only itself while the code half is still published.

The module registers **no artifact and no contract of its own**: it builds on the existing
`diff_scope_test_support` and `read_scope_test_support` fixtures rather than introducing a third one,
so its catalog footprint is two consumer rows on artifacts those modules already own.

## Code Commentary

### Logic

**`EndpointFixture` is one live leaf enclosure, and the fixture builder composes it from shipping
owners only.** `build_endpoint_fixture` runs `build_diff_fixture` (the shipped diff-scope fixture, which
creates the two datasets and a real committed Git tree), writes a real leaf enclosure contract through
`_enclosure`, materializes the candidate's tracked content in a real linked worktree
(`_materialize_candidate`), places the two dataset halves under the leaf's disposable review root
(`_place_datasets`), and returns an `EndpointFixture` whose `McpRuntimeConfig` points at the temporary
coordination root. `resolve()` is the real `resolve_review_candidate` call, asserted to have returned a
resolution rather than a refusal, so every case that needs the bound pair reads it from the operation
under test.

**The two index states are the fixture's own vocabulary.** `MODIFIED_PATH` and the tracked paths
reproduce the diff fixture's own candidate bytes so the recorded anchors observe exactly the blobs
they recorded — that is what makes "the source opens" a measurement rather than a claim.
`ELIGIBLE_UNTRACKED_PATH` and `STAGED_ADDITION_PATH` are the two ways a file can be in the candidate
and in no commit; `IGNORED_PATH` is the packet's boundary example, excluded by the repository's own
ignore rule. `LOCAL_COMMIT_PATH` and `UNCOMMITTED_PATH` exist for the committed/working contrast: one
is committed *after* the recorded endpoint is bound, the other is never committed at all.

**`recorded_range` writes the landed commit the way closeout does, and
`record_code_with_unrecorded_memory` builds the one state the degradation is about.** The first
replaces `code_commit` on the contract and re-reads it through `load_contract`, so the view reads a
recorded cell and not a fixture object. The second records the code landed commit while running an
external memory leg whose landed commit nothing has written — a real memory repository, worktree and
ledger, with every landed-commit cell empty — which is the shape the committed view has to degrade one
half at a time for.

**The endpoint cases measure identity, not labels.**
`test_the_live_candidate_binds_the_recorded_base_and_the_captured_tree` digests the worktree's real
index before and after the capture, because "the user's work is unchanged" is a claim about bytes and
not about intent; then asserts `baseline_code_tree_id == contract.code_base_commit`,
`candidate_code_tree_id` equals a *fresh* capture's `codeCandidateTree`, that both roots travel with
their tree ids, and that the captured tree's paths include the staged addition, the eligible untracked
file and the modified file while the ignored path is absent.

**`test_the_rendered_review_publishes_the_endpoints_and_reaches_the_whole_candidate` is the case that
falsifies the packet's non-conforming example.** It reads the real `read_knowledge_review` result,
asserts the payload's comparison carries the recorded base as `before_code_tree_id` and the captured
tree as `after_code_tree_id`, and asserts the published changed paths contain the untracked addition —
which `git diff --name-only HEAD` is then *measured* not to contain, so the two ranges are demonstrably
different populations rather than merely differently labelled. It also asserts the published source
locations open as `exact_recorded_blob`, that the published expansion command names the captured tree,
and — after serving the surface through `register_review_routes` and a `TestClient` — that the JSON
body the browser receives carries the same two ids. "Displayed, not only returned" is the point of that
last block.

**The three refusal cases separate three genuinely different movements.**
`test_a_capture_input_that_moves_before_publication_is_refused_by_name` edits the worktree between the
resolution and `compose_review`, then asserts the result is `refused`, that
`offending_input == "the captured candidate tree"`, and that `expected`/`observed` each carry the exact
tree id they compared. `test_a_capture_that_detects_a_moved_head_refuses_instead_of_publishing_a_stale_tree`
monkeypatches the capture owner's own `worktree_candidate_tree` so the head really moves between the
isolated index's `write-tree` and the owner's re-read of `HEAD`, and requires the owner's failure to
arrive as the surface's refusal naming `candidate` and carrying
`future-code-candidate-head-moved` — an unhandled capture error escaping the route is one of the two
states this refusal exists to prevent. `test_a_moved_code_head_names_the_head_as_the_side_that_moved`
commits the captured content, so only `observedCodeHead` moves, and asserts the refusal names exactly
that side and nothing else.

**The committed-range cases bind the recorded endpoints and keep the two modes apart.**
`test_a_committed_range_binds_the_recorded_commit_and_a_later_commit_does_not_move_it` records a landed
commit, reads the committed view and one committed file diff (asserting the exact before/after text),
then writes and commits a further file and requires the committed view to be **byte-for-byte equal** to
the first read with the later path absent — while the working view, with one dirty file, returns exactly
that one path. `test_an_unrecorded_committed_endpoint_is_refused_rather_than_read_from_head` commits
without recording, requires `FileNotFoundError` whose message names the missing committed range and
`mode=working`, asserts the live head does **not** appear in that message, and then shows the working
view still works. `test_an_unrecorded_memory_half_empties_only_itself_and_keeps_the_code_half` records
only the code commit and asserts the code half is still published with matching counters while the
memory half is `[]` with zeroed counters.


**The production composition gained four cases and a second fixture shape, and they measure R02 through the real route.** `build_endpoint_fixture(directory, *, datasets=False)` builds a leaf with a recorded base, a live worktree and a captured candidate and **neither dataset half**, and `EndpointFixture.task_request` is the selector-less request that opens the task-context review. The four cases: **(a)** a task-context review with no knowledge at all returns `state=review`, `comparison is None`, `staleness.state="not_compared"`, `knowledge.selection_state="task_context"`, and a `source.inventory` whose listed paths equal an independent `git diff --name-only -z` of the same two objects — read back from the **real HTTP route with no selector parameters** (200); **(b)** the production inventory keeps an unusual filename (`src/tab<TAB>newline<LF>name.py`, written into the leaf's real worktree and carried by the shipped capture) as the address it is expanded by, with the whole list equal to the independent Git observation; **(c)** a binary addition and a mode-only change are both listed with `content="binary"`/`mode_change=True` and no partial limitation declared; and **(d)** a non-UTF-8 pathname (`src/caf\xe9-latin1.py`, created through `os.fsencode` because no `str` path can express it) leaves the review openable with a **measured and partial** inventory, the path carried as `b'src/caf\xe9-latin1.py'`, the renderable remainder listed in full, `limitation:source_inventory_partial` declared, and the real route answering 200 (it answered 500 before the fix).

**The fixture gained a third shape, and it is additive: a real external memory mode** (`ICR-R14@v1`).
`build_endpoint_fixture(directory, *, datasets=True, memory_mode="disabled")` — the new keyword is the
third parameter, and `"disabled"` is its default, so every case that existed before this leaf builds
exactly the enclosure it built before. `memory_mode="external"` additionally composes a **real memory
repository with a linked worktree** (`_memory_plan` plus `_link_memory_worktree`, the same plan the
shipped diff fixture resolves), because a review whose records go through the curator authority needs a
contract whose enclosure really has a memory half: the authority's own canonical path is resolved
against it, published there, and read back through the production port. This is a fixture capability
rather than a case: the four R02 cases above still run in the default mode, and the module's own case
count and assertions are unchanged. The consuming module is
`mcp/tests/test_knowledge_review_evidence_channels.py`, whose `RecordedFixture` builds on
`memory_mode="external"`.


### Conventions

The module is marked `pytest.mark.evidence_unit`. Private helpers are one-purpose and named for what
they measure: `_digest` (a file's sha256), `_commit` (a real commit returning its id), `_tree_paths`
(one tree's paths through `git ls-tree`), `_captured_tree`/`_captured_identity` (the bound pair read off
the resolution), `_changed_paths_of` (the payload's published changed paths) and `_index_path`. The
fixture is function-scoped — "one fresh live enclosure per case; no case observes another's worktree
state" — and the paths it writes are constants at module level, so a case's vocabulary and its
assertions cannot drift.

### Invariants And Boundaries

- **Production composition only.** Each case drives the real resolution, the real capture owner, the
  real comparison and the real route; no preconstructed resolution, fake index or prebuilt payload is
  injected, and the one monkeypatch replaces the capture owner's own tree writer so a real detection
  fires.
- **The real Git index is evidence.** The index digest is taken before and after the capture, because
  an add-all capture that refreshed or rewrote the real index would leave it different.
- **A file in no commit and no index entry is the falsifier.** The eligible untracked addition is why
  a `HEAD`-to-unstaged range cannot be relabelled into the full task diff; the ignored path is why
  exclusions stay exclusions.
- **A moved input is a named refusal, never a stale publication.** Two identities are carried so the
  reader can compare what changed, and the head that moved is named rather than rounded into
  "something moved".
- **The two change-set modes are never mixed.** The committed range is the recorded pair and does not
  move when the branch moves; the working range is exactly the uncommitted delta; an unrecorded
  endpoint is answered as the body's own `state="unrecorded"` + `stateDetail` for the code half —
  never refused with a status error, and never read as a range measured empty — and is an empty half
  only for memory (260921-ICR-L25, register B6).
- **This module adds no catalog artifact.** It consumes the two existing shared-support fixtures, which
  is why its evidence-catalog footprint is two consumer rows and a re-pinned digest with unchanged
  counts.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the case module's own docstring and
cases, the production owners it drives (the resolution, the capture owner, the comparison, the
comparison route, the leaf change-set view), the register of the module's own catalog footprint, and
the packet requirement it evidences. Three details a reader should carry: the fixture's tracked paths
reproduce the diff fixture's candidate bytes on purpose, so the recorded anchors resolve against the
blobs they recorded; the moved-input case reads both identities out of the refusal rather than
asserting a message; and the module registers no artifact, so the two consumer rows plus the re-pinned
catalog digest are the whole memory-side footprint of adding a case module here.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of what it measures and why injection is excluded: a real enclosure, a real worktree, the real resolution and the real comparison.** | `read_knowledge_review`; `resolve_review_candidate` | mcp/tests/test_knowledge_review_source_endpoints.py:1-25; mcp/tests/test_knowledge_review_source_endpoints.py:44-45 |
| The lane registration: one `unit-regression` row, which is the whole delivery-category footprint. | "mcp/tests/test_knowledge_review_source_endpoints.py" |mcp/tests/test-evidence-lanes.toml:118-118|
| **The catalog footprint: a consumer row on each existing shared-support fixture, so no artifact and no contract is added and the populations do not move.** | "mcp/tests/test_knowledge_review_source_endpoints.py" | mcp/tests/evidence-lifecycle.toml:1405-1441; mcp/tests/evidence-lifecycle.toml:1442-1488 |
| The catalog byte pin the new consumer rows oblige, re-pinned deliberately beside the unchanged counts. | `LIFECYCLE_CATALOG_SHA256`; `LIFECYCLE_ARTIFACT_COUNT` | mcp/tests/test_dependency_ownership_ast_helpers.py:44-65 |
| The fixture's own vocabulary: the tracked paths that reproduce the diff fixture's bytes, the two ways a file is in the candidate and in no commit, the ignored boundary path, and the two committed/working contrast paths. | `MODIFIED_PATH`; `ELIGIBLE_UNTRACKED_PATH`; `STAGED_ADDITION_PATH`; `IGNORED_PATH`; `LOCAL_COMMIT_PATH`; `UNCOMMITTED_PATH` | mcp/tests/test_knowledge_review_source_endpoints.py:113-116; mcp/tests/test_knowledge_review_source_endpoints.py:120-120; mcp/tests/test_knowledge_review_source_endpoints.py:122-122 |
| **The live enclosure: the real contract, the real worktree, the real datasets and the real resolution, with `resolve()` asserted to return a resolution rather than a refusal — and the `memory_mode` shape that composes a real memory half for later leaves without changing the default.** | `EndpointFixture`; `build_endpoint_fixture`; `_enclosure`; `_memory_plan`; `_link_memory_worktree`; `_materialize_candidate`; `_place_datasets` | mcp/tests/test_knowledge_review_source_endpoints.py:122-207; mcp/tests/test_knowledge_review_source_endpoints.py:215-248; mcp/tests/test_knowledge_review_source_endpoints.py:250-292; mcp/tests/test_knowledge_review_source_endpoints.py:294-319; mcp/tests/test_knowledge_review_source_endpoints.py:321-338; mcp/tests/test_knowledge_review_source_endpoints.py:340-369; mcp/tests/test_knowledge_review_source_endpoints.py:371-381 |
| The two contract states a case can produce: a recorded landed commit, and the code-recorded/memory-unrecorded leg. | `recorded_range`; `record_code_with_unrecorded_memory` | mcp/tests/test_knowledge_review_source_endpoints.py:169-174; mcp/tests/test_knowledge_review_source_endpoints.py:176-206 |
| **The bound endpoints and the untouched real index: the two tree ids, the two roots travelling with them, and the captured tree's own paths.** | `test_the_live_candidate_binds_the_recorded_base_and_the_captured_tree` | mcp/tests/test_knowledge_review_source_endpoints.py:436-478 |
| **The falsifier for the packet's non-conforming example: the published ids, the untracked addition the `HEAD`-to-unstaged range cannot reach, the `exact_recorded_blob` locations, and the same ids in the served JSON body.** | `test_the_rendered_review_publishes_the_endpoints_and_reaches_the_whole_candidate` | mcp/tests/test_knowledge_review_source_endpoints.py:470-532 |
| **A moved capture input refused by name, with both identities read out of the refusal.** | `test_a_capture_input_that_moves_before_publication_is_refused_by_name` | mcp/tests/test_knowledge_review_source_endpoints.py:535-559 |
| The capture owner's own mid-capture head check arriving as the surface's named refusal. | `test_a_capture_that_detects_a_moved_head_refuses_instead_of_publishing_a_stale_tree` | mcp/tests/test_knowledge_review_source_endpoints.py:562-593 |
| The moved code head naming exactly the side that moved. | `test_a_moved_code_head_names_the_head_as_the_side_that_moved` | mcp/tests/test_knowledge_review_source_endpoints.py:596-623 |
| **The committed range bound to the recorded commits, unmoved by a later commit, with the working view keeping its own labelled population.** | `test_a_committed_range_binds_the_recorded_commit_and_a_later_commit_does_not_move_it` | mcp/tests/test_knowledge_review_source_endpoints.py:642-692 |
| **An unrecorded committed endpoint answered with its own `state="unrecorded"` and the route's sentence, the head absent from that detail, the counters a measured zero, and the same view reading `recorded` after `recorded_range` — so the state is a discriminator and not a constant.** | `test_an_unrecorded_committed_endpoint_is_answered_with_its_own_state_rather_than_read_from_head` | mcp/tests/test_knowledge_review_source_endpoints.py:695-741 |
| **The route level, which is the whole of B6: `GET /api/changeset/task?…&mode=committed` answers `200` for a live leaf whose landed commit is not recorded, the state survives serialization, and an unknown leaf is still a named `404` — the fix was not bought by turning every absent thing into a `200`.** | `test_the_route_answers_an_unrecorded_committed_view_without_a_status_error` | mcp/tests/test_knowledge_review_source_endpoints.py:744-792 |
| **One side's unrecorded endpoint never discarding the other side's resolved range; the code side reads `recorded` here, which is what keeps it apart from the case above.** | `test_an_unrecorded_memory_half_empties_only_itself_and_keeps_the_code_half` | mcp/tests/test_knowledge_review_source_endpoints.py:795-839 |
| The production owners these cases drive: the resolution, the composition and the route. | `resolve_review_candidate`; `require_current_candidate_identity`; `compose_review`; `register_review_routes` |mcp/src/agents_remember/application/review_candidate_resolution.py:160-247; mcp/src/agents_remember/application/review_candidate_resolution.py:269-298; mcp/src/agents_remember/application/knowledge_review.py:353-541; mcp/src/agents_remember/serving/review.py:542-627
| The leaf change-set view whose two modes the last three cases measure. | `leaf_changeset`; `leaf_file_diff`; `recorded_committed_range` | mcp/src/agents_remember/serving/changeset.py:455-497; mcp/src/agents_remember/serving/changeset.py:596-630; mcp/src/agents_remember/serving/changeset_endpoints.py:87-125 |
| The capture owner the fixture and the recheck both call. | `capture_future_code_candidate`; `FutureCodeCandidateIdentity` | mcp/src/agents_remember/worktrees/modules/future_code_candidate.py:14-51 |
| The fixtures this module consumes instead of introducing a third: the diff-scope fixture that builds the two datasets and the real committed tree, and the read-scope fixture whose paths the cases reuse. | `build_diff_fixture`; `DiffFixture`; `SUCCESSOR_PATH`; `BATCH_PATH_CANDIDATE_TEXT` | mcp/tests/diff_scope_test_support.py:93-94; mcp/tests/diff_scope_test_support.py:113-118; mcp/tests/diff_scope_test_support.py:155-242; mcp/tests/read_scope_test_support.py:116-125 |
| **The merged candidate's own case for the third state: a task-context review whose before half is damaged *states* the damage and still lists the complete source inventory — the refusal teaches the pane and the limitation list, and it does not remove the review.** | `test_a_task_context_review_states_a_damaged_half_and_still_lists_the_source_inventory` | mcp/tests/test_knowledge_review_source_endpoints.py:1071-1106 |
| **The precedence cases: one unreadable half leaves the readable side attributed and the rest unknown; the same pair read completely confirms absence where the lost half could not; a damaged half cannot support a negative conclusion.** | `test_one_unreadable_knowledge_half_leaves_the_readable_side_attributed_and_the_rest_unknown`; `test_the_same_pair_read_completely_confirms_absence_where_the_lost_half_could_not`; `test_a_damaged_knowledge_half_cannot_support_a_negative_attribution_conclusion` | mcp/tests/test_knowledge_review_source_endpoints.py:1118-1118; mcp/tests/test_knowledge_review_source_endpoints.py:1228-1228; mcp/tests/test_knowledge_review_source_endpoints.py:1264-1264 |
| **The empty-generation case: an identified empty first generation counts as completely inspected for absence.** | `test_an_identified_empty_first_generation_counts_as_completely_inspected_for_absence` | mcp/tests/test_knowledge_review_source_endpoints.py:1191-1225 |
| **The receipt cases: an unreadable candidate receipt is stated on the task route and refused on the subject route; a receipt that breaks after the preflight is stated in the pane and the limits.** | `test_an_unreadable_candidate_receipt_is_stated_on_the_task_route_and_refused_on_the_subject_route`; `test_a_receipt_that_breaks_after_the_preflight_is_stated_in_the_pane_and_the_limits` | mcp/tests/test_knowledge_review_source_endpoints.py:1394-1394 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every case runs in-process against a
temporary coordination root, its own repositories and its own datasets.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-28T17:08:17+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test-evidence-lanes.toml`) were re-pointed through the exact base-to-candidate line map; each moved row cites the same line content it cited at base. Wording is unchanged, and no stamp was advanced.
- 2026-09-26T01:00+02:00 — 260921-ICR-L25 curator (completion of the claim re-read recorded in the entry below; leaf `260921-ICR-L25`): **the card's verification metadata is advanced, and one duplicated metadata row is removed.** What was re-read, and when: on 2026-09-26 this seat read the renamed case's own source and confirmed that the row cites its current `def` — `test_an_unrecorded_memory_half_empties_only_itself_and_keeps_the_code_half` at `mcp/tests/test_knowledge_review_source_endpoints.py:795-839` — and that the claim's words match what the case asserts: one side's unrecorded endpoint never discards the other side's resolved range, and the code side reads `recorded` there. **Why the range is what it is:** a *generated mechanical projection* recorded in this document's own history (the `ccr-r10@v1` bullet that repointed the case to `687-719`) is what the gate quotes, and that range is superseded — the case lives at `795-839` since this leaf's own curation re-derived it. The projection is therefore replaced by a hand-derived range, which is the re-citation the guidance asks for. **A metadata defect fixed in the same pass:** the header carried **two** `lastUpdated` rows (`2026-09-23T04:31:57+02:00` and `2026-09-23T04:31`); the duplicate is removed rather than left as a two-valued field. **The stamp now names the last real commit on this line**: `d9e7e6e79ce532d16c689435ae95a63aab430f94` (2026-09-25T22:40:41+02:00). This leaf's delta is uncommitted, so the governed closeout owns the final stamp. No wording was changed to move a number. No commit was made.
- 2026-09-26T00:30+02:00 — 260921-ICR-L25 curator, round 3 (review of a mechanically projected range on the renamed case; leaf `260921-ICR-L25`, candidate `ar/260921-icr-l25-ar`): **the reopened claim was re-read against the current source and both the wording and the range are correct as they now stand.** The case `test_an_unrecorded_memory_half_empties_only_itself_and_keeps_the_code_half` was re-derived by this leaf's own curation and the row cites its current `def` extent; the mechanical projection the finding quotes was the older `ccr-r10@v1` bullet that pointed at `687-719`, which is **not** where the case lives now. The claim's words — that one side's unrecorded endpoint never discards the other side's resolved range, and that the code side reads `recorded` there — are exactly what the case asserts, and were verified by reading the case rather than by trusting the range. So the projection is superseded by a hand-derived range, and that is the re-citation the guidance asks for. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "mcp/tests/test_knowledge_review_source_endpoints.py" repointed to mcp/tests/test-evidence-lanes.toml:117-117. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `MODIFIED_PATH`; `ELIGIBLE_UNTRACKED_PATH`; `STAGED_ADDITION_PATH`; `IGNORED_PATH`; `LOCAL_COMMIT_PATH`; `UNCOMMITTED_PATH` repointed to mcp/tests/test_knowledge_review_source_endpoints.py:113-113; mcp/tests/test_knowledge_review_source_endpoints.py:114-114; mcp/tests/test_knowledge_review_source_endpoints.py:115-115; mcp/tests/test_knowledge_review_source_endpoints.py:116-116; mcp/tests/test_knowledge_review_source_endpoints.py:120-120; mcp/tests/test_knowledge_review_source_endpoints.py:122-122. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `test_a_task_context_review_states_a_damaged_half_and_still_lists_the_source_inventory` repointed to mcp/tests/test_knowledge_review_source_endpoints.py:1071-1106. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `test_an_identified_empty_first_generation_counts_as_completely_inspected_for_absence` repointed to mcp/tests/test_knowledge_review_source_endpoints.py:1191-1225. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T23:45+02:00 — 260921-ICR-L25 curator, round 2 (uncommitted change set on `ar/260921-icr-l25-ar`, code base `d9e7e6e79ce532d16c689435ae95a63aab430f94` plus the working-tree delta, memory base `39adea206651654dbfacf2ee1bb4e2f3763b515b`; round-2 report `report-l25-round2.md` = `9446232d…`): **body update — one case was renamed, one was added at the route level, and the invariant that stated the old behaviour was corrected in place.** The module grew 1434 → 1515 lines (+103/−22). `test_an_unrecorded_committed_endpoint_is_refused_rather_than_read_from_head` is now `test_an_unrecorded_committed_endpoint_is_answered_with_its_own_state_rather_than_read_from_head`: it asserts the body's `state="unrecorded"` with the route's sentence, the counters a measured zero, and — the part that keeps the state a **discriminator** rather than a constant — that the same view reads `state="recorded"` with an empty `stateDetail` after `recorded_range`. `test_the_route_answers_an_unrecorded_committed_view_without_a_status_error` is **new** and asserts the served layer, which is the whole of B6: `GET /api/changeset/task?…&mode=committed` returns **200**, the state survives serialization, and an unknown leaf is **still a named `404`**. It registers the real routes through `register_changeset_routes`, which is why the import block gained that name. **What the module still protects and did not trade away:** `HEAD` is never named in the detail and never substituted for the missing endpoint, and the module's own case for the memory half now records that the code side reads `recorded` there. **Citation accounting:** every row into this module was re-derived from each case's own `def` at this tip — `test_a_committed_range…` `:626-676` → `:642-692`, the renamed case `:679-701` → `:695-741`, the new route case → `:744-792`, `test_an_unrecorded_memory_half…` `:704-747` → `:795-839` — and the row into `serving/changeset.py` was re-derived too (`:402-489` → `leaf_changeset` `:455-497` and `leaf_file_diff` `:596-630`). **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.
- 2026-09-22T09:15:00+02:00 — 260921-ICR-L4 curator (sync-merge resolution of the parked candidate against the landed line, merged base code `d21bc8a6` / memory `75bb4d65`): **additive union with landed `260921-ICR-L14`/`260921-ICR-L3`.** Both sides' history kept newest-first; L14's `memory_mode` fixture shape is now a table row beside this leaf's six new cases, with every range re-derived against the merged 1423-line module (fixture insertion +59, this leaf's cases appended). Lane/lifecycle rows take the landed numbers (`:111`, `:1413`/`:1447`); the `register_review_routes` range takes L3's fix (`serving/review.py:219-298`). Header names the merged base on this leaf's candidate row. No verification stamp was advanced.
- 2026-09-22T08:30:00+02:00 — 260921-ICR-L4 curator (uncommitted change set on `ar/260921-icr-l4`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **six new cases for the precedence and receipt states (938 → 1364 lines).** The module now measures through one real enclosure the states the packet's precedence sentence decides: one unreadable half (readable side attributed, rest unknown), the identified empty first generation, the same pair read completely as the control, the damaged half supporting no negative conclusion, the unreadable receipt stated on the task route and refused on the subject route, and the receipt that breaks after the preflight stated in the pane and the limits. The import hunk moved every pre-existing construct by 17 lines, so every row into this module was re-derived against this candidate; rows into unchanged files are kept as recorded. No lane or catalog row was added — no new test module, so no catalog re-pin. **Stamp accounting:** old verification rows name the last real commit; this leaf's claims were re-read against the candidate and are stamp-class leftovers that only closeout can stamp.
- 2026-09-21T23:24+02:00 — 260921-ICR-L14 curator, **sync-merge resolution of the parked candidate against the landed ICR-L3 curation.** The two sides had curated this document independently and both sets of statements are kept: the landed `260921-ICR-L3` section, rows and history entries alongside this leaf's, tables unioned key by key (a row both sides carried keeps the ranges that hold its anchors in the merged code tree, the other side's range folded in where it is also true; rows only one side carried are kept in their own order), prose sections kept whole and Update History entries merged newest-first. The header states both facts: the production line is the master tip `a8d2431926d6b130012ca81ed2e85b14721c0615` (ICR-L3 landed) and this leaf's own code is still its uncommitted candidate. **Stamp accounting:** no verification stamp was invented; the stamp names the landed production line and the candidate rows name each uncommitted reading.
- 2026-09-21T22:40:00+02:00 — 260921-ICR-L14 curator (uncommitted change set on `ar/260921-icr-l14`, production line `d80a0513e928ef29a973527d09597c82c96fde87`): **the shared endpoint fixture gained one additive keyword, and the card now says what it is for.** `ICR-R14@v1`'s case module needs an enclosure whose contract really has a memory half — the curator authority's canonical path is resolved against it, published there and read back through the production port — so `build_endpoint_fixture` gained `memory_mode="disabled"` with `memory_mode="external"` composing a real memory repository and a linked worktree through `_memory_plan` and `_link_memory_worktree`. The card states the third shape, that the default keeps every pre-existing case byte-identical in what it builds, and that the capability is a fixture feature rather than a new case: this module's own case count and assertions are unchanged (938 → 997 lines, all of the growth in the fixture helper and its plan). **Citation accounting:** every range into this file was re-derived against the moved candidate, because this leaf's insertion moved every case below the fixture — the R02 cases are now `:419-451`, `:453-516`, `:518-543`, `:545-577`, `:579-607`, `:609-660`, `:662-685`, `:687-731`, `:733-810`, `:812-854`, `:856-888` and `:902-960`, `EndpointFixture` `:105-190` and `build_endpoint_fixture` `:192-231`. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` now name the **production line this reading was against** — `d80a0513e928ef29a973527d09597c82c96fde87`, the master line's current tip and this leaf's base — replacing the previous pair rather than leaving a stamp no reading in this pass measured; the candidate is uncommitted, so no commit contains the content a stamp would claim to have verified, and the governed closeout's own metadata refresh re-stamps the card against the code commit its transaction creates.
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **citation repair only, forced by the two consumer rows this leaf's module added.** This file is not a changed source file; the ranges that moved belong to `mcp/tests/test-evidence-lifecycle.toml` and `mcp/tests/test-evidence-lanes.toml`. Three rows were re-read and re-derived from the lines that carry their anchors on this candidate: the lane registration `:107` → `:110`, the two catalog consumer rows `:1410`/`:1439` → `:1411`/`:1444`, and the row naming the production owners, where `register_review_routes` is declared in `mcp/src/agents_remember/serving/review.py` at `:219-298` (the cited `:120-192` holds the port declarations, not the registrar). No claim wording or anchor was changed, and **no verification stamp was advanced** — the recorded stamp is kept, because the candidate is uncommitted and closeout owns the real commit.
- 2026-09-21T19:16:12+00:00: Generated citation repair: "mcp/tests/test_knowledge_review_source_endpoints.py" repointed to mcp/tests/test-evidence-lanes.toml:111-111. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-21T19:16:12+00:00 — retired by the 260921-ICR-L12 curator: this mechanical bullet bound `test_the_live_candidate_binds_the_recorded_base_and_the_captured_tree` to mcp/tests/test_knowledge_review_source_endpoints.py:419-450. The claim at `:199` was re-read against the case as this leaf strengthened it — the case now measures that both bound objects resolve in the repository the resolution names, with `git cat-file -t` — and re-cited to the case's own extent, mcp/tests/test_knowledge_review_source_endpoints.py:436-478. The review is what disposes of the projection, not the projection; no verification stamp was advanced because the candidate is uncommitted.
- 2026-09-21T19:16:12+00:00: Generated citation repair: `test_the_rendered_review_publishes_the_endpoints_and_reaches_the_whole_candidate` repointed to mcp/tests/test_knowledge_review_source_endpoints.py:453-512. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-21T19:16:12+00:00: Generated citation repair: `test_a_capture_input_that_moves_before_publication_is_refused_by_name` repointed to mcp/tests/test_knowledge_review_source_endpoints.py:518-542. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-21T19:16:12+00:00: Generated citation repair: `test_a_capture_that_detects_a_moved_head_refuses_instead_of_publishing_a_stale_tree` repointed to mcp/tests/test_knowledge_review_source_endpoints.py:545-576. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-21T19:16:12+00:00: Generated citation repair: `test_a_moved_code_head_names_the_head_as_the_side_that_moved` repointed to mcp/tests/test_knowledge_review_source_endpoints.py:579-603. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-21T19:16:12+00:00: Generated citation repair: `test_a_committed_range_binds_the_recorded_commit_and_a_later_commit_does_not_move_it` repointed to mcp/tests/test_knowledge_review_source_endpoints.py:609-659. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-21T19:16:12+00:00: Generated citation repair: `test_an_unrecorded_committed_endpoint_is_refused_rather_than_read_from_head` repointed to mcp/tests/test_knowledge_review_source_endpoints.py:662-684. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-21T19:16:12+00:00: Generated citation repair: `test_an_unrecorded_memory_half_empties_only_itself_and_keeps_the_code_half` repointed to mcp/tests/test_knowledge_review_source_endpoints.py:687-719. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-21T19:16:12+00:00: Generated citation repair: `test_a_task_context_review_states_a_damaged_half_and_still_lists_the_source_inventory` repointed to mcp/tests/test_knowledge_review_source_endpoints.py:962-997. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-21T18:09+02:00 — 260921-ICR-L20 curator (uncommitted change set on `ar/260921-icr-l20`, production line `71a4433e686b3380af97a0836bb82bab2c8f2aad`): **citation repair only, forced by this leaf's own moves in the files this card cites.** The source file this card documents did **not** change; this leaf appended one row to `mcp/tests/test-evidence-lanes.toml` at `:89` and two consumer rows to `mcp/tests/evidence-lifecycle.toml` at `:733` and `:1271`, so every lane row below `:88` shifted by one and every evidence-catalog line below those rows by one and two respectively. Each affected row was re-read against the construct it names and its range re-derived from that construct's own extent in the moved file — and, where a row's anchor is a lane or consumer entry, from the line that actually carries it — rather than shifted by a remembered delta. No claim was re-worded, no anchor was renamed and no row was dropped, and no verification stamp was advanced — the candidate is uncommitted and the governed closeout owns the real commits.
- 2026-09-21T15:17:00+02:00 — 260921-ICR-L2 curator, **the sync's code-side resolution added one case to this module and adapted two, and the card records all three.** `test_a_task_context_review_states_a_damaged_half_and_still_lists_the_source_inventory` (`903-938`) is the merged candidate's own case for the third state leaf `260921-ICR-L5`'s refusal introduced into leaf `260921-ICR-L2`'s task-context entry: a damaged before half is *stated* and the complete source inventory is still listed, which is the property neither leaf could measure alone. `test_an_unrecorded_memory_half_empties_only_itself_and_keeps_the_code_half` gained the adapted assertions inside its existing extent. Every row above was re-derived against the merged 938-line module rather than carried: the fixture row now cites the class and its five helpers at their own extents (`104-188`, `198-222`, `225-261`, `264-292`, `295-304`), and the four R02 cases keep the ranges the pre-merge candidate measured. No verification stamp was advanced: the candidate is uncommitted and closeout owns the real stamp.
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, base `702714fc05363cb28eacaf101ba8384475a6aa56`): **the fixture gained a no-datasets shape and the module gained the four cases R02 is measured by.** `build_endpoint_fixture(datasets=False)` plus `EndpointFixture.task_request` build the leaf a task with no knowledge actually has; the new cases measure the complete inventory with neither dataset half (through the payload *and* the real route with no selector parameters), filename identity for a tab/newline name carried by the shipped capture, non-text and mode-changed paths listed rather than dropped, and the non-UTF-8 boundary as a **partial** inventory that still answers 200 — the fix for the 500 the first draft produced. The module is now 900 lines against the same 900-line soft signal and 1200-line hard rail; the master ruling that keeps the consolidation is recorded on the boundary module's card. Citation rows were re-derived against this candidate. **Stamp accounting:** the verification rows still name `702714fc05363cb28eacaf101ba8384475a6aa56`, the last real commit on this line, because nothing in this leaf is committed; claims whose evidence this leaf's change moved were re-read against the candidate and are stamp-class leftovers that only closeout can stamp.

- 2026-09-21T13:07:00+02:00 — 260921-ICR-L1 curator (uncommitted change set on `ar/260921-icr-l1`, base `f745e16659c5602252bb185a2ffccc356c2bde26`): created this one-to-one card for the case module the leaf added as the production-composition evidence for `ICR-R01@v1`. The card records the eight cases as the packet's required demonstrations (bound endpoints with a byte-identical real index; the whole candidate reached, with the `HEAD`-to-unstaged population measured as different; a moved capture input refused by name with both identities; the capture owner's own head check surfaced as that refusal; the moved head named exactly; the committed range bound to the recorded commits and unmoved by a later commit; an unrecorded code endpoint refused by name without leaking the head; an unrecorded memory half emptying only itself) and records the module's **catalog footprint**: two consumer rows on the existing `diff_scope_test_support`/`read_scope_test_support` artifacts, no new artifact and no new contract, hence a re-pinned catalog digest with the counts unchanged, plus one `unit-regression` lane row. **Stamp accounting:** the two verification rows name `f745e16659c5602252bb185a2ffccc356c2bde26`, the last real commit on this line, because the external-memory refresh gate requires verification metadata before the memory commit; every construct this card cites exists only in this leaf's uncommitted candidate and no commit contains the content those rows would otherwise claim to have verified, so the governed closeout owns the real stamp.
## 260921-ICR-L12 The Live Candidate Root Names The Repository That Holds The Object

`260921-ICR-L12` (`ICR-R12@v1`) changes one landed assertion in this module, and the change is
reported here because it changes a dependency's stated value rather than adding to it. The case that
measures the bound endpoints asserted `resolved.candidate_code_root == contract.code_worktree`; the
candidate root now names the **repository** (`contract.code_repo_path`), because a tree id is
resolvable exactly where the object lives, a linked worktree shares its repository's object store, and
the repository is the root a durable comparison generation records — which is what lets a closed leaf's
review reproduce the live comparison byte for byte.

The assertion was **strengthened rather than re-pointed**: it now measures that both bound objects
really resolve in the repository the resolution named (`git cat-file -t` in that root for the baseline
and the candidate tree), so the stronger fact is a measurement and not a restatement of the
implementation. The fixture and every other case in the module are unchanged, and the new
committed-leaf cases build on this module's enclosure fixture rather than duplicating it.

## Update History
- 2026-09-23T04:45:00+02:00 — 260921-ICR-L12 curator, **review of a mechanically projected range (the check's own disposition request)**: the projection bullet above was retired after the claim it names was re-read against the construct its own words describe, and re-cited to that construct's declaration rather than to the mention the projection had bound. Answering the check's two questions: (1) the construct the new range covers does support the claim's wording; (2) the old range arrived by mechanical anchor-range projection, which is exactly why it is not evidence that the claim holds — the review, not the projection, is what disposes of it. The bullet is retired rather than left standing because a projection that has been superseded by a curator's re-citation would otherwise keep asking the same question forever.
- 2026-09-23T04:30:48+02:00 — 260921-ICR-L12 curator (candidate `ar/260921-icr-l12`, uncommitted; production line at this leaf's base `870701b43039cd205a8c98e418382729510c3de3`, confirmed from the enclosure contract): **the live candidate root names the repository that holds the object (ICR-R12@v1).** One landed
assertion changed value and got stronger — both bound objects are measured to resolve in the named
repository with `git cat-file -t` — because a reopened comparison can only reproduce the live one if the
root is the repository the record names. **Citation accounting:** every row into this module was
re-derived against the candidate. **Stamp accounting:** no verification stamp was advanced — the
candidate is uncommitted and the governed closeout owns the real stamp.

