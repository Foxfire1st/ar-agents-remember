# test_worktree_sync.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_worktree_sync.py`          |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T09:56+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`                         |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `../overview.md`                              |

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
| The sync module under test. | [sync.py](agents-remember/mcp/src/agents_remember/worktrees/modules/sync.py) |
| Contract `sync_log` round-trip relies on the contract serializer. | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |

## Update History

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator, code-quality hardening sweep.
  No content impact: `SyncFixture` now builds its contract through
  `default_contract(ContractTask(...), leaf=LeafIdentity(...), code=RepoBranchPlan(...),
  memory=RepoBranchPlan(...))` instead of the flat keyword list, and everything else is
  `ruff format` reflow of the two `git worktree add` argument lists, two `assertEqual` calls,
  and the `subprocess.run` inside `git()`. This card names no `default_contract` keyword, and
  the same repo paths, source/work branches, and base commits are still paired, so the eight
  documented sync cases and their assertions are unaffected.
- 2026-06-10T09:56+02:00: Created with issue #54 sub-task D (8 tests over live-worktree fixtures).
