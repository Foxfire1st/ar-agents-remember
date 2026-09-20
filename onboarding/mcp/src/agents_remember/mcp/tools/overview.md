# mcp/src/agents_remember/mcp/tools

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                             |
| sourceRoute            | `mcp/src/agents_remember/mcp/tools`            |
| doc_type               | `route-local-overview`                         |
| lastUpdated | 2026-09-18T15:30+02:00 |
| lastVerifiedCommitHash | `fb719f8936d337c4685f2758d4ba3731cd8b7fc5` |
| lastVerifiedCommitDate | 2026-09-20T12:31:16+02:00|
| reviewedWorkingCandidate | candidate `ar/260915-ks-l44-ar`, uncommitted; base `2a96eb883fb081e77a79485530ad7b83ccceff7b` |
| governingOverview      | `../../../../../overview.md`                   |

## Governing Overview

[overview.md](../../../../../overview.md)

## 260915-KS-L41 The Knowledge Payload Builders Bind A Run And Complete A Resolution Pair

This route owns the payload builders every mounted operation family delegates to, and this leaf changed
two of the five knowledge builders. `knowledge_integrity_check_payload` now takes an exact-input selector
and reports the run it actually read. `_ExactInputSelector` is the caller's `runId` and `inputDigest` as
one frozen value with an `as_wire()` echo that distinguishes "the caller named none" (`None`) from a
strategy of silence, and `_run_for_scope` applies it as a **binding** rather than a preference: a run
whose recorded identity or `detection_input_digest` does not match is skipped and the search continues
inside the requested scope, so a request naming inputs nothing was measured over reports no run instead
of the first identity-sorted match. `_runs_in_scope` and `_run_identity` answer the other half of the same
question by naming every run the scope holds — each with its own id, registered route and input digest —
so a caller that received one match can see it was one of several and issue an exact request from the
response it already has. `_report_facts` is the single composition all three non-success answers go
through (no run recorded, nothing matched, a run that could not be read), which is what keeps
`selectedRunId`, `inputDigest` and `inputIdentities` honestly empty exactly when nothing was selected
while `exactInputSelector` still echoes what was asked for; `_condition_report` names the selected run
beside the digest over its exact inputs and echoes the **run's own** `governing_route_id` as the scope
rather than the caller's string. The scope still selects and never borrows another scope's run.

`knowledge_read_payload` gained a `workspace_root` keyword and resolves the context's source-resolution
pair through `_source_resolution` / `_current_code_tree`: a caller-named root is completed with that
root's own current tree, the mount's workspace default is used only when the caller names no repository
*and* a tree can be resolved from it, and a root Git cannot answer for (not a repository, no Git, a
timeout, an answer that is not a tree id) yields neither half rather than a guess. A context carrying one
half is refused by its own model, so this is the change that turns a minimal schema-conformant read from
a raised validation error into a returned view. The other three builders are untouched, and the module's
standing property is unchanged: nothing here decides anything, and every builder still returns the
unresolved state wherever a decision would otherwise be required.

## IAS Frozen Worktree Payload Boundary

Worktree payload builders forward one typed contract-addressed sync intent through the application
layer and preserve its structured recovery guidance. They do not interpret a queue row as operation
state, synthesize legacy journal input, or hide a retained conflict behind a generic failure.
Selecting start/attach flows preserve the same `reconciling` evidence until exact source-pair
admission completes.

Task-document payloads remain independent of queue and activation state. A successful mutation may
cause downstream projection invalidation/rebuild, but no payload builder turns scheduling state into
authoring permission.

**The sync builder's resolution input is one paired value (260915-KS-L40).** `worktree_sync_payload`
takes `resolution: SyncResolutionInput | None` in place of a bare `resolution_action`, so the action and the
authored knowledge decision a `reconcile` call may carry travel together through this route and cannot
disagree here; the registration layer pairs the two published arguments before calling it. The builder is
otherwise unchanged: it still forwards typed arguments to `application.worktree_tools.worktree_sync_tool`
and returns through `base._tool_payload`, and it owns no journal, selector or resolution policy.

## 260915-CAPS-L9 `runtime_install_payload` Takes The Run's Request

`runtime_install_payload(config, request)` now takes one `RuntimeInstallRequest` instead of four
keyword flags. The builder is transport-thin and stays that way: the registered tool constructs the
request, the builder forwards it, and the `write_tool_report` label follows `request.dry_run`. The
change exists so `request.experiment` — the run's own selection input — reaches the application
entry point by construction rather than by a keyword list that can drift, and so the install payload
can report `selectionSource` for the mode it used.

## Purpose

`mcp/tools/` is the pure payload-builder registry for the Agents Remember MCP
server. It was split out of the former single `mcp/tools.py` module (commit
`01f503d`) into one submodule per tool domain, behind a facade `__init__.py`
that preserves the public import surface (L11: `task_reopen_payload` lives in the
task-domain `task_doc.py` submodule, and `PUBLIC_TOOLS` lists `task_reopen` beside
`task_doc`): every `*_payload` builder, the
`PUBLIC_TOOLS`/`RESERVED_TOOLS`/`TRANSPORT` constants, and the `_tool_payload`
re-export remain importable from `agents_remember.mcp.tools`.

## Current Structural Boundary

Agent-facing dispatch, parent/child messaging, retire, rename, and delegated gates enter through
`structural_agent.py` and structural gate builders. Their requests and responses contain real task
documents and roles, never runtime session/lifecycle/inbox/gate identifiers. `terminal.py` retains
exact-id adapters only for internal operator/control-plane composition; it is not a compatibility
public agent surface. The removed `leaf_ref.py` has no successor compatibility shim.

L23 payload builders start/observe/cancel closeout and integration by task contract and operation
kind while retaining operation fingerprints, candidate trees, and worker identities inside the
service plane. Memory payloads also expose the guarded `citation_fix` preview/apply operation so
range repairs use the validated MCP write boundary rather than direct store or file mutation.

## Where Registration Lives Now (260731-EFA-L2)

The `@server.tool()` declarations that used to sit in `mcp/server.py` moved to the new
**`mcp/registration/`** package (twelve family modules + `TOOL_REGISTRARS`). This route is
unchanged in responsibility — it is still the payload-builder registry — but its consumer changed:
`registration/<family>.py` imports the `*_payload` builders from `agents_remember.mcp.tools`, and
`server.py` is process wiring only.

That split is also why the builders here **do** take parameter objects while most tool declarations
retain flat signatures (approved discriminated request schemas are explicit exceptions). FastMCP derives each tool's published JSON schema from the Python signature, so a
model-typed parameter on a declaration would republish the tool as a nested object; a payload
builder has no such constraint. 260731-EFA-L2 armed `PLR0913` and moved these builders onto the
concept objects their application entry points take:

| Builder | Now takes |
| --- | --- |
| `worktree_start_payload` | `TaskIdentity`, `bases: TaskBases`, `execution: StartExecution` |
| `worktree_attach_payload` / `worktree_status_payload` | `task: TaskRef` |
| `worktree_closeout_preview_payload` / `..._apply_payload` | `CloseoutCommitMessages` (+ `CloseoutApproval` on apply) |
| `lifecycle_finalize_task_payload` | `docs: FinalizeTaskDocs` |
| `resolve_context_payload` | `task: TaskRef` |
| `task_doc_payload` | `target: TaskDocTarget`, `edit: TaskDocEdit` |
| `memory_baseline_adopt_payload` | `branches: MemoryBranches` |
| `memory_carryover_plan_payload` / `..._apply_payload` | `selection: CarryoverSelection` (+ `messages: CarryoverCommitMessages`) |
| `codex_benchmark_prepare_payload` / `..._run_payload` | `selection`, `preparation` (+ `run`) |
| the eight `grepai_*`/`cgc_*` builders | `scope: ProviderQueryScope` (+ GrepAI query/repo-scope objects) |
| `dispatch_agent_payload` / structural child/self builders | Structural request DTOs; ambient caller identity is injected by the plane |
| Structural gate builders | Structural gate request DTOs; exact correlation stays internal |
| `message_parent_payload` / `message_child_payload` | Whole-message structural requests whose current occupant is re-resolved |

Behaviour, refusal vocabularies and response shapes are unchanged throughout; only the argument
shape on the application-facing side moved.

## Hot Path Summary

`worktree.py` forwards closeout and direct-landing code/memory messages to the application without a ledger-message parameter. This MCP adapter neither writes a cache commit nor adds a ledger-currentness gate.

## Detailed Route Context

The worktree closeout payload forwards typed corrective catalog dispositions unchanged. Validation and recovery stay in the application/lifecycle owners, not this transport layer.

Payload builders now cover task-addressed operation controls, enclosure adoption, legacy inspect/migrate/archive, and fail-closed cleanup/abandon responses without private ids.

ACPUI-L2/L4 keep `terminal.py` as the settings-owned role dispatch builder while the daemon request
layer owns optional roleless selection. Complete role settings become `ResolvedLaunch`; missing
model/effort refuses before tmux, and complete values travel through the same opener to runner-side
dynamic model-gated validation. Spawn env and response fields preserve provenance, while normalized
model/effort never joins `sessionCommands`. If the selected session id already names a live process
with different launch identity, the opener returns `launch-conflict`; this builder maps it to
`launch-selection-invalid` and stops before expectations, log binding, brief delivery, or respawn.
Settings-defined non-native harnesses retain only their explicitly declared legacy mappings.

The internal terminal builder accepts a runtime occupant plus canonical task document and role for
operator assignment. Structural dispatch composes the same opener internally, then persists an
exact-pinned first brief. Ordinary structural messages persist a document+role address and re-resolve
the current occupant at post and delivery time; replacement therefore does not change the sender's
address.

### Historical Task-27 Through HFX Builder Account

The following retained migration account describes the earlier adapter-owned implementation. Current ownership is stated below; former public terminal/inbox/nudge names here are not in the current advertised set.

