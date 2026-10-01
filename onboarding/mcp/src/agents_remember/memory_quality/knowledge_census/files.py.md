# mcp/src/agents_remember/memory_quality/knowledge_census/files.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The census design authority is the coordination-root notes Doc12 (the
migration census and its measures) and Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`)
and the requirement packet `MIK-R20@v2` of task `260928_maintained-invariant-knowledge`; they live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

Locations, the reader and its entry point.

- The census locations. [1]
- A path's census ID. [2]
- The parsed census and the tree of censuses. [3]
- Location, canonical, schema, census and route-slug checks while reading. [4]
- The entry point. [5]
- Every census file parses by schema and is canonical. [6]

### Cross-Repo References

No meaningful cross-repo references found: the package reads one memory tree's bytes, handed in by the caller.

No cross-repo boundary is crossed by this file.
