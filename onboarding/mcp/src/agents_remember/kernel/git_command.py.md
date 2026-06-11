# mcp/src/agents_remember/kernel/git_command.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/git_command.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00|
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f`                         |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`git_command.py` is the shared low-level git command runner for kernel modules.
It consolidates the previously duplicated `cross_repo.run_git` and
`git_facts._run_git` helpers (F14) into a single `run_git()` entry point so the
git invocation flags, isolation, and timeout are defined in exactly one place.

## Code Commentary

### Logic

`run_git(repo_root, args)` shells out to `git` through `subprocess.run` and
returns the `CompletedProcess[str]` for the caller to inspect. It injects
`-c safe.directory=<repo_root>` before the caller's arguments, runs with
`cwd=repo_root`, captures stdout and stderr as text, detaches stdin via
`DEVNULL`, and enforces a 5-second timeout. It never raises on a non-zero git
exit (`check=False`); callers read `returncode`, `stdout`, and `stderr`
themselves.

### Conventions

`repo_root` is rendered with `as_posix()` for the `safe.directory` value so the
config string is forward-slashed and stable across platforms. The module keeps
to the standard library only and stays deliberately tiny.

### Invariants And Boundaries

- `check=False` is intentional: this runner reports git outcomes rather than
  raising, so callers must branch on `returncode` / `stderr`.
- The 5-second `timeout` is the single shared bound; a slow or hung git call
  surfaces as `subprocess.TimeoutExpired` to the caller.
- `safe.directory` is always set to `repo_root`, keeping invocations isolated
  to the target repository regardless of ambient git ownership state.
- This is the low-level runner only. It does not interpret git output, decode
  facts, or enforce repository/memory containment; those concerns belong to the
  callers (`git_facts.py`, `coordination_context/cross_repo.py`).

## Docs References

No external documentation is needed for this standard-library subprocess wrapper.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed for the shared git command runner. | n/a | n/a |

## Repo-Internal References

The two F14 consolidation consumers are the direct evidence for this shared
runner.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `git_facts.py` imports `run_git` and uses it for its git facts (e.g. work-tree and commit probes) instead of its former private `_run_git`. | imports `run_git` | [git_facts.py](agents-remember/mcp/src/agents_remember/kernel/git_facts.py) |
| `coordination_context/cross_repo.py` imports `run_git`, re-exports it in `__all__`, and uses it for branch and HEAD lookups, preserving the old `cross_repo.run_git` call site. | imports and re-exports `run_git` | [cross_repo.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context/cross_repo.py) |

## Cross-Repo References

The runner operates on whatever `repo_root` it is given, including sibling and
external-memory repositories, but the implementation contract is local to this
file and its kernel callers.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-31T12:30+02:00 — Created during the 1.0.0 review remediation.
