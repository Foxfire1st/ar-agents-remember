# test_worktree_stale_base.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_worktree_stale_base.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`                         |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
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
| The preflight and template under test. | "def _stale_base_preflight("; "def prepare_memory_for_start(" | mcp/src/agents_remember/worktrees/modules/start.py:381-422; mcp/src/agents_remember/worktrees/modules/startup/start_memory.py:39-64 |
| Freshness states come from the shared kernel (unit-tested separately). | `GitFreshnessTests` | mcp/tests/test_git_freshness.py:20-104 |

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces stale-base preflight and external-memory source-branch templating during worktree start.

### Current Invariants

- Stale code or memory bases block start with exact synchronization guidance.
- Memory source-branch creation is explicit configured behavior, not an inferred fallback.

## Update History

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-17T12:30+02:00 — No content impact: L5 coverage-pragma alignment only; the documented stale-base behavior is unchanged.

- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.

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