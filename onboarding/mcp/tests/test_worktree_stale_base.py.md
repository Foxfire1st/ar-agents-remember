# test_worktree_stale_base.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_worktree_stale_base.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T09:30+02:00                     |
| lastVerifiedCommitHash | `f62c732df2acc30ec3766f83c176a24b39c0bc46`                         |
| lastVerifiedCommitDate | 2026-06-10T10:41:09+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Covers the issue #54 worktree_start stale-base preflight
(`_stale_base_preflight`) and the memory source branch auto-template
(`_ensure_memory_source_branch` via `prepare_memory_for_start`).

## Code Commentary

### Logic

`StaleBasePreflightTests` uses bare-origin clone pairs (same fixture shape as
`test_git_freshness.py`) so remote movement is simulated by pushing from a
second clone: no upstream → no block; behind code branch → blocked with
`choose_stale_base_recovery` and a `staleBases` finding (`side: "code"`,
behind count); `proceed-stale` overrides; `fast-forward` recovers both a
parked branch (`branch -f`) and the checked-out branch (`merge --ff-only`),
asserting the branch tip equals the remote head; diverged stays blocked with
a `recovery_error`; an unreachable remote (`unknown`) does not block; a
behind memory repo blocks with `side: "memory"`.

`MemorySourceBranchTemplateTests` proves a missing memory source branch is
created at the official tip during a real `prepare_memory_for_start` (ledger
mapping the code base required), reported as `created-from-official-tip`;
dry-run reports `would-create-from-official-tip` without creating; an
existing branch reports `existing`.

### Invariants And Boundaries

Real git subprocess fixtures, no mocking. `_stale_base_preflight` is exercised
with a `SimpleNamespace` context because it only reads
`code_repository_name` for the retry guidance args.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The preflight and template under test. | [start.py](agents-remember-md/mcp/src/agents_remember/worktrees/modules/start.py) |
| Freshness states come from the shared kernel (unit-tested separately). | [test_git_freshness.py](agents-remember-md/mcp/tests/test_git_freshness.py) |

## Update History

- 2026-06-10T09:30+02:00: Created with the issue #54 sub-task B stale-base preflight and memory-branch auto-template (11 tests).
