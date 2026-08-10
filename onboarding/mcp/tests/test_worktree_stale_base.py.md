# test_worktree_stale_base.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_worktree_stale_base.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T09:30+02:00                     |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                         |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `../overview.md`                              |

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

### Conventions

The shared `make_contract(root, code, *, memory=None, source_branch=None)` factory takes each
side as a local frozen `RepoSide(repo, base_commit=None)` dataclass — the repository and the
commit the contract records as that side's fork point, kept together because the preflight
compares exactly that pair per side — and expands them into
`default_contract(ContractTask(...), leaf=LeafIdentity(...), code=RepoBranchPlan(...),
memory=RepoBranchPlan(...))`. A `RepoSide` with no `base_commit` falls back to the
`PLACEHOLDER_CODE_BASE` / `PLACEHOLDER_MEMORY_BASE` constants, which are deliberately never real
commits: a case that passes a real base commit is declaring that side is the one under test.

### Invariants And Boundaries

Real git subprocess fixtures, no mocking. `_stale_base_preflight` is exercised
with a `SimpleNamespace` context because it only reads
`code_repository_name` for the retry guidance args.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The preflight and template under test. | `_stale_base_preflight`, `prepare_memory_for_start` | mcp/src/agents_remember/worktrees/modules/start.py:325-366; mcp/src/agents_remember/worktrees/modules/start.py:909-947 |
| Freshness states come from the shared kernel (unit-tested separately). | `GitFreshnessTests` | mcp/tests/test_git_freshness.py:20-104 |

## Update History

- 2026-08-03T04:32:19+02:00 — W3-B08 curator: curated 4 citations (citation_anchor_missing=2, citation_prose_not_in_cit_form=0, citation_source_malformed=2); final scoped citation check clean.
- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator, code-quality hardening sweep. The `make_contract`
  fixture was reshaped: it no longer takes `code_repo`/`memory_repo`/`code_base_commit`/
  `memory_base_commit` as four independent keywords but a new module-level frozen `RepoSide`
  dataclass per side, and it builds the contract through
  `default_contract(ContractTask(...), leaf=LeafIdentity(...), code=RepoBranchPlan(...),
  memory=RepoBranchPlan(...))`. The former `"c1"`/`"m1"` defaults became the named
  `PLACEHOLDER_CODE_BASE` / `PLACEHOLDER_MEMORY_BASE` constants. Added a Conventions section
  recording that factory, since the card previously described the fixtures only as bare-origin
  clone pairs. All eleven cases and their block/recovery assertions are unchanged.
- 2026-06-10T09:30+02:00: Created with the issue #54 sub-task B stale-base preflight and memory-branch auto-template (11 tests).
