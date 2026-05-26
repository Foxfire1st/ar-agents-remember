# mcp/src/agents_remember/worktrees/modules/cleanup.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/cleanup.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T20:41+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Owns post-integration cleanup of registered worktrees, merged task branches,
and empty worktree folders.

## Code Commentary

Cleanup requires completed integration and explicit approval for real mutation.
It removes registered code and memory worktrees, deletes branches only when Git
proves they are merged, removes empty directories, records cleanup completion in
the contract, and reports branches Git refused to delete.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Integration creates the scratch memory integration branch name that cleanup may remove. | [integrate.py](agents-remember-md/mcp/src/agents_remember/worktrees/modules/integrate.py) |
| Worktree tests cover cleanup preconditions and completed cleanup state. | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |

## Update History

- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
