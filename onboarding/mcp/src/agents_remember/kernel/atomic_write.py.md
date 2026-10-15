# mcp/src/agents_remember/kernel/atomic_write.py

## Governing Overview

[mcp package overview](../../../overview.md)

## Purpose

Publishes one file through a sibling temporary file and a replacement, with explicit file and directory durability steps.

## Code Commentary

On Windows `_fsync_directory` returns without flushing a directory handle. File fsync and atomic replacement remain, but this owner supplies no directory-entry flush there; directory-fsync guarantees below apply where that flush is supported.

Owned atomic publication keeps the temporary descriptor open through rename and directory durability, then records its post-rename identity and payload digest. Pending announcements defer event judgment; failed durability clears the announcement, and a later destination stat never substitutes for the effect's descriptor.


`atomic_write_bytes` writes, flushes and fsyncs its unique sibling temporary file, then calls `os.replace` directly. Its failure handler removes that temporary file, and its `finally` block releases the in-process in-flight mark. After replacement it removes only same-target abandoned temporaries whose writers are proven gone, then fsyncs the destination directory. A live or unknown writer keeps its temporary file; an invalid process number is treated as unknown, and Windows skips this cleanup. Cleanup does not promise that every leftover is removable. [9]

`atomic_replace` separately reports rename failure while the destination retains its previous bytes, or directory-fsync failure after the destination has changed and the source is absent. Neither a post-replacement directory-fsync failure nor cleanup is rollback. The removed `fsync_file` helper has no current public implementation; file fsync is performed inside `atomic_write_bytes`.

### Logic

- `_temp_path_for` — the private temp this module writes before it replaces `path`, named under the same
  hidden-file convention the rest of the package uses.
- `_fsync_directory` — flush `directory`'s own entries so a completed rename survives a host loss.
- `atomic_write_bytes` — publish `payload` at `path`: write the temp, flush it, rename it, then fsync the
  directory, so readers see the old file or the new one and never both.
- `atomic_write_text` — `atomic_write_bytes` for text; the encoding is explicit, never the locale's.
- `atomic_replace` — move an already-written `source` onto `destination` atomically and durably, and fsync the
  destination's parent (and the source's, when they differ). Its two legs fail independently and are now reported
  separately: a failed rename raises `AtomicReplaceError(leg="replace", destination_state="previous-bytes")`,
  because the destination still holds its old bytes and nothing was published, while a failed directory flush
  after a successful rename raises `AtomicReplaceError(leg="directory-fsync", destination_state="source-absent")`,
  because the rename *did* publish the new bytes and only their durability is missing.

### Conventions

- Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.
- The module owns no policy: it never decides *what* to write, only how a write becomes visible and durable.

### Invariants And Boundaries

- **A reader never sees a partial file.** Every publish is a rename of a fully written, flushed temp onto the
  destination.
- **The directory fsync still runs after `os.replace`, and the resulting window is now named instead of merged.**
  A failure between the rename and the directory flush is no longer reported as a bare replace failure: each leg
  raises `AtomicReplaceError` carrying the leg (`replace` / `directory-fsync`), the destination path and the
  destination's state at the moment of the raise (`previous-bytes` / `source-absent`), so a caller can tell
  "nothing moved" from "the rename happened and the flush failed". The published consequences of the window are
  unchanged and remain a **caller-side** matter — a create can still answer `destination_occupied` when the
  destination is in fact the complete candidate it just created, and a publication can still return
  `publication_failed` where `publication_durability_unconfirmed` would be the more precise code; the module's
  ordering is what makes the ordinary case atomic, and it was not reordered. The observation came from `KS-R04`'s
  reviewer and the label was added by the `KS-R23` defect repair.
- **Boundary.** `atomic_replace` reports its failed rename/directory-fsync legs as `AtomicReplaceError`, which subclasses **both** the domain
  family (`AgentsRememberError`) and `OSError`, so an existing `except OSError` around a publish keeps observing
  the failure it always did; the caller owns the refusal code. It never decides whether a failed publish should be
  retried, and it never deletes or repairs a destination.

### Todos

None recorded for this slice. The post-rename fsync window is a disclosed limitation with a caller-side remedy,
not a scheduled repair: changing the ordering would trade a rare misreport for a non-atomic publish. Its
*labelling* half is no longer outstanding — `atomic_replace` now raises `AtomicReplaceError` naming the failed
leg and the destination's state, so the window is reportable without being reordered.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References




### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.

- `atomic_write_bytes` owns the current boundary described above. [6]
- `atomic_replace` owns the current boundary described above. [7]
- `_fsync_directory` owns the current boundary described above. [8]
- The process probe and same-target abandoned-temp cleanup retain live, unknown and unremovable writers. [9]
- - The private temp this module writes before it replaces `path`. [10]

- The directory flush runs where supported; on Windows this helper returns without flushing a directory handle. [11]

- - Atomic byte publication replaces the destination only after writing its temporary content; readers see the prior or replaced file. [12]
- - The atomic move of an already-written file onto a destination. [13]
