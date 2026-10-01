# mcp/src/agents_remember/mcp/tools

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| sourceRoute            | `mcp/src/agents_remember/mcp/tools`            |

## Governing Overview

[overview.md](../../../../../overview.md)

## 260928-MIK-L37 A Projection Refuses A Seed A Converted Tree Does Not Hold

After the cutover (MIK-R37) every remembered database-era revision ID names nothing in a converted memory tree, and
an empty, complete answer would read as "no knowledge". So [`knowledge.py`](knowledge.py.md)'s `_project_result`
now takes its dataset from `_projection_selection`: for a converted tree, the first view seed the tree does not hold
(`knowledge_paging/tree_seeds.tree_seed_refusal`) refuses the whole `knowledge_project` as `selector_absent`, naming
where current seeds come from. `knowledge_read` gets the same refusal one layer down, in
`application/knowledge_paging/tree_read`. A database selection is unchanged, and this route's seam is unchanged.

- The projection's dataset, or the refusal of an unheld seed. [35]


## 260928-MIK-L01 The Family-Complete Leaf Read, And A Root With No Commit Refused By Name

A converted tree's `knowledge_read` with `view: "source_context"` and `sourcePath`, and every `leaf`
continuation, is now the family-complete leaf read (MIK-R01): `_read_result` still hands the read to
`knowledge_paging.tree_read.read_tree_page`, which routes it to `_leaf_response`, so this route's seam is
unchanged. It returns the same selection under the same `manifestDigest` as the `read_ar_files` block (rule 6),
the `invariant` view names its families in `families` (rule 7), and every refusal after the selection names the
memory tree (rule 9, ruling N3 of 2026-09-30 00:08:39). [`knowledge.py`](knowledge.py.md) changes in two
places:

- **A named `repositoryRoot` with no commit, or that is not a repository, is refused**
  `selected_input_unavailable` naming the root (`_NoCodeTreeError`, the obligation carried from L02 of
  2026-09-29 21:17:07); it used to raise a pydantic `ValidationError`. It applies to database and tree reads
  alike (review R1 N7: intended).
- **`knowledge_project` reads a converted tree's views whole** (`ProjectionOptions(whole_views=...)`, the L02
  Q7 obligation accepted by the ruling of 2026-09-29 23:21:57); a database projection is unchanged.

- The named refusal of a root with no code tree. [1]
- A converted tree's projection reads each view whole. [2]
- The leaf response the paged tree read routes to, for a path or (since MIK-R05) a family seed, a path's refusal carrying its route chain. [3]

## 260928-MIK-L02 A Read Of A Converted Tree Is A Bounded Page

`_read_result` in [`knowledge.py`](knowledge.py.md) hands a converted memory tree's read to
`application/knowledge_paging/tree_read.read_tree_page` (MIK-R02), so every such response is a page cut to the
shared token threshold, and its `continuation` is the shared token that also resumes a walk the
published-intent block of `read_ar_files` began. `_tree_extras` prepares the proofs and the currentness once
per page, so both count toward the threshold; `_ordering` applies the default only when `orderingInput` is
absent; every converted-tree refusal states `threshold`. The database path is unchanged: no page, no
threshold, and its `limit` still bounds the view (architect rulings of 2026-09-29: 19:56:40 Q4, Q5; 20:40:40
F1, F3, F8).

- The seam that pages a converted tree's read, and the per-page extras. [4]
- Converted-tree refusals state the threshold. [5]

## 260928-MIK-L03 A Read Of A Converted Tree Carries Its Currentness

