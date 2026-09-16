# mcp/src/agents_remember/memory/knowledge/publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T11:30+02:00 |
| lastVerifiedCommitHash | `3332a4ce7029777d49feca22b499350435a9f83c`|
| lastVerifiedCommitDate | 2026-09-16T11:50:16+02:00|
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Install one closed snapshot at an admitted destination, **atomically and verifiably**.

The destination is a *file other readers open*: a memory tree is captured from it, a reader reopens it, and Git
may commit it. Two consequences shape the module:

1. **Publication is replace-or-nothing.** The install is the repository's atomic replace of an already-written,
   already-flushed stage, so a reader sees the previous snapshot or the new one and never a partial file. Any
   failure before the replace leaves the previous destination exactly as it was, and the private stage is removed.
2. **A no-op does not rewrite bytes.** When the destination already holds the same logical dataset — the same
   records, whatever its SQLite page layout happens to be — the existing bytes are retained and `no_change` is
   returned. Page layout is not knowledge, and rewriting the file would dirty a tree for a reason no reader could
   observe in the data.

## Code Commentary

### Logic

`publish_candidate_snapshot(destination, request)` is the composed entry point:

1. **Re-verify the candidate** by opening it through the ordinary lifecycle path (`open_candidate`). A refusal, or
   an identity that is not the one the publication was admitted against, is returned as a refusal — the identity
   branch is `stale_precondition` naming both digests (`_stale_candidate_refusal`), because "a fresher candidate is
   never published silently in place of the selected one".
2. **Freeze under the candidate's own lock** (`_freeze_under_candidate_lock`). The candidate store is opened, its
   single resource lock taken, the frozen stage produced by `freeze_closed_snapshot`, and the lock released. Every
   way the frozen point can fail to be produced — the stage directory, the copy, the verify, the flush — arrives
   as a typed refusal (`snapshot_incomplete`, or the freeze's own `stale_precondition`), so `publication_failed` is
   reserved for a failure of the **install**.
3. **Install under the destination's own lock** by delegating to `publish_prepared_snapshot`.

The stage directory is private and beside the destination (`_private_stage_directory`, a `mkdtemp` named
`.<destination>.*.stage`), and `_discard_stage_directory` removes it on the way out of both success and failure —
a removal failure is suppressed there so it cannot mask the refusal that says why the publication did not happen.

`publish_prepared_snapshot(prepared, request)` is the reusable half: a caller that produced a validated closed
database — a merged result, an import, a restored artifact — reaches the destination through exactly this path.
It re-reads the stage and refuses `snapshot_incomplete` if the stage is gone or is **not the file that was frozen
and verified** (its physical digest is re-checked against `PreparedKnowledgeSnapshot.file_digest`), then takes the
destination lock and installs.

`_install` is where the destination contract lives:

- `_observe_destination` reads the destination's identity **without writing it**; an unreadable destination is a
  `destination_stale` refusal naming what could not be read.
- `_matches_expected` compares the observation with `expected_destination` exactly — `None` means "expected to be
  absent" and matches only absence, so a file the caller never admitted is never overwritten.
- An identical logical dataset is the `no_change` outcome: the stage is discarded and the **existing bytes are
  retained**.
- Otherwise `atomic_replace` installs the stage, and `_readback` reopens the destination and reports what is
  actually there: `published` with the installed identity and the `previous_identity` it replaced, or a refusal
  (`publication_failed` when the installed file carries a different identity,
  `publication_durability_unconfirmed` when the replacement completed but the destination could not be re-read).

**Two locks, never nested.** The candidate lock protects the working database and is released before the
destination lock is taken; the destination lock protects the file being replaced. The lock resource is the
destination's hidden stem (`_publication_lock_resource` → `exclusive_file_lock` derives
`.<published-name>.lock`), so the lock file is **colocated with the resource it excludes** — a lock keyed anywhere
else would let two processes disagree about which resource they are excluding. Deleting that file on close is
**not** a cleanup: it is the live `flock` resource, and removing it while a publication holds it would let the
next publication take an unheld lock.

### Conventions

- Every failure path returns a typed refusal; `LockCapabilityError` from the lock primitive and an `OSError` from
  taking the lock both map to `lock_capability_unavailable`, because a publication that cannot prove exclusion must
  not proceed.
- `_render_identity` renders an absent destination as `<absent>` in facts, so `expected`/`observed` always carry a
  value.
- Private helpers are prefixed `_` and the two public functions are the only surface other modules import.

### Invariants And Boundaries

- **A refusal never replaces the destination.** Every refusal path leaves the previous file exactly as it was, and
  the honest code for "the replacement completed but could not be confirmed" is
  `publication_durability_unconfirmed`, not `publication_failed` — the two tell a caller different things about
  what is on disk.
- **`no_change` is a retained-bytes outcome**, decided on the **logical** digest rather than on bytes or mtime.
- **The destination lock is a live `flock` resource beside the destination.** It is never deleted, and it is the
  one file a captured memory tree will contain besides the snapshot itself.
