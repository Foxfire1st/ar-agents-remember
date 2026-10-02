# mcp/tests/test_knowledge_reopen.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**A leaf that writes again after its closeout, and the gate at the worktree closeout, end to end (decision records
DEC-0AEQ28 and DEC-TJ0CX7).** A leaf whose closeout closed its history file keeps that file frozen and writes a new,
attempt-qualified file. The first five test functions follow one leaf, reopened after its integration, through the
writer, the gate, the validator's freeze, the index, the onboarding gate and record landing. The other fourteen
cover the worktree closeout's gate and its preview, a leaf that continues after a closeout that was not integrated,
the judged tree, the governing row across attempts, and the writer's `items`. 19 test functions.

## Code Commentary

### Logic

- `test_a_reopened_leaf_writes_its_next_attempt_and_its_history_is_every_file`:
  1. attempt 1 is answered through the writer, the gate passes and the leaf closes out and integrates;
  2. a new edit reopens the invariant and its family (the closed rows no longer hold), while the closed trace rows
     still count, and the gate's refusal names `<leaf>-attempt-2.json`;
  3. the writer writes the rows into attempt 2 (`attempt: 2`, open) and the closed file keeps its bytes;
  4. the parsed tree's `histories[leaf]` is the merged reading and `history_files` holds both paths; the index
     answers "rows about X" from both files; MIK-R30's `_history_rows` reads both;
  5. a hand edit of the frozen file is refused by the validator (`R22.7`);
  6. record landing refuses an open second attempt (`knowledge-history-not-closed`), and after the second closeout
     passes, with the first file still byte-identical.
- `test_attempt_files_are_named_ordered_and_backward_compatible`: `history_path`, `owner_history_attempt`,
  `writable_attempt`, the refusal of `attempt` on a wave and of `attempt: 1`, and a first file with no `attempt` key.
- `test_the_closeout_closes_the_latest_attempt_and_never_reopens_a_closed_one`: with only a closed first file the
  closeout writes nothing; with an open second attempt it closes that one.
- `test_the_gate_names_the_attempt_the_writer_writes` (review R1 F10a): an attempt only the candidate closes is
  still the one named, never a next attempt.
- `test_record_landing_refuses_when_the_landed_history_cannot_be_listed` (review R1 F5): an open second attempt is
  `history-not-closed`; with `ls-tree` failing the finding is `run-incomplete`, never the closed first file alone.
- **The gate at the worktree closeout (INV-HWAWFT, INV-49E649, INV-WV1YQE).**
  - `test_the_public_closeout_refuses_an_open_item_and_commits_once_it_is_answered` enters through
    `closeout.closeout_result`: with an invariant item and its family item open it raises, naming both, with nothing
    committed or written on either side; once the rows exist it commits both sides, closes the history file and
    records itself in the contract, without integrating.
  - `test_the_closeout_preview_answers_what_the_apply_will_do`: a refused leaf's preview is
    `knowledge-gate-refused` (return code 2) with the findings, no commit approval and no next tool; sixty findings
    are capped at fifty with `truncated`; a passing preview is `would-closeout` with `knowledge_gate` pass, and
    the apply that follows evaluates the gate once more only, for the exact tree at the commit.
  - `test_an_unconverted_leafs_preview_carries_no_gate_verdict`: no `knowledge_gate` block and no evaluation.
  - `test_a_recovered_closeout_is_gated_like_a_fresh_one`: a resumed closeout records a commit the gate passes,
    refuses one committed by hand with an item open, and the finalization of a recovered closeout asks the gate
    before it proves the commits.
  - `test_the_closeouts_own_writes_cannot_trip_its_gate`: with the real metadata refresh, the judged tree is the
    committed tree; the closeout itself wrote `.gitignore`, the history closing, `entities.md` and two index
    caches; the worklist digest and items are identical before and after.
  - `test_a_file_rewritten_while_the_gate_runs_is_never_committed_unjudged`: a card rewritten in place, same size,
    in the second its index was written, after the gate judged, is refused before the memory commit's Git mutation ("changed
    while the gate ran") with the closing and `.gitignore` restored; on the rerun the commit and its proof are bound
    to the judged tree, and files written after the judged-tree check stay uncommitted.
