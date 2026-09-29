# mcp/tests/test_knowledge_index_surfaces.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_index_surfaces.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T08:01:17+02:00 |
| lastVerifiedCommitHash | `ffd043f1354e94a7dcf435e10b4b7224495cbcba`|
| lastVerifiedCommitDate | 2026-09-29T08:30:03+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R23 rule 6 at the worklist scope and the mounted tools.** `construct_registered_scope` over the index through the adapter, retired records never presented as live, and `knowledge_read`, `knowledge_diff` and `knowledge_project` resolving a `databasePath` that names a converted memory tree while keeping today's behaviour for everything else. Registered in the `unit-regression` lane; 10 collected cases.

## Code Commentary

### Logic

- **Registered scope** (parametrized `same-sides` and `candidate-changed`): the scope over the parity database and over its converted tree (base the Git tree, candidate the working tree) has the same members and followed edges, keyed by legacy ID, path, locator, side and edge kind; in the changed case the keys differ and the candidate contributes more edges.
- **Retired records:** a retired invariant and its claim are not projected and not selected by a path read, while the index answers the record as `retired`; a retired family is not projected and is still answered with its members.
- **Mounted tools:** a read by root and by the `knowledge.sqlite` spelling returns a family view with `memoryTree` and writes exactly one cache file named by the key, and is refused without a coordination root; diff between two tree directories names both sides in `memoryTrees` and project publishes with `memoryTree`; an unconverted selection gets today's `selected_input_unavailable` with no `memoryTree` and no cache.
- **Partial and unbuildable:** every surface reports a partial index as incomplete (read: `completeWithinDeclaredScope`, the payload's completeness and `indexComplete` all `false`; diff and project: `indexComplete: false`), with a complete control; with the coordination root pointing at a file, diff and project return `state: refused` rather than raising.
- **Preservation:** a store-authored `knowledge.sqlite` in an unconverted Git root reads identically with and without a coordination root, with no new fields and no cache directory.

### Conventions

- `_converted` and `_partial` build converted trees from the support module; `_canonical` and `_canonical_scope` spell a scope from either side's connection.

### Invariants And Boundaries

- The unconverted-root case uses a real store-authored database, not a fixture file, so the preservation boundary is measured on the shipped path.

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

The cases.

| Finding | Anchor | Source |
| --- | --- | --- |
| The registered scope over the index equals the scope over the database. | `test_the_registered_scope_constructs_the_same_scope_over_the_index` | mcp/tests/test_knowledge_index_surfaces.py:147-230 |
| Retired records are never live. | `test_a_retired_record_is_never_selected_as_live_and_is_answered_as_retired`; `test_a_retired_family_is_never_selected_as_live` | mcp/tests/test_knowledge_index_surfaces.py:243-278; mcp/tests/test_knowledge_index_surfaces.py:392-415 |
| The mounted tools over converted and unconverted selections. | `test_knowledge_read_resolves_a_converted_memory_tree_through_its_index`; `test_knowledge_diff_and_project_resolve_converted_trees`; `test_an_unconverted_selection_keeps_the_database_path` | mcp/tests/test_knowledge_index_surfaces.py:292-385 |
| Partial and unbuildable indexes on every surface. | `test_every_tool_surface_reports_a_partial_index_as_incomplete`; `test_an_unbuildable_index_is_refused_not_raised` | mcp/tests/test_knowledge_index_surfaces.py:427-525 |
| A real database in an unconverted root reads identically. | `test_a_real_database_in_an_unconverted_root_reads_identically` | mcp/tests/test_knowledge_index_surfaces.py:531-553 |
| The lane row. | "mcp/tests/test_knowledge_index_surfaces.py" | mcp/tests/test-evidence-lanes.toml:103-103 |

## Cross-Repo References

No meaningful cross-repo references found: every case builds its own repository under `tmp_path`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): created this card for the new file MIK-R23 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
