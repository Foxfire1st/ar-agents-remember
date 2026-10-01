# mcp/src/agents_remember/memory/knowledge/candidate_workspace.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

One candidate's local working state: **creation, resumption, cloning and disposal authority**.

A candidate is a *directory* holding one writable SQLite database, the immutable receipt that binds it to its
admission, and the database's own resource lock. An operation that owns the candidate may add its own local
record beside those two — the curator ingest writes the identities it has allocated into
`curator-allocation-journal.json` there — because that is the same kind of fact the receipt is: a local,
operation-scoped record of what this candidate is, never knowledge the repository holds. The layout is fixed,
not the file count: what `models/knowledge/snapshot.py` pins is which file is the working database, and a
sibling record an owner writes does not move that answer. That layout is fixed by `models/knowledge/snapshot.py` so the
admission that opens the candidate for writes and the publication that reads it cannot disagree about which file
is the working database — and so no absolute path is ever stored as knowledge.

Four properties are load-bearing:

1. **Two-phase creation.** The database and the receipt are built in a private staging directory and verified
   there; only then is the complete directory exposed at the admitted destination. A half-created candidate
   therefore never appears at the path a later lease would open.
2. **An existing destination is a resume attempt.** Creation refuses an occupied destination; the resume path
   reopens the same database, retains its journal/WAL state and verifies the receipt against the admission instead
   of overwriting the unpublished work it holds.
3. **A clone comes from a closed snapshot.** Cloning copies a *closed* representation produced by the same freeze
   procedure publication uses, so a clone can never inherit a WAL-dependent main file from the database it started
   from.
4. **Disposal is a verdict, not a deletion.** This module decides whether the authored work is provably retained
   or explicitly discarded; removing the directory belongs to the enclosure owner that already owns cleanup.

## Code Commentary

### Logic

**The two-phase creation path** (`_two_phase_create`, used by both `create_candidate` and `clone_candidate`).
An occupied destination is refused first (`_occupied_refusal` → `destination_occupied`, worded as "a resume
attempt rather than a creation target"). A private sibling directory is created (`_stage_directory`, named with
the pid and a uuid so two creators cannot collide), the builder produces the candidate inside it, then
`_expose_candidate` verifies the staged database, seals the receipt and installs the complete directory. A builder
that returns a refusal aborts before anything is exposed, and the `finally` removes the private directory unless
the expose succeeded. `created` is only ever reported after a **readback** through the ordinary resume path
(`_read_candidate`), so the reported identity and receipt are the ones a later open would see.

- `_build_empty_candidate` creates the declared schema and the repository row in the stage.
- `_build_cloned_candidate` opens the selected baseline, requires it to carry a repository row, and calls
  `freeze_closed_snapshot` into the stage's candidate database. The admission's namespace is enforced where the
  receipt is sealed, so a baseline bound elsewhere is refused with `candidate_binding_changed` rather than copied
  and relabelled. **No filesystem lock is taken on the baseline**: SQLite's own read transaction is what makes the
  copy consistent, a baseline that moved while it was frozen is caught by the identity comparison rather than
  serialized against, and a lock file beside a published snapshot would land inside a directory whose contents are
  captured as memory.
- `_expose_candidate` is the ordering that makes "created" honest: it reads the staged database
  (`_read_staged_candidate`: schema, namespace and identity from the database itself), builds the receipt from
  **those observed facts**, writes and reads it back, flushes the database with `fsync_file`, and only then
  `atomic_replace`s the stage onto the destination. A failure in the receipt/flush group returns
  `snapshot_incomplete` with nothing exposed — a candidate whose durability step failed can never be read back as
  created — while the expose itself reports `destination_occupied` (something appeared there after all) or
  `publication_failed`.

**The read and disposal paths.**

- `_read_candidate(operation, destination)` is the shared verification: both candidate inputs must be present
  (`_candidate_inputs` → `selected_input_unavailable` naming the exact missing file), the database opens
  (`_open_for_verification` maps `candidate_busy`, `unsupported_schema` and an unreadable file onto typed
  refusals), the receipt is compared with the admission (`_receipt_denial` → `receipt_binding_refusal`), and the
  identity is read from the live database. `open_candidate` is this path — the restart and branch-switch entry
  point — and it repairs and deletes nothing: the last committed batch is read straight out of the database
  through whatever journal or WAL state SQLite needs to recover.
- `authorize_candidate_disposal` is deliberately narrow. A `discard` disposition must name the identity the
  candidate holds **now**, so an authorization written for an earlier state cannot be replayed against newer
  unpublished work (`_disposal_identity_refusal` → `stale_precondition`). A `published` disposition must point at
  a database that reopens to that same logical identity (`_published_identity_refusal`), verified through a
  read-only connection — a stale published snapshot, a loose object or a successful read does not establish that
  no unique authored data remains. The result is a verdict (`disposable` with the identity it verified), not an
  action.

`_close_without_discarding_peers` closes the connection and leaves SQLite's own recovery files exactly where they
are. It is the same thing `OpenedKnowledgeStore.close` does today (that method no longer unlinks WAL/SHM peers),
and the helper exists so a later change to that method cannot quietly reintroduce an unlink underneath the
lifecycle without a test noticing.

### Conventions

- Every failure that a caller can act on is a **typed refusal returned inside the result**; `_refused` refuses a
  missing refusal value as a defect, so "refused with no reason" is not representable.
- `KnowledgeRefused` is raised internally where a helper deeper in the stack (the freeze procedure) needs to
  unwind, and is caught at the boundary and turned into the same typed result shape.
- Stage directories are this operation's own temporary output; `_discard_private_directory` removes only the
  directory this call created, with `ignore_errors=True` so cleanup cannot replace the caller's refusal.

### Invariants And Boundaries

- **A candidate is published only through its own directory.** Both write and publication derive their paths from
  the admitted candidate, so no caller can write into one database and publish another.
- **Creation never touches an occupied destination.** Refusing is the whole mechanism that keeps unpublished
  authored work from being overwritten by a routine re-run.
- **The receipt is derived from the database that exists**, never from the admission alone.
- **Nothing here deletes a journal or WAL peer of a real database.** Disposal is a verdict; the only files removed
  are a private stage this operation created and the stage's own peers (in the freeze procedure).
- **The layout is fixed elsewhere.** Both file names come from `models/knowledge/snapshot.py`; this module derives
  paths and never spells one out.
- **Boundary.** This module owns the candidate's local lifecycle. It does not publish a snapshot, take a
  destination lock, decide authority, or remove a candidate directory.

### Todos

None recorded for this slice. The disposal verdict names the enclosure owner as the remover by design; a leaf that
wants automatic reclamation should add it there rather than here.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The four public operations this module owns. [1]
- The two-phase creation and the ordering that makes `created` honest. [2]
- The empty-schema builder and the baseline clone that reuses the publication freeze. [3]
- The expose step: verify staged database, seal and read back the receipt, flush, then install. [4]
- The shared verification path a resume and a disposal both take. [5]
- The two narrow disposal grounds, each naming the identity it was measured against. [6]
- The occupied-destination refusal and the private stage directory. [7]
- The close that deliberately leaves SQLite's own recovery files in place. [8]
- The receipt write/read/binding comparison this lifecycle depends on. [9]
- The freeze procedure a clone reuses, and its closed-file guarantee. [10]
- The result vocabulary these operations return. [11]
- The new refusal codes the lifecycle introduced, including the honest durability code. [12]
- The nodes that protect the lifecycle's load-bearing behaviours. [13]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
