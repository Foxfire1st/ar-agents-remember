# mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T02:22:00+02:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Store and query one immutable SQLite citation source-index generation, proving that its metadata matches the published readiness authority.

## Code Commentary

### Logic

`Database` stores file identities, direct-anchor postings, compressed quote streams and their lookup indexes, and call-literal extents. `locations` routes non-quote anchors through keyed direct lookup and quote anchors through indexed candidate streams, returning deterministic file/range results.

`write_snapshot` flushes buffered postings and writes generation, content snapshot, roots, counters, application digest, and candidate selection. Filesystem selection is stored as an empty `candidate_tree` string; a Git selection stores its exact tree identity.

`open` checks the database's actual size, opens SQLite read-only/immutable, validates the exact metadata key set and readiness identity, and checks bounded counters. Roots and candidate selection must match the ready marker. Explicit integrity verification additionally performs SQLite `quick_check` and decodes/checks the application values and checksum; ordinary queries retain their keyed lookup path.

### Conventions

Readiness schema and limits come from `source_index_state`. This module owns SQLite layout, encoding, query telemetry, and database validation; source census, cache locking, and publication order remain in their existing acquisition owners.

### Invariants And Boundaries

- A missing `candidate_tree` metadata key is malformed; filesystem and Git-candidate generations cannot substitute for each other through equal content hashes.
- Generation/snapshot identity, roots, candidate selection, counters, and database size must agree with the supplied readiness marker before queries are admitted.
- SQLite structural validity alone does not prove packed postings, quote streams, or their cross-references are usable; explicit prebuild validation checks both layers.
- Stored candidate identity binds this database to an acquisition selection; it does not itself inspect Git or prove current working-tree bytes.

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The exact metadata schema binds generation, snapshot, roots, and candidate selection to readiness. | `_validate_generation_metadata` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:58-98 |
| Canonical bounded counters must match the ready marker. | `_generation_counters` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:101-126 |
| Opening checks size and metadata before admitting read-only queries, with explicit integrity checks when requested. | `open` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:224-262 |
| Snapshot publication records candidate identity alongside the application checksum and counters. | `write_snapshot` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:333-354 |
| Anchor queries retain distinct direct and quote lookup paths. | `locations` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:439-447 |
| Explicit integrity validation checks packed data, references, counters, and the stored digest. | `validate_application_integrity` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:486-507 |
| The application checksum covers query-bearing rows including FTS term/document pairs. | `_application_digest` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:744-782 |

## Update History

- 2026-09-06T02:22:00+02:00 — L30 recovery source review: Documented candidate-bound database metadata and retained query/integrity responsibilities; replaced stale source ranges. Verified against prepared code commit `97e8ed2e1fae21756c3ad995c30613d4fbfcc503`; source review does not claim Gate-5 execution or recovery acceptance.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
