# mcp/src/agents_remember/memory/knowledge/merge_schema.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/merge_schema.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:45+02:00 |
| lastVerifiedCommitHash | `9c12e8b1ec027b8bb07f4c0cc79ef99a655ff890` |
| lastVerifiedCommitDate | 2026-09-18T01:58:08+02:00|
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The structural preflight a common-base merge runs before any session exists.** It answers one question about each
input: *is its declared structure exactly the schema generation that input declares?* It answers it from SQLite's
own catalog — tables and their options, ordered columns with types, nullability and primary-key positions, foreign
keys, indexes, triggers and `user_version` — rather than from a version string, because two databases can agree on
`user_version` and disagree about a column type, a foreign key or a trigger.

**Which generation is asked about is itself read from the inputs, first.** `selected_generation(databases,
operation)` reads each of the three inputs' declared generation before anything else, refuses a disagreement — with
the shipped `schema_mismatch` code, naming the positional role that disagreed and the expected/observed versions —
and, when the inputs agree, makes that agreed generation the **operation's selected generation**. The structural
comparison and the session's table attachment then run under it, so a v1/v1/v1 merge on a generation-2 build still
validates and attaches generation 1's ten tables and is byte-comparable to its pre-refactor result. No input is
migrated and no input's generation is chosen as the winner.

**Why it runs before the session.** SQLite's changeset application can silently skip a table it cannot match: the
changeset carries no operation for a table that was never attached, and a table that exists on only one side is
exactly the schema disagreement this preflight refuses. A merge that produced a green result over such a pair would
have dropped a side's entire change set — and SQLite would still have returned success.

## Code Commentary

### Logic

**The generation is read first, and it is read from each input.** `selected_generation(databases, operation)` walks
the three positional inputs (`base`, `left`, `right`), reads each one's declared generation through
`declared_generation(path)` — which opens the file read-only and resolves `PRAGMA user_version` against the
registry, deciding nothing else — and returns the first disagreement as a `schema_mismatch` refusal whose expected
and observed facts are the two versions and whose detail names the positional role that declared the other one.
That refusal is produced **before any session exists**, and it is deliberately not a merge attempt that discovers
the problem later: an input is never migrated, never re-read under another generation, and one input's generation
is never chosen as the winner. An unregistered version takes the `unsupported_schema` refusal path with the
registry's version listing as `expected`, and an unreadable file takes `schema_mismatch`. When all three agree,
`selected_generation` returns that record and the rest of the operation consumes it.

`declared_structure(generation)` derives one generation's manifest by creating **that generation's** DDL in a
private in-memory database and introspecting the result, so the comparison runs against the same source of truth
that creates a database rather than against a second hand-written description of it.
`read_database_structure(path, generation)` / `read_structure(connection, generation)` read one file's actual
catalog under the same generation.

**`DatabaseStructure` carries the generation it was read under**, and that field is load-bearing rather than
descriptive: a structure that has already classified the tables it did not recognise into `extra_tables` can no
longer describe a foreign generation, and re-deriving the generation at comparison time is exactly the partially
threaded shape that read a version-1 input against generation 2 and then asked it for generation 2's tables.

`compare_structures(expected, observed, operation, role=…, generation=…)` returns the **first** structural
difference or `None`, and the checks run most-structural first: a missing table the **selected generation** declares,
then a table that generation does not declare, then the per-table comparison. Within a table, `_compare_table` runs
`_compare_column_details` (ordered names, types, nullability, primary-key positions), `_compare_foreign_keys`
(including deferral and delete actions), `_compare_indexes` (unique and named indexes, by name and by structure),
`_compare_triggers` (the immutability triggers, by name and normalised body) and `_compare_options` (`STRICT` and
`WITHOUT ROWID`, from `pragma_table_list`). The first difference is returned rather than a list, because a caller
acts on the reason the merge did not start and a later difference in the same input would not change that. The
manifest, the column map and the "table this generation does not declare" set all come from the selected
generation, and `_compare_table`'s expected and observed structures travel as one pair alongside it, so no check in
this module can consult a generation other than the one the operation selected.

