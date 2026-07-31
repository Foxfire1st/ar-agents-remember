# mcp/src/agents_remember/kernel/memory_init.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/memory_init.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T18:35+02:00|
| lastVerifiedCommitHash | `abc7cbcc74921cdcb57a61529445f61641e919e7` |
| lastVerifiedCommitDate | 2026-07-31T21:50:08+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`memory_init.py` provides the package-owned `c-00-initialize-memory-repo` skill memory scaffold behavior used
by the `memory_init` MCP tool.

## Code Commentary

### Logic

`initialize_memory()` resolves the repo through `McpRuntimeConfig`, plans or
creates the external memory root, standard `system/`, `onboarding/`, and `docs/`
folders, seed system files, and an optional Git repository initialization.

`_git_init_result()` (L35-L56) runs that initialization through the package's one
git runner: `run_git(memory_root, ["init"])` (L47), replacing the local
`subprocess.run(["git", "init"], cwd=memory_root, ...)` this file used to spawn
itself. The outcome is still reported as data — `ran`, `returncode`, `stdout`,
`stderr` — and a non-zero `returncode` makes `initialize_memory()` return
`ok: False` (L89-L98) rather than raise.

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

| Finding | Source Path |
| --- | --- |
| `memory_init` is wired through the Phase 04 controller. | [skill_tools.py](agents-remember/mcp/src/agents_remember/controllers/skill_tools.py) |
| MCP config defines repository memory roots. | [config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |
| The one git runner this module's `git init` goes through: `run_git` scrubs `GIT_REPOSITORY_SELECTOR_ENV` (L24-L33) via `git_environment` and bounds the command at `GIT_LOCAL_TIMEOUT_SECONDS = 300` by default (L53-L55; L67-L96). | [git_command.py](agents-remember/mcp/src/agents_remember/kernel/git_command.py) |

## Update History

- 2026-07-31T20:53+02:00 — 260731-EFA-L3 curator: body updated. The card described "an optional Git
  repository initialization" without saying how it was spawned, which is now the load-bearing fact:
  `_git_init_result` was one of the six drifted private git spawns and its
  `subprocess.run(["git", "init"], cwd=memory_root, ...)` — no `env=`, no `timeout` — was replaced
  by `run_git(memory_root, ["init"])` (L47). Documented the two consequences as invariants: the
  selectors are stripped, so an inherited `GIT_DIR` can no longer make `git init` build the
  repository elsewhere and still return 0; and the call is bounded at the runner's 300s default
  where it was previously unbounded, with `TimeoutExpired` propagating because this module catches
  nothing. Added the `git_command.py` repo-internal reference, anchored at L24-L33
  (`GIT_REPOSITORY_SELECTOR_ENV`), L53-L55 (the timeout classes), and L67-L96 (`run_git`). No
  citation repairs were needed: this card carried no line ranges before today.

- 2026-05-29T18:35+02:00: Extracted `_create_missing_dirs`, `_create_missing_files`, and `_git_init_result` from `initialize_memory` to reduce complexity; behavior-preserving (commit `e3dab63`).
- 2026-05-23T13:09+02:00: Created for MCP-owned memory initialization.
