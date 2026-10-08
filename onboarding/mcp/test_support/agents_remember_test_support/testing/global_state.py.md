# mcp/test_support/agents_remember_test_support/testing/global_state.py

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Owns the explicit registry of production module state that every supported pytest route snapshots
and restores. This behavior moved from the test tree so production plugins no longer import test
helpers.

## Code Commentary

`PROCESS_MUTABLE_STATES` is a closed register of syntactically discovered product process state.
Each row names its owner, one treatment and the reason: `restored`, `reset`, or `constant for tests`.
The companion source guard rejects unregistered, stale and duplicate rows; this is a governed
syntactic population, not a claim to discover every possible mutable object.

`OWNED_MUTABLE_STATES` derives only the restored rows: the checkout execution declaration, worklist
item-kind registrations and knowledge-validator registrations. Loaded restored owners are snapshotted
per test and restored before reporting leaks. Import-time-only registries retain their rows, including
registrations from deferred imports. Reset rows are handled before and after each test module, only
when their owner is already in `sys.modules`; resetting never imports a product module.

Cleanup follows the resource owner: wait for quality workers under their lock before clearing runs;
stop and join the ambient heartbeat; terminate and reap this process's tracked children; clear caches,
services and lock bookkeeping; undo installed wrappers together with their installation guards.
`begin_pytest_process` keeps one typed session snapshot and declares test mode;
`end_pytest_process` restores that snapshot. `preserve_owned_mutable_state` contains an entry point
whose contract deliberately sets process state.

## Invariants And Boundaries

- Each discovered state has exactly one justified treatment; constants survive deferred registration.
- Module cleanup resets loaded owners without importing new production modules.
- Restoration happens before a leak becomes a failure so later tests cannot inherit it.
- Begin/end are safe across every pytest exit path and repeated end calls.

## Evidence

### Repo-Internal References

- The one owned state register is explicit. [1]
- Process snapshot/restore uses one typed owner. [2]


- The closed register gives every state a treatment and causal rationale. [3]
- Module reset uses already-loaded owners only. [4]
- Worker completion precedes clearing the quality-run registry. [5]
- Ambient reset joins the actual heartbeat before returning. [6]
- Only process-owned spawned children are terminated and reaped. [7]