`require_supported_structure(database_path, operation, *, role, generation=…)` wraps that comparison as a refusal
and carries the role, so a refusal says which of the merge's three positions disagreed rather than only that one
did. `generation` is the operation's selected generation; omitting it makes this function select the input's own
declared generation itself — the same read `selected_generation` performs — which keeps a single-input caller honest
instead of validating against the running build. Its two failure shapes are distinct and stay distinct: a declared
generation this build does not register is an `unsupported_schema` refusal, while a file that cannot be read at all
is a `schema_mismatch`.

**One comparison per input against the selected generation — not a second pass comparing inputs to each other.**
Every accepted input is structurally identical to that one generation, so a pairwise pass would be unreachable: it
could only fire for an input the per-input pass had already refused. `compare_structures` is public because it *is*
that per-input comparison, and it is exposed so a caller can read the difference it found.

### Conventions

- Every compared fact is reduced to a stable rendered string (`_render_column`, `_render_foreign_keys`, `_render_indexes`, `_render_triggers`) and `_normalized_sql` collapses whitespace in a catalog SQL body, so a comparison is over structure rather than formatting.
- `_index_columns` compares an index's *shape* — which declared columns it covers, in order, from `key=1` entries with SQLite's trailing rowid entries excluded — because an auto-index's generated name is local naming rather than dataset structure. A **named** index is separately compared by name inside `_read_table`'s index tuple, because a dropped or renamed declared index is a real schema difference.
- `_INTERNAL_TABLE_PREFIX` excludes `sqlite_*` objects from the "table this generation does not declare" check.

### Invariants And Boundaries

- **It does not repair, migrate, add or drop anything.** Schema reconciliation is explicitly outside this operation,
  and so is migration *between* generations: three inputs that declare different generations are refused, not
  reconciled.
- **The inputs must agree before any session exists.** The generation is read from each input first; a disagreement
  is a `schema_mismatch` refusal naming the positional role and both versions, and the agreed generation — never the
  running build's and never one input's by preference — is what every later step uses. A version-1 merge on a
  generation-2 build therefore stays a version-1 merge.
- **It does not ignore an unfamiliar table to obtain a green result.** An input carrying a table outside the
  selected generation's manifest is not a dataset that generation wrote, so it is refused rather than merged
  around. "Unfamiliar" is the selected generation's word for it, so generation 2's tables are extra tables to a
  generation-1 merge and declared tables to a generation-2 one.
