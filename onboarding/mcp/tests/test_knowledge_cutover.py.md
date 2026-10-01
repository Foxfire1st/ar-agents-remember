# mcp/tests/test_knowledge_cutover.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The cutover's carried completions, tested on unconverted and converted fixture worlds (MIK-R37; L37 P1).** Nine
cases cover the cutover lock at every route, the frozen database, the rule that no production read selects the
database of a converted tree, and the shape of `origin.handoff.evidence`. The routes that need the CLI or the MCP
tool surface are tested beside their own suites: `knowledge-bootstrap` and the crossing owner's rows in
`test_knowledge_writer.py`, and the unheld read seeds in `test_knowledge_index_surfaces.py`.

## Code Commentary

### Logic

- **The lock at every route.** `_ROUTES` names fourteen route entries (knowledge-ingest, the database writer,
  memory-quality at leaf and repository scope, `worktree_sync`, the closeout validator and commit, the prepared
  closeout, direct landing, record landing with and without a named memory commit, a leaf's integration, a master
  or checkpoint landing, and the landing gate). `test_every_route_refuses_unconverted_memory_once_the_repository_holds_converted_memory`
  runs them in an unconverted world with a converted sibling branch: each refuses, naming `branch converted-line`
  and the crossing sync. With that branch deleted, each returns `None`.
- `test_the_prepared_closeout_refuses_by_the_lock_at_both_entry_points`: `execute_selected_closeout` and
  `_realize_prepared_memory` both raise with the code `unconverted-memory-locked`.
- `test_a_converted_worktree_locks_too_and_an_unanswered_probe_refuses`: an uncommitted marker in a registered
  worktree locks; a timeout and a non-zero probe both refuse as "never read as unlocked", the second with Git's
  own message.
- `test_only_a_definite_non_repository_reads_as_holding_no_converted_memory` (review R1 F4): a plain directory is
  unlocked; a pruned linked worktree, a `dubious ownership` exit and a `PermissionError` refuse by name.
- `test_a_bare_repository_git_cannot_open_refuses_by_name` (review R2-3): a healthy bare repository holds no lines;
  one Git cannot open refuses.
- `test_the_converting_candidate_is_gated_never_locked`: a candidate that holds the marker is judged by the gate
  (the port is called once) and never by the lock; a crossing sync and a code-only sync pass; the leaf's own
  converted commit lands on its unconverted line; a repository-level run on a converted checkout is not locked.
- `test_the_database_writer_is_frozen_on_a_converted_tree_and_names_the_file_writer`: `as_write_admission` raises
  `KnowledgeDatabaseFrozen` naming `knowledge-ingest`; a publication is refused `database_frozen` and writes
  nothing; an unconverted tree in a repository with no converted memory is admitted.
- `test_no_read_selects_the_database_of_a_converted_tree` (L23 F8): with the dataset reader patched to fail,
  `resolve_published_intent`, the final-output receipt and the sync rebinding answer `not-recorded`, and the
  unchanged-knowledge freeze returns the tree-comparison refusal.
- `test_hand_off_evidence_is_a_list_of_strings` (L24 carry).

### Conventions

- The worlds come from `knowledge_gate_test_support` (`build_gated`, `commit`, `git`); `_unconverted` builds an
  unconverted leaf beside a converted sibling branch named `LINE`.
- The module imports no CLI or MCP surface, which keeps it out of the dependency-ownership census's pinned
  consumers.

### Invariants And Boundaries

- Each guard is pinned by a mutation that the case kills (worker and reviewer mutation runs, 33 in review R2).
- The file holds proof entries (`proves`) for INV-JT28KJ (the cutover lock), INV-1XKX9ERN (the frozen database) and
  INV-T9M21FB4 (the unchanged-knowledge freeze refuses a converted leaf).

### Todos

- None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is `MIK-R37@v1` rules 3 and 6, `MIK-R09@v2` rule 6 and `MIK-R24@v1` rule 9, with the L37 decisions in `37_cutover-to-text-storage.json`; it lives outside the code and memory
repositories, so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: what the suite covers and where the CLI and MCP routes are tested. [1]
- Fourteen routes refuse while a branch is converted and return nothing once it is deleted. [2]
- A converted worktree locks, and an unanswered probe refuses. [3]
- Only a definite non-repository is unlocked. [4]
- A bare repository Git cannot open refuses by name. [5]
- The converting candidate is gated, never locked. [6]
- The database writer is frozen on a converted tree. [7]
- No read selects the database of a converted tree. [8]
- The lock under test. [9]

### Cross-Repo References

No meaningful cross-repo references found: the suite builds scratch repositories under its temporary directory.

No cross-repo boundary is crossed by this file.
