# mcp/src/agents_remember/testing/certifying_bootstrap.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/certifying_bootstrap.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T20:55+02:00 |
| lastVerifiedCommitHash | `77bc614506b8b50937aed6846523547d36045947` |
| lastVerifiedCommitDate | 2026-08-24T20:41:34+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Explicitly composes Dagger admission with the shared hermetic candidate process for certifying
pytest startup.

## Code Commentary

`prepare_certifying_pytest_bootstrap` requires admission first, then resolves the candidate
process, returning a typed pair. Root conftest receives this composition before it loads shared or
certifying-only plugins.

## Invariants And Boundaries

- Admission precedes candidate planning and collection.
- The diagnostic route cannot construct this result because it receives no admission capability.
- This module composes responsibilities; it does not reimplement either validator or bootstrap.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Certifying composition orders admission before candidate process creation. | `prepare_certifying_pytest_bootstrap` | mcp/src/agents_remember/testing/certifying_bootstrap.py:27-39 |

## Update History

- 2026-08-24T20:55+02:00 — Created for 260824-PDLS.
