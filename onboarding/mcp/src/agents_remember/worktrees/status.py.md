# mcp/src/agents_remember/worktrees/status.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/worktrees/status.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T05:03+02:00                     |
| lastVerifiedCommitHash | `9cdb4698da6bda9e8d28463dc65e03f1654cd8f3` |
| lastVerifiedCommitDate | 2026-05-24T05:20:03+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`status.py` projects an optional C-09 worktree contract into the read-only
worktree section used by context packets.

## Code Commentary

### Logic

`worktree_status_packet()` returns inactive/missing/invalid contract states
without mutating Git. For valid contracts it delegates to
`git_worktree_manager.status_payload()` and converts the worktree lifecycle
payload into the context packet shape.

`_packet_from_status_payload()` keeps the context packet small and stable by
lifting key lifecycle fields, dirty flags, source paths, and typed MCP next
hints while preserving the original status payload under `rawStatus`.

### Invariants And Boundaries

- This module is read-only; it must not create, close out, integrate, or clean
  worktrees.
- Contract parsing failures should become structured packet state rather than
  exceptions escaping context packet construction.
- Context packets expose typed `nextOperation`, `nextTool`, `nextArgs`, and
  `nextRequiredArgs` hints, not shell command strings.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Worktree lifecycle status and next hints are composed by the worktree manager. | [git_worktree_manager.py](agents-remember-md/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |
| Context packet assembly consumes this read-only worktree projection. | [context_packet.py](agents-remember-md/mcp/src/agents_remember/controllers/context_packet.py) |
| Worktree contract loading and validation live in the contract module. | [worktree_contract.py](agents-remember-md/mcp/src/agents_remember/worktrees/worktree_contract.py) |

## Update History

- 2026-05-24T05:03+02:00: Created onboarding after context-packet worktree status projection adopted typed MCP next hints.
