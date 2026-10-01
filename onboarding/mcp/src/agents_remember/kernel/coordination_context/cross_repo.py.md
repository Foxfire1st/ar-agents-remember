# mcp/src/agents_remember/kernel/coordination_context/cross_repo.py

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
`agents_remember.kernel.git_command` and re-exported via cit:([`__all__`], mcp/src/agents_remember/kernel/coordination_context/cross_repo.py:16-22)
alongside the two git helpers and the two resolvers.

Both git helpers name a timeout class rather than taking the runner's default:
cit:([`git_branch`], mcp/src/agents_remember/kernel/coordination_context/cross_repo.py:25-37) and cit:([`git_head_or_empty`], mcp/src/agents_remember/kernel/coordination_context/cross_repo.py:40-50) pass
`GitRunnerOptions(timeout=GIT_METADATA_TIMEOUT_SECONDS)` (30s). Context resolution runs on
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
  repository" (cit:([`code_repo_exclusion`], mcp/src/agents_remember/kernel/coordination_context/cross_repo.py:120-128)). A timeout raises `subprocess.TimeoutExpired` out of
  the runner instead, so a wedged adjacent repo surfaces as a failure rather
  than as a confident, wrong exclusion.
- `includeCode=false` is excluded because there is no code repo branch to
  validate.
- Memory inclusion degrades to code-only when the memory repo or ledger cannot
  satisfy the configured branch and ledger checks.

## Evidence

### Docs References

No external documentation is needed for the local cross-repo resolver.

No relevant external documentation is needed.

### Repo-Internal References

- `run_git` is imported from the kernel git command module rather than defined locally, and both helpers here pass `GIT_METADATA_TIMEOUT_SECONDS` from it. [1]
- Cross-repo entries are parsed from settings before this module resolves repository state. [2]
- External memory ledger parsing supplies memory compatibility facts. [3]
- Worktree support tests cover branch-gated cross-repo inclusion and legacy-string exclusion. [4]

### Cross-Repo References

No separate repository evidence is needed; the module reports adjacent repo facts at runtime.

No static cross-repo references are required.
