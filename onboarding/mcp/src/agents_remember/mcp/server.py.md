# mcp/src/agents_remember/mcp/server.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/mcp/server.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-10T15:07+02:00 |
| lastVerifiedCommitHash | `fdff55f2921d7aaa8ba240c11087d02c15a170d7` |
| lastVerifiedCommitDate | 2026-07-10T15:53:23+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`server.py` wires the stdio FastMCP server and registers the model-visible
Agents Remember tools. L11 registers `task_reopen` beside `task_doc`: reopen a
completed leaf task under its exact leaf id (state reset; worktree recreation stays
with `worktree_start`).
L9 registers `attach_terminal_session_to_leaf(session_id, leaf_key)` after `read_ar_files`. This is the
agent-facing hosted chat reassignment path: it forwards to `attach_terminal_session_to_leaf_payload`,
reuses the dashboard terminal catalog's role-scoped leaf uniqueness rules, and returns
`attached`/`leaf-taken`/`unknown-session` without spawning a session or requiring a worktree enclosure.
L2 registers `spawn_agent_session(harness?, leaf_key?, context?, submit, label?, model?, effort?, env?,
launch_args?, prompt_keywords?, session_commands?, level?, spawned_by_session?,
spawned_by_lifecycle?, kind)` right after attach: the agent-facing **dispatch**
path that CREATES a role-configured, leaf-attached, context-primed hosted session by composing the
existing serving primitives (opener + leaf claim + echo-confirmed paste), forwarding to
`spawn_agent_session_payload`. Since 260707-HFX2-L10 ordinary callers do not choose spend controls
on this transport surface: non-null legacy `harness`/`model`/`effort`, direct free-form
launch/session fields, `env.AR_SPAWN_MODEL`/`env.AR_SPAWN_EFFORT`, and maintained
harness-native spend/endpoint env keys refuse with `spend-override-unsupported` before spawning.
The docstring now documents the settings-only chain: `level` (leaf|master|portfolio, default leaf)
selects the `rolesPerLevel` settings rung; model/effort/free-form values come from agentic settings
only, are applied onto the harness argv per-harness, and are validated pre-spawn
(`effort-invalid`/`model-invalid`/`level-invalid`; claude's session-level `ultracode` still becomes
the first post-launch `/effort` paste). If role settings do not choose a harness, dispatch falls
through to repo-local/global `orchestration.spawn.harness`, then the detected registry default.

## Code Commentary

### 260707-HFX2-L17 Public Attach Signature

`attach_terminal_session_to_leaf` now exposes optional `role` and forwards it to the payload
builder. Omitting it is valid only when spawn provenance or a previously typed binding can supply
identity; hand-opened untyped harnesses receive `role-required`. The tool remains enclosure-free
and moves one existing session atomically.

### Logic

**260707-HFX2-L15 public spawn contract.** `spawn_agent_session` exposes
`replacement_for_leaf` for a deliberately unbound replacement seat and describes the brief as an
id-bearing, harness-log-confirmed input. Model/effort remain settings-owned launch/session
provenance; the replacement leaf is a chain-credit discriminator, not a second leaf claim.

