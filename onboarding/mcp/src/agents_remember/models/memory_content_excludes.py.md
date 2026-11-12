# mcp/src/agents_remember/models/memory_content_excludes.py

## Governing Overview

[models overview](overview.md)

## Purpose

The shared declaration of **what a memory-content commit never contains**. Its live consumers
are baseline adoption, direct landing and external closeout. Baseline adoption applies the tuple
while staging; direct landing and external closeout apply it while capturing the exact memory
content tree, and external closeout also uses it for the dirty check. Carryover restores worktree
content and creates no memory-content commit; it no longer consumes this constant. The source
module's four-seam docstring describes the earlier design, not the current callers.

The two members are real policy, not implementation detail:

- `memory.md` is the **computed ledger cache**, derived from the memory content and committed by
  its own transaction, so it is never carried along with the content it was computed from;
- `bootstrap/` is **transient bootstrap scaffolding** and is never part of a memory commit —
  neither the first baseline nor any later one.

## Code Commentary

### Logic

Three module constants and nothing else. `LEDGER_CACHE_RELATIVE_PATH` is `"memory.md"` and
`BOOTSTRAP_SCAFFOLDING_RELATIVE_PATH` is `"bootstrap"`; `MEMORY_CONTENT_EXCLUDES` is the
two-tuple the live consumers pass as `exclude_paths=`.

**They are worktree-relative path *names*, not Git pathspecs.** That distinction is the whole
reason this docstring exists and is the defect it was written from: the staging helpers take
names and build the pathspec themselves. `stage_worktree_content` runs
`git add -A -- . :(top,exclude)<name>` for each entry *and* `git update-index --force-remove --
<name>`; a pathspec string passed in here would be mangled into
`:(top,exclude):(exclude)bootstrap` and would silently match nothing.

The exclusion is only real because it rides the call that actually stages. `commit_if_dirty`
re-stages the whole worktree, so an exclusion applied to a bare `git add` *before* it is inert
and the file lands in the commit anyway. Baseline adoption therefore passes the tuple on its
actual private-index staging call. The historical baseline regression
`test_memory_branch_authority.py::test_the_first_baseline_never_commits_bootstrap_scaffolding`
fails if the old spelling returns.

### Conventions

- Baseline adoption, direct landing and external closeout read the shared constant. An added
  exclusion therefore reaches those consumers without three independent tuple edits.
- The declared name is the worktree-relative name. Never store a `:(...)` pathspec, and never
  store a glob.
- Exclusion means **excluded from the commit**, not deleted from the worktree: the developer's
  transient files stay on disk and show up as untracked content afterwards.

### Invariants And Boundaries

- Baseline adoption, direct landing and external closeout exclude `memory.md` and `bootstrap/`
  from their memory-content trees. Carryover does not create a memory-content commit.
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
- The staging helpers turn names into exclusion pathspecs and remove derived entries from the index. [2]
- Baseline adoption passes the shared exclusions on the private-index staging call. [3]
- Carryover applies worktree content without staging, committing or consuming this exclusion tuple. [4]
- External closeout applies the shared exclusions to its dirty check and exact memory-tree capture. [5]

- Since MIK-R09 the mandatory gate's exact-tree captures use it too (the closeout's `_exact_memory_tree`, direct landing's `_memory_content_tree`), so the tree the gate judges leaves out what the memory commit leaves out. [6]

- Direct landing applies the shared exclusions when capturing its exact memory-content tree. [7]

- Baseline adoption and commit_if_dirty regression cases exclude bootstrap scaffolding while leaving it on disk; they do not execute carryover or a full closeout. [8]

### Cross-Repo References

No sibling-repository contract defines this exclusion policy.

No meaningful cross-repo references found.
