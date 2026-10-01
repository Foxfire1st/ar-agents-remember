# mcp/src/agents_remember/benchmarks/runner_modules/commands.py

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

Small subprocess and Git command primitives used by benchmark workspace preparation. The module owns
dry-run command printing and failure reporting; the command execution itself belongs to the package's
one Git runner.

## Code Commentary

### Logic

`commands.py` owns dry-run command printing, Git command execution and cached-commit detection.
`run_git_command` prints the command and the directory it would run in when `dry_run` is set, and
otherwise runs it and raises with the last 2000 characters of git's own output on a non-zero exit:
preparation is a batch step, so a failed `clone` has to stop it rather than leave a half-made
workspace for the next case to be measured in. `repo_has_commit` answers whether a repository
already holds a commit.

### Every Command Goes Through The Canonical Runner

Neither function spawns anything. Both call `kernel.git_command.run_git`
cit:([`run_git`], mcp/src/agents_remember/kernel/git_command.py:149-213), which is what supplies the
repository-selector scrub, `core.longpaths=true`, the narrowed `safe.directory`, the declared stdin
and the timeout class. This module composes no argv of its own and imports no `subprocess`.

The two call sites differ only in what they tell the command:

- `run_git_command` cit:([`run_git_command`], mcp/src/agents_remember/benchmarks/runner_modules/commands.py:22-47) passes
  `GitRunnerOptions(work_dir=work_dir, timeout=timeout)`.
  cit:([`GitRunnerOptions`], mcp/src/agents_remember/kernel/git_command.py:115-128) `work_dir` separates *where git runs* from
  *which repository the command is about*: `git clone <url> <dest>` cannot run inside `<dest>`,
  because `<dest>` is what it is about to create.
- `repo_has_commit` cit:([`repo_has_commit`], mcp/src/agents_remember/benchmarks/runner_modules/commands.py:50-57) passes
  `GitRunnerOptions(timeout=GIT_METADATA_TIMEOUT_SECONDS)`, because `cat-file -e` is a
  constant-time metadata read.

**This card previously described a module that composed its own argv and stripped the environment
itself, and that is no longer what the source does.** Before 260731-EFA-L3 both calls were
`subprocess.run` invocations passing `env=git_environment()` and an argv built with
`-c core.longpaths=true -c safe.directory=*`. The consolidation onto the single runner removed the
local spawn, the local argv builder and the local environment plumbing, and it narrowed
`safe.directory` from the `*` wildcard to the one repository the command is about. The reason the
strip mattered is unchanged and worth keeping: `workspace.py` drives `clone`, `fetch --all --tags`,
`checkout --detach`, `reset --hard` and `clean -fdx` against a scratch benchmark workspace — the most
destructive command lines in the package — so with `GIT_DIR` or `GIT_WORK_TREE` inherited, a
`reset --hard` aimed at the scratch clone runs against whatever those name, and the uncommitted work
in *that* repository is what it destroys.

### Invariants And Boundaries

- This is not a generic shell surface; callers pass explicit command lists and this module is not a
  general process runner.
- Children must never inherit the process stdio: under the stdio MCP transport those descriptors are
  the JSON-RPC protocol pipes. `run_git` is what guarantees it — output is captured and stdin is
  `DEVNULL` unless a caller passes `input_text`.
- Children must never inherit a Git repository selector either. The scrub lives in `run_git`, so a
  future spawn added here that bypasses the runner is what re-arms the redirected-`reset --hard`
  failure — and the package-wide AST sweep in `mcp/tests/test_git_command.py` is what refuses a
  second runner at all.
- The two functions are re-exported by the `benchmarks/runner.py` compatibility facade, so
  repository preparation can monkeypatch them through it.
- Timeouts are named per command rather than left to the runner's local default: the preparation
  commands take the local class, and `repo_has_commit` takes the metadata class.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- The public benchmark facade re-exports this module's public functions and classes for compatibility. [1]
- The route-local overview summarizes how this module fits into the benchmark runner split. [2]
- The one Git runner both call sites go through, and the option object that carries `work_dir` and the timeout class. [3]
- `git_environment()` and the `GIT_REPOSITORY_SELECTOR_ENV` tuple the runner strips with. [4]
- The destructive argv this module is handed: `clone`, `fetch --all --tags`, `checkout --detach`, `reset --hard`, `clean -fdx`. [5]

### Cross-Repo References

No configured sibling repository is required for this module.