`create_server()` first calls `install_compact_content()` (idempotent) so the
JSON text mirror of every tool result is emitted without FastMCP's hardcoded
indentation, then installs the process-singleton ambient lifecycle
(`install_ambient(AmbientLifecycle(EventStore(observer_root(config))))`, slice 2b;
the store root resolves through the shared `observer.observer_root`, slice 3a) so
the `_tool_payload` choke point can tag tool calls, then builds the
FastMCP instance and registers typed tool functions that delegate to payload
builders. The current public surface includes context, drift, route index,
memory init, skill install, provider status, provider diagnostics, provider
watcher, GrepAI, CodeGraphContext, worktree, memory baseline/carryover, benchmark,
the public lifecycle signals (`lifecycle_start`, `lifecycle_resume`,
`lifecycle_turn_end_notification`, `lifecycle_end`, `switch_lifecycle`,
`lifecycle_phase`), the slice-3c `task_doc` authoring tool,
and the lifecycle gate surface. Task 25 registers `lifecycle_gate` as the single
agent-facing gate junction: it creates the typed durable gate, blocks the active
lifecycle with the developer-facing ask, and waits for a developer decision or gate-specific inbox response in one call,
and forwards the optional `required_decision` list to the payload layer.
`gate_decide` and `gate_list` remain public control-plane tools; `gate_decide`
hardcodes `decided_by="model"`/`decided_via="cli"` so the agent cannot
self-attribute a developer decision. L4 adds a trusted orchestration path to
that registration: when the optional `deciding_role` argument is supplied, the
payload is decided via `orchestration`, derives `decidedBy` from the active
lifecycle/session, and is checked against the configured gate policy before any
gate snapshot is appended. The retired split helpers
`lifecycle_block`, `gate_create`, `gate_wait`, and `gate_response_wait` are no
longer registered on the FastMCP surface; their payload builders remain
lower-level compatibility internals. The
former `direct_closeout_preview` / `direct_closeout_apply` registrations were
removed (issue #62): closeout is worktree-only. Slice 2c adds an `on_unsaved`
argument to the `switch_lifecycle` and `worktree_attach` registrations (the
save-gate decision `save`/`discard`); registration/forwarding only.

Task 10/L3 adds the inbox tools:
`operator_inbox_post(ask, response, lifecycle_id?, agent_id?, recipient_role?,
message_kind?, artifact_path?, deliver_to_hosted?)`,
`operator_inbox_poll(lifecycle_id?, agent_id?, recipient_role?)`, and
`operator_inbox_consume(entry_id)`. The server registers them after the gate
tools and forwards to `operator_inbox_*_payload` builders. MCP calls are
attributed to `model` / `cli`; trusted dashboard code can call the payload
builder directly with developer/dashboard attribution when the frontend response
path lands. L3 also registers `orchestration_nudge_manager(...)`, the public
manager-nudge helper that records the nudge event and queues a manager inbox
message.

Task 25 supersedes the former public wait helper choreography. Agents call
`lifecycle_gate` once at the gate junction; dashboard decisions and Chat/inbox
responses still use the existing control-plane stores behind that unified public
entrypoint. Returned inbox entries remain explicit-consume through
`operator_inbox_consume`, and that consume path removes the throwaway pending
inbox record.

Task 28 registers `lifecycle_turn_end_notification(summary)` as the public
**NOTIFY-AND-CONTINUE** turn-end tool, between the `lifecycle_resume` and
`lifecycle_end` registrations. It forwards the single `summary` to
`lifecycle_turn_end_notification_payload`; its docstring states the semantics —
notify the developer the turn is complete and stop, with no wait and no gate, the
next AR tool call next turn resuming the lifecycle automatically (the
`_tool_payload` choke point auto-dismisses the `awaiting-developer` state). This
is now the **active** turn-end path — the next-step hint engine repoints its
closeout/decide hints at it. The `lifecycle_gate` + `operator_inbox_*` junction
stays registered and the durable-gate stack remains valid, but it is **parked**:
no longer hinted as the normal turn-end choreography.

260703 L2 adds the boot-time dashboard supervision seam to `main()`: between
`load_config` and `run_server` it calls `maybe_autostart_dashboard(config)`
(from `serving/daemon.py`) — a no-op unless the trusted settings set
`dashboard.autoStart`, otherwise a daemon thread ensures the detached dashboard
daemon (adopt healthy / spawn absent / restart on version mismatch). The hook is
total and threaded so it can never delay or break the stdio handshake, and its
only output goes to stderr (stdout is the MCP protocol).

Dashboard task 14 registers `lifecycle_finalize_task`. The server signature
accepts a coordination-contained contract path, optional leaf task document,
optional parent/master document plus subtask number, `dry_run`, and
`teardown_providers`, then forwards to `lifecycle_finalize_task_payload`. Its
docstring states the terminal semantics: prove one parent-child branch edge,
run or verify cleanup, update task docs when paths are supplied, require PR
flows to merge and pull locally first, and keep squash equivalence out of the
default path.

The registered `memory_quality_check` tool accepts a repo id plus optional
check names/detail limits and forwards them to the payload/controller layer. It
is the full closeout quality gate; task-start guidance continues to use
`drift_check` for the maintenance worklist.

The public CGC provider surface is typed at registration time. The server
registers `cgc_symbol_search`, `cgc_callers`, `cgc_callees`,
`cgc_dependencies`, `cgc_complexity`, and `cgc_visualize` instead of a generic
`cgc_query` endpoint. All CGC and GrepAI query tools now accept an optional
`worktree` parameter forwarded to the payload layer, which routes to a
worktree's isolated provider stack.

The public GrepAI provider surface is typed at registration time as well.
`grepai_search` registers `repo_ids`, `all_repos`, `limit`, and
`output_format` around the required query, while `grepai_trace` registers
`trace_action`, `symbol`, optional repo scoping, optional graph depth, and
output format. The server only forwards these fields to the payload layer.

The `provider_watchers` docstring now describes `restart` (stop then start,
indexes preserved — use to wake a stale watcher) and `invalidate-indexes`
(DELETE and rebuild every index from scratch: full re-embed + full graph
re-index, slow and CPU-heavy) as distinct actions. The former `refresh` action
is no longer listed; it is rejected at the controller with guidance.

`worktree_cleanup` now accepts `teardown_providers` (default `true`), which
reclaims the worktree's isolated provider stack (containers, networks,
provider-runtime tree) before removing worktrees and branches.

