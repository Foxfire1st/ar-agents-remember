# mcp/src/agents_remember/kernel/memory_init.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/memory_init.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-16T02:51+02:00|
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`memory_init.py` provides the package-owned `c-00-initialize-memory-repo` skill memory scaffold behavior used
by the `memory_init` MCP tool.

## Code Commentary

### Logic

`initialize_memory` (mcp/src/agents_remember/kernel/memory_init.py:195-282) resolves the repo through
`McpRuntimeConfig`, plans or creates the external memory root, establishes its Git authority, then
creates the standard `system/`, `onboarding/`, and `docs/` folders and seed system files.

Before L4, `_git_init_result` ran that initialization through the package's one
git runner with `run_git(memory_root, ["init"])`, replacing the local
`subprocess.run(["git", "init"], cwd=memory_root, ...)` this file used to spawn
itself. The outcome is still reported as data — `ran`, `returncode`, `stdout`,
`stderr` — and a non-zero `returncode` makes `initialize_memory()` return
`ok: False` (mcp/src/agents_remember/kernel/memory_init.py:255-266) rather than raise.

**The branch is now chosen, not assumed.** The current path initializes a new external-memory
repository with `git init -b <initial_branch>` and records the exact local authority
`agents-remember.defaultBranch=<initial_branch>` (`DEFAULT_BRANCH_CONFIG_KEY`,
mcp/src/agents_remember/kernel/memory_init.py:13-13). `_resolved_initial_branch`
(mcp/src/agents_remember/kernel/memory_init.py:49-59) answers in two ways: an explicit
`initial_branch` argument, normalized by `_normalize_initial_branch`
(mcp/src/agents_remember/kernel/memory_init.py:16-30) — which accepts a `refs/heads/`-prefixed spelling
and refuses anything that is not one plain local branch name — or, when omitted, the **code
repository's currently checked-out branch** read by `_code_repository_branch`
(mcp/src/agents_remember/kernel/memory_init.py:33-46), which answers `None` for a detached checkout, a
missing path, or a path that is not a Git checkout. When neither source answers, the call **refuses
rather than inventing `main`**, with a message naming both ways to supply the branch
(mcp/src/agents_remember/kernel/memory_init.py:141-154). The payload always carries both
`initialBranch` and `initialBranchSource` (`explicit`, `code-repository-current-branch`, or
`unresolved`). An existing committed repository is a no-op. An existing unborn repository is
repairable when symbolic `HEAD` is on the expected branch or can be repointed to it and no local
branch exists, through `_repair_unborn_memory_repository`
(mcp/src/agents_remember/kernel/memory_init.py:103-137); any other unborn state, or a repository that
already carries refs, refuses with `_existing_unborn_refusal` naming the expected
`refs/heads/<branch>` (mcp/src/agents_remember/kernel/memory_init.py:89-100) instead of guessing.
Results expose `repairAttempted` when that bounded retry path is entered.

A missing coordination root is refused before any Git work
(mcp/src/agents_remember/kernel/memory_init.py:219-231): Git would happily create the missing parents,
so an absent coordination root would silently produce a memory repository under a path nothing else in
the product reads. The refusal names `runtime_install` and the `c-13-install-and-onboard` skill.

