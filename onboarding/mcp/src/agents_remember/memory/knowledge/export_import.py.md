# mcp/src/agents_remember/memory/knowledge/export_import.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The export and import operation**: encode one admitted dataset as its complete portable artifact, and
install such an artifact at an admitted destination — or refuse, with the destination untouched.

Three decisions shape the whole sequence, and each exists because the step before it cannot see what it
prevents: **validation before any database work**, **a private stage that is never the destination**, and
**publication on exact digest equality through L4's prepared-snapshot protocol**.

## Code Commentary

### Logic

`export_knowledge_dataset(request)` re-reads the dataset's identity **before** anything is encoded. A
dataset that moved between the caller's admission and the read is `stale_precondition` naming both
digests, rather than an artifact describing a dataset nobody selected. It encodes through
`export_envelope` + `encode_export` — the one encoder — and returns `ExportResult` carrying the artifact
text, the format, the identity and the artifact digest. **The encoder has no filesystem side effect at
all**: `artifact` is returned as a string and a caller that wants it on disk writes it through the
repository's own atomic write.

`import_knowledge_dataset(request)` runs one ordered sequence:

1. **`parse_export` then `validate_export`** — document shape, manifest, the whole-document canonical gate,
   the header check, then declared column order/types, primary-key uniqueness, namespace binding and the
   recomputed seal. An artifact that fails any of them **never reaches a database**, so a malformed
   document cannot leave a half-written stage for a later step to mistake for progress.
2. **Destination admission before any staging work** (`_destination_refusal`, through
   `publication.destination_observation`). `expected_destination` is a closed choice in effect: `None`
   means "the destination is expected to be absent", so an occupied destination is `destination_occupied`
   rather than replaced; an explicit identity means "expect exactly this", so an absent destination is
   `destination_absent_refusal` (`destination_stale`) rather than a silent fresh install. There is no
   third mode, and the reading here is an **admission** reading — the locked reading inside publication is
   the one that decides.
3. **A private stage** (`_private_stage_directory`, a `tempfile.mkdtemp` **outside** the destination's
   directory, because the destination directory is a published location and not a workbench):
   `_stage_imported_dataset` creates the schema from the manifest (never from the artifact), loads every
   canonical row in declared manifest order inside one `BEGIN IMMEDIATE` with the declared foreign keys
   **deferred to commit**, and closes.
4. **The staged verification** (`_verify_staged_dataset`), which is the same set of checks a normal store
   open performs and then some: `PRAGMA foreign_key_check` read directly rather than inferred from a
   successful commit; **the sealed aggregates** re-derived per retained revision; the typed aggregates
   read back through the canonical logical body; and the whole dataset's logical digest recomputed from
   the reopened file and compared with the artifact's.
5. **`require_closed_database(stage, identity)`** — the shared close-and-prove step the freeze also calls,
   so a stage opened in WAL mode is published as a closed delete-mode file with no peer. Then `fsync_file`,
   and `PreparedKnowledgeSnapshot` is handed to **`publish_prepared_snapshot`**, which takes the
   destination's lock, retains the existing bytes when they already hold this knowledge, and re-reads the
   installed file before reporting success. **Import owns no second install path and never patches a live
   database in place.**

**The staged sealed-aggregate read is the check this leaf's review made load-bearing.** `payload_digest` is
a canonical column of both revision tables, so it crosses the artifact boundary as ordinary text and
nothing about parsing the document establishes it. `_sealed_aggregate_refusal` re-derives every retained
revision's payload through the **shared** decoders in `records.py` (`decode_revision_row`,
`decode_family_revision_row`, with `decode_predecessor_rows` supplying the edges) and refuses with
`relationship_constraint` when the recomputed digest is not the stored one. Without it the one
row-internal identity this schema promotes to a stored column would be the one the import published
unchecked, and the resulting file would be one this package's own decoder and merge validation call
damaged.

**What this operation never does**, stated because a reader of the artifact will look for it: it does not
regenerate or renumber an identifier, infer missing provenance, manufacture an `accepted` state, restore a
Git commit, resolve an external source object, or claim anything about a second backend. `state_at_origin`
and `acceptance_ref` cross as the stored text they are — importing a row that says `accepted` imports that
*value*, and the receiving context grants it no authority. A dataset restored from an artifact is
knowledge, not history.

**Lock policy: one resource lock at a time, never nested.** Export takes no lock (it reads through a
connection reopened for the selected dataset). Import takes no lock while it stages or validates, because
the stage is private; the destination's lock is taken by the publication operation and released with it.

### Conventions

- Every failure is a typed refusal **inside** the result. Neither function raises `OSError`, `apsw.Error`
  or `ValueError` for a caller to catch; the two operations are named by `EXPORT_OPERATION` /
  `IMPORT_OPERATION` and by the `KnowledgeOperation` members of the same names.
