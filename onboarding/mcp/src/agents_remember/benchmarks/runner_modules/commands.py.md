# mcp/src/agents_remember/benchmarks/runner_modules/commands.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/benchmarks/runner_modules/commands.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T05:30+02:00     |
| lastVerifiedCommitHash | `592274a52cec61d97521771c630272c72240ed01` |
| lastVerifiedCommitDate | 2026-06-10T01:38:42+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

Small subprocess and Git command primitives used by benchmark workspace preparation.

## Code Commentary

### Logic

`commands.py` owns dry-run command printing, subprocess execution, Git command construction with long-path/safe-directory flags, and cached-commit detection. `run_command` detaches stdin and captures stdout/stderr (raising with a 2000-char failure tail on nonzero exit) instead of inheriting the process stdio; `repo_has_commit` detaches stdin likewise.

### Invariants And Boundaries

- This is not a generic shell surface; callers pass explicit command lists.
- Children must never inherit the process stdio: under the stdio MCP transport those descriptors are the JSON-RPC protocol pipes — inherited stdout would write child output straight into the response stream (GitHub #49 bug class; fenced by `test_subprocess_hygiene.py`).
- Repository preparation can monkeypatch these helpers through the facade compatibility wrapper.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The public benchmark facade re-exports this module's public functions and classes for compatibility. | [runner.py](agents-remember-md/mcp/src/agents_remember/benchmarks/runner.py) |
| The route-local overview summarizes how this module fits into the benchmark runner split. | [runner_modules overview](agents-remember-md/mcp/src/agents_remember/benchmarks/runner_modules/overview.md) |
| Benchmark behavior is covered through the existing worktree/tool test slices. | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |

## Cross-Repo References

No configured sibling repository is required for this module.

## Update History

- 2026-06-10T05:30+02:00 — `run_command` no longer inherits the process stdio (it inherited stdin AND stdout — under the stdio MCP transport child output would write into the JSON-RPC stream): output is captured, failures raise with a 2000-char tail; `repo_has_commit` detaches stdin.
- 2026-05-26T02:26+02:00: Created when `benchmarks/runner.py` was split into focused implementation modules.
