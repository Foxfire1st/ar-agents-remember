# mcp/src/agents_remember/observer/drift_snapshots.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `mcp/src/agents_remember/observer/drift_snapshots.py`  |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-07-31T00:00+02:00                                 |
| lastVerifiedCommitHash |                                                        `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |                                                        2026-07-31T19:28:50+02:00|
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

`prune_orphaned_drift_snapshots(config, *, contracts=None)` scans the coordination drift snapshot
directory. It keeps valid snapshots for configured repositories, keeps valid
snapshots whose `(repository, branch)` still matches a leaf enclosure with an
existing `code_worktree`, skips unreadable or wrong-schema JSON files, and
physically deletes the remaining valid worktree snapshots. This keeps invalid
diagnostic files available for manual inspection while pruning rows the memory
mirror would otherwise keep rendering forever.

Since 260712-PTS-L2 the live-worktree keys come from a `ContractSnapshot`:
`_active_worktree_snapshot_keys(coordination_root, *, contracts=None)` iterates
`snapshot.contracts.values()` instead of running its own
`iter_leaf_enclosure_contracts` walk + `load_contract` parse. The projection tick
passes its shared per-tick snapshot, so pruning adds ZERO contract parses — the
third per-tick contract walk is gone; a standalone call (`contracts=None`) builds
a local one-shot snapshot with identical behavior. The snapshot's contracts are
shared across ticks and are only read here, never mutated.

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
- Pruning never parses contracts inside the projection tick: it consumes the
  injected shared `ContractSnapshot` (and treats its contracts as immutable);
  only a standalone call builds its own local snapshot.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

This helper is intentionally small but load-bearing because it sits between the
drift producer, the observer projection tick, and worktree cleanup.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The helper centralizes the sanitized drift snapshot filename and exact dry-run/removal payload. | L19-L33 | [drift_snapshots.py](agents-remember/mcp/src/agents_remember/observer/drift_snapshots.py) |
| Projection pruning keeps configured repositories and still-existing leaf worktrees, skips invalid snapshots, and removes valid orphaned snapshots. | L36-L69 | [drift_snapshots.py](agents-remember/mcp/src/agents_remember/observer/drift_snapshots.py) |
| `prune_orphaned_drift_snapshots` and `_active_worktree_snapshot_keys` take the keyword-only `contracts` snapshot; the tick-injected snapshot means zero pruning-time contract parses. | L36-L44; L72-L80 | [drift_snapshots.py](agents-remember/mcp/src/agents_remember/observer/drift_snapshots.py) |
| The shared per-tick contract snapshot + stat-identity parse cache the pruner consumes. | L1-L112 | [contract_snapshot.py](agents-remember/mcp/src/agents_remember/observer/contract_snapshot.py) |
| `project_and_write` drives one `ProjectionInputState` per tick; that state builds the contract snapshot once during task refresh (with enclosure discovery) and passes it to the pruner before `read_drift_snapshots`, so the reducer sees the pruned snapshot set. | L214-L237 · L225-L238, L266-L270, L345-L350 | [projection_store.py](agents-remember/mcp/src/agents_remember/observer/projection_store.py) · [projection_inputs.py](agents-remember/mcp/src/agents_remember/observer/projection_inputs.py) |
| PTS-L2 tests pin prune-key parity with and without the shared snapshot. | L669-L700 | [test_projection_scaling_cs6.py](agents-remember/mcp/tests/test_projection_scaling_cs6.py) |
| Cleanup removes the contract's exact code-worktree snapshot and returns that result under `drift_snapshots`. | L325-L364 | [cleanup.py](agents-remember/mcp/src/agents_remember/worktrees/modules/cleanup.py) |
| Tests cover shared drift-snapshot path usage by reader/producer suites and projection-time pruning of orphaned worktree snapshots (line ranges repaired 2026-07-31; the dry-run/exact cleanup-removal coverage now lives with the worktree cleanup tests). | L2104-L2150; L2484-L2558; L2693-L2750 | [test_observer_projection.py](agents-remember/mcp/tests/test_observer_projection.py) |

## Cross-Repo References

No meaningful cross-repo references found.

## Update History

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 2 cross-file line citations and reworded one
  claim. The tick-time pruner call is no longer in `projection_store.py`: `project_and_write` (L214-L237)
  now delegates to `ProjectionInputState`, whose `read` orders the refreshes (L225-L238), whose
  `_refresh_tasks` builds the contract snapshot once and does enclosure discovery (L266-L270), and whose
  `_refresh_drift` passes `contracts=` to `prune_orphaned_drift_snapshots` immediately before
  `read_drift_snapshots` (L345-L350) — so the row now cites both files and names the state object. The
  `test_observer_projection.py` row now cites `DriftSnapshotReaderTests` L2104-L2150,
  `DriftSnapshotProducerTests` L2484-L2558, and the prune test plus its `_write_snapshot` helper
  L2693-L2750 (was L2027-L2060; L2616-L2671, which had drifted onto unrelated reader suites).
- 2026-07-31T16:40+02:00 — 260731-EFA-L2: the whole-tree `ruff format` pass (`00e8379`) reflowed
  `mcp/src/agents_remember/observer/drift_snapshots.py` and moved the lines this card cites, so
  the Citations column no longer pointed at the code its rows name. Corrected the ranges (L36-L71
  → L36-L69; L74-L82 → L72-L80). The behaviour described is unchanged — the file's AST is
  identical to the base revision — this is a citation repair only. Verification metadata pinned
  until closeout stamps the L2 commit.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-07-12T20:02+02:00 — 260712-PTS-L2: `prune_orphaned_drift_snapshots` and
  `_active_worktree_snapshot_keys` gained keyword-only `contracts: ContractSnapshot | None = None`;
  the projection tick injects the shared per-tick snapshot so pruning parses no contracts (the third
  per-tick contract walk removed), while a standalone call builds a local snapshot with identical
  behavior. Verification metadata pinned until closeout stamps the PTS-L2 commit.
- 2026-06-27T23:09+02:00 — Task 32 memory-mirror pruning: created onboarding for the shared drift snapshot path/removal/pruning helper. Verification metadata remains empty until closeout stamps the code commit.