The `mcp/registration/` family modules import the advertised `*_payload` builders from
`agents_remember.mcp.tools`; each builder forwards its arguments to its
domain application entry point and validates the result through `base._tool_payload`. Since
task 27 that choke point also attaches the engine-computed `nextStep` hint onto every
active-lifecycle response, computed by
`next_step.py`. **260707-HFX2-L2 (R5)** adds a third thing this same choke point
surfaces on every call: a `supervisorBanner` string when the serving daemon's
supervisor-sweep heartbeat has gone stale (`serving.supervisor_heartbeat
.agent_notifier_staleness_banner`, exception-contained at the call site) — issue #15's
"the watcher must be code AND watched" surfaced at the one place every MCP tool
response already passes through. **260731-EFA-L4 reordered this choke point**: both
attachments are now set on the *validated model* by `_attach_lifecycle_tail` BEFORE the
single `model_dump`, and the ambient emission hook runs LAST, off the finished payload.
The previous order — dump, count tokens, emit, then write the two keys into the dict —
served bytes the advertised `tokens` did not include and recorded that same short count
against the lifecycle. `operator_inbox_post_payload` is also the completion-wake edge:
for `turn-report` and `master-handover`, 260707-HFX2-L13 resolves and addresses the current manager
before creating the row/ack expectation and attempting hosted delivery, while ordinary peer messages
retain explicit addressing. Task 28 makes `lifecycle_turn_end_notification` the active
NOTIFY-AND-CONTINUE turn-end tool: `_tool_payload` auto-dismisses an
`awaiting-developer` lifecycle on the next call (`resume_from_await`, name-guarded
to skip the notification itself), and `next_step.py`'s active hints repoint onto
it — the `lifecycle_gate`/inbox stack stays exported but PARKED (un-hinted). Start
at `base.py` for the shared `_tool_payload` adapter and the re-exported `PUBLIC_TOOLS` tuple (whose
one definition is `models/tools/public_roster.py`), then the
domain submodule that owns the tool. Task 25 makes `lifecycle_gate_payload` the
public agent-facing gate junction; split gate/block/wait builders remain exported
for internal compatibility and tests but are not registered as public MCP tools. L9 adds the
`terminal.py` submodule and public `attach_terminal_session_to_leaf` builder, an agent-facing wrapper over
the dashboard terminal catalog move policy. L2 adds the public `spawn_agent_session` builder to that same
submodule — the agent-facing dispatch tool that composes the shared serving opener + a capture-verified
context paste (260707-HFX-L3: `contextDelivered` only after the pane provably shows the paste; failures ship `deliveryCapture`) to create a role-configured, leaf-attached, context-primed hosted session. HFX2-L10 makes
settings the spend authority for ordinary callers: legacy non-null `harness`/`model`/`effort`,
direct `launch_args`/`prompt_keywords`/`session_commands`, `AR_SPAWN_MODEL`/`AR_SPAWN_EFFORT`, and
maintained harness-native spend/endpoint env keys refuse with `spend-override-unsupported` before
leaf resolution, host spawn, catalog writes, expectation rows, or paste delivery. Since 260703-L16
the builder is the full settings-rung knob resolution + application seam: `_resolve_harness_dispatch`
folds `resolved_role_knobs(AR_SPAWN_ROLE, level)` (`rolesPerLevel` over flat `roles`; the `level`
parameter leaf|master|portfolio with recorded provenance), then falls through to repo-local/global
`orchestration.spawn.harness` and the first detected registry harness, resolves ids against the
EFFECTIVE registry (`orchestration.harnesses`; unknown-everywhere ids refuse naming the
`docs/reference/harnesses.md` manual), validates model/effort per-harness BEFORE spawning
(`model-invalid`/`effort-invalid`/`level-invalid`; claude's session-vocabulary `ultracode` becomes
the first post-launch `/effort` paste), and delivers the settings-owned free-form escape hatch
(`launchArgs` verbatim argv, `sessionCommands` pasted+submitted before the brief,
`promptKeywords` prepended to the brief) — never validated, recorded in spawn provenance and echoed
on the payload.
260707-HFX-L4 adds qualified leaf-ref validation at the terminal write boundary: attach/spawn accept
canonical qualified ids, doc ids, and unambiguous legacy stems/slugs, persist canonical qualified
`repo/master/doc-id` catalog keys, and return strict `leaf-ref-not-found` / `leaf-ref-ambiguous`
refusals with the expected `<repo>/<master-folder>/<doc-id>` form before any mutation.
L3 adds `orchestration.py` and public `orchestration_nudge_manager`, a rate-limited manager nudge helper
that records an orchestration nudge event and enqueues a manager-addressed inbox message.
**260707-HFX-L8** adds two public builders to `terminal.py` (issues #12/#4): `session_retire_payload`
(actor+target lookup, an idempotent `already-retired` fast path on an already-terminated target BEFORE
any authority check, `serving.retire_policy.check_retire_authority` enforcement — owner-never-self-
retires, manager scoped to its own master's worker/reviewer seats, orchestrator portfolio-wide —
`retire-refused` naming the exact clause on refusal, else `serving.retire.retire_entry` + a
`seat_events.log_retire_event`) and `session_rename_payload` (identity text only, `catalog.set_label` +
`seat_events.log_rename_event`, `spawn_role` never touched). `actor_session_id` is self-declared by the
caller (mirrors `spawn_agent_session`'s `spawned_by_session` pattern) — there is no ambient "who is
calling me" session-id resolution anywhere in this codebase.

## Current Response And Adapter Ownership

`base.py` **re-exports** the advertised tuple — its one definition moved to the zero-import `models`
leaf `models/tools/public_roster.py` at 260831-LOCR-L32, and `base.py` imports it at L14 and declares
it in `__all__` at L19, so the same **66**-name object stays importable from this package (62 at the
move, 63 from 260831-LOCR-L37, 66 since 260915-CAPS-L4). `base.py` also
forwards `_tool_payload` to `application/tool_response.py::complete_tool_response`. That application owner attaches bounded task-addressed guidance and notifier banners before `models/tools/tool_response.py::finalize_tool_response` performs its single validation/dump/token pass, then emits the completed call. `application/next_step.py` owns guidance. Gate policy and gate-log reclamation now live in `application/gate_tools.py`; this route's `gates.py` forwards public structural requests and separately retained internal exact-id adapters. `terminal.py`, `operator_inbox.py`, and the nudge helper likewise retain internal adapters; their exports do not advertise tools. `leaf_ref.py` is absent.

| Finding | Anchor | Source |
| --- | --- | --- |
| The MCP adapter delegates completed-response ownership to the application. | `_tool_payload` | mcp/src/agents_remember/mcp/tools/base.py:22-24 |
| The application attaches bounded guidance and records the completed result after finalization. | `complete_tool_response` | mcp/src/agents_remember/application/tool_response.py:84-98 |
| Wire validation and token finalization consume the enriched model in one serialization pass. | `finalize_tool_response` | mcp/src/agents_remember/models/tools/tool_response.py:15-26 |

## Historical EFA/HFX Layout

| Module          | Owns                                                                       |
| --------------- | -------------------------------------------------------------------------- |
| `base.py`       | `TRANSPORT`, `RESERVED_TOOLS` (empty), and `_tool_payload` — the choke point — plus the **re-export** of the exact ordered `PUBLIC_TOOLS` tuple, whose one definition moved to `models/tools/public_roster.py` at 260831-LOCR-L32 (L14 import, L19 `__all__`; the tuple held 62 names at the move, 63 from 260831-LOCR-L37, and **66** since 260915-CAPS-L4). Since 260731-EFA-L4 the choke point's order is: `model_validate` → (in-lifecycle only) `_attach_lifecycle_tail` → ONE `model_dump(mode="json", exclude_none=True)` → `finalize_payload_tokens` → `amb.emit_tool`. `_attach_lifecycle_tail(response, amb, tool_name)` runs the task-28 `awaiting-developer` auto-dismiss (`amb.resume_from_await()` for every tool except `lifecycle_turn_end_notification` — the name guard is mandatory, since the notification itself flows through here in the same call that set the state), then assigns `response.nextStep = next_step_for(...)` and `response.supervisorBanner = _agent_notifier_banner(amb)`. Both are assigned unconditionally, `None` included, because `exclude_none=True` drops them — so a lifecycle-less or live-supervisor response is byte-identical to before. Both remain exception-safe and never raise into the tool path (`_agent_notifier_banner` swallows an unreadable heartbeat file). |
| `next_step.py`  | The lifecycle next-step engine (task 27): pure `compute_next_step` maps the projected lifecycle state to one `NextStep` hint. Front half (no worktree contract yet) is a stable prose pointer back to the one-time `lifecycle_start` rundown (`FRONT_HALF_RUNDOWN`), and HFX-L6 rewrites that role framing around the architect-default developer-facing lifecycle with spawned backend orchestrators and curator closeout seats. Linear half (from `worktree_start`) delegates to `worktrees/modules/guidance.lifecycle_guidance` and overlays a turn-end hint at the gate moments. Task 28 made NOTIFY-AND-CONTINUE the active turn-end model: the `decide`/`_gate_after`/rundown ACTIVE hints now point at `lifecycle_turn_end_notification` (notify + stop, no wait), and a new `awaiting-developer` branch returns a `nextTool=None` stop hint. The `blocked` branch (a raised `lifecycle_gate` → `amb.block()`) still returns the `_AWAIT_GATE` await-developer hint at `lifecycle_resume` — the PARKED gate path, valid but un-hinted. A terminal `lifecycle_end` returns the loop-back hint. Edge `next_step_for` resolves state/contract/guidance and is exception-contained. 260731-EFA-L4: `next_step_for` returns `NextStep \| None` — the MODEL, not a dump of it — because the hint is a declared field of the response envelope and serializing it is the choke point's single `model_dump`; returning a dict here is what made the hint a key written into an already-dumped, already-token-counted payload. `_guidance_for` correspondingly widens `lifecycle_guidance`'s TypedDict with `dict(...)`: this hint layer reads guidance defensively by key and never re-emits its vocabulary. |
| `core.py`       | ping, server_info, context_packet, runtime_install, resolve_context, skills_install; `server_info` carries the shared boot-resolved serving-build payload; `compact_runtime_install_payload`. |
| `memory.py`     | drift_check, memory_quality_check, route_index_refresh, memory_init, baseline status/adopt, carryover plan/apply; `compact_carryover_payload`. |
| `providers.py`  | provider status/diagnostics/watchers, GrepAI search/trace, CGC query tools; `compact_diagnostics_payload`, `compact_watchers_payload`. |
| `worktree.py`   | worktree start/attach/status/sync/closeout/integrate/checkpoint-landing/cleanup/abandon, including `parent_task`/`leaf_id` forwarding for leaf enclosure lookup. |
| `benchmark.py`  | codex_benchmark_prepare, codex_benchmark_run.                              |
| `lifecycle.py`  | lifecycle signal builders driving the observer ambient lifecycle; `lifecycle_block_payload` is retained for lower-level compatibility. Since task 27 `lifecycle_start_payload` also emits the one-time `frontHalfRundown` (`next_step.py`'s `FRONT_HALF_RUNDOWN`). Task 28 adds `lifecycle_turn_end_notification_payload(summary)` — the NOTIFY-AND-CONTINUE turn end: drives `await_developer` → `awaiting-developer` and returns immediately (no gate, no wait), the one builder the choke-point auto-dismiss skips by name. |
| `lifecycle_finalize.py` | the terminal `lifecycle_finalize_task` builder, forwarding to the worktree finalizer and strict response model. |
| `task_doc.py`   | the `task_doc` JSON-primary task-document authoring builder (L14: master docs accept the additive `orchestrates` list — the dashboard's command-hierarchy source) (create/replace/set_status/set_step/add_step/remove_step/skip_step/read_steps/set_subtask/remove_subtask/set_section/append_decision/set_field/get; master ops are set_subtask/set_section), forwarding to the `task_doc_tools` application entry point. The builder is transport-thin and takes `operation` as a plain `str`, so this row's vocabulary mirrors the advertised set rather than anything the builder itself validates; the authoritative description lives in `mcp/registration/tasks.py`. |
| `gates.py`      | `lifecycle_gate_payload` (the public create+block+wait junction that blocks until a developer decision or gate-specific inbox response — or, with `wait=false` on a delegated SEAM kind (`SEAM_GATE_KINDS` only; plan-approval keeps its blocking brake) carrying a required non-empty `enclosure` (the master task name the integrate guard matches the gate by — an addressless raise refuses), validates-then-raises and continues, returning the gateId the handover packet carries — a refused raise persists no orphan gate and expires no sibling), public `gate_decide`/`gate_list` builders (decide resolves a bare gate id across lifecycles and refuses cli-attributed decisions on delegated kinds; list defaults to the ambient lifecycle when no id is passed, workspace only without an ambient), lower-level compatibility create/wait/response-wait builders, and the non-tool `gate_decide_for_lifecycle` the serving layer calls, config-rooted over a `GateStore(observer_root(config))`; lifecycle gate creation expires older open gates, targeted decisions reject stale gate ids, and `cancel` deletes throwaway gate interactions. Since 260731-EFA-L5 this module also **owns gate-log reclamation**: `_reclaim_gate_log` runs `GateStore.compact` at the end of every terminal decision, guarded by `GATE_OWNERSHIP.is_compaction_owner()` so the dashboard (which reaches `gate_decide_payload` directly) skips it — it moved here off the dashboard projection tick's 30-second rewrite, which raced this process's appends. The gate substrate itself lives in `controlplane/` (task 6). |
| `operator_inbox.py` | the three `operator_inbox_*` durable inbox builders (post/poll/consume), config-rooted over `OperatorInboxStore(observer_root(config))`; L3 adds agent role/message/artifact metadata plus optional hosted push delivery through the serving catalog/terminal paster seams; public consume returns the terminal snapshot and leaves physical expiry to compaction so concurrent delivery cannot resurrect it. The inbox substrate itself lives in `controlplane/` (task 10/L3). |
| `orchestration.py` | the L3 `orchestration_nudge_manager_payload` builder: records/rate-limits manager nudges, emits `orchestration.nudge`, and queues a manager inbox message through `operator_inbox_post_payload`. |
| `leaf_ref.py`   | shared MCP refusal-payload helper for `leaf-ref-not-found` / `leaf-ref-ambiguous`, keeping strict leaf-ref error envelopes out of the already-large terminal tool module. |
| `terminal.py`   | the L9 `attach_terminal_session_to_leaf_payload` builder (config-rooted over the dashboard `TerminalCatalog`, delegating durable reassignment to `serving.terminal_leaf_assignment`, returning `attached` / `leaf-taken` / `unknown-session` plus HFX-L4 leaf-ref refusals) AND the L2 `spawn_agent_session_payload` dispatch builder (L14: the payload records `spawnRole` from AR_SPAWN_ROLE for the chats command deck; L16/HFX2-L10: `_caller_spend_override_refusal` + `_resolve_harness_dispatch` + `_knob_refusal` + `_brief_packet` + `_deliver_spawn_pastes` + `_spawned_payload` — settings-only knob resolution with the `level` input, effective-registry harness resolution, per-harness model/effort validation, session-command delivery before the keyword-bearing brief, settings-owned free-form + level provenance) — it normalizes leaf refs, composes the shared `serving.terminal_opener.open_terminal_session` for live-identity validation, role-scoped leaf claim, native runner launch, and catalog upsert, then runs the capture-verified brief-delivery sequence. A live launch mismatch maps to `launch-selection-invalid` with no retry, expectation, or paste. Other strict response statuses remain `spawned`, `spend-override-unsupported`, `leaf-taken`, `harness-unknown`, `harness-not-detected`, `effort-invalid`, `model-invalid`, `level-invalid`, `leaf-ref-not-found`, `leaf-ref-ambiguous`, and `bad-kind`. 260731-EFA-L4 types the status seams against the wire aliases imported from `models.terminal` (`SpawnAgentSessionStatus`, `SessionRetireStatus`, `SessionRenameStatus`): `_spawn_refusal(status: SpawnAgentSessionStatus, ...)` and `_knob_refusal`'s `checks` tuple are annotated, so a refusal status this module invents is a pyright error at the producer rather than a `ValidationError` at `model_validate` — this payload is an untyped dict all the way to the MCP handler, which has no `except` for one. The retire/rename builders also collapse onto two constructors, `_retire_payload` and `_rename_payload`, so the shape rules have one site each: `_RETIRE_OK_STATUSES = frozenset({"retired", "already-retired"})` decides `ok` (previously written by hand at five call sites), retirement provenance rides a `closure=` argument and a policy clause rides `detail=` because nothing carries both, and `spawnedLabel` is emitted only when a row was actually renamed. |
| `__init__.py`   | Facade re-exporting the full builder surface and `_tool_payload`.          |

Since 2.5.1 this route also owns the response token-budget layer: the verbose
tools (`runtime_install`, `provider_diagnostics`, `provider_watchers`, and
since 2.5.2 the carryover plan/apply pair) write their full result to
`temp/tool-reports/<tool>/` via `mcp/tool_reports.py` (keep-last-5 / 7-day
write-time prune, secret redaction) and return a compact outcome with an
inline `reportPath` through the per-domain `compact_*_payload` helpers.

## Invariants And Boundaries

- `PUBLIC_TOOLS` — defined at `models/tools/public_roster.py` and re-exported by `base.py` — must
  match the declarations in `mcp/registration/`
  and the public response-model subset in `models/tool_registry.py`.
- **That match is checked against a live server, never against a payload that reports the tuple**
  (260831-LOCR-L29). `server_info` (`core.py`) returns `list(PUBLIC_TOOLS)` itself, so a case built
  on it compares the tuple to itself; `mcp/tests/test_tools.py::PublicSurfaceInventoryTests` registers
  every `TOOL_REGISTRARS` entry against a probe `FastMCP` and compares the live order instead. A tool
  this route registers but the tuple omits is advertised and — because
  `finalize_tool_response` indexes the response registry by name — unable to return a payload.
- `TOOL_RESPONSE_MODELS` may include retained compatibility builders that are not
  public MCP tools; do not infer public availability from facade exports alone.
- Every public payload returned from any submodule must go through
  `base._tool_payload`, which validates response shape only (request validation
  stays in server signatures and application entry points).
- **Anything the choke point adds to a response is a declared field of that response's
  model, set before the dump — never a key written into the dumped dict** (260731-EFA-L4).
  There is exactly ONE `model_dump` in the current model-owned finalizer reached through `_tool_payload`, and exactly one
  `finalize_payload_tokens` pass over its result, so "everything the caller receives is
  inside the count" holds by construction. A key added after the dump is served but
  uncounted, and — on the strict envelopes, which are `extra="forbid"` — makes the emitted
  object fail its own model. `TOOL_RESPONSE_MODELS` is typed `dict[str, type[ResponseEnvelope]]`
  precisely so setting these fields on the validated response type-checks.
- **`amb.emit_tool` follows finalization in `application/tool_response.py`**, so the `tokens` recorded against
  the lifecycle is the count the caller was actually served. Moving it back before the tail
  attachment re-introduces the short count in the event log even if the wire count is right.
  One consequence worth knowing when reading a log: the auto-dismiss now precedes the
  emission, so a turn-end dismissal appends `lifecycle.resumed` BEFORE the call's
  `tool.completed`, where it previously followed it. `emit_tool` records only
  `tool`/`tokens`/`ok`, so nothing in the event payload changed — only the order.
- A status string a builder writes must come from the wire alias in `models/`, annotated at
  the producing function, not spelled inline. These payloads are untyped dicts until
  `_tool_payload`, and by then a wrong status is a `ValidationError` inside an
  `@server.tool()` handler with no `except` for one.
- Payload builders stay transport-thin; deterministic behavior belongs in
  application entry points and package services. Import the domain application entry point that owns the
  tool's behavior — do not reintroduce a mega-facade.
- Submodules use `..` for `mcp`-package imports (`from .. import SERVER_NAME`,
  `from ..config import McpRuntimeConfig`) since they sit one level below the
  former `tools.py`.
- The facade `__init__.py` re-exports `_tool_payload` with an explicit
  `import _tool_payload as _tool_payload` so the conformance test's
  `tools._tool_payload` access keeps working.
- Compaction is wire-shape only and lives in this route, not in application entry points:
  the full result is written to the tool report BEFORE any compaction mutates
  it, decision/outcome facts stay inline, and
  `test_tool_response_budgets.py` holds every compact builder under
  `INLINE_BUDGET_CHARS` with deliberately fat inputs.
- **A builder on this route may reclaim a durable log it owns, and only on a write path, and only
  behind a non-raising ownership question** (260731-EFA-L5). `application/gate_tools.py::_reclaim_gate_log` is the
  one instance: `if not GATE_OWNERSHIP.is_compaction_owner(): return`, then
  `GateStore.compact` under `contextlib.suppress(OSError, ValueError)`, called at the end of
  `gate_decide_payload`. Two constraints, each with a named failure. It must not move onto a read
  path or a timer — a rewrite driven from the dashboard's projection tick is what cost 11.50% of
  gate snapshots at the base commit. And the check must stay a **question**, because builders on
  this route are not MCP-only: `serving/app.py` calls `gate_decide_payload` directly, so the
  dashboard executes this code, and a `CompactionOwnerError` (a `RuntimeError`) would pass straight
  through that suppress on every developer gate decision.
- **A reclaim failure must never cost the caller the operation that was already durable.** The
  suppress above wraps the reclaim only; the append, the delete and the expectation-row update
  ahead of it are not inside it, and the next decision on that lifecycle retries the prune.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Public response model registry maps each tool name to a Pydantic model. | `INTERNAL_COMPAT_TOOL_NAMES` | mcp/src/agents_remember/models/tools/tool_registry.py:120-141 |
| The checkpoint-landing name sits in the advertised tuple immediately after its integrate sibling, with the record-landing name next. | `worktree_checkpoint_landing`; `worktree_record_landing` | mcp/src/agents_remember/models/tools/public_roster.py:64-65 |
| The stop's name sits in the advertised tuple immediately after its sync sibling, in the working half of the surface. | `worktree_pause` | mcp/src/agents_remember/models/tools/public_roster.py:59-59 |
| Schema tests assert public tool and response model coverage. | `PublicToolResponseModelTests`; `PUBLIC_TOOL_RESPONSE_MODELS`; "def test_every_public_tool_has_a_schema_generating_response_model(" | mcp/tests/test_models.py:46-117 |
| The external-chat inbox builders post, poll, and consume operator responses. | "def operator_inbox_post_payload" | mcp/src/agents_remember/mcp/tools/operator_inbox.py:20-20 |
| The lifecycle finalizer builder exposes the terminal task finalization tool. | "def lifecycle_finalize_task_payload" | mcp/src/agents_remember/mcp/tools/lifecycle_finalize.py:15-15 |
| The linear-half hint delegates to the worktree guidance state machine. | "def lifecycle_guidance" | mcp/src/agents_remember/worktrees/modules/guidance.py:219-219 |
| The supervisor heartbeat store + staleness-banner helper `base.py`'s choke point calls (260707-HFX2-L2 R5). | "class AgentNotifierHeartbeatStore" | mcp/src/agents_remember/serving/agent_notifier_heartbeat.py:63-63 |
| The `ResponseEnvelope` union and the two choke-point fields (`nextStep`, `supervisorBanner`) declared on both envelope bases. | "class StrictResponseModel" | mcp/src/agents_remember/models/base.py:13-13 |
| The trusted terminal assignment response carries document-and-role binding plus private session correlation. | "class AttachTerminalSessionToTaskResponse" | mcp/src/agents_remember/models/terminal.py:32-44 |

Current working-candidate evidence for this route:

| Finding | Anchor | Source |
| --- | --- | --- |
| The application request owner has only code and memory messages. | `CloseoutCommitMessages` | mcp/src/agents_remember/application/worktree_tool_requests.py:110-115 |

## 260712-TRH-L4 Route Impact

The public tool route now exposes spawn-only creation, exact-session hosted_session_readiness, and an explicit dispatch-brief kind. Legacy context/submit refuses before side effects; promptKeywords apply once after readiness; completion requires delivered plus harness-log-confirmed proof.

### 260713-PHA-L5 Route Contract Review

The route remains governed by the shared hosted protocol bridge: exact adapter snapshots provide
readiness and liveness, correlated receipts sit beneath durable inbox rows, interactions use durable
gates, legacy/custom sessions are explicit unsupported states, and pane/log signals are diagnostic
only. Dashboard and packaged projections remain additive and synchronized.

## Historical 260731-EFA-L4 — The Choke Point Emits Its Own Contract

`_tool_payload` used to do this: validate, dump, count tokens, emit the observer event, then
write `nextStep` and `supervisorBanner` into the dumped dict. Two things were wrong with the
last step and both were silent.

- **The advertised token count excluded them.** `finalize_payload_tokens` stamps `tokens` from
  the dict it is handed; keys added afterwards are served but never counted. Because
  `amb.emit_tool` also ran before them, the count recorded against the lifecycle was short by
  the same amount, so the fuel gauge and the wire agreed with each other and both disagreed
  with reality.
- **`supervisorBanner` was declared on no model.** On a strict envelope (`extra="forbid"`) that
  makes a banner-carrying response fail its own `model_validate`; on a flexible one
  `extra="allow"` silently accepted it, which is the wrong kind of tolerance — that setting is
  for a PROVIDER's fields, not this package's.

The fix has two halves. `models/base.py` declares `supervisorBanner` on both envelope bases and
names their union `ResponseEnvelope`; `models/tool_registry.py` types both registries
`dict[str, type[ResponseEnvelope]]` instead of `type[BaseModel]`. That retyping is what makes
the reordering possible at all: against a bare `BaseModel`, `response.nextStep = ...` is not an
attribute a checker knows, so writing into the dict afterwards was the only type-clean option
available. `_tool_payload` now reads:

    response = model.model_validate(payload)
    amb = ambient()
    if amb is not None:
        _attach_lifecycle_tail(response, amb, tool_name)   # dismiss, nextStep, banner
    finalized = finalize_payload_tokens(response.model_dump(mode="json", exclude_none=True))
    if amb is not None:
        amb.emit_tool(tool_name, finalized)                # last, off the served payload

`next_step.py`'s `next_step_for` returns `NextStep | None` rather than a dumped dict, for the
same reason: serialization belongs to the one `model_dump`.

Historical coverage gap: the former response-conformance fixture used a workspace whose supervisor had never ticked, leaving the banner silent. Its subsequent stale-heartbeat fixture exercised both payload injections. Those tests have since been removed; this remains design history explaining why validation must consider the final injected payload, not a claim of retained coverage.

## Historical 260731-EFA-L5 — Gate-Log Reclamation Before The Application Move

One file on this route changed, `gates.py`, and the change is a **responsibility moving into this
route** rather than a payload edit: gate-log compaction. It used to ride
`observer/snapshots.read_gates` on a 30-second throttle — the dashboard's projection tick physically
rewriting a log the dashboard owns nothing in, racing this process's appends. That is where 11.50%
of appended gate snapshots were going at the base commit, and a lost snapshot there is not a missing
row: the `applied` marker is what stops one human approval being consumed twice.

`_reclaim_gate_log(store, lifecycle_id)` now runs at the end of `gate_decide_payload`, which is the
moment a record *becomes* reclaimable. Three properties are worth carrying at route level, because
each is a rule about how builders here may touch durable state:

1. **Write paths only.** `gate_list_payload` and both wait loops stay pure reads. Moving the reclaim
   here changes who prunes and when, never what a caller is shown.
2. **The ownership check is a question, not a refusal.** `serving/app.py` calls
   `gate_decide_payload` **directly**, so a builder on this route runs inside the dashboard process
   too. `is_compaction_owner()` answers `False` there and returns. A version that raised would send
   `CompactionOwnerError` — a `RuntimeError`, so invisible to `suppress(OSError, ValueError)` —
   out of every developer gate decision made from the dashboard.
3. **The observable consequence is space, never correctness.** Reclamation follows owner activity
   instead of a wall clock, so a gate expired on a quiet lifecycle keeps its superseded rows on disk
   until the next MCP decision there. `GateStore.projected_current` applies the identical
   keep-filter in memory on every tick, so the dashboard renders exactly what it rendered before.

The substrate this rides on is `ar-durable-store/1.0` in `controlplane/durable_store.py`, and it is
that route's to describe. The one thing to carry here: what makes the rewrite safe is the log's
unconditional `flock`, held across the read **and** the rewrite, in every process. Ownership decides
only who runs the pass.

## 260731-EFA-L9 Route Impact — Caller Re-Points

The MCP tool callers were rewritten by the L9 caller wave to import the responsibility-owning homes (`models/conversations/`, `kernel/primitives/`, `serving/ports.py`, `models/terminal_catalog.py`). Tool behavior and payloads are unchanged.

## L23 Package-Following Payload Imports

Core payload builders import runtime installation and skill installation from
`application.runtime`, while worktree payload builders import integration strategy from
`models.lifecycles.operation`. These are package-ownership moves only: payload validation,
task-document addressing, and transport-thin forwarding remain the route contract.

## 260815-DAG-L3 Queue Payload Route

`mcp/tools/closeout_queue.py` is the thin public payload builder for the registered
`closeout_queue` tool. It delegates the strict request to the ambient-authorized application
service and then uses the common `_tool_payload` envelope. Registration and response conformance
cover the public schema; scheduling, persistence, and lifecycle logic do not live on this route.

## 260815-DAG Master Full-Gate Repair Route Impact

`tools/{core,task_doc,worktree}.py` import paths updated to the moved `application/task_docs/*`.

## 260821-CLIVE-L2 Current Architecture

Tool payload composition preserves the closed application result vocabulary. The layer does not catch lower reader exceptions or reconstruct lifecycle facts; it serializes already projected public evidence and executable next actions.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| Lifecycle/adoption/legacy payloads — the enclosure-adoption payload builder was removed; lifecycle control now goes through `worktree_operation_control_payload`, and enclosure adoption survives only in the lifecycle-owned enclosure-adoption service. | `worktree_operation_control_payload` | mcp/src/agents_remember/mcp/tools/worktree.py:195-202 |

## 260821-DAGQC-L2 Typed Memory-Quality Adapters

The memory tool route now has three thin DTO-specific adapters over the single controller API.
They validate public responses but do not interpret wait flags, rebuild scope, or reproduce
capacity/poll failure translations.

## MCAR-L02 Curator-Coherence Adapter

`curator_coherence.py` is the sole thin adapter for the lifecycle-owned coherence API. It adds no
filename aliases or policy: configured admission and publication remain upstream, while the shared
tool-response boundary validates every success/refusal body.

## Status-Change Wait Payload

`worktree_status_wait_payload` was removed with the wait tool it served. The remaining worktree
builders — for example `worktree_attach_payload` — keep the same shape: they forward the typed
request to the application adapter and pass its result through the ordinary tool-response boundary
without adding polling, retry, cancellation, cursor advancement or journal mutation of their own.

| Finding | Anchor | Source |
| --- | --- | --- |
| The removed wait payload builder has no replacement; the surviving worktree builders still delegate the exact typed request and use the standard response wrapper. | "def worktree_attach_payload(" | mcp/src/agents_remember/mcp/tools/worktree.py:75-86 |

## 260831-LOCR-L30 Checkpoint-Landing Tool

This route's advertised surface grew by one name: `worktree_checkpoint_landing`, listed in
`base.py`'s `PUBLIC_TOOLS` immediately after `worktree_integrate` (the tuple held 62 names at L30; it
holds 63 since 260831-LOCR-L37) and
built by `mcp/tools/worktree.py::worktree_checkpoint_landing_payload`, which forwards to
`application/worktree_tools.py::worktree_checkpoint_landing_tool`. It is registered by
`mcp/registration/closeout.py`'s `_register_integration_command_tools` and carries
`models/worktree.py::WorktreeCheckpointLandingResponse` through
`models/tools/tool_registry.py::TOOL_RESPONSE_MODELS` — all three places a public tool must appear.

The three-part requirement is the L29 lesson applied by construction rather than by repair, and the
two landing tools are why the inventory suite drives one `finalize_tool_response` call per name:
their payloads differ only in the operation literal, so a set comparison would pass a registry swap.

## 260831-LOCR-L37 Pause Payload

This route gained one builder and one advertised name. `worktree_pause_payload` takes only
`contract_path`, forwards it to `application/worktree_tools.py::worktree_pause_tool`, and wraps the
result under the operation name `worktree_pause`; `worktree_pause` sits in `PUBLIC_TOOLS` immediately
after `worktree_sync` (the tuple now holds 63 names) and carries `WorktreePauseResponse` through
`TOOL_RESPONSE_MODELS`. All three places a public tool must appear were added together, which is the
L29 lesson applied by construction rather than by repair.

The builder owns no decision, and specifically not the one the split exists to protect: whether
anything is **published**. That decision does not exist on this path at all — the route it forwards to
cannot reach a publication module — and the publication this route also carries
(`worktree_checkpoint_landing_payload`, in the same module) is a different builder for a different
tool. Two names, two builders, two routes.

## 260831-LOCR-L29 Public-Inventory Repair

`base.py`'s `PUBLIC_TOOLS` gained `worktree_record_landing` immediately after `worktree_integrate`,
and the tuple held 61 names at that leaf (62 since 260831-LOCR-L30 added the checkpoint landing
route). `mcp/tools/worktree.py`'s
`worktree_record_landing_payload` and its `mcp/registration/closeout.py` declaration both already
existed, so the tool was registered and advertised while the census omitted it.

The consequence is specific to the choke point this route owns: `finalize_tool_response` indexes
`TOOL_RESPONSE_MODELS` by tool name, so the omission — together with the absent registry row in
`models/tools/tool_registry.py` — made the advertised tool raise instead of returning a payload. The
invariant below had no executor: `mcp/public_surface.py` compares a live `list_tools()` result to this
tuple, but the only test doing so read `server_info`, which returns `list(PUBLIC_TOOLS)` from
`core.py`, making the comparison self-referential. `mcp/tests/test_tools.py::PublicSurfaceInventoryTests`
now registers every `TOOL_REGISTRARS` entry against a probe `FastMCP` and compares the live order to
this tuple.

## 260831-LOCR-L32 The Advertised Tuple Moves To `models`; This Route Re-Exports It

`PUBLIC_TOOLS` is no longer **defined** in `base.py`. Its one definition is now the zero-import `models`
leaf `mcp/src/agents_remember/models/tools/public_roster.py` — the tuple's extent is `L22-L86` since
260831-LOCR-L37 added `worktree_pause`, and was `L22-L85` at L32; `base.py` imports it at L14 and
declares the re-export through `__all__` at L19, so `agents_remember.mcp.tools.PUBLIC_TOOLS` still
resolves the identical object — same tuple, same order, 62 unique names at the move and 63 since
260831-LOCR-L37 — and every builder,
registration path, and conformance comparison in this route is unchanged. `base.py` shrank from 79
lines to 24; `TRANSPORT` is now L16, `RESERVED_TOOLS` L17, and `_tool_payload` L22-L24.

**Why the tuple had to leave this route.** The move is what makes the worktree surface's next-move
vocabulary enforceable at the model boundary. `application/worktree_status.py::_project_terminal_contract_status`
writes `nextAction` / `nextTool` / `nextArgs` into the `worktree_status` payload, and enforcing those
values requires a `models` response model to read the roster. From `mcp` that read is not writable:
`models → mcp` is a `layers.toml` violation (models = 2, mcp = 22; the `mcp` charter forbids any import
from below), a function-local import trips `ruff PLC0415` with suppressions forbidden here, and
module-level imports in either direction are circular. The layering checker stayed at its exact
baseline of 16 violations with no `models → mcp` edge and no new cycle.

**Do not move it back, and do not add a second copy here.** A re-export is the whole relationship; a
local re-declaration would recreate the layering problem and could silently diverge from the tuple the
model layer reads.

The dated sections in this card that say `base.py`'s `PUBLIC_TOOLS` "gained" a name, or that the tuple
"is the authority on the advertised name set", describe the tuple **at their own leaf**. They remain
accurate history; the names, counts and registry rules they record still hold. Only the definition's
location changed, and it is now `models/tools/public_roster.py`.

## 260915-CAPS-L4 Capsule And Skill Payload Builders

This route gained three builders in one new submodule, `capsule_serving.py`. They are transport-thin in
the ordinary way — each re-shapes the declaration's flat arguments into the application request record,
calls one application entry point, and returns the result through `_tool_payload` — but two of their
properties are route-level facts:

- **The corpus override is a test seam, not a capability.** `skill_catalog_list_payload` and
  `skill_catalog_read_payload` accept optional `origin` / `root` keyword-only arguments, and the
  application layer serves the shipped corpus when neither is supplied. The registered declarations in
  `registration/capsule_serving.py` pass **no** override, so a live client cannot point the server at a
  different tree; the seam exists so the leaf's test module can drive a synthetic corpus without
  touching the shipped one. This is the route's flatness rule holding on the wire while the builder
  side keeps the extra parameter — the same asymmetry the builders' parameter objects exist for.
- **A refusal is already a value by the time it arrives here.** `RoleCapsuleResponse` carries the
  refusal in the same envelope as a success (`ok` false plus a typed `refusalStatus`), so these
  builders wrap a refusal exactly as they wrap a capsule. Nothing on this route translates an
  application refusal into a transport error.

The three names sit at the tail of `PUBLIC_TOOLS` and of `TOOL_RESPONSE_MODELS`, appended rather than
inserted so no existing advertised position moved.

One boundary this route must not blur: these three tools are **this server's own reads**. The
extension's enumeration surface is the `skills/list` **protocol method**, implemented on the
registration route (`registration/skills_extension.py`), not a tool — and the `skill://index.json`
resource this server also publishes is its own convenience surface in the Agent Skills discovery shape,
which is likewise not the extension's enumeration result.

| Finding | Anchor | Source |
| --- | --- | --- |
| The capsule builder re-shapes the flat declaration arguments into the application request record. | `role_capsule_compile_payload` | mcp/src/agents_remember/mcp/tools/capsule_serving.py:22-41 |
| The two skill builders build a corpus request only when an override was supplied, so the shipped corpus is the default. | `skill_catalog_list_payload`; `skill_catalog_read_payload` | mcp/src/agents_remember/mcp/tools/capsule_serving.py:44-63 |
| The declarations that call these builders, which pass no corpus override to the wire surface. | `_register_skill_tools` | mcp/src/agents_remember/mcp/registration/capsule_serving.py:121-140 |
| The capsule envelope carries its refusal in the same shape as a success. | `RoleCapsuleResponse` | mcp/src/agents_remember/models/role_capsule_resources.py:86-115 |
| The extension's enumeration surface is the `skills/list` method on the registration route, not a builder on this one. | `install_extension_methods` | mcp/src/agents_remember/mcp/registration/skills_extension.py:133-153 |
| This server's own index resource, kept deliberately distinct from that method. | `index_resource` | mcp/src/agents_remember/mcp/registration/capsule_serving.py:228-251 |

## 260915-KS-L20 The Five Knowledge Payload Builders, And Where A Handler Refuses To Decide

`mcp/tools/knowledge.py` adds one builder per mounted `knowledge_*` operation family, and its defining
property is what it does **not** do: no classification is computed, no effect label is inferred, no draft is
authored, no rationale is judged, no ambiguity is resolved by choosing, no missing assessment is filled, and
no compatibility verdict is produced. Where a handler would have to decide something, it returns the
unresolved state instead, and the module's brevity is the measurement of that rule rather than an accident
of scope. Two of the five are quoted at requirement level and their builders are the reason: `knowledge_read`
returns "recorded claims and assessments as attributed records", and the payload it returns **is the view
payload itself**, so the classification rule has exactly one implementation instead of a second renderer
here; `knowledge_diff` includes "semantic effect labels ... only when supplied by an identified
agent/assessment, not inferred from the diff", so `_supplied_effect_labels` collects the labels the
comparison already carries and never derives one.

**Four request records and one builder that takes none.** `ReadToolRequest`, `ChangeToolRequest`,
`DiffToolRequest` and `ProjectToolRequest` are the wire shapes, and each field they declare is an input the
caller must supply rather than a default the substrate chooses — the dataset path, the namespace, the
destination, the view name, the ordering input, the limit, the continuation, the authorized overwrites.
`knowledge_integrity_check_payload` takes no request at all, which is the honest shape for an operation
whose answer is "here are the recorded conditions and here is what could not be resolved":
`_recorded_conditions` reads the shipped detection run **for the named scope** — `_run_for_scope` matches
the caller's scope against the run's own registered traversal scope and `_no_run_for_scope` reports a scope
no recorded run measured — `_no_detection_run` reports the absence as a state rather than as an empty
condition list, and `_condition_report` carries each matched fact beside the condition that matched it.

**Two refusal builders exist so that a refusal never becomes a default.** `_refused_read` returns the
typed refusal naming the offending view and the code, and `_refused_project` names the destination and the
code, so a caller can always tell "nothing was selected" from "the selection was refused" — a distinction
the response models' `state` discriminator preserves on the wire. `DECLARED_CHANGE_KINDS` is the six-member
tuple of record kinds this surface may be *asked* about (`evidence_claim`, `verification_observation`,
`invariant_revision`, `assumption`, `semantic_change_set`, `requirement_revision`), and the refusal is
unconditional for every member of it: the shape records that the earlier spelling advertised two "admitted"
kinds and then refused both anyway, which made the tool's own description false, so the refusal now names
`WRITE_ENTRY_POINT` — the `agents-remember knowledge-ingest` subcommand — as where the write actually
happens, because inventing a second write path here is exactly the authority the requirement forbids this
route to add. `_projection_requests` builds one view request per requested view so
the projection builder reads each view through the same seam a direct read does, rather than through a
second selection path.

## 260915-KS-L32 The Integrity Lookup Is Bound To The Requested Scope

The route's read surface gains one optional seed and loses one silent substitution. `knowledge_read` now
publishes `sourcePath`, forwarded into `ReadToolRequest.source_path`, so a caller who knows only a file can
present that file as a seed and let the view layer resolve what governs it — a front door that does not
require first discovering an invariant revision id or a family revision id. On the integrity side the
correction is smaller and more consequential: the scope a caller names now **selects** the reported run
rather than being echoed beside one. Before this, every recorded `detection_run` row was read in record-id
order and the first was reported whatever scope the caller asked for, so with more than one run recorded
the answer was whichever run happened to sort first while the response still named the requested scope —
"scope X" printed beside conditions measured over scope Y. `_run_for_scope` now matches the caller's scope
against the run's own registered traversal scope (`governing_route_id`) and keeps searching past a run
measured over a different one; a caller naming no scope keeps the previous behaviour (the first recorded
run), and a caller whose scope matches no run is told so by `_no_run_for_scope` rather than handed another
run's conditions. The scope-selection invariant, the two new helpers and the `DECLARED_CHANGE_KINDS` /
`WRITE_ENTRY_POINT` correction to the L20 section above are the route-level record of it.

## Update History
- 2026-09-20T06:50+02:00 — 260915-KS-L40 curator (uncommitted CYCLE-02-remainder change set on `ar/260915-ks-l40-ar`, code base `f79f4db7`): **route body updated.** `worktree_sync_payload` now takes one paired `resolution: SyncResolutionInput | None` — the action plus the authored decision it may carry, paired one layer up in `registration/worktrees.py` — in place of a bare `resolution_action`; the paragraph is in the `IAS Frozen Worktree Payload Boundary` section above. The import block grew by the two vocabulary imports, so every builder on this route moved by three lines. A body change, not a metadata-only refresh.

- 2026-09-20T02:12+02:00 — 260915-KS-L32 memory-side conflict resolution (uncommitted; this worktree, code base `7dcec036`, merged tree = L30's landed `7ca3ac48` plus this leaf's four modified paths): **resolved the one conflicted reference row and the Update History block.** The row cites `mcp/tests/test_models.py`, modified by neither leaf, so upstream's `46-117` — the class's own declaration extent, from its `class` line through its last statement — was kept, and both sides' anchors were kept: the class, `PUBLIC_TOOL_RESPONSE_MODELS` and the quoted merged `def …(` line, each read inside that range in the code worktree. Update History is the union of both sides, newest first. No claim was re-worded, no anchor, row or citation dropped, and no verification stamp advanced.
- 2026-09-20T01:41+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): No route impact: this leaf changed no source this route governs. Its six paths are `application/knowledge_curator_ingest.py`, `application/knowledge_ingest.py`, `cli/knowledge_ingest.py`, `mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test_dependency_ownership_ast_helpers.py` and `mcp/tests/test_knowledge_curator_ingest_list.py` — none of them under `mcp/src/agents_remember/mcp/tools/`. The overview was re-read and no claim of its body is invalidated by this leaf; only its citation rows were repointed to the same constructs. No verification stamp is advanced.
- 2026-09-20T01:29+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **cleared this card's one reopened claim, answering both questions the checklist put to it.** (1) Does the construct the projected range covers support the claim's own words? Yes: "Schema tests assert public tool and response model coverage" is exactly what `PublicToolResponseModelTests` does — its first case asserts `set(PUBLIC_TOOLS) == set(PUBLIC_TOOL_RESPONSE_MODELS)` and then generates each registered model's JSON schema. (2) Was the range rebound from a mention to a declaration elsewhere? No: `mcp/tests/test_models.py:46-117` is the class's own declaration extent (the class at 46 through its last statement at 117), not a mention's target, so the mechanically projected range is the location the claim is about and it is **retained** — no re-cite and no re-wording was needed. **Stamp accounting:** the stale `lastVerifiedCommitHash`/`lastVerifiedCommitDate` rows (and the L20-era `reviewedWorkingCandidate` row beside them) were replaced by ONE `reviewedWorkingCandidate` row naming this candidate, because no commit contains the body as it now stands and no stamp was measured on it. The claim's "evidence changed" condition was an artifact of comparing against a commit that predates the consolidation: the class is byte-identical between this candidate's base `7dcec036` and the working tree, so the claim is current against the base this card now names.
- 2026-09-20T00:46:52+02:00 — 260915-KS-L32 curator (uncommitted change set on `ar/260915-ks-l32-ar`, code base `7dcec036`, memory base `66b2ae8a`): **added the L32 section** — the read surface's new `sourcePath` seed, and the integrity check's lookup now bound to the requested scope instead of reporting the first recorded run's conditions under whatever scope was asked for. The L20 section above was also corrected where this leaf's findings showed it describing code that does not exist: it named `ADMITTED_CHANGE_KINDS` as a two-member admitted tuple, but the module declares `DECLARED_CHANGE_KINDS` (six kinds) with an unconditional refusal naming `WRITE_ENTRY_POINT`, and `_recorded_conditions`'s description now names `_run_for_scope` and `_no_run_for_scope`. The `PublicToolResponseModelTests` row was repointed from `test_models.py:16-26` (import lines, which never held the anchor) to `46-61`, where the class and its single schema-generating case live after the 260915-KS-L29 consolidation. Body changed substantively; this entry is the history record, not a metadata-only refresh, and no verification stamp advanced because the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-19T22:28:52+00:00: Generated citation repair: `PublicToolResponseModelTests` repointed to mcp/tests/test_models.py:46-117. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "def lifecycle_guidance" repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:219-219. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:30+02:00 — 260915-KS-L20 curator (uncommitted change set on `ar/260915-ks-l20`, base `9f88a6de`): **added the L20 section** — the five builders for the five mounted `knowledge_*` families and the rule that keeps them short (nothing is decided here; where a handler would have to decide it returns the unresolved state); the two requirement-level quotations and why `knowledge_read` returns the view payload itself; the four request records plus the one operation that takes none; and the two refusal builders plus `ADMITTED_CHANGE_KINDS`, which is why an unadmitted record kind refuses with `registration_absent` instead of acquiring a second write path. The metadata block above now names this leaf's candidate as what was read; the body was changed substantively and this entry is the history record, not a metadata-only refresh.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `worktree_checkpoint_landing`; `worktree_record_landing` repointed to mcp/src/agents_remember/models/tools/public_roster.py:64-64; mcp/src/agents_remember/models/tools/public_roster.py:65-65. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `worktree_pause` repointed to mcp/src/agents_remember/models/tools/public_roster.py:59-59. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "def lifecycle_guidance" repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:215-215. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `worktree_operation_control_payload` repointed to mcp/src/agents_remember/mcp/tools/worktree.py:195-202. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T10:20:31+00:00 — 260915-CAPS-L9 curator: recorded that `runtime_install_payload` now takes the run's
  own `RuntimeInstallRequest` instead of four keyword flags, and why (the run's selection input
  reaches the entry point by construction, and the payload can report `selectionSource`).
  Verification metadata is left at its recorded value; the candidate is deliberately
  uncommitted.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "def lifecycle_guidance" repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:215-215. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T06:49:47+00:00: Generated citation repair: `worktree_operation_control_payload` repointed to mcp/src/agents_remember/mcp/tools/worktree.py:195-202. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T12:20+02:00 — 260915-CAPS-L4 curator, **closing pass** (uncommitted change set on
  `ar/260915-caps-l4`, base `b00a4ac2`): re-anchored the `_register_skill_tools` range against the
  current 278-line registration module and added the boundary row this route needs after the repairs:
  the three tools here are this server's **own** reads, while the extension's enumeration surface is the
  `skills/list` protocol method implemented on the registration route, and this server's
  `skill://index.json` resource is its own convenience surface rather than that method's result. The two
  properties recorded below (the corpus override as a test seam, refusal-as-value) are unchanged.

- 2026-09-16T11:45+02:00 — 260915-CAPS-L4 curator (uncommitted change set on `ar/260915-caps-l4`, base
  `b00a4ac2`): added the three new builders of `capsule_serving.py` to this route and recorded the two
  properties worth carrying at route level — the corpus `origin`/`root` override is a test seam the
  registered signatures deliberately exclude from the wire, and a refusal arrives already shaped as a
  value in the same envelope as a success, so no transport-level translation exists here. Corrected the
  advertised-name count this card carried in two current-state places (the `base.py` paragraph and the
  `base.py` layout row) from 62 to the measured **66** (62 at the L32 move, 63 from 260831-LOCR-L37, 66
  since this change), and recorded that the three names were appended at the tail. Verification
  metadata remains closeout-owned; no acceptance claim.

- 2026-09-15T00:56:17+00:00 — LCA ledger-retirement working-candidate curation: Documented removal of ledger message forwarding from the public worktree adapter. Existing verified commit/date remain historical provenance until producer-owned closeout. Source inspection only; no aggregate acceptance claim.

- 2026-09-13T17:20:55+00:00: Generated citation repair: `worktree_operation_control_payload` repointed to mcp/src/agents_remember/mcp/tools/worktree.py:199-206. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T19:02+02:00 — 260831-LOCR-L37: recorded the new `worktree_pause_payload` builder and the
  `worktree_pause` name, its position in `PUBLIC_TOOLS` immediately after `worktree_sync`, and its
  `WorktreePauseResponse` registry row — the three placements a public tool must occupy, all added at
  once. Stated that the builder owns no publication decision and that the publication in this module
  (`worktree_checkpoint_landing_payload`) is a different builder for a different tool. Corrected the L30
  count sentence, which pinned the tuple at 62 names. Verification metadata remains closeout-owned; no
  acceptance claim.
- 2026-09-13T00:40+02:00 — 260831-LOCR-L33 curator: this route's behavior is unchanged — the
  `task_doc.py` builder stays transport-thin and still accepts `operation` as a plain `str` — but the
  Layout row's operation vocabulary was stale, so it now carries the step-plane operations
  (`add_step`/`remove_step`/`read_steps`) and says explicitly that the row mirrors the advertised set
  rather than anything the builder validates (the authoritative description is in
  `mcp/registration/tasks.py`). No route impact beyond the corrected vocabulary.
- 2026-09-12T22:55+02:00 — 260831-LOCR-L32 curator: recorded that `base.py` now **re-exports**
  `PUBLIC_TOOLS` from its new single definition at `models/tools/public_roster.py:22-85`, and that this
  route's own behavior — the choke point, the builders, and the registration surface — is unchanged by
  the move. Corrected the three current-state places that named `base.py` as the roster's home (the
  Purpose/Hot Path entry point, the Current Response And Adapter Ownership paragraph, the `base.py`
  Layout row and the surface invariant) and repointed the checkpoint/record-landing citation from the
  mechanical `registration/closeout.py` projection back to the advertised tuple, where the claim
  actually lives. Added the section recording why the tuple had to leave this route. Verification
  metadata remains closeout-owned; no acceptance claim.
- 2026-09-12T20:53:11+00:00: Generated citation repair: `_tool_payload` repointed to mcp/src/agents_remember/mcp/tools/base.py:22-24. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T20:53:11+00:00: Generated citation repair: `worktree_checkpoint_landing`; `worktree_record_landing` repointed to mcp/src/agents_remember/mcp/registration/closeout.py:180-202; mcp/src/agents_remember/mcp/registration/closeout.py:204-229. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T02:50+02:00 — 260831-LOCR-L30 checkpoint landing: recorded the new `worktree_checkpoint_landing`
  name in this route's census (62), its payload builder and registered declaration, and the
  three-part public-tool requirement; corrected the two stale 61-name counts and re-derived the
  shifted `worktree.py`/`base.py`/registry ranges. Verification metadata remains closeout-owned; no
  acceptance claim.
- 2026-09-12T01:41:08+02:00 — 260831-LOCR-L29 public-surface repair: recorded the
  `worktree_record_landing` census addition for this route's choke point, corrected the two stale
  public-census counts on this card (64 → 61 and 63 → 61), stated the live-probe invariant with the
  self-referential-`server_info` warning, and added the reference row. Verification metadata remains
  closeout-owned; no acceptance claim.
- 2026-09-11T23:05:00+00:00: Two anchors named constructs that no longer exist anywhere in the tree: `worktree_enclosure_adopt_payload` and `worktree_status_wait_payload` are gone from `mcp/tools/worktree.py`, whose current builders are start, sync, attach, status, closeout-preview, closeout-apply, integrate, record-landing, operation-control, cleanup and abandon. The two rows now name surviving constructs — `worktree_operation_control_payload` (167-174) for lifecycle control and `worktree_attach_payload` (74-83) for the unchanged thin `_tool_payload` forwarding — and the Status-Change Wait Payload section records the removal.

- 2026-09-11T22:39:01+00:00: Generated citation repair: `_tool_payload` repointed to mcp/src/agents_remember/mcp/tools/base.py:75-77. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-09T02:35:47+02:00 — CCR-L38 inherited route reconciliation: re-read this route's purpose, member inventory, route summary, and invariants against frozen candidate code tree `4c6b7bc2362bc03d50fc7a0643f34b591b805d45`; the candidate's changed paths are outside source route `mcp/src/agents_remember/mcp/tools`, so no route/member/prose/invariant change is required. route-member-count=21; source inspection only; verification metadata remains unchanged pending producer-owned realization. No acceptance or certification claim.

- 2026-09-05T07:22+00:00 — L31 cumulative source review at `ea35964985f30080488270e71ac81657ac40682b`: Separated historical adapter/public-name accounts from current application-owned response, guidance and gate behavior; reviewed the new wait adapter. Verification records source review, not execution or acceptance.
- 2026-09-05T06:21+00:00 — Re-read the affected source declarations and repaired citation ranges shifted by CCR additions. Preserved the route contract and existing history; literal anchors identify the exact current construct where shared identifiers were ambiguous.

- 2026-09-05T06:12+00:00 — Composed retained CCR route contributions without replacing sibling knowledge; preserved prior source-verification metadata and historical entries.

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec: route coverage refreshes the public `worktree_status_wait` tool surface (payload export, package export, `PUBLIC_TOOLS` census); route index regenerated.

- 2026-08-30T15:15:36+02:00 — 260821-ARSPAWN-L4 route impact: the public inventory is 63 names in
  exact live order, and `server_info` projects the shared content-addressed runtime identity.
  Verification remains closeout-owned.

- 2026-08-29T08:52+02:00 — Added the single curator-coherence payload adapter; no compatibility
  route or overlapping tool was introduced. Verification remains closeout-owned.

- 2026-08-26T08:55+02:00 — Finalized the IAS worktree-payload boundary label against the frozen
  pass-13 candidate.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: replaced flat quality branching with strict sync/start/poll adapters over the canonical controller. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: citation-only repair repointed moved lifecycle, tool-model, direct-landing, legacy, or startup evidence to its canonical committed source path; this card's own documented behavior is unchanged.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: refreshed current route intent and source evidence for the accepted full L2 candidate; verification provenance and contract-scoped quality enforcement remain architect-closeout-owned.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair route impact: tool payload modules import paths updated to the moved packages. Verified at code commit e5cb139f.

- 2026-08-20T21:30+02:00 — 260815-DAG-L15 route impact: async memory-quality start/poll payload builders (L15-R7). Verified at code commit de3a0fd9.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16 route impact: `direct_landing_payload` joins the facade
  exports (`mcp/tools/direct_landing.py`), and `PUBLIC_TOOLS` advertises `direct_landing` (59
  names). Verified at code commit a9d50e08.

- 2026-08-15T09:10+02:00 — 260815-DAG-L3 route impact: added the closeout-queue payload adapter
  and kept ambient identity plus mechanics out of the MCP tool surface. Verification remains
  closeout-owned.

- 2026-08-13T09:05+02:00 — L23 route review: `core.py` follows runtime install/skills into the
  `application.runtime` package and `worktree.py` follows integration DTOs into
  `models.lifecycles.operation`. Payload-builder behavior and the public tool surface are
  unchanged; final provenance remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: added task-addressed lifecycle payload composition and the sanctioned citation-fix memory payload; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — 260731-EFA-L19 curator: reconciled the tool layer with structural
  document-and-role requests and plane-owned runtime addresses; retired exact-id agent tools do not
  remain as a parallel public control path.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 route impact: L9 caller/import re-points recorded and body updated.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B23 curator: replaced the `n/a` rows with exact
  anchors (deleting three unresolvable overview/missing-module rows); exact non-fixing check
  returns zero findings.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No route impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T13:20+02:00 — 260731-EFA-L5 curator: `gates.py` is the only file on this route the leaf
  touched, and it gained a responsibility rather than a payload change — gate-log reclamation moved
  here off the dashboard projection tick. Added the L5 section and updated the `gates.py` Layout row.
  Added two invariants, each naming the failure it prevents: a reclaim on this route may sit only on
  a write path and only behind a **non-raising** ownership question (because `serving/app.py` calls
  `gate_decide_payload` directly, so these builders execute in the dashboard process), and the
  reclaim's `suppress` must not widen to cover the durable work ahead of it. No tool name, payload
  shape, refusal vocabulary or registration changed. Verification metadata pinned until closeout
  stamps the L5 code commit.
- 2026-08-01T09:26+02:00 — 260731-EFA-L4 curator: **body corrected.** The `_tool_payload` order
  this card described is no longer the order in the code, and the description was load-bearing:
  the Hot Path Summary said the `nextStep` hint is attached "after the ambient emission hook" and
  the `base.py` Layout row said the auto-dismiss runs "after the ambient emission hook" too. Both
  are now inverted — `_attach_lifecycle_tail` (dismiss → `nextStep` → `supervisorBanner`) runs on
  the validated model BEFORE the single `model_dump`, and `amb.emit_tool` runs LAST off the
  finished payload. Rewrote both, added the route-impact section explaining what the old order cost
  (bytes served outside the advertised `tokens`, and the same short count recorded against the
  lifecycle) and why `TOOL_RESPONSE_MODELS`'s `type[BaseModel]` typing is the reason the fields
  were written into the dumped dict in the first place. Added four invariants: everything the
  choke point adds is a declared field set before the dump; there is exactly one `model_dump` and
  one token pass; `emit_tool` is last, with the resulting `lifecycle.resumed`-before-`tool.completed`
  log ordering noted; and a status string comes from the `models/` alias annotated at the producer.
  Updated the `next_step.py` row (`next_step_for` returns the model) and the `terminal.py` row
  (typed refusal seams, `_retire_payload`/`_rename_payload`, `_RETIRE_OK_STATUSES` replacing the
  hand-written `ok` at five call sites). **Corrected a stale count unrelated to this leaf but wrong
  on a file this leaf changed:** the `base.py` row claimed `PUBLIC_TOOLS` is 54; it is 58, and it
  matches `PUBLIC_TOOL_RESPONSE_MODELS` exactly (checked by importing both). Also recorded
  `RESERVED_TOOLS` as empty. Added two reference rows to the 2-column table. Verification metadata
  pinned until closeout stamps the L4 commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: added the **Where Registration Lives Now** section
  (the `@server.tool()` surface moved to the sibling `mcp/registration/` route, and the per-builder
  parameter-object table), corrected the `PUBLIC_TOOLS` invariant and the registration reference off
  `server.py`, and noted the wiring test. No builder's responsibility, response shape or refusal
  vocabulary changed. Verification metadata pinned until closeout stamps the L2 code commit.
- 2026-07-16T06:26+02:00 — 260714-ACPUI-L4 curator: documented the serving-owned optional roleless
  pair, immutable live launch truth, and `launch-conflict` to `launch-selection-invalid` mapping
  without retry or alternate spawn. Settings-owned role dispatch, exact shared opener, and durable
  brief/inbox delivery remain unchanged. Verification metadata remains pinned until closeout stamps
  the L4 code commit.
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: documented typed native role launch
  resolution, structural refusal, runner-side dynamic validation, provenance-only env, the
  no-synthesized-command rule, explicit custom-harness mappings, and the roleless temporal
  boundary. Verification metadata remains pinned until closeout stamps the L2 code commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed route impact for the accepted hosted cutover.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-10T22:18+02:00 — 260707-HFX2-L20 MCP-tools route impact: public consume keeps its
  terminal snapshot until compaction; the public response contract is unchanged.

- 2026-07-10T18:30+02:00 — No route impact: 260707-HFX2-L18 decomposed the existing
  `spawn_agent_session_payload` controller and added a plain-terminal regression to satisfy the
  strict CRAP gate; public tool names, payload/refusal shapes, settings-owned spend authority,
  pair arbitration, and this route's module responsibilities are unchanged.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17 MCP-tools route impact: threaded binding role through
  attach/spawn/expectation responses and pair-based retirement without changing settings authority.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15 MCP-tools route impact: documented bound-log spawn
  acceptance, isolated command verification, resolved/log provenance, and replacement-leaf
  expectations. Verification metadata remains pinned until closeout stamps the eventual L15 code
  commit.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 round-2 route impact: `operator_inbox.py` now treats
  completion/artifact posts as current-owner hierarchy signals and persists leaf/subject provenance;
  no public MCP tool name or request surface changed. Verification metadata remains pinned until
  closeout stamps the eventual L13 code commit.

- 2026-07-09T12:04+02:00 — 260707-HFX2-L10 route impact (spawn settings authority):
  `terminal.py::spawn_agent_session_payload` no longer treats caller `harness`/`model`/`effort`,
  direct launch/session controls, or spend-affecting env keys as a precedence rung. Those values
  refuse with `spend-override-unsupported` before any side effect; settings supply the spend chain
  and free-form launch/session controls. Module layout and public tool name are unchanged.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L10 commit.
- 2026-07-09T11:45+02:00 — No route impact: 260707-HFX2-L9 (supervisor redelivery cadence + signal
  throttling) changes `operator_inbox.py`'s delivery call to thread the configured supervisor
  redelivery floor through to hosted delivery — an internal parameter addition to an existing call,
  not a change to this route's public tool surface, response shape, or module responsibilities;
  detail lives on the file's own sidecar. Verification metadata pinned until closeout stamps the
  260707-HFX2-L9 commit.
- 2026-07-08T22:30+02:00 — No route impact: 260707-HFX2-L3 (paste injector hardening) changes only
  `terminal.py::_deliver_spawn_pastes`'s INTERNAL delivery mechanic (now routes through
  `serving.injector.deliver`, the one delivery path, instead of calling `TerminalPaster.paste`
  directly) — `spawn_agent_session_payload`'s public parameters, response shape, and every existing
  test assertion are unchanged; detail on the file's own sidecar.
