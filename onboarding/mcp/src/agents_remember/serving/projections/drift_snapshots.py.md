# mcp/src/agents_remember/serving/projections/drift_snapshots.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `mcp/src/agents_remember/serving/projections/drift_snapshots.py` |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-07-31T00:00+02:00                                 |
| lastVerifiedCommitHash |                                                        `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |                                                        2026-08-26T08:10:26+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[serving projections overview](overview.md)

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The helper centralizes the sanitized drift snapshot filename and exact dry-run/removal payload. | "def drift_snapshot_path(coordination_root: Path", "def remove_drift_snapshot(", "return _remove_snapshot_file(" | mcp/src/agents_remember/kernel/primitives/drift_snapshot.py:21-24; mcp/src/agents_remember/kernel/primitives/drift_snapshot.py:27-35; mcp/src/agents_remember/serving/projections/drift_snapshots.py:82-99 |
| Projection pruning keeps configured repositories and still-existing leaf worktrees, skips invalid snapshots, and removes valid orphaned snapshots. | `prune_orphaned_drift_snapshots`, `_active_worktree_snapshot_keys`, `_read_valid_snapshot` | mcp/src/agents_remember/serving/projections/drift_snapshots.py:23-56; mcp/src/agents_remember/serving/projections/drift_snapshots.py:59-69; mcp/src/agents_remember/serving/projections/drift_snapshots.py:72-79 |
| `prune_orphaned_drift_snapshots` and `_active_worktree_snapshot_keys` take the keyword-only `contracts` snapshot; the tick-injected snapshot means zero pruning-time contract parses. | `prune_orphaned_drift_snapshots`, `_active_worktree_snapshot_keys` | mcp/src/agents_remember/serving/projections/drift_snapshots.py:23-56; mcp/src/agents_remember/serving/projections/drift_snapshots.py:59-69 |
| The shared per-tick contract snapshot + stat-identity parse cache the pruner consumes. | `ContractSnapshot`, `ContractSnapshotCache` | mcp/src/agents_remember/serving/projections/contract_snapshot.py:37-49; mcp/src/agents_remember/serving/projections/contract_snapshot.py:60-126 |
| The projection-input module exposes the `read` and refresh entries. | "def read(", "def _refresh_tasks(", "def _refresh_drift(" | mcp/src/agents_remember/serving/projections/projection_inputs.py:225-225; mcp/src/agents_remember/serving/projections/projection_inputs.py:279-279; mcp/src/agents_remember/serving/projections/projection_inputs.py:368-368 |
| The projection-store module exposes the `project_and_write` entry. | "def project_and_write(" | mcp/src/agents_remember/serving/projections/projection_store.py:214-214 |
| PTS-L2 tests pin prune-key parity with and without the shared snapshot. | `ContractSnapshotSharedPassTests`, `test_reader_outputs_equal_with_and_without_shared_snapshot` | mcp/tests/test_projection_scaling_cs6.py:590-858 |
| Cleanup binds the `cleanup_result`. | `cleanup_result` | mcp/src/agents_remember/worktrees/modules/cleanup.py:611-656 |
| Tests cover shared drift-snapshot path usage by reader/producer suites and projection-time pruning of orphaned worktree snapshots (the dry-run/exact cleanup-removal coverage now lives with the worktree cleanup tests). | `DriftSnapshotReaderTests`, `DriftSnapshotProducerTests`, `test_project_and_write_prunes_orphaned_worktree_drift_snapshots`, `_write_snapshot` | mcp/tests/test_observer_projection_ledger.py:210-284; mcp/tests/test_observer_projection_ledger.py:419-457; mcp/tests/test_observer_projection_ledger.py:459-476; mcp/tests/test_observer_projection_readers.py:156-202 |

## Cross-Repo References

No meaningful cross-repo references found.

## Update History

- 2026-08-04T11:35:04+02:00 — 260731-EFA-L6 S18-B10 curator: applied reviewer verdict D1-D25 repairs and the pre-PASS whole-claim audit; split the pooled projection-flow row into path-correct generated entry-point claims and rechecked this card through the locked exact-document fixer/check.

- 2026-08-03T03:00:24+02:00 — W3-B04 curator: curated 7 table citations and 5 prose citations (12 total), supplying exact anchors and paths; the scoped fixer generated all final extents.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired the projection input/store references and focused test row after the source move; the current operative ranges are recorded in Repo-Internal References above.
- 2026-07-31T16:40+02:00 — 260731-EFA-L2: the whole-tree `ruff format` pass (`00e8379`) reflowed
  `mcp/src/agents_remember/serving/projections/drift_snapshots.py` and moved the lines this card cites, so
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