- **`read_structure` writes nothing.** Every read is through the catalog, and `read_database_structure` opens the
  file read-only. The read-only opener also carries the generation-selection read: `declared_generation` cannot
  write the file whose declaration it is learning.
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
| The manifest derived by creating the DDL and introspecting it, so the comparison runs against the same source of truth as the schema itself. | `declared_structure` | mcp/src/agents_remember/memory/knowledge/merge_schema.py:173-188 |
| One canonical table's compared facts, including declared column order and primary-key positions. | "One canonical table's declared structure, as the catalog reports it." | mcp/src/agents_remember/memory/knowledge/merge_schema.py:53-66; mcp/src/agents_remember/memory/knowledge/merge_schema.py:60-73 |
| The catalog reader that answers the structure question without writing anything. | `read_structure`; `read_database_structure` | mcp/src/agents_remember/memory/knowledge/merge_schema.py:191-217; mcp/src/agents_remember/memory/knowledge/merge_schema.py:220-227 |
| The refusal that names which merge role disagreed. | `require_supported_structure` | mcp/src/agents_remember/memory/knowledge/merge_schema.py:226-258 |
| The first-difference comparison and its most-structural-first order. | `compare_structures` | mcp/src/agents_remember/memory/knowledge/merge_schema.py:261-305 |
| The per-table comparison and the five per-aspect comparators. | `_compare_table`; `_compare_column_details`; `_compare_foreign_keys`; `_compare_indexes`; `_compare_triggers`; `_compare_options` | mcp/src/agents_remember/memory/knowledge/merge_schema.py:308-341; mcp/src/agents_remember/memory/knowledge/merge_schema.py:344-363; mcp/src/agents_remember/memory/knowledge/merge_schema.py:366-383; mcp/src/agents_remember/memory/knowledge/merge_schema.py:386-403; mcp/src/agents_remember/memory/knowledge/merge_schema.py:406-423; mcp/src/agents_remember/memory/knowledge/merge_schema.py:426-443 |
| The index-shape rule that treats an auto-index name as local naming while a declared index name is structure. | `_index_columns` | mcp/src/agents_remember/memory/knowledge/merge_schema.py:497-511 |
| The stable renderings and whitespace normalisation that make the comparison structural rather than textual. | `_normalized_sql`; `_render_column`; `_render_triggers` | mcp/src/agents_remember/memory/knowledge/merge_schema.py:514-517; mcp/src/agents_remember/memory/knowledge/merge_schema.py:520-524; mcp/src/agents_remember/memory/knowledge/merge_schema.py:545-550 |
| The schema generation this manifest must match, and the fingerprint the store stamps. | `SCHEMA_USER_VERSION`; `schema_fingerprint` | mcp/src/agents_remember/memory/knowledge/schema.py:27-27; mcp/src/agents_remember/memory/knowledge/schema.py:425-442 |
| The unit node that refuses seven structural differences plus a reorder, a rename, a weakened trigger body and a changed `user_version`. | "def test_every_structural_violation_is_refused_before_a_session_exists(" | mcp/tests/test_knowledge_guarded_merge.py:122-215 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-17T20:39:57+00:00: Generated citation repair: `require_supported_structure` repointed to mcp/src/agents_remember/memory/knowledge/merge_schema.py:226-258. No content impact: mechanical anchor-range projection bound to citation source snapshot b181d6d0b4e4cacc1833ff166c579061a1762313f644c682eec8ffc186d8d42f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:39:57+00:00: Generated citation repair: `compare_structures` repointed to mcp/src/agents_remember/memory/knowledge/merge_schema.py:261-305. No content impact: mechanical anchor-range projection bound to citation source snapshot b181d6d0b4e4cacc1833ff166c579061a1762313f644c682eec8ffc186d8d42f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:39:57+00:00: Generated citation repair: `_index_columns` repointed to mcp/src/agents_remember/memory/knowledge/merge_schema.py:497-511. No content impact: mechanical anchor-range projection bound to citation source snapshot b181d6d0b4e4cacc1833ff166c579061a1762313f644c682eec8ffc186d8d42f; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T19:11+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): **recorded that this preflight now decides *which* generation it is asking about before it asks anything structural, and that the answer is the inputs' own agreement.** The card previously described a preflight against one build-time generation ("is its declared structure exactly the supported schema generation?"), which is false as written: the preflight reads each input's declared generation **first** through `declared_generation`/`selected_generation`, refuses a disagreement **before any session exists** with the shipped `schema_mismatch` code naming the positional role and the expected/observed versions, and — the part a future reader must not flatten — when the inputs agree, that agreed generation *is* the operation's selected generation. Everything downstream is threaded from it: `declared_structure(generation)`, `read_structure(connection, generation)`, `read_database_structure(path, generation)`, `compare_structures(…, generation=…)`, `_compare_table`'s manifest/column map, and the session's table-attachment set, so a **v1/v1/v1 merge on this generation-2 build still validates and attaches generation 1's ten tables** and is byte-comparable to its pre-refactor result. `DatabaseStructure` now carries the generation it was read under, because a structure that has already classified unrecognised tables into `extra_tables` can no longer describe a foreign generation — the partially threaded shape that validated a version-1 input against generation 2 and then asked it for generation 2's tables. The shipped silent-skip failure stays stated as the reason the preflight runs before a session: a table present on only one side is a change set that vanishes while SQLite still returns success. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate` in the row 73 of this card from mcp/tests/test_knowledge_guarded_merge.py:111-180 to mcp/tests/test_knowledge_guarded_merge.py:248-250, the extent of the construct the claim is about (the checker named line(s) [19, 248] as its live location)
- 2026-09-16T13:45+02:00 — 260915-KS-L5 curator (uncommitted change set on `ar/260915-ks-l05`, base `3332a4ce`): created this one-to-one card for the new structural preflight. It records the manifest derived from the DDL that creates a database rather than from a second description of it, the first-difference comparison and its most-structural-first order, the index-shape rule that treats an auto-index name as local naming while a declared index's name is structure, and the two boundaries a consumer most needs: the preflight runs before a session exists because SQLite can silently skip a table it cannot match, and it neither repairs nor ignores an unfamiliar table to obtain a green result. The card also records that there is exactly one comparison per input against the declared generation and why a pairwise pass would be unreachable — the statement this leaf's review corrected. Verification metadata remains empty until closeout stamps the code commit.