### Invariants And Boundaries

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `memory_init` is wired through the Phase 04 application entry point. | `memory_init` | mcp/src/agents_remember/mcp/registration/memory.py:182-204 |
| MCP config defines repository memory roots. | `McpRuntimeConfig` | mcp/src/agents_remember/kernel/primitives/runtime_config.py:113-137 |
| The branch resolution this file performs: explicit argument, code-repository branch, or a refusal. | `_normalize_initial_branch`; `_code_repository_branch`; `_resolved_initial_branch`; `_git_init_result` | mcp/src/agents_remember/kernel/memory_init.py:16-30; mcp/src/agents_remember/kernel/memory_init.py:33-46; mcp/src/agents_remember/kernel/memory_init.py:49-59; mcp/src/agents_remember/kernel/memory_init.py:140-192 |
| The bounded unborn-repository repair path and its refusal. | `_repair_unborn_memory_repository`; `_existing_unborn_refusal` | mcp/src/agents_remember/kernel/memory_init.py:103-137; mcp/src/agents_remember/kernel/memory_init.py:89-100 |
| The recorded authority's consumers: first-baseline adoption and branch mutation. | `_baseline_default_branch`; `memory_repository_default_branch` | mcp/src/agents_remember/memory/baseline.py:149-192; mcp/src/agents_remember/worktrees/integration/integration_branch_repository.py:51-87 |
| The branches case set that holds this behavior end to end. | `test_memory_init_mints_and_records_the_named_initial_branch`; `test_memory_init_inherits_the_code_repositorys_current_branch_by_default`; `test_memory_init_refuses_rather_than_inventing_a_branch_when_it_has_no_answer`; `test_the_unborn_repair_path_accepts_the_configured_branch_instead_of_main` | mcp/tests/test_memory_branch_authority.py:109-125; mcp/tests/test_memory_branch_authority.py:127-144; mcp/tests/test_memory_branch_authority.py:146-164; mcp/tests/test_memory_branch_authority.py:166-185 |
| The one git runner this module's `git init` goes through: `git_environment` scrubs `GIT_REPOSITORY_SELECTOR_ENV` (L56-L72), `GIT_LOCAL_TIMEOUT_SECONDS = 300` is the default bound (L93-L93), and `run_git` applies both (L150-L215). | `run_git`; `git_environment`; `GIT_LOCAL_TIMEOUT_SECONDS` | mcp/src/agents_remember/kernel/git_command.py:150-215; mcp/src/agents_remember/kernel/git_command.py:141-149; mcp/src/agents_remember/kernel/git_command.py:93-93 |

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: `memory_init` repointed to mcp/src/agents_remember/mcp/registration/memory.py:182-204. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T17:59+02:00 — 260915-CAPS-L13 curator: **body rebased on the initial-branch parameter
  this leaf added** (`CAPS-R13@v1`, the absorbed UNO-L2 runtime-correctness scope). The card's central
  claim was stale and said the opposite of the code: it described `git init -b main` with a recorded
  `agents-remember.defaultBranch=main`, and an unborn repair path "only when symbolic `HEAD` is
  exactly `refs/heads/main`". It now records the real behaviour — a branch chosen from the explicit
  argument or the code repository's checked-out branch, normalized by `_normalize_initial_branch`,
  recorded verbatim, with a refusal that names both ways to supply it when neither source answers, and
  a repair path that accepts the configured branch. Added the recorded-authority invariant and its two
  consumers, the coordination-root refusal, the payload's `initialBranchSource` values, and the new
  anchors with re-derived ranges (the stale `initialize_memory` 59-109 citation is replaced by the
  function's real 195-282 range). Verification metadata is left at the leaf base commit because the
  source is uncommitted — the governed closeout stamps the real code commit.
- 2026-08-16T02:51+02:00 — L4 integration-branch authority: documented exact external-memory
  default-branch initialization, idempotent unborn-main repair, fail-closed mismatches, and the
  pre-scaffold authority ordering that preserves unrelated repository contents on refusal.

- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-02T16:45:41+02:00 — 260731-EFA-L6 curator W1-B10: repaired 5 citation findings; scoped recheck clean.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T20:53+02:00 — 260731-EFA-L3 curator: body updated. The card described "an optional Git
  repository initialization" without saying how it was spawned, which is now the load-bearing fact:
  `_git_init_result` was one of the six drifted private git spawns and its
  `subprocess.run(["git", "init"], cwd=memory_root, ...)` — no `env=`, no `timeout` — was replaced
  by `run_git(memory_root, ["init"])`. Documented the two consequences as invariants: the
  selectors are stripped, so an inherited `GIT_DIR` can no longer make `git init` build the
  repository elsewhere and still return 0; and the call is bounded at the runner's 300s default
  where it was previously unbounded, with `TimeoutExpired` propagating because this module catches
  nothing. Added the `git_command.py` repo-internal reference, anchored at L24-L33
  (`GIT_REPOSITORY_SELECTOR_ENV`), L53-L55 (the timeout classes), and L67-L96 (`run_git`). No
  citation repairs were needed: this card carried no line ranges before today.

- 2026-05-29T18:35+02:00: Extracted `_create_missing_dirs`, `_create_missing_files`, and `_git_init_result` from `initialize_memory` to reduce complexity; behavior-preserving (commit `e3dab63`).
- 2026-05-23T13:09+02:00: Created for MCP-owned memory initialization.
