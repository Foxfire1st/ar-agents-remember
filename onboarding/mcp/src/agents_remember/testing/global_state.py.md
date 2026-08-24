# mcp/src/agents_remember/testing/global_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/global_state.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T20:55+02:00 |
| lastVerifiedCommitHash | `77bc614506b8b50937aed6846523547d36045947` |
| lastVerifiedCommitDate | 2026-08-24T20:41:34+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Owns the explicit registry of production module state that every supported pytest route snapshots
and restores. This behavior moved from the test tree so production plugins no longer import test
helpers.

## Code Commentary

`OWNED_MUTABLE_STATES` currently registers the kernel checkout-execution declaration.
`begin_pytest_process` snapshots it once and declares test mode; `end_pytest_process` restores it.
One typed `_PytestProcessState` owns the session snapshot without module-global rebinding or lint
suppression. `preserve_owned_mutable_state` contains production calls that intentionally declare a
process role.

## Invariants And Boundaries

- The registry is explicit; this module does not pretend to discover arbitrary globals.
- Restoration happens before a leak becomes a failure so later tests cannot inherit it.
- Begin/end are safe across every pytest exit path and repeated end calls.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one owned state register is explicit. | `OWNED_MUTABLE_STATES` | mcp/src/agents_remember/testing/global_state.py:34-42 |
| Process snapshot/restore uses one typed owner. | `_PytestProcessState`; `begin_pytest_process`; `end_pytest_process` | mcp/src/agents_remember/testing/global_state.py:20-22; mcp/src/agents_remember/testing/global_state.py:61-75 |

## Update History

- 2026-08-24T20:55+02:00 — Moved from `mcp/tests/_global_state.py`; preserved the explicit
  checkout-mode ownership and added shared-route lifecycle plus typed session state.
- 2026-08-10T18:31+02:00 — The predecessor card recorded kernel checkout execution as the owned
  state and explicit pytest mode as the normal baseline.
