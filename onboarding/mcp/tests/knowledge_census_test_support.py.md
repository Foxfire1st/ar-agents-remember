# mcp/tests/knowledge_census_test_support.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The census design authority is the coordination-root notes Doc12 (the
migration census and its measures) and Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`)
and the requirement packet `MIK-R20@v2` of task `260928_maintained-invariant-knowledge`; they live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The fixture builders.

- The six routes and their cards. [1]
- A claim document. [2]
- The converted tree with a pinned census. [3]
- 42 claims: 31 T, 4 F, 5 U, 2 P. [4]
- Every route migrated, with two status entries. [5]

### Cross-Repo References

No meaningful cross-repo references found: the fixture is in-memory bytes.

No cross-repo boundary is crossed by this file.
