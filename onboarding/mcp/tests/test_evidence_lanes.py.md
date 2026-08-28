# mcp/tests/test_evidence_lanes.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_evidence_lanes.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Forces every pytest node into one explicit evidence category, validates the executable lane
registry, and rejects missing, duplicate, conflicting, or silently inferred classifications.

## Code Commentary

### Logic

The suite verifies exhaustive one-to-one category registration and the non-accepting diagnostic
contract, checks trigger-to-marker expressions, loads the checked-in lane manifest to classify
representative unit/integration/provider nodes, and forces loud refusal for conflicting markers,
ad-hoc checked-in markers, or an unknown file. Plugin hooks must register all markers and attach
the category plus lane digest to every collected item.

### Conventions

Synthetic items expose only the pytest surface used by the plugin. Representative node paths come
from the real repository manifest so a drift between registry and checked-in classification fails
this test.

### Invariants And Boundaries

- No unmarked test silently defaults to unit or any other lane.
- Each evidence category and marker is unique.
- Stress stays out of affected runs; diagnostic execution requires its explicit route.
- Provider conformance is classified from the checked-in manifest, not guessed from a runtime
  opt-in marker.

### Todos

None.

## Docs References

No Domain Documentation source is configured; lane semantics are repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation is required for the explicit lane registry. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The registry is exhaustive and diagnostic evidence is explicitly non-accepting. | `test_every_category_has_one_lane_and_diagnostic_evidence_is_non_accepting`; `test_incomplete_or_ambiguous_registry_is_refused` | mcp/tests/test_evidence_lanes.py:61-84 |
| Trigger expressions keep stress, provider, migration, release, and diagnostic ownership distinct. | `test_cadence_expressions_keep_stress_out_of_affected_runs` | mcp/tests/test_evidence_lanes.py:86-93 |
| Real manifest classification is exact and unknown or conflicting classifications fail loudly. | `test_item_category_is_exact_and_provider_gates_are_provider_evidence` | mcp/tests/test_evidence_lanes.py:95-143 |
| Plugin hooks register the lane markers and publish category/digest properties. | `test_plugin_registers_the_registry_and_reports_category_on_each_item` | mcp/tests/test_evidence_lanes.py:145-162 |

## Cross-Repo References

No meaningful cross-repository boundary applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| Classification is wholly repository-local. | — | — |

## Update History

- 2026-08-28T06:28+02:00 — PDLS wave 005 curator: created the missing sidecar for exhaustive,
  explicit, fail-loud evidence-lane classification.
