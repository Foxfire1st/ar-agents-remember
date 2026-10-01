# mcp/src/agents_remember/serving/structural_dispatch.py

## Governing Overview

[Serving overview](overview.md)

## Purpose

Provides cross-process per-seat dispatch serialization and durable pinned-brief evidence reads.

## Code Commentary

### Logic

`exclusive_structural_dispatch_lock` hashes repository, task path, and role into one of 4,096 stable
stripes. A reclaimed process-local keyed lock composes threads, while `fcntl.flock` holds the
stripe's lazily created zero-length runtime file across spawn plus brief publication.
`pinned_dispatch_brief` finds the one exact brief for the private current occupant. The viability
and status helpers translate durable inbox state into a convergent structural result.

### Conventions

The lock identity is canonical structural identity. The hashed stripe and its runtime file are
private mechanics, not a public seat address or recovery record.

### Invariants And Boundaries

- Different canonical seats normally remain concurrent; there is no repository- or process-global lock.
- Process death releases the whole-file stripe lock; catalog and inbox evidence, not the lock
  artifact, drive recovery.
- The 4,096-stripe namespace fixes the filesystem upper bound; the process lock map contains only
  live holders/waiters and reclaims the key after they drain.
- A hash collision may serialize unrelated seats but cannot merge their durable state. Stripe files
  remain until runtime/coordination teardown because unlinking a live file could split lock generations.
- Only lock path/open/acquisition failures become `StructuralDispatchLockError`; downstream
  transaction I/O retains its own failure family. There is no fallback that would provide false
  cross-process safety.
- More than one exact-pinned brief for one generation is ambiguous and fails closed.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

- One bounded process-plus-POSIX lock path linearizes only the addressed seat transaction. [1]

### Repo-Internal References

- Pinned-brief lookup binds the inbox row to document, role, and private occupant. [2]
- Viability and status are derived from durable inbox state. [3]

### Cross-Repo References

No cross-repository dependency governs this unit.
