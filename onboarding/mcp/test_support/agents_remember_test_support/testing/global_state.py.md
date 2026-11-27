# mcp/test_support/agents_remember_test_support/testing/global_state.py

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Owns the explicit registry of production module state that every supported pytest route snapshots
and restores. Lives in test support so production plugins do not import test helpers.

## Code Commentary

The grammar-parser (`canvas.kit_references._js_language`, `memory_quality.style.citations.grammars.language`, and `_process_typescript_anchor_identifier`) and lifecycle-cache reset entries name process-owned caches cleared between test modules via `_clear_cache` or `_clear`. Request scopes clear their own owner maps when they leave.

`PROCESS_MUTABLE_STATES` is a closed register of syntactically discovered product process state.
Each row names its owner, treatment and reason. The four treatments are `restored`, `reset`, `constant for tests` and `quiescent`. The knowledge-index `_builds` dictionary and `_active_temps` set use `quiescent`. The cache owns their cleanup. The in-process thread success and failure tests check both collections for the fixture directory after the threads finish.
The companion source guard rejects unregistered, stale and duplicate rows; this is a governed
syntactic population, not a claim to discover every possible mutable object.

`OWNED_MUTABLE_STATES` derives only the restored rows: the checkout execution declaration, worklist
item-kind registrations and knowledge-validator registrations. Loaded restored owners are snapshotted
per test and restored before reporting leaks. Import-time-only registries retain their rows, including
registrations from deferred imports. Reset rows are handled before and after each test module, only
when their owner is already in `sys.modules`; resetting never imports a product module.

The closed register includes `agents_remember.kernel.primitives.runtime_config._LEGACY_GATE_DELEGATION_WARNED` with the default `reset` treatment and `_clear` resetter between test modules rather than per-test restoration. It also retains ordinary `_clear` resets for closeout digest-file stats and lifecycle operation location/record caches. The removed session-log cache and ambient singleton are not reset owners. No scanner exemption or production reset applies; restored rows keep their per-test treatment.

The reset register also includes measured answer-folder budgets, suspended held-message sweep walks, message-stem counters, atomic-write temporary paths, the installed tool-event writer, `serving.background_accounting._BackgroundPool.executor` (drained under `_BACKGROUND_POOL_LOCK` and cleared by `_reset_background_pool`), `serving.projections.host_activity` `_ENDINGS` and `_ROLE_RECORDS`, and `application.role_capsules.wire_budget._wire_encoding` (`@lru_cache`, cleared via `_clear_cache` between test modules). Sweep walks and the writer delegate cleanup to their owning resetters rather than merely clearing a wrapper mapping.

Cleanup follows the resource owner: wait for quality workers under their lock before clearing runs;
terminate and reap this process's tracked children; clear caches,
services and lock bookkeeping; undo installed wrappers together with their installation guards.
`begin_pytest_process` keeps one typed session snapshot and declares test mode;
`end_pytest_process` restores that snapshot. `preserve_owned_mutable_state` contains an entry point
whose contract deliberately sets process state.

## Invariants And Boundaries

- Each discovered state has exactly one justified treatment; constants survive deferred registration.
- Module cleanup resets loaded owners without importing new production modules.
- Restoration happens before a leak becomes a failure so later tests cannot inherit it.
- Begin/end are safe across every pytest exit path and repeated end calls.
- The reset register also forgets master-architect host adapters, explainer in-flight send/build ledgers, and per-root move watches between modules. `worktrees.services._current` is absent from the register because the service supplier is one holder object reset explicitly before and after each module by the shared pytest module fixture.

## Evidence

### Repo-Internal References

- The one owned state register is explicit. [1]

- Module reset uses already-loaded owners only. [4]

- Worker completion precedes clearing the quality-run registry. [5]

- Only process-owned spawned children are terminated and reaped. [7]

- Process snapshot and restore use one typed state owner. [2]

- The closed register gives each registered process state one treatment and a reason. [3]

- Resetting loaded owners delegates sweep cleanup and tool-writer cleanup to their resetters. [8]
- The closed process registry gives _LEGACY_GATE_DELEGATION_WARNED the default _clear reset between test modules when its owner is already loaded. [9]
- The closeout digest-file stats, lifecycle location cache and process-owned lifecycle operation-record memo use ordinary _clear resets between test modules. [10]
- The reset register discards loaded master-architect host adapters, Explainer send and build ledgers, and per-root move watches between test modules. [11]
- The reset register clears `canvas.kit_references._js_language` with `_clear_cache` between test modules to forget loaded JavaScript grammar memoization. [13]