- **A published snapshot carries knowledge only while the exact code/memory inputs in the candidate receipt and
  the caller's resolved context live.** The publication moves a database, not a binding: the receipt's inputs and
  the consumer's context are what make the published bytes meaningful at a point in time.
- **Boundary.** This module installs a file. It does not decide when a publication is authorized, does not commit
  anything to Git, and does not compare the published dataset with a consumer's expected context — that comparison
  is `materialization.publication_state`.

### Todos

None recorded for this slice. One disclosed limitation is carried by `kernel/atomic_write.py.md` rather than
silenced here: the directory fsync runs **after** `os.replace`, so a failure in that window is reported as a
replace failure — which is why a create can answer `destination_occupied` for a destination that holds the
complete candidate it just created, and why this module can return `publication_failed` where
`publication_durability_unconfirmed` would be the more precise code.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The composed publication entry point, including its identity re-check and lock ordering. | `publish_candidate_snapshot` | mcp/src/agents_remember/memory/knowledge/publication.py:66-111 |
| The reusable install half and its stage-digest re-check. | `publish_prepared_snapshot` | mcp/src/agents_remember/memory/knowledge/publication.py:114-170 |
| The install: observe without writing, compare exactly, retain on `no_change`, replace, then read back. | `_install`; `_observe_destination`; `_matches_expected` | mcp/src/agents_remember/memory/knowledge/publication.py:176-212; mcp/src/agents_remember/memory/knowledge/publication.py:260-268; mcp/src/agents_remember/memory/knowledge/publication.py:271-276 |
| The readback that decides between `published`, `publication_failed` and the honest durability code. | `_readback` | mcp/src/agents_remember/memory/knowledge/publication.py:215-249 |
| The destination-stale refusal and the candidate-moved refusal, each naming both digests. | `_stale_destination`; `_stale_candidate_refusal` | mcp/src/agents_remember/memory/knowledge/publication.py:279-293; mcp/src/agents_remember/memory/knowledge/publication.py:296-314 |
| The candidate lock that protects the working database, released before the destination lock is taken. | `_freeze_under_candidate_lock`; `exclusive_candidate_lock` | mcp/src/agents_remember/memory/knowledge/publication.py:323-339; mcp/src/agents_remember/memory/knowledge/store.py:487-506 |
| The private stage directory, its cleanup and the suppression that protects the caller's refusal. | `_private_stage_directory`; `_discard_stage_directory` | mcp/src/agents_remember/memory/knowledge/publication.py:342-350; mcp/src/agents_remember/memory/knowledge/publication.py:353-362 |
| The hidden lock resource that lands `.<published-name>.lock` beside the destination. | `_publication_lock_resource`; `exclusive_file_lock` | mcp/src/agents_remember/memory/knowledge/publication.py:365-373; mcp/src/agents_remember/kernel/file_lock.py:87-116 |
| The freeze procedure behind the stage, and the stage shape it returns. | `freeze_closed_snapshot`; `discard_stage`; `PreparedKnowledgeSnapshot` | mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:66-109; mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:206-209; mcp/src/agents_remember/models/knowledge/snapshot.py:224-236 |
| The atomic replace whose directory fsync records the new name, not the bytes under it. | `atomic_replace`; `fsync_file` | mcp/src/agents_remember/kernel/atomic_write.py:78-92; mcp/src/agents_remember/kernel/atomic_write.py:95-105 |
| The read-only dataset identity every comparison in this module uses. | `dataset_identity`; `logical_digest` | mcp/src/agents_remember/memory/knowledge/logical.py:118-138; mcp/src/agents_remember/memory/knowledge/logical.py:82-85 |
| The publication outcome vocabulary and the destination request. | `SnapshotPublicationResult`; `SnapshotDestinationRequest`; `PublishSnapshotRequest` | mcp/src/agents_remember/models/knowledge/snapshot.py:259-293; mcp/src/agents_remember/models/knowledge/snapshot.py:239-249; mcp/src/agents_remember/models/knowledge/snapshot.py:252-256 |
| The nodes that protect the publication's failure behaviour. | "test_a_failed_replacement_leaves_the_prior_destination_byte_identical"; "test_a_publication_whose_readback_fails_reports_the_destination_it_actually_left"; "test_a_logical_no_op_retains_the_published_bytes" | mcp/tests/test_knowledge_snapshot_publication.py:112-141; mcp/tests/test_knowledge_snapshot_publication.py:143-176; mcp/tests/test_knowledge_snapshot_publication.py:178-202 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T11:30+02:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): created this one-to-one card for the new publication module. It records replace-or-nothing as a refusal invariant, the logical-digest `no_change` that deliberately retains existing bytes, the two locks that are never nested, the hidden `.<published-name>.lock` resource beside the destination (and that deleting it is **not** the fix, because it is the live `flock`), the durability-versus-install distinction between `publication_failed` and `publication_durability_unconfirmed`, and the two carried statements a consumer needs: a published snapshot carries knowledge only while the receipt's exact inputs and the caller's resolved context live, and `authorization_ref` is carried but never examined here. The disclosed `atomic_write` nuance (directory fsync after `os.replace`) is cross-referenced to its own card rather than restated as a property of this module. Verification metadata remains empty until closeout stamps the code commit.
