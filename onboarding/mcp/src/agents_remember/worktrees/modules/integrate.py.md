# mcp/src/agents_remember/worktrees/modules/integrate.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/integrate.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00 |
| lastVerifiedCommitHash | `abc7cbcc74921cdcb57a61529445f61641e919e7` |
| lastVerifiedCommitDate | 2026-07-31T21:50:08+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Owns integration of completed worktree task branches back into their source
branches.

## Code Commentary

The module validates closeout state, checks fast-forward eligibility, reports
blocked non-fast-forward cases, optionally replays code and memory content for
reviewed parallel changes, merges integrated commits, verifies the memory
ledger mapping, and updates integration fields in the contract.

**Two frozen parameter objects and one extracted phase (260731-EFA-L2):**

- **`IntegrationSources(current_code_source, current_memory_source, code_replay_required,
  memory_replay_required)`** — where each side's source branch stands when integration starts: its
  current head, and whether that head has already moved past the commit closeout landed (which is
  exactly what makes a fast-forward impossible and `--strategy replay` necessary). Head and verdict
  are read in the same breath per side and every consumer needs both.
  `IntegrationSources.replay_required` is a property (`code_replay_required or
  memory_replay_required`) — the ff-only block now reads `sources.replay_required` rather than
  re-OR-ing at the call site. `_integration_replay_requirements` returns it;
  `_blocked_non_ff_result` and `_dry_run_result` consume it.
- **`IntegratedCommits(code, memory_content, ledger)`** — the three commits one integration lands.
  Every step past the replay decision — the merge, the contract rewrite, the result payload —
  consumes all three or none, so `_merge_integrated_commits(contract, commits)` and
  `_integrated_result(contract, args, commits, *, handover_warning)` take the triple.
- **`_apply_integration(contract, args, sources, *, handover_warning)`** — the real (non-dry-run)
  path lifted out of `integrate_result`: land the code commit, then the memory commits, then merge
  both into their sources. `integrate_result` now reads as guard, replay decision, dry-run branch,
  delegate.

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

- 2026-07-31T21:00+02:00 — 260731-EFA-L3 curator: No content impact: the leaf's whole diff to
  `integrate.py` is one import line — `run_git` moved out of the `modules.git` import block to
  `agents_remember.kernel.git_command` — and this sidecar names no runner, subprocess style or
  timeout. I specifically re-checked the one claim the shared runner's new 300s bound could have
  broken, the all-or-nothing merge: `_merge_integrated_commits` still wraps the memory-side
  `merge --ff-only` and the ledger-mapping check in `except Exception`, and
  `subprocess.TimeoutExpired` is an `Exception`, so even a merge that outruns the bound still hits
  `run_git(..., ["reset", "--hard", code_head_before])` and the memory equivalent before re-raising
  — integration still cannot leave a half-integrated state. `IntegrationSources` (with
  `replay_required`), `IntegratedCommits`, `_apply_integration` and the `rebase` /
  `rebase --onto` replay call sites are untouched.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `C901`/`PLR0913` armed with no
  exemptions): added the frozen `IntegrationSources` (with its `replay_required` property) and
  `IntegratedCommits`, re-signed `_integration_replay_requirements` / `_blocked_non_ff_result` /
  `_dry_run_result` / `_merge_integrated_commits` / `_integrated_result` onto them, and lifted the
  real integration path into `_apply_integration`. The all-or-nothing merge, the replay decision
  and every payload field are unchanged. Verification metadata pinned until closeout stamps the L2
  commit.
- 2026-07-05T19:55+02:00 - L8 builder cycle 7: added pure `unmatched_handover_gate_warning` (the enclosure spelling-check on gateless integrates, AR4-1b) and the dry-run now evaluates-but-does-not-enforce the seam guard, carrying `handover_gate` + the warning in the preview with no contract mutation (AR4-2). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T19:10+02:00 - L8 builder cycle 6: extracted `handover_gate_guard` (pure, testable) — cross-lifecycle fold + enclosure addressing replaces the inert `contract.lifecycle_id` lookup (AR3-1(b)). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): master-handover-approval enforcement consumer added at the integrate edge. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-05-31T12:30+02:00 — Documented all-or-nothing merge: pre-validate both fast-forwards and roll both branches back on memory-side failure (1.0.0 review remediation).
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
