# test_next_step.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_next_step.py`              |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T09:05+02:00                     |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

Nearest route overview: [../overview.md](../overview.md) (the `mcp/` overview).

## Purpose

Pins the task-27 lifecycle next-step engine
`mcp/src/agents_remember/mcp/tools/next_step.py`: the single state→next-move
projection attached to every tool response at the `mcp.tools.base._tool_payload`
choke point. Two test classes split the pure state machine (`compute_next_step`
/ `_from_guidance`) from the exception-contained edge (`next_step_for`) plus the
`lifecycle_start` rundown. Guards the contract that an in-lifecycle response
always carries one actionable hint while a lifecycle-less response stays silent,
and that the I/O edge never raises into a tool call. Task 28 added the
NOTIFY-AND-CONTINUE assertions: every ACTIVE hint (front-half/`decide`/the
`_gate_after` overlays/the `lifecycle_start` rundown) now points at
`lifecycle_turn_end_notification`, an `awaiting-developer` lifecycle hints the
stop (`nextTool=None`), and an end-to-end test proves the choke-point auto-dismiss
(the notification does not self-dismiss; the next call resumes). The parked
`blocked`-gate await/resume tests stay intact.

260731-EFA-L4 added the **advertised-count** half: both keys the choke point writes
(`nextStep`, `supervisorBanner`) are now declared fields of the response envelope, are set on the
model *before* the single dump, and must therefore be inside the `tokens` number the response
advertises — and the opportunistic banner must never take down the tool call it rides on.

## Code Commentary

### Logic

`PureEngineTests` exercises `compute_next_step(state, contract, tool_name,
guidance=…)` directly:

- **No hint** outside a lifecycle (`state=None`) and when terminal
  (`state="completed"`) → `None`.
- **`lifecycle_end`** with `state=None` returns the loop-back `NextStep` whose
  `summary` names both `lifecycle_start` and `worktree_attach`; any other
  lifecycle-less call (`ping`) stays `None`.
- **Blocked at a gate** (`state="blocked"`, asserted for both `close` and `build`
  phases, `test_blocked_at_a_gate_awaits_the_decision`): returns `_AWAIT_GATE` —
  `nextTool="lifecycle_resume"` and a summary containing "await" — never the
  post-gate operational step, proving the gate can open in any phase and is never
  jumped. The PARKED gate path — unchanged by task 28.
- **Awaiting-developer** (`state="awaiting-developer"`, phase `build`,
  `test_awaiting_developer_hints_the_stop`): the task-28 NOTIFY-AND-CONTINUE stop —
  `nextTool is None` and the summary contains "resumes automatically".
- **Front-half generic** (`contract=None`, phase `reframe-research`,
  `test_front_half_generic_points_back_to_the_rundown`): summary mentions
  "rundown", and task 28 repointed it to `nextTool="lifecycle_turn_end_notification"`
  with a `summary` in `nextArgs`.
- **`decide`** (`contract=None`, `test_decide_points_to_the_turn_end_notification`)
  → `nextTool="lifecycle_turn_end_notification"` with a `summary` in `nextArgs`
  (task 28 repointed it off the old `worktree-intent` gate).
- **Linear, no gate moment** (contract present + `guidance=_GUIDANCE`):
  delegates to `_from_guidance` → `nextOperation="continue_work"`,
  `nextTool="worktree_status"`, and no `kind` in `nextArgs`.
- **Turn-end overlay** via `_gate_after`, keyed on tool + contract sub-state —
  task 28 repointed all three off their former approval gates onto
  `lifecycle_turn_end_notification` (each asserts that `nextTool` + a `summary` in
  `nextArgs`): `worktree_closeout_preview` *while `approved_for_commit` is False*
  (`test_closeout_preview_hints_the_turn_end_until_approved`), falling back to
  guidance once approved; `worktree_integrate` (`closeout_status="completed"`,
  `integration_status="not-started"`, `test_integrate_dry_run_hints_the_turn_end`);
  `lifecycle_finalize_task` (`integration_status="completed"`, `cleanup="pending"`,
  `test_finalize_dry_run_hints_the_turn_end`).
- **`_from_guidance`** maps the guidance dict's `summary`/`nextOperation`/
  `nextTool`/`nextArgs` onto the `NextStep` shape.

