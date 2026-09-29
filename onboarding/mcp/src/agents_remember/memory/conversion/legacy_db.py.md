# mcp/src/agents_remember/memory/conversion/legacy_db.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/conversion/legacy_db.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T14:21:42+02:00 |
| lastVerifiedCommitHash | `8b0254263c6998b1d4814b2e97c1bd231d39350f`|
| lastVerifiedCommitDate | 2026-09-29T15:00:35+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The read-only legacy database reader and the one-time export (MIK-R24 rules 4 and 9).** The committed
`knowledge.sqlite` is read, never written. Every line and every user converts through this reader, so it
outlives the database code, which MIK-R26 retires. Each invariant and family is exported at its head
revision as a record file, and every realization claim on a head revision becomes a `realizes` entry.

## Code Commentary

### Logic

- `export_database(database, objects)` opens the file with `SQLITE_OPEN_READONLY` and runs `_export`.
- **Heads and depth (`_heads`).** A head is the revision no predecessor row names as parent. `revision`
  is its depth in the predecessor chain, with the root at 1. On the real tree the depths are 37 / 54 / 3.
  A cycle, or a second head for one identity, raises `ExportError`.
- **Records.** The `id` is `derived_record_id(kind, legacy_id)`, and the legacy ID is kept in
  `origin.legacyId`. A collision among derived IDs refuses, naming both legacy IDs. The slug comes from
  `display_label` (`slug`), and `status` from `state_at_origin` (`_status` refuses a value with no
  text-format status). `conditions` lines beginning `Hand-off kind:`, `Producer's disposition:` or
  `Evidence:` (`HANDOFF_PREFIXES`) move to `origin.handoff.evidence`. Families get `routes: []` (MIK-R04
  `route_unassigned`), and every record gets `admission: "legacy-unassessed"`.
- **Origins (`_Origins`).** `origin.task` and `origin.leaf` come from the head's `provenance.actor_ref`.
  A parenthesised leaf ID (`… (260921-ICR-L30)`) gives both. A leaf-document path
  (`…/<task-dir>/NN_<slug>.json`) gives the leaf `<task>-LNN`, where the task ID is learned from a
  parenthesised leaf in the same task directory, so the export stays a pure function of the database.
  Otherwise the task alone is given.
- **Realizations (`_export_realizations`).** Every claim on a head revision becomes an entry with ID
  `derived_realization_id(legacy invariant, path, new locator)`, not the claim ID, which changes on every
  revision. A collision refuses, naming both legacy claims. The anchor keeps the claim's recorded blob and
  translated locator (`_new_locator`), and `content` is computed in that recorded blob, with the top-level
  reading. A claim that does not resolve in its recorded blob refuses the export. A claim bound only
  through the top-level reading is listed (`disambiguated`). The hand-off role `incidental` is written
  `support`, per MIK-R12's ruling.

### Conventions

- Table and column names are the real schema's spelling. The test fixture builds only those tables and
  columns, so the export runs the same queries on the fixture as on a real `knowledge.sqlite`.

### Invariants And Boundaries

- **Nothing is re-hashed at the conversion's code tree**, so staleness recorded in the database stays
  visible (D9). Earlier revisions stay readable in the Git history of `knowledge.sqlite`.
- **A derived-ID collision is never resolved silently**, because a silent rule could resolve differently on
  different lines.
- The export authors no knowledge: records carry the database's text, with only the hand-off lines moved.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R24@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`24_conversion-and-boundary-crossing.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The reader, the heads, the origins and the export.

| Finding | Anchor | Source |
| --- | --- | --- |
| The read-only open. | `export_database` | mcp/src/agents_remember/memory/conversion/legacy_db.py:181-188 |
| Head revisions and their depth in the predecessor chain. | `_heads` | mcp/src/agents_remember/memory/conversion/legacy_db.py:79-114 |
| Task and leaf from `actor_ref`, learned per task directory. | `_Origins` | mcp/src/agents_remember/memory/conversion/legacy_db.py:117-141 |
| Hand-off lines leave `conditions`. | `HANDOFF_PREFIXES`; `_split_conditions` | mcp/src/agents_remember/memory/conversion/legacy_db.py:46-46; mcp/src/agents_remember/memory/conversion/legacy_db.py:144-147 |
| Records: derived IDs, collisions refused, status, revision, admission, family routes. | `_export` | mcp/src/agents_remember/memory/conversion/legacy_db.py:191-276 |
| Entries in their recorded blobs, derived IDs from (invariant, path, locator), collisions refused. | `_export_realizations`; `_new_locator` | mcp/src/agents_remember/memory/conversion/legacy_db.py:279-333; mcp/src/agents_remember/memory/conversion/legacy_db.py:157-169 |
| The export matches a legacy database in the real column spelling. | `test_the_database_exports_head_records_and_entries_in_their_recorded_blobs` | mcp/tests/test_knowledge_conversion.py:176-219 |
| The fixture database. | `legacy_database` | mcp/tests/knowledge_conversion_test_support.py:192-297 |

## Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): created this card for the new file MIK-R24 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
