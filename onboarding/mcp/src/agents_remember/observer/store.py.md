# mcp/src/agents_remember/observer/store.py

## Governing Overview

[observer overview](overview.md)

## Purpose

`store.py` appends every event to the bounded shared workspace Event River and reads its validated JSONL records.

## Code Commentary

### Workspace River cursor and lock

Workspace appends now take a POSIX `flock` on `workspace/events.lock`, the same cross-process lock
used by physical compaction and live reads. `events.cursor.json` stores the non-negative virtual
`baseOffset`, written atomically, and `workspace_logical_size` exposes virtual EOF. This lock is
necessary rather than generic defensive code: serving and MCP processes both append while the live
compactor replaces the file, so an unlocked rewrite can lose writes or tear cursor state.

All events route to `workspace/events.jsonl`; no per-lifecycle logs or heartbeat-sidecar merge APIs remain. Optional scopeKey is correlation, not physical routing or a writer exemption.

### 260928-MIK-L114 River Admission And Write-Free Reads

`workspace_river_lock` optionally times out with `TimeoutError`/`OSError`. `workspace_river_read` opens an existing lockfile without creating observer files: it yields true only after acquiring the shared lock, and false if opening or locking fails. The helper itself performs no lockless base/file read. Serving's separate `_read_source_lines` owns the missing-lock branch: it admits that window only when the lockfile is absent before and after the read; otherwise it repeats under a confirmed shared hold, returning no rows with the caller's cursor unchanged when that hold is unavailable. `EventStore.append` always enters common size admission under the River lock; session identity cannot bypass it.

`EventStore.read()` skips invalid/torn persisted rows; damaged activity records establish no task status.

`EventStore(observer_root).log_path()` is always `workspace/events.jsonl`. `append(event)` creates parent directories and passes alias-serialized bytes to `admit_workspace_river_row`; `read()` validates surviving records as `Event` objects.

## Invariants And Boundaries

- River writers and compaction serialize with a shared lock, without an exclusive-live-session exemption.
- Retention may replace the file and advance its virtual base; this is not crash-atomic across separate files.
- Browser tailing is separately write-free; events are observations, not authored task-stage authority.

## Evidence

### Repo-Internal References

- EventStore serializes and validates the shared Event envelope. [1]
- Every append uses bounded workspace admission; tolerant reads admit valid records only. [2]
- The read helper reports whether an existing shared lock was actually acquired; it does not perform a lockless read. [3]
- Serving, not the helper, owns the guarded missing-lock base/file window and the confirmed-hold fallback. [4]
