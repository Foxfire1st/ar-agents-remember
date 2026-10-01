# mcp/src/agents_remember/mcp/registration/worktrees.py

## Governing Overview

[registration route overview](overview.md)

## 260731-EFA-L8 Change

The tool-registration functions gained bare-`*` keyword-only signatures (the 19
PLR0917 fixes across `mcp/registration/*.py`); the rule stays enabled and call sites
already pass keywords. Registered tools are unchanged.

## Purpose

`register_worktree_tools(server, config)` declares the **working half** of a worktree-backed task:
`worktree_start`, `worktree_attach`, `worktree_status`, `worktree_sync`, and — since
260831-LOCR-L37 — `worktree_pause`. The landing half (closeout, integrate, cleanup, abandon) is a
separate family in `closeout.py`, and `worktree_checkpoint_landing` — the explicitly requested
**publication** of an unfinished master — belongs to that half, not this one. The module docstring
says "create, re-attach, observe, sync, stop" for exactly that reason.

## Code Commentary

### Logic

`worktree_start` is the widest declaration in the family and splits into the three parameter objects
its application entry point takes — who the task is, what it is cut from, and how the start runs:

- `TaskIdentity(repo_id, task_name, worktree_name, leaf_id, parent_task, workflow_kind)` —
  `workflow_kind` defaults to `light-task` (the other value is `chat-task`).
- `TaskBases(source_branch, work_branch, memory_mode, memory_choice, stale_base_choice)`.
- `StartExecution(dry_run, skip_provider_setup, retry_provider_setup)`.

Its docstring carries two contracts that are invisible in the types. The **stale-base preflight**:
a start refuses when the source branch is behind or diverged from its remote tracking branch, and
the blocked `choose_stale_base_recovery` result is cleared by re-running with
`stale_base_choice='fast-forward'` or `'proceed-stale'`. And the **async provider setup**: start
returns within seconds with the providers block reporting `starting` plus a `progressFile`; the
caller polls `worktree_status` until a terminal state (a seed copy takes seconds, a refused seed
falls back to a full reindex flagged `seedFallback`), and re-runs with `retry_provider_setup=true`
after a failed or stale setup.

`worktree_attach` and `worktree_status` both pack their five locators into a `TaskRef` — the same
bundle `resolve_context` uses. Attach is read-only (it mutates no git) and takes `on_unsaved`
(`save` promotes an unsaved fleeting lifecycle, `discard` abandons it) to clear the save gate.
Status reports phase, dirty flags, next-step hints, and the live provider-setup block.

`worktree_sync(contract_path, memory_sync_choice, resolution_action, dry_run)` forwards flat with
shared `Literal` types. Its help now describes retained code/chosen-memory conflicts: the agent
resolves and stages in the reported worktree, then calls the same contract with
`resolution_action='continue'`, or restores pinned pre-sync heads with `cancel`. It does not expose
an operation id or promise abort-on-conflict behavior. `skip-memory` is an admission/preflight
choice, not a way to change an already-running generation.

### Invariants And Boundaries

- Flat signature, packing in the body — `TaskIdentity`/`TaskBases`/`StartExecution` and `TaskRef`
  belong to the application entry point boundary.
- `worktree_start` and `worktree_sync` are mutating and register `dry_run=False`; `worktree_attach`
  and `worktree_status` are read-only and take no dry-run flag.
- Contract creation, git mechanics, provider setup, and lifecycle promotion live in
  `application/worktree_tools.py` and the `worktrees/` package.
- Registration publishes the shared closed memory-choice/continue/cancel vocabulary; no free-string
  compatibility parameter or alternate sync tool is registered.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

### Repo-Internal References

- The stop declaration: single flat `contract_path`, registered description carrying the pause/publish-nothing/hand-back contract and naming the separate publication. [1]
- **The public sync declaration: typed memory choice, contract-addressed continue/cancel, and the flat `knowledge_resolution` argument whose description carries the engine's diagnosis and both decisions' meanings.** [2]
- The start payload forwards task identity, bases and execution configuration to the application owner. [3]
- The attach payload forwards the requested worktree attachment to the application owner. [4]
- The status payload reads status through the application owner. [5]
- The sync payload forwards the paired resolution value to the application owner. [6]
- The identity parameter object `TaskIdentity` (repo_id, task_name, worktree_name, leaf_id, parent_task, workflow_kind defaulting to `light-task`), defined in the application request boundary. [7]
- The bases parameter object `TaskBases` (source_branch, work_branch, memory_mode, memory_choice, stale_base_choice), defined in the application request boundary. [8]
- The execution parameter object `StartExecution` (dry_run, skip_provider_setup, retry_provider_setup), defined in the application request boundary. [9]
- `TaskRef` — the shared task locator attach and status pack. [10]
- **The pairing this registrar performs, and the vocabulary the decision is typed by.** [11]

### Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned registration surface.

## L23 Final Candidate Disposition

Public worktree registrations remain task-addressed and immediate-returning. Durable operation
identity, candidate trees, worker processes, and recovery state stay behind the application/service
boundary and are not added to the tool schema.

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## 260821-CLIVE-L2 Current Contract

The current source seams include `register_worktree_tools`. The public schema/composition layer exposes task-addressed controls plus explicit legacy and enclosure-adoption routes without private operation ids. Registration and payload building do not own journal state or compatibility decisions.

### Reconciled Source Evidence

- The current module exposes `register_worktree_tools` at this ownership boundary, re-read and re-cited at the current declaration. [12]

## 260821-CLIVE Stable-Address Registration Contract

Registered help now makes the address chain explicit: start reserves the configured contract
address and enclosure manifest before exposing work; attach resumes only through that exact locator
and never scans task/worktree/report paths; status resolves the independent locator and then either
the live root journal or exact terminal archive/receipt. Conflicting reservations and invalid
terminal proof fail closed, with no inferred enclosure-root fallback.

## 260831-CCR-L15 Status-Wait Server Tool

**Superseded for the registration surface.** L15 added a `@server.tool()` `worktree_status_wait`
here, dispatched to `worktree_status_wait_payload`. Neither exists on this route today: the tool is
not registered, no payload builder remains, and the name is absent from `PUBLIC_TOOLS` and
`TOOL_RESPONSE_MODELS`. What survives is the response model
`models/worktree.py::WorktreeStatusWaitResponse` (operation literal `worktree_status_wait`) — a
declared wire shape with no live registration. This card records the current state rather than the
L15 state, because the L15 paragraph would otherwise assert a registered tool a caller cannot reach.

## 260831-LOCR-L37 Stop Registration

`_register_worktree_stop_tools(server, config)` is the fourth registrar in the family and declares
one tool, `worktree_pause(contract_path)`. `register_worktree_tools` calls the four in order: start,
address, observation, stop.

The registered description is the whole public contract an agent reads, and it says the three
things a stop must say: that it **PAUSES an atomic master** and hands control back to the developer;
that it **publishes NOTHING** — no ref move, no commit, no landing, no ledger row — while releasing
the master's atomic-series activation selection and leaving its code and memory work branches,
worktrees, enclosure and every unstarted leaf exactly as they were; and that the result **proposes no
next step**, so resuming is the normal attach/start route rather than a pause verb. It names
`worktree_checkpoint_landing` as the separate, explicitly requested **PUBLICATION** and states that
pausing never does that.

The signature is flat and single-argument (`contract_path`), like every other tool on this route, so
the published JSON schema stays a flat object. `mcp/tests/test_tools.py` pins this wording.

**Two verbs, two registrars, two halves.** This file registers the stop; `closeout.py` registers the
publication. Neither is reachable through the other, and the split is the point: before L37 an agent
that wanted to stop a master found only a protected-branch publication under the name it reached for.

## 260915-KS-L40 The Authored Sync Resolution On The Public Surface

**`worktree_sync` gained a third argument, `knowledge_resolution: AuthoredReconciliation | None`**, and the published description is where an agent learns the whole recovery. The signature stays **flat** — `contract_path`, `memory_sync_choice`, `resolution_action`, `knowledge_resolution`, `dry_run` — because on this route the signature *is* the published JSON schema, so the decision is advertised as its own argument rather than as a nested object. The registrar pairs the two into the one `SyncResolutionInput` the payload layer takes before forwarding, which is also why the pairing is visible here and only here.

The description now carries the diagnosis as well as the action: a retained *knowledge dataset* conflict is reported **with the engine's own diagnosis** — the table, the operation and the exact row it refused, plus the action it advertises — and is settled by authoring one decision for that row, `resolution_action='reconcile'` with `knowledge_resolution={table, record_id, decision}`, where `decision` is one of the conflict's advertised decisions. Both meanings are stated in prose (`keep-left` retracts the arriving change so the stored value stands; `keep-right` applies it over the stored value) because an agent that has to read the enum's source to choose has not been told what it is choosing. The merge then continues in the same call. No registrar, tool name, registration order or advertised count changed.