- 2026-07-08T18:45+02:00 — 260707-HFX2-L2 route impact (supervisor sweep, R5, issue #15): the
  shared `base.py::_tool_payload` choke point gains a third attachment, `supervisorBanner`, surfaced
  on every public tool response when the serving daemon's supervisor sweep heartbeat has gone
  stale. No new tool, no module-layout change — see `base.py`'s own sidecar for the exact call
  shape. Verification metadata pinned until closeout stamps the 260707-HFX2-L2 commit.
- 2026-07-08T14:45+02:00 — No route impact: 260707-HFX2-L1 adds R1/R2/R4 field extensions and new expectation-row/routing calls inside `gates.py`/`operator_inbox.py`/`terminal.py` (each module's own sidecar documents the change); the route's module layout, tool registry, and facade contract are unchanged.
- 2026-07-08T02:43+02:00 — 260707-HFX-L8 route impact (seat lifecycle: retirement + live identity +
  turn-state, issues #12/#4): `terminal.py` gains two public builders, `session_retire_payload` and
  `session_rename_payload`; `base.py`'s `PUBLIC_TOOLS` grows to 54; the facade `__init__.py` and
  `server.py` registration/`models/tool_registry.py` all gain the matching entries (`SessionRetireResponse`/
  `SessionRenameResponse`). Retire authority (`serving.retire_policy.check_retire_authority`) is
  enforced in the builder, not the transport layer, consistent with this route's "deterministic
  behavior belongs in controllers/services" invariant. Verification metadata pinned until closeout
  stamps the HFX-L8 commit.
- 2026-07-07T23:55+02:00 — 260707-HFX-L6 route impact: `next_step.py`'s
  front-half role wording and the terminal/spawn role path now align with the architect-default
  developer-facing lifecycle, spawned backend orchestrators, and curator closeout seat; public tool
  registration and payload-builder boundaries are unchanged. Verification metadata pinned until
  closeout stamps the HFX-L6 commit.
- 2026-07-07T23:30+02:00 — 260707-HFX-L4 route impact: terminal attach/spawn payloads now normalize
  leaf refs through the task tree before catalog writes and spawn provenance, returning
  `leaf-ref-not-found` / `leaf-ref-ambiguous` refusals with the expected
  `<repo>/<master-folder>/<doc-id>` form; `leaf_ref.py` carries the shared refusal payload helper.
  Verification metadata pinned until closeout stamps the 260707-HFX-L4 commit.
- 2026-07-07T23:20+02:00 — 260707-HFX-L3 route impact: `terminal.py`'s spawn delivery is
  capture-verified (no more echo-confirm false success — the SF-1 blind seat); a False outcome always
  carries evidence (`deliveryCapture`, explicit `"(empty pane capture)"` marker when empty) and the
  capture also attaches on submit-failure.
- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application): `terminal.py`'s spawn builder became
  the knob resolution + application seam (rolesPerLevel via the new `level` parameter,
  orchestration.harnesses effective registry, per-harness dispatch-time model/effort validation
  with the claude two-vehicle effort vocabulary, the free-form launchArgs/promptKeywords/
  sessionCommands escape hatch with provenance, session commands pasted before the brief), and
  `server.py`'s registration grew the matching parameters. Verification metadata pinned until
  closeout stamps the L16 commit.

- 2026-07-06T23:59:58+02:00 — L14 route impact (body): task_doc row notes the `orchestrates` field; terminal row notes the persisted `spawnRole`. Verification metadata pinned until closeout stamps the L14 commit.

- 2026-07-06T23:59:36+02:00 — 260703-L14 (visual hierarchy + chat grouping) route impact: `terminal.py`'s `spawned` payload now reports `spawnRole` (the AR_SPAWN_ROLE the opener persisted on the catalog row; omitted when `None`). Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-06T23:02+02:00 — 260703-L13 (settings unification): `terminal.py`'s
  `spawn_agent_session_payload` gained the settings-driven harness resolution seam
  (`_resolve_spawn_harness` + `_spawn_repo_root`; harness optional; refusals name the
  settings source); no other builder or the public tool set changed. Verification metadata
  pinned until closeout stamps the L13 commit.

- 2026-07-05T19:55+02:00 — 260703-L8 route impact (cycle 7, small): `lifecycle_gate` `wait=false` additionally requires a non-empty `enclosure` (the integrate guard's address; refused before any mutation, AR4-1a) — the `gates.py` row carries the requirement. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T19:25+02:00 — 260703-L8 route impact (cycle 6, owner follow-up): Layout table de-duplicated (the stale second `gates.py`/`operator_inbox.py` rows removed) and the live `gates.py` row brought to cycle-6 semantics (SEAM-kind-restricted validate-then-raise `wait=false`; `gate_list` ambient default). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T19:10+02:00 — 260703-L8 route impact (cycle 6, small): `lifecycle_gate` wait=false is now restricted to delegated SEAM kinds and validates BEFORE mutating (a refused raise persists no orphan gate and expires no sibling); `gate_list` defaults to the ambient lifecycle when no id is given (workspace only without an ambient). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T18:24+02:00 — 260703-L8 route impact (cycle 5, small): `lifecycle_gate` gains `wait=false` (raise-and-continue for policy-delegated kinds, returning the gateId); `gate_decide` resolves bare gate ids across lifecycles (GateStore.find) and refuses cli-attributed decisions on delegated kinds. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T16:32+02:00 — No route impact: next_step FRONT_HALF_RUNDOWN re-worded to the event-loop + ladder vocabulary (AR-13); strings only, no tool behavior change (260703-L8 cycle 4).
- 2026-07-05T01:32+02:00 — No route impact: next_step FRONT_HALF_RUNDOWN reframe bullet now names the orchestrator lifecycle (`l-01-agent-lifecycles` roles/orchestrator.md); string wording only, no tool behavior change (260703-L9).
- 2026-07-04T12:32+02:00 — 260703-L4 route impact: `gates.py` now handles
  policy-checked orchestration gate decisions with deciding role, no owner
  self-approval, and gate evidence refs. Verification metadata pinned until
  closeout stamps the L4 commit.
- 2026-07-04T12:31+02:00 - L3 route impact: added `orchestration.py` and
  `orchestration_nudge_manager`, while `operator_inbox.py` gained role/message
  metadata and optional hosted push delivery. Verification metadata pinned until
  closeout stamps the L3 commit.
- 2026-07-04T11:10+02:00 — L2 route impact: the `terminal.py` submodule gains the public
  `spawn_agent_session_payload` dispatch builder beside `attach_terminal_session_to_leaf_payload`;
  `base.py`'s `PUBLIC_TOOLS`, the facade, `server.py`, and `models/tool_registry.py` now
  expose/validate the agent-facing session-spawn path. It composes the shared serving opener +
  echo-confirmed paste (durable behavior stays in `serving/`; this builder stays transport-thin).
  Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-03T00:35+02:00 — L11 route impact: task_doc.py hosts task_reopen_payload; base.py advertises task_reopen next to task_doc.
- 2026-07-02T17:04+02:00 — L9 route impact: added the `terminal.py` tools submodule and public
  `attach_terminal_session_to_leaf` tool. `base.py`, the facade, `server.py`, and `models/tool_registry.py`
  now expose/validate the agent-facing hosted chat reassignment path. Verification metadata pinned until
  closeout stamps the L9 commit.
- 2026-06-27T22:00+02:00 — Task 28 (NOTIFY-AND-CONTINUE active turn end): the route
  now documents `lifecycle_turn_end_notification` as the active turn-end tool —
  `lifecycle.py` adds `lifecycle_turn_end_notification_payload(summary)`, `base.py`
  grew `PUBLIC_TOOLS` to 51 and gained the `_tool_payload` `awaiting-developer`
  auto-dismiss (name-guarded), and `next_step.py`'s ACTIVE hints
  (`decide`/`_gate_after`/rundown) repointed off `lifecycle_gate` onto it with a new
  `awaiting-developer` `nextTool=None` stop branch. The `lifecycle_gate`/inbox stack
  stays exported but parked (un-hinted). Hot Path Summary + Layout updated.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T20:16+02:00 — Task 27 follow-up: the `next_step.py` Layout row now
  records the gate-await behavior — a `blocked` lifecycle (a raised `lifecycle_gate`
  → `amb.block()`) returns the `lifecycle_resume` await hint, carrying the chain
  through the open gate. Verification metadata pinned until closeout stamps the
  code commit.
- 2026-06-27T18:43+02:00 — Task 27: added `next_step.py` (the lifecycle next-step
  engine) to the Layout; `base._tool_payload` now attaches the engine-computed
  `nextStep` to every active-lifecycle response (after the emission hook), and
  `lifecycle.py::lifecycle_start_payload` emits a one-time `frontHalfRundown`.
  Hot Path Summary and references updated. Verification metadata pinned until
  closeout stamps the task-27 code commit.
- 2026-06-26T18:43+02:00 — Regression fix: `gates.py` row now records that
  public `lifecycle_gate_payload` waits until a developer decision or
  gate-specific inbox response, and does not wake on stale lifecycle-scoped inbox
  rows.
- 2026-06-26T17:05+02:00 — Regression fix: `gates.py` row now records
  `lifecycle_gate_payload` as the public create+block+bounded-wait junction,
  not a wait-initialization junction.
- 2026-06-26T14:16+02:00 — Task 25: route overview now identifies `lifecycle_gate_payload` as the public gate junction and classifies split gate/block/wait builders as internal compatibility exports.
- 2026-06-25T14:02+02:00 — Task 24 reopened: `gates.py` now treats omitted `lifecycle_id` as the active ambient lifecycle for gate creation, rejecting lifecycle-less creation instead of producing workspace-shaped lifecycle gates.
- 2026-06-25T13:20+02:00 — Task 23/24: gate payloads now treat cancel/response-wait cleanup as deletion of throwaway interaction rows, and `gate_response_wait` owns the default five-minute wait loop.
- 2026-06-25T07:26+02:00 — Task 19: the gate tool surface gained `gate_response_wait`; `gates.py`
  now enforces one open lifecycle gate by expiring older open gates, supports targeted decision notes,
  and waits on both durable gate state and matching operator-inbox entries. Verification metadata pinned
  until closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: payload builders now expose `parent_task` and `leaf_id` on resolver/worktree entrypoints, while closeout/integration continue to use explicit leaf enclosure `series-contract.md` paths. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T22:50+02:00 — Dashboard task 14: added `lifecycle_finalize.py` to the route. `PUBLIC_TOOLS`, the facade, the server, and the response registry now include `lifecycle_finalize_task`. Verification metadata pinned until closeout stamps the source commit.
- 2026-06-23T13:44+02:00 — Task 10 backend inbox: added `operator_inbox.py` to the route and grew `base.py`/facade exports with `operator_inbox_post`, `operator_inbox_poll`, and `operator_inbox_consume`. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-19T07:23 — No route impact: slice 3c R5 threads a `dry_run` flag through the `task_doc.py` payload builder (forwarding only); the `mcp/tools/` route model this overview describes is unchanged (detail in the file sidecar). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T12:10+02:00 — Task 6 slice 6b: `gates.py` gained a non-tool helper `gate_decide_for_lifecycle` (the dashboard write-path the serving layer calls); the registered public-tool surface is unchanged (still 47 tools, no `PUBLIC_TOOLS`/registry edit), so the payload-builder route model this overview describes holds. Verification metadata pinned until closeout stamps the 6b code commit.
- 2026-06-18T01:05+02:00 — Task 6 slice 6a: new `gates.py` domain submodule (the four `gate_*` control-plane builders) added to the Layout; `base.py`'s `PUBLIC_TOOLS` and the facade exports grew to 47. The gate substrate itself lives in `controlplane/`. Verification metadata pinned until closeout stamps the 6a code commit.
- 2026-06-14T00:16 — Slice 3c commit 3: the `task_doc.py` Layout row now lists the master ops (`set_subtask`/`set_section`); the builder gained `subtask`/`section` forwarding. Verification metadata pinned until closeout stamps the 3c commit-3 code commit.
- 2026-06-13T22:34 — Slice 3c commit 1: new `task_doc.py` builder added to the Layout (the JSON-primary task-document authoring tool forwarding to the `task_doc_tools` controller); `base.py`'s `PUBLIC_TOOLS` and the facade exports grew to 43. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
- 2026-06-13T18:45+02:00 — No route impact: slice 2c only forwards a new `on_unsaved` argument through `lifecycle.py`'s `switch_lifecycle_payload` and `worktree.py`'s `worktree_attach_payload`; the payload-builder route model this overview describes is unchanged (detail in the file sidecars).
- 2026-06-13T16:41+02:00 — Slice 2b: new `lifecycle.py` domain submodule (the six `lifecycle_*` signal builders) added to the Layout; `base.py`'s `_tool_payload` gained the ambient emission hook and `PUBLIC_TOOLS` grew to 42. Verification metadata pinned until closeout stamps the 2b code commit.
- 2026-06-11T06:47+02:00 — Issue #62 worktree-only closeout: `worktree.py` dropped the two `direct_closeout_*` payload builders (Layout row updated to the current worktree verb set, including sync/abandon); `base.py`'s `PUBLIC_TOOLS` and the facade exports shrank to 36 names.
- 2026-06-10T09:56+02:00 — No route impact: sub-task D adds `worktree_sync_payload` (plus the `PUBLIC_TOOLS`/facade registrations) following the existing one-builder-per-tool pattern; the payload-builder route model this overview describes is unchanged (detail in the file sidecars).
- 2026-06-10T09:30+02:00 — No route impact: `tools/worktree.py` and `tools/core.py` only forward the new `stale_base_choice` / `include_freshness` arguments to their controllers (GitHub #54); the payload-builder surface this overview describes is unchanged.
- 2026-06-10T07:40+02:00 — No route impact: `tools/worktree.py` only forwards the new `retry_provider_setup` flag to the controller (GitHub #53).
- 2026-06-10T05:30+02:00 — Route body caught up with the 2.5.1/2.5.2 response-budget layer (compact builders per domain, tool-report filing, report-before-compaction and budget-test invariants); previous closeouts had only stamped the verification header. Developer-flagged gap.
- 2026-05-30T21:33+02:00: Re-verified the route against `8927f03` after the 0.9.x run; the per-domain Layout, hot path, and invariants still match the current exports. `core.py` gained `no_cache`/`install_provider_deps` forwarding in `runtime_install_payload` (documented on the file card); the registry's public surface is unchanged.
- 2026-05-29T18:35+02:00: Split `mcp/tools.py` (831 lines) into this `mcp/tools/` package by domain (commit `01f503d`); moved the registry purpose, invariants, and references here from the retired `tools.py.md`. Import surface unchanged.
- 2026-05-28T19:52+02:00: (from `tools.py`) Updated after all public payload builders were wired through the Pydantic response model registry and controller imports were split by domain.
- 2026-05-26T23:11+02:00: (from `tools.py`) Refreshed verification metadata after source commit `5ab704a` landed typed GrepAI payload forwarding.
- 2026-05-24T02:47+02:00: (from `tools.py`) Updated after public tool expectations added `memory_quality_check`.
- 2026-05-23T13:09+02:00: (from `tools.py`) Established for the complete Phase 04 public MCP tool surface.

## Update History


- 2026-09-20T05:55+02:00 — 260915-KS-L41 curator (uncommitted change set on `ar/260915-ks-l41-ar`, code base `756c47b3` at this leaf's cut and `f79f4db745ad00b908d6ce4871d0b4ab2320207c` after the L39 sync, memory base `da33325c` at the cut and `37d0787571bfbf92890049ee0614fa159012be39` after it): **added the L41 section, which is this route's own impact.** The section is new at the top of the route's change narrative and states the two builder-side changes: `knowledge_integrity_check_payload` now takes an exact-input selector (`_ExactInputSelector`, with `_run_for_scope` applying it as a binding rather than a preference, `_runs_in_scope` / `_run_identity` naming every run the scope holds, `_report_facts` composing all three non-success answers, and `_condition_report` naming the selected run beside the digest over its exact inputs and echoing the run's own route as the scope), and `knowledge_read_payload` now resolves the context's `(repository_root, code_tree_id)` pair through `_source_resolution` / `_current_code_tree` so a minimal schema-conformant read returns a view rather than raising the context model's incomplete-resolution refusal. The section also restates that the scope still selects and never borrows another scope's run, and that nothing in this module decides anything. The card carried no `reviewedWorkingCandidate` row; one was added naming this leaf's candidate. This card's verification metadata — `lastVerifiedCommitHash`/`lastVerifiedCommitDate` — is retained as recorded, because the candidate is uncommitted and the governed closeout owns the real stamp.

## 260915-KS-L44 The Read Request States What Owns The Knowledge Selection

**This route's impact is one docstring in `mcp/tools/knowledge.py`, and what it records is a finding rather than a new contract.** `ReadToolRequest` (`:106-135`) now states that `databasePath` and `repositoryId` **are** the knowledge selection and that the caller owns both: the runtime config's per-repository scope carries no knowledge-database or namespace field, a repository's coordination declaration (`context_packet`) and the memory layer's `system/settings.json` name roots, paths and policy but no knowledge database, namespace or `repositoryId`, no shipped helper or filename convention resolves a repository or a task to a knowledge SQLite path (`knowledge.db` appears only in test support), and the repository namespace is minted by ingestion (`create_repository`), so it is a fact about a store that already exists. The published schema keeps both **required** rather than optional-with-a-default, because a default here would be this surface inventing a selection; a cold planner that has not been told the pair cannot discover it from this server.

**Nothing was widened.** Exposing a real discovery contract — a settings key, a `context_packet` field, a resolver — is a product decision and is deliberately **not** taken by this leaf. The mounted builders, the refusal vocabulary, the source-resolution pair, the detection-run selection and the projection path are all unchanged; the docstring is the only edit at this surface.

## Update History
- 2026-09-21T12:40+02:00 — 260915-KS-L44 curator (uncommitted CYCLE-03 change set on `ar/260915-ks-l44-ar`, code base `2a96eb88`): **route body updated.** The section above is appended at the end of this route's change narrative, so no existing heading moved. It records this route's own impact — the read request's docstring now naming the caller as the owner of the `databasePath`/`repositoryId` selection, with the five observations that make that a fact (no config field, no coordination field, no memory-settings key, no resolver or filename convention, and a namespace minted at ingestion), the reason the schema keeps both required, and the explicit boundary that a discovery contract is a product decision this leaf did not take. No verification stamp was advanced; the candidate is uncommitted and the governed closeout owns the real stamp.
