# mcp/tests/test_knowledge_census_files.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R20: census file formats, the mechanical inventory, the writer and the validator's census
rules.** Over the fixture census of `knowledge_census_test_support`, each case changes a selected fixture property and checks the expected rule/message. The eight parametrized integrity cases assert rule and message inclusion, not singleton equality; other groups retain their specific equality assertions. Registered in the `unit-regression` lane; the earlier 28-case collection is historical, not freshly recertified here. Current descriptions below are static assertions.

## Code Commentary

### Logic

- **Formats.** Every census file parses by schema and is canonical; route slugs are readable and
  injective; the models refuse inconsistent claims and statuses.
- **Inventory.** Rows carry their governing route; `take_inventory` pins exact commits over real
  `tmp_path` Git repositories and refuses `no-such-branch` and an all-zero commit.
- **Writer.** The writer-positive cases assert successful appends; this does not imply every completed-migration fixture passes the validator; refusals (including an unconverted tree) write nothing; an
  interrupted `create` can be repeated; model refusals are `CensusWriteError`.
- **Rules.** The nine census rules are registered and refusing. Wave-one marks every route migrated,
  so the current based fixture retains refusing `LEGACY_COUNT` debt. Assessments/statuses are
  append-only (with a two-parent merge); corrections and merged excluded statuses leave only that
  debt, while assessment/status rewrites and pinned-inventory edits include it beside the R20 rule.
  Deleting a status file or keeping a blocked route leaves migration incomplete: carried debt reports
  rather than being treated as completed. The baseline and inventory are pinned; eight parametrised integrity cases
  (location, canonical, slug, census, row, duplicate, records, route); the slug-ends-like-a-pinned-file
  regression; five stable-field cases (`text`, `location`, `kind` and `applicability` under
  `R20.2-claim-stable`, a changed `id` as a removed claim), each also checking that setting the
  disposition removes the R20 refusal but leaves `LEGACY_COUNT` refusing in the migration-complete
  fixture; the rule cache keeps no tree even after that refusing report.

### Conventions

- Helpers `_validate`, `_census_rules`, `_with_claims` and `_census_on` validate or build a writer over the fixture.

### Invariants And Boundaries

- Refusal cases assert the tree bytes are unchanged.

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

The case groups.

- Formats and slugs. [1]
- The writer appends and refuses. [2]
- Integrity rules name file, field and rule. [4]

### Cross-Repo References

No meaningful cross-repo references found: the cases build `tmp_path` repositories.

No cross-repo boundary is crossed by this file.

- Pinned files and append-only statuses: complete migration leaves legacy-debt refusals; deleted/blocked status branches keep debt reportable. [3]
- Stable claim fields: settlement removes the R20 finding but leaves LEGACY_COUNT refusing; cache release is asserted after a refusing report. [5]
- Current source delta inspected statically: Distinguish census-local settlement/writer success from migration-complete debt refusal; cache is checked after refusal. [6]
