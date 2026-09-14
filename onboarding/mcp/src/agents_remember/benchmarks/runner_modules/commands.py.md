# mcp/src/agents_remember/benchmarks/runner_modules/commands.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/benchmarks/runner_modules/commands.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-14T17:20+02:00 |
| lastVerifiedCommitHash | `270704b86116728a64ada83ee258a0e7726206b4` |
| lastVerifiedCommitDate | 2026-09-14T18:18:08+02:00|
| governingOverview      | `overview.md`                              |

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

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The public benchmark facade re-exports this module's public functions and classes for compatibility. | `run_git_command`; `repo_has_commit` | mcp/src/agents_remember/benchmarks/runner.py:14-15 |
| The route-local overview summarizes how this module fits into the benchmark runner split. | `## Hot Path Summary` | onboarding/mcp/src/agents_remember/benchmarks/runner_modules/overview.md:20-68 |
| The one Git runner both call sites go through, and the option object that carries `work_dir` and the timeout class. | `run_git`; `GitRunnerOptions` | mcp/src/agents_remember/kernel/git_command.py:149-213; mcp/src/agents_remember/kernel/git_command.py:115-128 |
| `git_environment()` and the `GIT_REPOSITORY_SELECTOR_ENV` tuple the runner strips with. | `GIT_REPOSITORY_SELECTOR_ENV`; `git_environment` | mcp/src/agents_remember/kernel/git_command.py:55-64; mcp/src/agents_remember/kernel/git_command.py:140-146 |
| The destructive argv this module is handed: `clone`, `fetch --all --tags`, `checkout --detach`, `reset --hard`, `clean -fdx`. | `prepare_repo` | mcp/src/agents_remember/benchmarks/runner_modules/workspace.py:38-75 |

## Cross-Repo References

No configured sibling repository is required for this module.

## Update History

- 2026-09-14T17:20+02:00 — 260913-LCA-L3 (uncommitted change set on `ar/260913-lca-l3-ar`, base
  `7317108b`): both call sites now pass `GitRunnerOptions` instead of keyword arguments —
  `GitRunnerOptions(work_dir=work_dir, timeout=timeout)` for the preparation command and
  `GitRunnerOptions(timeout=GIT_METADATA_TIMEOUT_SECONDS)` for `repo_has_commit`. Behavior is
  unchanged; the timeout class each site names is unchanged. The same pass corrected the card's body,
  which still described the pre-260731-EFA-L3 module: it claimed this file does not call `run_git`
  and that both spawns pass `env=git_environment()` from their own `subprocess.run` calls. Neither is
  true — the module composes no argv, imports no `subprocess`, and goes through the one runner, which
  is what now supplies the selector scrub, `core.longpaths`, the narrowed `safe.directory`, the
  declared stdin and the timeout class. The section was rewritten as "Every Command Goes Through The
  Canonical Runner" with the consolidation recorded rather than deleted, and the invariants were
  re-pointed at the runner and at the package-wide single-runner sweep in
  `mcp/tests/test_git_command.py`. Verification metadata remains closeout-owned; no acceptance claim
  and no verification stamp advanced.

- 2026-09-06T22:41:21+00:00: Generated citation repair: `GIT_REPOSITORY_SELECTOR_ENV` repointed to mcp/src/agents_remember/kernel/git_command.py:55-64. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-07T00:25+02:00 — Removed the obsolete deleted-test coverage claim; production behavior and original verification history remain unchanged.

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
