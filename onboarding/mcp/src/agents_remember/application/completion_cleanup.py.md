# mcp/src/agents_remember/application/completion_cleanup.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/application/completion_cleanup.py`  |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated | 2026-08-25T23:19+02:00 |
| lastVerifiedCommitHash | `c51373425be3e3f488590ad2f444810df89b4ffb`|
| lastVerifiedCommitDate | 2026-08-26T19:22:10+02:00|
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
`autoLandedSeats`. Candidate selection uses `binding_task_document_ref`, so a staged replacement is
closed with the same canonical leaf seat instead of escaping cleanup through its replacement field.

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
- Primary and staged-replacement rows are compared through their canonical binding document.

### Todos

None.

## Docs References

No Domain Documentation entries are configured for this repository, and this module implements a
repository-local orchestration policy.

## Repo-Internal References

The worktree application entry points invoke this owner only after successful non-dry-run edges;
tests pin edge wiring separately from cleanup failure containment.

| Finding | Anchor | Source |
| --- | --- | --- |
| The completion owner resolves task truth, folds report evidence, and applies the configured close/land policy. | `auto_complete_seats` | mcp/src/agents_remember/application/completion_cleanup.py:29-72 |
| Candidate selection includes every non-terminated role occupant bound to the canonical task document. | `_completion_candidates` | mcp/src/agents_remember/application/completion_cleanup.py:115-124 |
| Focused tests prove contract, retirement-race, per-seat failure, and opt-out landing containment. | `CompletionCleanupContainmentTests` | mcp/tests/test_completion_cleanup.py:47-169 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this module.

## Update History

- 2026-08-25T23:19+02:00 — Contract-wide citation curation: re-read the current anchored claim(s), retained the supported wording, and cleared verification metadata for closeout-owned restamping.

- 2026-08-25T22:27+02:00 — No content impact: final ARSPAWN-L2 review confirmed the existing
  canonical-binding cleanup description already matches the unchanged one-line candidate delta.
  Verification remains closeout-owned.

- 2026-08-25T19:51+02:00 — 260821-ARSPAWN-L2: candidate selection now uses the canonical binding
  document so a staged replacement participates in completion cleanup. Verification remains
  closeout-owned.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — Replaced qualified-leaf cleanup with canonical task-document topology,
  task-addressed turn-report proof, and task-bound landing/retirement.
- 2026-08-10T13:00+02:00 — 260731-EFA-L9 curator: No content impact: re-read the current staged completion-edge cleanup policy; the report-gated worker/reviewer/curator boundary remains accurately described. Verification metadata remains pinned until closeout.
- 2026-08-10T06:28+02:00 — Created when completion-seat cleanup was extracted from the worktree
  application entry-point module. The split preserves exact-report-gated close behavior, the
  landed/archive opt-out, owner-role exclusion, per-seat containment, and additive response fields.
  Verification metadata remains blank until closeout stamps the code commit.
