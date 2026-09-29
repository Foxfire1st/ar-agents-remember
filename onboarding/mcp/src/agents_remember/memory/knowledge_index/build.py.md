# mcp/src/agents_remember/memory/knowledge_index/build.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge_index/build.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T08:01:17+02:00 |
| lastVerifiedCommitHash | `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d`|
| lastVerifiedCommitDate | 2026-09-29T09:20:54+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**Build one index file from one memory tree's files (MIK-R23 rules 1, 3 and Failure).** The builder reads a `MemoryTreeSnapshot` and nothing else — no database, no working directory, no second tree — parses every knowledge file through the MIK-R21/R07 models, and writes one row per recorded relationship into the `ix_*` tables and the projected logical tables.

## Code Commentary

### Logic

- `parse_tree(snapshot)` walks the files in sorted order into a `ParsedTree` (records, entries, file and route sidecars, histories, the layout marker, problems). A file that fails to decode or parse is appended to `problems` with its path and the first 2,000 characters of the reason; `ParsedTree.state` is `partial` when any problem exists.
- `_parse_knowledge_file` accepts only `knowledge/<kind-dir>/<file>.json`: `history/` files parse as `HistoryFile` keyed by owner; any other directory must be a record directory, the record must be that directory's kind, its ID must equal the file name's ID, and a second file claiming an ID already indexed is a problem.
- `_parse_onboarding_file` accepts file sidecars (whose `path` must map back to where the sidecar sits, and whose realization and proof entry IDs must be unique across the tree) and route sidecars (same location rule); any other onboarding JSON is a problem.
- `build_index(snapshot, destination)` opens a new SQLite file with journaling off, runs `create_or_validate_schema` (the store's logical tables), then in one transaction creates the `ix_*` tables, writes the rows, calls `projection.project`, and writes `ix_meta`. It returns a `BuildReport` (key, state, converted, problems, record/entry/history-row counts).
- `_write_rows` writes problems, records (with `ix_member`/`ix_route` for a family and `member`/`supersedes` links), entries (with the anchor's `path` filled from the sidecar), sidecar references as `cites` links (record, anchor or requirement endpoints), and history rows with their `because` links.
- `_write_link` classifies a link target: an `Anchor`, a `RequirementReference` (keyed `repository/path#id@version`), a `route:` target, or a record ID.

### Conventions

- `_Owner` is the owner side of a recorded relationship (source, kind, file), so every `ix_link` row names where it was recorded.
- JSON cells are written sorted and compact (`_json`).

### Invariants And Boundaries

- **A file that fails its schema is reported, never guessed at**: the index is marked `partial`, the file is named, and the rest of the tree is indexed.
- The only `partial` causes beyond a schema failure are a file at a location its format does not allow and a duplicate record or entry ID — cases the index cannot answer without choosing. Every other integrity rule is the validator's (MIK-R22).
- Nothing is derived beyond joins over recorded fields.

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

The parser, the builder and the row writers.

| Finding | Anchor | Source |
| --- | --- | --- |
| The builder's contract: one snapshot in, problems named, nothing derived. | "A file that fails its schema is reported, never guessed at." | mcp/src/agents_remember/memory/knowledge_index/build.py:1-16 |
| The parsed tree and its completeness. | `ParsedTree`; `state` | mcp/src/agents_remember/memory/knowledge_index/build.py:90-104 |
| What one build reports. | `BuildReport` | mcp/src/agents_remember/memory/knowledge_index/build.py:107-117 |
| Parsing: every failure becomes a named problem. | `parse_tree`; `_parse_file` | mcp/src/agents_remember/memory/knowledge_index/build.py:120-129; mcp/src/agents_remember/memory/knowledge_index/build.py:167-178 |
| Location, kind, file-name and duplicate-ID rules for record and sidecar files. | `_parse_knowledge_file`; `_parse_onboarding_file` | mcp/src/agents_remember/memory/knowledge_index/build.py:181-201; mcp/src/agents_remember/memory/knowledge_index/build.py:204-226 |
| One transaction: the store schema, the `ix_*` tables, the rows, the projection and the metadata. | `build_index` | mcp/src/agents_remember/memory/knowledge_index/build.py:132-159 |
| The row writers: records, entries, members, routes, links, references and history rows. | `_write_rows`; `_write_record`; `_write_link`; `_write_references`; `_reference_endpoint`; `_link`; `_write_history` | mcp/src/agents_remember/memory/knowledge_index/build.py:243-271; mcp/src/agents_remember/memory/knowledge_index/build.py:274-302; mcp/src/agents_remember/memory/knowledge_index/build.py:326-338; mcp/src/agents_remember/memory/knowledge_index/build.py:383-407; mcp/src/agents_remember/memory/knowledge_index/build.py:305-323; mcp/src/agents_remember/memory/knowledge_index/build.py:369-380; mcp/src/agents_remember/memory/knowledge_index/build.py:341-354 |
| The metadata row set a cached file is checked against. | `_write_meta` | mcp/src/agents_remember/memory/knowledge_index/build.py:410-422 |
| A file failing its schema marks the index partial and is named; an unconverted tree indexes empty. | `test_a_file_failing_its_schema_marks_the_index_partial_and_is_named`; `test_an_unconverted_tree_is_indexed_empty_and_says_so` | mcp/tests/test_knowledge_index.py:285-313; mcp/tests/test_knowledge_index.py:316-327 |

## Cross-Repo References

No meaningful cross-repo references found: the index reads one memory tree, addressed explicitly by the caller, and nothing else.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`test_knowledge_index.py`) were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact base-to-working line map; no claim wording changed. No verification stamp was advanced.
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): created this card for the new file MIK-R23 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
