# mcp/tests/knowledge_census_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/knowledge_census_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T09:30:11+02:00 |
| lastVerifiedCommitHash | `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695`|
| lastVerifiedCommitDate | 2026-09-29T09:57:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The fixture census for the MIK-R20 tests.** `census_tree_files()` extends the validator's converted
fixture tree (`knowledge_validator_test_support.fixture_tree_files`) with a root route and four more
onboarding routes (six in all) and one census, `wave-1`, whose inventory is built mechanically by
`build_inventory`. `wave_one_files()` adds the packet's conforming example: 42 claims (31 T, 4 F, 5 U,
2 P), seven per route, and every route `migrated` against one tree.

## Code Commentary

### Logic

- Constants: `CENSUS`, the fake commits, `ROUTES`, `EXTRA_SOURCES` (including one unrouted file) and
  `ROUTE_ARTIFACT` (the card each route's claims come from).
- Builders: `provenance`, `assessment`, `claim`, `claims_document`, `status_document` and `json_of`.
- `wave_one_claims` distributes the 42 verdicts round-robin over the six routes; `concern_found` claims
  are `discarded_false`, others `kept_as_prose`; kinds alternate.

### Conventions

- Imported by `test_knowledge_census_files.py` and `test_knowledge_census_report.py`; not itself a test module.

### Invariants And Boundaries

- The fixture census passes the validator unchanged; tests edit one file and expect exactly the owning rule.

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

The fixture builders.

| Finding | Anchor | Source |
| --- | --- | --- |
| The six routes and their cards. | `ROUTES`; `ROUTE_ARTIFACT` | mcp/tests/knowledge_census_test_support.py:29-47 |
| A claim document. | `claim` | mcp/tests/knowledge_census_test_support.py:62-75 |
| The converted tree with a pinned census. | `census_tree_files` | mcp/tests/knowledge_census_test_support.py:99-119 |
| 42 claims: 31 T, 4 F, 5 U, 2 P. | `wave_one_claims` | mcp/tests/knowledge_census_test_support.py:122-135 |
| Every route migrated, with two status entries. | `wave_one_files` | mcp/tests/knowledge_census_test_support.py:138-149 |

## Cross-Repo References

No meaningful cross-repo references found: the fixture is in-memory bytes.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T09:30:11+02:00 — 260928-MIK-L20 curator (uncommitted change set on `ar/260928-mik-l20`, code base `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d` plus the staged delta): created this card for the new file MIK-R20 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
