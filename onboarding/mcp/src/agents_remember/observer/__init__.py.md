# mcp/src/agents_remember/observer/__init__.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`__init__.py` is the observer package's public surface: it re-exports the
substrate write side, the slice-2b ambient lifecycle surface, the slice-3a
projection read side (schema + reducer + the shared store-root resolver), and the
slice-07 served-onboarding ledger surface.

## Code Commentary

The current facade re-exports event/store and ID-minting primitives, `AmbientLifecycle`, `install_ambient` and `reset_ambient`, lifecycle state vocabulary, projection/reducer types and functions, timing constants and `Clock`, and the served ledger/schema/key surface including `ServedLedger`. `observer_root` is imported from `kernel.primitives.observer_paths`. The `ambient()` getter and dependency-heavy snapshot/projection I/O readers remain direct submodule imports rather than package exports.

`require_ambient`, `GuardedStartError`, `AgentPickupNode`, `ExpectationRowNode` and `age_seconds` are not exported by this current facade. Their earlier slice descriptions below are historical, not a surviving signal/expectation surface. The current import/export inventory is source evidence, not execution of a reader or an independent CODE pass.

### Historical slice/export provenance

The prior slice account is retained at its authored source epoch. Superseded names and the older read-front-door description here establish no current capability:

Re-exports the write side — `Event`, `OBSERVER_EVENT_SCHEMA`, `Actor`, `Trust`,
`now_iso` (`events.py`), `EventStore` (`store.py`), `new_ulid` (`ulid.py`); the
slice-2b ambient surface `AmbientLifecycle`, `install_ambient`, `require_ambient`,
`reset_ambient` (`ambient.py`); the state vocabulary `LifecycleState`, `State`,
`Phase`, `LifecycleError`, `GuardedStartError` (`lifecycle_state.py`); the timing
config `HEARTBEAT_SECONDS`/`STALE_AFTER_SECONDS`/`TTL_SECONDS` + `Clock` +
`age_seconds` (now sourced from `timeutil`, slice 3a); and the slice-3a
projection read side — `observer_root` (`paths.py`), the schema
`LifecycleProjection`/`WorkspaceProjection`/`EnclosureNode`/`ProviderNode`/
`Metrics`/`ActionAvailability` (`projection.py`), and the fold
`project_lifecycle`/`project_workspace`/`enclosure_actions` (`reducer.py`). Slice
3b extends that surface with the analytical schema nodes (`Analytics`,
`DriftSnapshotNode`, `SidecarStaleNode`, `SetupSummaryNode`, `SetupProgressNode`,
`RouteCoverageNode`, `ToolReportNode`, `LedgerNode`, and task-23/24
`AgentPickupNode`) and the rollup
functions (`build_analytics`, `staleness_histogram`). Since
260707-HFX2-L1, `ExpectationRowNode` (the R2 durable expectation/deadline-row
projection surface) is re-exported alongside `AgentPickupNode` and pinned in
`__all__`. Slice 3c
re-exports `TaskDocNode` — and, R1, `SeriesNode` (the series-master surface node).
Slice 07 re-exports the served-onboarding ledger surface — `SERVED_RECORD_SCHEMA`,
`ServedRecord`, `ServedStore`, and `served_key` (`served_store.py`) — the dedup
substrate the `read_ar_files` front-door folds. `__all__` pins that
surface. The `ambient()` getter is intentionally *not*
re-exported here — `base.py` imports it directly from the submodule so it never
shadows the `ambient` module name. The I/O readers (`snapshots`,
`projection_store`) are **not** re-exported: consumers import them directly so
importing the package never drags in the providers/worktrees machinery.

## Invariants And Boundaries

- Slice 2a was the write side; slice 2b added the ambient lifecycle + signal
  surface; slice 3a adds the *pure* projection core (schema + reducer +
  `observer_root`) re-exported here.
- The dependency-heavy I/O readers (`snapshots`, `projection_store`) are imported
  directly by their consumers, never re-exported, so the package import stays
  light for the write side.

## Evidence

### Repo-Internal References

- The route this package exposes. [1]
- The ambient lifecycle singleton re-exported here. [2]
- The state vocabulary re-exported here. [3]
- The projection schema re-exported here. [4]
- The reducer functions re-exported here. [5]
- The shared store-root resolver re-exported here. [6]
- The timing config + age helper now sourced here. [7]
- The served-onboarding ledger re-exported here (`ServedStore`/`ServedRecord`/`served_key`/`SERVED_RECORD_SCHEMA`). [8]

- The current explicit facade exports the retained dependency-light observer and served-ledger names, not the removed guard/pickup/expectation/age-helper surface. [9]
