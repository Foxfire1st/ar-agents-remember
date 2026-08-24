# mcp/tests/test_python_direct_cohort.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_python_direct_cohort.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T20:55+02:00 |
| lastVerifiedCommitHash | `77bc614506b8b50937aed6846523547d36045947` |
| lastVerifiedCommitDate | 2026-08-24T20:41:34+02:00 |
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
| The module contains exactly seven top-level tests. | `test_*` | mcp/tests/test_python_direct_cohort.py:24-54 |
| The checked-in manifest records selection and closure rationale. | `Python Direct Diagnostic Cohort Manifest` | docs/design/python-direct-cohort.md:1-101 |

## Update History

- 2026-08-24T20:55+02:00 — Created for 260824-PDLS; CodeRabbit's fixed-tuple typing delta is folded
  into the final candidate.
