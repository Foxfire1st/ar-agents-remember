# mcp/src/agents_remember/application/curator_stored_revisions.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The module's own statement: replay and admission are answered by the candidate's rows, never by the journal.** [1]
- Every stored revision, read over a read-only connection. [2]
- **The recorded revisions the candidate already stores; empty with no dataset yet.** [3]
- The read-only opener it uses. [4]
- **The callers: the committed set filled at the start of the run, the admission exemption, and the replay marking.** [5]
- **The cases: a committed legacy operation replays (with and without base history), and a recorded-but-uncommitted one is still refused.** [6]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
