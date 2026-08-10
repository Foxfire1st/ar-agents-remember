# mcp/src/agents_remember/mcp/tools/lifecycle.py

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `mcp/src/agents_remember/mcp/tools/lifecycle.py`   |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-06-27T22:00+02:00                      |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`         |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                      |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The singleton these builders drive through `application/lifecycle_tools`, plus the ambient requirement and the ask builder. | "def require_ambient("; "def build_ask(" | mcp/src/agents_remember/observer/ambient.py:638-638; mcp/src/agents_remember/observer/ambient.py:674-674; mcp/src/agents_remember/application/lifecycle_tools.py:3-16 |
| The `coerce_phase` boundary validator. | `coerce_phase` | mcp/src/agents_remember/observer/lifecycle_state.py:149-153 |
| The choke point each builder returns through. | `_tool_payload` | mcp/src/agents_remember/mcp/tools/base.py:73-75 |
| Source of `FRONT_HALF_RUNDOWN`, emitted as `frontHalfRundown` on `lifecycle_start`. | `FRONT_HALF_RUNDOWN` | mcp/src/agents_remember/application/next_step.py:57-69; mcp/src/agents_remember/application/lifecycle_tools.py:41-41 |
| The response models these payloads validate against. | `LifecycleResponse` | mcp/src/agents_remember/models/lifecycle.py:30-35 |
| Where these lifecycle signal tools (now including `lifecycle_turn_end_notification`) are declared — `register_lifecycle_tools`, which takes the config unused because these payloads act on the ambient lifecycle. | `register_lifecycle_tools` | mcp/src/agents_remember/mcp/registration/lifecycle.py:18-59 |
| The design's signal surface (§1.3). | `### 1.3 Signals (the complete model-facing surface)` | docs/design/observable-lifecycle.md:71-88 |

## Update History

- 2026-08-04T18:13+02:00 — 260731-EFA-L6 S18-B14 curator: repaired 6 citation rows with exact anchors and ledger-verified ranges; re-pointed the FRONT_HALF_RUNDOWN citation from the removed `mcp/tools/next_step.py` to `application/next_step.py` plus its emission site in `application/lifecycle_tools.py`, narrowed the singleton claim to the application-layer delegation, and cited the §1.3 design heading at its exact level. Scoped citation recheck is green. Verification metadata remains pinned until closeout.

- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: `lifecycle.py` itself is unchanged by this leaf,
  but its reference row pointed at `server.py` for where these six signals are registered; they are
  now declared in `mcp/registration/lifecycle.py`, whose registrar takes the config unused because
  these payloads act on the ambient lifecycle. Reference repointed; nothing else touched.
- 2026-06-27T22:00+02:00 — Task 28 (NOTIFY-AND-CONTINUE turn end): added `lifecycle_turn_end_notification_payload(summary)` — it drives `require_ambient().await_developer(summary=…)` (state → `awaiting-developer`) and returns immediately through `_tool_payload` with no gate and no wait, echoing `summary`. It is the one builder the choke-point auto-dismiss skips by name, so its own response reports `awaiting-developer`. Also repointed the `frontHalfRundown` closing step off the parked `lifecycle_gate(plan-approval)` hand-off to "notify via `lifecycle_turn_end_notification` and stop". Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T18:43+02:00 — Task 27: `lifecycle_start_payload` now adds `"frontHalfRundown": list(FRONT_HALF_RUNDOWN)` — the one-time, non-linear front-half roadmap — via a new top-level import `from .next_step import FRONT_HALF_RUNDOWN`. The per-tool nextStep chain only begins once the worktree exists. No other builders changed.
- 2026-06-26T14:16+02:00 — Task 25: classified `lifecycle_block_payload` as a lower-level compatibility builder; the public gate path now lives in `gates.lifecycle_gate_payload`.
- 2026-06-13T18:45+02:00: Slice 2c — `switch_lifecycle_payload` gained `on_unsaved`
  (validated via `coerce_save_decision`, forwarded to `AmbientLifecycle.switch`);
  leaving a fleeting lifecycle now routes through the blocking save gate.
  Verification metadata is pinned until closeout stamps the 2c code commit.
- 2026-06-13T16:41+02:00: Created for slice 2b — the six `lifecycle_*` payload
  builders. Verification metadata is pinned until closeout stamps the 2b code
  commit.
