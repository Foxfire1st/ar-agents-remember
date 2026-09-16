# mcp/src/agents_remember/memory/knowledge/closed_snapshot.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/closed_snapshot.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T17:45+02:00 |
| lastVerifiedCommitHash | `4eb2b1992f6183fba06e9f31aa664d9a93094c26`|
| lastVerifiedCommitDate | 2026-09-16T18:28:38+02:00|
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
than the other. **The "prove this finished file is closed" step is shared more widely than the freeze**: the
portable import's private stage is closed through the same `require_closed_database`, so "closed" is one
definition rather than one per producer of a finished database file.

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
4. **Prove the finished file is a closed database** (`require_closed_database`) — the one shared step below.
5. **Flush the file's own data** (`fsync_file`) — the directory fsync in `atomic_replace` records that the new
   *name* exists and says nothing about the bytes it points at, so the staged file is flushed before it is handed
   to a publication that will rename it.

**`require_closed_database(stage_path, expected)` is the reusable half, and it is why this module has two
producers rather than one.** Any producer that has just written a complete database file — this freeze, the
portable import's private stage, a later restore — proves it the same way, so "closed" means one thing rather
than one thing per caller. It is exactly two steps, in this order, and neither substitutes for the other:

- **Normalize on a fresh connection** (`_normalize_stage`) — a backup destination **inherits the source's
  journal mode**: a WAL source leaves a staged file whose header still says `wal` even when the destination
  connection was set to `delete` *before* the copy. The mode is therefore established on a newly opened
  connection to the finished copy, and read back (`_CLOSED_JOURNAL_MODE = "delete"`), so the accepted mode is
  observed rather than requested.
- **Prove it by reopening read-only** (`_verify_closed_stage`) — the staged file must have **no** journal/WAL
  peer (`journal_peers`), must reopen in the `delete` journal mode, must declare the expected schema generation,
  and must hold the pinned logical dataset. A writable connection could repair what it is checking, so it is not
  asked.

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
- **The closure has two producers and one definition.** `freeze_closed_snapshot` and the portable import's
  `_stage_imported_dataset` both call `require_closed_database`, and the freeze's behaviour is unchanged by the
  sharing because the function body is precisely the two calls the freeze made, in the same order. **The leaf's
  own claim is exactly two things:** the primitive is *called* by both producers (`export_import.py:399`,
  `closed_snapshot.py:123`) and its *normalisation* is what closes the file. `_verify_closed_stage`, the peer
  proof and the normalisation's own re-read are **L4's pre-existing lines**, unchanged here, and their coverage
  authority is L4's review — the properties they assert are carried elsewhere (the mode by the normalisation, the
  identity by the publication's readback), which is why no node moved.
- **Boundary.** This module produces a closed *file*. It does not choose a destination, take a destination lock,
  publish, or decide whether a candidate may be disposed of.

### Todos

