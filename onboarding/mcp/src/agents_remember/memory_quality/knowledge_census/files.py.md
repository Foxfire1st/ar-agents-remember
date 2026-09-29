# mcp/src/agents_remember/memory_quality/knowledge_census/files.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_census/files.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T09:30:11+02:00 |
| lastVerifiedCommitHash | `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695`|
| lastVerifiedCommitDate | 2026-09-29T09:57:49+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**Where census files live and how a memory tree's censuses are read (MIK-R20 rule 1).**
`read_censuses(files)` reads every file under `knowledge/census/` of one memory tree (path to exact bytes,
as the validator's `KnowledgeTree` holds them) into a `CensusTree` of `ParsedCensus` directories and
`CensusProblem`s. The path helpers `baseline_path`, `inventory_path`, `claims_path` and
`route_status_path` are the one spelling of each census location.

## Code Commentary

### Logic

- `census_id_of(path)` returns the census ID of a path under `knowledge/census/<id>/…`, or `None`.
- `_Reader.read` refuses a path outside a census directory or with an invalid census ID; `_expected_model`
  maps the location to its model (`baseline.json`, `inventory.json`, `claims/<slug>.json`,
  `routes/<slug>.json`) and anything else is "not a census file location".
- `_Reader.document` decodes strict UTF-8 JSON, compares with `canonical_text` (a mismatch is a
  `canonical` problem naming the formatter command) and dispatches through `parse_document`.
- `_Reader.place` refuses a file naming another census, and a claims or status file whose `route`
  does not match its filename slug.
- `require_pinned_files` reports a census without both `baseline.json` and `inventory.json`.

### Conventions

- Every failure is a problem, never an exception: the checks decide which rule reports it (`shape` → `R20.1-census-shape`, `canonical` → `R20.1-census-canonical`).

### Invariants And Boundaries

- A file that did not parse is absent from its `ParsedCensus`, so one bad file gives one problem, not a cascade.
- `parsed.py` still skips `knowledge/census/`; this module is the only reader of census files.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The census design authority is the coordination-root notes Doc12 (the
migration census and its measures) and Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`)
and the requirement packet `MIK-R20@v2` of task `260928_maintained-invariant-knowledge`; they live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

Locations, the reader and its entry point.

| Finding | Anchor | Source |
| --- | --- | --- |
| The census locations. | `baseline_path`; `route_status_path` | mcp/src/agents_remember/memory_quality/knowledge_census/files.py:49-50; mcp/src/agents_remember/memory_quality/knowledge_census/files.py:61-62 |
| A path's census ID. | `census_id_of` | mcp/src/agents_remember/memory_quality/knowledge_census/files.py:65-71 |
| The parsed census and the tree of censuses. | `ParsedCensus`; `CensusTree` | mcp/src/agents_remember/memory_quality/knowledge_census/files.py:82-91; mcp/src/agents_remember/memory_quality/knowledge_census/files.py:94-103 |
| Location, canonical, schema, census and route-slug checks while reading. | `_Reader` | mcp/src/agents_remember/memory_quality/knowledge_census/files.py:120-218 |
| The entry point. | `read_censuses` | mcp/src/agents_remember/memory_quality/knowledge_census/files.py:221-229 |
| Every census file parses by schema and is canonical. | `test_every_census_file_parses_by_schema_and_is_canonical` | mcp/tests/test_knowledge_census_files.py:91-106 |

## Cross-Repo References

No meaningful cross-repo references found: the package reads one memory tree's bytes, handed in by the caller.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T09:30:11+02:00 — 260928-MIK-L20 curator (uncommitted change set on `ar/260928-mik-l20`, code base `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d` plus the staged delta): created this card for the new file MIK-R20 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
