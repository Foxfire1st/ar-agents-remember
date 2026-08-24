# mcp/src/agents_remember/testing/diagnostic_bootstrap.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/diagnostic_bootstrap.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T21:23+02:00 |
| lastVerifiedCommitHash | `b99501852bcfa5f499a25e7183063751f6133a28` |
| lastVerifiedCommitDate | 2026-08-24T21:21:58+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Composes a still-current eligible decision with the shared hermetic process without importing or
consulting Dagger admission.

## Code Commentary

`prepare_diagnostic_pytest_bootstrap` verifies candidate currency before creating the process.
`diagnostic_pytest_environment` creates the isolated child environment and explicitly removes the
Dagger attestation variable even if the parent supplied it.

## Invariants And Boundaries

- The bootstrap type has no admission or certifying field.
- Candidate drift refuses before execution.
- An admission failure is never a signal to call this module.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Diagnostic composition requires a current eligible selection. | `prepare_diagnostic_pytest_bootstrap` | mcp/src/agents_remember/testing/diagnostic_bootstrap.py:33-47 |
| Dagger attestation is scrubbed from the diagnostic child. | `diagnostic_pytest_environment` | mcp/src/agents_remember/testing/diagnostic_bootstrap.py:50-64 |

## Update History

- 2026-08-24T21:23+02:00 — Created for 260824-PDLS.
