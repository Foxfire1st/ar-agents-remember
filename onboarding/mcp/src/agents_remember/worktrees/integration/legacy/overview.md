# Legacy Lifecycle Bridge Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration/legacy` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-05T07:08+00:00 |
| lastVerifiedCommitHash | `ea35964985f30080488270e71ac81657ac40682b` |
| lastVerifiedCommitDate | 2026-09-05T06:48:29+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Integration overview](../overview.md)

## What This Area Is

The bounded schema-1 lifecycle migration and archive bridge. It exists only for proven persisted
legacy records and publishes current journal/archive evidence through explicit typed transitions.

## Hot Path Summary

`legacy_operation_bridge.py` inspects and migrates; `legacy_operation_archive.py` validates and
publishes crash-safe terminal archives and receipts.

Migrated closeout records now derive canonical task intent from the exact contract-owned
leaf. Failure to resolve that intent becomes the same typed `LegacyBridgeError` family;
the bridge does not manufacture an intent from historic prose. The authority, failure,
public-result, and schema modules remain explicit siblings of the two main entry owners.

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

- 2026-09-05T07:08+00:00 — L31 cumulative source review at `ea35964985f30080488270e71ac81657ac40682b`: Documented canonical task intent on schema-1 closeout migration and explicit sibling ownership. Verification records current source claims, not execution or acceptance.

- 2026-08-25T15:44+02:00 — Created for the isolated schema-1 migration/archive boundary.
  Verification remains closeout-owned.
