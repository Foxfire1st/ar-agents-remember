# mcp/src/agents_remember/benchmarks/runner_modules/commands.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/benchmarks/runner_modules/commands.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T05:30+02:00     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

Small subprocess and Git command primitives used by benchmark workspace preparation.

## Code Commentary

### Logic

`commands.py` owns dry-run command printing, subprocess execution, Git command construction with long-path/safe-directory flags, and cached-commit detection. `run_command` detaches stdin and captures stdout/stderr (raising with a 2000-char failure tail on nonzero exit) instead of inheriting the process stdio; `repo_has_commit` detaches stdin likewise.

### Both Spawns Pass `env=git_environment()`

Neither `subprocess.run` here inherits the ambient environment. Both pass
`env=git_environment()` from `agents_remember.kernel.git_command`, which is `os.environ` minus the
`GIT_DIR`-family repository selectors (`GIT_REPOSITORY_SELECTOR_ENV`: `GIT_DIR`, `GIT_WORK_TREE`,
`GIT_INDEX_FILE`, `GIT_OBJECT_DIRECTORY`, `GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_COMMON_DIR`,
`GIT_NAMESPACE`, `GIT_PREFIX`).

This module does not call `run_git`, and that is deliberate rather than an oversight. It composes
its own argv through `git_command()` — which adds `-c core.longpaths=true -c safe.directory=*`, its
own requirements — and `run_command` is a *generic* runner: it is handed whatever argv the caller
built, git or not. So it strips the selectors on the environment side instead.

The reason is the argv it is handed. `workspace.py` drives `run_command(git_command(...))` for
`clone`, `fetch --all --tags`, `checkout --detach`, `reset --hard` and `clean -fdx` against a
scratch benchmark workspace — the most destructive command lines in the package. With `GIT_DIR` or
`GIT_WORK_TREE` inherited, a `reset --hard` aimed at the scratch clone runs against whatever those
name, and the uncommitted work in *that* repository is what it destroys. The strip is therefore
applied to every command this runner spawns rather than only to the ones whose argv happens to
start with `git` today.

### Invariants And Boundaries

- This is not a generic shell surface; callers pass explicit command lists.
- Children must never inherit the process stdio: under the stdio MCP transport those descriptors are the JSON-RPC protocol pipes — inherited stdout would write child output straight into the response stream (GitHub #49 bug class; fenced by `test_subprocess_hygiene.py`).
- Children must never inherit a git repository selector either. Both spawns pass `env=git_environment()`; adding a third spawn without it is what re-arms the redirected-`reset --hard` failure.
- This module is invisible to the package-wide AST guard in `test_git_command.py::SingleRunnerTests`, which recognises only a spawn whose argv is a list literal starting with `"git"`. `git_command()` composes the argv, so the guard cannot see these two spawns and `BenchmarkRunnerEnvironmentTests` asserts the property directly instead.
- Repository preparation can monkeypatch these helpers through the facade compatibility wrapper.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The public benchmark facade re-exports this module's public functions and classes for compatibility. | `run_git_command`; `repo_has_commit` | mcp/src/agents_remember/benchmarks/runner.py:14-15 |
| The route-local overview summarizes how this module fits into the benchmark runner split. | `## Hot Path Summary` | onboarding/mcp/src/agents_remember/benchmarks/runner_modules/overview.md:20-68 |
| Benchmark behavior is covered through the existing worktree/tool test slices. | `BenchmarkRunnerPortabilityTests` | mcp/tests/test_worktree_support_benchmark.py:32-665 |
| `git_environment()` and the `GIT_REPOSITORY_SELECTOR_ENV` tuple both spawns strip. | `GIT_REPOSITORY_SELECTOR_ENV` | mcp/src/agents_remember/kernel/git_command.py:33-42 |
| The destructive argv this runner is handed: `clone`, `fetch --all --tags`, `checkout --detach`, `reset --hard`, `clean -fdx`. | `prepare_repo` | mcp/src/agents_remember/benchmarks/runner_modules/workspace.py:38-75 |
| `BenchmarkRunnerEnvironmentTests` points `GIT_DIR` at a decoy repository, runs a real `reset --hard` through `run_command`, and asserts the decoy's uncommitted work survives; a second test does the same for `repo_has_commit`. | `BenchmarkRunnerEnvironmentTests` | mcp/tests/test_git_command.py:663-791 |

## Cross-Repo References

No configured sibling repository is required for this module.

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout: normalized the Repo-Internal References
  table to the tree-wide 3-column `Finding | Anchor | Source` format with source-backed
  citations (the citation-curation wave's format migration). No behavior claim changed.
- 2026-07-31T20:48+02:00 — 260731-EFA-L3 curator: both `subprocess.run` calls now pass
  `env=git_environment()` (from `agents_remember.kernel.git_command`) instead of inheriting the
  ambient environment, so the `GIT_DIR`-family repository selectors are stripped from every child.
  The card described stdio hygiene as the only thing this runner fenced, which was no longer the
  whole story: `workspace.py` hands it `clone`, `checkout --detach`, `reset --hard` and
  `clean -fdx`, and an inherited `GIT_DIR`/`GIT_WORK_TREE` aims those at a repository nobody chose.
  Added the "Both Spawns Pass `env=git_environment()`" section, recorded why this module keeps its
  own `git_command()` argv rather than calling `run_git`, and added the invariant plus the note
  that the package-wide AST guard cannot see these composed spawns — `BenchmarkRunnerEnvironmentTests`
  covers them directly instead. Added three reference rows. This card's reference table carries
  source paths only, so it holds no line-range citations to repair.

- 2026-06-10T05:30+02:00 — `run_command` no longer inherits the process stdio (it inherited stdin AND stdout — under the stdio MCP transport child output would write into the JSON-RPC stream): output is captured, failures raise with a 2000-char tail; `repo_has_commit` detaches stdin.
- 2026-05-26T02:26+02:00: Created when `benchmarks/runner.py` was split into focused implementation modules.