- **A leaf that continues after a closeout that was not integrated (INV-MS9BMJ).**
  - `test_a_leaf_that_continues_after_its_closeout_writes_its_next_attempt`: nothing left to commit is still
    judged; the committed closed file may not be edited (`R22.7-history-frozen`); a new edit is refused, naming
    attempt 2; the writer starts attempt 2 and the second closeout closes it, with the first file byte-identical;
    a frozen row whose entry the writer carried is not judged again; the landing check freezes the first attempt
    only once the contract records that closeout.
  - `test_a_history_file_closed_by_a_hand_commit_is_not_frozen`: such a file is still read and refused at the
    closeout; the gate's memo tells two leaf heads apart.
  - `test_the_latest_row_about_a_subject_governs_across_attempts`: for the writer, the gate's currentness and
    the validator's re-anchor rule; a `changed` row that restates no earlier `changed` row is refused.
- **The governing row of a changed record (INV-XN0FG8).**
  - `test_a_changed_record_is_governed_by_its_changed_row_in_every_attempt`: (a) the same revision step restated
    with a corrected effect and reason; (b) a later `no_impact` row held open by the gate and refused by the
    validator; (c) a second change at the next revision with its own `changed` row, the record two revisions
    ahead of the parent line; and the validator alone refusing a hiding row at a recorded landing.
  - `test_a_change_on_the_parent_line_may_be_answered_by_any_later_row`: the validator rule's two limits, and a
    `changed` row that cannot restate once a `no_impact` row is the leaf's latest earlier row.
  - `test_a_family_whose_guarantee_the_leaf_changed_is_governed_by_its_changed_row` and
    `test_a_route_condition_reads_the_one_governing_family_row_across_attempts`: a family's one governing row; a
    later `changed` row answers a route condition, a later `no_impact` row reopens it.
- `test_the_writer_fills_a_rows_items_from_the_leafs_worklist`: items the hand-off names are kept, a row that
  names none gets the items it answers, and a missing or malformed worklist fills nothing and refuses nothing.

### Conventions

- The world is `knowledge_gate_test_support.build_gated`; `_close_out_and_integrate` closes the history, commits
  both sides, lands them on `main` and leaves the leaf reopened on a line that holds its frozen file.
- `_Continued` is that world with a contract that can record the leaf's completed closeout that was not
  integrated (`closed_out`). `_closeout` runs `external_closeout_commits` with only the journal hooks stubbed;
  `_public_closeout` and `_public_preview` run `closeout_result` whole, with only what the fixture has none of
  stubbed (the enclosure admission, the operation journal, a remote's branch authority).

### Invariants And Boundaries

- The first file's bytes are asserted unchanged after every later step: the freeze is byte-level.
- Trace rows are presence-based: a closed `onboarding_trace` row answers a reopened leaf's item for the same card.

### Todos

- None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is `MIK-R07@v2` rule 7 and `MIK-R09@v2` rules 3 and 5, with the decision records DEC-0AEQ28
(attempt files) and DEC-TJ0CX7 (the gate at the plain closeout) in this memory's `knowledge/decisions/`.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: reopen after a converted closeout. [1]

- A reopened leaf writes its next attempt, and its history is every file. [2]
- Attempt files are named, ordered and backward compatible. [3]
- The closeout closes the latest attempt and never reopens a closed one. [4]
- The gate names the attempt the writer writes. [5]
- Record landing refuses when the landed history cannot be listed. [6]
- The history target under test. [7]
- The merged reading under test. [8]

- The public closeout refuses an open item and commits once it is answered. [9]
- The closeout preview answers what the apply will do. [10]
- An unconverted leaf's preview carries no gate verdict. [11]
- A leaf that continues after its closeout writes its next attempt. [12]
- A file rewritten while the gate runs is never committed unjudged. [13]
- The latest row about a subject governs across attempts. [14]
- A changed record is governed by its changed row in every attempt. [15]
- A change on the parent line may be answered by any later row. [16]
- A family whose guarantee the leaf changed is governed by its changed row. [17]
- A route condition reads the one governing family row across attempts. [18]
- The writer fills a row's items from the leaf's worklist. [19]
- A history file closed by a hand commit is not frozen. [20]
- A recovered closeout is gated like a fresh one. [21]
- The closeout's own writes cannot trip its gate. [22]
- A world whose contract records the leaf's completed closeout that was not integrated. [23]
- The public closeout, run whole. [24]

### Cross-Repo References

No meaningful cross-repo references found: the suite builds scratch repositories under its temporary directory.

No cross-repo boundary is crossed by this file.
