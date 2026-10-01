# mcp/src/agents_remember/memory_quality/knowledge_validator/parsed.py

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**Reads every file of a knowledge tree once, through the MIK-R21 and MIK-R07 models, and sorts every problem to the rule that owns it.** `parse_tree` places each path by location (layout marker, `knowledge/history/`, `knowledge/census/`, a record directory, onboarding Markdown or onboarding JSON), checks canonical formatting, validates with the model its location and `schema` name, and returns a `ParsedTree` of records, sidecars, histories, Markdown texts and `ParseProblem`s.

## Code Commentary

### Logic

- Each `ParseProblem` carries a `category` so that exactly one rule reports it: `extra_forbidden` at the top level of a record is `single_owner` (rule 4); a `locator` location is `locator` and an anchor `content` is `content` (rule 6); a filename that does not begin with the record's ID is `identity` (rule 2); a non-canonical file is `canonical`; a kind-disallowed link relation is `relation` (rule 3); everything else is `shape` (rule 1).
- `json_document` decodes UTF-8, parses with `canonical.parse_json`, and compares `canonical_text(document)` with the text. A mismatch names `agents-remember knowledge-format <path>`.
- `record` maps the directory to a `RecordKind` and splits the filename with `split_record_filename`. A record's Markdown is kept as Markdown. A record whose JSON does not parse still counts as existing through the ID in its filename (`unparsed_record_ids`), so one broken record gives one shape violation, not one per link to it.
- `disallowed_relations` checks each raw link against `RELATIONS_BY_KIND` before the model runs, and records the field `links.<i>.relation`. `drop_unnamed_relation_error` then removes the model's own duplicate error, which names no field (review R1 finding 3).
- `history` requires `knowledge/history/<owner-id>.json` and parses with `parse_history_document` (shape only).
- `sidecar` requires a file or route sidecar at exactly `file_sidecar_path`/`route_sidecar_path` of its own `path`.
- `knowledge/census/` is skipped here (`CENSUS_DIRECTORY`): since MIK-R20 (leaf 260928-MIK-L20) census files are read by `rules_census` through `memory_quality/knowledge_census`, not by this parser, so the validator is not forked and census problems are owned by the `R20.*` rules.
- `parse_sidecars_leniently` reads only the sidecars of a *base* tree that parse, ignoring everything else; the registry uses it to find carried anchors.

### Conventions

- Parsing never raises for bad content: every failure becomes a problem, and the rules decide.
- It reuses the L21/L07 models and path helpers unchanged.

### Invariants And Boundaries

- Every knowledge file is read once, and each problem is owned by one rule.
- Unknown files under `knowledge/` are refused as "not a knowledge file location".
- History row IDs are not collected for uniqueness: history is shape-only.

### Todos

- When a record has both a disallowed relation and another model-level error, Pydantic stops at the first failing validator, so the second error appears only after the first is repaired (review R1 round 2 note).

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The validator's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R22@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The problem categories, the parser and its entry points.

- The problem categories and the rule each maps to. [1]
- The parsed result, including unparsed record IDs that still resolve. [2]
- Location dispatch, canonical check, relation attribution and sidecar placement. [3]
- The tree entry point and the lenient base reader. [4]
- A disallowed relation is refused under the relations rule with its field. [5]
- A non-canonical file names the formatter command. [6]

### Cross-Repo References

No meaningful cross-repo references found: the validator reads one memory tree and one paired code tree, both addressed explicitly by the caller.

No cross-repo boundary is crossed by this file.
