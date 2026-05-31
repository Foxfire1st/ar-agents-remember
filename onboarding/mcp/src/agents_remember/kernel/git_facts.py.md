# mcp/src/agents_remember/kernel/git_facts.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/kernel/git_facts.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:45+02:00|
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f`                         |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`git_facts.py` reads read-only Git facts for context-packet assembly: the repo's
branch, HEAD commit, dirty flag, and an availability state. It never mutates the
repository and degrades gracefully — any git or filesystem problem becomes a
`GitFacts` with `state="unavailable"` and an `error` string rather than an
exception escaping to the caller.

## Code Commentary

### Logic

`read_git_facts(repo_id, repo_root)` resolves the path and delegates to
`_read_git_facts`, catching `OSError`/`SubprocessError` into an `unavailable`
`GitFacts`. `_read_git_facts` short-circuits to `unavailable` when the path is
missing, is not a directory, or is not a git work tree; otherwise it reads HEAD
(empty HEAD -> `unavailable`), the current branch, and `status --porcelain` for
the dirty flag. `state` is `available` when a branch is present and `detached`
when HEAD has no branch. `git_facts_to_packet` projects a `GitFacts` into the
context-packet dict, adding `error` only when set. `_git_stdout` returns trimmed
stdout or `""` on non-zero exit; `_git_error` picks the most informative of
stderr/stdout/default.

### Conventions

All git calls go through the shared `run_git` runner imported from
`kernel/git_command.py` (F14) — this module no longer defines its own private
`_run_git`. Callers read `returncode`/`stdout` rather than relying on raises.

### Invariants And Boundaries

- Read-only: this module never writes to the repository.
- Failure is data, not an exception: every error path returns a `GitFacts` with
  `state="unavailable"` and an `error` message.
- The git invocation flags, `safe.directory` isolation, and the 5-second timeout
  live in the shared `run_git` runner, not here. This module owns fact decoding
  only.
- `state` is exactly one of `available`, `detached`, or `unavailable`.

## Docs References

No external documentation is needed for this standard-library git-facts reader.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed for git-facts assembly. | n/a | n/a |

## Repo-Internal References

The shared git runner and the context-packet consumer are the direct evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Git invocations are delegated to the shared `run_git` runner rather than a private wrapper. | imports `run_git` | [git_command.py](agents-remember-md/mcp/src/agents_remember/kernel/git_command.py) |
| `git_facts_to_packet` output feeds the context packet's repo summary. | `read_git_facts` / `git_facts_to_packet` | [context_packet.py](agents-remember-md/mcp/src/agents_remember/controllers/context_packet.py) |

## Cross-Repo References

`read_git_facts` runs against whatever `repo_root` it is given, including sibling
code repos and external-memory repos, but its contract is local to this file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-31T12:45+02:00 — Created during the 1.0.0 review remediation; git calls now go through the shared `kernel/git_command.run_git` runner (F14) instead of a private `_run_git`. (Pre-existing onboarding gap: this file had no sidecar before.)
