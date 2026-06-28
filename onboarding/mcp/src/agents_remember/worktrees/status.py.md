# mcp/src/agents_remember/worktrees/status.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/status.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T19:52+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`status.py` projects an optional `c-09-git-worktree-manager` skill worktree contract into the read-only
worktree summary used by context packets.

## Code Commentary

`worktree_status_packet()` returns inactive, missing-contract, or invalid-contract
states without mutating Git. For valid contracts it delegates to
`git_worktree_manager.status_payload()` and maps the result into the compact
context-facing worktree shape. The projection no longer preserves the full
manager payload as `rawStatus`; `WorktreeSummary` owns the explicit context
fields.

## Invariants And Boundaries

- This module is read-only; it must not create, close out, integrate, or clean
  worktrees.
- Contract parsing failures should become structured packet state rather than
  escaping context packet construction.
- Context packets expose typed lifecycle and next-operation hints, not shell
  command strings or raw manager payloads.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Worktree lifecycle status and next hints are composed by the worktree manager. | [git_worktree_manager.py](agents-remember/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |
| Worktree summary model constrains the context-facing shape. | [worktree.py](agents-remember/mcp/src/agents_remember/models/worktree.py) |
| Context packet assembly consumes this read-only worktree projection. | [context_packet.py](agents-remember/mcp/src/agents_remember/controllers/context_packet.py) |

## Series-Contract Notes

Status packets mirror the leaf enclosure identity fields from `guidance.status_payload`, including `enclosurePath`, `leafId`, and `kind`.

## Update History

- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: status packets now include `enclosurePath`, `leafId`, and `kind`, and missing/invalid contract states mirror the explicit enclosure path in their payloads. Verification metadata pinned until closeout stamps the code commit.
- 2026-05-28T19:52+02:00: Updated after context worktree status moved to explicit `WorktreeSummary` fields without raw-status passthrough.
- 2026-05-24T05:03+02:00: Created onboarding after context-packet worktree status projection adopted typed MCP next hints.
