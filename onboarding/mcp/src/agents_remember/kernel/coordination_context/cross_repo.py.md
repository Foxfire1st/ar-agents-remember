# mcp/src/agents_remember/kernel/coordination_context/cross_repo.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/cross_repo.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`cross_repo.py` resolves branch-gated adjacent repository facts for
`crossRepo.allow` settings.

## Code Commentary

### Logic

The module validates each configured allow entry, checks the adjacent code repo
branch (`git_branch`) and HEAD (`git_head_or_empty`), optionally checks the
matching external memory repo branch, and reads the memory ledger when memory
inclusion is enabled. It returns included, included-code-only, or excluded state
with concrete reasons. `run_git` is no longer defined here; it is imported from
`agents_remember.kernel.git_command` and re-exported via cit:([`__all__`], mcp/src/agents_remember/kernel/coordination_context/cross_repo.py:12-18)
alongside the two git helpers and the two resolvers.

Both git helpers name a timeout class rather than taking the runner's default:
cit:([`git_branch`], mcp/src/agents_remember/kernel/coordination_context/cross_repo.py:21-29) and cit:([`git_head_or_empty`], mcp/src/agents_remember/kernel/coordination_context/cross_repo.py:32-38) pass
`timeout=GIT_METADATA_TIMEOUT_SECONDS` (30s). Context resolution runs on
essentially every tool call and both commands are constant-time reads, so 30s
can only be reached when git is blocked on an index lock — and inheriting the
runner's `GIT_LOCAL_TIMEOUT_SECONDS` (300s) would let one wedged
`branch --show-current` hold an MCP tool call for five minutes instead of
failing it.

### Invariants And Boundaries

- Cross-repo inclusion is read-only toward adjacent repositories.
- A stalled git is not laundered into an exclusion reason. `git_branch` and
  `git_head_or_empty` return `""` only for a **non-zero return code**, and
  `code_repo_exclusion` reads an empty branch as "detached or not a git
  repository" (cit:([`code_repo_exclusion`], mcp/src/agents_remember/kernel/coordination_context/cross_repo.py:108-116)). A timeout raises `subprocess.TimeoutExpired` out of
  the runner instead, so a wedged adjacent repo surfaces as a failure rather
  than as a confident, wrong exclusion.
- `includeCode=false` is excluded because there is no code repo branch to
  validate.
- Memory inclusion degrades to code-only when the memory repo or ledger cannot
  satisfy the configured branch and ledger checks.

## Docs References

No external documentation is needed for the local cross-repo resolver.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `run_git` is imported from the kernel git command module rather than defined locally, and both helpers here pass `GIT_METADATA_TIMEOUT_SECONDS` from it. | `run_git` | mcp/src/agents_remember/kernel/git_command.py:85-151 |
| Cross-repo entries are parsed from settings before this module resolves repository state. | `parse_cross_repo_allow`; `parse_cross_repo_allow_entry` | mcp/src/agents_remember/kernel/coordination_context/setting_values.py:44-58; mcp/src/agents_remember/kernel/coordination_context/setting_values.py:61-70 |
| External memory ledger parsing supplies memory compatibility facts. | `parse_ledger_text`; `parse_ledger_rows` | mcp/src/agents_remember/kernel/memory_ledger.py:52-104; mcp/src/agents_remember/kernel/memory_ledger.py:123-132 |
| Worktree support tests cover branch-gated cross-repo inclusion and legacy-string exclusion. | `WorktreeSupportTests` | mcp/tests/test_worktree_support.py:671-746 |

## Cross-Repo References

No separate repository evidence is needed; the module reports adjacent repo facts at runtime.

| Finding | Anchor | Source |
| --- | --- | --- |
| No static cross-repo references are required. | n/a | n/a |

## Update History

- 2026-08-02T17:12:10+02:00 — W1-B04 curator: repaired 5 citation claims (4 table rows, 1 prose citation); scoped recheck clean (0 findings).

- 2026-07-31T20:55+02:00 — 260731-EFA-L3 curator: body updated. The Logic prose was true but no
  longer complete: cit:([`git_branch`], mcp/src/agents_remember/kernel/coordination_context/cross_repo.py:21-29) and cit:([`git_head_or_empty`], mcp/src/agents_remember/kernel/coordination_context/cross_repo.py:32-38) now import and pass
  cit:([`GIT_METADATA_TIMEOUT_SECONDS`], mcp/src/agents_remember/kernel/coordination_context/cross_repo.py:9-9), because the runner's default moved from a hard-coded 5s to
  `GIT_LOCAL_TIMEOUT_SECONDS = 300` and these two constant-time reads sit on the path of
  essentially every tool call. Added the reason and a boundary that only became worth stating once
  a timeout existed: the `""` return is reserved for a non-zero return code, which
  cit:([`code_repo_exclusion`], mcp/src/agents_remember/kernel/coordination_context/cross_repo.py:108-116) reports as "detached or not a git repository", whereas a stall
  raises `TimeoutExpired` and so cannot be laundered into that exclusion reason. Repaired 1
  citation into a file this leaf changed: the git-runner row's unanchored "run_git import" became
  `L53-L55` (the three timeout constants) and `L67-L96` (`run_git`'s signature and body). The other
  three rows point at `setting_values.py`, `memory_ledger.py` and `test_worktree_support.py`, none
  of which this leaf touched, so their non-numeric citations were left as they were.

- 2026-05-31T12:50+02:00 — `run_git` is now imported from `agents_remember.kernel.git_command` (local definition removed) and re-exported via a new `__all__`; `git_head` renamed to `git_head_or_empty` (now docstringed) with its `code_repository_info` call site updated; corrected Logic prose to name `git_branch`/`git_head_or_empty` and the shared `run_git`, and added the git_command repo-internal reference (1.0.0 review remediation).
- 2026-05-25T20:57+02:00: Created by extracting branch-gated cross-repo state resolution from the `c-08-ar-coordination-context-resolver` skill resolver.
