# mcp/tests/test_knowledge_review_source_endpoints.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_review_source_endpoints.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-21T13:07:00+02:00 |
| reviewedWorkingCandidate | candidate `ar/260921-icr-l1`, uncommitted; base `f745e16659c5602252bb185a2ffccc356c2bde26` |
| lastVerifiedCommitHash | `702714fc05363cb28eacaf101ba8384475a6aa56` |
| lastVerifiedCommitDate | 2026-09-21T13:27:46+02:00|
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
  endpoint is a refusal by name for the code half and an empty half only for memory.
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
| **The module's own statement of what it measures and why injection is excluded: a real enclosure, a real worktree, the real resolution and the real comparison.** | `read_knowledge_review`; `resolve_review_candidate` | mcp/tests/test_knowledge_review_source_endpoints.py:1-25; mcp/tests/test_knowledge_review_source_endpoints.py:33-37 |
| The lane registration: one `unit-regression` row, which is the whole delivery-category footprint. | "mcp/tests/test_knowledge_review_source_endpoints.py" | mcp/tests/test-evidence-lanes.toml:105-105 |
| **The catalog footprint: a consumer row on each existing shared-support fixture, so no artifact and no contract is added and the populations do not move.** | "mcp/tests/test_knowledge_review_source_endpoints.py" | mcp/tests/evidence-lifecycle.toml:1404-1404; mcp/tests/evidence-lifecycle.toml:1435-1435 |
| The catalog byte pin the new consumer rows oblige, re-pinned deliberately beside the unchanged counts. | `LIFECYCLE_CATALOG_SHA256`; `LIFECYCLE_ARTIFACT_COUNT` | mcp/tests/test_dependency_ownership_ast_helpers.py:44-65 |
| The fixture's own vocabulary: the tracked paths that reproduce the diff fixture's bytes, the two ways a file is in the candidate and in no commit, the ignored boundary path, and the two committed/working contrast paths. | `MODIFIED_PATH`; `ELIGIBLE_UNTRACKED_PATH`; `STAGED_ADDITION_PATH`; `IGNORED_PATH`; `LOCAL_COMMIT_PATH`; `UNCOMMITTED_PATH` | mcp/tests/test_knowledge_review_source_endpoints.py:82-96 |
| **The live enclosure: the real contract, the real worktree, the real datasets and the real resolution, with `resolve()` asserted to return a resolution rather than a refusal.** | `EndpointFixture`; `build_endpoint_fixture`; `_enclosure`; `_materialize_candidate`; `_place_datasets` | mcp/tests/test_knowledge_review_source_endpoints.py:103-172; mcp/tests/test_knowledge_review_source_endpoints.py:181-199; mcp/tests/test_knowledge_review_source_endpoints.py:201-281 |
| The two contract states a case can produce: a recorded landed commit, and the code-recorded/memory-unrecorded leg. | `recorded_range`; `record_code_with_unrecorded_memory` | mcp/tests/test_knowledge_review_source_endpoints.py:135-172 |
| **The bound endpoints and the untouched real index: the two tree ids, the two roots travelling with them, and the captured tree's own paths.** | `test_the_live_candidate_binds_the_recorded_base_and_the_captured_tree` | mcp/tests/test_knowledge_review_source_endpoints.py:336-367 |
| **The falsifier for the packet's non-conforming example: the published ids, the untracked addition the `HEAD`-to-unstaged range cannot reach, the `exact_recorded_blob` locations, and the same ids in the served JSON body.** | `test_the_rendered_review_publishes_the_endpoints_and_reaches_the_whole_candidate` | mcp/tests/test_knowledge_review_source_endpoints.py:370-431 |
| **A moved capture input refused by name, with both identities read out of the refusal.** | `test_a_capture_input_that_moves_before_publication_is_refused_by_name` | mcp/tests/test_knowledge_review_source_endpoints.py:434-458 |
| The capture owner's own mid-capture head check arriving as the surface's named refusal. | `test_a_capture_that_detects_a_moved_head_refuses_instead_of_publishing_a_stale_tree` | mcp/tests/test_knowledge_review_source_endpoints.py:461-492 |
| The moved code head naming exactly the side that moved. | `test_a_moved_code_head_names_the_head_as_the_side_that_moved` | mcp/tests/test_knowledge_review_source_endpoints.py:495-522 |
| **The committed range bound to the recorded commits, unmoved by a later commit, with the working view keeping its own labelled population.** | `test_a_committed_range_binds_the_recorded_commit_and_a_later_commit_does_not_move_it` | mcp/tests/test_knowledge_review_source_endpoints.py:525-575 |
| **An unrecorded committed endpoint refused by name with the live head absent from the message, while the working view stays readable.** | `test_an_unrecorded_committed_endpoint_is_refused_rather_than_read_from_head` | mcp/tests/test_knowledge_review_source_endpoints.py:578-601 |
| **One side's unrecorded endpoint never discarding the other side's resolved range.** | `test_an_unrecorded_memory_half_empties_only_itself_and_keeps_the_code_half` | mcp/tests/test_knowledge_review_source_endpoints.py:603-635 |
| The production owners these cases drive: the resolution, the composition and the route. | `resolve_review_candidate`; `require_current_candidate_identity`; `compose_review`; `register_review_routes` | mcp/src/agents_remember/application/review_candidate_resolution.py:130-226; mcp/src/agents_remember/application/knowledge_review.py:377-485; mcp/src/agents_remember/serving/review.py:120-192 |
| The leaf change-set view whose two modes the last three cases measure. | `leaf_changeset`; `leaf_file_diff`; `recorded_committed_range` | mcp/src/agents_remember/serving/changeset.py:402-489; mcp/src/agents_remember/serving/changeset_endpoints.py:87-125 |
| The capture owner the fixture and the recheck both call. | `capture_future_code_candidate`; `FutureCodeCandidateIdentity` | mcp/src/agents_remember/worktrees/modules/future_code_candidate.py:14-51 |
| The fixtures this module consumes instead of introducing a third: the diff-scope fixture that builds the two datasets and the real committed tree, and the read-scope fixture whose paths the cases reuse. | `build_diff_fixture`; `DiffFixture`; `SUCCESSOR_PATH`; `BATCH_PATH_CANDIDATE_TEXT` | mcp/tests/diff_scope_test_support.py:93-94; mcp/tests/diff_scope_test_support.py:112-112; mcp/tests/diff_scope_test_support.py:155-242; mcp/tests/read_scope_test_support.py:116-125 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every case runs in-process against a
temporary coordination root, its own repositories and its own datasets.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-21T13:07:00+02:00 — 260921-ICR-L1 curator (uncommitted change set on `ar/260921-icr-l1`, base `f745e16659c5602252bb185a2ffccc356c2bde26`): created this one-to-one card for the case module the leaf added as the production-composition evidence for `ICR-R01@v1`. The card records the eight cases as the packet's required demonstrations (bound endpoints with a byte-identical real index; the whole candidate reached, with the `HEAD`-to-unstaged population measured as different; a moved capture input refused by name with both identities; the capture owner's own head check surfaced as that refusal; the moved head named exactly; the committed range bound to the recorded commits and unmoved by a later commit; an unrecorded code endpoint refused by name without leaking the head; an unrecorded memory half emptying only itself) and records the module's **catalog footprint**: two consumer rows on the existing `diff_scope_test_support`/`read_scope_test_support` artifacts, no new artifact and no new contract, hence a re-pinned catalog digest with the counts unchanged, plus one `unit-regression` lane row. **Stamp accounting:** the two verification rows name `f745e16659c5602252bb185a2ffccc356c2bde26`, the last real commit on this line, because the external-memory refresh gate requires verification metadata before the memory commit; every construct this card cites exists only in this leaf's uncommitted candidate and no commit contains the content those rows would otherwise claim to have verified, so the governed closeout owns the real stamp.
