# mcp/src/agents_remember/memory/knowledge_index/query.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge_index/query.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T08:49:57+02:00 |
| lastVerifiedCommitHash | `e49ba07865b3848cd36759cea6b37bba7d0d51c3`|
| lastVerifiedCommitDate | 2026-09-29T15:47:03+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The answers one index gives for one tree (MIK-R23 rule 3).** A `KnowledgeIndex` is one opened index file. Every lookup is a `SELECT` on a read-only connection, and every answer is an `Answer[T]` carrying the index's `IndexState` — the tree key it was built for, `complete` or `partial`, whether the tree is converted, and the files that failed — so a caller cannot present an answer from a partial index as complete without discarding that field.

## Code Commentary

### Logic

- `KnowledgeIndex(path, expected_key=…)` opens the file read-only, reads `ix_meta`, and raises `IndexMismatchError` when the file is not an index, is another `INDEX_FORMAT`, or was built for a different key than expected (rule 5). It then loads the problems and builds `state`.
- The lookups: `entries_at_path` (path → realizations and proofs), `invariant` (the record, its realizations with paths, proofs, families, the links pointing at it other than family membership, and the history rows about it), `family` (members and routes), `families_governing` (every `(family, route)` whose route is the path or one of its ancestors — exact matches from `_self_and_ancestors`, never a name prefix; since MIK-R04, leaf 260928-MIK-L04, the candidate list ends with the root route `.`, so a family routed at `.` governs every path, as the validator's `route_covers` does), `incoming_links` (any record → links pointing at it), `history_rows_of` (a leaf, wave or crossing owner → its rows), `history_rows_about` (a subject → rows across all owners) and `record`.
- Since MIK-R28 two more lookups: `proofs_of(invariant_ids)` (the `proof` entries of those invariants) and `invariants_without_proof()` (the live invariants no proof entry names). See the section below.
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

## 260928-MIK-L28 Proof Lookups (MIK-R28 Rules 4 And 5)

- `proofs_of(invariant_ids)` answers the `ix_entry` rows of kind `proof` whose invariant is one of the
  given IDs, by path then entry ID. An empty list answers `()` without a query. `knowledge_proofs.view_proofs`
  uses it for the `invariant` view (one ID) and the `family` view (every member).
- `invariants_without_proof()` answers every **live** invariant (`status != 'retired'`) that no proof
  entry names, by ID. A retired invariant is not listed. The docstring states the rule-5 boundary: the list
  is information, not a gate, because the admission rule (MIK-R27) accepts criteria other than a proving
  test.
- Both answers carry the index state like every other lookup, so a partial index is never read as a
  complete "without proof" list.

| Finding | Anchor | Source |
| --- | --- | --- |
| The proofs of a set of invariants. | `proofs_of` | mcp/src/agents_remember/memory/knowledge_index/query.py:260-268 |
| The live invariants no proof names; information, not a gate. | `invariants_without_proof`; "status != 'retired'" | mcp/src/agents_remember/memory/knowledge_index/query.py:270-282 |
| A retired invariant is excluded from the list. | `test_the_index_lists_live_invariants_without_proof` | mcp/tests/test_knowledge_proofs.py:343-356 |

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
| The lookup list and the rule that every answer carries the index state. | "every answer carries the index's" | mcp/src/agents_remember/memory/knowledge_index/query.py:1-22 |
| The state every answer carries, and the answer wrapper. | `IndexState`; `Answer` | mcp/src/agents_remember/memory/knowledge_index/query.py:46-57; mcp/src/agents_remember/memory/knowledge_index/query.py:60-65 |
| Opening refuses another format or another tree's key. | `KnowledgeIndex`; `IndexMismatchError`; `expected_key` | mcp/src/agents_remember/memory/knowledge_index/query.py:139-167; mcp/src/agents_remember/memory/knowledge_index/query.py:41-42 |
| The reused read code opens the index file under the index namespace. | `database_path`; `repository_id` | mcp/src/agents_remember/memory/knowledge_index/query.py:181-185; mcp/src/agents_remember/memory/knowledge_index/query.py:187-189 |
| The rule-3 lookups. | `entries_at_path`; `families_governing`; `incoming_links`; `history_rows_of`; `history_rows_about` | mcp/src/agents_remember/memory/knowledge_index/query.py:193-200; mcp/src/agents_remember/memory/knowledge_index/query.py:239-249; mcp/src/agents_remember/memory/knowledge_index/query.py:251-252; mcp/src/agents_remember/memory/knowledge_index/query.py:254-255; mcp/src/agents_remember/memory/knowledge_index/query.py:257-258 |
| The reverse identity lookup and the ancestor match that never matches on a name prefix and ends with the root route. | `text_id`; `_self_and_ancestors` | mcp/src/agents_remember/memory/knowledge_index/query.py:287-293; mcp/src/agents_remember/memory/knowledge_index/query.py:383-392 |
| A family routed at the root governs a root-level file and a deep file. | `test_a_family_routed_at_the_root_governs_every_path` | mcp/tests/test_knowledge_index.py:217-232 |
| The answer cases: path lookups, invariant, family and route, incoming links, and history rows by subject and by leaf (the index query moved here from MIK-R07). | `test_path_lookups_return_realizations_and_proofs`; `test_an_invariant_answers_its_code_tests_families_links_and_history`; `test_a_family_answers_members_and_routes_and_routes_answer_their_families`; `test_incoming_links_reach_any_record`; `test_history_rows_are_found_by_subject_and_by_leaf` | mcp/tests/test_knowledge_index.py:157-168; mcp/tests/test_knowledge_index.py:171-195; mcp/tests/test_knowledge_index.py:198-214; mcp/tests/test_knowledge_index.py:235-240; mcp/tests/test_knowledge_index.py:243-259 |

## Cross-Repo References

No meaningful cross-repo references found: the index reads one memory tree, addressed explicitly by the caller, and nothing else.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T15:26:13+02:00 — 260928-MIK-L28 curator (uncommitted change set on `ar/260928-mik-l28`, code base `8b0254263c6998b1d4814b2e97c1bd231d39350f` plus the working-tree delta and untracked files): **body update — two proof lookups.** Added a Logic bullet and the section "260928-MIK-L28 Proof Lookups": `proofs_of` and `invariants_without_proof` (live invariants only; information, not a gate). Three cited rows. The module docstring's lookup list grew by three lines, so every range below it moved; the rows were re-pointed by the exact base-to-working line map (they are multi-anchor rows the installed fixer declined), and the "lookup list" row now ends at `:22`. No claim wording changed there. No verification stamp was advanced.
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): **body update — `_self_and_ancestors` ends with the root route `.`, so `families_governing` answers a family routed at `.` for every path (MIK-R04, review R3-1).** The lookups bullet and the ancestor row are reworded, one invariant and one row added. The other rows were re-pointed by the exact one-line shift of the `ROOT_ROUTE_PATH` import, their claims unchanged. No verification stamp was advanced.
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): created this card for the new file MIK-R23 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
