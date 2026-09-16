# mcp/src/agents_remember/kernel/atomic_write.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/kernel/atomic_write.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T11:30+02:00 |
| lastVerifiedCommitHash | `3332a4ce7029777d49feca22b499350435a9f83c` |
| lastVerifiedCommitDate | 2026-09-16T11:50:16+02:00|
| governingOverview | `mcp/overview.md` |

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
  destination's parent (and the source's, when they differ).
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
- **Disclosed limitation — the directory fsync runs after `os.replace`.** A failure in the window between the
  rename and the directory flush is therefore reported as a **replace failure**, even though the rename itself
  succeeded. Two visible consequences are recorded rather than hidden: a create can answer `destination_occupied`
  when the destination is in fact the complete candidate it just created, and a publication can return
  `publication_failed` where `publication_durability_unconfirmed` would be the more precise code. The observation
  came from `KS-R04`'s reviewer; it is recorded, not fixed, because the honest remedy is a caller-side one (reopen
  the destination and revalidate) and the module's ordering is what makes the ordinary case atomic.
- **Boundary.** This module reports a durability failure as an `OSError`; the caller owns the refusal code. It
  never decides whether a failed publish should be retried, and it never deletes or repairs a destination.

### Todos

None recorded for this slice. The post-rename fsync window recorded above is a disclosed limitation with a
caller-side remedy, not a scheduled repair: changing the ordering would trade a rare misreport for a
non-atomic publish.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The private temp this module writes before it replaces `path`. | `_temp_path_for` | mcp/src/agents_remember/kernel/atomic_write.py:21-29 |
| The directory flush that makes a completed rename survive a host loss. | `_fsync_directory` | mcp/src/agents_remember/kernel/atomic_write.py:32-48 |
| The one atomic publish: readers see the old file or the new one, never both. | `atomic_write_bytes`; `atomic_write_text` | mcp/src/agents_remember/kernel/atomic_write.py:51-70; mcp/src/agents_remember/kernel/atomic_write.py:73-75 |
| The atomic move of an already-written file onto a destination. | `atomic_replace` | mcp/src/agents_remember/kernel/atomic_write.py:78-92 |
| **The file-data flush this leaf exposed, for a producer that wrote the file through another owner.** | `fsync_file` | mcp/src/agents_remember/kernel/atomic_write.py:95-105 |
| The producer that needs it: a closed snapshot stage whose bytes must reach stable storage before the rename publishes the name. | `freeze_closed_snapshot` | mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:66-109 |
| The receipt write that goes through this module's atomic byte publish. | `write_candidate_receipt` | mcp/src/agents_remember/memory/knowledge/candidate_receipt.py:49-58 |
| The install whose failure is reported as a replace failure. | `_install` | mcp/src/agents_remember/memory/knowledge/publication.py:176-212 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T11:30+02:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): **replaced this card's generated symbol dump with the durability contract it actually carries, and recorded the new `fsync_file` helper plus one disclosed limitation.** The card previously listed the module's five definitions with line ranges and nothing else; it now states what the two fsyncs each make durable (the *name* versus the *bytes*), which is the distinction the new helper exists for — a producer that writes a file through another owner (a database closing its own handles) still has to flush it before a rename publishes it. The disclosed limitation is recorded rather than fixed: the directory fsync runs **after** `os.replace`, so a failure in that window is reported as a replace failure, which is why a create can answer `destination_occupied` for a destination that holds the complete candidate it just created and why a publication can return `publication_failed` where `publication_durability_unconfirmed` would be the more precise code. That observation came from this leaf's reviewer. Citation ranges were re-derived against the working tree and the unverified August stamp was replaced by the card's actual verification state. Verification metadata keeps the L3 commit stamp, which closeout restamps for this leaf.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
