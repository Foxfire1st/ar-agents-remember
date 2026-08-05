# mcp/src/agents_remember/observer/__init__.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/__init__.py`   |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-08T14:35+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                                    |

## Purpose

`__init__.py` is the observer package's public surface: it re-exports the
substrate write side, the slice-2b ambient lifecycle surface, the slice-3a
projection read side (schema + reducer + the shared store-root resolver), and the
slice-07 served-onboarding ledger surface.

## Code Commentary

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
`RouteCoverageNode`, `ToolReportNode`, `LedgerNode`, `TokenSample`, and task-23/24
`AgentPickupNode`) and the rollup
functions (`build_analytics`, `staleness_histogram`, `token_series`). Since
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The route this package exposes. | `# mcp/src/agents_remember/observer/ — Observable-Lifecycle Substrate And Projection Overview` | onboarding/mcp/src/agents_remember/observer/overview.md:1-1042 |
| The ambient lifecycle singleton re-exported here. | `AmbientLifecycle` | mcp/src/agents_remember/observer/ambient.py:90-594 |
| The state vocabulary re-exported here. | `LifecycleState` | mcp/src/agents_remember/observer/lifecycle_state.py:187-210 |
| The projection schema re-exported here. | `LifecycleProjection` | mcp/src/agents_remember/observer/projection.py:99-138 |
| The reducer functions re-exported here. | `project_lifecycle`; `project_workspace` | mcp/src/agents_remember/observer/reducer.py:79-106; mcp/src/agents_remember/observer/reducer.py:126-179 |
| The shared store-root resolver re-exported here. | `observer_root` | mcp/src/agents_remember/observer/paths.py:32-34 |
| The timing config + age helper now sourced here. | `HEARTBEAT_SECONDS`; `STALE_AFTER_SECONDS`; `TTL_SECONDS`; `Clock` | mcp/src/agents_remember/observer/timeutil.py:21-21; mcp/src/agents_remember/observer/timeutil.py:29-31 |
| The served-onboarding ledger re-exported here (`ServedStore`/`ServedRecord`/`served_key`/`SERVED_RECORD_SCHEMA`). | `ServedStore`; `ServedRecord`; `served_key`; `SERVED_RECORD_SCHEMA` | mcp/src/agents_remember/observer/served_store.py:44-44; mcp/src/agents_remember/observer/served_store.py:52-54; mcp/src/agents_remember/observer/served_store.py:57-75; mcp/src/agents_remember/observer/served_store.py:78-121 |

## Update History

- 2026-08-03T02:46:38+02:00 — W3-B01 curator: curated 8 Repo-Internal table citations with exact overview, lifecycle, state, projection, reducer, path, timing, and served-ledger anchors. Verification metadata remains unchanged for closeout.
- 2026-07-08T14:35+02:00 — 260707-HFX2-L1: re-exports `ExpectationRowNode` alongside `AgentPickupNode` (R5 projection surfacing). Verification metadata pinned until closeout stamps the 260707-HFX2-L1 commit.
- 2026-06-25T13:20+02:00 — Task 23/24: re-exported `AgentPickupNode`, the projection surface for waiting-for-agent/check-chat task-row feedback.
- 2026-06-22T22:33+02:00 — Slice 07: re-export the served-onboarding ledger surface (`SERVED_RECORD_SCHEMA`, `ServedRecord`, `ServedStore`, `served_key`) and pin it in `__all__`; the I/O readers stay unexported by design. Body and references only — verification metadata pinned until closeout stamps the slice-07 code commit.
- 2026-06-19T03:17+02:00 — Slice 3c reopened (R1): re-export `SeriesNode` (the series-master surface node); the I/O readers (incl. `read_series_documents`) stay unexported by design. Verification metadata pinned until closeout stamps the R1 code commit.
- 2026-06-13T22:34: Slice 3c commit 2 — re-export `TaskDocNode` (the surface-7 node); the I/O readers stay unexported by design. Verification metadata pinned until closeout stamps the 3c commit-2 code commit.
- 2026-06-13T20:48+02:00: Slice 3b — re-export the analytical schema nodes
  (`Analytics` + the surface nodes + `TokenSample`) and the rollup functions
  (`build_analytics`, `staleness_histogram`, `token_series`); the I/O readers stay
  unexported by design. Verification metadata is pinned until closeout stamps the
  3b code commit.
- 2026-06-13T19:30+02:00: Slice 3a — re-export the projection read side
  (`observer_root`; the schema models; `project_lifecycle`/`project_workspace`/
  `enclosure_actions`) and source the timing constants + `Clock`/`age_seconds`
  from `timeutil`. The I/O readers (`snapshots`, `projection_store`) stay
  unexported by design. Verification metadata is pinned until closeout stamps the
  3a code commit.
- 2026-06-13T16:41+02:00: Slice 2b — re-export the ambient lifecycle surface
  (`AmbientLifecycle`, install/require/reset, config constants) and the state
  vocabulary (`LifecycleState`, `State`, `Phase`, errors). Verification metadata
  pinned until closeout stamps the 2b code commit.
- 2026-06-13T11:15+02:00: Created for slice 2a. Verification metadata is pinned
  until closeout stamps the 2a code commit.
