# mcp/src/agents_remember/serving/terminal_catalog.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `mcp/src/agents_remember/serving/terminal_catalog.py`        |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-08T14:38+02:00                                      |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                  |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[serving overview](overview.md)

## Purpose

`serving/terminal_catalog.py` is the durable JSON catalog store for dashboard-owned terminal and
harness sessions. 260731-EFA-L9 moved the row vocabulary (`TerminalCatalogEntry`, its literals and
pure parsers) to `models/terminal_catalog.py`; this module now owns the store only — path
resolution, cross-process locking, atomic writes, batch unit-of-work, compaction, and the
liveness probe recording loop.

## Code Commentary

### Logic

`terminal_catalog_path` (cit:([`terminal_catalog_path`], mcp/src/agents_remember/serving/terminal_catalog.py:42-42)) resolves the catalog file under the
coordination root. "class TerminalCatalog:" (cit:(["class TerminalCatalog:"], mcp/src/agents_remember/serving/terminal_catalog.py:48-48)) holds the cross-process file lock and
instance `RLock` across the complete batch body: `batch()` is a read-once/write-once unit of
work for full-catalog sweeps and session-open transactions. Same-thread mutators re-enter safely;
another request thread cannot see the process-wide batch buffer. Other catalog instances may read
only the last atomically committed file while a batch is in flight. `compact()` reclaims aged
`terminated` tombstones (`TERMINATED_RETENTION_SECONDS = 86400`) while preserving running, exited,
and landed/archive rows; landed cleanup remains an explicit manual path.

`record_liveness_probe` persists probe outcomes into the row through the moved copiers, so a
daemon restart cannot erase hysteresis progress. Writes go through the kernel atomic-write helper
and the dedicated `terminal_catalog_lock` module, keeping readers lock-free against unique-temp
atomic replace.

### Conventions

- Store-only: row shape, literals, and parsing live in `models/terminal_catalog.py`; do not
  reintroduce row vocabulary here.
- Everything slow/sweep-like goes through `batch()`; single-row mutations go through the same
  lock path so readers never observe a half-written catalog.

### Invariants And Boundaries

- The module must not import the conversation package (layering rail enforced; the row vocabulary
  is the shared seam).
- A `terminated` row is never revived; a `landed` row is preserved by liveness sweeps and only
  explicit cleanup retires it.

### Todos

No known follow-up in this file.

## Docs References

No external/domain documentation is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The row vocabulary and liveness config are imported from the models package. | "class TerminalCatalogEntry:" | mcp/src/agents_remember/models/terminal_catalog.py:68-68 |
| The exclusive catalog lock guards the store's cross-process mutations. | `exclusive_terminal_catalog_lock` | mcp/src/agents_remember/serving/terminal_catalog_lock.py:12-12 |

## Cross-Repo References

No cross-repository implementation governs this store.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: rewrote after the row vocabulary moved to
  `models/terminal_catalog.py`; preserved the batch/compact/atomic-write store knowledge from the
  pre-split card. Verification metadata pinned until closeout stamps the L9 code commit.
