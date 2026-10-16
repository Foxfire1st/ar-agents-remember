# mcp/src/agents_remember/serving/projections/paths.py

## Purpose

`serving/projections/paths.py` (moved from `observer/paths.py` by 260731-EFA-L9) retains
the serving projection path helpers for `logs/observer` and drift snapshots. The original
single-resolution-point design is historical intent, not a current ownership census: this
module and `kernel/primitives/observer_paths.py` define separate same-named helpers.

## Governing Overview

[serving projections overview](overview.md)

## Code Commentary

This module's `observer_root(config)` delegates to its own `observer_logs_root` and returns
`config.coordination_root / "logs" / "observer"`. It imports `McpRuntimeConfig` only under
`TYPE_CHECKING` and has no reducer/snapshot imports. `serving/projections/projection_store.py`
imports this definition and calls it at the projection I/O edge.

The startup writer uses a different definition: `application/runtime/startup.py` imports
`observer_root` from `agents_remember.observer`, whose `__init__.py` re-exports it from
`kernel/primitives/observer_paths.py`. That kernel definition delegates to its own
`observer_logs_root`; matching results do not make the two definitions one owner.
`build_tool_event_writer` constructs `ToolEventWriter(EventStore(observer_root(config)), caller)`,
and `initialize_mcp_application` installs that workspace-river writer. `create_server` invokes
that application startup owner; it no longer installs an ambient lifecycle/EventStore.

Slice 3b adds the shared **drift-snapshot contract**: `observer_logs_root(
coordination_root)` (the `logs/observer` base both helpers share),
`drift_snapshot_dir(coordination_root)` (`logs/observer/drift`), and the
`DRIFT_SNAPSHOT_SCHEMA` string. Both the *producer* (the memory_quality drift run,
which persists the snapshot) and the *reader* (`snapshots.read_drift_snapshots`)
import these from here, so the on-disk contract has one definition and never drifts
between the two sides (North-Star #5).

## Invariants And Boundaries

- **Two definitions currently resolve `logs/observer`.** The projection I/O edge imports
  this module's `observer_root`; the application startup writer imports the separate kernel
  definition through the `observer` facade. Each delegates to its own `observer_logs_root`.
  Do not infer shared definition ownership from their equal path result.
- Keep this module free of reducer/snapshot imports; the startup writer does not currently
  import it for `observer_root`.
- The drift-snapshot dir + schema (slice 3b) live here as the single shared
  contract the producer and reader both import — neither hard-codes the path.

## Evidence

### Repo-Internal References

- The application startup writer installs workspace-river ToolEventWriter, using observer_root imported from the observer facade rather than this serving module. [1]
- create_server invokes the application startup owner; it does not install an ambient lifecycle. [6]
- The observer facade re-exports the kernel observer_root definition used by startup. [7]
- The kernel observer_root delegates to the kernel observer_logs_root; this is separate from the serving module definition. [8]

- The projection I/O edge imports this serving module's observer_root and calls it for the projection store root. [2]
- The drift snapshot reader using `drift_snapshot_dir` + the schema (3b). [3]
- The drift-run producer that writes the snapshot to `drift_snapshot_dir` (3b). [4]
- The store-layout + one-read-abstraction design. [5]

- The serving module separately defines observer_logs_root, observer_root and drift_snapshot_dir; its single-owner docstring is not an importer inventory. [9]
