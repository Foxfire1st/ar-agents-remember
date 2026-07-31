# mcp/tests/test_codex_history_production_path.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_codex_history_production_path.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-27T14:20+02:00 |
| lastVerifiedCommitHash |  `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |  2026-07-31T19:28:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Replays the original 4,846,576-byte failure through the production-shaped Codex stdio, capability
probe, adapter, Unix control IPC, and selected-child active projection path while proving second-wave
failure containment and sibling/parent continuity.

## Code Commentary

### Logic

One fake app-server process emits the exact measured below-fuse response. The test observes
items-list `-32601`, turns/full success, and no legacy `thread/read`. It then introduces a cyclic
second-wave child and a healthy sibling: only the cyclic child becomes unavailable, while the first
child, second sibling, parent control, and event path remain usable.

### Conventions

This is deliberately a composed seam rather than another unit fixture. Its exact payload size and
request transcript protect the diagnosed transport/projection interaction.

### Invariants And Boundaries

- The measured valid payload must cross the shared transport.
- Installed 0.145-shaped evidence is items unsupported and turns accepted; the test must never claim
  that both bounded methods succeed.
- Child failure remains a typed local projection state and never tears down the parent bridge.

### Todos

None known.

## Docs References

No Domain Documentation source is configured.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The protocol accepts valid payloads through the separate 128 MiB emergency fuse. | L18-L23; L217-L240 | [codex_app_server_protocol.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_protocol.py) |
| The active projector hydrates only selected children and contains typed failures. | L67-L137 | [projector/child_history.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/projector/child_history.py) |
| `refresh_agent_native` on the facade — the entry point this test drives — hydrates then delegates to that child-history projection. | L159-L160; L146-L148 | [projector/facade.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/projector/facade.py); [projector/rebuild_coordinator.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/projector/rebuild_coordinator.py) |

## Cross-Repo References

The fake Codex process is repository-local; no external repository is executed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired the citation broken by the
  `active/projector.py` -> `active/projector/` package split (commit `3a8ff70`). The selected-child
  behaviour this test drives now lives in `projector/child_history.py`: `ChildHistoryProjection`
  L67-L137 — the four-way eligibility gate and `already-hydrated` short-circuit (L67-L76), the
  `MAX_AGENT_NATIVE_INFLIGHT`=64 capacity refusal and per-thread singleflight task (L77-L97), and
  `_hydrate`'s containment of `NativeHistoryLimitExceeded` / `NativeHistoryUnavailable` into an
  `unavailable` `AgentHistoryHydration` plus an `agent_history_state_item`, with the symmetric
  `recovered` emission on a later successful retry (L99-L137) — which is exactly the
  `cyclic.status == "unavailable"` + sibling-continuity assertion at L346-L349 of this test. Added a
  second row for the call path the test actually touches: `facade.refresh_agent_native` (L159-L160)
  -> `RebuildCoordinator.refresh_child` (L146-L148) -> that projection.

- 2026-07-31T16:50+02:00 — No content impact: 260731-EFA-L2 curator checked this file against the
  leaf diff. The single test body was split for the complexity gate — projector construction moved
  into `_projector_over_control_entry` and the transport-log checks into `_assert_wire_evidence` —
  and `ActiveSessionProjector` is now built from `ProjectedSession(...)` plus
  `readers=BridgeReaders(...)`, with the roster fixture passing `agents=CollabAgents(...)`. The
  assertions themselves moved without changing: the single `thread/items/list` probe refused with
  `-32601`, the measured `responseBytes`, the `None`/`opaque-A`/`opaque-B` cursor cycle, the
  healthy-sibling turn call and the "never `thread/read`" check all still run in the same test.
  The sidecar names no helper and cites no line range into this file, so its Logic paragraph and
  all three invariants hold as written.
- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: created strict 1:1 onboarding for the exact
  measured-size production seam and second-wave continuity regression. Verification metadata
  remains blank because the new test is uncommitted.
