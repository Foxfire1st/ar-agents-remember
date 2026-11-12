# mcp/src/agents_remember/application/worktree_code_state.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The code tree a read observes, and the working-tree capture it reads through (MIK-R73 rule 7).** A read
answers over the bytes the caller is working with. When the checkout holds uncommitted changes those bytes
belong to no commit, so the module captures the working tree with Git's own isolated mechanism and holds that
capture for the length of the read.

## Code Commentary

### Logic

- `head_tree_id(repository)` is `HEAD^{tree}`, or `None` for a root that cannot be read or has no commit — the
  caller then states `unmeasured`.
- `worktree_is_clean(repository)` asks `git status --porcelain -z --untracked-files=normal
  --ignore-submodules=none` and counts untracked files and submodule changes as dirt: an untracked file is
  still a byte the caller is working with, and `git status` reports a gitlink.
- `capture_worktree(repository)` makes a scratch directory and calls `capture_tree_into` (the same capture the
  knowledge index uses) — a scratch index seeded from the repository's, `git add --all`, `git write-tree`,
  with the new blobs staged in a scratch object store. It returns a `WorktreeCapture(repository, tree_id,
  object_directory)`; `close()` removes the scratch index and store.
- `hold_observed_code_tree(repository)` returns `(ObservedCodeTree | None, WorktreeCapture | None)`: a clean
  checkout gives `CODE_STATE_COMMIT` with the commit's own tree and no capture; a dirty one gives the
  captured tree, `CODE_STATE_WORKING_TREE` unless the captured id equals `HEAD`'s (then `commit`), and the
  capture for the caller to close.
- `observed_code_tree(repository)` is the single-step form: a context manager that closes the capture when
  the read ends.

### Conventions

- `ObservedCodeTree.to_document()` is the wire shape: `repositoryRoot`, `treeId`, `codeState`.
- The scratch store is read-only input to the observer; the repository's index, refs, object store and
  worktree are never opened for writing.

### Invariants And Boundaries

- **Immutability is mechanical, not promised:** nothing captured enters the repository, and a second capture
  of an unchanged worktree returns the same tree id.
- **The capture lives exactly as long as the read.** A multi-step reader holds it to its last page; a
  one-step reader closes it.
- **A continuation captures again.** Because no store outlives its page, a continued working-tree walk
  re-captures; an unchanged worktree continues, a changed one is refused so the rest of a stale anchor set is
  never served.
- **A clean checkout answers at the commit** and captures nothing.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is `MIK-R73@v1` rule 7
of task `260928_maintained-invariant-knowledge`; the packet lives outside the code and memory repositories and
is named here, not cited as a row.

### Repo-Internal References

No numbered references are recorded for this new module. The capture mechanism it reuses is
`memory/knowledge_index/tree.py::capture_tree_into`, whose own card carries its contract.

### Cross-Repo References

None: one code checkout, named by its caller.
