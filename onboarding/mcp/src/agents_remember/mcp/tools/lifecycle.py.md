# mcp/src/agents_remember/mcp/tools/lifecycle.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Payload builders for lifecycle signal payloads. Each drives the
process-singleton ambient lifecycle (`require_ambient`) and returns the modeled
response through `_tool_payload`, so a lifecycle signal is itself an attributed
tool call.

## Code Commentary

`_state_fields(state)` pulls `lifecycleId`/`state`/`phase` from a
`LifecycleState`. The builders: `lifecycle_start_payload` (no args; always starts
fleeting), `lifecycle_block_payload(kind, prompt, options)` (lower-level
compatibility builder that echoes the ask via `build_ask`; public agent gate
choreography uses `lifecycle_gate_payload` in `gates.py`), `lifecycle_resume_payload`,
`lifecycle_turn_end_notification_payload(summary)` (the task-28 NOTIFY-AND-CONTINUE
turn end: drives `await_developer(summary=…)` → state `awaiting-developer` and
returns immediately — no gate, no wait — echoing `summary` in the response),
`lifecycle_end_payload(outcome)`,
`lifecycle_phase_payload(phase)` (validates the raw string via `coerce_phase`),
and `switch_lifecycle_payload(on_unsaved=None)` (validates the decision via
`coerce_save_decision` and forwards it to `AmbientLifecycle.switch` — leaving a
fleeting lifecycle without a decision raises `SaveGateRequired`). Each returns
`_tool_payload("<name>", {...})` with `ok`/`operation` plus the state fields;
start/switch add `fleeting`. `lifecycle_start_payload` additionally emits
`frontHalfRundown` (= `list(FRONT_HALF_RUNDOWN)` imported top-level from
`next_step.py`) — the one-time, non-linear front-half roadmap (reframe →
research → job-selection → task-file-exists? → task_doc → notify via
`lifecycle_turn_end_notification` and stop; task 28 repointed this closing step
off the parked `lifecycle_gate(plan-approval)` hand-off). It is prose, emitted
once at start, because the per-tool `nextStep` chain only begins once the worktree
contract exists (`worktree_start` onward).

Because every builder routes through `_tool_payload`, the choke point emits a
`tool.completed` for the signal call too: `lifecycle_start` produces
`lifecycle.started` then its own `tool.completed`, while `lifecycle_end` clears
the ambient first so it produces no trailing `tool.completed` by construction.
`lifecycle_turn_end_notification` is the one tool the choke-point auto-dismiss
skips by name (task 28), so its own response still reports the `awaiting-developer`
state before the next AR tool call resumes the lifecycle to `running`.

## Invariants And Boundaries

- The builders are config-free: they use the process singleton, not
  `McpRuntimeConfig`. `require_ambient` raises `LifecycleError` if no ambient is
  installed in the process.
- Request validation stays at the boundary (`coerce_phase`; `outcome` validated
  in `AmbientLifecycle.end`); the builders only assemble the response dict.
- `switch_lifecycle` leaves the current lifecycle and mints a fresh one; leaving a
  fleeting one needs an explicit `on_unsaved` (save/discard) or it raises
  `SaveGateRequired`. Resuming an *existing* lifecycle is contract-resolved through
  `worktree_attach`, not this builder — the model never handles ids.

## Evidence

### Repo-Internal References

- The singleton these builders drive through `application/lifecycle_tools`, plus the ambient requirement and the ask builder. [1]
- The `coerce_phase` boundary validator. [2]
- The choke point each builder returns through. [3]
- Source of `FRONT_HALF_RUNDOWN`, emitted as `frontHalfRundown` on `lifecycle_start`. [4]
- The response models these payloads validate against. [5]
- Where these lifecycle signal tools (now including `lifecycle_turn_end_notification`) are declared — `register_lifecycle_tools`, which takes the config unused because these payloads act on the ambient lifecycle. [6]
- The design's signal surface (§1.3). [7]
