# mcp/src/agents_remember/worktrees/modules/integrate.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/integrate.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-05T19:55+02:00 |
| lastVerifiedCommitHash | `e358c4ac520d94ae2e597ae3cbe186e07a4d1063` |
| lastVerifiedCommitDate | 2026-07-07T05:26:14+02:00|
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

As of cycle 6 the master-exit seam consumer is re-addressed by MASTER identity: the pure `handover_gate_guard` helper folds EVERY gate log (`GateStore.all_current()` — the raiser's lifecycle differs from the integrating contract's) and selects `master-handover-approval` gates whose `enclosure` matches the contract's `task_name` or `parent_task_name`; the latest matching gate must be policy-valid-approved under the CONFIGURED policy (`args.gate_policy`, now threaded from the controller) or the non-dry run returns handover-gate-blocked. Gateless — no gate addressed to this master — stays additive. Cycle 7 makes the exact-string address and the preview honest (AR4-1b/AR4-2): the pure sibling `unmatched_handover_gate_warning` reports, when NO gate addresses this contract but open `master-handover-approval` gates exist in the fold, a `handover_gate_warning` payload field (`unmatched_open_gates` + a verify-the-enclosure-spelling note) on the dry-run and integrated results, so a typo'd enclosure is loud instead of silently gateless; and the guard is now EVALUATED on the dry-run path too — enforced only on the real run — with the preview carrying `handover_gate` (`permitted`/`gateId`/`reason`) and a summary naming `handover-gate-blocked` when the real run would refuse, while the dry-run path persists no contract mutation.

## Update History

- 2026-07-05T19:55+02:00 - L8 builder cycle 7: added pure `unmatched_handover_gate_warning` (the enclosure spelling-check on gateless integrates, AR4-1b) and the dry-run now evaluates-but-does-not-enforce the seam guard, carrying `handover_gate` + the warning in the preview with no contract mutation (AR4-2). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T19:10+02:00 - L8 builder cycle 6: extracted `handover_gate_guard` (pure, testable) — cross-lifecycle fold + enclosure addressing replaces the inert `contract.lifecycle_id` lookup (AR3-1(b)). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): master-handover-approval enforcement consumer added at the integrate edge. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-05-31T12:30+02:00 — Documented all-or-nothing merge: pre-validate both fast-forwards and roll both branches back on memory-side failure (1.0.0 review remediation).
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
