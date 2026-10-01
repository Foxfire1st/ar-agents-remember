# mcp/src/agents_remember/memory/knowledge/publication.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Install one closed snapshot at an admitted destination, **atomically and verifiably**.

The destination is a *file other readers open*: a memory tree is captured from it, a reader reopens it, and Git
may commit it. Two consequences shape the module:

1. **Publication is replace-or-nothing.** The install is the repository's atomic replace of an already-written,
   already-flushed stage, so a reader sees the previous snapshot or the new one and never a partial file. Any
   failure before the replace leaves the previous destination exactly as it was, and the private stage is removed.
2. **A no-op does not rewrite bytes.** When the destination already holds the same logical dataset — the same
   records, whatever its SQLite page layout happens to be — the existing bytes are retained and `no_change` is
   returned. Page layout is not knowledge, and rewriting the file would dirty a tree for a reason no reader could
   observe in the data.

## Code Commentary

### Logic

`publish_candidate_snapshot(destination, request)` is the composed entry point:

1. **Re-verify the candidate** by opening it through the ordinary lifecycle path (`open_candidate`). A refusal, or
   an identity that is not the one the publication was admitted against, is returned as a refusal — the identity
   branch is `stale_precondition` naming both digests (`_stale_candidate_refusal`), because "a fresher candidate is
   never published silently in place of the selected one".
2. **Freeze under the candidate's own lock** (`_freeze_under_candidate_lock`). The candidate store is opened, its
   single resource lock taken, the frozen stage produced by `freeze_closed_snapshot`, and the lock released. Every
   way the frozen point can fail to be produced — the stage directory, the copy, the verify, the flush — arrives
   as a typed refusal (`snapshot_incomplete`, or the freeze's own `stale_precondition`), so `publication_failed` is
   reserved for a failure of the **install**.
3. **Install under the destination's own lock** by delegating to `publish_prepared_snapshot`.

The stage directory is private and beside the destination (`_private_stage_directory`, a `mkdtemp` named
`.<destination>.*.stage`), and `_discard_stage_directory` removes it on the way out of both success and failure —
a removal failure is suppressed there so it cannot mask the refusal that says why the publication did not happen.

`publish_prepared_snapshot(prepared, request)` is the reusable half: a caller that produced a validated closed
database — a merged result, an import, a restored artifact — reaches the destination through exactly this path.
It re-reads the stage and refuses `snapshot_incomplete` if the stage is gone or is **not the file that was frozen
and verified** (its physical digest is re-checked against `PreparedKnowledgeSnapshot.file_digest`), then takes the
destination lock and installs.

`destination_observation(destination_path)` is the public **admission** reading, and it is deliberately not the
authority for a replace. It answers what one destination holds right now, without writing or locking it, so an
operation can refuse an occupied or unexpected destination *before* it does expensive work and can name what it
found. Publication takes its own reading again under the destination lock, and **that locked reading is the one
that decides** — a dataset that moved between the two is caught there.

`_install` is where the destination contract lives:

- `_observe_destination` reads the destination's identity **without writing it**; an unreadable destination is a
  `destination_stale` refusal naming what could not be read.
- `_matches_expected` compares the observation with `expected_destination` exactly — `None` means "expected to be
  absent" and matches only absence, so a file the caller never admitted is never overwritten.
- An identical logical dataset is the `no_change` outcome: the stage is discarded and the **existing bytes are
  retained**.
- Otherwise `atomic_replace` installs the stage, and `_readback` reopens the destination and reports what is
  actually there: `published` with the installed identity and the `previous_identity` it replaced, or a refusal
  (`publication_failed` when the installed file carries a different identity,
  `publication_durability_unconfirmed` when the replacement completed but the destination could not be re-read).

**Two locks, never nested.** The candidate lock protects the working database and is released before the
destination lock is taken; the destination lock protects the file being replaced. The lock resource is the
destination's hidden stem (`_publication_lock_resource` → `exclusive_file_lock` derives
`.<published-name>.lock`), so the lock file is **colocated with the resource it excludes** — a lock keyed anywhere
else would let two processes disagree about which resource they are excluding. Deleting that file on close is
**not** a cleanup: it is the live `flock` resource, and removing it while a publication holds it would let the
next publication take an unheld lock.

