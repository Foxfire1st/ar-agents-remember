# mcp/tests/test_knowledge_reopen.py

## Governing Overview

[tests route overview](overview.md)

## Purpose
Checks append-only leaf attempt histories and the exact-tree memory gate on closeout and recovery.

## Code Commentary
A reopened leaf writes its next attempt without reopening a closed history file; the latest row about a subject governs across attempts. Closeout closes the latest attempt, preview reads its verdict, and an unconverted preview now refuses with the central legacy-format message before invariant evaluation. A continued leaf creates its next attempt. A file rewritten while the gate runs must not be committed unjudged, and a missing landed history refuses by name. Removed canonical-dataset reopen scenarios are historical, not current helpers or tests. This card records assertions, not a passing run.

The same-size, same-second Git rewrite scenario imports the single `rewrite_in_the_second_of_the_index_write` owner from [knowledge_index_test_support.py](knowledge_index_test_support.py.md). Its real clock alignment is the scenario's subject; the 120-second alignment guard does not assert scheduler speed. The original captured-tree/currentness assertions remain at this file's test owner.

### Logic
- `test_a_reopened_leaf_writes_its_next_attempt_and_its_history_is_every_file`:
  1. attempt 1 is answered through the writer, the gate passes and the leaf closes out and integrates;
  2. a new edit reopens the invariant, its family and the file/route onboarding traces: the closed
     source-bound trace rows still bind the first edit's blobs and are stale for the new edit. The
     gate's refusal names `<leaf>-attempt-2.json`;
  3. the writer writes the rows, including the refreshed source-bound traces, into attempt 2
     (`attempt: 2`, open); the closed first file keeps its bytes;
  4. the parsed tree's `histories[leaf]` is the merged reading and `history_files` holds both paths; the index
     answers "rows about X" from both files; MIK-R30's `_history_rows` reads both and retains each
     winning onboarding row together with its own file's closed flag;
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
  - `test_an_unconverted_leafs_preview_carries_no_gate_verdict`: historical name retained, but now asserts
    `knowledge-gate-refused`, legacy-format guidance, no invariant-gate evaluation and unchanged sides.
  - `test_a_file_rewritten_while_the_gate_runs_is_never_committed_unjudged`: a card rewritten in place, same size,
    in the second its index was written, after the gate judged, is refused before the memory commit's Git mutation ("changed
    while the gate ran") with the closing and `.gitignore` restored; on the rerun the commit and its proof are bound
    to the judged tree, and files written after the judged-tree check stay uncommitted.
- **A leaf that continues after a closeout that was not integrated (INV-MS9BMJ).**
  - `test_a_leaf_that_continues_after_its_closeout_writes_its_next_attempt`: nothing left to commit is still
    judged; the committed closed file may not be edited (`R22.7-history-frozen`); a new edit is refused, naming
    attempt 2; the writer starts attempt 2, naming the file and overview traces again beside the
    re-anchor and sibling comment row. The second closeout closes it with the first file byte-identical;
    a frozen invariant row whose entry the writer carried is not judged again; the landing check freezes the first attempt
    only once the contract records that closeout.
  - `test_the_latest_row_about_a_subject_governs_across_attempts`: for the writer, the gate's currentness and
    the validator's re-anchor rule; a `changed` row that restates no earlier `changed` row is refused. The refusal request explicitly supplies `world.gate().worklist`, so it reaches revision/changed-row admission rather than stopping at missing-worklist preflight.

### Conventions
- The world is `knowledge_gate_test_support.build_gated`; `_close_out_and_integrate` closes the history, commits
  both sides, lands them on `main` and leaves the leaf reopened on a line that holds its frozen file.
- `_Continued` is that world with a contract that can record the leaf's completed closeout that was not
  integrated (`closed_out`). `_closeout` runs `external_closeout_commits` with only the journal hooks stubbed;
  `_public_closeout` and `_public_preview` run `closeout_result` whole, with only what the fixture has none of
  stubbed (the enclosure admission, the operation journal, a remote's branch authority). Since the candidate
  verdict's memory-refresh check resolves its own context through `closeout_external`, `_public_preview` stubs
  that module's `contract_context` at the same seam.

### Invariants And Boundaries
- The first file's bytes are asserted unchanged after every later step: the freeze is byte-level.
- Trace rows are source-bound, not presence-based: a closed row with `sources` can stale after a new
  source edit and must be judged again in the next attempt. Only sourceless historical rows have
  closed-file compatibility; a sourceless row in an open file answers nothing. `_write` recomputes
  the leaf worklist when none is supplied so overview rows bind the item's actual source set. Closed
  history remains byte-frozen; that freeze does not make a source-bound answer permanently current.

### Todos
- None recorded.

## Evidence

### Repo-Internal References

- `test_a_reopened_leaf_writes_its_next_attempt_and_its_history_is_every_file` owns the current boundary described above. [25]
- `test_the_public_closeout_refuses_an_open_item_and_commits_once_it_is_answered` owns the current boundary described above. [26]


- The shared owner establishes a same-size rewrite in the index-write second. [29]


- The module docstring: reopen after a converted closeout. [30]
- Attempt files are named, ordered and backward compatible. [32]
- The closeout closes the latest attempt and never reopens a closed one. [33]
- The gate names the attempt the writer writes. [34]
- Record landing refuses when the landed history cannot be listed. [35]
- The history target under test. [36]
- The public closeout refuses an open item and commits once it is answered. [38]
- The closeout preview answers what the apply will do. [39]

- Legacy preview refuses without evaluating the invariant gate or changing the compared sides. [40]

- A file rewritten while the gate runs is never committed unjudged. [42]
- A world whose contract records the leaf's completed closeout that was not integrated. [44]
- The public closeout, run whole. [45]

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is `MIK-R07@v2` rule 7 and `MIK-R09@v2` rules 3 and 5, with the decision records DEC-0AEQ28
(attempt files) and DEC-TJ0CX7 (the gate at the plain closeout) in this memory's `knowledge/decisions/`.

No configured live documentation source was available for this pass.

### Cross-Repo References

No meaningful cross-repo references found: the suite builds scratch repositories under its temporary directory.

No cross-repo boundary is crossed by this file.

- Reopening after a new source edit asks invariant, family and file/route traces again in attempt 2; the first history stays byte-identical. [31]
- The merged reading includes refreshed attempt-2 traces, and `_history_rows` keeps the winning row's own closed flag. [37]
- A continued leaf writes its next attempt, including file/overview source-bound traces after the new edit; frozen invariant history remains separate. [41]
- Current source delta inspected statically: Replace closed-trace presence claims with refreshed source bindings and own-file closed provenance; retain freeze and exact-tree assertions. [46]

- `test_a_file_rewritten_while_the_gate_runs_is_never_committed_unjudged` owns the current boundary described above. [27]
- `test_the_latest_row_about_a_subject_governs_across_attempts` owns the current boundary described above. [28]
- The latest row about a subject governs across attempts. [43]
