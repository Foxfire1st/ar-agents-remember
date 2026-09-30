# mcp/src/agents_remember/memory/knowledge_index/schema.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge_index/schema.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T04:01:40+02:00 |
| lastVerifiedCommitHash | `8a2d4b478971bf40cca0f24d5e5d24a0844bd563`|
| lastVerifiedCommitDate | 2026-09-30T04:16:14+02:00|
| governingOverview | `../overview.md` |

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

The format name and the tables.

| Finding | Anchor | Source |
| --- | --- | --- |
| The layout's statement: two table sets, nothing authored, deleting the file loses nothing. | "Nothing here is authored" | mcp/src/agents_remember/memory/knowledge_index/schema.py:1-15 |
| The format name a cached file must carry to be reused, `ar-knowledge-index/v2` since the MIK-R25 seal fix. | `INDEX_FORMAT` | mcp/src/agents_remember/memory/knowledge_index/schema.py:23-23 |
| The `ix_*` tables and their reverse-direction indexes. | `INDEX_DDL`; `ix_link`; `ix_history_row` | mcp/src/agents_remember/memory/knowledge_index/schema.py:25-103 |
| The index file declares its format and key. | `test_the_index_file_declares_its_format_and_key` | mcp/tests/test_knowledge_index.py:403-414 |

## Cross-Repo References

No meaningful cross-repo references found: the index reads one memory tree, addressed explicitly by the caller, and nothing else.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T04:01:40+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): **body updated for MIK-R25.** `INDEX_FORMAT` is now `ar-knowledge-index/v2`, so v1 caches (whose revision seals the store refuses) are rebuilt (ruling 22:22:37 Q6). **Reopened claim re-read and reworded:** the `INDEX_FORMAT` Logic bullet and row now name v2 and why; the bullet this pass's fixer wrote for that row was removed because the claim was reworded. No verification stamp was advanced.
- 2026-09-30T01:47:37+00:00: Generated citation repair: `test_the_index_file_declares_its_format_and_key` repointed to mcp/tests/test_knowledge_index.py:403-414. No content impact: mechanical anchor-range projection bound to citation source snapshot a85c638de10bc300eb93d4b69fedcbaf6e141873de546e8335d0f51f59402273; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): created this card for the new file MIK-R23 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
