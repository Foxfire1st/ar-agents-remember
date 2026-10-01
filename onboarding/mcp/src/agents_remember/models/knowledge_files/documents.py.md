# mcp/src/agents_remember/models/knowledge_files/documents.py

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
  `ar-history/v1` or whose `path` is not `history_path(<its owner id>, <its attempt>)`: the file name is the
  owner (leaf, wave or crossing) and, for a reopened leaf, its attempt, which is what keeps two leaves from
  ever writing one file.
- `record_path(kind, id, slug, extension)` → `knowledge/<dir>/<ID>-<slug>.<json|md>`;
  `split_record_filename` inverts it and refuses anything else (including a sequential `INV-0143`).
- `history_path(owner)`, `census_directory(id)`, `file_sidecar_path(source)` (→
  `onboarding/<source>.json`) and `route_sidecar_path(route)` (`.` → `onboarding/overview.json`).
- **Attempt-qualified history paths (L37 reopen ruling).** `history_path(owner_id, attempt=None)` returns the
  plain `knowledge/history/<owner-id>.json` for no attempt or attempt 1, and `<owner-id>-attempt-<n>.json` for
  n >= 2. `owner_history_attempt(path, owner_id)` inverts it: 1 for the plain file, n for an attempt file, and
  `None` for any other path (including `-attempt-1` and another owner's file).

### Conventions

- Paths are POSIX strings relative to the memory repository root; `KNOWLEDGE_ROOT` and
  `ONBOARDING_ROOT` are the two top directories.

### Invariants And Boundaries

- The slug is display only; the ID is the identity.
- This module declares locations; it performs no filesystem access.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The format's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R21@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The models dispatched to come from `records.py` and `sidecars.py`.

- The layout table. [1]
- The schema table, including the history schema and the four census schemas. [2]
- The document union gains the census documents. [3]
- Schema dispatch, refusing unknown schemas. [4]
- A history file is read only at its owner's path, with its attempt for a reopened leaf. [5]
- Record paths and the filename split. [6]
- Sidecar paths, with `.` as the root route. [7]

- The history path of an owner and attempt. [8]
- Which attempt of an owner's history a path names. [9]
- Attempt files are named, ordered and backward compatible. [10]

### Cross-Repo References

No meaningful cross-repo references found: the module reads and writes only files of the memory
repository layout it declares, and calls no sibling repository or external service.

No cross-repo boundary is crossed by this file.
