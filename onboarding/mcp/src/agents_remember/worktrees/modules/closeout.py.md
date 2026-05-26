# mcp/src/agents_remember/worktrees/modules/closeout.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/closeout.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T20:41+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Owns worktree and direct closeout preview/apply behavior.

## Code Commentary

Closeout validates source branch positions and explicit commit approval, commits
code first, refreshes onboarding metadata and entity fingerprints to that new
code commit, commits memory content, updates the external memory ledger, and
returns the closeout payload. Direct closeout applies the same ordering to the
current source branches without task worktrees.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Ledger updates use the kernel memory ledger parser and renderer. | [memory_ledger.py](agents-remember-md/mcp/src/agents_remember/kernel/memory_ledger.py) |
| Worktree tests cover dry-run previews, approval notes, missing onboarding blocking, and direct closeout ledger updates. | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |

## Update History

- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
