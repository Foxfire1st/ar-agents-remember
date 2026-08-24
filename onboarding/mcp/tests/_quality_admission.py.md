# mcp/tests/_quality_admission.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/_quality_admission.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T20:55+02:00 |
| lastVerifiedCommitHash | `77bc614506b8b50937aed6846523547d36045947` |
| lastVerifiedCommitDate | 2026-08-24T20:41:34+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Exposes the already-validated certifying admission capability from root conftest to Dagger-suite
tests that exercise quality planning APIs directly.

## Code Commentary

`QUALITY_TEST_ADMISSION` aliases `CERTIFYING_BOOTSTRAP.admission`; it does not fabricate a token or
re-run admission. Imports therefore fail before collection outside the certifying route.

## Invariants And Boundaries

- This helper is Dagger-suite-only and cannot authorize host diagnostics.
- Tests pass the real capability into APIs whose type contract requires it.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The helper only aliases the conftest composition. | `QUALITY_TEST_ADMISSION` | mcp/tests/_quality_admission.py:5-5 |

## Update History

- 2026-08-24T20:55+02:00 — Created for 260824-PDLS.
