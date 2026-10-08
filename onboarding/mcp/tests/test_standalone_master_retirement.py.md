# mcp/tests/test_standalone_master_retirement.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

The integration cases for what finalization does to a master, for retiring a master that no sprint commands, for the
retry rules of both retirement routes, and for the restart notice and the archive reader's canonical-path check. It
reuses the `World` fixture of `test_master_retirement.py`. The module is in the `integration` lane.

## Code Commentary

### Logic

- **Finalization never archives a master (three cases).** A sprint-commanded master completes its sprint row, keeps its
  folder, and the archive result is `skipped` with `reason: sprint-commands-master`, the sprint named and
  `task_doc.retire_master` in the detail. A master no sprint commands keeps its folder, no ref moves, and the archive
  result is `master-archived-only-by-retire` with no `reviewArtifacts` and no `archivePath`. An ordinary standalone task
  keeps today's `root-series-still-active` result and its leaf update `skipped`. `archive_completed_root_task` itself
  never archives a task that holds a series contract. An organizational master that no sprint commands finalizes with
  its folder kept.
- **Contradictory typed sprint rows refuse finalization.** Two typed rows for the same master refuse as
  `task-document-resolution-blocked` with `task-sprint-linkage-row-duplicate` in both a dry run and a real run;
  the task tree and contract stay unchanged. A sprint without a typed row for the master is not broken linkage
  and permits finalization, as does a valid single correlated row.
- **Retiring a master no sprint commands.** The dry run and real run edit no sprint and write the proof into the
  master's folder; a sprint-commanded master, a mismatched `masterRef` or `removeEdges` are refused.
  Pending cleanup alone permits the dry run; an existing child worktree refuses with no write.
  Source or evidence drift before publication refuses before the hook runs; a failed move restores the folder
  and removes the proof; an interrupted move resumes only for the same request; and a partial hook failure
  keeps the retirement and retries the cleanup only.
- **Retry refusals.** A retry with other edge arguments, a different reason, or a stored `archiveRef` or `masterRef` of
  another namespace is refused and every byte stays unchanged.
- **Hook exceptions and restoration.** An exception of any type from the hook ends as a reported failure and the same
  request recovers. An exception of any type before archival (`RuntimeError`, `KeyError`) ends restored on both routes.
- **Receipts and notice.** A repeated completed request writes no new receipt. A build whose model lacks the
  `retirement` key refuses with a restart instruction. Successful previews and retirements, repeated completed requests,
  cleanup failures and refusals after a retirement record exists carry "Restart required"; a refusal before anything
  is recorded carries no restart notice.
- **Archive reader.** An operation record stored under a name that does not match its content is refused by
  `terminal_operation_evidence` and by the retirement.

### Conventions

- `lone` creates a completed master with a series contract that no sprint commands; `retire_lone` calls the operation on it.

### Invariants And Boundaries

- These cases prove that a finalized master's folder stays in place, and the routes' recovery and refusal rules.

## Evidence

- Finalizing a sprint-commanded master completes its row, keeps the folder and names the sprint. [1]
- Finalizing a master no sprint commands keeps it and names the retire route. [2]
- An ordinary standalone task keeps today's skip. [3]
- The archive step never archives a task that holds a series contract. [4]
- A partial hook failure on a lone master keeps the retirement and retries the cleanup only. [5]
- A retry with other edge arguments is refused with no change. [6]
- Any exception before archival ends restored on both routes. [7]
- A record that does not match its canonical file name is refused. [8]

- Pending cleanup alone permits preview while a real child worktree refuses. [9]
- A refusal before a retirement record exists carries no restart notice. [10]
