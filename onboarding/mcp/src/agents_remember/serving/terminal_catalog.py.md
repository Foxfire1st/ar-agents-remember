# mcp/src/agents_remember/serving/terminal_catalog.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `mcp/src/agents_remember/serving/terminal_catalog.py`        |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated | 2026-09-10T09:30+02:00 |
| lastVerifiedCommitHash | `a5c29cb63dcb6f0d1ca32d0cf7822457df43cfa4`|
| lastVerifiedCommitDate | 2026-09-11T18:44:06+02:00|
| governingOverview      | `overview.md`                                               |

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

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The catalog queries current occupancy by task document and role through the shared selector. | `active_for_task` | mcp/src/agents_remember/serving/terminal_catalog.py:97-106 |
| One exact generation idempotently binds one durable pinned-brief receipt. | `DispatchBriefReceiptStore` | mcp/src/agents_remember/serving/terminal_catalog.py:434-460 |
| Legacy rows migrate before strict model parsing. | "rows = migrate_terminal_catalog_v1(self.path.parent.parent.parent, rows)" | mcp/src/agents_remember/serving/terminal_catalog.py:411-411 |
| The current catalog model owns strict row serialization. | `TerminalCatalogEntry` | mcp/src/agents_remember/models/terminal_catalog.py:68-571 |
| The explicit contention read decodes the last atomically replaced file and never joins an active batch. | `list_committed` | mcp/src/agents_remember/serving/terminal_catalog.py:86-92 |
| An exactly-equal single matching row is not rewritten; duplicate ids still take the replace-and-append path. | `upsert` | mcp/src/agents_remember/serving/terminal_catalog.py:108-116 |
| One dirty-gated atomic replacement per batch, including dirty-partial flush on a body exception. | `batch`; `_write_disk` | mcp/src/agents_remember/serving/terminal_catalog.py:281-313; mcp/src/agents_remember/serving/terminal_catalog.py:422-431 |

## Cross-Repo References

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

## Update History

- 2026-09-10T09:30+02:00 — 260831-LOCR-L22 curator: recorded the committed-snapshot contention read,
  the exact-equal single-row `upsert` no-op guard, and the dirty-gated zero-or-one batch replacement
  contract; repaired the moved `active_for_task`, `DispatchBriefReceiptStore`, migration, and
  `TerminalCatalogEntry` citations. Verification metadata remains pinned until closeout.
- 2026-08-31T04:59+02:00 — 260821-ARSPAWN-L5 independent-review repair: bounded execution-evidence
  compaction to worker/curator and leaf-altitude reviewer generations rather than treating every
  polymorphic reviewer as leaf execution. Verification remains closeout-owned.

- 2026-08-26T16:03+02:00 — Post-failure repair: extracted dispatch-receipt mutation into
  `DispatchBriefReceiptStore`, preserving the same atomic catalog storage boundary while returning
  `TerminalCatalog` to the 15-operation surface cap. Verification remains closeout-owned.


- 2026-08-25T23:19+02:00 — Contract-wide citation curation: re-read the current anchored claim(s), retained the supported wording, and cleared verification metadata for closeout-owned restamping.

- 2026-08-25T22:27+02:00 — 260821-ARSPAWN-L2 final curation: clarified one-receipt idempotency
  and the prohibition on carrying address-bound proof across a document or role move. Verification
  remains closeout-owned.

- 2026-08-25T19:51+02:00 — 260821-ARSPAWN-L2: current-seat lookup now recognizes the staged heir
  after incumbent exit, and the catalog owns idempotent pinned-brief receipt binding. Verification
  remains closeout-owned.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: recorded task-registration gating for terminated leaf-seat reclamation. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-11T14:29+02:00 — Re-read the current `TerminalCatalogEntry` model used by this store
  and widened its citation to include the dataclass declaration; verification metadata remains
  unchanged for governed closeout.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: rewrote after the row vocabulary moved to
  `models/terminal_catalog.py`; preserved the batch/compact/atomic-write store knowledge from the
  pre-split card. Verification metadata pinned until closeout stamps the L9 code commit.
