# mcp/src/agents_remember/memory/knowledge_index/build.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**Build one index file from one memory tree's files (MIK-R23 rules 1, 3 and Failure).** The builder parses the selected `MemoryTreeSnapshot` and writes its relationships into the `ix_*` and projected logical tables. When the snapshot identifies a repository, the build uses its Git objects to verify recorded review evidence.

## Code Commentary

The reviewer child's enabled memo shares document parses keyed by the exact bytes' SHA-256 and retains up to 65,536 entries under a 256 MiB retained charge. Each tree still validates the document's placement. An oversized parse can serve the current reader without entering the memo.

### Logic

- `parse_tree(snapshot)` walks indexed JSON files in sorted order into a `ParsedTree` (records, entries, file and route sidecars, histories, the layout marker, problems). Markdown prose companions are skipped before decoding and parsing; their bytes are retained by the snapshot for worklist comparison, not interpreted as JSON. A JSON file that fails to decode or parse is appended to `problems` with its path and the first 2,000 characters of the reason; `ParsedTree.state` is `partial` when any problem exists.
- `_parse_knowledge_file` accepts only `knowledge/<kind-dir>/<file>.json`: `history/` attempt files parse as `HistoryFile` keyed by owner. The converted review catalog has separate parsing and contributes its review evidence; any other directory must be a record directory, the record must be that directory's kind, its ID must equal the file name's ID, and a second file claiming an ID already indexed is a problem.
- `_parse_onboarding_file` accepts file sidecars (whose `path` must map back to where the sidecar sits, and whose realization and proof entry IDs must be unique across the tree) and route sidecars (same location rule); any other onboarding JSON is a problem.
- `build_index(snapshot, destination)` opens a new SQLite file with journaling off, runs `create_or_validate_schema` (the store's logical tables), then in one transaction

When writing `ix_revision` rows, the builder also populates each revision's `consolidation` outcome column from closed consolidation history files via `consolidation_outcomes`. creates the `ix_*` tables, writes the rows and named revisions, populates the derived FTS5 table via `populate_fts(connection, parsed)`, calls `projection.project`, and writes `ix_meta`. It returns a `BuildReport` (key, state, converted, problems, record/entry/history-row counts).
- `_write_rows` writes problems, records (with `ix_member`/`ix_route` for a family and `member`/`supersedes` links), entries (with the anchor's `path` filled from the sidecar), sidecar references as `cites` links (record, anchor or requirement endpoints), and history rows with their `because` links.
- `_write_link` classifies a link target: an `Anchor`, a `RequirementReference` (keyed `repository/path#id@version`), a `route:` target, or a record ID.
- **History files by path, and each owner's merged history (L37 reopen ruling).** `ParsedTree.history_files` holds
  every history file by its path. `ParsedTree.histories` is each owner's history read as one: when a second file
  of the same owner is parsed, `merged_leaf_history` merges the owner's files in attempt order. `_write_rows`
  writes every file's rows under its own path (`_write_history(connection, path, history)`), and the
  `BuildReport`'s row count sums the files, so a reopened leaf's closed file and later attempt are both indexed.

### Conventions

- `_Owner` is the owner side of a recorded relationship (source, kind, file), so every `ix_link` row names where it was recorded.
- JSON cells are written sorted and compact (`_json`).

### Invariants And Boundaries

- **A file that fails its schema is reported, never guessed at**: the index is marked `partial`, the file is named, and the rest of the tree is indexed.
- The only `partial` causes beyond a schema failure are a file at a location its format does not allow and a duplicate record or entry ID — cases the index cannot answer without choosing. Every other integrity rule is the validator's (MIK-R22).
- The selected tree's history and eligible exact-content evidence supply revision standing. The build stores standing beside record status and stores named revisions in `ix_revision` for the writer aggregate. These observations are derived during the build.

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

The parser, the builder and the row writers.



- What one build reports. [3]

- Parsing skips Markdown companions before decoding; indexed JSON decode/schema failures become named problems. 

- Location, kind, file-name and duplicate-ID rules for record and sidecar files. 
- The metadata row set a cached file is checked against. [8]
- A file failing its schema marks the index partial and is named; an unconverted tree indexes empty. [9]

- The parsed tree keeps each history file by path and each owner's merged history. 
- History rows are written per file, under the file's own path. [11]

### Cross-Repo References

No meaningful cross-repo references found: the index reads one memory tree, addressed explicitly by the caller, and nothing else.

No cross-repo boundary is crossed by this file.


- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/memory/knowledge_index/build.py::parse_tree - the bytes it recorded now occur 3 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/memory/knowledge_index/build.py::_parse_onboarding_file - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/memory/knowledge_index/build.py::_parse_knowledge_file - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.

- The index builds record standing, named-revision rows, and `ix_fts` together in its write transaction. [16]

- A converted review catalog is parsed as review evidence separately from owner attempts. [17]

- The builder names parse problems and derives revision standing from the selected memory tree's history and exact review evidence. [1]

- The parsed tree keeps each history file by path and each owner's merged history. [10]

- One transaction: the store schema, the `ix_*` tables, the rows, `populate_fts`, the projection and the metadata. [6]
- The row writers: records, entries, members, routes, links, references and history rows. [7]
- The parsed tree and its completeness. [2]
