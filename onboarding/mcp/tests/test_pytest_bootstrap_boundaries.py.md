# mcp/tests/test_pytest_bootstrap_boundaries.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_pytest_bootstrap_boundaries.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T20:55+02:00 |
| lastVerifiedCommitHash | `77bc614506b8b50937aed6846523547d36045947` |
| lastVerifiedCommitDate | 2026-08-24T20:41:34+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Provides the compact pure four-state proof for valid certification, valid diagnostics,
invalid/missing certifying admission, and attempted diagnostic elevation.

## Code Commentary

The matrix proves a valid nonce/file handshake mints the private capability, diagnostic bootstrap
never consults admission, invalid certifying facts refuse before candidate resolution, and
diagnostic evidence cannot enter quality. Additional cases cover handshake failures, caller-shaped
capabilities, Git/temp/cache isolation, reversible environment application, shared-versus-
certifying plugin imports, and global-state restoration.

## Invariants And Boundaries

- These pure model tests do not claim Dagger acceptance.
- The final full graph remains responsible for exercising the real composition.
- Diagnostic validity and certifying invalidity are separate states, not fallback branches.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| One test covers all four authority states. | `test_four_state_authority_matrix` | mcp/tests/test_pytest_bootstrap_boundaries.py:71-107 |
| Handshake and caller-shaped failures are total. | `test_admission_matrix_is_total_and_does_not_expose_the_nonce` | mcp/tests/test_pytest_bootstrap_boundaries.py:109-127 |

## Update History

- 2026-08-24T20:55+02:00 — Created for 260824-PDLS.