`_read_result` in [`knowledge.py`](knowledge.py.md) now adds `currentness` for a converted memory tree whose
view was not refused (MIK-R03): each returned invariant's state at the code tree the caller named with
`codeTreeId` (since MIK-R02, the continuation's tree on a resumed page), computed once per page through
`knowledge_paging.currentness.WalkCurrentness`. Only `codeTreeId` is a request; a
`repositoryRoot` alone gives `unverifiable`, and `HEAD` is never used (architect ruling 2,
2026-09-29T18:42:37). The block is computed after the selection-failure boundary and degrades every failure
to `unverifiableReason`, so it never refuses the read (ruling N2, 19:13:41). The payload is unchanged. A
database read carries no `currentness`.

- The read's currentness, at the walk's code tree, prepared once per page with the proofs. [6]

## 260928-MIK-L08 The Integrity Check Returns A Leaf's Worklist

`knowledge_integrity_check_payload` in [`knowledge.py`](knowledge.py.md) now takes one
`IntegrityCheckRequest` and an optional `contractPath` (MIK-R08 rule 7). A dataset (`databasePath` with
`repositoryId`) is reported as before; a leaf alone gives a `reported` result without conditions; naming
neither is refused with `selected_input_unavailable`. When a contract is named, the result gains
`worklistState` and `worklist` from `application/knowledge_worklist/surface.leaf_worklist_fields`: the
latest worklist the leaf's memory-quality run or completed sync persisted beside its series contract. The
builder computes nothing and writes nothing. The dataset pair is optional for this tool only. No other
builder on this route changed; MIK-R26 reshapes the tool later.

- The request value and the routing, with the worklist fields. [7]

## 260928-MIK-L28 A Read Of A Converted Tree Carries Its Proofs

`knowledge_read_payload`'s `_read_result` in [`knowledge.py`](knowledge.py.md) adds an optional `proofs`
field (MIK-R28 rule 4): for an `invariant` or `family` view of a converted memory tree, the proof entries of
the invariant or of every family member, each `{id, invariant, path, anchor, facet, sidecar}`. It is read
through `application/knowledge_proofs.tree_view_proofs`, which opens the tree's index only for those two
views. **The additive optional field is accepted (architect ruling, 2026-09-29).** A database read and the
other three views carry no `proofs`, so the installed runtime's output is unchanged. A proof never states
that its test passed or that the invariant holds. `IndexMismatchError` joined `_SELECTION_FAILURES`, so an
index opened for the wrong key is the ordinary dataset refusal. No other builder on this route changed.

- A converted tree's page carries `proofs`, prepared once per page since MIK-R02. [8]
- A key mismatch is a selection failure. [9]

## 260928-MIK-L12 The Mounted Refusal Names The File Route

`knowledge_change_payload` still refuses every kind with `registration_absent`; its refusal detail gained one
sentence: on a converted memory tree (`knowledge/layout.json`) both shipped CLI entry points write knowledge
files through the curator file writer (MIK-R12) instead of the database. The tool stays registered and refusing
by architect ruling, until MIK-R26 (leaf L26). No builder, request model or other payload on this route changed.

- The refusal detail's new sentence. [10]

## 260921-ICR-L32 The Write Plane Is Named By Both Its Shipped Entry Points

The route's L20 paragraph above was **completed rather than replaced**: the mounted `knowledge_change`
refusal now names one writer and **both** shipped CLI entry points that reach it — `WRITE_ENTRY_POINT`
(`agents-remember knowledge-ingest`, a leaf enclosure's ordinary route) beside `TASKLESS_WRITE_ENTRY_POINT`
(`agents-remember knowledge-bootstrap`, a repository with no enclosure in scope) — and the module comment at
the top of `knowledge.py` says the same two, so the file no longer contradicts itself 20 lines below a
comment claiming both names are used wherever a model is told where the write plane is reachable. Nothing
else on this route moved: the same five builders, the same declared kinds, the same unconditional
`registration_absent` for every one of them. The second constant is `260921-ICR-L32`'s addition; the first
sentence was true when `ICR-R20@v1` wrote it and incomplete after `ICR-R29@v1` shipped the second route.

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

- The MCP adapter delegates completed-response ownership to the application. [11]
- The application attaches bounded guidance and records the completed result after finalization. [12]
- Wire validation and token finalization consume the enriched model in one serialization pass. [13]

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

## Evidence

### Repo-Internal References

- Public response model registry maps each tool name to a Pydantic model. [14]
- The checkpoint-landing name sits in the advertised tuple immediately after its integrate sibling, with the record-landing name next. [15]
- The stop's name sits in the advertised tuple immediately after its sync sibling, in the working half of the surface. [16]
- Schema tests assert public tool and response model coverage. [17]
- The external-chat inbox builders post, poll, and consume operator responses. [18]
- The lifecycle finalizer builder exposes the terminal task finalization tool. [19]
- The linear-half hint delegates to the worktree guidance state machine. [20]
- The supervisor heartbeat store + staleness-banner helper `base.py`'s choke point calls (260707-HFX2-L2 R5). [21]
- The `ResponseEnvelope` union and the two choke-point fields (`nextStep`, `supervisorBanner`) declared on both envelope bases. [22]
- The trusted terminal assignment response carries document-and-role binding plus private session correlation. [23]

Current working-candidate evidence for this route:

- The application request owner has only code and memory messages. [24]

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

- Lifecycle/adoption/legacy payloads — the enclosure-adoption payload builder was removed; lifecycle control now goes through `worktree_operation_control_payload`, and enclosure adoption survives only in the lifecycle-owned enclosure-adoption service. [25]

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

- The removed wait payload builder has no replacement; the surviving worktree builders still delegate the exact typed request and use the standard response wrapper. [26]

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

- The capsule builder re-shapes the flat declaration arguments into the application request record. [27]
- The two skill builders build a corpus request only when an override was supplied, so the shipped corpus is the default. [28]
- The declarations that call these builders, which pass no corpus override to the wire surface. [29]
- The capsule envelope carries its refusal in the same shape as a success. [30]
- The extension's enumeration surface is the `skills/list` method on the registration route, not a builder on this one. [31]
- This server's own index resource, kept deliberately distinct from that method. [32]

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
where the write actually happens — **one** writer, reached by **both** shipped CLI entry points
(`WRITE_ENTRY_POINT`, the `agents-remember knowledge-ingest` subcommand for a leaf enclosure's ordinary
route, beside `TASKLESS_WRITE_ENTRY_POINT`, the `agents-remember knowledge-bootstrap` subcommand for a
repository with no enclosure in scope) — because inventing a second write path here is exactly the
authority the requirement forbids this route to add. **The second name is `260921-ICR-L32`'s correction of
this route's own L20 sentence**: `ICR-R20@v1` named only `knowledge-ingest`, which was true when it was the
sole reachable entry point, and `ICR-R29@v1`'s second route left the naming incomplete in the one place a
model reads when it decides. `_projection_requests` builds one view request per requested view so
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

## 260915-KS-L44 The Read Request States What Owns The Knowledge Selection

**This route's impact is one docstring in `mcp/tools/knowledge.py`, and what it records is a finding rather than a new contract.** `ReadToolRequest` (`:106-135`) now states that `databasePath` and `repositoryId` **are** the knowledge selection and that the caller owns both: the runtime config's per-repository scope carries no knowledge-database or namespace field, a repository's coordination declaration (`context_packet`) and the memory layer's `system/settings.json` name roots, paths and policy but no knowledge database, namespace or `repositoryId`, no shipped helper or filename convention resolves a repository or a task to a knowledge SQLite path (`knowledge.db` appears only in test support), and the repository namespace is minted by ingestion (`create_repository`), so it is a fact about a store that already exists. The published schema keeps both **required** rather than optional-with-a-default, because a default here would be this surface inventing a selection; a cold planner that has not been told the pair cannot discover it from this server.

**Nothing was widened.** Exposing a real discovery contract — a settings key, a `context_packet` field, a resolver — is a product decision and is deliberately **not** taken by this leaf. The mounted builders, the refusal vocabulary, the source-resolution pair, the detection-run selection and the projection path are all unchanged; the docstring is the only edit at this surface.

## 260928-MIK-L23 A `databasePath` May Name A Converted Memory Tree

**Route meaning extended (MIK-R23@v1).** [`knowledge.py`](knowledge.py.md)'s read, diff and project builders
now pass every caller-selected dataset path through `_select`, the application's `select_knowledge_dataset`:
a path naming a converted memory tree (its root, or its published `knowledge.sqlite` location) is read
through the derived index of that tree's current state, and every other path is opened as before. The
responses gain the optional `memoryTree` (`memoryTrees` for a comparison) and `indexComplete`; a partial index
forces every completeness statement to `false`. `_SELECTION_FAILURES` makes an index that cannot be built a
refusal (`snapshot_unavailable` naming the tree) on all three handlers. No input schema changed. A tree-backed
read is bound to the index's constant namespace, so seeds are its projected UUIDs.

- The shared selection and its refusal mapping, which since MIK-R01 also refuses a named root with no code tree by name. [33]
- A partial index is never presented as complete. [34]
