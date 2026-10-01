# mcp/src/agents_remember/memory/knowledge_index/schema.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The index's own `ix_*` tables (MIK-R23 rule 3) and its format name.** The index file holds two table sets side by side: these tables, which answer rule 3's lookups directly — each relationship the files record once, from its owner's side, is one row, indexed on both ends so the reverse direction is one `SELECT` too — and the knowledge store's logical tables, filled by `projection.py`, so the existing read code runs over the index unchanged.

## Code Commentary

### Logic

- `INDEX_FORMAT` is `ar-knowledge-index/v2` since MIK-R25 (v1 before): projected revision rows now carry the store's own
  payload seal (`projection.py`), so an index built by v1, whose seals the store's revision readers refuse, is treated as
  absent and rebuilt rather than reused (ruling 2026-09-29T22:22:37 Q6). A cached file of another format is treated as
  absent and rebuilt.
- `INDEX_DDL` creates `ix_meta` (name/value: format, key, source, location, state, converted, builtAt), `ix_problem` (path, detail), `ix_record` (id, kind, path, revision, status, document), `ix_entry` (realization or proof: id, kind, invariant, path, sidecar, document), `ix_member` and `ix_route` (family → invariant, family → route), `ix_link` (source, source kind, relation, target kind, target, detail, origin path) and `ix_history_row` (id, owner, owner kind, closed, path, subject, disposition, document).
- Secondary indexes cover the reverse lookups: entries by path and by invariant, members by invariant, routes by route, links by target and by source, history rows by subject and by owner.

### Conventions

- Every table is `STRICT`; each record, entry and row keeps its canonical JSON `document` so a lookup returns what the file recorded.

### Invariants And Boundaries

- Nothing here is authored: every row is a join over recorded fields of one tree's files, and deleting the file loses nothing.

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

The format name and the tables.

- The layout's statement: two table sets, nothing authored, deleting the file loses nothing. [1]
- The format name a cached file must carry to be reused, `ar-knowledge-index/v2` since the MIK-R25 seal fix. [2]
- The `ix_*` tables and their reverse-direction indexes. [3]
- The index file declares its format and key. [4]

### Cross-Repo References

No meaningful cross-repo references found: the index reads one memory tree, addressed explicitly by the caller, and nothing else.

No cross-repo boundary is crossed by this file.
