# test_memory_branch_authority.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

The shipped behavioral check for **which branch a repository's memory is founded on**, plus the retained
bootstrap role/no-task-altitude shape and memory-content exclusion that keeps bootstrap scaffolding
out of a memory commit. Removed supplied-document/taskless launch checks are not current coverage.

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

**Seventeen source test definitions in four retained groups.** The module drives the real public operations
(`memory_init_tool`, `memory_baseline_adopt_tool`) on real Git repositories created under
`tmp_path`; it installs `MCP_SRC` and `MCP_TESTS` on `sys.path` so it exercises the shipped modules
rather than a copy.

*Group 1 — the memory branch is chosen, recorded and followed (12 cases).* Minting records the
named branch and validates the recorded name against a real ref; an omitted branch inherits the code
repository's checked-out branch, and the call **refuses rather than inventing `main`** when neither
source has an answer. The unborn repair path accepts the configured branch. For an already-referenced repository the named case asserts `ok=True`, no `repairAttempted`, and unchanged ref/HEAD rather than refusal; a value that is not one local branch name is refused, and a
recorded `refs/heads/` spelling is accepted and normalized. Baseline adoption follows the configured
branch, refuses a branch the memory repository does not record, and the memory default-branch
accessor validates the recorded name against its refs while still refusing a recorded name with no
ref. An absent coordination root is refused before anything is created.

*Group 2 — the bootstrap role's remaining shape (2 definitions).* The source asserts the bootstrap role has no task altitude and no task-altitude set names it. The removed taskless-role-set admission checks supply no present coverage.

*Group 3 — the reviewed round-2 findings, pinned (2 cases).* `bootstrap/` is absent from the first
baseline's commit and still on disk afterwards, asserted on `git ls-files` — the committed tree — not
on a comment; and the same exclusion holds on the helper a later memory commit uses. These are the
two cases that fail if the exclusion goes inert again. Both now run under a bound validator: fresh
`memory_init` trees are converted, so the first baseline validates the staged tree through the
knowledge validator instead of committing unvalidated, and the `bound_validation` fixture binds real
worktree services (`GitKnowledgeValidation` with `GitBaseConverter`) for exactly that.

*Group 4 — the manifest (1 definition).* The retained manifest check asserts no task altitude for the free agent. The former supplied-document/taskless launch-argument check is removed; it supplies no current admission guarantee. These are inspected source assertions, not executed test acceptance.


## Evidence

### Docs References

No external or domain documentation governs this repository-local check.

No relevant documentation found after checking live sources.

### Repo-Internal References

- The module's own statement of the property, the four seams, and the two-sides rule. [1]
- Group 1 — minting, inheriting and refusing to invent a branch. [2]
- Group 1 — the repair path, the name narrowing, and the recorded spelling. [3]
- Group2 asserts bootstrap is published outside every task-altitude role set, not taskless policy bypass. [5]
- Group4 checks the manifest bootstrap altitude is nonblank and not sprint/master/leaf while task roles keep their own altitude; no supplied-document resolution coverage remains. [7]
- The branch authority the first group drives. [8]
- The adoption seam whose hard-coded `main` the first group replaced. [9]
- The recorded-name validation the first group holds, and its malformed-name refusal. [10]
- The exclusion policy the third group pins. [12]
- The lane row that keeps the fail-closed evidence registry loading clean. [15]

- Converted first baselines run under a bound validator via the bound_validation fixture. [16]


### Cross-Repo References

No sibling-repository contract defines this check.

No meaningful cross-repo references found.

- Group 1 — adoption follows the recorded branch, and the default-branch accessor validates it. [4]
- Group 3 — the exclusion, pinned on the commit tree. [6]
- The staging helper the third group's failure mode lives in. [13]
