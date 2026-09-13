# mcp/tests/test_post_integration_cleanup_guidance.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_post_integration_cleanup_guidance.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-12T19:50+02:00 |
| lastVerifiedCommitHash | `9c8a7a42a3d761b13c462874c7b312313a11c0ae` |
| lastVerifiedCommitDate | 2026-09-13T19:56:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Pins the published projection for the two states that follow a landing: a landed contract whose task
edge has not been finalized yet routes to **finalization**, and a **checkpointed** series is still
working. Integration used to end by asking the developer whether to remove the worktrees; the
automatic procedure that replaced that prompt then grew its own retry vocabulary, and
260831-LOCR-L31 removed both halves of that shape — the retry `worktree_cleanup` move with the
`cleanup-pending` branch that emitted it, and the `retry_cleanup` member with it.

Since 260831-LOCR-L30 it also pins the checkpoint projection: a checkpointed contract must not read
as closeout-done-and-awaiting-integration, because the tool that state points at refuses while the
series is open.

## Code Commentary

### Logic

`_integrated_contract(root)` cit:([`_integrated_contract`], mcp/tests/test_post_integration_cleanup_guidance.py:23-45)
builds the minimal contract each case needs: a leaf in `closeout_status="completed"`,
`integration_status="completed"`, `cleanup="pending"` with `memory_mode="internal"` (so no ledger is
read). Every case derives its variant with `dataclasses.replace`, which keeps each case about one
cell.

Three cases:

- `test_a_pending_cleanup_offers_finalization_and_never_a_cleanup_decision` cit:(["test_a_pending_cleanup_offers_finalization_and_never_a_cleanup_decision"], mcp/tests/test_post_integration_cleanup_guidance.py:48-48)
  — the landed-but-unfinalized contract projects `cleanup-pending`, `finalize`,
  `lifecycle_finalize_task` with the contract's own args **and**
  `nextRequiredArgs == ["contract_path"]`. Both halves of the old case changed: the operation and tool
  are the terminal ones, and the required-argument assertion is new because
  `lifecycle_finalize_task` is addressed by contract — a projection that named the tool without its
  one argument would tell an operator to call something they cannot address. The summary assertions
  moved with it (`"finalizing the task edge"`, `"reclaims the code and memory worktrees"`), and
  `"worktree_cleanup"` is asserted **absent** from the summary. The "never a cleanup decision" half of
  the name is still carried by the second case.
- `test_the_cleanup_decision_is_no_longer_in_the_next_operation_vocabulary` cit:(["test_the_cleanup_decision_is_no_longer_in_the_next_operation_vocabulary"], mcp/tests/test_post_integration_cleanup_guidance.py:67-67)
  — the assertion inverted this leaf: `retry_cleanup` is **not** a `NextOperation` member, `finalize`
  is, and `request_cleanup_decision` still is not. Removal rather than addition is the point: the
  member had exactly one writer, the branch the first case now covers, so it was deleted instead of
  parked beside `finalize`.
- `test_a_checkpointed_series_keeps_working_instead_of_being_told_to_integrate` cit:(["test_a_checkpointed_series_keeps_working_instead_of_being_told_to_integrate"], mcp/tests/test_post_integration_cleanup_guidance.py:83-83)
  — 260831-LOCR-L30: the same contract with `integration_status="checkpointed"` projects phase
  `worktree-started`, `continue_work`, `worktree_status` with the contract's args, and a summary
  containing `checkpointed` and "cleanup is deliberately not pending". Before the branch existed the
  phase fell through to `integration-pending` and `worktree_integrate`, the tool that refuses while
  the series is open.

### Conventions

Plain module-level `pytest` functions rather than a `unittest` class, matching the file's original
shape. Everything is hermetic: the contract is constructed in `tmp_path`, no repository is created,
and no worktree service is bound, so the module runs in the ordinary unit population.

### Invariants And Boundaries

- **The projection is asserted by phase, operation, tool, args and required args**, not by summary
  text alone; the summary assertions are additive (the words a reader needs) rather than the
  contract. `nextRequiredArgs` joined the set in 260831-LOCR-L31 because `lifecycle_finalize_task`
  takes one contract argument, and a projection that names a tool without it is a dead end rather
  than a next move.
- **One cell per case.** Each variant is a single `replace`, so a failure names the cell that changed
  the behaviour rather than a fixture that drifted.
- **The checkpoint case pins the fallthrough's absence.** Its assertions are exactly the ones that
  failed before the `checkpointed` branch existed, so it is non-vacuous by construction.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this memory repo, and these assertions
concern this repository's own guidance projection, so the retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The projection under test, including the finalization branch the first case pins and the checkpointed branch the third pins. | `_post_integration_phase` | mcp/src/agents_remember/worktrees/modules/guidance.py:255-331 |
| The checkpointed branch itself. | "if contract.integration_status == \"checkpointed\":" | mcp/src/agents_remember/worktrees/modules/guidance.py:308-308 |
| The vocabulary member the second case now proves removed, and the one that replaced it (declared on the wire model, imported by guidance). | `NextOperation`; `NextTool` | mcp/src/agents_remember/models/worktree.py:50-58; mcp/src/agents_remember/models/worktree.py:59-66 |
| The finalization route the first case pins, and the required contract argument the phase must carry with it. | `_post_integration_phase`; "tool=\"lifecycle_finalize_task\"" | mcp/src/agents_remember/worktrees/modules/guidance.py:255-331; mcp/src/agents_remember/worktrees/modules/guidance.py:301-305 |
| The terminal operation that now owns reclamation, so the projected move is not a cleanup retry. | `lifecycle_finalize_task_tool` | mcp/src/agents_remember/application/worktree_tools.py:862-893 |

## Cross-Repo References

These are in-process assertions over a constructed contract; no sibling repository or external system
participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Update History
- 2026-09-13T17:20:55+00:00: Generated citation repair: `lifecycle_finalize_task_tool` repointed to mcp/src/agents_remember/application/worktree_tools.py:862-893. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T19:50+02:00 — 260831-LOCR-L31: the first case was renamed with its subject —
  `test_a_pending_cleanup_offers_a_retry_and_never_a_cleanup_decision` →
  `test_a_pending_cleanup_offers_finalization_and_never_a_cleanup_decision` — because the
  `cleanup-pending` phase now routes `finalize` / `lifecycle_finalize_task` with
  `nextRequiredArgs == ["contract_path"]` instead of a `retry_cleanup` / `worktree_cleanup` move;
  recorded the new assertion set (including that `"worktree_cleanup"` is absent from the summary) and
  the **inverted** second case (`retry_cleanup not in NextOperation`, `finalize in`), which is a
  removal rather than an addition because the branch the first case covers was that member's only
  writer. Added `nextRequiredArgs` to the asserted-projection invariant and re-pointed the guidance
  and model reference ranges after this leaf's line movement. Verification metadata remains
  closeout-owned; no acceptance claim.
- 2026-09-12T04:10+02:00 — Created by the 260831-LOCR-L30 follow-up curator pass. Documents the
  three cases, the one-cell-per-case fixture convention, and the checkpoint projection the new case
  pins (which is the exact set of assertions that failed before the `checkpointed` branch existed).
  Verification metadata is pinned to the leaf base commit and remains closeout-owned.

- 2026-09-12T01:26:36+00:00: Generated citation repair: `_post_integration_phase`; `retry_cleanup` repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:255-329; mcp/src/agents_remember/worktrees/modules/guidance.py:302-302. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b5cbe38ab438de766feb0fc3860228f5125b623ebbee641f90211d51326d68e; claim bytes unchanged; generated by ccr-r10@v1.