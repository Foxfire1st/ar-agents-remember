# mcp/tests/test_codex_history_production_path.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_codex_history_production_path.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-12T04:15+02:00               |
| lastVerifiedCommitHash |  `65cb81f7de4db13c0627264fec1eb46f444e0ee3`|
| lastVerifiedCommitDate | 2026-08-12T04:57:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Replays the original 4,846,576-byte failure through the production-shaped Codex stdio, capability
probe, adapter, Unix control IPC, and selected-child active projection path while proving second-wave
failure containment and sibling/parent continuity.

## Code Commentary

#

- 260731-EFA-L7 (trace delta): the Codex history production-path suite keeps its assertions; its imports were reconciled with the split adapter family.
## Logic

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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The protocol accepts valid payloads through the separate 128 MiB emergency fuse. | `CODEX_REMOTE_COMPATIBILITY_CEILING_BYTES` | mcp/src/agents_remember/serving/codex_app_server_protocol.py:27-27 |
| The active projector hydrates only selected children and contains typed failures. | `ChildHistoryProjection` | mcp/src/agents_remember/serving/conversation/active/projector/child_history.py:25-173 |
| "async def refresh_agent_native(self" on the facade — the entry point this test drives — hydrates then delegates to that child-history projection. | "async def refresh_agent_native(self", "return await self._coordinator.refresh_child(thread_id)" | mcp/src/agents_remember/serving/conversation/active/projector/facade.py:159-160; mcp/src/agents_remember/serving/conversation/active/projector/rebuild_coordinator.py:146-148 |

## Cross-Repo References

The fake Codex process is repository-local; no external repository is executed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-12T04:15+02:00 — No content impact: 260731-EFA-L22 migrated the composed fake process's
  initialize user agent to the current Desktop host-first form with exact client suffix; measured
  history transport, containment, and continuity assertions are unchanged.

- 2026-08-07T23:35:00+02:00 — 260731-EFA-L7 curator (trace delta): body verified against the current code and updated (260731-EFA-L7 (trace delta): the Codex history production-path suite keeps its assertions; its impor...). Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-02T16:45:41+02:00 — 260731-EFA-L6 curator W1-B10: repaired 12 citation findings (3 rows and 6 historical pointers); scoped recheck clean.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired the citation broken by the
  `active/projector.py` -> `active/projector/` package split (commit `3a8ff70`). The selected-child
  behaviour this test drives now lives in `projector/child_history.py`: `ChildHistoryProjection`
  cit:([`ChildHistoryProjection`], mcp/src/agents_remember/serving/conversation/active/projector/child_history.py:25-173) — the four-way eligibility gate and `already-hydrated` short-circuit cit:([`ChildHistoryProjection`], mcp/src/agents_remember/serving/conversation/active/projector/child_history.py:25-173), the
  `MAX_AGENT_NATIVE_INFLIGHT`=64 capacity refusal and per-thread singleflight task cit:([`ChildHistoryProjection`], mcp/src/agents_remember/serving/conversation/active/projector/child_history.py:25-173), and
  `_hydrate`'s containment of `NativeHistoryLimitExceeded` / `NativeHistoryUnavailable` into an
  `unavailable` `AgentHistoryHydration` plus an `agent_history_state_item`, with the symmetric
  `recovered` emission on a later successful retry cit:([`ChildHistoryProjection`], mcp/src/agents_remember/serving/conversation/active/projector/child_history.py:25-173) — which is exactly the
  `cyclic.status == "unavailable"` + sibling-continuity assertion at cit:([`test_measured_history_crosses_transport_probe_ipc_and_selected_projection`], mcp/tests/test_codex_history_production_path.py:281-365) of this test. Added a
  second row for the call path the test actually touches: `facade.refresh_agent_native` cit:([`refresh_agent_native`], mcp/src/agents_remember/serving/conversation/active/projector/facade.py:159-160)
  -> `RebuildCoordinator.refresh_child` cit:([`refresh_child`], mcp/src/agents_remember/serving/conversation/active/projector/rebuild_coordinator.py:150-152) -> that projection.

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
