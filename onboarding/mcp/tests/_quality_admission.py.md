# mcp/tests/_quality_admission.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/_quality_admission.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:51:23+00:00 |
| lastVerifiedCommitHash | `b99501852bcfa5f499a25e7183063751f6133a28` |
| lastVerifiedCommitDate | 2026-08-24T21:21:58+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Provides modeled admission input for quality-plan tests using injected runners.

## Code Commentary

The helper creates a temporary nonce file and calls `require_dagger_admission` with an explicit local environment mapping and attestation path. `QUALITY_TEST_ADMISSION` is a modeled input to these tests. It does not import a global certifying bootstrap, modify the process environment, or change the real Dagger attestation path.

## Invariants And Boundaries

Real delivery obtains its capability through the executor handshake. This fixture does not declare a daemon identity or certify host test execution. Its temporary file is cleaned after constructing the input.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Explicit modeled input with no process-environment mutation. | `QUALITY_TEST_ADMISSION` | mcp/tests/_quality_admission.py:1-21 |

## Update History

- 2026-09-06T21:51:23+00:00 — Reconciled the landed IAS source delta and actual preparation/fixture boundaries; existing verification pins and history are preserved.

- 2026-08-24T21:23+02:00 — Created for 260824-PDLS.
