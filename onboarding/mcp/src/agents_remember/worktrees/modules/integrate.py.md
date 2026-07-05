# mcp/src/agents_remember/worktrees/modules/integrate.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/integrate.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-05T18:20+02:00 |
| lastVerifiedCommitHash | `e3b11ab9e2f3f89d45c6de01c21040600f2b3c7a` |
| lastVerifiedCommitDate | 2026-07-05T17:03:17+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Owns integration of completed worktree task branches back into their source
branches.

## Code Commentary

The module validates closeout state, checks fast-forward eligibility, reports
blocked non-fast-forward cases, optionally replays code and memory content for
reviewed parallel changes, merges integrated commits, verifies the memory
ledger mapping, and updates integration fields in the contract.

The merge of integrated commits is all-or-nothing: both the code and memory
fast-forwards are pre-validated as ancestors before either branch is mutated,
and if the memory-side merge or ledger-mapping check fails after the code
branch has advanced, both branches are reset hard to their pre-merge heads
before the failure re-raises, so integration never leaves a half-integrated
state.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Worktree contract fields record closeout and integration commit state. | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| Worktree tests cover fast-forward integration, replay, and conflict blocking. | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |

As of cycle 5 integrate_result enforces the master-exit seam (mirror of the closeout gate): on a non-dry run, an existing master-handover-approval gate on the contract's lifecycle must be policy-valid-approved or the integration returns handover-gate-blocked; gateless stays additive.

## Update History

- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): master-handover-approval enforcement consumer added at the integrate edge. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-05-31T12:30+02:00 — Documented all-or-nothing merge: pre-validate both fast-forwards and roll both branches back on memory-side failure (1.0.0 review remediation).
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
