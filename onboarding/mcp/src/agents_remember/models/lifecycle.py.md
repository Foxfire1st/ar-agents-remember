# mcp/src/agents_remember/models/lifecycle.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                                |
| path                   | `mcp/src/agents_remember/models/lifecycle.py`  |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-06-27T22:00+02:00                      |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`     |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                                  |

## Purpose

Response models for lifecycle signal payloads — strict, operation-bearing
`ToolResponse` subclasses. These are the wire contract the builders return,
deliberately distinct from the persisted `observer.Event` record.

## Code Commentary

`LifecycleResponse(ToolResponse)` is the shared shape: `lifecycleId`, `state`,
and `phase`, where `state`/`phase` reuse the observer's `State`/`Phase` Literals
so the response is as drift-proof as the event envelope. Subclasses:
`LifecycleStartResponse` and `SwitchLifecycleResponse` add `fleeting`, and
`LifecycleStartResponse` additionally carries an optional
`frontHalfRundown: list[str] | None = None` (task 27) — the one-time, non-linear
front-half prose roadmap (reframe → research → job-selection →
task-file-exists? → `task_doc`). It is declared because the model is strict
(`extra="forbid"`); kept optional + `exclude_none` so older callers and the
conformance fixtures that omit it stay valid. The list content is owned by
`next_step.py::FRONT_HALF_RUNDOWN` and emitted in
`mcp/tools/lifecycle.py::lifecycle_start_payload`, not synthesized here.
`LifecycleBlockResponse` adds an optional `ask` and is now retained for the
lower-level compatibility builder rather than advertised as a public MCP tool;
`LifecycleResumeResponse`, `LifecyclePhaseResponse`, and `LifecycleEndResponse`
are the bare shape, distinguished by their `operation` value.
`LifecycleTurnEndNotificationResponse(LifecycleResponse)` adds a required
`summary: str` — it is the public response for the task-28
`lifecycle_turn_end_notification` tool, the NOTIFY-AND-CONTINUE turn end
(leaf-28): the lifecycle is left `awaiting-developer` (non-terminal) and
`summary` echoes the developer-facing turn-end note, with the next AR tool call
auto-resuming the lifecycle to running. The parked `lifecycle_gate` path keeps
using `LifecycleGateResponse` (in `models/gates.py`), unchanged. All are
registered in `TOOL_RESPONSE_MODELS` and inherit `extra="forbid"`.

## Invariants And Boundaries

- AR-owned, so STRICT (`extra="forbid"`) — the conformance test asserts every
  non-flexible registered model forbids extra fields.
- Not an `observer.Event`: these carry the token envelope and are MCP responses;
  the `Event` record carries no token fields and is never returned by a tool.
- `state`/`phase` import the observer Literals rather than redeclaring strings, so
  the response and the lifecycle state cannot drift apart.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The `ToolResponse` strict envelope base (`ok`/`operation`/`tokens`). | "class ToolResponse(ResponseModel):" | mcp/src/agents_remember/models/base.py:63-63 |
| The `State`/`Phase` Literals reused as response field types. | "State = Literal[LiveState, TerminalState]"; "Phase = Literal[" | mcp/src/agents_remember/observer/lifecycle_state.py:120-120; mcp/src/agents_remember/observer/lifecycle_state.py:124-124 |
| Where these models are registered against tool names. | "\"ping\": PingResponse,"; "PUBLIC_TOOL_RESPONSE_MODELS: dict[str, type[ResponseEnvelope]] = {" | mcp/src/agents_remember/models/tool_registry.py:117-117; mcp/src/agents_remember/models/tool_registry.py:181-181 |
| The builders that assemble payloads validated against these models; `lifecycle_start_payload` fills `frontHalfRundown`. | "def lifecycle_start_payload() -> dict[str, Any]:" | mcp/src/agents_remember/mcp/tools/lifecycle.py:20-20 |
| Owner of the `FRONT_HALF_RUNDOWN` list content emitted as `frontHalfRundown`. | "FRONT_HALF_RUNDOWN: list[str] = [" | mcp/src/agents_remember/application/next_step.py:57-57 |
| The persisted-record peer these are deliberately *not*. | "class Event(BaseModel):"; "OBSERVER_EVENT_SCHEMA =" | mcp/src/agents_remember/observer/events.py:23-23; mcp/src/agents_remember/observer/events.py:39-39 |

## Update History

- 2026-08-02T17:00+02:00 — 260731-EFA-L6 curator W1-B03: repaired 6 citation rows with exact anchors and current source paths; scoped citation recheck recorded separately. Verification metadata remains pinned until closeout.

- 2026-06-27T22:00+02:00 — Task 28 (NOTIFY-AND-CONTINUE turn end): added `LifecycleTurnEndNotificationResponse(LifecycleResponse)` with a required `summary: str` — the public, strict response model for the new `lifecycle_turn_end_notification` tool (lifecycle left `awaiting-developer`, the developer-facing summary echoed, next AR call auto-resumes to running). The parked `lifecycle_gate`/`LifecycleBlockResponse` path is kept untouched. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T18:43+02:00 — Task 27: `LifecycleStartResponse` gained an optional `frontHalfRundown: list[str] | None = None` — the one-time front-half prose roadmap emitted by `lifecycle_start`. Declared because the model is strict; optional + `exclude_none` keeps older callers/fixtures valid. Content owned by `next_step.py::FRONT_HALF_RUNDOWN`, emitted via `lifecycle.py::lifecycle_start_payload`.
- 2026-06-26T14:16+02:00 — Task 25: classified `LifecycleBlockResponse` as the response model for the retained lower-level compatibility builder; the public gate path now uses `lifecycle_gate` and `LifecycleGateResponse`.
- 2026-06-13T16:41+02:00: Created for slice 2b — the six `lifecycle_*` strict
  response models. Verification metadata is pinned until closeout stamps the 2b
  code commit.