`EdgeAndChokePointTests` installs a real `AmbientLifecycle` (over a tmp
`EventStore`, with `timing=AmbientTiming(heartbeat_seconds=3600)`) via
`install_ambient`, with cleanups for
`reset_ambient` + `amb.shutdown` + tmpdir. It drives `next_step_for(amb, tool_name)`, which
**returns a `NextStep | None` model** — since 260731-EFA-L4 the choke point assigns it to the
declared envelope field `ResponseEnvelope.nextStep` rather than writing a dumped dict into the
payload afterwards, so the edge assertions read attributes (`step.nextTool`, `step.nextArgs`) just
as the pure ones do:

- **No active lifecycle** → `None`.
- **Blocked gate (live seam)**: after `amb.start()` + `amb.block(kind=…)`,
  `next_step_for(amb, "lifecycle_gate")` returns `nextTool="lifecycle_resume"` —
  the raised gate's response carries the await/resume hint, not a premature step.
- **Front half / dry-run windows** (`test_next_step_for_*`,
  `test_dry_run_window_in_decide_shows_turn_end`,
  `test_corrupt_contract_degrades_gracefully`): a `promote`d lifecycle whose
  enclosure file is missing or torn (`}{ not a contract`) degrades to the
  front-half hint — task 28 made it `nextTool="lifecycle_turn_end_notification"`
  with a `summary` in `nextArgs` (never silent, never raises).
- **Linear delegation**: a written contract (`write_contract`) + promote yields
  `nextOperation="continue_work"` (`test_next_step_for_linear_delegates_to_guidance`).
- **Choke point**: `lifecycle_start_payload()` carries
  `frontHalfRundown == FRONT_HALF_RUNDOWN` and a `nextStep` whose
  `nextTool == "lifecycle_turn_end_notification"` with a `summary` in `nextArgs`
  cit:([`test_tool_payload_attaches_next_step_and_lifecycle_start_emits_rundown`], mcp/tests/test_next_step.py:298-303).
- **Advertised token count covers the hint** (L305-L317,
  `test_advertised_token_count_covers_the_attached_next_step`): the hint is several hundred
  characters and it is on the wire, so it is in the count. It was not —
  `finalize_payload_tokens` ran over the dump and `nextStep` was written in afterwards, so every
  in-lifecycle response advertised a total that excluded the largest thing the choke point adds.
  Asserted as a **fixed point over the payload as served**: `payload["tokens"] ==
  count_response_tokens(payload)`, and then that recounting the payload *without* `nextStep`
  yields strictly less — so the equality cannot be satisfied incidentally.
- **…and the supervisor banner** (L319-L331,
  `test_advertised_token_count_covers_the_agent_notifier_banner`): the same invariant for the other
  choke-point field. A supervisor that ticked and then went quiet past the cutoff
  (`AgentNotifierHeartbeatStore(self.root).tick(now=now - 6h)`) puts a banner on **every** response;
  the test asserts `"supervisor stale"` is in `payload["supervisorBanner"]`, the same fixed-point
  and strictly-less pair, and — the point of the leaf — `PingResponse.model_validate(payload)`,
  which is only possible now that `supervisorBanner` is a declared envelope field.
- **A raising staleness probe degrades to silence** (L333-L345,
  `test_a_raising_staleness_probe_degrades_to_silence`): patching
  `agents_remember.mcp.tools.base.agent_notifier_staleness_banner` to raise `OSError` must yield
  **no** `supervisorBanner` key, a response that still validates, and a `tokens` value that is
  still the fixed point. The banner is opportunistic and defended: it must never take down the
  tool call it rides on, and the response must not be a half-built envelope.
- **Auto-dismiss end-to-end**
  (`test_turn_end_notification_does_not_self_dismiss_then_next_call_resumes`):
  `lifecycle_turn_end_notification_payload(...)` parks the lifecycle in
  `awaiting-developer` and its OWN response keeps `nextTool` absent + "resumes
  automatically" (the choke-point name-guard prevents self-dismiss) while the
  projected `build_attention_queue(lifecycles, [],
  AnalyticalInputs(drift_snapshots=[], setup_progress=[]))` holds exactly one
  `awaiting-developer` item;
  then an arbitrary next call (`ping_payload()`) auto-resumes the lifecycle to
  `running` and that attention item disappears.

### Conventions

`sys.path.insert(0, mcp/src)` before package imports (the suite idiom). `_state`
builds a `LifecycleState` (`fleeting = enclosure is None`); `_contract` builds a
fully-populated `WorktreeContract` over a tmp `Path` with keyword `overrides`
for the sub-state fields each gate case needs. `# type: ignore` annotates the
deliberately-loose `state`/`phase` literals and `**base` splat. Edge tests use a
`tempfile.TemporaryDirectory` instance plus `addCleanup`; pure tests use the
`with tempfile.TemporaryDirectory()` form.