None recorded for this slice. The peer probe covers `-wal`, `-shm` and `-journal`; a future SQLite journal mode
with a different peer name would have to extend `_JOURNAL_PEER_SUFFIXES`, which is why the probe and the cleanup
share one tuple. One evidence reservation is carried rather than silenced: `_verify_closed_stage` and the peer
proof are L4's pre-existing lines and their coverage authority is L4's review — this leaf shares them, calls them
and proves the normalisation's effect on the published destination, and does not claim a mutation for every line
inside the primitive.

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
| **The reusable "prove this finished file is a closed database" step both producers call — the import stages through it as well as the freeze.** | `require_closed_database` | mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:66-89 |
| The ordered freeze procedure and its all-or-nothing refusal. | `freeze_closed_snapshot` | mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:92-137 |
| The pinned view, the in-view identity re-check and the through-the-engine copy. | `_copy_pinned_view`; `_run_backup`; `_pinned_read_view` | mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:140-153; mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:156-167; mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:240-249 |
| The inherited-journal-mode problem and the fresh connection that establishes and reads back the mode. | `_normalize_stage` | mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:170-187 |
| The read-only proof: no peer, closed mode, declared schema and the pinned dataset. | `_verify_closed_stage` | mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:190-220 |
| The peer probe and the stage-only cleanup whose failure is suppressed. | `journal_peers`; `discard_stage`; `_discard_owned_stage` | mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:223-231; mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:234-237; mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:269-280 |
| The refusal for a candidate that moved between admission and acquisition. | `_stale_candidate_refusal` | mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:252-266 |
| The file flush that the directory fsync in `atomic_replace` does not substitute for. | `fsync_file`; `atomic_replace` | mcp/src/agents_remember/kernel/atomic_write.py:95-105; mcp/src/agents_remember/kernel/atomic_write.py:78-92 |
| The read-only connection and journal-mode reader the verification uses. | `open_read_only_database`; `journal_mode`; `inspect_schema` | mcp/src/agents_remember/memory/knowledge/connection.py:55-66; mcp/src/agents_remember/memory/knowledge/connection.py:69-72; mcp/src/agents_remember/memory/knowledge/connection.py:106-122 |
| The stage shape this procedure returns. | `PreparedKnowledgeSnapshot` | mcp/src/agents_remember/models/knowledge/snapshot.py:224-236 |
| **The second producer this leaf added: the portable import stages its dataset and closes it through the same step.** | `_stage_imported_dataset` | mcp/src/agents_remember/memory/knowledge/export_import.py:364-405 |
| The publication that installs a frozen stage, and the clone that reuses this same procedure. | `publish_prepared_snapshot`; `_build_cloned_candidate` | mcp/src/agents_remember/memory/knowledge/publication.py:114-170; mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:246-291 |
| The node that proves a WAL-resident batch is published whole while a main-file copy is not. | "test_a_wal_resident_batch_is_published_whole_while_a_main_file_copy_is_not" | mcp/tests/test_knowledge_snapshot_publication.py:81-110 |
| **The node this leaf owns for the closure, which measures the property on the published destination.** | "test_a_frozen_snapshot_of_a_wal_resident_candidate_is_published_closed" | mcp/tests/test_knowledge_portable_boundaries.py:88-131 |
| **The node that proves the import's stage is closed before it is published.** | "test_a_stage_opened_in_wal_mode_is_published_as_a_closed_database" | mcp/tests/test_knowledge_portable_boundaries.py:533-570 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T17:45+02:00 — 260915-KS-L6 curator (uncommitted change set on `ar/260915-ks-l06`, base `7db50f8f`): **recorded the second producer of the closure and the one definition behind it.** The portable import stages a database and must publish it closed, so the freeze's last two steps were extracted into `require_closed_database(stage_path, expected)` — normalize on a fresh connection, then prove it by reopening read-only — and `freeze_closed_snapshot` now calls it, behaviour-preserving because the body is precisely the two calls the freeze made in the same order. The card records the extent of this leaf's claim exactly: the primitive is **called** by both producers (`export_import.py:399`, `closed_snapshot.py:123`) and its **normalisation** is what closes the file, while `_verify_closed_stage`, the peer proof and the normalisation's own re-read remain **L4's pre-existing lines** whose coverage authority is L4's review. It also records that this leaf owns a node for the closure measured on the **published destination** rather than on the private stage. Every citation range below was re-derived against the working tree, and the rows the L4 card carried that no longer held their anchors (the freeze, the peer probe, the stage cleanup, `_pinned_read_view`, `_stale_candidate_refusal`) were corrected. Verification metadata: lastUpdated advanced, commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.
- 2026-09-16T11:30+02:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): created this one-to-one card for the new closed-snapshot freeze. It records the six ordered steps and why each is where it is — most importantly that a backup destination **inherits the source's journal mode**, so the closed mode has to be established and read back on a fresh connection to the finished copy, and that the file's own data is flushed because the directory fsync in the atomic replace records the new *name* and says nothing about the bytes it points at. It also records the stage-only cleanup rule (never a destination's peers) and the shared peer-suffix tuple that keeps the probe and the cleanup from diverging. Verification metadata remains empty until closeout stamps the code commit.
