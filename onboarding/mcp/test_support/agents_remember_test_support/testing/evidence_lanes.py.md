# mcp/test_support/agents_remember_test_support/testing/evidence_lanes.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/testing/evidence_lanes.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Defines the complete executable category and cadence registry applied during certifying pytest
collection.

## Code Commentary

### Logic

`EVIDENCE_LANES` gives every evidence category one marker, authority, minimum fidelity, expected
lifetime, and trigger set. `expression_for` maps affected, provider-bump, scheduled, migration, and
release triggers to explicit pytest populations. During collection, `category_for_item` first
requires the test file to have exactly one entry in the exhaustive lane manifest and then verifies
that any marker agrees with that declaration. The resolved category is attached to every report
item.

### Conventions

There is no unmarked-unit convention. Every test file must declare one category in
`mcp/tests/test-evidence-lanes.toml`; an exact-node override is permitted only where that narrower
identity is intentional. Missing, stale, unknown, duplicate, or marker-conflicting declarations
are collection errors.

### Invariants And Boundaries

- Categories and markers are unique, and the lane manifest exhausts the current test-file
  population; omissions and conflicts refuse collection.
- Affected execution excludes sustained stress, while release has no marker filter.
- Diagnostic evidence uses exact-node selection and cannot be selected by this plugin.
- Category assignment does not itself grant acceptance authority.

### Todos

None.

## Docs References

No external documentation owns the repository cadence taxonomy.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The eight lanes define authority, fidelity, lifetime, and triggers. | `EVIDENCE_LANES` | mcp/test_support/agents_remember_test_support/testing/evidence_lanes.py:19-116 |
| Registry validation and collection routing are fail-closed. | `validate_lane_registry`; `category_for_item` | mcp/test_support/agents_remember_test_support/testing/evidence_lanes.py:132-225 |
| The manifest loader proves complete, non-conflicting test-file coverage before collection. | `load_lane_manifest` | mcp/test_support/agents_remember_test_support/testing/lane_manifest.py:58-127 |

## Cross-Repo References

No adjacent repository controls lane membership.

## Update History

- 2026-08-28T04:37+02:00 — Corrected the canonical lane-manifest path to
  `mcp/tests/test-evidence-lanes.toml`.
- 2026-08-27T11:14+02:00 — Removed the implicit unmarked-unit convention. Collection now requires
  exhaustive explicit lane declarations and refuses missing or conflicting identity.
- 2026-08-25T01:56+02:00 — Created for executable evidence categories and cadence separation.
