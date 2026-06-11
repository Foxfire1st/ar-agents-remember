# mcp/src/agents_remember/kernel/git_freshness.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/git_freshness.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T08:39+02:00                     |
| lastVerifiedCommitHash | `f62c732df2acc30ec3766f83c176a24b39c0bc46`                         |
| lastVerifiedCommitDate | 2026-06-10T10:41:09+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`git_freshness.py` answers one lifecycle-long question for issue #54: is a
local branch current with its upstream? It is the shared freshness kernel
consumed by the `context_packet` freshness section (lifecycle-start
checkpoint) and intended for the `worktree_start` stale-base preflight and
`worktree_status`/`worktree_sync` (mid-task detection and sync) in the same
series.

## Code Commentary

### Logic

`read_branch_freshness(repo_root, branch=None, *, fetch=True, fetch_timeout=30)`
resolves the branch (default: the checked-out branch), looks up its
remote-tracking ref via `upstream_ref` (`rev-parse --abbrev-ref
<branch>@{upstream}`), optionally runs one bounded `git fetch <remote>` via
`fetch_remote`, counts `ahead/behind` with `git rev-list --left-right --count
<local>...<upstream>`, and folds the result into a frozen `BranchFreshness`
dataclass with `state` one of: `current`, `behind`, `ahead`, `diverged`,
`no-upstream`, `no-branch` (detached HEAD), `unknown` (fetch failed or counts
unresolvable — counts from the stale tracking ref are still reported when
computable), or `unavailable` (git/filesystem error). `freshness_to_packet`
projects the dataclass into the context-packet dict, adding `error` only when
set.

### Conventions

Mirrors `git_facts.py`: frozen dataclass + `*_to_packet` projector, shared
`run_git` from `kernel.git_command` for everything except the fetch (which
needs its own longer timeout than `run_git`'s fixed 5s, so it shells out
directly with the same `safe.directory` override and `stdin=DEVNULL`).

### Invariants And Boundaries

- The only repository mutation is the optional fetch of remote-tracking refs;
  the working tree and local branches are never touched.
- Errors degrade to data (`state` + `error`), never exceptions escaping to the
  caller — packet assembly must not fail because a remote is unreachable.
- `state="unknown"` (failed fetch) must never be treated as `behind` by
  callers; preflights warn on it but do not block.

### Todos

Sub-tasks B/D of the issue #54 series will consume this kernel from the
worktree modules; keep the API free of worktree-specific concepts.

## Docs References

No external Domain Documentation source is configured for this memory repo.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Shared low-level git runner (5s timeout) used for all non-fetch commands. | [git_command.py](agents-remember/mcp/src/agents_remember/kernel/git_command.py) |
| Style precedent: read-only git facts with dataclass + packet projector. | [git_facts.py](agents-remember/mcp/src/agents_remember/kernel/git_facts.py) |
| The context packet controller is the first consumer (`_freshness_packet`). | [context_packet.py](agents-remember/mcp/src/agents_remember/controllers/context_packet.py) |
| Kernel unit tests cover all states against local bare-origin fixtures. | [test_git_freshness.py](agents-remember/mcp/tests/test_git_freshness.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-06-10T08:39+02:00: Created as the issue #54 freshness kernel (upstream lookup, bounded fetch, ahead/behind counts, `BranchFreshness` states) consumed by the `context_packet` freshness section.
