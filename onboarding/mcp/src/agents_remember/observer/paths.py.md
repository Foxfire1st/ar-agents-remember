# mcp/src/agents_remember/observer/paths.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/paths.py`      |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-13T20:48+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
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

| Finding | Source Path |
| --- | --- |
| The writer that resolves the root here to install the ambient `EventStore`. | [mcp/server.py](agents-remember/mcp/src/agents_remember/mcp/server.py) |
| The reader I/O edge that resolves the same root. | [projection_store.py](agents-remember/mcp/src/agents_remember/observer/projection_store.py) |
| The drift snapshot reader using `drift_snapshot_dir` + the schema (3b). | [snapshots.py](agents-remember/mcp/src/agents_remember/observer/snapshots.py) |
| The drift-run producer that writes the snapshot to `drift_snapshot_dir` (3b). | [onboarding_drift_check/summary.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py) |
| The store-layout + one-read-abstraction design. | [docs/design/observable-lifecycle.md](agents-remember/docs/design/observable-lifecycle.md) |

## Update History

- 2026-06-13T20:48+02:00: Slice 3b — added the shared drift-snapshot contract
  (`observer_logs_root`, `drift_snapshot_dir`, `DRIFT_SNAPSHOT_SCHEMA`) so the
  memory_quality producer and the observer reader resolve one on-disk path/schema.
  Verification metadata is pinned until closeout stamps the 3b code commit.
- 2026-06-13T19:30+02:00: Created for slice 3a — the shared `observer_root(config)`
  resolver, extracted from the inline path in `server.py`. Verification metadata
  is pinned until closeout stamps the 3a code commit.