### Conventions

- Every failure path returns a typed refusal; `LockCapabilityError` from the lock primitive and an `OSError` from
  taking the lock both map to `lock_capability_unavailable`, because a publication that cannot prove exclusion must
  not proceed.
- `_render_identity` renders an absent destination as `<absent>` in facts, so `expected`/`observed` always carry a
  value.
- Private helpers are prefixed `_` and the two public functions are the only surface other modules import.

### Invariants And Boundaries

- **A refusal never replaces the destination.** Every refusal path leaves the previous file exactly as it was, and
  the honest code for "the replacement completed but could not be confirmed" is
  `publication_durability_unconfirmed`, not `publication_failed` — the two tell a caller different things about
  what is on disk.
- **`no_change` is a retained-bytes outcome**, decided on the **logical** digest rather than on bytes or mtime.
- **The destination lock is a live `flock` resource beside the destination.** It is never deleted, and it is the
  one file a captured memory tree will contain besides the snapshot itself — **because the destination's own
  directory is a published location, not a workbench**: the portable import stages its database in a private
  temporary directory and installs it by atomic replace, so the destination directory holds the published file
  and this lock and nothing else. Whether a memory-tree *capture* of a destination directory enumerates files or
  the directory is **L4's open question Q1**, carried forward rather than answered here.
- **A published snapshot carries knowledge only while the exact code/memory inputs in the candidate receipt and
  the caller's resolved context live.** The publication moves a database, not a binding: the receipt's inputs and
  the consumer's context are what make the published bytes meaningful at a point in time.
- **Boundary.** This module installs a file. It does not decide when a publication is authorized, does not commit
  anything to Git, and does not compare the published dataset with a consumer's expected context — that comparison
  is `materialization.publication_state`.
- **A publication into a converted memory tree is refused `database_frozen` (L37, MIK-R37 rule 3).**
  `publish_prepared_snapshot` asks `frozen_database_refusal(request.destination_path)` before the stage checks:
  when the destination's directory holds `knowledge/layout.json`, the result is a refusal whose next action is
  `FILE_WRITER_ROUTE` (`knowledge-ingest`, or `knowledge-bootstrap --wave`). This is the one install sink, so
  ingest, bootstrap, import and merge are all covered, and the frozen `knowledge.sqlite` stays in place,
  unwritten, until MIK-R26 removes it. The three stage checks moved unchanged into `_stage_refusal`.
  `frozen_database_refusal` is a realization of INV-1XKX9ERN.

### Todos

None recorded for this slice. One disclosed limitation is carried by `kernel/atomic_write.py.md` rather than
silenced here: the directory fsync runs **after** `os.replace`, so a failure in that window is reported as a
replace failure — which is why a create can answer `destination_occupied` for a destination that holds the
complete candidate it just created, and why this module can return `publication_failed` where
`publication_durability_unconfirmed` would be the more precise code.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The composed publication entry point, including its identity re-check and lock ordering. [1]
- The reusable install half and its stage-digest re-check. [2]
- The install: observe without writing, compare exactly, retain on `no_change`, replace, then read back. [3]
- **The public admission reading this leaf added, which never decides a replace — the locked reading does.** [4]
- The readback that decides between `published`, `publication_failed` and the honest durability code. [5]
- The destination-stale refusal and the candidate-moved refusal, each naming both digests. [6]
- The candidate lock that protects the working database, released before the destination lock is taken. [7]
- The private stage directory, its cleanup and the suppression that protects the caller's refusal. [8]
- The hidden lock resource that lands `.<published-name>.lock` beside the destination. [9]
- The freeze procedure behind the stage, and the stage shape it returns. [10]
- The atomic replace whose directory fsync records the new name, not the bytes under it. [11]
- The read-only dataset identity every comparison in this module uses. [12]
- The publication outcome vocabulary and the destination request. [13]
- **The second caller of the admission reading: the portable import's destination check, which runs before any staging work.** [14]
- The nodes that protect the publication's failure behaviour. [15]

- A database destination inside a converted memory tree is refused, naming the file writer. [16]
- The publication asks the freeze first, then the stage checks. [17]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
