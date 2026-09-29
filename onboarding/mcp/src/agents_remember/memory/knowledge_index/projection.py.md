# mcp/src/agents_remember/memory/knowledge_index/projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge_index/projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T08:01:17+02:00 |
| lastVerifiedCommitHash | `ffd043f1354e94a7dcf435e10b4b7224495cbcba`|
| lastVerifiedCommitDate | 2026-09-29T08:30:03+02:00|
| governingOverview | `../overview.md` |

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
- **Retired records are not projected.** `project` skips a `status: retired` invariant or family (`RETIRED_STATUS`); a family's projected membership omits a retired or absent member, and a realization of an unprojected invariant is not projected. Those records stay in the `ix_*` tables.
- `_realization` writes one `source_anchor` (the anchor's blob as `git_blob` identity, the locator in the legacy spelling) and one `realization_claim`; `_legacy_locator` restores a symbol's `language` from the path suffix (`grammar_of`), or `unparsed`.

### Conventions

- Every spelling the projection invents is a named constant with a comment where it is defined.

### Invariants And Boundaries

- The mapping is a pure function of the files.
- Proofs, links, history rows, routes and facet records are not projected; they are answered from the `ix_*` tables.
- A retired record is never selected as live by the reused reads.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The index's design authority is the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the requirement
packet `MIK-R23@v1` of task `260928_maintained-invariant-knowledge`; both live outside the code and
memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The projection constants, the identity map and the table writers.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's statement of the mapping: identities, namespace, provenance, retired records and what is not projected. | "Retired records are not live, so they are not projected." | mcp/src/agents_remember/memory/knowledge_index/projection.py:1-35 |
| The chosen constants: namespace, dataset namespace, authority home, epoch, display prefix, retired status. | `INDEX_NAMESPACE`; `INDEX_REPOSITORY_ID`; `INDEX_AUTHORITY_HOME`; `PROJECTED_RECORDED_AT`; `DISPLAY_VERSION_PREFIX`; `RETIRED_STATUS` | mcp/src/agents_remember/memory/knowledge_index/projection.py:59-68 |
| The reverse identity map. | `UUID_DDL`; `text_uuid`; `_map` | mcp/src/agents_remember/memory/knowledge_index/projection.py:70-76; mcp/src/agents_remember/memory/knowledge_index/projection.py:79-82; mcp/src/agents_remember/memory/knowledge_index/projection.py:108-113 |
| The projection entry point, which leaves retired records out. | `project` | mcp/src/agents_remember/memory/knowledge_index/projection.py:85-105 |
| Provenance and state mapping. | `_provenance`; `_state` | mcp/src/agents_remember/memory/knowledge_index/projection.py:120-134; mcp/src/agents_remember/memory/knowledge_index/projection.py:137-140 |
| The invariant, family and realization writers. | `_invariant`; `_family`; `_realization`; `_legacy_locator` | mcp/src/agents_remember/memory/knowledge_index/projection.py:143-172; mcp/src/agents_remember/memory/knowledge_index/projection.py:175-220; mcp/src/agents_remember/memory/knowledge_index/projection.py:223-252; mcp/src/agents_remember/memory/knowledge_index/projection.py:255-272 |
| Parity: the reused selection selects the same set over the index as over the database. | `test_the_reused_selection_selects_the_same_set_over_the_index_as_over_the_database` | mcp/tests/test_knowledge_index_reuse.py:142-201 |
| Retired invariants and families are never selected as live and are answered as retired. | `test_a_retired_record_is_never_selected_as_live_and_is_answered_as_retired`; `test_a_retired_family_is_never_selected_as_live` | mcp/tests/test_knowledge_index_surfaces.py:243-278; mcp/tests/test_knowledge_index_surfaces.py:392-415 |

## Cross-Repo References

No meaningful cross-repo references found: the index reads one memory tree, addressed explicitly by the caller, and nothing else.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): created this card for the new file MIK-R23 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