- `read_artifact(path) -> str | KnowledgeRefusal` is the file-reading half, and its two failures are
  different facts with different codes: a path that cannot be read at all is
  `selected_input_unavailable` (answering it with an empty document would be the "absent selection reads
  as no knowledge" confusion this package refuses everywhere else), while bytes that are **not UTF-8** are
  `invalid_export`, because a portable artifact is UTF-8 by construction and decoding strictly is what
  keeps a malformed file from being read through a replacement-character guess. **Nothing on this boundary
  raises** — no `OSError`, no `UnicodeDecodeError`.
- Typed JSON columns are stored through `records.encode_typed_column`, the same encoder every other write
  in this package uses — not a convenience: it is what makes "the value that was validated" and "the text
  a later read decodes" the same value rather than a second spelling the store would have to accept.
- `_binding`'s `isinstance` guard is **defence in depth**: the row reader refuses every value this branch
  would refuse, one step earlier, so a weakened mutation of this guard leaves the suite green. The source
  says so at the guard rather than leaving it to be read as coverage.
- `_private_stage_directory` returns a fresh directory per import; `_discard` removes the stage database
  and any journal peer of it, then the directory, on the way out of both success and failure.

### Invariants And Boundaries

- **A refusal publishes nothing, and a partially imported dataset is not an observable state.** Every
  refusal path leaves the destination byte-identical, with no staging directory surviving beside it. The
  evidence measures all three: the destination's file digest, the row counts, and the destination
  directory's contents.
- **The destination holds the published database *and* L4's lock resource.** `.<name>.lock` is created
  beside every destination and is never unlinked by design, because it is the live `flock` resource rather
  than a leftover. **L4's open question Q1 is carried forward rather than answered here**: whether a
  memory-tree *capture* of a destination directory enumerates files or the directory is L4's decision, and
  this leaf does not change the lock.
- **The declared identity is proven, not asserted.** `verified_identity` is carried independently of the
  result state, so a validated artifact whose publication was refused still names the identity it
  verified; and `ImportResult` refuses at construction a destination whose logical digest differs from the
  verified one.
- **The import is addressed at a dataset, and the destination at an admission.** A stale caller is told
  rather than obeyed on both sides.
- **Boundary.** This module is the operation. It does not decide authority, does not commit anything to
  Git, writes no ledger row, and does not own the format (`export_portable.py`), the refusal vocabulary
  (`export_refusals.py`) or the publication protocol (`publication.py`).

### Todos

None recorded for this slice. Three carried observations belong to the owning seat rather than to a defect
here: the `destination_occupied` choice for an occupied destination with no admitted identity is a policy
decision (the storage design names no code for that fact and the vocabulary already declared this one);
the staged digest equality is a **documented non-experiment** (see below); and the two unreachable
postconditions are kept and disclosed rather than removed.

**The staged digest equality cannot be falsified by a black-box case, and that is stated rather than
implied.** `_verify_staged_dataset` compares the staged file's recomputed `logical_digest` with the
identity the artifact declared; removing that comparison leaves every case green and always will, because
the rows loaded into the stage are the rows `validate_export` already proved produce that digest, loaded
through the store's own canonical encoder and read back through its own decoder. It is retained because it
is the check the requirement names and the only guard against a future loader that stored something other
than what it validated. The foreign-key read in the same function is reachable only on a stage damaged
with enforcement off, because the deferred foreign keys refuse a dangling row at commit; the direct-probe
assertion in the same case exercises the read.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The module's three shaping decisions and the never-does list, in the form a consumer may rely on. [1]
- The two operation names a caller branches on. [2]
- **The export: the identity re-read that makes "the artifact I produced is the dataset I admitted" checkable, and the encode through the one encoder.** [3]
- **The import sequence: validate, admit the destination, stage, verify, close, publish.** [4]
- The value-or-refusal file reader and its two different codes (`selected_input_unavailable` for unreadable, `invalid_export` for non-UTF-8). [5]
- The refusal for a dataset that moved between admission and export. [6]
- **The destination admission before any staging work, with its three states and no third mode.** [7]
- The private stage: schema from the manifest, one deferred-FK transaction, declared manifest order. [8]
- **The staged verification: foreign-key read, sealed aggregates, typed aggregates and the recomputed identity — including the documented non-experiment.** [9]
- **The staged sealed-aggregate read that the review made load-bearing: every retained revision's payload re-derived before publish.** [10]
- The outcome rendering, including the independently carried verified identity. [11]
- The single shared "prove this finished file is a closed database" step both producers call. [12]
- The publication protocol every install goes through, and the admission reading the destination check uses. [13]
- The shared decoders the sealed check owns the seal through, and the typed-column encoder the load uses. [14]
- The reader, encoder, envelope builder and validator this operation composes rather than re-implements. [15]
- The refusal vocabulary of this boundary, one factory per observable failure point. [16]
- **The node that proves an artifact whose sealed payload contradicts its digest is refused before publish, over both revision tables.** [17]
- **The node that proves destination admission refuses before any staging work, with every state's own code.** [18]
- The nodes that prove a successful import leaves no stage journal or peer behind, and that a refused import preserves the destination byte-for-byte. [19]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The artifact may travel between machines, but
nothing on this path reads a second repository, resolves a Git object or writes a ledger row.

No meaningful cross-repo references found.
