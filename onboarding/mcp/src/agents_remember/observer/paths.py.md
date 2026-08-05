# mcp/src/agents_remember/observer/paths.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/paths.py`      |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-13T20:48+02:00                           |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                                    |

## Purpose

`paths.py` is the single resolution point for the observer store root — the one
read/write path abstraction (design §2.3 / North-Star #5) so a future synced
coordination store is a swap at one site, not a refactor (slice 3a).

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The writer that resolves the root here to install the ambient `EventStore` (`create_server` → `initialize_mcp_application`). | `install_ambient`; `observer_root` | mcp/src/agents_remember/application/server_startup.py:15-17; mcp/src/agents_remember/mcp/server.py:17-21 |
| The reader I/O edge that resolves the same root. | `observer_root` | mcp/src/agents_remember/observer/projection_store.py:211-222 |
| The drift snapshot reader using `drift_snapshot_dir` + the schema (3b). | `read_drift_snapshots` | mcp/src/agents_remember/observer/snapshots.py:934-970 |
| The drift-run producer that writes the snapshot to `drift_snapshot_dir` (3b). | `drift_snapshot_dir` | mcp/src/agents_remember/observer/paths.py:37-39 |
| The store-layout + one-read-abstraction design. | `### 2.3 Store layout` | docs/design/observable-lifecycle.md:172-194 |

## Update History

- 2026-08-04T18:16+02:00 — 260731-EFA-L6 S18-B16 curator: repaired 4 citation rows; the writer row was re-bound to the moved install path — `create_server` (mcp/server.py L17-L21) now delegates to `initialize_mcp_application` (application/server_startup.py L15-L17), which installs the ambient EventStore with `observer_root`. Scoped fixer + non-fixing recheck green under the frozen snapshot; verification metadata unchanged.

- 2026-06-13T20:48+02:00: Slice 3b — added the shared drift-snapshot contract
  (`observer_logs_root`, `drift_snapshot_dir`, `DRIFT_SNAPSHOT_SCHEMA`) so the
  memory_quality producer and the observer reader resolve one on-disk path/schema.
  Verification metadata is pinned until closeout stamps the 3b code commit.
- 2026-06-13T19:30+02:00: Created for slice 3a — the shared `observer_root(config)`
  resolver, extracted from the inline path in `server.py`. Verification metadata
  is pinned until closeout stamps the 3a code commit.
