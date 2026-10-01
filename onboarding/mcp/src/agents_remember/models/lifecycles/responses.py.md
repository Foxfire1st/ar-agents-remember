# mcp/src/agents_remember/models/lifecycles/responses.py

## Governing Overview

[lifecycles overview](overview.md)

## Purpose

Response models for lifecycle signal payloads — strict, operation-bearing
`ToolResponse` subclasses. These are the wire contract the builders return,
deliberately distinct from the persisted `observer.Event` record.

## Code Commentary

`LifecycleResponse(ToolResponse)` is the shared shape: `lifecycleId`, `state`,
and `phase`. This module owns the shared `LiveState`, `EndOutcome`, `TerminalState`, `State`, and
`Phase` vocabularies; observer lifecycle state imports them rather than redeclaring the wire sets.
Subclasses:
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
- `state`/`phase` are declared once here and imported by observer lifecycle state, so
  the response and persisted lifecycle projection cannot drift apart.

## Evidence

### Repo-Internal References

- The `ToolResponse` strict envelope base (`ok`/`operation`/`tokens`). [1]
- The `State`/`Phase` Literals reused as response field types (declared here since L9). [2]
- The registry maps lifecycle signal tools to their declared response models. [3]
- The public response-model registry filters internal compatibility tool names from the complete model registry. [4]
- The builders that assemble payloads validated against these models; `lifecycle_start_payload` fills `frontHalfRundown`. [5]
- Owner of the `FRONT_HALF_RUNDOWN` list content emitted as `frontHalfRundown`. [6]
- The persisted-record peer these are deliberately *not*. [7]
