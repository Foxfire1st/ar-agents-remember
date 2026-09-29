# mcp/src/agents_remember/models/knowledge_files/documents.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge_files/documents.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T04:55:39+02:00 |
| lastVerifiedCommitHash | `45fe37749b388de348d16ced50c28c03490dce64`|
| lastVerifiedCommitDate | 2026-09-29T05:18:17+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

**Where each knowledge file lives, and which model reads it (MIK-R21 rules 1 and 2).** The module
docstring is the layout table (records, layout marker, history, census, file and route sidecars);
the functions compute those memory-repository-relative paths and `parse_document` dispatches a
parsed JSON document to its model by its `schema` field.

## Code Commentary

### Logic

- `RECORD_DIRECTORIES` maps kinds to `knowledge/` directories (`invariants`, `families`, `decisions`,
  `incidents`, `assumptions`, `limitations`, `failure-modes`, `scenarios`, `diagnostics`, `terms`).
- `SCHEMA_MODELS` is every record schema plus the two sidecar schemas and the layout marker;
  `parse_document` refuses a missing or unknown `schema` (history and census schemas belong to
  MIK-R07 and MIK-R20 and are deliberately not registered). `parse_document_text` parses strictly
  through `canonical.parse_json` first.
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
| Schema dispatch, refusing unknown schemas. | `parse_document` | mcp/src/agents_remember/models/knowledge_files/documents.py:76-85 |
| Record paths and the filename split. | `record_path`; `split_record_filename` | mcp/src/agents_remember/models/knowledge_files/documents.py:97-104; mcp/src/agents_remember/models/knowledge_files/documents.py:107-113 |
| Sidecar paths, with `.` as the root route. | `file_sidecar_path`; `route_sidecar_path` | mcp/src/agents_remember/models/knowledge_files/documents.py:132-135; mcp/src/agents_remember/models/knowledge_files/documents.py:138-143 |

## Cross-Repo References

No meaningful cross-repo references found: the module reads and writes only files of the memory
repository layout it declares, and calls no sibling repository or external service.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T04:55:39+02:00 — 260928-MIK-L21 curator (uncommitted change set on `ar/260928-mik-l21`, code base `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` plus the working-tree delta): created this card for the new file MIK-R21 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
