# mcp/src/agents_remember/application/completion_cleanup.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/application/completion_cleanup.py`  |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-08-10T06:28+02:00                                       |
| lastVerifiedCommitHash |                                                              `c9ae4dbd8adb650f116b9d4f86343b496c3e5f32`|
| lastVerifiedCommitDate |                                                              2026-08-12T17:53:40+02:00|
| governingOverview      | `overview.md`                                                |

## Governing Overview

[Application overview](overview.md)

## Purpose

`completion_cleanup.py` owns the resource-cleanup policy that runs only after a worktree
integration or lifecycle-finalization edge has already succeeded. It closes completed
worker/reviewer/curator seats when an exact durable report proves their turn finished, while
preserving the historical landed/archive mode as an explicit settings opt-out.

## Code Commentary

### Logic

`auto_complete_seats` resolves the enclosure contract to a canonical `TaskDocumentRef` through
`TaskDocumentTopology` and opens the durable terminal catalog. With
`autoCloseCompletedSeats=true`, `_retire_reported_leaf_seats` folds the operator inbox once, admits
only `turn-report` records with the exact `senderAgentId` and matching
`subjectTaskDocumentRef`, and retires matching live or landed task seats through `retire_entry`.
Missing proof is returned in
`autoCloseDeferredSeats`; per-seat exceptions are returned in `autoCloseFailedSeats`; successful
retirements are returned in `autoClosedSeats` and logged best-effort after catalog provenance is
durable. With auto-close disabled, the same finite role set uses `land_seats_for_task` and returns
`autoLandedSeats`.

### Conventions

The completion edge supplies the human-readable reason and edge identifier. This module supplies
the finite eligible-role boundary and all cleanup side effects. Result keys use the public wire
names declared by the integration and finalization response models.

### Invariants And Boundaries

- Automatic close is report-gated by exact session and exact task-document identity; a missing or
  wrong-task report never kills a process.
- Only worker, reviewer, and curator are candidates. Manager and orchestrator are coordination
  owners and cannot enter the automatic cleanup set.
- Cleanup is subordinate to the already-successful completion edge. Contract, inbox, catalog,
  host, landing, or observer-log failures cannot rewrite integration/finalization success.
- Retirement uses the normal graceful-stop, tmux termination, and catalog-provenance path.
  Transcripts and durable reports are not deleted.
- The inbox is folded once per edge and the candidate list is read once, avoiding per-seat store
  rescans.

### Todos

None.

## Docs References

No Domain Documentation entries are configured for this repository, and this module implements a
repository-local orchestration policy. No relevant external documentation was available.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain contract governs this repository-local cleanup policy. | — | — |

## Repo-Internal References

The worktree application entry points invoke this owner only after successful non-dry-run edges;
tests pin edge wiring separately from cleanup failure containment.

| Finding | Anchor | Source |
| --- | --- | --- |
| Integration and finalization call `auto_complete_seats` only after their underlying edge succeeds. | `worktree_integrate_tool`; `lifecycle_finalize_task_tool` | mcp/src/agents_remember/application/worktree_tools.py:359-401; mcp/src/agents_remember/application/worktree_tools.py:514-545 |
| Normal retirement terminates the host and persists catalog retirement provenance without touching transcripts. | `retire_entry` | mcp/src/agents_remember/serving/retire.py:37-71 |
| Durable inbox folding supplies the exact report rows used as the close barrier. | "def current(self) -> dict[str, OperatorInboxEntry]:" | mcp/src/agents_remember/controlplane/operator_inbox_store.py:141-141 |
| Integration tests prove all eligible roles, owner exclusions, report matching, provenance, transcript retention, and opt-out landing. | `AutoLandHookIntegrationTests` | mcp/tests/test_seat_lifecycle.py:645-869 |
| Focused tests prove contract, retirement-race, per-seat failure, and opt-out landing containment. | `CompletionCleanupContainmentTests` | mcp/tests/test_completion_cleanup.py:47-169 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this module.

| Finding | Anchor | Source |
| --- | --- | --- |
| Cleanup reads only repositories and runtime paths already resolved by Agents Remember configuration. | — | — |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — Replaced qualified-leaf cleanup with canonical task-document topology,
  task-addressed turn-report proof, and task-bound landing/retirement.
- 2026-08-10T13:00+02:00 — 260731-EFA-L9 curator: No content impact: re-read the current staged completion-edge cleanup policy; the report-gated worker/reviewer/curator boundary remains accurately described. Verification metadata remains pinned until closeout.
- 2026-08-10T06:28+02:00 — Created when completion-seat cleanup was extracted from the worktree
  application entry-point module. The split preserves exact-report-gated close behavior, the
  landed/archive opt-out, owner-role exclusion, per-seat containment, and additive response fields.
  Verification metadata remains blank until closeout stamps the code commit.
