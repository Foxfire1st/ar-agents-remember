# mcp/tests/test_post_integration_cleanup_guidance.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_post_integration_cleanup_guidance.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-12T04:10+02:00 |
| lastVerifiedCommitHash | `5410fb07d0d3a73f4d81d57ed020bbfcdaaa2267` |
| lastVerifiedCommitDate | 2026-09-12T18:45:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Pins the published projection for the two states that follow a landing: cleanup that did not finish
is a **retry**, and a **checkpointed** series is still working. Integration used to end by asking the
developer whether to remove the worktrees; once reclamation became automatic, the projection must
stop describing that decision, and the vocabulary member that carried it must go with it.

Since 260831-LOCR-L30 it also pins the checkpoint projection: a checkpointed contract must not read
as closeout-done-and-awaiting-integration, because the tool that state points at refuses while the
series is open.

## Code Commentary

### Logic

`_integrated_contract(root)` cit:([`_integrated_contract`], mcp/tests/test_post_integration_cleanup_guidance.py:20-42)
builds the minimal contract each case needs: a leaf in `closeout_status="completed"`,
`integration_status="completed"`, `cleanup="pending"` with `memory_mode="internal"` (so no ledger is
read). Every case derives its variant with `dataclasses.replace`, which keeps each case about one
cell.

Three cases:

- `test_a_pending_cleanup_offers_a_retry_and_never_a_cleanup_decision` cit:(["test_a_pending_cleanup_offers_a_retry_and_never_a_cleanup_decision"], mcp/tests/test_post_integration_cleanup_guidance.py:45-45)
  — the un-reclaimed contract projects `cleanup-pending`, `retry_cleanup`, `worktree_cleanup` with the
  contract's own args, and a summary that says the cleanup is automatic and names the retry. The
  "never a cleanup decision" half of the name is carried by the second case, which proves the
  vocabulary member is gone.
- `test_the_cleanup_decision_is_no_longer_in_the_next_operation_vocabulary` cit:(["test_the_cleanup_decision_is_no_longer_in_the_next_operation_vocabulary"], mcp/tests/test_post_integration_cleanup_guidance.py:58-58)
  — `retry_cleanup` is a `NextOperation` member and `request_cleanup_decision` is not.
- `test_a_checkpointed_series_keeps_working_instead_of_being_told_to_integrate` cit:(["test_a_checkpointed_series_keeps_working_instead_of_being_told_to_integrate"], mcp/tests/test_post_integration_cleanup_guidance.py:65-65)
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

- **The projection is asserted by phase, operation, tool and args**, not by summary text alone; the
  summary assertions are additive (the words a reader needs) rather than the contract.
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
| The projection under test, including the checkpointed branch the third case pins. | `_post_integration_phase` | mcp/src/agents_remember/worktrees/modules/guidance.py:255-331 |
| The checkpointed branch itself. | "if contract.integration_status == \"checkpointed\":" | mcp/src/agents_remember/worktrees/modules/guidance.py:307-307 |
| The vocabulary member the second case proves removed (declared on the wire model, imported by guidance). | `NextOperation` | mcp/src/agents_remember/models/worktree.py:50-58 |
| The cleanup retry the first case pins. | `_post_integration_phase`; `retry_cleanup` | mcp/src/agents_remember/worktrees/modules/guidance.py:255-329 |

## Cross-Repo References

These are in-process assertions over a constructed contract; no sibling repository or external system
participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Update History
- 2026-09-12T04:10+02:00 — Created by the 260831-LOCR-L30 follow-up curator pass. Documents the
  three cases, the one-cell-per-case fixture convention, and the checkpoint projection the new case
  pins (which is the exact set of assertions that failed before the `checkpointed` branch existed).
  Verification metadata is pinned to the leaf base commit and remains closeout-owned.

- 2026-09-12T01:26:36+00:00: Generated citation repair: `_post_integration_phase`; `retry_cleanup` repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:255-329; mcp/src/agents_remember/worktrees/modules/guidance.py:302-302. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b5cbe38ab438de766feb0fc3860228f5125b623ebbee641f90211d51326d68e; claim bytes unchanged; generated by ccr-r10@v1.