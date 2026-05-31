# mcp/src/agents_remember/worktrees/modules/cleanup.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/cleanup.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Owns post-integration cleanup of registered worktrees, merged task branches,
and empty worktree folders.

## Code Commentary

`cleanup_result` takes the typed `WorktreeArgs` dataclass (imported from
`agents_remember.worktrees.modules.args`), replacing the former
`argparse.Namespace`; it reads `args.approved`, `args.dry_run`, and
`args.contract_path`, asserting the latter is non-`None` before loading the
contract. Cleanup requires completed integration and explicit approval for real
mutation. It removes registered code and memory worktrees, deletes branches only
when Git proves they are merged, removes empty directories, records cleanup
completion in the contract, and reports branches Git refused to delete.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Defines the `WorktreeArgs` dataclass that types the `cleanup_result` input. | [args.py](agents-remember-md/mcp/src/agents_remember/worktrees/modules/args.py) |
| Integration creates the scratch memory integration branch name that cleanup may remove. | [integrate.py](agents-remember-md/mcp/src/agents_remember/worktrees/modules/integrate.py) |
| Worktree tests cover cleanup preconditions and completed cleanup state. | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |

## Update History

- 2026-05-31T12:50+02:00 — `cleanup_result` arg re-typed from `argparse.Namespace` to the new `WorktreeArgs` dataclass (imported from `modules.args`) with an `args.contract_path is not None` assert; corrected Code Commentary to name the typed param and added the args.py reference (1.0.0 review remediation).
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
