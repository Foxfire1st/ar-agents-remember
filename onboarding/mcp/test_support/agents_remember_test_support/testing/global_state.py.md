# mcp/test_support/agents_remember_test_support/testing/global_state.py

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

## Evidence

### Repo-Internal References

- The one owned state register is explicit. [1]
- Process snapshot/restore uses one typed owner. [2]
