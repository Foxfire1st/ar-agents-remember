# mcp/src/agents_remember/serving/projections/drift_snapshots.py

## Governing Overview

[serving projections overview](overview.md)

## Purpose

`drift_snapshots.py` owns serving-time retention of worktree drift snapshots.
Naming and exact cleanup deletion belong to `kernel/primitives/drift_snapshot.py`;
this serving module consumes the observer directory/schema contract and prunes
valid orphan snapshots, optionally announcing its own removals.

## Code Commentary

### Logic

`kernel/primitives/drift_snapshot.py::drift_snapshot_path(coordination_root, *, repository, branch)` sanitizes the
repository and branch tokens the same way drift report paths are sanitized, then
returns the corresponding `logs/observer/drift/<repo>__<branch>.json` path.

The kernel `remove_drift_snapshot(...)` removes or dry-runs the exact snapshot for one
repository/branch pair and returns a small result payload with the path,
repository, branch, removal state, and an honest reason when the file is already
absent or unlink fails.

`prune_orphaned_drift_snapshots` first enumerates actual native branch refs for configured repositories and contract code repositories. Only a complete branch/contract/snapshot census permits valid orphan removal. Configured membership or an existing code-worktree directory alone does not preserve a nonexistent branch, and a failed Git/listing read or skipped contract proves no removal. Unlink failure is explicit; malformed/unreadable snapshots are kept diagnostically and invalidate the kind’s removal proof.

The injected immutable `ContractSnapshot` is reused for repository/branch identities; a standalone call builds its own snapshot. `_observe_branches` lists refs once per repository root on drift/task invalidation, not idle heartbeat, and uses the same subject names as the producing snapshots. `read_drift_snapshot` is shared by pruning and projection and validates schema, nonempty repository/branch, nonnegative integer counts (not bool) and optional nonempty fingerprint. Missing fingerprints preserve older acknowledgements; they are not invented recovery evidence.

### Conventions

Filename naming remains kernel-owned. Shared `read_drift_snapshot` enforces more than the schema tag; pruning and projection consume the same validated payload shape.

### Invariants And Boundaries

- Kernel naming/exact cleanup boundaries remain distinct from serving orphan pruning.
- Native branch existence decides live drift subjects; configured repository and directory presence are insufficient.
- Any incomplete source proof prevents removal for the kind; invalid snapshots remain available for diagnosis.
- Contract snapshots are read-only and shared; standalone calls may build their own.
- Changed complete fingerprints identify drift recurrence; missing fingerprints and unknown health do not.

### Todos

None.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

This helper is intentionally small but load-bearing because it sits between the
drift producer, the observer projection tick, and worktree cleanup.


| Cleanup binds the `cleanup_result`. | `cleanup_result` | mcp/src/agents_remember/worktrees/modules/cleanup.py:611-656 |


### Cross-Repo References

No meaningful cross-repo references found.

- Kernel naming/exact cleanup retains its boundary. [1]
- Drift pruning reuses the supplied contract snapshot (or builds one standalone), lists native heads once per configured/contract code repository and observes configured and worktree branch identities. A skipped contract, failed ref census or invalid/unreadable snapshot makes removal proof incomplete: invalid snapshots are skipped and every valid snapshot is retained. Only a complete census permits removal of a valid snapshot whose repository/branch identity is absent; physical checkout existence alone is not the keep policy. [2]

- `prune_orphaned_drift_snapshots` takes the keyword-only `contracts` snapshot and hands it to `_observe_branches`; the tick-injected snapshot means zero pruning-time contract parses.  Anchor: `prune_orphaned_drift_snapshots`, `_observe_branches` [3]

- Contract snapshots remain immutable shared inputs. [4]
