# mcp/src/agents_remember/application/curator_stored_revisions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/curator_stored_revisions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T17:09:54+02:00 |
| lastVerifiedCommitHash | `eda947325ccbe0791973953265278597e968a34a`|
| lastVerifiedCommitDate | 2026-09-28T18:11:05+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

Answers, from a curator candidate's own dataset, **which invariant revisions it already stores**. The
curator writer (`knowledge_curator_ingest.py`) uses the one answer twice: to mark a repeated creation
operation as a **replay** rather than a second write, and to decide that an operation whose recorded
revision is already stored is **not admitted again**, so the realization admission checks are not asked
of its exact retry.

## Code Commentary

### Logic

`stored_revisions(database)` opens the candidate database read-only and returns every
`invariant_revision.revision_id` with the statement it records. `committed_revisions(database,
recorded)` intersects the allocation journal's recorded revision ids with that set; it returns an empty
set when nothing was recorded or when the candidate has no database file yet (a first run).

### Conventions

Read-only access through the shipped `open_read_only_database`; the connection is always closed. The
module has no write path and holds no state.

### Invariants And Boundaries

- **The dataset, never the journal, answers "was this committed?"** The allocation journal is written
  before the batch runs and cannot know whether that batch committed; a recorded revision the dataset
  does not hold is a recorded-but-uncommitted operation (for example a crash between the journal write
  and the batch) and is **not** exempt from admission.
- **Replay and admission share one answer.** `_with_replays` marks replays from `stored_revisions`;
  `ingest_curator_list` fills `_Allocations.committed` from `committed_revisions`; `_resolve_creation`
  skips the realization checks only for a held allocation in that set. Changed content under such a key
  is still refused `allocation_content_conflict` by the ingest.
- Extracted from `knowledge_curator_ingest._stored_revisions` by leaf `260921-ICR-L45` with the same
  query and behavior; nothing about replay changed.

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement: replay and admission are answered by the candidate's rows, never by the journal.** | "The same answer decides admission." | mcp/src/agents_remember/application/curator_stored_revisions.py:1-12 |
| Every stored revision, read over a read-only connection. | `stored_revisions` | mcp/src/agents_remember/application/curator_stored_revisions.py:22-32 |
| **The recorded revisions the candidate already stores; empty with no dataset yet.** | `committed_revisions` | mcp/src/agents_remember/application/curator_stored_revisions.py:35-41 |
| The read-only opener it uses. | `open_read_only_database` | mcp/src/agents_remember/memory/knowledge/connection.py:52-63 |
| **The callers: the committed set filled at the start of the run, the admission exemption, and the replay marking.** | `ingest_curator_list`; `_resolve_creation`; `_with_replays` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1116-1243; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2221-2254; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2050-2056 |
| **The cases: a committed legacy operation replays (with and without base history), and a recorded-but-uncommitted one is still refused.** | `test_a_committed_operation_without_rationale_replays_with_no_base_history_needed`; `test_a_recorded_but_uncommitted_allocation_without_rationale_is_still_refused` | mcp/tests/test_curator_realization_authoring.py:387-397; mcp/tests/test_curator_realization_authoring.py:400-432 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-28T17:09:54+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`; primary ICR-R20@v1, review R4 PASS): created this card. **Semantic transition:** the stored-revision reader moved here from the ingest unchanged, and gained a second consumer — the committed-allocation admission exemption ruled by the Architect on review R1 (2026-09-28T12:17:09+02:00, finding F1) and guarded history-independently per the 16:15:11 ruling (O3). Verification stamp names the code base; closeout owns the real stamp.