`worktree_abandon` is newly registered. It discards a worktree-backed task
without integration: reclaims its isolated provider stack, removes worktrees,
deletes task branches, and removes the group dir. Without `force` it refuses
dirty worktrees and unmerged branches (reporting them); `force=true` discards
with `git worktree remove --force` / `git branch -D`.

`lifecycle_finalize_task` is the terminal worktree lifecycle tool. It must be
previewed with `dry_run=true` before real cleanup/finalization because the real
call may run cleanup and write task documents.

`runtime_install` registers the reconcile flags `dry_run` (act-by-default
`False`), `include_benchmarks`, `install_provider_deps` (default `True`), and
`no_cache` (default `False`). Its operator text now distinguishes preserved user
data (`memory-repos/`, `providers/data/`) from managed scaffold, and explains
that `install_provider_deps=true` may refresh `providers/runners/` after
stopping watchers so containers rebind cleanly, then starts/rechecks watchers
without rebuilding indexes. `no_cache=true` forces a from-scratch provider image
rebuild that bypasses the skip-if-tag-exists shortcut. Registered tool functions
carry human-facing descriptions (docstrings) surfaced to the harness's tool
list.

`codex_benchmark_run` exposes an optional `codex_sandbox` argument whose
registered default is `CODEX_BENCHMARK_SANDBOX` (imported from
`agents_remember.benchmarks.runner`), which now resolves to Codex's own
`default` sandbox rather than `danger-full-access`. Callers must opt into
`danger-full-access` explicitly (trusted local runs only). The server only
forwards the value; the runner validates it against its allowlist and maps
`default` to an omitted `--sandbox` CLI argument. A real benchmark run is also
refused unless the MCP settings enable benchmarks (`benchmarksEnabled`), and
benchmark tools stay `dry_run=True` so a run is never implicit.

`provider_diagnostics` is registered as the explicit detail tool for raw
provider state, keeping `context_packet` and `provider_status` focused on
compact readiness summaries.

