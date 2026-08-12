# mcp/src/agents_remember/kernel/memory_init.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/memory_init.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00|
| lastVerifiedCommitHash | `c9ae4dbd8adb650f116b9d4f86343b496c3e5f32` |
| lastVerifiedCommitDate | 2026-08-12T17:53:40+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`memory_init.py` provides the package-owned `c-00-initialize-memory-repo` skill memory scaffold behavior used
by the `memory_init` MCP tool.

## Code Commentary

### Logic

`initialize_memory()` resolves the repo through `McpRuntimeConfig`, plans or
creates the external memory root, standard `system/`, `onboarding/`, and `docs/`
folders, seed system files, and an optional Git repository initialization.

cit:([`_git_init_result`], mcp/src/agents_remember/kernel/memory_init.py:35-56) runs that initialization through the package's one
git runner: cit:(["run_git(memory_root, [\"init\"])"], mcp/src/agents_remember/kernel/memory_init.py:49-49), replacing the local
`subprocess.run(["git", "init"], cwd=memory_root, ...)` this file used to spawn
itself. The outcome is still reported as data — `ran`, `returncode`, `stdout`,
`stderr` — and a non-zero `returncode` makes `initialize_memory()` return
`ok: False` cit:([`initialize_memory`], mcp/src/agents_remember/kernel/memory_init.py:59-109) rather than raise.

### Invariants And Boundaries

- The memory root comes from the trusted MCP config, not a tool argument.
- Unknown repo ids are rejected before filesystem work starts.
- `dry_run` defaults to `False` (act-by-default): a plain call creates the
  scaffold; `dry_run=true` reports directories, files, and Git initialization
  without mutating.
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
| `memory_init` is wired through the Phase 04 application entry point. | `memory_init` | mcp/src/agents_remember/mcp/registration/memory.py:123-137 |
| MCP config defines repository memory roots. | `McpRuntimeConfig` | mcp/src/agents_remember/kernel/primitives/runtime_config.py:113-137 |
| The one git runner this module's `git init` goes through: `run_git` scrubs `GIT_REPOSITORY_SELECTOR_ENV` (L24-L33) via `git_environment` and bounds the command at `GIT_LOCAL_TIMEOUT_SECONDS = 300` by default (L53-L55; L67-L96). | `run_git`, `git_environment`, `GIT_LOCAL_TIMEOUT_SECONDS` | mcp/src/agents_remember/kernel/git_command.py:70-70; mcp/src/agents_remember/kernel/git_command.py:76-82; mcp/src/agents_remember/kernel/git_command.py:85-151 |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-02T16:45:41+02:00 — 260731-EFA-L6 curator W1-B10: repaired 5 citation findings; scoped recheck clean.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T20:53+02:00 — 260731-EFA-L3 curator: body updated. The card described "an optional Git
  repository initialization" without saying how it was spawned, which is now the load-bearing fact:
  `_git_init_result` was one of the six drifted private git spawns and its
  `subprocess.run(["git", "init"], cwd=memory_root, ...)` — no `env=`, no `timeout` — was replaced
  by cit:(["run_git(memory_root, [\"init\"])"], mcp/src/agents_remember/kernel/memory_init.py:49-49). Documented the two consequences as invariants: the
  selectors are stripped, so an inherited `GIT_DIR` can no longer make `git init` build the
  repository elsewhere and still return 0; and the call is bounded at the runner's 300s default
  where it was previously unbounded, with `TimeoutExpired` propagating because this module catches
  nothing. Added the `git_command.py` repo-internal reference, anchored at L24-L33
  (`GIT_REPOSITORY_SELECTOR_ENV`), L53-L55 (the timeout classes), and L67-L96 (`run_git`). No
  citation repairs were needed: this card carried no line ranges before today.

- 2026-05-29T18:35+02:00: Extracted `_create_missing_dirs`, `_create_missing_files`, and `_git_init_result` from `initialize_memory` to reduce complexity; behavior-preserving (commit `e3dab63`).
- 2026-05-23T13:09+02:00: Created for MCP-owned memory initialization.
