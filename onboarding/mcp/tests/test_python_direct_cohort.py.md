# mcp/tests/test_python_direct_cohort.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_python_direct_cohort.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T21:23+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Holds the closed seven-node real-production cohort adopted for canonical Python diagnostics.

## Code Commentary

The assertions were moved from integration-heavy modules without changing production behavior:
provider ID normalization, known/unknown gate and decision-role coercion, and route normalization.
One local fixture/helper chain exercises safe dependency closure. The fixed two-item helper return
keeps the cohort's exact tuple shape visible to static typing.

## Invariants And Boundaries

- These are existing production assertions, not synthetic classifier fixtures.
- The cohort is exactly seven selectors; expansion requires a separate decision and manifest edit.
- Direct passes are diagnostic; the same assertions must appear in Dagger acceptance evidence.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module contains exactly seven top-level tests. | `test_stable_provider_id_never_returns_empty`; `test_known_gate_kind_passes_through`; `test_unknown_gate_kind_is_refused`; `test_known_decision_role_passes_through`; `test_unknown_decision_role_is_refused_by_name`; `test_normalize_route_root_forms`; `test_normalize_route_strips_slashes_and_backticks` | mcp/tests/test_python_direct_cohort.py:24-27; mcp/tests/test_python_direct_cohort.py:30-31; mcp/tests/test_python_direct_cohort.py:34-36; mcp/tests/test_python_direct_cohort.py:39-40; mcp/tests/test_python_direct_cohort.py:43-45; mcp/tests/test_python_direct_cohort.py:48-50; mcp/tests/test_python_direct_cohort.py:53-54 |
| The checked-in manifest records selection and closure rationale. | `# Python Direct Diagnostic Cohort Manifest` | docs/design/python-direct-cohort.md:1-99 |

## Update History

- 2026-08-24T21:23+02:00 — Created for 260824-PDLS; CodeRabbit's fixed-tuple typing delta is folded
  into the final candidate.