`context_packet` registers `include_freshness` (issue #54, default `false`):
its docstring tells callers the flag fetches remote-tracking refs and reports
ahead/behind for the code and memory checkouts plus whether the ledger maps
code HEAD — the lifecycle-start staleness checkpoint.

`worktree_start` registers `stale_base_choice` (issue #54): its docstring
documents the stale-base preflight (refuses behind/diverged source branches),
the `fast-forward` / `proceed-stale` recoveries, and the auto-created memory
source branch templated from the code source branch name.

`worktree_sync` is newly registered (issue #54 sub-task D): the mid-task base
sync taking `contract_path`, optional `memory_sync_choice`
(`merge-memory`/`skip-memory`), and `dry_run`; its docstring documents the
atomic pair advance, the mid-cycle carryover-first block, and the
sync-early-before-memories doctrine. `worktree_status`'s freshness block
recommends it when recorded bases fall behind local source tips.

Registered tools follow an **act-by-default** `dry_run` contract: effectful
tools and the read-only `cgc_*`/`grepai_*` query tools register `dry_run=False`,
so a plain call does the work (queries return results; `dry_run=true` returns
the planned provider command without executing it). The two `*_closeout_apply`
tools keep `dry_run=False` paired with explicit `*_preview` tools, and the two
`codex_benchmark_*` tools are the only `dry_run=True` defaults — a real
benchmark run clones repos and executes Codex agents, so it stays preview-first.

`read_ar_files` is registered (slice 07): the read-only batch paired
source+onboarding read (≤5 repo-relative paths) forwarding to
`read_ar_files_payload`. Its docstring now states the **research-phase read**
doctrine (S4): in a managed repo this is the read for the research phase (the
lifecycle up to the build decision — the 260703-L10 sweep retired the
pre-convergence "build/job" compound from this docstring) — use it instead of a
native read so each
file comes paired with its onboarding plus the repository and governing route
overviews; native read is reserved as the **edit precondition** once building
begins.

`task_doc` is registered (slice 3c): the JSON-primary task-document authoring tool
taking `repo_id`, `operation`
(`create`/`replace`/`set_status`/`set_step`/`set_subtask`/`remove_subtask`/`set_section`/
`append_decision`/`set_field`/`get`), optional `task_name`/`contract_path`/`slug`, and the
`fields`/`step`/`decision`/`subtask`/`section` payloads. It forwards to
`task_doc_payload`; the JSON is the source of truth and `task.md` is a generated render
(mutating except `operation='get'`). `replace` takes a full replacement document in `fields`,
validates it through the same schema path, and rewrites the existing JSON+markdown without
allowing the replacement to move to a different task-document path. `kind:"master"` series wrappers use the
`subtask`/`section` payloads (`set_subtask`/`remove_subtask`/`set_section`); `remove_subtask` drops a
sub-task row and deletes its leaf doc (json+md) unless `subtask.keep_file`; `set_step` is leaf-only. `dry_run`
(act-by-default `False`, R5) builds + validates and returns `rendered`/`diff`/`wouldLose` **without**
writing — the preview before adopting a hand `.md`.

260707-HFX-L8 registers two seat-lifecycle tools right after `spawn_agent_session`:
`session_retire(actor_session_id, session_id, reason="manual retire")` forwards to
`session_retire_payload`. Its docstring is the model-visible statement of the authority policy —
owner-never-self-retires; a manager may retire only worker/reviewer seats of its OWN master; the
orchestrator may retire any seat, including a completed manager — and the full status vocabulary
(`retired`/`already-retired`/`unknown-session`/`unknown-actor`/`retire-refused`). `session_rename(
session_id, label)` forwards to `session_rename_payload`; its docstring states rename is identity
text only (the seat's spawned role never changes, L6 role-seat immutability) and that the FIRST
rename freezes the original spawn-time label into provenance. Both are registration/forwarding
only — behavior lives in the payload builders (`mcp/tools/terminal.py`).

### Invariants And Boundaries

- Server functions should perform registration and argument forwarding only.
- Tool behavior and safety checks belong in payload builders/controllers.
- `install_compact_content()` must run before tools are exercised; keep the call
  at the top of `create_server()`. It only affects text-mirror serialization, not
  `structuredContent` or tool behavior.
- `install_ambient(...)` runs once per `create_server()` (one ambient lifecycle
  per server process); the `lifecycle_*` tools and the `_tool_payload` emission
  hook read that singleton. Keep the install near the top, before tools run.
- Do not add a raw shell or arbitrary command tool to this server.
- Do not collapse GrepAI back into free-form query/native argument forwarding;
  the registration should mirror the supported MCP contract.
- Do not turn benchmark sandbox selection into a generic Codex argument surface.
- Keep detailed provider troubleshooting behind `provider_diagnostics`; do not
  hide raw provider internals in `context_packet`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Payload builders are defined in the `mcp/tools/` package (split by domain behind a facade `__init__.py`). | [tools/](agents-remember/mcp/src/agents_remember/mcp/tools) |
| Provider diagnostics payloads are modeled separately from compact provider summaries. | [providers.py](agents-remember/mcp/src/agents_remember/models/providers.py) |
| The config loader rejects coordinator `system/settings.json` as MCP authority. | [config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |
| The shared observer store-root resolver used to install the ambient. | [observer/paths.py](agents-remember/mcp/src/agents_remember/observer/paths.py) |
| The compact-content shim installed at server creation minifies tool-result text. | [compact_content.py](agents-remember/mcp/src/agents_remember/mcp/compact_content.py) |
| The `runtime_install` tool docstring names preserved user data, managed provider scaffold replacement, watcher rebind behavior, and non-index-rebuilding post-install watcher checks. | [server.py](agents-remember/mcp/src/agents_remember/mcp/server.py) |
| The inbox tools are registered after the gate tools with fixed model/cli attribution. | [server.py](agents-remember/mcp/src/agents_remember/mcp/server.py) |
| Gate delegation policy is parsed from trusted settings and enforced in payload builders. | [config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) and [tools/gates.py](agents-remember/mcp/src/agents_remember/mcp/tools/gates.py) |
| `session_retire`/`session_rename` forward to the payload builders that implement the authority check and catalog mechanics. | [tools/terminal.py](agents-remember/mcp/src/agents_remember/mcp/tools/terminal.py) |

## Series-Contract Notes

FastMCP registrations expose `parent_task` and `leaf_id` on `resolve_context`, `worktree_start`, `worktree_attach`, and `worktree_status`, matching the controller and source API signatures.

As of cycle 5 the lifecycle_gate registration exposes wait (default true) with the raise-and-continue contract documented in the docstring; cycle 6 makes both gate docstrings match the payload layer exactly — `lifecycle_gate` says wait=false is reserved for delegated seam kinds (any other kind blocks), and `gate_list` says a missing lifecycle_id defaults to the ACTIVE (ambient) lifecycle with the workspace log as the no-ambient fallback; cycle 7 extends the `lifecycle_gate` docstring with the new wait=false requirement that `enclosure=<master task name>` be supplied (the address integration enforcement matches the gate by), keeping the registration truthful about the payload layer's refusal.

## Update History

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: widened the public attach tool with role-aware binding
  while preserving provenance-defaulted callers and explicit refusal for untyped hand-opened seats.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: added the public `replacement_for_leaf` argument and
  updated the tool contract from pane/capture confirmation to unique-id harness-log confirmation.
  Verification metadata remains pinned until closeout stamps the eventual L15 code commit.

- 2026-07-09T12:04+02:00 — 260707-HFX2-L10 (spawn settings authority): `spawn_agent_session`
  registration retains legacy spend parameters only as compatibility tripwires. The docstring now
  states that ordinary callers declare role/level and that harness/model/effort, direct
  launch/session controls, namespaced spawn model/effort env, and maintained harness-native
  spend/endpoint env keys return `spend-override-unsupported` before spawning. Verification metadata
  pinned until closeout stamps the 260707-HFX2-L10 commit.

- 2026-07-08T02:43+02:00 — 260707-HFX-L8 (seat lifecycle: retirement + live identity): registered
  `session_retire(actor_session_id, session_id, reason)` and `session_rename(session_id, label)`
  right after `spawn_agent_session`, forwarding to `session_retire_payload`/`session_rename_payload`.
  Docstrings state the retire authority policy and status vocabulary, and the rename identity-only/
  role-immutability contract. Registration/forwarding only. Verification metadata pinned until
  closeout stamps the HFX-L8 commit.
- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application): `spawn_agent_session` gained the
  free-form escape-hatch parameters (`launch_args`, `prompt_keywords`, `session_commands`) and the
  dispatch `level` parameter; its docstring now documents the per-harness knob application, the
  pre-spawn `effort-invalid`/`model-invalid`/`level-invalid` refusals, and the rolesPerLevel
  resolution chain. Registration forwarding only — behavior lives in the payload builder.
  Verification metadata pinned until closeout stamps the L16 commit.

- 2026-07-06T22:42+02:00 — 260703-L13 (settings unification): `spawn_agent_session.harness`
  became optional (`str | None = None`) and the tool docstring documents the explicit >
  repo-local > global > detection-gated resolution chain. Registration order and every other
  tool unchanged. Verification metadata pinned until closeout stamps the L13 commit.

- 2026-07-06T13:35+02:00 — 260703-L10 round 2 (L10R-2): the `read_ar_files` docstring's pre-convergence "build/job decision" compound became "build decision" (the l-01 vocabulary; the flipped session-start directive says the same). Docstring text only — no signature, payload, or registration change. Verification metadata pinned until closeout stamps the L10 commit.
- 2026-07-05T19:55+02:00 - L8 builder cycle 7: lifecycle_gate docstring now names the wait=false enclosure requirement (AR4-1a ride-along). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T19:10+02:00 - L8 builder cycle 6: lifecycle_gate/gate_list docstrings aligned with the seam-kind wait=false restriction and the ambient-defaulting gate_list (AR3-3/AR3-5). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): lifecycle_gate wait passthrough registered. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-04T12:32+02:00 — 260703-L4: `lifecycle_gate`/`gate_decide`
  registrations forward gate evidence refs, and `gate_decide(deciding_role=...)`
  uses the server-enforced orchestration decision path instead of model/cli
  attribution. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-04T12:31+02:00 - L3: expanded the operator inbox tool signatures for
  role/message/delivery metadata and registered `orchestration_nudge_manager`.
  Verification metadata pinned until closeout stamps the L3 commit.
- 2026-07-04T11:10+02:00 — L2 (agent-orchestration spawn-dispatch): registered
  `spawn_agent_session(harness, leaf_key?, context?, submit, label?, model?, effort?, env?,
  spawned_by_session?, spawned_by_lifecycle?, kind)` after `attach_terminal_session_to_leaf`,
  forwarding to `spawn_agent_session_payload`. Its docstring states it composes the existing session
  primitives (serving opener + optional leaf attach with server-arbitrated `leaf-taken` + echo-confirmed
  context paste with optional submit), injects the model/effort/env knobs at spawn, and records
  spawned-by provenance. Registration/forwarding only. Verification metadata pinned until closeout stamps
  the L2 commit. (Distinct from the 260703-L2 daemon-supervision entry below.)
- 2026-07-03T11:45+02:00 — 260703 L2: `main()` calls `maybe_autostart_dashboard(config)` between
  `load_config` and `run_server` — threaded, total, stderr-only dashboard daemon supervision
  gated by the `dashboard.autoStart` settings key. Verification metadata pinned until closeout
  stamps the code commit.
- 2026-07-03T00:30+02:00 — L11 registers the `task_reopen` tool (task-domain reset of a completed leaf; dry_run preview; delegates to task_reopen_payload).
- 2026-07-02T17:04+02:00 — L9: registered `attach_terminal_session_to_leaf(session_id, leaf_key)` as the
  agent-facing path for moving an existing hosted terminal/chat session between durable leaves. Verification
  metadata pinned until closeout stamps the L9 commit.
- 2026-06-29T22:57+02:00 — CRUD completion (L2): the `task_doc` registration docstring now lists the
  `remove_subtask` master op (`subtask={number, keep_file?}` — drops the row and deletes the leaf doc
  unless `keep_file`). Registration/forwarding only; no schema change. Verification metadata pinned
  until closeout stamps the code commit.
- 2026-06-27T22:00+02:00 — Task 28 (NOTIFY-AND-CONTINUE turn end): registered the
  public `lifecycle_turn_end_notification(summary)` tool between `lifecycle_resume`
  and `lifecycle_end`, forwarding to `lifecycle_turn_end_notification_payload`
  (notify + stop, no wait/gate; the next AR tool call auto-resumes). Added it to
  the public lifecycle-signals list and a Code Commentary paragraph noting it is
  now the active turn-end path while the `lifecycle_gate`/`operator_inbox_*`
  junction stays registered but parked (un-hinted). Verification metadata pinned
  until closeout stamps the code commit.
- 2026-06-26T18:43+02:00 — Regression fix: refreshed `lifecycle_gate`
  registration prose so it describes the public call as waiting for a developer
  decision or gate-specific inbox response, not returning on unrelated lifecycle
  inbox rows.
- 2026-06-26T17:12+02:00 — Regression fix: refreshed `lifecycle_gate`
  registration prose so the server sidecar records the public call as
  create+block+bounded-wait, not wait-state initialization only.
- 2026-06-26T16:15+02:00 — Task 25 closeout verification: refreshed the server
  registration detail for `lifecycle_gate(required_decision=...)` and the advertised
  `task_doc replace` operation; verified against code commit `2017434`.
- 2026-06-26T14:16+02:00 — Task 25: registered `lifecycle_gate` as the public gate junction and removed `lifecycle_block`, `gate_create`, `gate_wait`, and `gate_response_wait` from the advertised FastMCP surface; the split builders remain internal compatibility payloads.
- 2026-06-25T13:20+02:00 — Task 23/24: `gate_response_wait` now documents one normal five-minute wait window and physical deletion of consumed throwaway inbox entries.
- 2026-06-25T07:17+02:00 — Task 19: registered `gate_response_wait`, the bounded combined gate/inbox wait helper for dashboard gate Chat responses, and documented that returned inbox entries remain explicit-consume. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: MCP tool wrappers now expose `parent_task` and `leaf_id` on context and worktree start/attach/status tools, passing them through to the controller layer. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T22:50+02:00 — Dashboard task 14: registered `lifecycle_finalize_task`, forwarding to the new payload builder with contract/task-doc paths, dry-run, and provider-teardown controls. Verification metadata pinned until closeout stamps the source commit.

- 2026-06-23T13:44+02:00 — Task 10 backend inbox: registered `operator_inbox_post`, `operator_inbox_poll`, and `operator_inbox_consume`, forwarding to the new payload builders with MCP-route attribution fixed to model/cli. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-23T07:25+02:00 — slice 09 (gate-signal adoption, S2): the `gate_create` tool docstring's `kind` list now includes the three new `GateKind` literals (`plan-approval`, `worktree-intent`, `push-approval`) — the full l-01 gate spine — plus the note that `closeout-approval` is the commit gate (there is no separate `commit-approval`). Docstring text only (registration/forwarding unchanged). Refreshed the gate-tools line in Code Commentary. Verification metadata pinned until closeout stamps the slice-09 code commit.
- 2026-06-23T00:53+02:00 — Slice 07 (S4): the `read_ar_files` registration's docstring now teaches the **research-phase read** doctrine — in a managed repo it is the read for the research phase (up to the build/job decision), used instead of native read so each file is paired with its onboarding plus the repository/route overviews; native read is the edit precondition once building begins. Registration/forwarding only (docstring text). Verification metadata pinned until closeout stamps the slice-07 code commit.
- 2026-06-19T07:23 — Slice 3c reopened (R5, dry-run/preview): the `task_doc` registration gained a `dry_run` argument (act-by-default `False`; `true` returns `rendered`/`diff`/`wouldLose` without writing) + a docstring line. Registration/forwarding only. Verification metadata pinned until closeout stamps the R5 code commit.
- 2026-06-18T01:05+02:00 — Task 6 slice 6a: registered the four control-plane gate tools (`gate_create`/`gate_decide`/`gate_wait`/`gate_list`), forwarding to the `gates` payload builders; `gate_decide` is registered with fixed `model`/`cli` attribution. Registration/forwarding only. Verification metadata pinned until closeout stamps the 6a code commit.
- 2026-06-14T00:16 — Slice 3c commit 3: the `task_doc` registration gained `subtask`/`section` arguments and its docstring lists the master ops (`set_subtask`/`set_section`) for `kind:"master"` series wrappers. Registration/forwarding only. Verification metadata pinned until closeout stamps the 3c commit-3 code commit.
- 2026-06-13T22:34 — Slice 3c commit 1: registered the `task_doc` authoring tool (forwarding `operation`/`task_name`/`contract_path`/`slug`/`fields`/`step`/`decision` to `task_doc_payload`). Registration/forwarding only. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
- 2026-06-13T19:30+02:00 — Slice 3a: `create_server()` resolves the observer store root via the shared `observer_root(config)` (`install_ambient(AmbientLifecycle(EventStore(observer_root(config))))`) instead of the inline `coordination_root/"logs"/"observer"` path. Behavior unchanged. Verification metadata pinned until closeout stamps the 3a code commit.
- 2026-06-13T18:45+02:00 — Slice 2c: `switch_lifecycle` and `worktree_attach` registrations gained an `on_unsaved` argument (the save-gate decision), forwarded to their payload builders. Verification metadata pinned until closeout stamps the 2c code commit.
- 2026-06-13T16:41+02:00 — Slice 2b: `create_server()` installs the process-singleton ambient lifecycle (`install_ambient(AmbientLifecycle(EventStore(...)))`) and registers the six `lifecycle_*` signal tools. Verification metadata pinned until closeout stamps the 2b code commit.
- 2026-06-11T06:47+02:00 — Unregistered `direct_closeout_preview`/`direct_closeout_apply` and dropped their payload-builder imports (issue #62 worktree-only closeout).
- 2026-06-10T09:56+02:00: Registered `worktree_sync` (contract_path, memory_sync_choice, dry_run) for the issue #54 mid-task base sync.
- 2026-06-10T09:30+02:00: `worktree_start` registers `stale_base_choice` and documents the stale-base preflight + recoveries + memory branch auto-template (issue #54 sub-task B).
- 2026-06-10T08:39+02:00: `context_packet` registers `include_freshness` and documents the fetch + ahead/behind + ledger-mapping report (issue #54).
- 2026-06-10T07:30+02:00 — `worktree_start` registers `retry_provider_setup` and its docstring documents the async contract (returns in seconds; providers `starting` + progressFile; poll worktree_status; seed copy seconds vs seedFallback reindex minutes; retry on failed/stale). `worktree_status` docstring documents the providers poll block and its states (GitHub #53).
- 2026-06-04T22:15+02:00: Updated `runtime_install` operator text to clarify provider runner refresh during `install_provider_deps=true`, watcher rebind/recheck behavior, and index preservation.
- 2026-06-02T04:40+02:00: `skills_install` tool dropped the `layout` parameter after the installer became a single flat copy (U-01-core-skills dissolved). `l-01-session-job-lifecycle` skill series, Sub-task B/S7, mcp 1.1.0.
- 2026-06-02T04:25+02:00: `worktree_start` docstring dropped the retired `heavy-task` workflow_kind (now `light-task`/`chat-task`) after the heavy workflow was retired. `l-01-session-job-lifecycle` skill series, Sub-task B/S6, mcp 1.1.0.
- 2026-06-01T00:00+02:00 — `provider_watchers` docstring updated to name `restart` (index-preserving) and `invalidate-indexes` (destructive rebuild) as distinct actions, replacing `refresh`. All CGC/GrepAI query tools gained `worktree` parameter. `worktree_cleanup` gained `teardown_providers`. `worktree_abandon` newly registered with `force`. Updated Code Commentary Logic section.
- 2026-05-31T12:30+02:00 — Resolved the hardening follow-up: `codex_sandbox`'s registered default is now `CODEX_BENCHMARK_SANDBOX` (Codex's own `default` sandbox, not `danger-full-access`), callers must opt into full access explicitly, and a real run is refused unless MCP settings set `benchmarksEnabled` (1.0.0 review remediation).
- 2026-05-30T21:33+02:00: Documented the 0.9.x registration changes — `runtime_install`'s `no_cache` flag (from-scratch image rebuild) alongside `install_provider_deps`, the human-facing tool descriptions now surfaced to the harness, and the literal `codex_sandbox="danger-full-access"` registered default (noted as a hardening follow-up). Verified against `8927f03`.
- 2026-05-29T20:20+02:00: Recorded the act-by-default `dry_run` contract (effectful + `cgc_*`/`grepai_*` query tools register `dry_run=False`; only `codex_benchmark_*` keeps `dry_run=True`) and refreshed the stale payload-builder reference to the `mcp/tools/` package.
- 2026-05-29T08:53+02:00: Updated after `create_server()` began installing the FastMCP compact-content shim to minify tool-result text mirrors.
- 2026-05-28T19:52+02:00: Updated after registering the dedicated `provider_diagnostics` MCP tool.
- 2026-05-26T23:11+02:00: Refreshed verification metadata after source commit `5ab704a` landed typed GrepAI search and trace registration.
- 2026-05-26T22:54+02:00: Updated after GrepAI search and trace registration gained typed scope, output, and trace-action arguments.
- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` exposed benchmark sandbox options through the MCP server.
- 2026-05-24T08:56+02:00: Updated after `codex_benchmark_run` registered the optional `codex_sandbox` forwarding argument.
- 2026-05-24T02:47+02:00: Updated after registering `memory_quality_check` as the closeout quality gate.
- 2026-05-23T20:42+02:00: Updated CGC registration from generic `cgc_query` to typed CGC tools.
- 2026-05-23T13:09+02:00: Updated for the complete Phase 04 public MCP tool surface.
