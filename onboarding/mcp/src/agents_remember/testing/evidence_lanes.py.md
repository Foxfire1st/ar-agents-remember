# mcp/src/agents_remember/testing/evidence_lanes.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/evidence_lanes.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
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
release triggers to non-overlapping pytest populations. Collection assigns provider-gated tests
from the lifecycle catalog and appends the resolved category to every report item.

### Conventions

Unmarked tests are ordinary unit regressions. Provider gates are provider conformance even when a
test author omitted the category marker.

### Invariants And Boundaries

- Categories and markers are unique and exhaustive; conflicts refuse collection.
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
| The eight lanes define authority, fidelity, lifetime, and triggers. | `EVIDENCE_LANES` | mcp/src/agents_remember/testing/evidence_lanes.py:19-116 |
| Registry validation and collection routing are fail-closed. | `validate_lane_registry` | mcp/src/agents_remember/testing/evidence_lanes.py:129-220 |
| Focused tests force categories, conflicts, provider gates, and cadence expressions. | `test_every_category_has_one_lane_and_diagnostic_evidence_is_non_accepting` | mcp/tests/test_evidence_lanes.py:59-125 |

## Cross-Repo References

No adjacent repository controls lane membership.

## Update History

- 2026-08-25T01:56+02:00 — Created for executable evidence categories and cadence separation.
