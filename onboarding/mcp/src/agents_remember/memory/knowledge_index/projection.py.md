# mcp/src/agents_remember/memory/knowledge_index/projection.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The index as a knowledge dataset (MIK-R23 rule 6).** The recorded-scope selection (`memory/knowledge/read.py`), the views and the read seams in `application/` are SQL over the knowledge store's logical tables, addressed by UUIDs. Rule 6 adapts them to the index rather than rewriting them, so the index file *is* a dataset of the store's newest schema generation: this module fills `repository`, `invariant`, `invariant_revision`, `family`, `family_revision`, `family_member`, `source_anchor` and `realization_claim` from the same parsed files, and every existing reader that takes a `database_path` reads the index unchanged.

## Code Commentary

### Logic

- **Identities.** `text_uuid(role, text_id)` is `uuid5` in the fixed `INDEX_NAMESPACE`; `_map` records every mapping in `ix_uuid` (uuid, text ID, role), so a read's UUIDs translate back to `INV-…`, `FAM-…` and `RLZ-…`. A record has one revision in a tree, so its revision UUID is derived from `<ID>@<revision>`.
- **Namespace.** Every row is bound to the constant `INDEX_REPOSITORY_ID` with authority home `INDEX_AUTHORITY_HOME` (`ar-knowledge-index`): the index is keyed by its tree alone.
- **Provenance.** `_provenance` names the origin (task and leaf or wave, else `unrecorded`) and the record file; `recorded_at` is the fixed epoch `PROJECTED_RECORDED_AT`, which no reader may read as a recording time.
- **State.** `_state` maps `accepted` to `accepted` with an acceptance ref naming the file, and anything else live to `proposed`. `display_version` is `r<revision>` (`DISPLAY_VERSION_PREFIX`); an invariant's `display_label` is its text ID.
- **Seals (MIK-R25; ruling 2026-09-29T22:22:37 Q6).** Each projected `invariant_revision` and `family_revision` row carries the store's own payload digest (`revision_payload_digest`, `family_revision_payload_digest` from `models/knowledge/digest.py`), computed over an `InvariantRevision`/`FamilyRevision` built from exactly the projected cells (with a `_UNSEALED` placeholder for its own digest field and the provenance decoded by `decode_authorship`). Before, rows carried `sha256(record.to_document())`; the store's revision readers verify the logical seal on every decode, so the reviewer's family roster raised `KnowledgeStorageError` on every index. The fix is shared with L23's code and is why `INDEX_FORMAT` is `ar-knowledge-index/v2` (`schema.py`): v1 caches are rebuilt. `_state` now returns the typed `KnowledgeState`.
- **Retired records are not projected.** `project` skips a `status: retired` invariant or family (`RETIRED_STATUS`); a family's projected membership omits a retired or absent member, and a realization of an unprojected invariant is not projected. Those records stay in the `ix_*` tables.
- `_realization` writes one `source_anchor` (the anchor's blob as `git_blob` identity, the locator in the legacy spelling) and one `realization_claim`; `_legacy_locator` restores a symbol's `language` from the path suffix (`grammar_of`), or `unparsed`.

### Conventions

- Every spelling the projection invents is a named constant with a comment where it is defined.

### Invariants And Boundaries

- The mapping is a pure function of the files.
- Proofs, links, history rows, routes and facet records are not projected; they are answered from the `ix_*` tables.
- A retired record is never selected as live by the reused reads.
- A projected revision row decodes through the store's own revision readers: its seal is the store's digest over the projected cells.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The index's design authority is the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the requirement
packet `MIK-R23@v1` of task `260928_maintained-invariant-knowledge`; both live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The projection constants, the identity map and the table writers.

- The module's statement of the mapping: identities, namespace, provenance, retired records, the store's own seals (MIK-R25) and what is not projected. [1]
- The chosen constants: namespace, dataset namespace, authority home, epoch, display prefix, retired status. [2]
- The reverse identity map. [3]
- The projection entry point, which leaves retired records out. [4]
- Provenance and state mapping. [5]
- The invariant, family and realization writers. [6]
- The seal of each projected revision row is the store's own digest over the projected cells. [7]
- Parity: the reused selection selects the same set over the index as over the database. [8]
- Retired invariants and families are never selected as live and are answered as retired. [9]

### Cross-Repo References

No meaningful cross-repo references found: the index reads one memory tree, addressed explicitly by the caller, and nothing else.

No cross-repo boundary is crossed by this file.
