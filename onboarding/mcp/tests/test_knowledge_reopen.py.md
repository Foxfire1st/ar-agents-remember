# mcp/tests/test_knowledge_reopen.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**Reopen after a converted closeout, end to end (L37 ruling of 2026-10-01T01:57:55).** A leaf reopened after its
closeout keeps its closed history file frozen and writes a new, attempt-qualified file. The five cases follow one
leaf through the writer, the gate, the validator's freeze, the index, the onboarding gate and record landing.

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

### Conventions

- The world is `knowledge_gate_test_support.build_gated`; `_close_out_and_integrate` closes the history, commits
  both sides, lands them on `main` and leaves the leaf reopened on a line that holds its frozen file.

### Invariants And Boundaries

- The first file's bytes are asserted unchanged after every later step: the freeze is byte-level.
- Trace rows are presence-based: a closed `onboarding_trace` row answers a reopened leaf's item for the same card.

### Todos

- None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the L37 rulings of 2026-10-01T01:57:55 and 03:36:39 (Q6) in `37_cutover-to-text-storage.json`, with `MIK-R07@v2` rule 7; it lives outside the code and memory
repositories, so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: the reopen ruling under test. [1]
- A reopened leaf writes its next attempt, and its history is every file. [2]
- Attempt files are named, ordered and backward compatible. [3]
- The closeout closes the latest attempt and never reopens a closed one. [4]
- The gate names the attempt the writer writes. [5]
- Record landing refuses when the landed history cannot be listed. [6]
- The history target under test. [7]
- The merged reading under test. [8]

### Cross-Repo References

No meaningful cross-repo references found: the suite builds scratch repositories under its temporary directory.

No cross-repo boundary is crossed by this file.
