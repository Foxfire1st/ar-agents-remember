# mcp/src/agents_remember/memory/knowledge/materialization.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/materialization.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T11:30+02:00 |
| lastVerifiedCommitHash | `3332a4ce7029777d49feca22b499350435a9f83c`|
| lastVerifiedCommitDate | 2026-09-16T11:50:16+02:00|
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The publication gate a read has to pass before it may answer from a closed snapshot.**

An authored write lands in the runtime candidate; a *published* snapshot is a separate artifact produced by an
explicit publication. Those two can disagree, and when they do the disagreement **is the point**: a reader that
answers from the closed file while the runtime candidate holds newer committed work would silently present stale
knowledge as current.

So a read acquires its candidate-tree context only after this comparison. It reads the same identity every
consumer uses and reports the two it measured; it **never resolves the difference**. Publishing is the caller's
explicit operation, and no read writes rows, publishes bytes or attaches them to an older memory tree. The other
half of that contract — proving the observed memory tree contains this exact published blob — belongs to the
candidate-tree acquisition that already owns Git object identity.

## Code Commentary

### Logic

`publication_state(candidate, published_path)` returns one of three measurements, and each branch is a different
kind of fact:

- **`refused` with `candidate_binding_changed`** when the live candidate's identity cannot be read at all
  (`KnowledgeStorageError`, `apsw.Error`, `OSError`). A read never repairs a namespace; the refusal tells the
  caller to admit the candidate through the operation that owns its binding.
- **`refused` with `selected_input_unavailable`** when the published path does not exist — an absent input is an
  *input error*, never an empty dataset, because the alternative is a reader reporting "no knowledge" for a
  candidate whose file simply was not there.
- **`refused` with `unsupported_schema`** when the closed snapshot exists but is not a dataset of this schema (the
  `KnowledgeStorageError` branch of `dataset_identity`), and **`selected_input_unavailable`** when it cannot be
  read for any other reason.
- **`current`** when the two `logical_digest` values are equal — the same records, whatever the page layout is.
- **`candidate_snapshot_unpublished`** when they differ, reporting **both** identities and leaving the caller to
  decide which side moved: a newer runtime candidate needs a publication, and a stale published file needs to be
  republished or refused by the caller's own context comparison.

Both database identities are read the same way — through a **read-only** connection
(`OpenedKnowledgeStore.snapshot_identity()` for the live candidate, `logical.dataset_identity` for the closed
file) — so a pass that could repair the file it is checking cannot happen. A snapshot whose identity is confirmed
by a writable connection is not confirmed by a reader.

`unpublished_refusal(state, destination_ref)` restates the `candidate_snapshot_unpublished` measurement as the
read-side refusal. It is a separate step on purpose: the state value stays a **measurement**, and the refusal is
built only by a caller that has decided to refuse. A state that is not the unpublished one has no refusal to
restate and raises `KnowledgeStorageError` — that is a caller defect, not a returned value.

### Conventions

- The three refusal codes used here are existing contract codes plus the publication group's
  `candidate_snapshot_unpublished`; no new vocabulary is invented for the read path.
- `unpublished_refusal` renders an absent published identity as `<absent>` rather than omitting the fact.
- The module reads, never writes: it holds no lock, takes no transaction and touches no destination.

### Invariants And Boundaries

- **A read never publishes and never attaches rows to an older snapshot.** The gate reports; the caller acts.
- **An absent or unreadable input is an input error, not an empty dataset.** Both branches name the exact path.
- **The comparison is by logical digest, not by bytes or mtime.** A `VACUUM`ed copy is the same knowledge.
- **`current` is the only state in which the caller may answer from the closed file**, and the caller still
  compares the reported identity with its own resolved context — this module measures, it does not authorize.
- **Boundary.** Proving that a Git tree actually contains the published blob belongs to the candidate-tree
  acquisition; this module stops at the file's logical identity.

### Todos

None recorded for this slice.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The three-way measurement and the five branches it reports. | `publication_state` | mcp/src/agents_remember/memory/knowledge/materialization.py:34-99 |
| The separate restatement step that keeps the state a measurement. | `unpublished_refusal` | mcp/src/agents_remember/memory/knowledge/materialization.py:102-120 |
| The read-only dataset identity both sides are read through. | `dataset_identity`; `open_read_only_database` | mcp/src/agents_remember/memory/knowledge/logical.py:118-138; mcp/src/agents_remember/memory/knowledge/connection.py:55-66 |
| The live candidate identity the comparison starts from. | `snapshot_identity` | mcp/src/agents_remember/memory/knowledge/store.py:304-318 |
| The read-side refusal the unpublished state is restated as. | `candidate_snapshot_unpublished_refusal`; `selected_input_unavailable_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:930-949; mcp/src/agents_remember/memory/knowledge/refusals.py:882-902 |
| The value this module returns and the caller-facing claim it supports. | `PublicationState` | mcp/src/agents_remember/models/knowledge/snapshot.py:296-321 |
| The application entry point that exposes the gate. | `knowledge_publication_state` | mcp/src/agents_remember/application/knowledge_snapshot.py:150-155 |
| The node that proves a newer runtime candidate reports unpublished until it is published. | "test_a_newer_runtime_candidate_reports_candidate_snapshot_unpublished_until_published" | mcp/tests/test_knowledge_snapshot_publication.py:363-401 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T11:30+02:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): created this one-to-one card for the new read-side publication gate. It records the three-way measurement and its five branches, the rule that an absent input is an input error rather than an empty dataset, that both sides are read through read-only connections so a pass cannot repair what it checks, and that `unpublished_refusal` is a separate step so the state stays a measurement. It also records the boundary this module deliberately stops at: proving a Git tree contains the published blob belongs to the candidate-tree acquisition. Verification metadata remains empty until closeout stamps the code commit.
