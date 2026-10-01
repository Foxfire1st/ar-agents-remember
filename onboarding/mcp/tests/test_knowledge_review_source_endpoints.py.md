# mcp/tests/test_knowledge_review_source_endpoints.py

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

**The attribution-precedence cases live next door.** `260921-ICR-L4` added six `ICR-R04@v1` cases here:
the precedence across knowledge availability, and the two candidate-receipt states. `260921-ICR-L57`
moved them verbatim into
[`test_knowledge_review_attribution_precedence.py`](test_knowledge_review_attribution_precedence.py.md)
when this module crossed the 1200-line rail (1515 → 1093 lines, 20 → 14 cases). That module builds its
enclosure through this module's `build_endpoint_fixture`, `EndpointFixture` and `LEAF_ID`, which is one
more reason the fixture's default shape must not change.

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the case module's own docstring and
cases, the production owners it drives (the resolution, the capture owner, the comparison, the
comparison route, the leaf change-set view), the register of the module's own catalog footprint, and
the packet requirement it evidences. Three details a reader should carry: the fixture's tracked paths
reproduce the diff fixture's candidate bytes on purpose, so the recorded anchors resolve against the
blobs they recorded; the moved-input case reads both identities out of the refusal rather than
asserting a message; and the module registers no artifact, so the two consumer rows plus the re-pinned
catalog digest are the whole memory-side footprint of adding a case module here.

- **The module's own statement of what it measures and why injection is excluded: a real enclosure, a real worktree, the real resolution and the real comparison.** [1]
- The lane registration: one `unit-regression` row, which is the whole delivery-category footprint. [2]
- **The catalog footprint: a consumer row on each existing shared-support fixture, so no artifact and no contract is added and the populations do not move.** [3]
- The catalog byte pin the new consumer rows oblige, re-pinned deliberately beside the unchanged counts. [4]
- The fixture's own vocabulary: the tracked paths that reproduce the diff fixture's bytes, the two ways a file is in the candidate and in no commit, the ignored boundary path, and the two committed/working contrast paths. [5]
- **The live enclosure: the real contract, the real worktree, the real datasets and the real resolution, with `resolve()` asserted to return a resolution rather than a refusal — and the `memory_mode` shape that composes a real memory half for later leaves without changing the default.** [6]
- The two contract states a case can produce: a recorded landed commit, and the code-recorded/memory-unrecorded leg. [7]
- **The bound endpoints and the untouched real index: the two tree ids, the two roots travelling with them, and the captured tree's own paths.** [8]
- **The falsifier for the packet's non-conforming example: the published ids, the untracked addition the `HEAD`-to-unstaged range cannot reach, the `exact_recorded_blob` locations, and the same ids in the served JSON body.** [9]
- **A moved capture input refused by name, with both identities read out of the refusal.** [10]
- The capture owner's own mid-capture head check arriving as the surface's named refusal. [11]
- The moved code head naming exactly the side that moved. [12]
- **The committed range bound to the recorded commits, unmoved by a later commit, with the working view keeping its own labelled population.** [13]
- **An unrecorded committed endpoint answered with its own `state="unrecorded"` and the route's sentence, the head absent from that detail, the counters a measured zero, and the same view reading `recorded` after `recorded_range` — so the state is a discriminator and not a constant.** [14]
- **The route level, which is the whole of B6: `GET /api/changeset/task?…&mode=committed` answers `200` for a live leaf whose landed commit is not recorded, the state survives serialization, and an unknown leaf is still a named `404` — the fix was not bought by turning every absent thing into a `200`.** [15]
- **One side's unrecorded endpoint never discarding the other side's resolved range; the code side reads `recorded` here, which is what keeps it apart from the case above.** [16]
- The production owners these cases drive: the resolution, the composition and the route. [17]
- The leaf change-set view whose two modes the last three cases measure. [18]
- The capture owner the fixture and the recheck both call. [19]
- The fixtures this module consumes instead of introducing a third: the diff-scope fixture that builds the two datasets and the real committed tree, and the read-scope fixture whose paths the cases reuse. [20]
- **The merged candidate's own case for the third state: a task-context review whose before half is damaged *states* the damage and still lists the complete source inventory — the refusal teaches the pane and the limitation list, and it does not remove the review.** [21]

### Cross-Repo References

No cross-repository behavior is implemented in this file. Every case runs in-process against a
temporary coordination root, its own repositories and its own datasets.

No meaningful cross-repo references found.

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
