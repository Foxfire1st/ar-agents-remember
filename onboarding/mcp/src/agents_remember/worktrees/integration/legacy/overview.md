# Legacy Lifecycle Bridge Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration/legacy` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash |  `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e`|
| lastVerifiedCommitDate |  2026-08-25T17:21:45+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Integration overview](../overview.md)

## What This Area Is

The bounded schema-1 lifecycle migration and archive bridge. It exists only for proven persisted
legacy records and publishes current journal/archive evidence through explicit typed transitions.

## Hot Path Summary

`legacy_operation_bridge.py` inspects and migrates; `legacy_operation_archive.py` validates and
publishes crash-safe terminal archives and receipts.

## Local Invariants And Traps

- No generic compatibility reader or silent schema fallback is allowed.
- Existing current migrations must match exact legacy bytes and canonical identity.
- Archive publication and unlink recovery are idempotent and evidence-gated.

## File-Level Onboarding Map

| Source File | Onboarding | Status |
| --- | --- | --- |
| `legacy_operation_bridge.py` | [legacy_operation_bridge.py.md](legacy_operation_bridge.py.md) | covered |
| `legacy_operation_archive.py` | [legacy_operation_archive.py.md](legacy_operation_archive.py.md) | covered |

## Docs And Boundary References

No configured external source applies. Schema/current-operation owners are same-repository.

## Update History

- 2026-08-25T15:44+02:00 — Created for the isolated schema-1 migration/archive boundary.
  Verification remains closeout-owned.
