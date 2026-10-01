# mcp/src/agents_remember/serving/terminal_catalog.py

## Governing Overview

[serving overview](overview.md)

## Purpose

Owns the durable hosted-occupant catalog and structural seat queries. It runs the one-way legacy
catalog migration before strict current parsing. It is also the sole owner of the sweep's unit of
work: `batch()` is the one place that decides whether a catalog file replacement happens at all,
and `list_committed()` is the explicit contention read that never joins an active batch.

## Code Commentary

### Logic

`TerminalCatalog` reads/writes current task-document-and-role rows, looks up the singular running
occupant of a structural seat, and retains replacement/provenance/evidence fields. Reads migrate
legacy rows first and then validate the current model; writers do not emit both schemas.
`active_for_task` consumes the shared incumbent/staged-heir selector.
`DispatchBriefReceiptStore` composes with the catalog atomic storage unit to idempotently bind one
durable inbox receipt to the exact generation and refuse a different second receipt.
Address-bound receipt lifetime is owned by the row transformation: same-seat promotion retains it,
while cross-seat or role movement clears it before this store writes the new row.

`list()` (cit:([`list`], mcp/src/agents_remember/serving/terminal_catalog.py:80-84)) and `get()`
(cit:([`get`], mcp/src/agents_remember/serving/terminal_catalog.py:94-95)) read the instance
SNAPSHOT through `_read_snapshot` (cit:([`_read_snapshot`], mcp/src/agents_remember/serving/terminal_catalog.py:364-375)),
so a same-instance batch exposes its in-memory buffer to them. `list_committed`
(cit:([`list_committed`], mcp/src/agents_remember/serving/terminal_catalog.py:86-92)) is the
deliberate exception: it decodes the last atomically replaced file through the existing read-only
`_read_disk` (cit:([`_read_disk`], mcp/src/agents_remember/serving/terminal_catalog.py:395-420))
and applies the same non-terminated filter as `list()`. It exists so a sweep that lost the
non-blocking sweep lock can still return current catalog state: `_read_snapshot` would wait on the
catalog `RLock` that the winning sweep holds for its whole batch, which is the contended-sweep
stall this operation removes. It adds no cache, alternate parser, lock branch, or optional-method
fallback, and it changes nothing about the ordinary read surface.

`upsert` (cit:([`upsert`], mcp/src/agents_remember/serving/terminal_catalog.py:108-116)) short-circuits
only the exact full-row equality case: exactly one stored row matches the incoming id and compares
equal, so the call returns without mutating the batch or the file. Any changed field — adapter raw
payload, cursors, liveness evidence, failure counts/timestamps, or another observation field —
keeps the row unequal and the write happens. Two or more matching rows (a duplicate-id row) still
take the existing replace-and-append path, so the guard cannot hide duplicate cleanup.

`batch()` (cit:([`batch`], mcp/src/agents_remember/serving/terminal_catalog.py:281-313)) remains the
sole catalog unit of work for a sweep: it reads disk once at begin, routes mutators through the
in-memory buffer (`_read`/`_write`), and in its `finally` performs exactly one atomic
`_write_disk` (cit:([`_write_disk`], mcp/src/agents_remember/serving/terminal_catalog.py:422-431))
only when the buffer is dirty. A clean or empty context therefore performs zero physical
replacements; one or many logical mutations perform one; a body exception after earlier mutations
flushes the dirty partial once and propagates, leaving later rows unobserved and providing no
rollback. Nested batches reuse the outer buffer.

### Conventions

Catalog methods expose runtime ids only as occupant correlations. Topology qualification lives in the
task/structural resolver rather than this persistence class.

### Invariants And Boundaries

- One running occupant may claim a singular task-document-and-role seat.
- Migration is one-way and precedes strict parsing.
- Spawn ancestry remains audit provenance.
- Current writers never restore leaf-key fields.
- A staged heir is current only after the incumbent leaves.
- One generation may bind exactly one pinned dispatch-brief receipt.
- Receipt evidence cannot migrate to another canonical address.
- The catalog is the sole owner of the sweep's batch. No caller adds a second transaction, and the
  batch performs no logical rollback: dirty-partial progress is real durable progress.
- `list_committed()` must keep reading only the last atomically replaced file. Routing it through
  the instance snapshot path would reintroduce the contended-sweep wait it exists to remove.
- The equal-row `upsert` guard changes WHEN a replacement happens, never WHAT a row contains: it
  is exact full-row equality against exactly one matching id.

### Todos

Removal of migration code requires a separately governed durability-epoch decision.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- The catalog queries current occupancy by task document and role through the shared selector. [1]
- One exact generation idempotently binds one durable pinned-brief receipt. [2]
- Legacy rows migrate before strict model parsing. [3]
- The current catalog model owns strict row serialization. [4]
- The explicit contention read decodes the last atomically replaced file and never joins an active batch. [5]
- An exactly-equal single matching row is not rewritten; duplicate ids still take the replace-and-append path. [6]
- One dirty-gated atomic replacement per batch, including dirty-partial flush on a body exception. [7]

### Cross-Repo References

No cross-repository implementation dependency governs this file.

## 260821-CLIVE Execution-Evidence-Safe Compaction

Compaction recognizes task-bound worker and curator rows plus reviewer rows whose recorded spawn
altitude is leaf (including legacy rows with no recorded level) through their current or replacement
task-document ref. Master and sprint reviewers are review-plane seats, not leaf execution evidence.
A terminated leaf-execution row past retention is reclaimable only after its id is
present in the explicit task-registered set. Running, exited, landed, recent, and unregistered leaf
execution rows remain. Thus ordinary retention cannot turn observed execution into “never started.”

## 260831-LOCR-L22 Current Delta — Committed Read, Equal-Row No-Op, Dirty-Gated Batch

Three catalog-local facts are now explicit, and ordinary read semantics are deliberately unchanged:

1. `list_committed()` is the contention read for a sweep that could not take the non-blocking
   sweep lock. It decodes the last atomically replaced file directly and applies the same
   non-terminated filter as `list()`; `list()`/`get()` keep returning the instance snapshot,
   including an active batch buffer.
2. `upsert()` no longer dirties the batch when exactly one stored row with the same id compares
   equal. That is what turns a repeated clean liveness sweep into a zero-replacement sweep, and it
   is why the liveness projections now build the final row before their single upsert.
3. `batch()` keeps its current exception semantics: one dirty-gated atomic file replacement on
   exit, zero when clean, dirty-partial progress flushed once and propagated on a body exception.
   "Single-write batching" is not all-or-nothing logical rollback, and no caller may add one.

Verified against the uncommitted LOCR-L22 candidate (branch `ar/260831-locr-l22`, HEAD
`4bbe2c37b0fa70b07af4ddbc247aeee1f58343b0`); verification metadata stays pinned until closeout
stamps the leaf code commit.
