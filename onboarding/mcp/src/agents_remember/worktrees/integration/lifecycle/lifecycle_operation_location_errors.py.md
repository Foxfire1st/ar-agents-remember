# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_location_errors.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_location_errors.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb`|
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Worktree-integration overview](../overview.md)

## Purpose

Centralizes typed lifecycle-location failures and exact regular-file reads for locator, manifest,
contract, journal, archive, and receipt authority.

## Code Commentary

The reader distinguishes genuine absence from present-but-invalid state. An unreadable,
non-regular, or symlinked authority file is a conflict and is never silently treated as missing.

## Invariants And Boundaries

- Present-invalid authority fails closed.
- All location callers share one failure vocabulary instead of reimplementing lower-level catches.
- No scan, guessed path, compatibility reader, or raw-Git fallback is introduced.

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: created from the final typed location-error boundary. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.
