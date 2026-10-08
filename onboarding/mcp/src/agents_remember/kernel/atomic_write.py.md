# mcp/src/agents_remember/kernel/atomic_write.py

## Governing Overview

[mcp package overview](../../../overview.md)

## Purpose

Publishes one file through a sibling temporary file and a replacement, with explicit file and directory durability steps.

## Code Commentary

`atomic_write_bytes` writes, flushes and fsyncs its unique sibling temporary file, then calls `os.replace` directly. Its failure handler removes that temporary file, and its `finally` block releases the in-process in-flight mark. After replacement it removes only same-target abandoned temporaries whose writers are proven gone, then fsyncs the destination directory. A live or unknown writer keeps its temporary file; an invalid process number is treated as unknown, and Windows skips this cleanup. Cleanup does not promise that every leftover is removable. [9]

`atomic_replace` separately reports rename failure while the destination retains its previous bytes, or directory-fsync failure after the destination has changed and the source is absent. Neither a post-replacement directory-fsync failure nor cleanup is rollback. The removed `fsync_file` helper has no current public implementation; file fsync is performed inside `atomic_write_bytes`.

## Evidence

### Repo-Internal References

- `atomic_write_bytes` owns the current boundary described above. [6]
- `atomic_replace` owns the current boundary described above. [7]
- `_fsync_directory` owns the current boundary described above. [8]

- The process probe and same-target abandoned-temp cleanup retain live, unknown and unremovable writers. [9]
