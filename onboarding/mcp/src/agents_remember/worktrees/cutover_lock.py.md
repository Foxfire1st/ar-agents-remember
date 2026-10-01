# mcp/src/agents_remember/worktrees/cutover_lock.py

## Governing Overview

[worktrees route overview](overview.md)

## Purpose

**The cutover lock: unconverted memory is read, never written, checked, synced or landed (MIK-R09 rule 6, second
bullet; MIK-R24 rule 9).** A route that has already decided its memory is unconverted on every side asks this module
one question: does the memory repository hold converted memory anywhere? If it does, the route refuses and names the
crossing sync. If it does not, the route behaves exactly as it did before the text-storage master. The module holds
no switch, flag or install-time state: the lock is a fact about the repository.

## Code Commentary

### Logic

- **When the lock holds (L37 ruling).** `converted_memory_location(repository)` answers where the repository holds
  converted memory, or `None`:
  - `_converted_branch` lists every local branch tip (`for-each-ref refs/heads`) and asks one
    `cat-file --batch-check` whether each tip holds `knowledge/layout.json`. The first branch that does is named
    `branch <name>`.
  - `_converted_worktree` lists the registered worktrees (`worktree list --porcelain`) and looks for the marker
    file in each working tree. The first that holds it is named `worktree <path>`.

  The second probe is why the lock is live from the installation of the cutover build: the cutover leaf's memory
  worktree holds the converted tree before any branch tip does (MIK-R37 rule 2).
- **`cutover_lock_refusal(repository, *, operation, line)`** is the one entry every route calls. It returns `None`
  when there is no repository directory or the repository holds no converted memory. Otherwise it returns the
  refusal sentence: the operation, the line, where the converted memory is, that unconverted memory is only read
  (`legacy-format`), and that the line converts through `worktree_sync`, the crossing sync (MIK-R24 rule 8).
- **Who calls it.** The worktree layer reaches it through `knowledge_gate.leaf_cutover_refusal` (the closeout
  validator, the closeout memory commit, direct landing, record landing, a leaf's integration),
  `knowledge_gate.prepared_closeout_lock` (both prepared-closeout entries), `knowledge_gate.landing_gate_refusal`
  (master and checkpoint landing), `knowledge_crossing.unconverted_line_refusal` (writes and leaf memory-quality
  runs) and `sync_transaction._cutover_locked` (managed sync admission). The application and CLI layers call it
  directly for the database writer's front door, a repository-level memory-quality run, `knowledge-bootstrap` and
  `memory_carryover_apply`.

### Conventions

- The caller decides that the route's sides are unconverted. This module never reads a contract and never judges a
  candidate: a converting candidate holds the marker on its own side, so its route goes to the gate, against the
  converted base (MIK-R24 rule 7), and never asks the lock.
- The lock is scoped to the memory repository of the route it guards. Another code repository's memory is locked
  only once it holds converted memory itself.

### Invariants And Boundaries

- **Fail closed.** `_git` turns a non-zero exit, a timeout and an `OSError` into `CutoverProbeError`, and
  `cutover_lock_refusal` words that as a refusal: "an unanswered probe is never read as unlocked".
- **Only a definite non-repository is unlocked.** `_is_repository` answers `False` only when `git rev-parse
  --git-dir` fails **and** nothing on disk says there is a repository: `_holds_git_entry` finds no `.git` entry in
  the directory or any parent, and the directory is not itself a bare repository (`HEAD` plus `objects/`). A pruned
  linked worktree, a `safe.directory` ownership refusal, a permission error or a broken repository raises
  `CutoverProbeError`. The check is structural, so a localized Git message cannot read as "unlocked".
- **A refused route writes nothing here.** The module only reads Git metadata and the marker file.
- **Never create a converted branch or worktree in a live memory repository outside a leaf.** One branch tip or one
  registered worktree that holds the marker locks every unconverted line of that repository, for every session on
  the machine. Experiments use a `git clone --shared` scratch clone.

### Todos

- None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is `MIK-R09@v2` rule 6, `MIK-R24@v1` rule 9 and `MIK-R37@v1`
rule 6 of task `260928_maintained-invariant-knowledge`, with the rulings in its leaf document
`37_cutover-to-text-storage.json` (2026-10-01T03:36:39 and 2026-10-01T05:05:16); they live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: what is refused, when the lock holds, and fail closed. [1]
- Where the repository holds converted memory: a branch tip, then a registered worktree. [2]
- Every local branch tip is asked for the marker in one batch. [3]
- A registered worktree whose working tree holds the marker locks too. [4]
- The refusal: an unanswered probe refuses by name, and a locked repository names the crossing sync. [5]
- Only a definite non-repository reads as holding no converted memory. [6]
- A `.git` entry in the directory or a parent, or a bare repository, says there is a repository. [7]
- A failed or timed-out Git probe is named, never read as empty output. [8]
- The worktree layer's routes reach the lock through one helper that names the leaf's line. [9]
- Every route refuses unconverted memory once the repository holds converted memory, and is unchanged once it does not. [10]
- The converting candidate is gated, never locked. [11]
- A plain directory is unlocked; a pruned worktree, an ownership refusal and a permission error refuse by name. [12]

### Cross-Repo References

No meaningful cross-repo references found: the module probes one memory repository through Git.

No cross-repo boundary is crossed by this file.
