# mcp/tests/test_knowledge_census_files.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_census_files.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T09:30:11+02:00 |
| lastVerifiedCommitHash | `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695`|
| lastVerifiedCommitDate | 2026-09-29T09:57:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R20: census file formats, the mechanical inventory, the writer and the validator's census
rules.** Over the fixture census of `knowledge_census_test_support`, a test changes one thing and checks
that exactly the owning rule answers. Registered in the `unit-regression` lane; 28 collected cases.

## Code Commentary

### Logic

- **Formats.** Every census file parses by schema and is canonical; route slugs are readable and
  injective; the models refuse inconsistent claims and statuses.
- **Inventory.** Rows carry their governing route; `take_inventory` pins exact commits over real
  `tmp_path` Git repositories and refuses `no-such-branch` and an all-zero commit.
- **Writer.** Appends pass the validator; refusals (including an unconverted tree) write nothing; an
  interrupted `create` can be repeated; model refusals are `CensusWriteError`.
- **Rules.** The nine rules are registered and refusing; assessments and statuses are append-only (with
  a two-parent merge); the baseline and inventory are pinned; eight parametrised integrity cases
  (location, canonical, slug, census, row, duplicate, records, route); the slug-ends-like-a-pinned-file
  regression; five stable-field cases (`text`, `location`, `kind` and `applicability` under
  `R20.2-claim-stable`, a changed `id` as a removed claim), each also checking that setting the
  disposition passes; the rule cache keeps no tree.

### Conventions

- Helpers `_validate`, `_census_rules`, `_with_claims` and `_census_on` validate or build a writer over the fixture.

### Invariants And Boundaries

- Refusal cases assert the tree bytes are unchanged.

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

The case groups.

| Finding | Anchor | Source |
| --- | --- | --- |
| Formats and slugs. | `test_every_census_file_parses_by_schema_and_is_canonical`; `test_route_slugs_are_readable_and_injective` | mcp/tests/test_knowledge_census_files.py:91-106; mcp/tests/test_knowledge_census_files.py:109-115 |
| The writer appends and refuses. | `test_the_writer_appends_observations_and_its_tree_passes_the_validator`; `test_the_writer_refuses_and_writes_nothing` | mcp/tests/test_knowledge_census_files.py:237-269; mcp/tests/test_knowledge_census_files.py:272-300 |
| Pinned files. | `test_the_baseline_and_inventory_are_pinned` | mcp/tests/test_knowledge_census_files.py:367-375 |
| Integrity rules name file, field and rule. | `test_census_integrity_rules_name_file_field_and_rule` | mcp/tests/test_knowledge_census_files.py:378-449 |
| Stable claim fields. | `test_a_recorded_claims_identity_and_cohort_fields_are_stable` | mcp/tests/test_knowledge_census_files.py:502-532 |

## Cross-Repo References

No meaningful cross-repo references found: the cases build `tmp_path` repositories.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T09:30:11+02:00 — 260928-MIK-L20 curator (uncommitted change set on `ar/260928-mik-l20`, code base `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d` plus the staged delta): created this card for the new file MIK-R20 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
