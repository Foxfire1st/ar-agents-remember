# mcp/src/agents_remember/models/knowledge_files/documents.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge_files/documents.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T09:30:11+02:00 |
| lastVerifiedCommitHash | `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695`|
| lastVerifiedCommitDate | 2026-09-29T09:57:49+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

**Where each knowledge file lives, and which model reads it (MIK-R21 rules 1 and 2).** The module
docstring is the layout table (records, layout marker, history, census, file and route sidecars);
the functions compute those memory-repository-relative paths and `parse_document` dispatches a
parsed JSON document to its model by its `schema` field. Since MIK-R07 it also reads per-leaf
history files (`ar-history/v1`), binding each file's name to its owner. Since MIK-R20 it also
dispatches the four census schemas (`ar-census-*/v1`, from `census.py`).

## Code Commentary

### Logic

- `RECORD_DIRECTORIES` maps kinds to `knowledge/` directories (`invariants`, `families`, `decisions`,
  `incidents`, `assumptions`, `limitations`, `failure-modes`, `scenarios`, `diagnostics`, `terms`).
- `SCHEMA_MODELS` is every record schema plus the two sidecar schemas, the layout marker and, since
  MIK-R07, `ar-history/v1` → `history.HistoryFile`; `KnowledgeDocument` gains `HistoryFile` too.
  Since MIK-R20, `**CENSUS_MODELS` adds `ar-census-baseline/v1`, `ar-census-inventory/v1`,
  `ar-census-claims/v1` and `ar-census-route/v1`, and `KnowledgeDocument` gains `CensusDocument`, so
  every census file dispatches like any other. `parse_document` refuses a missing or unknown
  `schema`. `parse_document_text` parses strictly through `canonical.parse_json` first.
- `parse_history_document(path, text)` parses a history file and refuses one that is not
  `ar-history/v1` or whose `path` is not `history_path(<its owner id>)`: the file name is the
  owner (leaf, wave or crossing), which is what keeps two leaves from ever writing one file.
- `record_path(kind, id, slug, extension)` → `knowledge/<dir>/<ID>-<slug>.<json|md>`;
  `split_record_filename` inverts it and refuses anything else (including a sequential `INV-0143`).
- `history_path(owner)`, `census_directory(id)`, `file_sidecar_path(source)` (→
  `onboarding/<source>.json`) and `route_sidecar_path(route)` (`.` → `onboarding/overview.json`).

### Conventions

- Paths are POSIX strings relative to the memory repository root; `KNOWLEDGE_ROOT` and
  `ONBOARDING_ROOT` are the two top directories.

### Invariants And Boundaries

- The slug is display only; the ID is the identity.
- This module declares locations; it performs no filesystem access.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The format's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R21@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The models dispatched to come from `records.py` and `sidecars.py`.

| Finding | Anchor | Source |
| --- | --- | --- |
| The layout table. | "knowledge/<kind-dir>/<ID>-<slug>.json" | mcp/src/agents_remember/models/knowledge_files/documents.py:6-6 |
| The schema table, including the history schema and the four census schemas. | `SCHEMA_MODELS`; `HISTORY_SCHEMA`; `CENSUS_MODELS` | mcp/src/agents_remember/models/knowledge_files/documents.py:64-71 |
| The document union gains the census documents. | `KnowledgeDocument`; `CensusDocument` | mcp/src/agents_remember/models/knowledge_files/documents.py:73-75 |
| Schema dispatch, refusing unknown schemas. | `parse_document` | mcp/src/agents_remember/models/knowledge_files/documents.py:84-93 |
| A history file is read only at its owner's path. | `parse_history_document` | mcp/src/agents_remember/models/knowledge_files/documents.py:132-143 |
| Record paths and the filename split. | `record_path`; `split_record_filename` | mcp/src/agents_remember/models/knowledge_files/documents.py:105-112; mcp/src/agents_remember/models/knowledge_files/documents.py:115-121 |
| Sidecar paths, with `.` as the root route. | `file_sidecar_path`; `route_sidecar_path` | mcp/src/agents_remember/models/knowledge_files/documents.py:154-157; mcp/src/agents_remember/models/knowledge_files/documents.py:160-165 |

## Cross-Repo References

No meaningful cross-repo references found: the module reads and writes only files of the memory
repository layout it declares, and calls no sibling repository or external service.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T09:30:11+02:00 — 260928-MIK-L20 curator (uncommitted change set on `ar/260928-mik-l20`, code base `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d` plus the staged delta): **body update — MIK-R20 registers the four `ar-census-*/v1` schemas.** `SCHEMA_MODELS` now spreads `census.CENSUS_MODELS` and `KnowledgeDocument` includes `CensusDocument`; the former Logic statement that census schemas are "deliberately not registered" was false after this change and was replaced. Purpose and Logic were updated, the schema row re-derived (`:64-71`, reworded) and a union row added (`:73-75`); the remaining rows moved by the import and union lines and were re-pointed. The validator still does not read census files through `parsed.py`: they are read by `memory_quality/knowledge_census/files.py`. No verification stamp was advanced.
- 2026-09-29T06:00:00+02:00 — 260928-MIK-L07 curator (uncommitted change set on `ar/260928-mik-l07`, code base `45fe37749b388de348d16ced50c28c03490dce64` plus the working-tree delta): MIK-R07 registers `ar-history/v1` in `SCHEMA_MODELS` and `KnowledgeDocument` and adds `parse_history_document`, which binds a history file's path to its owner. Purpose, Logic and the Repo-Internal table were updated; the sidecar-path row was re-measured to the shifted lines.
- 2026-09-29T04:55:39+02:00 — 260928-MIK-L21 curator (uncommitted change set on `ar/260928-mik-l21`, code base `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` plus the working-tree delta): created this card for the new file MIK-R21 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