### Invariants And Boundaries

- The pure tests must NOT touch disk for the contract sub-state cases — they pass
  a constructed `WorktreeContract`, so the gate overlay is asserted in isolation
  from contract I/O.
- The edge tests assert the no-raise contract: every degraded path
  (missing/torn contract, no lifecycle) returns a value (`None` or a hint), never
  an exception — mirroring `next_step_for`'s blanket containment. Since 260731-EFA-L4 the same
  rule is asserted one level up for the *banner*: a raising staleness probe yields no key, not a
  broken response.
- Both engines are read by attribute (`step.nextArgs`), because both return `NextStep | None`.
  The dict-by-key reads the edge tests used are gone with the dumped-dict attachment they went
  with; only the payload-level assertions still index a dict, and they index the **payload**
  (`payload["nextStep"]["nextArgs"]`, `payload["tokens"]`), not a hint object.
- The advertised `tokens` must be a fixed point over the payload **as served**: everything the
  caller receives is a field of the one model dumped at the choke point, so recounting the emitted
  dict must reproduce the number exactly. Each of the two count tests pairs that equality with a
  strictly-less recount over the payload minus the field under test, so neither can pass by
  coincidence.

### Todos

None.

## Docs References

| Source | Relevance |
| --- | --- |

No relevant documentation found after checking live sources.

## Repo-Internal References

The suite pins `next_step.py` and the collaborators it resolves at the edge plus
the `lifecycle_start` payload it asserts the rundown on.

| Finding | Anchor | Source |
| --- | --- | --- |
| The next-step engine under test. | `next_step_for` | mcp/src/agents_remember/application/next_step.py:260-281 |
| The choke point that attaches `nextStep` to every response. | `_tool_payload` | mcp/src/agents_remember/mcp/tools/base.py:73-75 |
| `lifecycle_start_payload` whose `frontHalfRundown` + `nextStep` are asserted. | `lifecycle_start_payload` | mcp/src/agents_remember/mcp/tools/lifecycle.py:20-21 |
| The ambient lifecycle installed/started/promoted by the edge tests. | `AmbientLifecycle`; `install_ambient` | mcp/src/agents_remember/observer/ambient.py:112-635; mcp/src/agents_remember/observer/ambient.py:669-671 |
| The projected `LifecycleState` the pure tests construct. | `LifecycleState` | mcp/src/agents_remember/observer/lifecycle_state.py:156-179 |
| The `EventStore` backing the ambient under test. | `EventStore` | mcp/src/agents_remember/observer/store.py:103-171 |
| `WorktreeContract` + `write_contract`/`load_contract` used by the gate + edge cases. | `WorktreeContract`; `write_contract`; `load_contract` | mcp/src/agents_remember/worktrees/worktree_contract.py:230-285; mcp/src/agents_remember/worktrees/worktree_contract.py:436-469; mcp/src/agents_remember/worktrees/worktree_contract.py:472-475 |
| The `NextStep` shape the assertions read, and the `nextStep` / `supervisorBanner` fields now declared on both response envelopes. | `NextStep`; `ResponseModel`; `FlexibleResponseEnvelope` | mcp/src/agents_remember/models/base.py:22-38; mcp/src/agents_remember/models/base.py:41-60; mcp/src/agents_remember/models/base.py:69-84 |
| The `lifecycle_guidance` state machine the linear half delegates to. | `lifecycle_guidance` | mcp/src/agents_remember/worktrees/modules/guidance.py:200-210 |
| `count_response_tokens` / `finalize_payload_tokens` — the counter the fixed-point assertions call and the one the choke point runs over the dump. | `count_response_tokens`; `finalize_payload_tokens` | mcp/src/agents_remember/models/tokens.py:208-215; mcp/src/agents_remember/models/tokens.py:232-249 |
| `agent_notifier_staleness_banner` — the probe the degrade test patches, and the store that makes it fire. | `agent_notifier_staleness_banner` | mcp/src/agents_remember/serving/agent_notifier_heartbeat.py:135-151 |
| `PingResponse`, the model the banner-carrying payload is validated against. | `PingResponse` | mcp/src/agents_remember/models/core.py:14-17 |

## Cross-Repo References

No meaningful cross-repo references found.

## Update History

- 2026-08-02T21:08+02:00 — 260731-EFA-L6 W2-B09 curator: repaired 8 citation entries (15 findings); no Tier-3 findings.

