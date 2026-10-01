# mcp/src/agents_remember/serving/projections/paths.py

## Purpose

`serving/projections/paths.py` (moved from `observer/paths.py` by 260731-EFA-L9) is the single resolution point for the observer store root — the one
read/write path abstraction (design §2.3 / North-Star #5) so a future synced
coordination store is a swap at one site, not a refactor (slice 3a).

## Governing Overview

[serving projections overview](overview.md)

## Code Commentary

`observer_root(config)` returns `config.coordination_root / "logs" / "observer"`.
The module is deliberately dependency-light: `McpRuntimeConfig` is imported only
under `TYPE_CHECKING` (the body just walks `coordination_root`), so the **write**
side — `server.create_server` installing the ambient `EventStore` — can resolve
the root without importing the read-side reducer/snapshot machinery.

Slice 3b adds the shared **drift-snapshot contract**: `observer_logs_root(
coordination_root)` (the `logs/observer` base both helpers share),
`drift_snapshot_dir(coordination_root)` (`logs/observer/drift`), and the
`DRIFT_SNAPSHOT_SCHEMA` string. Both the *producer* (the memory_quality drift run,
which persists the snapshot) and the *reader* (`snapshots.read_drift_snapshots`)
import these from here, so the on-disk contract has one definition and never drifts
between the two sides (North-Star #5).

## Invariants And Boundaries

- **One place resolves `logs/observer`.** Both the writer (`server.py`) and the
  reader (`projection_store`) call `observer_root`; no call site hard-codes the
  path.
- Keep this module free of reducer/snapshot imports so importing it stays cheap
  for the write side.
- The drift-snapshot dir + schema (slice 3b) live here as the single shared
  contract the producer and reader both import — neither hard-codes the path.

## Evidence

### Repo-Internal References

- The writer that resolves the root here to install the ambient "install_ambient(AmbientLifecycle(EventStore(observer_root(config))))" ("def create_server(config: McpRuntimeConfig) -> Any:" → "def initialize_mcp_application(config: McpRuntimeConfig) -> None:"). [1]
- The reader I/O edge that resolves the same root. [2]
- The drift snapshot reader using `drift_snapshot_dir` + the schema (3b). [3]
- The drift-run producer that writes the snapshot to `drift_snapshot_dir` (3b). [4]
- The store-layout + one-read-abstraction design. [5]
