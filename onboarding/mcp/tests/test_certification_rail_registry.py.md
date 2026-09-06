# mcp/tests/test_certification_rail_registry.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_certification_rail_registry.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash | `0506b57a1a80e0b377e9cc3303e1841d3bd4799a`|
| lastVerifiedCommitDate | 2026-09-01T12:17:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Portable rail registry and typed result-manifest contracts.

## Code Commentary

### Logic

A generic repository compiles deterministic immutable plans for five gates. Identical rails deduplicate while conflicts and independent graph/classification findings survive. Result manifests preserve independent failures and successes, block only dependants, and enforce declared bounded evidence and artifacts.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Diagnostic altitude cannot be promoted to certifying authority; a report-only pass cannot erase an enforcing failure. The suite is repository-neutral and does not prove live profile execution.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Non agents remember registry compiles one deterministic plan per gate. | `test_non_agents_remember_registry_compiles_one_deterministic_plan_per_gate` | mcp/tests/test_certification_rail_registry.py:34-60 |
| Canonicalization deduplicates identical rails but rejects conflicts. | `test_canonicalization_deduplicates_identical_rails_but_rejects_conflicts` | mcp/tests/test_certification_rail_registry.py:63-73 |
| Registry validation reports independent graph and classification failures. | `test_registry_validation_reports_independent_graph_and_classification_failures` | mcp/tests/test_certification_rail_registry.py:76-101 |
| Gate manifest keeps failed and independent siblings and blocks only dependant. | `test_gate_manifest_keeps_failed_and_independent_siblings_and_blocks_only_dependant` | mcp/tests/test_certification_rail_registry.py:104-125 |
| Passing suite requires declared artifacts and bounded evidence. | `test_passing_suite_requires_declared_artifacts_and_bounded_evidence` | mcp/tests/test_certification_rail_registry.py:128-148 |
| Diagnostic result cannot be promoted to certifying altitude. | `test_diagnostic_result_cannot_be_promoted_to_certifying_altitude` | mcp/tests/test_certification_rail_registry.py:151-187 |
| Result refuses evidence and artifacts outside the plan contract. | `test_result_refuses_evidence_and_artifacts_outside_the_plan_contract` | mcp/tests/test_certification_rail_registry.py:190-228 |
| Two independent failures remain visible with only the dependant blocked. | `test_two_independent_failures_remain_visible_with_only_the_dependant_blocked` | mcp/tests/test_certification_rail_registry.py:231-253 |
| Report only result cannot turn an enforcing failure green. | `test_report_only_result_cannot_turn_an_enforcing_failure_green` | mcp/tests/test_certification_rail_registry.py:256-280 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-09-01T03:11+02:00 — Created for generic registry, plan, and terminal-result contract
  evidence. Verification remains closeout-owned until the source candidate is committed.