- 2026-08-01T09:05+02:00 — 260731-EFA-L4 curator: corrected a claim this card made twice and
  recorded three new tests. **The correction:** the card said `next_step_for` "returns the
  JSON-dumped dict, not a `NextStep`" and that assertions "read the dumped dict by key
  (`step["nextArgs"]`) for `next_step_for`". Both are now false — `next_step_for` is typed
  `NextStep | None` cit:([`next_step_for`], mcp/src/agents_remember/application/next_step.py:260-281) and every edge case in `EdgeAndChokePointTests` reads
  attributes (`step.nextTool`, `step.nextArgs`), because the choke point assigns the hint to the
  declared envelope field `ResponseEnvelope.nextStep` before the single dump rather than writing a
  dict into the payload afterwards (`mcp/tools/base.py` `_attach_lifecycle_tail`). Rewrote both
  passages. **New coverage** in `EdgeAndChokePointTests`:
  cit:([`test_advertised_token_count_covers_the_attached_next_step`], mcp/tests/test_next_step.py:305-317) —
  `payload["tokens"] == count_response_tokens(payload)` and the recount without `nextStep` is
  strictly less, closing the gap where `finalize_payload_tokens` ran before the hint was written
  in; cit:([`test_advertised_token_count_covers_the_agent_notifier_banner`], mcp/tests/test_next_step.py:319-331) — the same pair for
  `supervisorBanner` off a supervisor ticked six hours into the past, plus
  `PingResponse.model_validate(payload)`, which only became possible once the key was declared;
  and cit:([`test_a_raising_staleness_probe_degrades_to_silence`], mcp/tests/test_next_step.py:333-345) — a patched
  `base.agent_notifier_staleness_banner` raising `OSError` yields no key, a still-valid response, and
  an intact token fixed point. Added the matching invariants and three Repo-Internal rows
  (`models/tokens.py`, `serving/supervisor_heartbeat.py`, `models/core.py`). Every other assertion,
  test name and hint expectation in this card was re-read against the 389-line source and is
  unchanged. Verification metadata pinned until closeout stamps the L4 commit.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2: both construction shapes this card spelled out for
  `EdgeAndChokePointTests` moved behind parameter objects, so the body was corrected.
  `AmbientLifecycle` no longer takes `heartbeat_seconds=3600` directly — it is now
  `timing=AmbientTiming(heartbeat_seconds=3600)` — and `build_attention_queue`'s two trailing list
  arguments collapsed into one `AnalyticalInputs(drift_snapshots=…, setup_progress=…)`, which the
  auto-dismiss bullet now names. Every test name, hint assertion, gate-await path and the
  NOTIFY-AND-CONTINUE contract itself are unchanged.
- 2026-06-27T22:00+02:00 — Task 28 (NOTIFY-AND-CONTINUE turn end): the ACTIVE-hint assertions were repointed off `lifecycle_gate` onto `lifecycle_turn_end_notification` — `test_front_half_generic_points_back_to_the_rundown`, the renamed `test_decide_points_to_the_turn_end_notification`, the renamed `_gate_after` overlays (`test_closeout_preview_hints_the_turn_end_until_approved`/`test_integrate_dry_run_hints_the_turn_end`/`test_finalize_dry_run_hints_the_turn_end`), the edge dry-run/torn-contract cases, and the `lifecycle_start` choke-point rundown assertion. Added `test_awaiting_developer_hints_the_stop` (`nextTool=None`, "resumes automatically") and the end-to-end `test_turn_end_notification_does_not_self_dismiss_then_next_call_resumes` (the notification keeps its own response on `awaiting-developer`; the next call auto-resumes). The parked `blocked`-gate await/resume tests are unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T20:16+02:00 — Added two gate-await tests: `test_blocked_at_a_gate_awaits_the_decision` (pure — a `blocked` state in both `close` and `build` phases yields `_AWAIT_GATE`/`lifecycle_resume`) and `test_next_step_for_blocked_gate_awaits_resume` (edge — the live `amb.start()` + `amb.block(...)` seam returns the resume hint on the `lifecycle_gate` response). Both pin the blocked-state branch added to `compute_next_step`.
- 2026-06-27T18:43+02:00 — Added file-level onboarding for the new task-27 test suite covering the `compute_next_step` state machine (front-half/decide pointers, linear guidance delegation, the closeout/integrate/finalize gate overlays, `_from_guidance`, and `lifecycle_end` loop-back), the exception-contained `next_step_for` edge (missing/torn-contract degradation, dry-run windows), and the `_tool_payload`/`lifecycle_start` rundown choke point. Verification metadata pinned until closeout stamps the task-27 code commit.

