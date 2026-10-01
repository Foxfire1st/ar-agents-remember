# mcp/src/agents_remember/kernel/memory_init.py

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`memory_init.py` provides the package-owned `c-00-initialize-memory-repo` skill memory scaffold behavior used
by the `memory_init` MCP tool.

## Code Commentary

### Logic

`initialize_memory` (mcp/src/agents_remember/kernel/memory_init.py:216-317) resolves the repo through
`McpRuntimeConfig`, plans or creates the external memory root, establishes its Git authority, then
creates the standard `system/`, `onboarding/`, and `docs/` folders and seed system files.

Before L4, `_git_init_result` ran that initialization through the package's one
git runner with `run_git(memory_root, ["init"])`, replacing the local
`subprocess.run(["git", "init"], cwd=memory_root, ...)` this file used to spawn
itself. The outcome is still reported as data — `ran`, `returncode`, `stdout`,
`stderr` — and a non-zero `returncode` makes `initialize_memory()` return
`ok: False` (mcp/src/agents_remember/kernel/memory_init.py:289-300) rather than raise.

**The branch is now chosen, not assumed.** The current path initializes a new external-memory
repository with `git init -b <initial_branch>` and records the exact local authority
`agents-remember.defaultBranch=<initial_branch>` (`DEFAULT_BRANCH_CONFIG_KEY`,
mcp/src/agents_remember/kernel/memory_init.py:13-13). `_resolved_initial_branch`
(mcp/src/agents_remember/kernel/memory_init.py:70-80) answers in two ways: an explicit
`initial_branch` argument, normalized by `_normalize_initial_branch`
(mcp/src/agents_remember/kernel/memory_init.py:37-51) — which accepts a `refs/heads/`-prefixed spelling
and refuses anything that is not one plain local branch name — or, when omitted, the **code
repository's currently checked-out branch** read by `_code_repository_branch`
(mcp/src/agents_remember/kernel/memory_init.py:54-67), which answers `None` for a detached checkout, a
missing path, or a path that is not a Git checkout. When neither source answers, the call **refuses
rather than inventing `main`**, with a message naming both ways to supply the branch
(mcp/src/agents_remember/kernel/memory_init.py:169-179). The payload always carries both
`initialBranch` and `initialBranchSource` (`explicit`, `code-repository-current-branch`, or
`unresolved`). An existing committed repository is a no-op. An existing unborn repository is
repairable when symbolic `HEAD` is on the expected branch or can be repointed to it and no local
branch exists, through `_repair_unborn_memory_repository`
(mcp/src/agents_remember/kernel/memory_init.py:124-158); any other unborn state, or a repository that
already carries refs, refuses with `_existing_unborn_refusal` naming the expected
`refs/heads/<branch>` (mcp/src/agents_remember/kernel/memory_init.py:110-121) instead of guessing.
Results expose `repairAttempted` when that bounded retry path is entered.

A missing coordination root is refused before any Git work
(mcp/src/agents_remember/kernel/memory_init.py:246-252): Git would happily create the missing parents,
so an absent coordination root would silently produce a memory repository under a path nothing else in
the product reads. The refusal names `runtime_install` and the `c-13-install-and-onboard` skill.

**A new memory repository is created in the text format (MIK-R24 rule 9).** Beside the seed files,
`initialize_memory` writes the layout marker `knowledge/layout.json`, whose bytes are
`LAYOUT_MARKER_TEXT`, the canonical formatting of `{"schema": "ar-memory-layout/v2", "conversion": "1"}`
(mcp/src/agents_remember/kernel/memory_init.py:19-21). The spelling lives here because the kernel ranks
below the models, and a test pins it to the formatter's output. The marker is written **only for a brand-new
root**, and the payload's `layoutMarker` says which case applied:

- `present`: the marker already exists and is left alone;
- `unconverted-existing-memory`: the root already holds `knowledge.sqlite` or any onboarding `*.md`
  (`_holds_legacy_memory`, mcp/src/agents_remember/kernel/memory_init.py:24-34). Writing the marker beside
  legacy cards would make the old format be read as the new one, so such a root converts through the
  conversion command or a crossing sync, never by being marked;
- `existing-repository-unchanged`: the root already has `.git`. An existing repository is repaired, never
  re-founded;
- `created`: a fresh root; the `knowledge/` directory and the marker join the planned scaffold
  (mcp/src/agents_remember/kernel/memory_init.py:268-280).

Since L37 (the L24 nit) the early return when Git initialization fails carries `layoutMarker` too: `not-created`
when this run would have created the marker (nothing was written), and the case's own value otherwise.

### Invariants And Boundaries

- **Only a new root is ever marked.** An existing repository, or a root holding legacy cards or a database, is never given `knowledge/layout.json` by this initializer.
- The memory root comes from the trusted MCP config, not a tool argument.
- Unknown repo ids are rejected before filesystem work starts.
- `dry_run` defaults to `False` (act-by-default): a plain call creates the
  scaffold; `dry_run=true` reports directories, files, and Git initialization
  without mutating.
- Git initialization or repair is validated after creating at most the requested memory-root
  directory and before creating any Agents Remember child directory or seed file. Refusing an
  unrelated unborn repository therefore preserves its existing non-Git paths and bytes.
- **The initial branch is data, never a constant.** `main` is not assumed anywhere on this path: the
  branch comes from the explicit argument or the code repository's checked-out branch, is recorded
  verbatim, and the call refuses rather than defaulting when neither source has an answer.
- The memory-init local default authority is scoped to freshly initialized or exactly provable
  unborn external-memory repositories. It is not a fallback for code repositories or ambiguous
  existing repositories.
- The `agents-remember.defaultBranch` value this module records is the authority two later seams
  read: `memory._baseline_default_branch` (first-baseline adoption) and
  `memory_repository_default_branch` (branch mutation). Neither compares the recorded name to a
  literal; both validate it against the refs that exist.
- `git init` must go through `run_git`, because `run_git` strips the
  `GIT_DIR`-family selectors. `git init` honours an inherited `GIT_DIR` over its
  `cwd`, so the direct spawn this file used to do could initialise a repository
  somewhere else entirely and still report `returncode == 0` for a memory root
  that never became a repo — a success record for work that did not happen where
  it was asked.
- The call is now bounded by the runner's default `GIT_LOCAL_TIMEOUT_SECONDS`
  (300s) where the direct spawn passed no `timeout` at all. On a stall
  `subprocess.TimeoutExpired` propagates out of `initialize_memory()`: this
  module catches nothing, so the tool call fails loudly rather than hanging.

## Evidence

### Repo-Internal References

- `memory_init` is wired through the Phase 04 application entry point. [1]
- A new memory repository is created with the layout marker; an existing or legacy root is never marked. [2]
- The marker case: only a new root is created in the text format. [3]
- MCP config defines repository memory roots. [4]
- The branch resolution this file performs: explicit argument, code-repository branch, or a refusal. [5]
- The bounded unborn-repository repair path and its refusal. [6]
- The recorded authority's consumers: first-baseline adoption and branch mutation. [7]
- The branches case set that holds this behavior end to end. [8]
- The one git runner this module's `git init` goes through: `git_environment` scrubs `GIT_REPOSITORY_SELECTOR_ENV` (L56-L72), `GIT_LOCAL_TIMEOUT_SECONDS = 300` is the default bound (L93-L93), and `run_git` applies both (L150-L215). [9]

- The failed-Git early return reports the marker as not created. [10]
