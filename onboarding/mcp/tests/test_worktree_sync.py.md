# test_worktree_sync.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_worktree_sync.py`          |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                         |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
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
directly (the application/payload layers are covered by the conformance suite's
representative `worktree_sync` payload).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The sync module under test. | `sync_result` | mcp/src/agents_remember/worktrees/modules/sync.py:36-119 |
| Contract `sync_log` round-trip relies on the contract serializer. | `sync_log` | mcp/src/agents_remember/worktrees/worktree_contract.py:279-279 |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B23 curator: rebased the `sync_log` range; exact
  non-fixing check returns zero findings.

- 2026-08-02T21:14+02:00 — W2-B03 curator: resolved 2 initial citation findings (1 anchor, 0 prose, 1 source); scoped recheck PASS (0 findings). Verification metadata unchanged.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator, code-quality hardening sweep.
  No content impact: `SyncFixture` now builds its contract through
  `default_contract(ContractTask(...), leaf=LeafIdentity(...), code=RepoBranchPlan(...),
  memory=RepoBranchPlan(...))` instead of the flat keyword list, and everything else is
  `ruff format` reflow of the two `git worktree add` argument lists, two `assertEqual` calls,
  and the `subprocess.run` inside `git()`. This card names no `default_contract` keyword, and
  the same repo paths, source/work branches, and base commits are still paired, so the eight
  documented sync cases and their assertions are unaffected.
- 2026-06-10T09:56+02:00: Created with issue #54 sub-task D (8 tests over live-worktree fixtures).
