# mcp/src/agents_remember/models/lifecycles/finalize.py

## Governing Overview

[lifecycles overview](overview.md)

## Purpose

Defines the strict public response contract for `lifecycle_finalize_task`.

## Code Commentary

`LifecycleFinalizeTaskResponse` inherits from `ToolResponse`, so it uses the
strict Agents Remember response-envelope convention. It declares the finalizer
operation name plus identity fields (`taskId`, `taskName`, `lifecycleId`), the
current finalizer `state`, `dryRun`, contract path, optional landed commit and
target branch, blocker list, cleanup detail, task-update detail, and summary.

The model intentionally does not accept the full `worktree_status` payload. The
finalizer response is a separate terminal contract: it reports only the edge
proof, cleanup result, task-document reconciliation, and blockers relevant to
finalization.

Completion-seat cleanup is additive to finalization truth. Default-on auto-close reports
`autoClosedSeats`, `autoCloseDeferredSeats`, and `autoCloseFailedSeats`; the explicit settings
opt-out retains `autoLandedSeats` for the historical landed/archive path. All four lists remain
empty for dry runs or disabled edges and do not replace the finalizer state, blocker, cleanup, or
task-document evidence.

## Agent archive in the finalize response (MIK-R76)

`LifecycleFinalizeTaskResponse` declares `agentArchive`, the report the finalizer carries from the
cleanup or abandon transaction (`archived`, `alreadyArchived`, `gone`, `owed`, `leftAlone` and a
summary). It is empty when no archive ran.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- Strict tool response base class is defined here. [1]
- Public response registry maps `lifecycle_finalize_task` to this model. [2]
- The finalizer response model is the current wire authority; deleted representative-payload tests provide no current pass. [3]
- `lifecycle_finalize_task_tool` populates `autoLandedSeats` from `_auto_land_completed_seats`, gated by `config.retirement.auto_land_on_finalize`. [4]
- `RetirementSettings.auto_land_on_finalize` is the config gate this field's population depends on. [5]

## Series-Contract Notes

`LifecycleFinalizeTaskResponse` carries both the leaf `enclosurePath` and the root-level `taskArchive` result so finalization can report contract cleanup and root archival separately.


## PDLS Reconciliation

Finalize responses now carry bounded typed task-document projection effects so queue invalidation/rebuild hints remain explicit without blocking task authoring.

This change preserves the file's existing authority boundary. No threshold exception, silent
fallback, or compatibility reader was added.
## 260918-TSIP-L4 — The Two Atomic-Series Projections Declared (`D53`)

`LifecycleFinalizeTaskResponse` now declares the atomic-series terminal projection it was
already receiving: `atomicSeriesActivation: AtomicSeriesActivationFact | None` and
`atomicSeriesActivationRelease: AtomicSeriesActivationReleaseFact | None` (**`:53`**, **`:54`**;
the class runs **`:18-54`**, file **39 → 54 lines**). `AtomicSeriesActivationReleaseFact` is new
in `models/worktree.py` and is imported with `AtomicSeriesActivationFact` at **`:12-15`**, which
is why every line at or below the old `:12` moved `+4`.

**This model was the only strict consumer of that projection and the only one that did not
declare it**, so the transaction completed and the caller was handed
`2 validation errors for LifecycleFinalizeTaskResponse` instead of the payload that would have
told it so. The direction is settled by the product, not by this file:
`application/worktree_status.py:317` projects `atomicSeriesActivation` on the tool that reads
status, and both keys are already declared on `WorktreeSummary` (a nested `extra="forbid"` model)
and on `WorktreeCommandResponse` (the flexible base every worktree response inherits). Deleting
them here would make the terminal operation the one place a caller cannot learn whether the
series activation was released.

**The two keys do not arrive together on every arm.** On the success path `_finalized_result`
copies both from `worktrees/modules/finalize.py:209-210`; on the `activation-release-blocked` arm
(`:161-177`) the key arrives through `**activation_release.payload`, and only
`atomicSeriesActivationRelease` is present there, because the bridge writes
`atomicSeriesActivation` only after a *successful* release
(`worktrees/activation/atomic_series_activation_terminal.py:49`, against the `except` at `:33-44`).
Both are optional here for that reason. Pinned by
`mcp/tests/test_tool_response_conformance.py`, whose
`test_the_two_atomic_series_keys_are_declared_together` asserts the declaring set is exactly
`{"lifecycle_finalize_task"}`.
