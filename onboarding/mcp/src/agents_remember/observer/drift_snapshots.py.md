# mcp/src/agents_remember/observer/drift_snapshots.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `mcp/src/agents_remember/observer/drift_snapshots.py`  |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-06-27T23:09+02:00                                 |
| lastVerifiedCommitHash |                                                        `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`|
| lastVerifiedCommitDate |                                                        2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[observer Overview](overview.md)

## Purpose

`drift_snapshots.py` centralizes the observer drift-snapshot file contract and
the retention policy for worktree-owned snapshots. It gives the drift producer,
projection tick, and cleanup path one shared way to name and remove snapshot
files so stale dashboard mirror rows do not survive after their worktree has
been deleted.

## Code Commentary

### Logic

`drift_snapshot_path(coordination_root, repository, branch)` sanitizes the
repository and branch tokens the same way drift report paths are sanitized, then
returns the corresponding `logs/observer/drift/<repo>__<branch>.json` path.

`remove_drift_snapshot(...)` removes or dry-runs the exact snapshot for one
repository/branch pair and returns a small result payload with the path,
repository, branch, removal state, and an honest reason when the file is already
absent or unlink fails.

`prune_orphaned_drift_snapshots(config)` scans the coordination drift snapshot
directory. It keeps valid snapshots for configured repositories, keeps valid
snapshots whose `(repository, branch)` still matches a leaf enclosure with an
existing `code_worktree`, skips unreadable or wrong-schema JSON files, and
physically deletes the remaining valid worktree snapshots. This keeps invalid
diagnostic files available for manual inspection while pruning rows the memory
mirror would otherwise keep rendering forever.

### Conventions

The filename contract is shared through this module rather than reconstructed in
each producer or test. Snapshot validity is schema-based
(`ar-drift-snapshot/v1`), matching the observer reader's contract.

### Invariants And Boundaries

- The drift snapshot path helper is the single naming contract for drift
  producer writes, reader fixtures, projection pruning, and cleanup deletion.
- Pruning only deletes valid drift-snapshot JSON with a recognized schema.
  Malformed, unreadable, or wrong-schema files are skipped rather than guessed.
- Configured repository snapshots are durable analytical inputs and are never
  pruned as worktree orphans.
- Worktree snapshots survive while their leaf contract exists and the recorded
  code worktree path still exists.
- Cleanup removes only the exact code-worktree snapshot named by its contract;
  unrelated repository/branch snapshots remain for their own lifecycle.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

This helper is intentionally small but load-bearing because it sits between the
drift producer, the observer projection tick, and worktree cleanup.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The helper centralizes the sanitized drift snapshot filename and exact dry-run/removal payload. | L17-L31; L85-L102 | [drift_snapshots.py](agents-remember/mcp/src/agents_remember/observer/drift_snapshots.py) |
| Projection pruning keeps configured repositories and still-existing leaf worktrees, skips invalid snapshots, and removes valid orphaned snapshots. | L34-L60; L63-L82 | [drift_snapshots.py](agents-remember/mcp/src/agents_remember/observer/drift_snapshots.py) |
| `project_and_write` calls the pruner after enclosure discovery and before `read_drift_snapshots`, so the reducer sees the pruned snapshot set. | L85-L115 | [projection_store.py](agents-remember/mcp/src/agents_remember/observer/projection_store.py) |
| Cleanup removes the contract's exact code-worktree snapshot and returns that result under `drift_snapshots`. | L325-L364 | [cleanup.py](agents-remember/mcp/src/agents_remember/worktrees/modules/cleanup.py) |
| Tests cover shared path usage, projection-time pruning, dry-run cleanup reporting, and exact cleanup removal. | L1240-L1264; L1755-L1808 | [test_observer_projection.py](agents-remember/mcp/tests/test_observer_projection.py) |

## Cross-Repo References

No meaningful cross-repo references found.

## Update History

- 2026-06-27T23:09+02:00 — Task 32 memory-mirror pruning: created onboarding for the shared drift snapshot path/removal/pruning helper. Verification metadata remains empty until closeout stamps the code commit.
