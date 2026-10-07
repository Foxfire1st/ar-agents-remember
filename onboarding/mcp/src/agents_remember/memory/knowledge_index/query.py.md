# mcp/src/agents_remember/memory/knowledge_index/query.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The answers one index gives for one tree (MIK-R23 rule 3).** A `KnowledgeIndex` is one opened index file. Every lookup is a `SELECT` on a read-only connection, and every answer is an `Answer[T]` carrying the index's `IndexState` — the tree key it was built for, `complete` or `partial`, whether the tree is converted, and the files that failed — so a caller cannot present an answer from a partial index as complete without discarding that field.

## Code Commentary

### Logic

- `KnowledgeIndex(path, expected_key=…)` opens the file read-only, reads `ix_meta`, and raises `IndexMismatchError` when the file is not an index, is another `INDEX_FORMAT`, or was built for a different key than expected (rule 5). It then loads the problems and builds `state`.
- The lookups: `entries_at_path` (path → realizations and proofs), `invariant` (the record, its realizations with paths, proofs, families, the links pointing at it other than family membership, and the history rows about it), `family` (members and routes), `families_governing` (every `(family, route)` whose route is the path or one of its ancestors — exact matches from `_self_and_ancestors`, never a name prefix; since MIK-R04, leaf 260928-MIK-L04, the candidate list ends with the root route `.`, so a family routed at `.` governs every path, as the validator's `route_covers` does), `incoming_links` (any record → links pointing at it), `history_rows_of` (a leaf, wave or crossing owner → its rows), `history_rows_about` (a subject → rows across all owners) and `record`.
- Since MIK-R28 two more lookups: `proofs_of(invariant_ids)` (the `proof` entries of those invariants) and `invariants_without_proof()` (the live invariants no proof entry names). See the section below.
- Since MIK-R25, `record_ids(kind)` answers every record ID of one kind in the tree, sorted: the reviewer's per-side currentness (`application/review_tree_knowledge.side_currentness`) asks it for every `invariant` and `family`.
- Since MIK-R29, five lookups serve the path-based knowledge reader: `entries_under(directory)`, `entries_in_directory(directory)`, `live_entry_paths_under(directory)`, `links_to_path(path)` and `records_of_kind(kind)`. See the section below. `_incoming` now delegates to a shared `_links(where, parameters)` with the same SQL and the same `ORDER BY`, so the MIK-R05 and MIK-R25 callers are unaffected.
- `text_id(projected_uuid)` reads `ix_uuid`, the reverse of the projection's identity map.
- `database_path` is the file itself — the dataset the reused read code opens — and `repository_id` is the index's constant namespace.
- `history_row(row_id)` (L37) answers one history row by its ID, or `None`. The reader uses it to name the
  record a row is about when a link's source is a history row.

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

- The proofs of a set of invariants. [1]
- The live invariants no proof names; information, not a gate. [2]
- A retired invariant is excluded from the list. [3]

## 260928-MIK-L29 The Reader's Directory, Path And Record Lookups

Five additive lookups, each an ordinary `Answer[T]` carrying the index state, serve the path-based knowledge reader
(`application/knowledge_reader`, MIK-R29):

- `entries_under(directory)`: the realization and proof entries at the directory or any path below it; the root
  route `.` (or an empty directory) holds every entry. **A path prefix never matches a sibling that merely shares
  its spelling:** `dash` holds `dash/x`, not `dashboard/x` (`_under` matches the path itself or `substr` against
  `<directory>/`). The reader's `subtree` view pages these.
- `entries_in_directory(directory)`: the entries of the files **directly** in the directory, not in its
  subdirectories (no further `/` after the prefix): the bounded directory view's own-level entries (review F2).
- `live_entry_paths_under(directory)`: the source path of every entry at or under the directory whose invariant is a
  live record (joined with `ix_record`, not retired, not missing), one per entry: the counts the explorer, the
  directory summary and the subtree agree on.
- `links_to_path(path)`: every relationship whose target is the code anchor or route at the path, through the
  shared `_links`.
- `records_of_kind(kind)`: every record of one kind by ID, built on `record_ids`: the reader's record list and the
  decisions its derived superseded status is computed from.

The unused `outgoing_links` the first version added was removed (review F12). The helpers `_prefix`, `_under` and
`_split` are module-level and private.

- Entries at or under a directory; a sibling sharing the prefix is never matched. [4]
- Entries of the files directly in a directory (F2). [5]
- Live entry paths under a directory, for the reader's counts. [6]
- Links to a path's anchors or route; every record of one kind. [7]
- `_incoming` delegating to the shared link query, same SQL and order. [8]
- The directory condition and the prefix it is built from. [9]
- The sibling-prefix, own-level, retired-count and route-link cases. [10]


## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The index's design authority is the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the requirement
packet `MIK-R23@v1` of task `260928_maintained-invariant-knowledge`; both live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The index handle, the answer types and the lookups.

- The lookup list and the rule that every answer carries the index state. [11]
- Every record ID of one kind, sorted: the reviewer's per-side currentness (MIK-R25) and, since MIK-R29, the reader's `records_of_kind`. [12]
- The state every answer carries, and the answer wrapper. [13]

- Opening refuses another format or another tree's key. [14]

- The reused read code opens the index file under the index namespace. [15]
- The rule-3 lookups. [16]
- The reverse identity lookup and the ancestor match that never matches on a name prefix and ends with the root route. [17]
- A family routed at the root governs a root-level file and a deep file. [18]
- The answer cases: path lookups, invariant, family and route, incoming links, and history rows by subject and by leaf (the index query moved here from MIK-R07). [19]

- One history row by its ID. [20]

### Cross-Repo References

No meaningful cross-repo references found: the index reads one memory tree, addressed explicitly by the caller, and nothing else.

No cross-repo boundary is crossed by this file.
