# mcp/src/agents_remember/kernel/atomic_write.py

## Governing Overview

[mcp package overview](../../../overview.md)

## Purpose

Publish file content atomically through the package's single owner. It is the one module in the repository that
knows how to make a *name* change visible all at once, and it is used by the memory ledger, the task documents, the
onboarding writer and — since `KS-R04` — the knowledge snapshot publication.

## Code Commentary

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
- **`fsync_file`** — the file-data half of that contract, exposed by `KS-R04` for a producer that writes a file
  through **another owner**. A database that closes its own handles, for instance, still has to reach stable
  storage before a rename publishes it: the directory fsync in `atomic_replace` records that the new *name* exists
  and says nothing about the bytes the name points at, so one does not substitute for the other. The helper opens
  the path read-only and fsyncs its descriptor, which is why it can be used on a file this package did not write.

### Conventions

- Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.
- The module owns no policy: it never decides *what* to write, only how a write becomes visible and durable.

### Invariants And Boundaries

- **A reader never sees a partial file.** Every publish is a rename of a fully written, flushed temp onto the
  destination.
- **The two fsyncs are not interchangeable.** `_fsync_directory` makes the *name* durable; `fsync_file` makes the
  *bytes* durable. A caller publishing a file it wrote through another owner needs both.
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
- **Boundary.** This module reports a failed publish as `AtomicReplaceError`, which subclasses **both** the domain
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

- The private temp this module writes before it replaces `path`. [1]
- The directory flush that makes a completed rename survive a host loss. [2]
- The one atomic publish: readers see the old file or the new one, never both. [3]
- The atomic move of an already-written file onto a destination. [4]
- **The file-data flush this leaf exposed, for a producer that wrote the file through another owner.** [5]
- The producer that needs it: a closed snapshot stage whose bytes must reach stable storage before the rename publishes the name. [6]
- The receipt write that goes through this module's atomic byte publish. [7]
- The install whose failure is reported as a replace failure. [8]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
