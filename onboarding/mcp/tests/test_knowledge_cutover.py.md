# mcp/tests/test_knowledge_cutover.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Checks the converted-memory cutover lock across the admitted write/closeout/sync routes and the refusal of canonical database reads.

## Code Commentary


The probes distinguish a definite repository absence from an unreadable or ambiguous Git repository, assert unconverted-route refusal both with and without converted memory elsewhere, use a converted worktree only to word recovery guidance, and permit the converting candidate only through its gate. A read case asserts that no read selects a database for a converted tree; another validates hand-off evidence as strings. The old database-writer-freeze test is removed and cannot be cited as a current writer execution. These source assertions are not a current run certificate.

### Logic

The integration gate moved to `modules/integration_gate.py`. The synthetic master gate probe holds chain proof passing because it has no canonical task/enclosure population; it is gate/cutover evidence, not a chain-proof witness. The converted leaf case allows a validator refusal but asserts it is never an unconverted-memory lock.

- `test_the_prepared_closeout_refuses_by_the_lock_at_both_entry_points`: `execute_selected_closeout` and
  `_realize_prepared_memory` both raise with the code `unconverted-memory-locked`.
- `test_a_converted_worktree_locks_too_and_an_unanswered_probe_refuses`: an uncommitted marker in a registered worktree is named in the already-required unconverted refusal; it does not decide admission. A timeout and a non-zero probe retain their named "never read as unlocked" errors, the second with Git's own message.
- `test_only_a_definite_non_repository_reads_as_holding_no_converted_memory` (review R1 F4): a plain directory is
  unlocked; a pruned linked worktree, a `dubious ownership` exit and a `PermissionError` refuse by name.
- `test_a_bare_repository_git_cannot_open_refuses_by_name` (review R2-3): a healthy bare repository holds no lines;
  one Git cannot open refuses.
- `test_the_converting_candidate_is_gated_never_locked`: a candidate that holds the marker is judged by the gate
  (the port is called once) and never by the lock; a crossing sync and a code-only sync pass; the converted leaf pair reaches judgment without the cutover-lock refusal, while its
  synthetic validator may still refuse; a repository-level run on a converted checkout is not locked.

- `test_no_read_selects_the_database_of_a_converted_tree`: `resolve_published_intent` selects a derived
  database beneath the coordination runtime/knowledge-index directory, not the legacy `knowledge.sqlite`.
  The legacy bytes remain unchanged. This test calls no freeze, final-output receipt or sync rebinding and
  installs no dataset-reader failure patch; it is not a proof of unchanged-knowledge freeze refusal.
- `test_hand_off_evidence_is_a_list_of_strings` (L24 carry).

### Conventions

- The worlds come from `knowledge_gate_test_support` (`build_gated`, `commit`, `git`); `_unconverted` builds an
  unconverted leaf beside a converted sibling branch named `LINE`.

- `_unconverted` builds the unconverted world with **one** unconverted commit under both the `main` and the `leaf`
  branch, beside a converted sibling branch. Two separate commits would be the same commit only when they fall in
  one second; otherwise their merge base is the converted commit, and the sync is a crossing sync, which is rightly
  not refused.

### Invariants And Boundaries

- Each guard is pinned by a mutation that the case kills (worker and reviewer mutation runs, 33 in review R2).

The following is the original proof inventory, before MIK-R26 removed the frozen-database case; it is not the current proof-entry inventory. Only the surviving cutover assertions remain current proof evidence; the historical unchanged-knowledge relation is withdrawn because its bound test no longer exercises that API.

- The file holds proof entries (`proves`) for INV-JT28KJ (the cutover lock), INV-1XKX9ERN (the frozen database) and
  INV-T9M21FB4 (the unchanged-knowledge freeze refuses a converted leaf).

### Todos

- None recorded.

## Evidence


### Repo-Internal References

- `test_no_read_selects_the_database_of_a_converted_tree` owns the current boundary described above. [12]
- `test_a_converted_worktree_locks_too_and_an_unanswered_probe_refuses` owns the current boundary described above. [13]

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is `MIK-R37@v1` rules 3 and 6, `MIK-R09@v2` rule 6 and
`MIK-R24@v1` rule 9; the packets live outside the code and memory repositories, so they are named here and not
cited as a row. The historical decisions DEC-FCNRNT (conditional repository-wide lock) and DEC-VMMJDN (unlocked onboarding card writers) are superseded for current operations by MIK-R46@v2: unconverted memory is read or converted, while ordinary operations refuse it with the central `legacy-format` message. The converted-memory-location probe only supplies recovery wording; it does not admit a never-converted repository.

No configured live documentation source was available for this pass.


- Converted memory elsewhere words the already-required legacy refusal; unreadable probes retain their named error [14]

- Only a definite non-repository is unlocked. [15]
- A bare repository Git cannot open refuses by name. [16]

- The converting candidate is gated, never locked. [17]

- No read selects the database of a converted tree. [18]
- The lock under test. [19]
- One unconverted commit under both branches. [20]

### Cross-Repo References

No meaningful cross-repo references found: the suite builds scratch repositories under its temporary directory.

No cross-repo boundary is crossed by this file.

- `test_every_route_refuses_unconverted_memory_with_or_without_converted_memory_elsewhere` asserts the unconditional `legacy-format` refusal and conversion step, including after the only converted branch is removed. [11]
