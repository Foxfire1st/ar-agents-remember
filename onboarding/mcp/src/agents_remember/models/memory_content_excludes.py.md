# mcp/src/agents_remember/models/memory_content_excludes.py

## Governing Overview

[models overview](overview.md)

## Purpose

The one declaration of **what a memory-content commit never contains**. Four seams create
memory-content commits — baseline adoption, memory carryover, external closeout and direct
landing — and every one of them used to spell its own inline exclusion tuple. This module is the
lowest layer all four can read, so a fifth exclusion is added once instead of being missed in
three places.

The two members are real policy, not implementation detail:

- `memory.md` is the **computed ledger cache**, derived from the memory content and committed by
  its own transaction, so it is never carried along with the content it was computed from;
- `bootstrap/` is **transient bootstrap scaffolding** and is never part of a memory commit —
  neither the first baseline nor any later one.

## Code Commentary

### Logic

Three module constants and nothing else. `LEDGER_CACHE_RELATIVE_PATH` is `"memory.md"` and
`BOOTSTRAP_SCAFFOLDING_RELATIVE_PATH` is `"bootstrap"`; `MEMORY_CONTENT_EXCLUDES` is the
two-tuple every producing seam passes as `exclude_paths=`.

**They are worktree-relative path *names*, not Git pathspecs.** That distinction is the whole
reason this docstring exists and is the defect it was written from: the staging helpers take
names and build the pathspec themselves. `stage_worktree_content` runs
`git add -A -- . :(top,exclude)<name>` for each entry *and* `git update-index --force-remove --
<name>`; a pathspec string passed in here would be mangled into
`:(top,exclude):(exclude)bootstrap` and would silently match nothing.

The exclusion is only real because it rides the call that actually stages. `commit_if_dirty`
re-stages the whole worktree, so an exclusion applied to a bare `git add` *before* it is inert
and the file lands in the commit anyway — that was this leaf's baseline defect, and
`test_memory_branch_authority.py::test_the_first_baseline_never_commits_bootstrap_scaffolding`
fails if the old spelling returns.

### Conventions

- Adding an exclusion is a one-line change here plus no seam edit: the four producers already
  read this constant. That is the property the module exists to create.
- The declared name is the worktree-relative name. Never store a `:(...)` pathspec, and never
  store a glob.
- Exclusion means **excluded from the commit**, not deleted from the worktree: the developer's
  transient files stay on disk and show up as untracked content afterwards.

### Invariants And Boundaries

- A memory-content commit contains no `memory.md` and no `bootstrap/` path, on all four
  producing seams — first baseline, carryover, external closeout and direct landing.
- The constant is the only sanctioned source of those names. A literal `("memory.md",)` at a
  content-staging seam is the drift this module removes.
- Non-content staging seams (candidate-tree digests, cleanliness gates) keep their own narrower
  exclusions deliberately: widening them would change what "the memory worktree is clean" means
  for every other task.
- The staging helper takes names; this module must not start producing pathspecs.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation governs this repository-local exclusion policy.

No relevant documentation found after checking live sources.

### Repo-Internal References

- The declared policy: the ledger cache, the bootstrap scaffolding, and their one tuple. [1]
- The staging helper that turns each name into `:(top,exclude)<name>` plus an `update-index --force-remove`. [2]
- Producer 1 — baseline adoption consumes the constant on the call that stages. [3]
- Producer 2 — memory carryover consumes the same constant in its apply path. [4]
- Producer 3 — external closeout consumes it on the dirty check, the stage and the commit. [5]

- Since MIK-R09 the mandatory gate's exact-tree captures use it too (the closeout's `_exact_memory_tree`, direct landing's `_memory_content_tree`), so the tree the gate judges leaves out what the memory commit leaves out. [6]

- Producer 4 — direct landing consumes it on its memory commit. [7]
- The two cases that fail if the exclusion becomes inert again. [8]

### Cross-Repo References

No sibling-repository contract defines this exclusion policy.

No meaningful cross-repo references found.
