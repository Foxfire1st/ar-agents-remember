# mcp/test_support/agents_remember_test_support/testing/global_state.py

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

### STOP-delta current source contract

The closed product-process register now includes agents_remember.kernel.primitives.runtime_config._LEGACY_GATE_DELEGATION_WARNED with the default reset treatment and existing _clear resetter between test modules. It is not a per-test-restored lock. The shared guard and treatment rules remain unchanged; registration is not execution of the reset control.

These are current source/assertion-carrier meanings. The qualified attempt14 CODE verdict is inherited, not a Curator test run, native freeze-currentness certification or independent MEMORY acceptance. Earlier contrary accounts are historical only; unaffected contracts and typed provenance remain.

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

The closed register also gives the existing closeout digest-file stats, lifecycle location cache and lifecycle operation-record cache ordinary `_clear` resets at module boundaries. It adds no scanner exemption or production reset; restored rows retain their per-test treatment.

The reset register also includes measured answer-folder budgets, suspended held-message sweep walks, message-stem counters, atomic-write temporary paths and the installed tool-event writer. Sweep walks and the writer delegate cleanup to their owning resetters rather than merely clearing a wrapper mapping.

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
- Loaded-owner reset includes delegated sweep and tool-writer cleanup. [8]

- The closed product-process register now includes agents_remember.kernel.primitives.runtime_config._LEGACY_GATE_DELEGATION_WARNED with the default reset treatment and existing _clear resetter between test modules. It is not a per-test-restored lock. The shared guard and treatment rules remain unchanged; registration is not execution of the reset control. [9]

- The closed register also gives the existing closeout digest-file stats, lifecycle location cache and lifecycle operation-record cache ordinary `_clear` resets at module boundaries. It adds no scanner exemption or production reset; restored rows retain their per-test treatment. [10]
