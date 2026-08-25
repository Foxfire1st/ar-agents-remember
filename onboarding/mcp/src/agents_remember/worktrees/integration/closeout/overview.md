# Closeout Integration Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration/closeout` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash |  `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e`|
| lastVerifiedCommitDate |  2026-08-25T17:21:45+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Integration overview](../overview.md)

## What This Area Is

Closeout-door publication, source reconstruction, ledger recovery, organizational repair, and
recovery projection. It separates door/scheduling evidence from the durable operation journal.

## Hot Path Summary

`door_source.py` reconstructs the exact waiting source; `ledger_recovery.py` advances code and
memory proof after partial closeout without making the disposable queue own commit evidence.

## Local Invariants And Traps

- Door publication authorizes entry; the operation journal owns running and terminal evidence.
- Recovery is idempotent and candidate-bound; missing or conflicting proof refuses loudly.
- Queue invalidation never erases an already-claimed lifecycle operation.

## File-Level Onboarding Map

| Source File | Onboarding | Status |
| --- | --- | --- |
| `door_source.py` | [door_source.py.md](door_source.py.md) | covered |
| `ledger_recovery.py` | [ledger_recovery.py.md](ledger_recovery.py.md) | covered |

## Docs And Boundary References

No configured external source applies. The lifecycle and queue overviews describe adjacent owners.

## Update History

- 2026-08-25T15:44+02:00 — Created for the recoverable closeout-door/journal boundary.
  Verification remains closeout-owned.
