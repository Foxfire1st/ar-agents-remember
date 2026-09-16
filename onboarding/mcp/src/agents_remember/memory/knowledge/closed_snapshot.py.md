# mcp/src/agents_remember/memory/knowledge/closed_snapshot.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/closed_snapshot.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T11:30+02:00 |
| lastVerifiedCommitHash | `3332a4ce7029777d49feca22b499350435a9f83c`|
| lastVerifiedCommitDate | 2026-09-16T11:50:16+02:00|
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Freeze **one consistent, closed, self-contained copy** of a candidate's pinned dataset, and *prove* it rather
than assume it.

A SQLite main file is not a database on its own: committed content may still live in a journal or WAL beside it,
so a file copied while the database is live can reopen to **older** records than the ones it was copied from.
Everything in this module exists to make one copy that cannot be in that state. It is the shared freeze procedure:
the publication path and the candidate clone both call it, so neither can produce a copy with a weaker property
than the other.

## Code Commentary

### Logic

`freeze_closed_snapshot(store, expected, stage_path)` runs one ordered procedure, and each step is where it is for
a reason:

1. **Pin the view** (`_pinned_read_view`) — a read transaction pins the exact logical view that is verified, so the
   identity check and the copy describe *one* dataset rather than two readings of a moving one.
2. **Re-check the admitted identity inside that view** (`_copy_pinned_view`) — the store's bound namespace must be
   the expected one, the database must carry a repository row, and the live logical digest must equal the admitted
   digest; a mismatch is `stale_precondition` naming both digests (`_stale_candidate_refusal`).
3. **Copy through SQLite** (`_run_backup`) — `Connection.backup` reads database state through the engine,
   including whatever is committed in the journal or WAL, so an uncommitted writer's rows are excluded and a
   committed-but-WAL-resident batch is included.
4. **Normalize on a fresh connection** (`_normalize_stage`) — a backup destination **inherits the source's journal
   mode**: a WAL source leaves a staged file whose header still says `wal` even when the destination connection was
   set to `delete` *before* the copy. The mode is therefore established on a newly opened connection to the
   finished copy, and read back (`_CLOSED_JOURNAL_MODE = "delete"`), so the accepted mode is observed rather than
   requested.
5. **Prove it by reopening read-only** (`_verify_closed_stage`) — the staged file must have **no** journal/WAL peer
   (`journal_peers`), must reopen in the `delete` journal mode, must declare the expected schema generation, and
   must hold the pinned logical dataset.
6. **Flush the file's own data** (`fsync_file`) — the directory fsync in `atomic_replace` records that the new
   *name* exists and says nothing about the bytes it points at, so the staged file is flushed before it is handed
   to a publication that will rename it.

`discard_stage` / `_discard_owned_stage` remove one private stage **and its peers**, and nothing else; a removal
failure is suppressed so the caller keeps the typed refusal that says why the freeze failed instead of losing it to
a secondary filesystem error. `PreparedKnowledgeSnapshot` carries the logical identity the stage was frozen from
and the physical digest of the staged bytes.

### Conventions

- `_CLOSED_JOURNAL_MODE` is `delete` because SQLite's own rollback journal is created and removed around a write
  and never holds committed state once the writer is gone; a `wal` header instead makes the file's completeness
  depend on a peer that a copy does not carry.
- The `_JOURNAL_PEER_SUFFIXES` tuple is shared by the peer probe and the stage cleanup, so the files that are
  checked and the files that are removed cannot diverge.
- `_journal_peers` returns `list[Path]` in declaration order so a refusal can name the peers it found.

### Invariants And Boundaries

- **Nothing here deletes a journal to make a database look clean.** The only files this module removes are the
  peers of a **private stage it abandoned**, never a peer of a destination.
- **A stage path is created, never reused.** An existing stage path is a `KnowledgeStorageError`, because a
  reused name could hide a previous freeze's bytes.
- **The freeze is all-or-nothing.** Any failure after the copy removes the stage and raises one typed refusal
  (`snapshot_incomplete`, or `stale_precondition` for the identity branch), so a caller never receives a partial
  stage.
- **The mode is observed, not requested.** The staged file's journal mode is read back on a fresh connection
  because the backup destination's header inherits the source's mode.
- **Boundary.** This module produces a closed *file*. It does not choose a destination, take a destination lock,
  publish, or decide whether a candidate may be disposed of.

### Todos

None recorded for this slice. The peer probe covers `-wal`, `-shm` and `-journal`; a future SQLite journal mode
with a different peer name would have to extend `_JOURNAL_PEER_SUFFIXES`, which is why the probe and the cleanup
share one tuple.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one journal mode a published snapshot may carry, and the peer suffixes the probe and cleanup share. | `_CLOSED_JOURNAL_MODE`; `_JOURNAL_PEER_SUFFIXES` | mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:62-62; mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:63-63 |
| The ordered freeze procedure and its all-or-nothing refusal. | `freeze_closed_snapshot` | mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:66-109 |
| The pinned view, the in-view identity re-check and the through-the-engine copy. | `_copy_pinned_view`; `_run_backup`; `_pinned_read_view` | mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:112-125; mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:128-139; mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:213-221 |
| The inherited-journal-mode problem and the fresh connection that establishes and reads back the mode. | `_normalize_stage` | mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:142-159 |
| The read-only proof: no peer, closed mode, declared schema and the pinned dataset. | `_verify_closed_stage` | mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:162-192 |
| The peer probe and the stage-only cleanup whose failure is suppressed. | `journal_peers`; `discard_stage`; `_discard_owned_stage` | mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:195-203; mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:206-209; mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:241-252 |
| The refusal for a candidate that moved between admission and acquisition. | `_stale_candidate_refusal` | mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:224-238 |
| The file flush that the directory fsync in `atomic_replace` does not substitute for. | `fsync_file`; `atomic_replace` | mcp/src/agents_remember/kernel/atomic_write.py:95-105; mcp/src/agents_remember/kernel/atomic_write.py:78-92 |
| The read-only connection and journal-mode reader the verification uses. | `open_read_only_database`; `journal_mode`; `inspect_schema` | mcp/src/agents_remember/memory/knowledge/connection.py:55-66; mcp/src/agents_remember/memory/knowledge/connection.py:69-72; mcp/src/agents_remember/memory/knowledge/connection.py:106-122 |
| The stage shape this procedure returns. | `PreparedKnowledgeSnapshot` | mcp/src/agents_remember/models/knowledge/snapshot.py:224-236 |
| The publication that installs a frozen stage, and the clone that reuses this same procedure. | `publish_prepared_snapshot`; `_build_cloned_candidate` | mcp/src/agents_remember/memory/knowledge/publication.py:114-170; mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:246-291 |
| The node that proves a WAL-resident batch is published whole while a main-file copy is not. | "test_a_wal_resident_batch_is_published_whole_while_a_main_file_copy_is_not" | mcp/tests/test_knowledge_snapshot_publication.py:81-110 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T11:30+02:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): created this one-to-one card for the new closed-snapshot freeze. It records the six ordered steps and why each is where it is — most importantly that a backup destination **inherits the source's journal mode**, so the closed mode has to be established and read back on a fresh connection to the finished copy, and that the file's own data is flushed because the directory fsync in the atomic replace records the new *name* and says nothing about the bytes it points at. It also records the stage-only cleanup rule (never a destination's peers) and the shared peer-suffix tuple that keeps the probe and the cleanup from diverging. Verification metadata remains empty until closeout stamps the code commit.
