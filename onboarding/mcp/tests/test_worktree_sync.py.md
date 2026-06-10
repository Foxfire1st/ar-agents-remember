# test_worktree_sync.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_worktree_sync.py`          |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T09:56+02:00                     |
| lastVerifiedCommitHash | `f62c732df2acc30ec3766f83c176a24b39c0bc46`                         |
| lastVerifiedCommitDate | 2026-06-10T10:41:09+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Covers `worktree_sync` (issue #54): pulling the moved official line into live
code/memory worktrees and advancing the contract base pair.

## Code Commentary

### Logic

`SyncFixture` builds real code and ledgered memory repos with actual
`git worktree add` work branches plus a written contract; `move_official_code`
and `map_official_memory` move the official lines (the latter lands an
onboarding change and a ledger row mapping the new code tip). Tests prove: the
pure pre-closeout fast-forward advances both worktrees, the contract base
pair, and appends a `sync_log` entry; an unmapped new code tip blocks as
mid-cycle; a matching pair is a no-op; dry-run previews without mutating; a
conflicting code merge blocks, aborts, and leaves the work branch at its
pre-merge HEAD; local memory commits + moved official memory block with
`needs-review` requiring `memory_sync_choice`; `skip-memory` advances the code
base only; `merge-memory` merges disjoint memory and advances both.

### Invariants And Boundaries

Real git subprocess fixtures; exercises `sync_result` via `WorktreeArgs`
directly (the controller/payload layers are covered by the conformance suite's
representative `worktree_sync` payload).

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The sync module under test. | [sync.py](agents-remember-md/mcp/src/agents_remember/worktrees/modules/sync.py) |
| Contract `sync_log` round-trip relies on the contract serializer. | [worktree_contract.py](agents-remember-md/mcp/src/agents_remember/worktrees/worktree_contract.py) |

## Update History

- 2026-06-10T09:56+02:00: Created with issue #54 sub-task D (8 tests over live-worktree fixtures).
