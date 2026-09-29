# mcp/src/agents_remember/memory/knowledge_index/query.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge_index/query.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T08:49:57+02:00 |
| lastVerifiedCommitHash | `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d`|
| lastVerifiedCommitDate | 2026-09-29T09:20:54+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The answers one index gives for one tree (MIK-R23 rule 3).** A `KnowledgeIndex` is one opened index file. Every lookup is a `SELECT` on a read-only connection, and every answer is an `Answer[T]` carrying the index's `IndexState` — the tree key it was built for, `complete` or `partial`, whether the tree is converted, and the files that failed — so a caller cannot present an answer from a partial index as complete without discarding that field.

## Code Commentary

### Logic

- `KnowledgeIndex(path, expected_key=…)` opens the file read-only, reads `ix_meta`, and raises `IndexMismatchError` when the file is not an index, is another `INDEX_FORMAT`, or was built for a different key than expected (rule 5). It then loads the problems and builds `state`.
- The lookups: `entries_at_path` (path → realizations and proofs), `invariant` (the record, its realizations with paths, proofs, families, the links pointing at it other than family membership, and the history rows about it), `family` (members and routes), `families_governing` (every `(family, route)` whose route is the path or one of its ancestors — exact matches from `_self_and_ancestors`, never a name prefix; since MIK-R04, leaf 260928-MIK-L04, the candidate list ends with the root route `.`, so a family routed at `.` governs every path, as the validator's `route_covers` does), `incoming_links` (any record → links pointing at it), `history_rows_of` (a leaf, wave or crossing owner → its rows), `history_rows_about` (a subject → rows across all owners) and `record`.
- `text_id(projected_uuid)` reads `ix_uuid`, the reverse of the projection's identity map.
- `database_path` is the file itself — the dataset the reused read code opens — and `repository_id` is the index's constant namespace.

### Conventions

- Answers are frozen dataclasses (`Entry`, `EntriesAtPath`, `Link`, `HistoryRow`, `Record`, `InvariantKnowledge`, `FamilyKnowledge`) holding the recorded JSON `document`, ordered deterministically.
- `KnowledgeIndex` is a context manager; callers close it.

### Invariants And Boundaries

- Reads stay read-only: the connection is opened with `open_read_only_database`.
- The index never serves an answer built for a different key when the caller states the key.
- A retired record is answered with `status: "retired"`; it is only the projection that leaves it out.
- The index's route match and the validator's `route_covers` agree: a route governs a path when it is the path, an ancestor directory of it, or the root route `.` (review R3-1).

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

The index handle, the answer types and the lookups.

| Finding | Anchor | Source |
| --- | --- | --- |
| The lookup list and the rule that every answer carries the index state. | "every answer carries the index's" | mcp/src/agents_remember/memory/knowledge_index/query.py:1-19 |
| The state every answer carries, and the answer wrapper. | `IndexState`; `Answer` | mcp/src/agents_remember/memory/knowledge_index/query.py:43-54; mcp/src/agents_remember/memory/knowledge_index/query.py:57-62 |
| Opening refuses another format or another tree's key. | `KnowledgeIndex`; `IndexMismatchError`; `expected_key` | mcp/src/agents_remember/memory/knowledge_index/query.py:136-164; mcp/src/agents_remember/memory/knowledge_index/query.py:38-39 |
| The reused read code opens the index file under the index namespace. | `database_path`; `repository_id` | mcp/src/agents_remember/memory/knowledge_index/query.py:178-182; mcp/src/agents_remember/memory/knowledge_index/query.py:184-186 |
| The rule-3 lookups. | `entries_at_path`; `families_governing`; `incoming_links`; `history_rows_of`; `history_rows_about` | mcp/src/agents_remember/memory/knowledge_index/query.py:190-197; mcp/src/agents_remember/memory/knowledge_index/query.py:236-246; mcp/src/agents_remember/memory/knowledge_index/query.py:248-249; mcp/src/agents_remember/memory/knowledge_index/query.py:251-252; mcp/src/agents_remember/memory/knowledge_index/query.py:254-255 |
| The reverse identity lookup and the ancestor match that never matches on a name prefix and ends with the root route. | `text_id`; `_self_and_ancestors` | mcp/src/agents_remember/memory/knowledge_index/query.py:260-266; mcp/src/agents_remember/memory/knowledge_index/query.py:356-365 |
| A family routed at the root governs a root-level file and a deep file. | `test_a_family_routed_at_the_root_governs_every_path` | mcp/tests/test_knowledge_index.py:217-232 |
| The answer cases: path lookups, invariant, family and route, incoming links, and history rows by subject and by leaf (the index query moved here from MIK-R07). | `test_path_lookups_return_realizations_and_proofs`; `test_an_invariant_answers_its_code_tests_families_links_and_history`; `test_a_family_answers_members_and_routes_and_routes_answer_their_families`; `test_incoming_links_reach_any_record`; `test_history_rows_are_found_by_subject_and_by_leaf` | mcp/tests/test_knowledge_index.py:157-168; mcp/tests/test_knowledge_index.py:171-195; mcp/tests/test_knowledge_index.py:198-214; mcp/tests/test_knowledge_index.py:235-240; mcp/tests/test_knowledge_index.py:243-259 |

## Cross-Repo References

No meaningful cross-repo references found: the index reads one memory tree, addressed explicitly by the caller, and nothing else.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): **body update — `_self_and_ancestors` ends with the root route `.`, so `families_governing` answers a family routed at `.` for every path (MIK-R04, review R3-1).** The lookups bullet and the ancestor row are reworded, one invariant and one row added. The other rows were re-pointed by the exact one-line shift of the `ROOT_ROUTE_PATH` import, their claims unchanged. No verification stamp was advanced.
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): created this card for the new file MIK-R23 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
