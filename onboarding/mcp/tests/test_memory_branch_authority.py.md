# test_memory_branch_authority.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

The shipped behavioral check for **which branch a repository's memory is founded on**, plus the two
structures the same leaf introduced: the free agent's taskless admission, and the memory-content
exclusion that keeps bootstrap scaffolding out of a memory commit.

Its leading property is stated in its own module docstring: the memory repository's initial branch
is the branch the developer names, and every seam that later compares a branch against "the memory
repository's default" reads that recorded name instead of a hard-coded one. Four seams carry it and
each one refuses if it is wrong — `memory_init` mints and records the branch, its repair path
accepts the recorded branch instead of demanding `refs/heads/main`, `_baseline_default_branch`
follows the recorded branch so the first baseline can be adopted on a repository founded on
anything, and `memory_repository_default_branch` validates the recorded name against the refs that
exist rather than against the literal `main`.

## Code Commentary

### Logic

**Twenty cases in four groups.** The module drives the real public operations
(`memory_init_tool`, `memory_baseline_adopt_tool`) on real Git repositories created under
`tmp_path`; it installs `MCP_SRC` and `MCP_TESTS` on `sys.path` so it exercises the shipped modules
rather than a copy.

*Group 1 — the memory branch is chosen, recorded and followed (12 cases).* Minting records the
named branch and validates the recorded name against a real ref; an omitted branch inherits the code
repository's checked-out branch, and the call **refuses rather than inventing `main`** when neither
source has an answer. The unborn repair path accepts the configured branch and still refuses a
repository that already carries refs; a value that is not one local branch name is refused, and a
recorded `refs/heads/` spelling is accepted and normalized. Baseline adoption follows the configured
branch, refuses a branch the memory repository does not record, and the memory default-branch
accessor validates the recorded name against its refs while still refusing a recorded name with no
ref. An absent coordination root is refused before anything is created.

*Group 2 — the free agent's shape (4 cases).* The `bootstrap` role is a free agent with no task
altitude; without a task document only the named taskless roles are admitted; the set is a named,
readable export rather than a bare literal inside a refusal; and no task altitude set in the source
names `bootstrap`. The group's own banner records the developer ruling it protects, so a later
reader cannot "fix" the seat by giving it the altitude it must not have.

*Group 3 — the reviewed round-2 findings, pinned (2 cases).* `bootstrap/` is absent from the first
baseline's commit and still on disk afterwards, asserted on `git ls-files` — the committed tree — not
on a comment; and the same exclusion holds on the helper a later memory commit uses. These are the
two cases that fail if the exclusion goes inert again.

*Group 4 — the taskless document and the manifest (2 cases).* A document supplied to a taskless role
still resolves but skips the altitude check, so a bad reference is still refused; and the manifest
declares no task altitude for the free agent while the nine task-bound roles keep theirs, which
keeps the exception scoped.

### Conventions

- Every case creates its own repository under `tmp_path` and drives the public operation; no fixture
  is shared across cases and no test reaches into a private helper to assert a private fact.
- Every comparison takes its two sides from different artifacts — the recorded config, the actual
  ref, the returned payload, and, where a refusal is the behaviour, the refusal's own text. That is
  what makes a case falsifiable rather than self-derived.
- The module is registered in `mcp/tests/test-evidence-lanes.toml` under `unit-regression`; a new
  case belongs in this module rather than in a separate ad-hoc script.
- The one production spelling the cases read is imported, not restated:
  `DEFAULT_BRANCH_CONFIG_KEY` comes from `kernel.memory_init` and `MEMORY_CONTENT_EXCLUDES` from
  `models.memory_content_excludes`, so a rename fails the case instead of silently passing.

### Invariants And Boundaries

- **The memory branch is data, never a constant.** Every comparison validates the recorded name
  against a real ref; no case may be "fixed" by reintroducing a comparison against `main`.
- **`bootstrap/` is excluded from memory-content commits, not deleted from the worktree.** The
  second half of the assertion is as load-bearing as the first: the developer's transient files stay
  on disk as untracked content.
- **The exclusion must ride the call that stages.** An exclusion applied to a bare `git add` before
  `commit_if_dirty` re-stages the worktree is inert; the case exists precisely because that was
  measured as broken.
- **The taskless set is policy, not an implementation detail.** The case asserts the export is named
  and readable, so the ruling stays legible to the next reader instead of collapsing into a literal.
- **A taskless role still resolves a supplied document.** Being exempt from the altitude check is not
  a licence to skip resolution; a bad reference stays refused.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation governs this repository-local check.

No relevant documentation found after checking live sources.

### Repo-Internal References

- The module's own statement of the property, the four seams, and the two-sides rule. [1]
- Group 1 — minting, inheriting and refusing to invent a branch. [2]
- Group 1 — the repair path, the name narrowing, and the recorded spelling. [3]
- Group 1 — adoption follows the recorded branch, and the default-branch accessor validates it. [4]
- Group 2 — the free agent's shape, with the ruling the group protects. [5]
- Group 3 — the exclusion, pinned on the commit tree. [6]
- Group 4 — a supplied document still resolves, and the manifest exception stays scoped. [7]
- The branch authority the first group drives. [8]
- The adoption seam whose hard-coded `main` the first group replaced. [9]
- The recorded-name validation the first group holds, and its malformed-name refusal. [10]
- The taskless admission the second and fourth groups hold. [11]
- The exclusion policy the third group pins. [12]
- The staging helper the third group's failure mode lives in. [13]
- The lane row that keeps the fail-closed evidence registry loading clean. [14]

### Cross-Repo References

No sibling-repository contract defines this check.

No meaningful cross-repo references found.
