# mcp/src/agents_remember/memory/knowledge/merge_schema.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/merge_schema.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:45+02:00 |
| lastVerifiedCommitHash | `7db50f8f4a67e60f9011266110ad6d0156f1a905` |
| lastVerifiedCommitDate | 2026-09-16T14:02:05+02:00 |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The structural preflight a common-base merge runs before any session exists.** It answers one question about one database: *is its declared structure exactly the supported schema generation?* It answers it from SQLite's own catalog — tables and their options, ordered columns with types, nullability and primary-key positions, foreign keys, indexes, triggers and `user_version` — rather than from a version string, because two databases can agree on `user_version` and disagree about a column type, a foreign key or a trigger.

**Why it runs before the session.** SQLite's changeset application can silently skip a table it cannot match: the changeset carries no operation for a table that was never attached, and a table that exists on only one side is exactly the schema disagreement this preflight refuses. A merge that produced a green result over such a pair would have dropped a side's entire change set.

## Code Commentary

### Logic

`declared_structure()` derives the manifest by creating the DDL in a private in-memory database and introspecting the result, so the comparison runs against the same source of truth that creates a database rather than against a second hand-written description of it. `read_database_structure(path)` / `read_structure(connection)` read one file's actual catalog.

`compare_structures(expected, observed)` returns the **first** structural difference or `None`, and the checks run most-structural first: a missing canonical table, then a table this generation does not declare, then the per-table comparison. Within a table, `_compare_table` runs `_compare_column_details` (ordered names, types, nullability, primary-key positions), `_compare_foreign_keys` (including deferral and delete actions), `_compare_indexes` (unique and named indexes, by name and by structure), `_compare_triggers` (the immutability triggers, by name and normalised body) and `_compare_options` (`STRICT` and `WITHOUT ROWID`, from `pragma_table_list`). The first difference is returned rather than a list, because a caller acts on the reason the merge did not start and a later difference in the same input would not change that.

`require_supported_structure(structure, role)` wraps that comparison as a refusal and carries the role, so a refusal says which of the merge's three positions disagreed rather than only that one did.

**One comparison per input against the declared generation — not a second pass comparing inputs to each other.** Every accepted input is structurally identical to that one declaration, so a pairwise pass would be unreachable: it could only fire for an input the per-input pass had already refused. `compare_structures` is public because it *is* that per-input comparison, and it is exposed so a caller can read the difference it found.

### Conventions

- Every compared fact is reduced to a stable rendered string (`_render_column`, `_render_foreign_keys`, `_render_indexes`, `_render_triggers`) and `_normalized_sql` collapses whitespace in a catalog SQL body, so a comparison is over structure rather than formatting.
- `_index_columns` compares an index's *shape* — which declared columns it covers, in order, from `key=1` entries with SQLite's trailing rowid entries excluded — because an auto-index's generated name is local naming rather than dataset structure. A **named** index is separately compared by name inside `_read_table`'s index tuple, because a dropped or renamed declared index is a real schema difference.
- `_INTERNAL_TABLE_PREFIX` excludes `sqlite_*` objects from the "table this generation does not declare" check.

### Invariants And Boundaries

- **It does not repair, migrate, add or drop anything.** Schema reconciliation is explicitly outside this operation.
- **It does not ignore an unfamiliar table to obtain a green result.** An input carrying a table outside the declared manifest is not a dataset this schema wrote, so it is refused rather than merged around.
- **`read_structure` writes nothing.** Every read is through the catalog, and `read_database_structure` opens the file read-only.
- **Boundary.** This module answers a structure question and returns a refusal or a difference. It does not merge, produce deltas, apply anything, or decide whether a merge may proceed.

### Todos

None recorded for this slice.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The manifest derived by creating the DDL and introspecting it, so the comparison runs against the same source of truth as the schema itself. | `declared_structure` | mcp/src/agents_remember/memory/knowledge/merge_schema.py:78-88 |
| One canonical table's compared facts, including declared column order and primary-key positions. | "One canonical table's declared structure, as the catalog reports it." | mcp/src/agents_remember/memory/knowledge/merge_schema.py:53-66; mcp/src/agents_remember/memory/knowledge/merge_schema.py:70-75 |
| The catalog reader that answers the structure question without writing anything. | `read_structure`; `read_database_structure` | mcp/src/agents_remember/memory/knowledge/merge_schema.py:91-108; mcp/src/agents_remember/memory/knowledge/merge_schema.py:111-118 |
| The refusal that names which merge role disagreed. | `require_supported_structure` | mcp/src/agents_remember/memory/knowledge/merge_schema.py:121-139 |
| The first-difference comparison and its most-structural-first order. | `compare_structures` | mcp/src/agents_remember/memory/knowledge/merge_schema.py:142-183 |
| The per-table comparison and the five per-aspect comparators. | `_compare_table`; `_compare_column_details`; `_compare_foreign_keys`; `_compare_indexes`; `_compare_triggers`; `_compare_options` | mcp/src/agents_remember/memory/knowledge/merge_schema.py:186-213; mcp/src/agents_remember/memory/knowledge/merge_schema.py:216-235; mcp/src/agents_remember/memory/knowledge/merge_schema.py:238-255; mcp/src/agents_remember/memory/knowledge/merge_schema.py:258-275; mcp/src/agents_remember/memory/knowledge/merge_schema.py:278-295; mcp/src/agents_remember/memory/knowledge/merge_schema.py:298-315 |
| The index-shape rule that treats an auto-index name as local naming while a declared index name is structure. | `_index_columns` | mcp/src/agents_remember/memory/knowledge/merge_schema.py:369-383 |
| The stable renderings and whitespace normalisation that make the comparison structural rather than textual. | `_normalized_sql`; `_render_column`; `_render_triggers` | mcp/src/agents_remember/memory/knowledge/merge_schema.py:386-389; mcp/src/agents_remember/memory/knowledge/merge_schema.py:392-396; mcp/src/agents_remember/memory/knowledge/merge_schema.py:417-422 |
| The schema generation this manifest must match, and the fingerprint the store stamps. | `SCHEMA_USER_VERSION`; `schema_fingerprint` | mcp/src/agents_remember/memory/knowledge/schema.py:27-27; mcp/src/agents_remember/memory/knowledge/schema.py:375-392 |
| The unit node that refuses seven structural differences plus a reorder, a rename, a weakened trigger body and a changed `user_version`. | "test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate" | mcp/tests/test_knowledge_guarded_merge.py:111-180 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T13:45+02:00 — 260915-KS-L5 curator (uncommitted change set on `ar/260915-ks-l05`, base `3332a4ce`): created this one-to-one card for the new structural preflight. It records the manifest derived from the DDL that creates a database rather than from a second description of it, the first-difference comparison and its most-structural-first order, the index-shape rule that treats an auto-index name as local naming while a declared index's name is structure, and the two boundaries a consumer most needs: the preflight runs before a session exists because SQLite can silently skip a table it cannot match, and it neither repairs nor ignores an unfamiliar table to obtain a green result. The card also records that there is exactly one comparison per input against the declared generation and why a pairwise pass would be unreachable — the statement this leaf's review corrected. Verification metadata remains empty until closeout stamps the code commit.
