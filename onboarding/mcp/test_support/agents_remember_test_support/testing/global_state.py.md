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

The closed register retains ordinary `_clear` resets for closeout digest-file stats and lifecycle operation location/record caches. The removed session-log cache and ambient singleton are not reset owners. No scanner exemption or production reset is added; restored rows retain their per-test treatment.

The reset register also includes measured answer-folder budgets, suspended held-message sweep walks, message-stem counters, atomic-write temporary paths and the installed tool-event writer. Sweep walks and the writer delegate cleanup to their owning resetters rather than merely clearing a wrapper mapping.

Cleanup follows the resource owner: wait for quality workers under their lock before clearing runs;
terminate and reap this process's tracked children; clear caches,
services and lock bookkeeping; undo installed wrappers together with their installation guards.
`begin_pytest_process` keeps one typed session snapshot and declares test mode;
`end_pytest_process` restores that snapshot. `preserve_owned_mutable_state` contains an entry point
whose contract deliberately sets process state.


**L184 — INV-VDWN33.** Shared state that survives between cases is how a suite becomes order-dependent. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Invariants And Boundaries

- Each discovered state has exactly one justified treatment; constants survive deferred registration.
- Module cleanup resets loaded owners without importing new production modules.
- Restoration happens before a leak becomes a failure so later tests cannot inherit it.
- Begin/end are safe across every pytest exit path and repeated end calls.


The reset register also forgets master-architect host adapters, explainer in-flight send/build ledgers, and per-root move watches between modules. The obsolete `worktrees.services._current` row and its resetter are removed because the service supplier is now one holder object; the shared pytest module fixture resets that holder explicitly before and after each module. These declarations do not claim a reset was executed in this inspection.

## Evidence

### Repo-Internal References

- The one owned state register is explicit. [1]


- Process snapshot/restore uses one typed owner. [2]



- The closed register gives every state a treatment and causal rationale. 


- Module reset uses already-loaded owners only. [4]

- Worker completion precedes clearing the quality-run registry. [5]

- Only process-owned spawned children are terminated and reaped. [7]


- Loaded-owner reset includes delegated sweep and tool-writer cleanup. [8]




- The closed product-process register now includes agents_remember.kernel.primitives.runtime_config._LEGACY_GATE_DELEGATION_WARNED with the default reset treatment and existing _clear resetter between test modules. It is not a per-test-restored lock. The shared guard and treatment rules remain unchanged; registration is not execution of the reset control. 




- The closed register also gives the existing closeout digest-file stats, lifecycle location cache and lifecycle operation-record cache ordinary `_clear` resets at module boundaries. It adds no scanner exemption or production reset; restored rows retain their per-test treatment. 



## 260928-MIK-L177 A9 — The Background Pool Is Process State Too

`PROCESS_MUTABLE_STATES` gains a `serving.background_accounting` row for `_BackgroundPool.executor`
with its own resetter, `_reset_background_pool`: it takes `_BACKGROUND_POOL_LOCK`, drains the executor
and clears the slot, so the next test module builds a fresh pool. A further row forgets
`serving.projections.host_activity._ENDINGS`. Both are entries in the declaration this module already
keeps — process state a test module must not inherit — not a claim about production behaviour.

- The reset register also forgets master-architect host adapters, explainer in-flight send/build ledgers, and per-root move watches between modules. The obsolete `worktrees.services._current` row and its resetter are removed because the service supplier is now one holder object; the shared pytest module fixture resets that holder explicitly before and after each module. These declarations do not claim a reset was executed in this inspection. [11]


Anchor: `PROCESS_MUTABLE_STATES` [10]


Anchor: `PROCESS_MUTABLE_STATES` [3]


Anchor: `PROCESS_MUTABLE_STATES` [9]

- Retired at the fifth freeze d59c3493: mcp/test_support/agents_remember_test_support/testing/global_state.py::PROCESS_MUTABLE_STATES - the bytes it recorded now occur 3 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.
