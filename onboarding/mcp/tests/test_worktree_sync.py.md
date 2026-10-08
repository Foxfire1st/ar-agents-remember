# mcp/tests/test_worktree_sync.py

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Checks supported worktree sync, parked-WIP restoration, real conflicts and continuation/cancellation on fixture repositories.

## Code Commentary

SyncFixture drives the public transaction with an explicit code and memory pair. Cases check paired fast-forward and contract bases, code-conflict continuation, source-ref resolution, cache exclusions, cancelled restoration and memory-content conflict recovery. Memory conflicts are current knowledge-file/content conflicts; the canonical dataset reconciliation engine and its old helper vocabulary are retired. The transaction journal must describe its actual stop/continue state rather than infer completion from matching HEADs. No source or index operation is authorized by reading these tests, and no run is claimed.

## Evidence

### Repo-Internal References

- `SyncFixture` owns the current boundary described above. [12]
- `WorktreeSyncTests` owns the current boundary described above. [13]
