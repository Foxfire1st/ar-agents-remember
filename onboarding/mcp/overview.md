# mcp/ — MCP Package Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| sourceRoute            | `mcp/`                                     |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-07-04T23:43+02:00 |
| lastVerifiedCommitHash | `0347c7e627c0278c29a9c72d0a3494d65638d7f8` |
| lastVerifiedCommitDate | 2026-07-05T18:02:19+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`mcp/` is the package-managed Agents Remember MCP server. It turns coordinator
startup and provider lifecycle behavior into typed, host-side operations backed
by importable Python services instead of model-edited coordinator scripts or
coordinator `system/settings.json`. The tool surface gained `task_reopen` (L11):
reopen a fully landed leaf task under its exact leaf id — a task-domain state reset
whose worktree recreation stays with `worktree_start`. The agent-orchestration L2
adds `spawn_agent_session` — the agent-facing **dispatch** tool that CREATES a
role-configured, leaf-attached, context-primed hosted session by composing the
existing serving primitives (the shared session opener + optional leaf attach with
server-arbitrated `leaf-taken` + an echo-confirmed context paste with optional
submit), injects the model/effort/env role knobs at spawn, and records spawned-by
provenance — so orchestrators spawn managers and managers spawn workers without
dashboard clicks. The package-data runtime skill mirror now carries the L5
super-integration doctrine for orchestrated series: super branches from main,
masters branch from super, leaves branch from masters, C-11 carries every edge,
the orchestrator integrates completed masters from a super-sourced worktree, and
the final super-to-main PR is followed by main-memory carry-over and push. L6
sharpens the same runtime skill mirror's adversarial review procedures: managers
spawn master-exit reviewers, orchestrators spawn super-exit reviewers, verdicts
land in series `notes/reports/`, and the handover gate carries
`reviewer-verdict` evidence refs that L4 policy may require. Since L12 every managed
provider container carries an explicit compose memory cap (watchers 512m,
falkordb/ollama 2g, runner 1g, postgres 512m) with self-recycling OOM behavior.

## Hot Path Summary

Start in `src/agents_remember/mcp/config.py` for trusted settings parsing,
`src/agents_remember/mcp/server.py` and the `mcp/tools/` package for exposed
MCP tools (`server.py` installs `mcp/compact_content.py` to minify tool-result
text; verbose tools additionally file bulk diagnostics under
`temp/tool-reports/` via `mcp/tool_reports.py` and return compact outcomes
with a `reportPath`), `models/tool_registry.py` for public response contracts,
`controllers/context_packet.py` for compact `ContextPacketV2` startup packets,
and `controllers/runtime_install.py` plus `install/runtime.py` for MCP-owned
runtime installation. Provider status is composed in `providers/status.py`; the serving/observer path can
refresh the persisted provider current-state snapshot before live dashboard projection so provider rows are
not limited to the last explicit diagnostics/status command.
provider lifecycle settings are generated from MCP settings in
`providers/settings.py`. Provider lifecycle implementation is now split between
the `providers/lifecycle/` facade/shared helpers and provider-owned
`providers/cgc/lifecycle/` plus `providers/grepai/lifecycle/` packages; there
is no legacy `provider_lifecycle.py` facade. Memory-layer quality control lives under
`src/agents_remember/memory_quality/`: integrity checks include the onboarding
drift classifier/summary, and style checks currently include update-history
newest-first ordering. Shared onboarding-document parsing, route-overview discovery, and the
"meaningful body vs metadata/history" change classification live in
`kernel/onboarding_doc.py`; the closeout body gates in
`worktrees/modules/onboarding.py` consume them and accept explicit
`No content impact:` / `No route impact:` Update History markers as in-band
reviewed-no-impact attestations. Branch freshness (issue #54: is a local
branch current with its upstream, plus ahead/behind counts) lives in
`kernel/git_freshness.py` beside `kernel/git_facts.py`; the `context_packet`
controller surfaces it as the opt-in `include_freshness` packet section
together with a `ledgerMapsCodeHead` check, forming the lifecycle-start
staleness checkpoint. Branch-memory carryover
(`memory/carryover.py`) plans route-overview candidates beside file sidecars
(route-keyed, never auto-carried when content differs), regenerates
official-side route indexes after a carry, guarded on a clean official-ref
checkout, and fast-forwards memory `main` to the official checkout tip
(`memory_main_advance`, issue #54) so non-main cycles no longer leave memory
main behind. Worktree lifecycle finalization lives in
`worktrees/modules/finalize.py` and is exposed as `lifecycle_finalize_task`;
it proves the landed commit is reachable from the contract's local
target/source branch, checks memory carryover, runs or verifies cleanup, and
reconciles JSON-primary task documents after landing. Runtime package data under
`src/agents_remember/package_data/` is synchronized from canonical root runtime
asset folders by `scripts/sync-runtime.py`, and the sync behavior is covered by
`mcp/tests/test_sync_runtime.py` plus the pre-commit check. The built dashboard cockpit
ships under `package_data/dashboard/`, synced from `dashboard/dist/` by
`scripts/sync-dashboard.py` (slice 05 replaces the slice-04 placeholder with the real
Vite/React bundle), covered by `mcp/tests/test_sync_dashboard.py` plus the
pre-commit/pre-push and CI `--check`.

## Route Model

The MCP package separates three surfaces:

- `agents_remember.mcp` owns transport wiring, tool registration, and trusted
  settings parsing.
- `agents_remember.controllers` owns operation-level composition such as
  `context_packet`, provider tools, worktree tools, memory tools, benchmarks,
  and `runtime_install`.
- `agents_remember.models` owns public MCP response contracts and the
  tool-to-response-model registry used by the `mcp/tools/` payload builders.
- First-class service domains such as `kernel`, `providers`, `memory_quality`,
  `worktrees`, and `install` own deterministic behavior.
- `agents_remember.observer` owns the observable-lifecycle **event substrate +
  projection** (the 3.0 browser-dashboard direction): the append-only
  `ar-observer-event/v1` log, local ULID minting, the per-lifecycle event store,
  the ambient lifecycle + six `lifecycle_*` signal tools (with the `_tool_payload`
  emission hook attributing every tool call), and the **projection read side**: the
  pure reducer that folds the logs plus file snapshots into the resolved state tree
  — the structural surfaces (slice 3a) plus the slice-3b analytical surfaces (drift
  read from a persisted snapshot, sidecar staleness, setup, route coverage, tool
  reports, ledger), the derived rollups, and — slice 05 — the server-computed
  **attention queue** (`build_attention_queue` → the derived `Analytics.attentionQueue`), plus —
  slice 05 (5c) — paused **persistent lifecycles** synthesized from worktree contracts,
  **per-worktree provider stacks** (surface 4, bound to worktree/repo/role), Task 12's repo-covered
  workspace provider nodes (CGC watcher rows and GrepAI configured `targetRepos` become repo satellites;
  GrepAI `targetRepos` are addressable project targets inside one aggregate provider instance, not
  separate per-repo provider processes, while providers without explicit target evidence stay aggregate),
  and the **full task content** on
  `TaskDocNode` for the in-dashboard task reader. Task 29 adds lifecycle-aware raw-event lifetime
  handling and projection freshness hygiene: terminal lifecycle `events.jsonl` logs are physically
  pruned after the post-completion grace window, fresh raw-event SSE connections start from retained
  offsets instead of replaying all history, projection reads cache repo surfaces briefly, and worktree
  provider/runtime projection admits only active enclosure-backed groups instead of parked or stale
  worktrees. Task 29 S7 adds actionable-drift provenance/dismissal and keeps raw Event River row
  lifetime at the backend retention boundary rather than a frontend count cap. Task 34 re-keys that
  raw-event retention on **inactivity** rather than termination: `event_retention.py` prunes a fleeting
  or enclosure lifecycle log after >1h with no real (non-heartbeat) activity (not on `lifecycle.ended`),
  `ambient.py`'s heartbeat ticker decays after ~10 min idle so a dormant log ages out, and `/api/events`
  does one retained-backlog scan per connect, filters `lifecycle.heartbeat`, and streams a bounded
  chunked backlog. Task 32 adds physical retention for persisted
  drift snapshots: cleanup deletes the exact code-worktree snapshot for the contract being reclaimed,
  and projection prunes valid deleted-worktree drift snapshots before reading the analytical surface.
  Task 33 adds the `WorkspaceProjection.activeWorktreeGroups` field (sourced from the same
  `active_enclosure_worktree_groups` admission the Engine Room uses) that the dashboard Topology consumes
  to bound its constellation to active worktree enclosures.
  Task 21 adds the folder-keyed master token aggregate:
  `SeriesNode.seriesTokenTotal` is composed from projected sibling leaf task docs and lifecycle token totals.
  Slice 05l Part 1 (backend teardown
  visibility) extends the Engine Room surface: the reducer now projects the `abandoned` worktree
  phase (from `worktrees/modules/guidance.py`) and **drops disposed** (cleaned-up/abandoned)
  enclosures from the active `engineProcesses` so the frontend (05k) animates the teardown.
  Slice 05l Part 2 hardens the **landing-arc probe** (`worktrees/modules/landing.py`) so the
  dashboard follows a REAL remote landing: the protected target `origin/<base>` is probed **directly**
  via `git ls-remote` (visible across the whole landing window before any PR and even when `gh` is
  absent), and the PR ref carries gh's open/merge timestamp on the additive `LandingRefNode.at`.
  Slice 05m lands **carryover-before-cleanup** lifecycle correctness in `worktrees/modules/`
  (`guidance.carryover_done` reads the official ledger; `lifecycle_guidance` routes a
  `carryover-pending` phase before `cleanup-pending`; `cleanup_result` hard-refuses cleanup until the
  parked memory is carried home), and the observer reducer now follows it — `_GUIDANCE_PHASE` projects
  `carryover-pending` and the engine-room node carries the display-only `carryoverDoneAt` milestone
  (5k renders the seam). Task 13 corrects cleanup's branch and dry-run preview rules in the same
  worktree domain: task work branches are deleted only after explicit reachability proof against the
  contract source branch, and dry-runs classify worktree group directories after planned
  worktree/provider-runtime removals. Task 14 narrows cleanup to the finalized child edge: cleanup
  retires task work branches only and preserves parent/source branches for their own lifecycle edge.
  Task 23/24/L3 adds the interaction-retention read side: gate logs and operator-inbox rows are treated as
  disposable interaction records, `read_gates` can TTL-compact them, and `AgentPickupNode` projects
  pending inbox entries as waiting-for-agent/check-chat feedback for the dashboard, including L3
  sender/recipient role, message kind, artifact, and hosted-delivery metadata.
  The series-contract resolver helpers in `worktrees/task_resolver.py` now own task-name lookup,
  nested parent-task disambiguation, leaf `enclosures/<leaf-id>/series-contract.md` paths, archive
  exclusion, and root-task archival into `tasks/<repo>/0_archive/`.
  Slice 09 (gate-signal
  adoption) removes the dirty-tree → `commit-approval-pending` branch from
  `worktrees/modules/guidance.py` (a visibility bug): a dirty worktree now projects its honest
  lifecycle-position phase (closeout-completed → `integration-pending`) rather than a fabricated
  commit-approval gate — the commit gate is owned by the closeout preview / a raised
  `closeout-approval` gate, never `git status`. Task 27 adds the **lifecycle
  next-step hint engine** ([next_step.py](agents-remember/mcp/src/agents_remember/mcp/tools/next_step.py)):
  a `NextStep` hint computed from the projected lifecycle state (phase +
  worktree-contract sub-state) and attached to EVERY tool response at the same
  `_tool_payload` choke point that emits the lifecycle events — the front half
  is a one-time prose rundown emitted by `lifecycle_start` (`frontHalfRundown`)
  plus a stable pointer, the linear half delegates to the worktree
  `guidance.lifecycle_guidance` state machine and overlays a gate-raise hint
  (`lifecycle_gate(kind=…)`) at the gate moments, and a terminal `lifecycle_end`
  returns a loop-back hint — generalizing the worktree-only guidance to the
  whole lifecycle spine. Task 28 introduces the **NOTIFY-AND-CONTINUE turn-end
  model**: a new non-terminal `awaiting-developer` lifecycle state
  (`observer/lifecycle_state.py` + `ambient.await_developer`/`resume_from_await`)
  and the public `lifecycle_turn_end_notification(summary)` tool (notify + stop,
  no wait/inbox) become the **active** turn-end path, the `_tool_payload` choke
  point auto-dismisses `awaiting-developer` on the next tool call, and the
  next-step hints (`decide`, the closeout/integration/cleanup overlays, the
  front-half rundown) are **repointed** from `lifecycle_gate` to it; the
  `lifecycle_gate`/`operator_inbox_*` stack is **parked** — kept and valid, but no
  longer hinted as turn-end choreography (the gate-open/blocked-gate double-emit is
  also fixed with a one-line reducer dedup). Task 30 updates the worktree closeout behavior at the
  package level: a re-closeout after a completed integration may reopen the
  integration state when new code or memory content is not yet on the source
  branch, while a clean no-op re-closeout preserves the completed integration
  markers. It is a service domain
  with its own route overview. See `docs/design/observable-lifecycle.md`.
- `agents_remember.worktrees.modules.finalize` owns the terminal
  `lifecycle_finalize_task` operation for one parent-child branch edge. It
  depends on completed closeout/integration/carryover facts, uses local Git
  ancestry against the contract source branch for both direct and PR-gated
  edges after the target branch is pulled, avoids squash-merge equivalence, and
  updates only the supplied leaf task plus immediate parent row after cleanup.
- `agents_remember.tasks` owns the **JSON-primary task document**
  (`ar-task-document/v1`): the persisted schema, the deterministic markdown renderer,
  and the JSON+md store; the `task_doc` MCP tool authors documents and the observer
  projects active JSON task docs with optional lifecycle context (slice 3c; closes note-03 gap #8).
  `task_doc` also exposes a schema-validated full-document `replace` operation for task
  resets/replans that need to rewrite structural arrays such as steps, examples, and decisions. Task 21
  adds same-root leaf-to-master row sync and batch leaf/master persistence for `task_doc` writes.
  A service domain with its own route overview.
- `agents_remember.serving` owns the **dashboard serving layer** (slice 04): a FastAPI
  app over the observer projection — one shared projector ticking `project_and_write`, a
  multiplexed `state` SSE stream (snapshot + per-entity deltas via `serving.delta`), a
  one-shot state endpoint, a raw `event` SSE channel with byte-offset resume
  (`serving.events`) plus a Task 29 S7 `ready` event after retained raw backlog replay, a
  `POST /api/actions/{action}` plane that records targeted gate-decision verbs as
  developer-attributed gate decisions (including stale-gate and rejection-note handling), allows
  gate-id-only `cancel` to delete stale workspace-shaped gate rows, and
  acknowledges lifecycle transitions without mutation and persists targetless actionable-drift dismissals
  (`serving.actions`), `POST /api/operator-inbox` for trusted developer/dashboard writes into
  the external-chat operator inbox, sim-mode replay over the projector's clock/feeder seams
  (`serving.sim`), and the static
  cockpit mount. Transport only (no interpretation), reading through `McpRuntimeConfig` +
  `observer.paths` (NS #5); launched by `agents-remember dashboard` (the umbrella
  `agents-remember` CLI under `cli/`; 260703 L1 makes `--config` optional there —
  `cli/discovery.py` walks upward from the working directory, the settings convention before an
  `.mcp.json` registration's recorded path, nearest wins, semantically probing usability so the
  repo's tracked placeholder template never shadows real settings). 260703 L2 adds **daemon
  supervision** (`serving/daemon.py`): `--daemon`/`--status`/`--stop` on the same CLI (state under
  `<coordinationRoot>/logs/dashboard/`; `--port` defaults from the new fail-loud `dashboard`
  settings object), and `dashboard.autoStart` makes every `agents-remember-mcp` boot ensure the
  daemon — adopt healthy, spawn absent, restart on version mismatch — via the threaded, total,
  stderr-only `maybe_autostart_dashboard` hook in `mcp/server.py` `main()`. Slice 6d-1 adds the **Mode B2 terminal host**
  (`serving.terminal`): a registry of tmux-wrapped stdlib-`pty` sessions that launch the harness
  render-not-scrape (fixed-argv, OS-user creds, localhost), opened by the
  `POST /api/terminal/{session}` opener (6e-2a/6e-2b — the dashboard spawns + owns a shell or a detected
  harness; `serving.harnesses` + `GET /api/harnesses` drive the per-harness launch buttons) and served
  over the `/api/terminal/{session}` WebSocket bridge (`serving.app`, slice 6d-2; the `websockets`
  core dep), with the xterm.js visual in 6e. Slice 6f hardens delivery into a session — the host strips
  Ctrl-Z for bare-pane harnesses, and `POST /api/terminal/{session}/image` (the `python-multipart` dep)
  carries a pasted screenshot by saving it under the session cwd for path-injection. Task 22 adds the
  durable dashboard terminal catalog (`serving.terminal_catalog`, persisted under
  `logs/dashboard/terminal-sessions.json`), `GET /api/terminal/sessions`, WebSocket rehydration of
  cataloged tmux sessions after server restart, stale-row exit marking, `POST
  /api/terminal/{session}/terminate`, and image-upload cwd fallback through the catalog. Task 22
  follow-ups keep that catalog durable across browser refresh and multi-tab use: openers create
  detached tmux sessions, each WebSocket attaches its own tmux client, browser disconnects detach
  non-destructively, and explicit termination stays hidden across later exit bookkeeping. L9 adds the
  shared `serving.terminal_leaf_assignment` move policy and the public
  `attach_terminal_session_to_leaf` MCP tool so an agent can move its hosted chat's durable `leafKey`
  through the same catalog uniqueness rules as the dashboard attach route. Agent-orchestration L2 adds the
  shared `serving.terminal_opener` (the single hosted-session opener the `POST /api/terminal/{session}`
  route and the agent-facing `spawn_agent_session` MCP tool both compose — no parallel spawn path) plus
  `serving.terminal_paste` (server-side echo-confirmed stdin paste, backing a new
  `POST /api/terminal/{session}/paste` endpoint and the tool's context delivery); `serving.terminal` gains
  a `tmux new-session -e KEY=VALUE` env knob-injection seam and `serving.terminal_catalog` gains spawned-by
  provenance columns. A service domain with its own
  route overview.
- `agents_remember.controlplane` owns the **gate control plane** (task 6): the durable,
  append-only `ar-gate-record/v1` `GateRecord` + `GateStore` (co-located with the observer
  event log under `observer_root`) and the five `gate_*` MCP tools (`mcp/tools/gates.py`)
  (slice 6a), plus the **enforcement policy** `enforcement.py` (slice 6b/L4): a
  `closeout-approval` gate, once developer-approved or approved by a configured
  delegated orchestration role, binds `worktree_closeout_apply` server-side (a
  model self-approval and an owner lifecycle self-approval are rejected; gateless
  lifecycles keep the chat commit gate). L4 adds `gate_policy.py`, default
  all-human settings, human-pinned integration/push/cleanup gates, and
  reviewer-verdict evidence refs for delegated approvals. Slice 09 extends `GateKind` to the full l-01
  gate spine (`plan-approval` / `worktree-intent` / `closeout-approval` / `push-approval` /
  `integration-approval` / `cleanup-approval` / `agent-question` / `provider-retry` /
  `alarm-ack`) — `closeout-approval` IS the commit gate (no separate `commit-approval`).
  `mcp/server.py` now advertises `lifecycle_gate` as the public agent-facing junction for this
  spine: it creates the typed gate, blocks the active lifecycle, waits for a developer decision or gate-specific inbox response,
  and forwards `required_decision`; the older split gate/block/wait helpers remain lower-level
  internals rather than normal public choreography. Task 28 **parks** this whole gate/inbox
  turn-end choreography behind the new NOTIFY-AND-CONTINUE `lifecycle_turn_end_notification` tool:
  `lifecycle_gate` stays registered and the durable-gate stack stays valid, but it is no longer the
  hinted turn-end path. Task 19 adds the single-current-gate invariant (new lifecycle gates
  append `expired` snapshots for older open gates), while dashboard/operator-inbox paths continue to
  provide the developer-attributed response side.
  Dashboard
  *projection* of gates is live. Task 10/L3 adds the durable operator/agent inbox
  in the same service domain: `OperatorInboxEntry` / `OperatorInboxStore`
  queue ask+response entries addressed by lifecycle, external agent, or recipient role, while
  `operator_inbox_post` / `operator_inbox_poll` / `operator_inbox_consume` expose the
  backend mailbox for chats the dashboard cannot inject into and for agent-to-agent messages that can
  also be pushed into hosted sessions. The dashboard serving layer's `POST /api/operator-inbox`
  endpoint writes the same entries with developer/dashboard attribution and L3 adds hosted push
  delivery through `serving.inbox_delivery`; `orchestration_nudge_manager` records/rate-limits nudges
  and queues manager inbox rows. A service domain with its own route overview.

The trusted MCP settings file must be absolute and outside the coordinator root.
It supplies `coordinationRoot`, `workspaceRoot`, allowed repository IDs,
allowed provider IDs, timeout caps, optional orchestration gate delegation, and
optional repository contract paths. The
server derives repository roots, memory roots, provider runtime roots, provider
data roots, and provider log roots from those settings. Tool calls name allowed
repo IDs and boolean options; they do not pass arbitrary host paths.

Provider runtime layout now uses a provider runtime root plus a central log
root under the coordinator:

```text
<coordinationRoot>/
  providers/
    runners/
      codegraphcontext/
      grepai/
    data/
      codegraphcontext/
      grepai/
  logs/
    mcp/
    providers/
      codegraphcontext/
      grepai/
      setup/
      status/
```

The `runtime_install` MCP tool operation copies runtime package assets to the
configured coordinator root and can run provider dependency installation through
package-local lifecycle code. It generates lifecycle settings from MCP settings,
not coordinator `system/settings.json`; provider setup records image locks,
setup summaries, and provider-state files through the package lifecycle code.
Settings-backed `grepai-memory` is Docker-only: the complete stack is the
managed runner image/container, PostgreSQL/pgvector, Ollama, and their shared
Docker network, with no host GrepAI binary or host Ollama fallback. Managed
GrepAI auto host-port selection prefers `61432` for PostgreSQL and `61434` for
Ollama so the dashboard/provider stack does not claim common neighboring
developer-service ports `5432` and `11434`.

The package data that `runtime_install` copies is not edited as an independent
source of truth. Canonical runtime assets live at the repository root in
`agents-md-files/`, `benchmarks/`, `providers/`, and `system/`; the sync script
replaces the corresponding package-data folders and reports missing, extra, or
changed files in check mode.

## Invariants And Boundaries

- MCP settings are authority; coordinator files can teach the model what to ask
  for but cannot grant provider or path authority.
- MCP tool calls must not accept `coordinationRoot`, `sourceRoot`, provider
  runtime roots, or arbitrary filesystem paths.
- Provider install/status must use generated lifecycle settings from
  `McpRuntimeConfig`.
- Provider status reports watcher/current-state readiness and recovery actions;
  the prior runner-integrity gate was removed in the 1.0.0 remediation.
- `providers/runners`, `providers/data`, `logs/mcp`, and `logs/providers` are
  the active provider/runtime log layout; `providers/_bin`, `providers/_venvs`,
  `providers/<provider>`, and `provider-data` are not active runtime roots.
- CGC managed execution is Docker-runner owned; do not add host `venvRoot`,
  host `cgc` executable, or site-packages patch fallback paths.
- `grepai-memory` must remain Docker-or-bust in the MCP runtime; do not add
  host binary or host Ollama fallbacks.
- Resolver, provider lifecycle, memory quality, and worktree code under
  `mcp/src/agents_remember` is a package-local implementation surface. Original
  runtime scripts are not the MCP execution authority.
- Public MCP tool payloads should validate through
  `models.tool_registry.PUBLIC_TOOL_RESPONSE_MODELS`; compact context belongs
  in `ContextPacketV2`, and detailed provider state belongs in
  `provider_diagnostics`.
- Skipped provider details are still a modeled public contract: compact
  provider summaries report aggregate skipped state, omit provider detail rows,
  and rely on optional-null provider `ok` fields to survive JSON
  serialization/re-validation.
- On stdio transport the server's stdin/stdout ARE the JSON-RPC pipes:
  every `subprocess` call in the package must declare its stdin handling
  (`stdin=DEVNULL` or piped `input`), enforced by the
  `test_subprocess_hygiene.py` AST guard and the end-to-end stdio transport
  test (2.5.1, GitHub #49).
- Provider readiness is content-gated, not liveness-gated: global `ok`
  requires both running containers and actual graph/workspace content;
  healthy-but-busy targets surface in the compact summary's `indexing` list
  without degrading state (2.5.0).
- Long-running provider seed/clone operations are guarded by stall watchdogs
  (kill on zero progress), never by total-duration caps — copying index data
  instead of re-indexing is what makes rapid worktree provider deployment
  viable, and it scales with index size by design (2.5.1).
- Verbose tool responses are budgeted: bulk passthrough detail belongs in
  `temp/tool-reports/<tool>/` (keep-last-5 / 7-day write-time prune, secret
  redaction) with the compact inline outcome carrying `reportPath`;
  `test_tool_response_budgets.py` is the regression line (2.5.1/2.5.2).
- Long-running tool work must be observable, not silent: `worktree_start`
  returns within seconds and provider setup runs on a background thread that
  writes a durable, heartbeat-stamped `setup-progress.json` (`providers/
  setup_progress.py` + `worktrees/modules/provider_async.py`); `worktree_status`
  is the poll surface, a dead heartbeat projects as `stale`, and
  `retry_provider_setup` is the recovery path. The seed-refused→full-reindex
  transition is flagged as `seedFallback` the moment it happens (GitHub #53).
- In-container argv must be container-form: everything after `--` in a
  provider runner command executes inside the Linux container, so paths are
  rendered via `to_container_path` (`providers/context_common.py`) — host-form
  `C:/` paths fail silently into expensive fallbacks (GitHub #58).

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| MCP settings reject coordinator `system/settings.json`, forbid settings inside the coordinator, and derive provider runtime roots under `providers/runners/<provider>`. | [config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |
| The tool surface exposes `context_packet`, provider diagnostics, runtime, memory, worktree, benchmark, and install tools; handlers delegate to controllers and response validation flows through the model registry. | [mcp/tools/](agents-remember/mcp/src/agents_remember/mcp/tools/); [server.py](agents-remember/mcp/src/agents_remember/mcp/server.py); [tool_registry.py](agents-remember/mcp/src/agents_remember/models/tool_registry.py) |
| `server.py` installs a FastMCP shim that minifies the JSON text mirror of tool results without touching structured content. | [compact_content.py](agents-remember/mcp/src/agents_remember/mcp/compact_content.py) |
| `context_packet` composes resolver, git, worktree, compact provider summary, and optional drift and branch-freshness status into `ContextPacketV2`; detailed provider state is exposed by `provider_diagnostics`. | [context_packet.py](agents-remember/mcp/src/agents_remember/controllers/context_packet.py); [context_packet model](agents-remember/mcp/src/agents_remember/models/context_packet.py); [provider models](agents-remember/mcp/src/agents_remember/models/providers.py); [git_freshness.py](agents-remember/mcp/src/agents_remember/kernel/git_freshness.py) |
| `runtime_install` derives install target and provider settings from `McpRuntimeConfig` and calls package-local install/lifecycle services. | [runtime_install.py](agents-remember/mcp/src/agents_remember/controllers/runtime_install.py); [install runtime](agents-remember/mcp/src/agents_remember/install/runtime.py) |
| Runtime package data is synchronized from canonical root asset folders, and tests verify missing, extra, changed, and target-scope behavior. | [sync-runtime.py](agents-remember/scripts/sync-runtime.py); [test_sync_runtime.py](agents-remember/mcp/tests/test_sync_runtime.py); [pre-commit hook](agents-remember/.githooks/pre-commit) |
| The built dashboard cockpit bundle is synchronized from `dashboard/dist/` into `package_data/dashboard/` and gated by `--check` — the built-bundle digest **plus** a source-freshness fingerprint of the build inputs (the `src` tree minus tests + the production configs, recorded in a sibling `package_data/dashboard.fingerprint`), so a `dashboard/src` change shipped without a rebuild is flagged at the commit gate the way a changed skill is. | [sync-dashboard.py](agents-remember/scripts/sync-dashboard.py); [test_sync_dashboard.py](agents-remember/mcp/tests/test_sync_dashboard.py); [pre-commit hook](agents-remember/.githooks/pre-commit) |
| Provider lifecycle settings are generated from MCP settings and include `providers/runners`, `providers/data`, `logs/mcp`, and `logs/providers` paths. | [settings.py](agents-remember/mcp/src/agents_remember/providers/settings.py) |
| Provider status reports watcher status and structured recovery actions; the prior runner-integrity check was removed in the 1.0.0 remediation. | [status.py](agents-remember/mcp/src/agents_remember/providers/status.py) |
| Provider lifecycle is now a facade plus focused provider/shared packages instead of a monolithic file. | [providers/lifecycle/](agents-remember/mcp/src/agents_remember/providers/lifecycle/); [CGC lifecycle overview](src/agents_remember/providers/cgc/lifecycle/overview.md); [GrepAI lifecycle overview](src/agents_remember/providers/grepai/lifecycle/overview.md) |
| Memory quality combines drift integrity and onboarding style checks for closeout. | [check.py](agents-remember/mcp/src/agents_remember/memory_quality/check.py); [history_order.py](agents-remember/mcp/src/agents_remember/memory_quality/style/update_history/history_order.py) |

## Update History

- 2026-07-05T19:10+02:00 — No route impact: route model unchanged — 260703-L8 cycle 6 hardens seam internals inside existing routes (integrate guard re-addressing at worktrees/modules, all_current at controlplane, wait=false seam restriction + ambient gate_list at mcp/tools, integrate policy pass-through at controllers) plus doctrine/template updates inside the lifecycle skill tree. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T18:24+02:00 — No route impact: route model unchanged — 260703-L8 cycle 5 lands the seam channel (gates wait/decide semantics documented at mcp/tools; store.find at controlplane; the integrate consumer at worktrees/modules) plus doctrine/template updates inside the lifecycle skill tree and a next_step summary wording fix. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T16:32+02:00 — No route impact: route model unchanged — 260703-L8 cycle 4 lands the seam-ruling remediation (reviewer.md rename + manager-brief.md inside the lifecycle skill tree; config wires the at-seams flag through parse_gate_delegation; next_step rundown re-worded; four skill mirrors touched). Tool signatures unchanged; the new gate kind is documented at the controlplane route. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T04:40+02:00 — No route impact: 260703-L8 de-harnessing pass: the two .claude-code.md runtime-mirror overlays are deleted and their sub-agent doctrine folded into the portable orchestrator/worker files as capability-conditional sections; SKILL resolution drops the variant layer. Markdown doctrine only; file cards for the two overlays retire with their sources; no mcp source or route model change.

- 2026-07-05T04:16+02:00 — No route impact: 260703-L8 reopened pass restructures four runtime-mirror doctrine files inside skills/l-01-agent-lifecycles (orchestrator = event loop + three jobs; designer = the hat; SKILL registry/router wording; manager flat-run + reopen rule) — markdown doctrine only, no mcp source, tool signature, or route model change.

- 2026-07-05T01:32+02:00 — No route impact: route model unchanged — 260703-L9 lifecycle convergence merges the two runtime lifecycle skill trees into `skills/l-01-agent-lifecycles/` (SKILL.md = router + minimal frame; `roles/` from `jobs/`; `lenses.md` from `job-variants.md`; templates gain `worker-brief.md` + the relocated `deep-research-report.md`); file cards moved/renamed accordingly and four c/w skill mirrors carry one-line reference updates. The mcp source deltas are name/path/comment-level only (orchestration_artifacts template root, next_step rundown wording, abandon/reducer comments); tool signatures and route behavior unchanged. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T23:43+02:00 — No route impact: L8 fixes `serving/changeset.py` master net diff tip resolution inside the already-documented change-set serving route; no MCP tool signature, response shape, package route model, or higher-level subsystem boundary changed. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-04T13:16+02:00 — No route impact: 260703-L6 sharpened the synced
  `l-02-agent-orchestration` runtime skill docs/templates only — adversarial reviewer seam-specific
  rubrics, verdict variants, `notes/reports/` artifact placement, and `reviewer-verdict` gate evidence
  refs. No MCP Python source, tool signature, response schema, or package route behavior changed.
  Verification metadata pinned until closeout stamps the L6 commit.
- 2026-07-04T13:03+02:00 — 260703-L5 route model update: the synced
  `l-02-agent-orchestration` runtime skill mirror now carries the full super integration branch
  topology (super from main, masters from super, leaves from masters), orchestrator master-to-super
  worktree integration, C-11 memory carry-over at every edge, ledger mapping, final super-to-main PR +
  main-memory carry-over + push, and the 260630-derived master finalize/archive plus parallel-master
  reconcile follow-ups as sequenced manual backlog. Verification metadata pinned until closeout stamps
  the L5 commit.
- 2026-07-04T12:32+02:00 — 260703-L4 route impact: the MCP package now parses
  opt-in `orchestration.gateDelegation`, exposes the gate policy/controlplane
  schema, enforces policy-valid delegated closeout approvals server-side, and
  projects gate evidence refs. Verification metadata pinned until closeout
  stamps the L4 commit.
- 2026-07-04T12:31+02:00 - L3 route impact: MCP now includes generalized
  agent-to-agent inbox metadata, hosted push delivery, orchestration nudge
  helpers, and dashboard-visible delivery projection. Verification metadata
  pinned until closeout stamps the L3 commit.
- 2026-07-04T11:10+02:00 — agent-orchestration L2 route impact: added the public `spawn_agent_session`
  MCP tool (agent-facing session dispatch) — it changes the mcp tool/model surface (`mcp/tools/terminal.py`
  + `models/terminal.py` + `base.py`/facade/`server.py`/`tool_registry.py`) and extends the `serving`
  subsystem with the shared `terminal_opener` + `terminal_paste` modules, the `tmux -e` env seam, the
  spawned-by catalog columns, and a `POST /api/terminal/{session}/paste` endpoint. Composition-only over
  existing serving primitives (no parallel spawn path). Updated the Purpose tool-surface note and the
  `agents_remember.serving` route-model bullet. Verification metadata pinned until closeout stamps the L2
  commit. (Distinct from the 260703-L2 daemon-supervision entry below.)
- 2026-07-04T11:00+02:00 — No route impact: route model unchanged — orchestration 260703-L1 adds the new `l-02-agent-orchestration` skill tree (14 files: `SKILL.md` = the orchestration frame, five `jobs/<role>.md` job files + two `jobs/<role>.claude-code.md` per-harness variants, six `templates/` report shapes) under `package_data/runtime/skills/`, sync-propagated via `scripts/sync-skills.py`. Registered 14 new file cards in this route's `coveredFiles`, bumped `coverageCounts` (sourceFilesInScope 499→513, fileSidecars 193→207). Skills are model-interpreted markdown, not mcp Python; no mcp source, tool signature, or route behavior changed. Verification metadata on the new file cards pinned until closeout stamps the L1 commit.
- 2026-07-04T10:15+02:00 — No route impact: orchestration 260703-L0 resynced the generated shipped dashboard bundle (mcp/src/agents_remember/package_data/dashboard, a build artifact excluded from memory scope) plus dashboard.fingerprint via scripts/sync-dashboard.py after dashboard-source changes; no mcp Python source, tool, or route behavior changed. Reviewed, overview body accurate as-is.
- 2026-07-03T12:59+02:00 — No route impact: 260703 L4 release bump only (pyproject version +
  SERVER_VERSION fallback to 3.0.0rc2); no mcp behavior or structure change.
- 2026-07-03T12:58+02:00 — No route impact: 260703 L3 rewrote `mcp/README.md`'s Install And Run
  (the PyPI page gains the uv-tool + dashboard + daemon install story; detail in the
  `mcp/README.md` sidecar). Documentation only — the mcp package route model, structure, and
  behavior are unchanged.
- 2026-07-03T12:57+02:00 — 260703 L2 route impact: `serving/` gains `daemon.py` (dashboard daemon
  supervision), the CLI gains `--daemon`/`--status`/`--stop`/`--no-access-log` with settings-default
  `--port`, `mcp/config.py` parses the fail-loud `dashboard` settings object (autoStart, port), and
  `mcp/server.py` `main()` gains the threaded `maybe_autostart_dashboard` boot hook. Covered by
  `mcp/tests/test_dashboard_daemon.py` + new `test_config.py` cases. Verification metadata pinned
  until closeout stamps the code commit.
- 2026-07-03T12:55+02:00 — 260703 L1 route impact: the umbrella CLI under `cli/` gains
  `cli/discovery.py` — trusted-settings auto-discovery making `--config` optional on
  `agents-remember dashboard` (upward walk, convention-then-registration, nearest wins, semantic
  usability probe vs the tracked placeholder template) — covered by
  `mcp/tests/test_cli_discovery.py`. Verification metadata pinned until closeout stamps the code
  commit.
- 2026-07-03T12:50+02:00 — No route impact: L15 push-gate fixups (type narrowing + test import hygiene only; the pre-push quality gate now exits 0 across the tree).
- 2026-07-03T11:20+02:00 — No route impact: L14 release bump only (pyproject version + SERVER_VERSION fallback); no mcp behavior or structure change.
- 2026-07-03T02:58+02:00 — No route impact: L13 reopen drill second cycle (marker comment extension only).
- 2026-07-03T02:40+02:00 — No route impact: L13 reopen drill: a marker comment in mcp/tests/conftest.py only; no mcp behavior or structure change.
- 2026-07-03T01:55+02:00 — L12 route impact: provider compose templates gain memory caps; CGC watch hygiene fixed (enriched .cgcignore reaches the watch context, committed bundle excluded per-repo, fired debounce timers popped via a maintained patch, image revision ar2).
- 2026-07-03T00:35+02:00 — L11 route impact: task_reopen tool added (tasks/reopen.py + leaf_doc.py, task_doc-side controller/payload/model); worktree start honors cleanup=reopened and restamps leaf-doc lifecycles; the reducer projects abandon terminality from contracts.
- 2026-07-02T21:45+02:00 — No route impact: the L10 binding repair is a one-line-scale join fix inside
  `observer/snapshots.py` (described in the observer route overview) plus its
  `mcp/tests/test_observer_projection.py` regression; no MCP tool surface or subsystem narrative
  changed at this granularity. Verification metadata pinned until closeout stamps the L10 commit.
- 2026-07-02T20:55+02:00 — No route impact: the L8-r1 correction (pill-click-triggered direct leaf
  paste instead of auto-paste-on-selection) is a dashboard frontend change; the only `mcp/`-route
  effect is the regenerated `package_data/dashboard/` bundle + `dashboard.fingerprint`. Verification
  metadata pinned until closeout stamps the L8-r1 commit.
- 2026-07-02T20:15+02:00 — No route impact: operations-integration L8 is a dashboard frontend change
  (direct leaf-chat highlight paste + obsolete response-UI cleanup); the only `mcp/`-route effect is the
  regenerated `package_data/dashboard/` bundle + `dashboard.fingerprint`. No MCP package source, tool
  surface, or subsystem narrative changed. Verification metadata pinned until closeout stamps the L8
  commit.
- 2026-07-02T18:35+02:00 — No route impact: operations-integration L7 repaired the `cgc_dependencies`
  native subcommand (`analyze deps`) inside `controllers/provider_tools.py`, refreshed the packaged CGC
  guidance table, and locked the argv contract in `mcp/tests/test_tools.py`. No MCP tool surface or
  subsystem narrative changed at this granularity. Verification metadata pinned until closeout stamps
  the L7 commit.
- 2026-07-02T17:25+02:00 — No route impact: the reopened-L6 copy-mode escape stays inside
  `serving/terminal.py` (typing after wheel scrolling cancels tmux copy-mode; described in the serving
  route overview) and its `mcp/tests/test_terminal.py` coverage. No MCP tool surface or subsystem
  narrative changed at this granularity. Verification metadata pinned until closeout stamps the
  follow-up commit.
- 2026-07-02T17:04+02:00 — L9 route impact: added a package-level agent-facing terminal reassignment tool
  (`attach_terminal_session_to_leaf`) and the shared serving helper used by both MCP and the dashboard
  route. This changes the public MCP tool/model surface and the dashboard terminal catalog subsystem.
  Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-02T16:35+02:00 — No route impact: the reopened-L6 wheel/paste fixes touch
  `serving/terminal.py` (the per-session tmux mouse `TmuxConfigurer` seam, described in the serving
  route overview), its `mcp/tests/test_terminal.py` coverage, and the regenerated
  `package_data/dashboard/` bundle + `dashboard.fingerprint`. No MCP tool surface or subsystem
  narrative changed at this granularity. Verification metadata pinned until closeout stamps the
  follow-up commit.
- 2026-07-02T15:03+02:00 — No route impact: the L6 alternate-buffer wheel follow-up rebuilt and
  re-synced the generated `package_data/dashboard/` bundle plus `dashboard.fingerprint` after the
  `Terminal` wheel routing change under `dashboard/src/`. The shipped bundle remains generated static
  package data served by the existing dashboard package path; no MCP package source behavior, tool
  surface, or subsystem narrative changed. Verification metadata pinned until closeout stamps the
  follow-up commit.
- 2026-07-02T14:15+02:00 — No route impact: L6 closeout rebuilt and re-synced the generated
  `package_data/dashboard/` bundle plus `dashboard.fingerprint` after the leaf-chat draft handoff and
  terminal scrollback frontend changes under `dashboard/src/`. The shipped bundle remains generated
  static package data served by the existing dashboard package path; no MCP package source behavior,
  tool surface, or subsystem narrative changed.
- 2026-07-01T01:43+02:00 — No route impact: L6 rebuilt and re-synced the generated
  `package_data/dashboard/` bundle plus `dashboard.fingerprint` after the right-rail chat context-handoff
  frontend changes under `dashboard/src/`. The shipped bundle remains generated static package data served
  by the existing dashboard package path; no MCP package source behavior, tool surface, or subsystem
  narrative changed. Verification metadata pinned until closeout stamps the L6 commit.
- 2026-06-30T00:00:00+02:00 — No route impact: L5 (Sidebar chat: leaf-keyed attachment) added the leaf→chat registry to
  the serving layer — `serving/app.py` gained the `leafKey` opener claim + `POST /api/terminal/{session}/attach-leaf`
  (`409 leaf-taken`, running-only) and `serving/terminal_catalog.py` gained `TerminalCatalogEntry.leaf_key`
  + `active_for_leaf`, and the generated `package_data/dashboard/` bundle (+ fingerprint) was
  rebuilt/re-synced for the sidebar-chat frontend (the rail River⇄Chat toggle + leaf attach). The serving
  change is documented in the `serving/` route overview + the `app.py`/`terminal_catalog.py` sidecars; the
  shipped bundle remains generated static package data; the mcp-package overview's subsystem narrative is
  unchanged. Verification metadata pinned until closeout stamps the L5 commit.
- 2026-06-29T23:18+02:00 — No route impact: `worktrees/modules/start.py` now derives the recorded memory base from the source branch tip (not the repo HEAD); nothing at the mcp-package route level changes (detail in the start.py file sidecar; task 260629_post-landing-cleanup L3).
- 2026-06-29T23:00+02:00 — No route impact: operations-integration L4a — `serving/changeset.py` gained the
  doc-reader leaf change-set endpoints (`/api/changeset/{task,file-diff}` `leaf` + `mode` selector;
  committed/working views by leaf-id off the persisted contract), and the generated `package_data/dashboard/`
  bundle (+ fingerprint) was rebuilt/re-synced for the doc-reader change-set buttons + the diff-highlight
  rectangle. The serving change is documented in the `serving/` route overview + the `changeset.py` sidecar;
  the shipped bundle remains generated static package data; the mcp-package subsystem narrative is unchanged.
  Verification metadata pinned until closeout stamps the L4a commit.
- 2026-06-29T22:57+02:00 — No route impact: the `task_doc` MCP tool docstring now lists the `remove_subtask` op (server.py registration/forwarding only); nothing at the mcp-package route level changes (detail in the server.py / task_doc_tools.py file sidecars; task 260629_post-landing-cleanup L2).
- 2026-06-29T17:00+02:00 — No route impact: operations-integration L4 review follow-up — `serving/changeset.py` gained the master NET change-set (`master_changeset` net `base→tip` + `master_file_diff`, the `/api/changeset/file-diff` `master` param), and the generated `package_data/dashboard/` bundle (+ fingerprint) was rebuilt/re-synced for the master-inspection + code-view readability/scroll polish. The serving change is documented in the `serving/` route overview + the `changeset.py` sidecar; the shipped bundle remains generated static package data; the mcp-package overview's subsystem narrative is unchanged. Verification metadata pinned until closeout stamps the L4 follow-up commit.
- 2026-06-29T16:40+02:00 — No route impact: operations-integration L4 rebuilt and re-synced the generated `package_data/dashboard/` bundle (+ the sibling `package_data/dashboard.fingerprint`) with `scripts/sync-dashboard.py` after the Change-Set Viewer frontend source changes under the in-scope root `dashboard/src/` sub-project (new `@codemirror/merge` dep). The shipped bundle remains generated static package data served by the existing dashboard package path; no mcp-package source behavior or tool surface changed. Verification metadata pinned until closeout stamps the L4 code commit.
- 2026-06-29T15:30+02:00 — No route impact: operations-integration L3 added a read-only change-set API (`serving/changeset.py`: `GET /api/changeset/{task,file-diff,master}`) plus a shared `serving/scope.py` (scope resolution + error map extracted from `serving/files.py`) and a new `worktrees/modules/git.py` `changed_files_with_counts` primitive. These are serving-layer / worktrees-module additions documented in the `serving/` and `worktrees/modules/` route overviews and the file sidecars; the mcp-package overview's subsystem narrative is unchanged. Verification metadata pinned until closeout stamps the L3 code commit.
- 2026-06-29T09:06+02:00 — No route impact: operations-integration L2 rebuilt and re-synced the generated `package_data/dashboard/` bundle (+ the sibling `package_data/dashboard.fingerprint`) with `scripts/sync-dashboard.py` after the File Viewer frontend source changes under the in-scope root `dashboard/src/` sub-project. The shipped bundle remains generated static package data served by the existing dashboard package path; no mcp-package source behavior or tool surface changed. Verification metadata pinned until closeout stamps the L2 code commit.
- 2026-06-28T22:41+02:00 — No route impact: operations-integration L1 added a read-only dashboard files API (`serving/files.py`) plus a shared `kernel/sidecar_pairing.py` helper and its test. These are serving-layer / shared-kernel additions documented in the `serving/` route overview and the file sidecars; the mcp-package overview's subsystem narrative is unchanged. Verification metadata pinned until closeout stamps the L1 code commit.
- 2026-06-28T20:30+02:00 — No route impact: a `find_worktree_contract` archive-skip + docstring fix under `kernel/coordination_context/`; nothing at the mcp-package route level changes (detail in the contracts.py file sidecar; task 260628_post-landing-cleanup).
- 2026-06-28T16:17+02:00 — Task 35 route impact: `scripts/sync-dashboard.py --check` is now source-aware —
  `sync` fingerprints the dashboard build inputs (the `src` tree minus tests, plus the production configs)
  into a sibling `package_data/dashboard.fingerprint`, and `--check` re-verifies it, so the pre-commit gate
  flags a `dashboard/src` change shipped without a rebuild (not only the built-bundle digest), mirroring how
  the skill gate flags a changed skill. Covered by `test_sync_dashboard.py` `SourceFingerprintTests`.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-28T13:54+02:00 — Task 34 route impact: the package-level observer/serving summary now records
  **inactivity-keyed** raw Event River retention (superseding the post-termination grace-window pruning):
  `event_retention.py` prunes a fleeting/enclosure lifecycle log after >1h of no real (non-heartbeat)
  activity rather than on `lifecycle.ended`, `ambient.py`'s heartbeat ticker decays after ~10 min idle,
  and `/api/events` does one retained-backlog scan per connect, filters `lifecycle.heartbeat`, and
  streams a bounded chunked backlog. Detail lives in the observer and serving route overviews plus the
  `event_retention.py`, `ambient.py`, and `events.py` sidecars. Verification metadata pinned until
  closeout stamps the task-34 code commit.
- 2026-06-28T07:45+02:00 — Task 33 route impact: the observer projection now exposes an `activeWorktreeGroups`
  field (from `active_enclosure_worktree_groups`, shared with the Engine Room) that the dashboard Topology
  consumes for active-enclosure scoping. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-28T07:43+02:00 — Task 29 S7 route impact: the package summary now records actionable-drift
  provenance/dismissal, raw Event River `ready` hydration, and the no-frontend-count-cap boundary.
  Detail lives in the observer, serving, controlplane, memory-quality, and dashboard route overviews.
  Verification metadata pinned until closeout stamps the task-29 code commit.
- 2026-06-28T06:08+02:00 — Task 29 route impact: the package-level observer/serving summary now records
  lifecycle-aware raw Event River retention and active-enclosure projection admission. The raw
  `events.jsonl` substrate remains episodic rather than audit-grade: terminal lifecycle logs are pruned
  after the grace window, fresh raw SSE connections start from retained offsets, projection caches repo
  surfaces briefly, and worktree provider/runtime data is admitted only for active enclosure-backed
  worktree groups. Detail lives in the observer and serving route overviews plus the
  `event_retention.py`, `worktree_provider_admission.py`, `projection_store.py`, `snapshots.py`, and
  `events.py` sidecars. Verification metadata pinned until closeout stamps the task-29 code commit.
- 2026-06-28T03:33+02:00 — Task 32 route impact: the package-level observer summary now records
  physical retention for persisted drift snapshots — cleanup removes the exact code-worktree snapshot
  for a reclaimed contract and projection prunes valid deleted-worktree snapshots before reading
  analytics. Verification metadata pinned until closeout stamps the task-32 code commit.
- 2026-06-28T03:21+02:00 — Task 31 route impact: the package-level dashboard path now refreshes provider
  current-state before live projection ticks, inspects worktree provider containers for isolated stacks, and
  projects missing expected provider roles into Engine Room instead of leaving empty provider containers
  ambiguous. Detail lives in the `observer/`, `serving/`, `providers/`, and dashboard panel sidecars.
  Verification metadata pinned until closeout stamps the task-31 code commit.
- 2026-06-27T22:00+02:00 — Task 28 route impact (NOTIFY-AND-CONTINUE turn end): the
  `agents_remember.observer` next-step paragraph now records the new non-terminal
  `awaiting-developer` state + public `lifecycle_turn_end_notification(summary)` tool
  (notify + stop, no wait/inbox) as the **active** turn-end path, the `_tool_payload`
  auto-dismiss, the next-step hint **repoint** from `lifecycle_gate`, and the one-line
  reducer gate-open/blocked-gate dedup; the `agents_remember.controlplane` bullet now
  records that the `lifecycle_gate`/`operator_inbox_*` turn-end choreography is **parked**
  (kept and valid, un-hinted). Per-file detail lives in the `observer/`, `mcp/tools/`, and
  `models/` route overviews + the file sidecars. Verification metadata pinned until closeout
  stamps the code commit.
- 2026-06-27T21:20+02:00 — Task 30 route impact: the package-level worktree lifecycle
  summary now records the already-integrated re-closeout reset behavior in
  `worktrees/modules/closeout.py`: changed closeouts reopen integration for
  re-integration, while no-op re-closeouts keep completed integration markers.
  Detailed behavior lives in the `worktrees/modules` route overview and the
  closeout sidecar. Verification metadata pinned until closeout stamps the code
  commit.
- 2026-06-27T20:16+02:00 — No route impact: the task-27 follow-up adds a gate-await
  branch to `mcp/tools/next_step.py` (a `blocked` lifecycle now hints
  `lifecycle_resume`, carrying the chain through the open gate). The next-step
  engine is already inventoried in this route's `agents_remember.observer` Route
  Model bullet and its architecture is unchanged (detail in the file sidecar).
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T18:43+02:00 — Task 27 route impact: the `agents_remember.observer`
  Route Model bullet now records the lifecycle next-step hint engine
  (`mcp/tools/next_step.py`) — a `NextStep` hint folded from the projected
  lifecycle state and attached to every tool response at the `_tool_payload`
  choke point (one-time `lifecycle_start` `frontHalfRundown` front half, the
  linear half delegating to `guidance.lifecycle_guidance` with a
  `lifecycle_gate(kind=…)` gate overlay, and a terminal `lifecycle_end`
  loop-back), generalizing worktree-only guidance to the whole lifecycle spine.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T15:24+02:00 — Task 22 follow-up route impact: the package-level serving summary now records
  detached tmux session creation, independent per-browser WebSocket attaches, non-destructive browser
  disconnect, and sticky explicit termination for cataloged dashboard terminal sessions. Detailed
  behavior lives in the serving route overview and sidecars. Verification metadata pinned until closeout
  stamps the follow-up code commit.
- 2026-06-26T23:15+02:00 — Task 22 route impact: the dashboard serving route now persists terminal
  session metadata in `serving.terminal_catalog`, lists catalog rows, rehydrates live tmux sessions on
  WebSocket attach, marks stale rows exited, and terminates cataloged sessions on request. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-26T20:18+02:00 — Task 21 route impact: task-document writes now synchronize same-root master
  rows, and observer analytics expose `SeriesNode.seriesTokenTotal` for the dashboard master reader.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T19:40+02:00 — No route impact: task 20 reopened for Event River
  lifecycle-label fallback and only re-synced the generated
  `package_data/dashboard/` bundle under `mcp/` after frontend source changes
  in `dashboard/src/data` and `dashboard/src/panels`. The shipped bundle remains
  generated static package data served by the existing dashboard package path;
  no MCP tool surface, serving contract, or package route model changed.
  Verification metadata pinned until closeout stamps the reopened task-20 code
  commit.
- 2026-06-26T18:43+02:00 — Regression fix: package-level control-plane
  paragraph now records `lifecycle_gate` as blocking until a developer decision
  or gate-specific inbox response, with stale lifecycle-scoped inbox rows ignored
  by the public junction.
- 2026-06-26T18:23+02:00 — No route impact: task 20 rebuilt and re-synced the generated
  `package_data/dashboard/` bundle after Event River frontend source changes under `dashboard/src/panels/`.
  The shipped bundle remains generated static package data served by the existing dashboard package path;
  no MCP tool surface, serving contract, or package route model changed. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-06-26T17:05+02:00 — Regression fix: package-level control-plane
  paragraph now records `lifecycle_gate` as create + block + bounded wait, so
  the public agent-facing junction is no longer described as wait-state
  initialization only.
- 2026-06-26T16:15+02:00 — Task 25 closeout verification: refreshed the package-level
  control-plane paragraph for the unified public `lifecycle_gate` registration and verified
  the `task_doc replace` summary against code commit `2017434`.
- 2026-06-26T15:33+02:00 — No route impact: task 25 preserves the source branch's
  `task_doc replace` operation; lifecycle-gate API consolidation is documented in the scoped
  control-plane, MCP-tool, model, and observer sidecars, so the package-level task-document summary
  remains the replacement-repair wording. Verification metadata pinned until closeout stamps the code
  commit.
- 2026-06-25T14:02+02:00 — Task 24 reopened: MCP package overview records ambient-bound gate creation plus gate-id-only cancel cleanup for stale workspace-shaped gates.
- 2026-06-25T13:20+02:00 — Task 23/24: MCP package overview now records disposable gate/inbox interaction retention, agent-pickup projection, and the rebuilt dashboard bundle.
- 2026-06-25T09:55+02:00 — GrepAI provider lifecycle now documents and tests non-conflicting preferred auto host ports (`61432` PostgreSQL, `61434` Ollama) while retaining container service ports `5432`/`11434`.
- 2026-06-25T07:26+02:00 — Task 19 gate interaction polish: the MCP package now exposes
  `gate_response_wait`, keeps one open gate per lifecycle by expiring older gates, records targeted
  dashboard Yes/No decisions with rejection notes, preserves Chat as operator-inbox/message-only, and
  ships the rebuilt dashboard bundle. Verification metadata pinned until closeout stamps the code
  commit.
- 2026-06-24T18:17+02:00 — No route impact: empty-state backdrop zoom-stability rebuilt and re-synced the
  generated `package_data/dashboard/` bundle after the frontend source and SC2 boomerang asset changes in
  `dashboard/src` / `dashboard/public/assets`. The shipped bundle remains generated output served by the
  existing MCP dashboard package path; no MCP tool surface, serving contract, or package route model changed.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T16:39+02:00 — Task 17 package route correction: refreshed the task-document summary so
  observer projection is active-doc-first with optional lifecycle context, rather than requiring a
  lifecycle key before Operations can show a task. Detail lives in the observer route overview and
  sidecars. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T13:59+02:00 — No route impact: the Task 17 progress-count follow-up only re-synced the
  generated dashboard bundle under `src/agents_remember/package_data/dashboard/` after a
  `dashboard/src/panels/DetailPanel.tsx` display fix; no MCP package service surface changed.
  Verification metadata pinned until closeout stamps the follow-up code commit.
- 2026-06-24T12:57+02:00 — No route impact: the Task 17 master-selection follow-up only re-synced the
  generated dashboard bundle under `src/agents_remember/package_data/dashboard/` after a
  `dashboard/src/panels/DetailPanel.tsx` fix; no MCP package service surface changed. Verification
  metadata pinned until closeout stamps the follow-up code commit.
- 2026-06-24T12:43+02:00 — No route impact: Task 18 rebuilt and re-synced the generated
  `package_data/dashboard/` bundle after the Operations task-title ellipsis fix in `dashboard/src`.
  The MCP package route model is unchanged; the synced assets remain generated output owned by
  `scripts/sync-dashboard.py` and checked by `mcp/tests/test_sync_dashboard.py`. Verification metadata
  pinned until closeout stamps the code commit.
- 2026-06-24T12:21+02:00 — No route impact: Task 17 updates `mcp/tests/test_observer_projection.py`
  coverage for observer task/series `createdAt` and master objective projection within the existing
  observer/test route model; no new MCP service domain or package route was added. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-24T08:59+02:00 — No route impact: observer task-document correction keeps
  `series-contract.md` as enclosure/process state only; lifecycle-readable task content comes from
  JSON-primary `ar-task-document/v1` docs. Detail lives in the `observer/` overview plus
  `snapshots.py`, `projection.py`, and `test_observer_projection.py` sidecars. The generated dashboard
  bundle under `package_data/dashboard/` was re-synced from `dashboard/dist`; no MCP tool surface
  changed. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:26+02:00 — Series-contract task resolver: refreshed the worktree lifecycle Route Model
  paragraph to mention `worktrees/task_resolver.py`, which centralizes task-name lookup, nested
  parent-task disambiguation, leaf enclosure contract paths, active archive exclusion, and completed
  root-task archival. Detail lives in the new `task_resolver.py` sidecar. Verification metadata pinned until
  closeout stamps the series-contract resolver code commit.
- 2026-06-24T00:16+02:00 — Task 14 cleanup correction: updated the worktree lifecycle Route Model paragraph to reflect the current child-edge cleanup contract. Cleanup still hard-refuses before carryover and proves task work branches against the contract source branch, but it no longer retires parent/source branches; those branches are finalized by their own lifecycle edge.
- 2026-06-23T23:04+02:00 — Dashboard task 14 adds the terminal `lifecycle_finalize_task` MCP operation. Refreshed the Hot Path Summary and Route Model for `worktrees/modules/finalize.py`: one branch-edge ancestry proof after landing, memory carryover check, cleanup verification, JSON-primary leaf + immediate parent-row reconciliation, no squash equivalence.
- 2026-06-23T22:31+02:00 — Task 12 S2 clarification: refined the observer summary to distinguish
  GrepAI process aggregation from addressable repo/project targets, so `targetRepos` can project as repo
  satellites without implying separate per-repo provider processes.
- 2026-06-23T22:09+02:00 — Task 12 S2 correction: refined the observer read-side summary after GrepAI
  target evidence was verified in MCP config/current-state flow. CGC watcher rows and GrepAI
  configured `targetRepos` now both project as repo-scoped workspace provider nodes; only providers
  without target evidence remain aggregate.
- 2026-06-23T21:58+02:00 — Task 12 S2 refreshed the observer read-side summary for repo-covered
  workspace provider projection: CGC per-repo watcher rows now become repo-scoped provider nodes,
  while unsupported provider coverage remains aggregate. Detail lives in the `observer/` route
  overview plus the `provider_nodes.py`, `snapshots.py`, `projection.py`, and
  `test_observer_projection.py` sidecars.
- 2026-06-23T16:17+02:00 — Task 13 cleanup correctness: refreshed the `agents_remember.observer` / worktree lifecycle Route Model paragraph for the cleanup source-branch proof and dry-run directory preview fix; detailed behavior lives in the `worktrees/modules` route overview and `cleanup.py` sidecar.
- 2026-06-23T16:02+02:00 — No route impact: task 12 S1 refreshed the shipped dashboard bundle under
  `src/agents_remember/package_data/dashboard/` with `scripts/sync-dashboard.py` after changing the
  topology frontend source. The MCP package route model and Python serving/control/tool behavior are
  unchanged; this is generated static frontend package data only.
- 2026-06-23T15:05+02:00 — Task 10 dashboard fallback: added the serving-layer `POST /api/operator-inbox` bridge to the package overview, tying the dashboard no-hosted-session path to the external-chat operator inbox. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-23T14:33+02:00 — No route impact: Task 11 refreshed the shipped dashboard bundle under
  `src/agents_remember/package_data/dashboard/` with `scripts/sync-dashboard.py` after changing the
  browser cockpit. The MCP package route model and Python serving/control/tool behavior are unchanged;
  this is generated static frontend package data only.
- 2026-06-23T13:44+02:00 — Task 10 backend inbox: documented the external-chat operator inbox as a control-plane sibling to gates and the three new `operator_inbox_*` tools. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-23T07:25+02:00 — slice 09 (gate-signal adoption): refreshed the `agents_remember.controlplane` Route Model bullet for the `GateKind` extension to the full l-01 gate spine (`plan-approval` / `worktree-intent` / `push-approval` added; `closeout-approval` IS the commit gate, tracked by the `gate_create` docstring), and the `agents_remember.observer` bullet for the `worktrees/modules/guidance.py` visibility fix — `lifecycle_guidance` no longer reads a `commit-approval-pending` gate off `git status`, so a dirty worktree projects its honest lifecycle-position phase (closeout-completed → `integration-pending`). The mcp package route model this overview describes is unchanged; per-route detail lives in the `controlplane/` + `worktrees/modules/` route overviews + the `records.py` / `server.py` / `guidance.py` sidecars. Verification metadata pinned until closeout stamps the slice-09 code commit.
- 2026-06-23T01:40+02:00 — No route impact: slice 07b v1 carries the read's `repoId` on the `read.packet` — `observer/ambient.emit_read_packet` now takes `repo_id` and emits `data.repoId`, `controllers/read_files.py` passes `repo.repo_id`, and `mcp/tests/test_read_ar_files.py` asserts it (the dashboard `EventRiver` consumes it, out of this package). No MCP tool signature, controller surface, or schema changed; detail lives in the `controllers/` + `observer/` route overviews + file sidecars, and the mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the slice-07b code commit.
- 2026-06-23T00:53+02:00 — No route impact: slice 07 S4+S5 is doctrine/docstring text only — the `read_ar_files` tool docstring (`mcp/server.py`) now states the research-phase-read role, the `controllers/read_files.py` + `observer/served_store.py` docstrings retarget the compact-reset producer to the post-3.0 agentic-control-plane (consumer + `refresh` kept as defensive scaffolding), and the synced runtime mirrors under `package_data/runtime/` (coordinator `AGENTS.md`, `c-04`/`l-01` `SKILL.md`) carry the research-phase-read doctrine. No MCP tool signature, controller surface, or schema changed; detail lives in the `controllers/` + `observer/` route overviews + file sidecars, and the mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the slice-07 code commit.
- 2026-06-21T06:40+02:00 — Slice 05m (carryover-before-cleanup): refreshed the `agents_remember.observer` Route Model bullet for the carryover-before-cleanup lifecycle correctness landed in `worktrees/modules/` (`guidance.carryover_done` reads the official ledger; the new `carryover-pending` phase routes `memory_carryover_apply` before `cleanup-pending`; `cleanup_result` hard-refuses cleanup until the carry runs and then retires the work + PR'd source branches) and the observer reducer that now follows it (`_GUIDANCE_PHASE` projects `carryover-pending`; the engine-room node carries the display-only `carryoverDoneAt`). The mcp-package detail lives in the `worktrees/modules/` + `observer/` route overviews + file sidecars; the mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the 05m code commit.
- 2026-06-21T05:30+02:00 — Slice 05l Part 2 (landing-arc probe hardening): refreshed the `agents_remember.observer` Route Model bullet for the hardened `worktrees/modules/landing.py` probe — the protected target `origin/<base>` is now probed directly via `ls-remote` (visible across the whole landing window before any PR and independent of `gh`) and the PR ref carries gh's open/merge timestamp on the additive `LandingRefNode.at`, so the dashboard can follow a REAL remote landing; carryover/cleanup lifecycle correctness is a separate upcoming slice (05m). The mcp-package detail lives in the `worktrees/modules/` + `observer/` route overviews + file sidecars; the mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the 05l-P2 code commit.
- 2026-06-21T04:10+02:00 — Slice 05l Part 1 (backend teardown visibility): the `agents_remember.observer` reducer now projects the `abandoned` worktree phase (sourced from `worktrees/modules/guidance.py`'s new `cleanup == "abandoned"` branch) and **drops disposed** (cleaned-up/abandoned) enclosures from the Engine Room `Analytics.engineProcesses` so the frontend (05k) animates the teardown; refreshed the observer Route Model bullet. The mcp-package detail lives in the `observer/` + `worktrees/modules/` route overviews + file sidecars; the mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the 05l-P1 code commit.
- 2026-06-21T02:44+02:00 — No route impact: slice 6g changes are observer-local — `observer/read_task_documents` contract-pairs masters + resolves cross-master links, and `observer/projection.TaskDocNode` gains `subTasks`/`sections`/`masterLifecycleId` (detail in `src/agents_remember/observer/overview.md`). The `mcp/` package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the 6g code commit.
- 2026-06-19T20:30+02:00 — Task 6 slice 6f: `agents_remember.serving` gained `POST /api/terminal/{session}/image` (save a validated screenshot under the session cwd for path-injection, `python-multipart` dep) and a harness-scoped Ctrl-Z strip on the terminal host. Refreshed the serving Route Model bullet; per-file detail lives in `serving/overview.md` + the `app.py`/`terminal.py` sidecars. Verification metadata pinned until closeout stamps the 6f code commit.
- 2026-06-19T15:50+02:00 — No route impact: the 5h H4 cleanup teardown + landing-source flag fix only re-synced the generated dashboard bundle under `package_data/dashboard/` (excluded from memory scope); no mcp-package source behavior changed. The frontend change lives in the in-scope root `dashboard/src/`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T15:00+02:00 — No route impact: the 5h H3 remote/PR strip readability + connector pass only re-synced the generated dashboard bundle under `package_data/dashboard/` (excluded from memory scope); no mcp-package source behavior changed. The frontend change lives in the in-scope root `dashboard/src/`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T14:05+02:00 — No route impact: task 6 slice 6e-4 modified `serving/terminal.py` (controlling-tty via `os.login_tty` + a seeded winsize so tmux honors resize) and `mcp/tests/test_terminal.py` (added `test_spawn_seeds_default_winsize`); both are internal to the already-documented `serving/` sub-route (detail in `serving/overview.md` + the `terminal.py` / `test_terminal.py` sidecars). The `mcp/` package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the 6e-4 code commit.
- 2026-06-19T13:57+02:00 — No route impact: slice 5h H3 only re-synced the generated dashboard bundle under `package_data/dashboard/` (excluded from memory scope; synced from `dashboard/dist`); no mcp-package source behavior changed. The H3 frontend change (engine-room remote/PR landing strip) lives in the in-scope root `dashboard/src/` with its own route + file sidecars. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T07:23+02:00 — No route impact: slice 3c R5 adds a `dry_run` flag to the `task_doc` tool (act-by-default false; true returns `rendered`/`diff`/`wouldLose` without writing) — an optional param on an existing tool, no new tool surface; the mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T06:39+02:00 — No route impact: the engine-room crash fix rebuilt the shipped dashboard bundle under `package_data/dashboard/` (synced from `dashboard/dist`); it is a generated artifact and no mcp package route surface changed. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T06:03+02:00 — No route impact: slice 3c reopened (R4, leaf-doc fidelity) adds leaf schema fields (`statusNote`/`headerNotes`/`HeaderNote`) + freeform leaf `sections` in the `tasks/` route, a `_MUTABLE_FIELDS`/`set_section` controller tweak, and the synced w-02 skill guidance under `package_data/runtime/skills/`; no MCP tool surface changed (the `task_doc` signature is unchanged) and the mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T05:15+02:00 — No route impact: slice 3c reopened (R3, deferred-examples honesty) adds an optional `codeExamplesNote` schema field + a renderer branch in the `tasks/` route and the synced w-02 skill guidance under `package_data/runtime/skills/`; no MCP tool surface changed (the `task_doc` tool signature is unchanged) and the mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T04:18+02:00 — No route impact: slice 3c reopened (R2, heading-vs-outcome) adds an optional `Step.outcome` + a renderer tweak in the `tasks/` route (the checkbox carries the distinct outcome; a bare step is heading-only); detail in the `tasks/` overview + the `document.py`/`render.py` sidecars. The mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T03:17+02:00 — No route impact: slice 3c reopened (R1, masters observable) adds a folder-keyed series/master projection inside the `observer/` route (`read_series_documents` + `SeriesNode`/`Analytics.series`) plus the `series_total`/`series_done` helpers in the `tasks/` route; both carry their own sub-route overviews and the mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T21:27+02:00 — Task 6 slice 6e-2b: `agents_remember.serving` gained `harnesses.py` (the curated harness launch registry — Claude Code/Codex/Pi.dev + `shutil.which` detection) + `app.py`'s `GET /api/harnesses` and a `kind="harness"` opener branch. Refreshed the serving Route Model bullet (opener now spawns a shell *or* a detected harness). Per-file detail lives in the `serving/` route. Verification metadata pinned until closeout stamps the 6e-2b code commit.
- 2026-06-18T21:25+02:00 — No route impact: slice 5h Tier 2 enriches the `observer/` ledger window with per-side commit message + date via a best-effort batched `git log` (detail in the `observer/` overview) and expands `mcp/tests/test_observer_projection.py` under this route with `LedgerCommitMetaTests` (real git repos); the mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T18:00+02:00 — No route impact: slice 5h's ledger popover extends the `observer/` ledger surface (additive `LedgerNode.rows` / `EngineProcessNode.ledgerRows`; detail in the `observer/` overview) and expands `mcp/tests/test_observer_projection.py` under this route with the windowing tests; the mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T17:40+02:00 — Task 6 slice 6e-2a: `agents_remember.serving` `app.py` gained the `POST /api/terminal/{session}` **opener** (the dashboard spawns + owns a shell session at `config.workspace_root` via the pure `resolve_terminal_launch` → `host.open`; server-resolved command). Refreshed the serving Route Model bullet. Harness kinds + per-harness buttons are 6e-2b. Verification metadata pinned until closeout stamps the 6e-2a code commit.
- 2026-06-18T16:10+02:00 — Task 6 slice 6d-2: `agents_remember.serving` `app.py` gained the `@app.websocket("/api/terminal/{session}")` Mode B2 bridge (PTY ↔ WebSocket — binary out, JSON `stdin`/`resize` in, `{type:exit}` on child exit, attach-only + tmux-persistent) + the `terminal_host` `create_app` param; `pyproject.toml` added the `websockets` core dep (uvicorn's WS impl). Refreshed the serving Route Model bullet; per-file detail lives in the `serving/` route. The xterm.js visual is 6e. Verification metadata pinned until closeout stamps the 6d-2 code commit.
- 2026-06-18T15:40+02:00 — Task 6 slice 6d-1: `agents_remember.serving` gained the **Mode B2 terminal host** (`terminal.py` — a `TerminalHost` registry of tmux-wrapped stdlib-`pty` sessions, injectable spawn, fixed-argv/localhost posture) + `mcp/tests/test_terminal.py`. Refreshed the serving Route Model bullet; per-file detail lives in the `serving/` route. The WebSocket bridge + `websockets` dep are 6d-2, the xterm.js visual 6e. Verification metadata pinned until closeout stamps the 6d-1 code commit.
- 2026-06-18T14:05+02:00 — No route impact: task 6 slice 6c Part A is within the `agents_remember.observer` sub-route (gate projection — `read_gates` + `_attach_gates` / `_gate_attention` materialize a durable gate onto the lifecycle); the mcp package route model this overview describes is unchanged — detail lives in the `observer/` route overview + file sidecars (the `mcp/tests` test addition has no package-route impact). Verification metadata pinned until closeout stamps the 6c Part A code commit.
- 2026-06-18T12:10+02:00 — Task 6 slice 6b: the `agents_remember.controlplane` domain became **enforcing** — new `enforcement.py` (`evaluate_closeout_gate`) binds `worktree_closeout_apply` on a developer-approved gate, and `agents_remember.serving`'s POST plane records gate decisions (`gate_decide_for_lifecycle`). Refreshed the controlplane + serving Route Model bullets; per-file detail lives in those routes + the synced l-01/c-12-closeout skill sidecars under this package. Verification metadata pinned until closeout stamps the 6b code commit.
- 2026-06-18T08:51+02:00 — No route impact: slice 5h H1 adds the `worktrees/modules/landing.py` best-effort landing-arc probe (detail in the `worktrees/modules/` overview) and the `observer` `landing`/`integrationStrategy` projection fields (detail in the `observer/` overview); the new `mcp/tests/test_landing.py` + the expanded `test_observer_projection.py` under this route carry no mcp-package route-model impact. The mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the 5h code commit.
- 2026-06-18T01:05+02:00 — Task 6 slice 6a: new `agents_remember.controlplane` service domain (the gate control-plane substrate — `GateRecord` + `GateStore`) plus the four `gate_*` MCP tools registered through `server.py`/`mcp/tools`/`models` (47-tool surface). Added the controlplane Route Model bullet; per-file detail lives in the new `controlplane/` route and the `gates` sidecars. Verification metadata pinned until closeout stamps the 6a code commit.
- 2026-06-16T03:50+02:00 — No route impact: slice 5f S5 only re-synced the generated dashboard bundle under `package_data/dashboard/` (excluded from memory scope); no mcp-package source behavior changed. The S5 frontend change (lifecycle-phase header pulse) lives in the in-scope root `dashboard/src/`.
- 2026-06-16T03:40+02:00 — No route impact: slice 5f S4 only re-synced the generated dashboard bundle under `package_data/dashboard/` (excluded from memory scope); no mcp-package source behavior changed. The S4 frontend change (conduit power-up flow packets) lives in the in-scope root `dashboard/src/`.
- 2026-06-16T03:35+02:00 — No route impact: slice 5f S3 only re-synced the generated dashboard bundle under `package_data/dashboard/` (excluded from memory scope); no mcp-package source behavior changed. The S3 frontend changes (promotion morph + alarm-parity test) live in the in-scope root `dashboard/src/`.
- 2026-06-16T03:25+02:00 — No route impact: slice 5f S6 closed the §9 observability gaps in `observer/reducer.py` (the `_start_attention` attention source + `start_progress` threading) and `worktrees/modules/start.py` (happy-path start-progress emits); the mcp package route model this overview describes is unchanged — detail lives in the `observer/` + `worktrees/modules/` route overviews and the file sidecars.
- 2026-06-16T03:05+02:00 — No route impact: slice 5f S2 only re-synced the generated dashboard bundle under `package_data/dashboard/` (excluded from memory scope); no mcp-package source behavior changed. The S2 frontend changes (Engine Room birth motion + fleeting rendering) live in the in-scope root `dashboard/src/`.
- 2026-06-16T02:30+02:00 — No route impact: slice 5f S1 only re-synced the generated dashboard bundle under `package_data/dashboard/` (excluded from memory scope); no mcp-package source behavior changed. The S1 frontend change (full-bleed cockpit layout) lives in the in-scope root `dashboard/src/`.
- 2026-06-16T01:55+02:00 — No route impact: slice 5f S0 only re-synced the generated dashboard bundle under `package_data/dashboard/` (excluded from memory scope); no mcp-package source behavior changed. The S0 frontend changes live in the in-scope root `dashboard/src/` with their own route overviews + file sidecars.
- 2026-06-15T19:35+02:00 — No route impact: slice 5e's mcp-side changes (the observer `engineProcesses` surface + `worktrees/start_progress.py` §5.4) are captured in the `observer/` and `worktrees/modules/` route overviews + file sidecars; the mcp package route model this overview describes is unchanged.
- 2026-06-15T17:00+02:00 — No route impact: slice 5d only re-synced the generated dashboard bundle under `package_data/dashboard/` (excluded from memory scope); no mcp-package source behavior changed. The 5d frontend re-architecture (Panda + React Aria) lives in the now-in-scope root `dashboard/src/` with its own route overviews + file sidecars.
- 2026-06-14T23:30+02:00 — Slice 05 (5c): the `agents_remember.observer` read side now synthesizes paused persistent lifecycles from worktree contracts, reads per-worktree provider stacks (surface 4), and carries the full task content on `TaskDocNode`; `agents_remember.serving` `sim.py` materializes fixture structural surfaces and `events.py` single-encodes the raw SSE channel. Under `mcp/tests`, `test_observer_projection.py`/`test_serving.py` gained the matching cases plus a new `mcp/tests/fixtures/build_rich_sim.py` rich-sim generator (its own sidecar). Refreshed the observer Route Model bullet; the cockpit UI is frontend (out-of-scope root `dashboard/`). Verification metadata pinned until closeout stamps the 5c code commit.
- 2026-06-14T17:30+02:00 — Slice 05 (5b): the `agents_remember.observer` projection gained the server-computed **attention queue** (`AttentionItem` + the derived `Analytics.attentionQueue`, the pure `build_attention_queue` wired through `project_workspace`); refreshed the observer Route Model bullet. The expanded `mcp/tests/test_observer_projection.py` under this route carries no mcp-package route-model impact (detail in the file/route cards). The 5b cockpit panels are frontend, living in the out-of-scope root `dashboard/`. Verification metadata pinned until closeout stamps the 5b code commit.
- 2026-06-14T15:52+02:00 — Slice 05a: the package now ships the **real** dashboard cockpit bundle under `package_data/dashboard/` (the slice-04 placeholder is replaced by the Vite/React build, synced by `scripts/sync-dashboard.py`); added `mcp/tests/test_sync_dashboard.py` and wired `sync-dashboard.py --check` into both githooks + the CI workflow. The mcp package route model is otherwise unchanged (the cockpit React/TS sources live in the out-of-scope root `dashboard/`). Verification metadata pinned until closeout stamps the 5a code commit.
- 2026-06-14T11:30+02:00 — Slice 04 commit 4b: extended `agents_remember.serving` with the raw `event` SSE channel (`events.py` — byte-offset `Last-Event-ID` resume), sim-mode replay (`sim.py` — a replay clock + fixture feeder over the projector's `now`/`before_tick` seams), and the no-mutation `POST /api/actions/{action}` skeleton (`actions.py`); `app.py` gained `/api/events` + `/api/actions`, `cli/dashboard.py` the `--sim`/`--sim-speed` flags. Refreshed the serving Route Model bullet; per-file detail lives in the new + updated `serving/` sidecars. Verification metadata pinned until closeout stamps the 4b code commit.
- 2026-06-14T11:30+02:00 — Slice 04 commit 4a: new `agents_remember.serving` service domain (the dashboard serving spine — FastAPI app, shared projector, per-entity SSE deltas, static mount) with its own route overview, plus the umbrella `agents-remember` CLI (`cli/__main__.py` + `cli/dashboard.py`) and `fastapi`/`uvicorn` core deps. Added the serving Route Model bullet; per-file detail lives in the new `serving/` route + `cli/` sidecars. Verification metadata pinned until closeout stamps the 4a code commit.
- 2026-06-14T00:16+02:00 — No route impact: slice 3c commit 3 extends the `agents_remember.tasks` domain with `kind:"master"` (a `subTasks` series index + ordered `sections`) and the master `task_doc` ops (`set_subtask`/`set_section`); the per-route detail lives in the `tasks/`, `mcp/tools`, and controller overviews + the file sidecars, and the mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the 3c commit-3 code commit.
- 2026-06-13T23:10+02:00 — Slice 3c commit 2: the observer read side first added task-document projection (`read_task_documents` → `Analytics.taskDocuments`; later Task 17 made projection active-doc-first with optional lifecycle context), and the `w-02-light-task-workflow` skill under `package_data` adopted JSON-primary authoring (synced from canonical `skills/`). Updated the tasks Route Model bullet (the observer projects them, not "will project"). Verification metadata pinned until closeout stamps the 3c commit-2 code commit.
- 2026-06-13T22:34+02:00 — Slice 3c commit 1: new `agents_remember.tasks` service domain (the JSON-primary `ar-task-document/v1` schema + renderer + store) and the `task_doc` authoring tool registered through `server.py`/`mcp/tools`/`models` (43-tool surface). Added the tasks Route Model bullet; per-file detail lives in the new `tasks/` route and the `task_doc` sidecars. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
- 2026-06-13T20:48+02:00 — Slice 3b: the `agents_remember.observer` projection read side gained the analytical surfaces (drift snapshot, sidecar staleness, setup, route coverage, tool reports, ledger) + the rollups; refreshed the observer Route Model bullet (no longer "analytical surfaces land in 3b"). The drift-producer snapshot write in `memory_quality/summary.py` and the expanded `mcp/tests/test_observer_projection.py` under this route carry no mcp-package route-model impact (detail lives in their file/route cards). Verification metadata pinned until closeout stamps the 3b code commit.
- 2026-06-13T19:30+02:00 — Slice 3a: the `agents_remember.observer` domain gained the projection **read side** (`reducer.py`, `projection.py`, `snapshots.py`, `projection_store.py`, plus the shared `paths.py`/`timeutil.py`); the observer Route Model bullet no longer says the read side "arrives in a later slice." Per-file detail lives in the `observer/` route. Verification metadata pinned until closeout stamps the 3a code commit.
- 2026-06-13T18:45+02:00 — No route impact: slice 2c extends the mcp-internal `observer` domain (resume + save gate: `save_gate.py`, ambient `promote`/`attach`) and forwards an `on_unsaved` argument through the lifecycle/worktree tools; the per-route detail lives in the `observer` and `mcp/tools` overviews, and the mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the 2c code commit.
- 2026-06-13T16:41+02:00 — Slice 2b: the `agents_remember.observer` domain gained the ambient lifecycle and the six `lifecycle_*` signal tools, and `server.py` + `mcp/tools/base.py` wired the `install_ambient` call plus the `_tool_payload` emission hook; updated the observer Route Model bullet. Per-file detail lives in the `observer/` and `mcp/tools/` routes. Verification metadata pinned until closeout stamps the 2b code commit.
- 2026-06-13T11:15+02:00 — New `agents_remember.observer` service domain (slice 2a of the 3.0 browser-dashboard series): the observable-lifecycle event substrate write side — `ar-observer-event/v1` envelope, local ULID mint, append-only per-lifecycle event store — with its own route overview under this package. Added it to the Route Model; per-file detail lives in the new `observer/` route. Later slices add the ambient lifecycle + signal tools and the projection read side.
- 2026-06-12T19:06+02:00 — No route impact: the issue #83 changes under this route are the worktree-manager facade re-exports, the test additions, the 2.9.1 version bump, and the synced c-12-closeout and l-01-session-job-lifecycle skill copies (issue #83 doctrine plus the two-turn gate protocol); the closeout worklist behavior itself is documented at the `mcp/src/agents_remember/worktrees/modules` route, and the package layout/routing this overview describes is unchanged.
- 2026-06-11T15:20+02:00 — No route impact: carryover gained the memory-only-doc and entity-catalog candidate kinds inside memory/carryover.py and the c-11 packaged skill doc; route structure and module responsibilities on this route are unchanged (detail lives in the per-file cards).
- 2026-06-11T14:07+02:00: No route impact: re-verified against merged main `c2c2dcb` after the upstream doc-link/typo merges (PRs #69-#73) and the repository rename from `agents-remember-md` to `agents-remember`; card content already matched the source.
- 2026-06-11T06:47+02:00 — No route impact: issue #62 removed the `direct_closeout_*` tool surface (server registrations, payload builders, controllers, models, CLI subcommand, tests) — closeout is worktree-only; the package structure this overview describes is unchanged (detail in the file sidecars and sub-route overviews).
- 2026-06-10T10:26+02:00 — No route impact: package version bumped to 2.8.0 (`pyproject.toml`, `SERVER_VERSION` fallback) for the GitHub #54 release; runtime skills (l-01/c-09/c-11) teach the new freshness checkpoints; route behavior unchanged.
- 2026-06-10T09:56+02:00 — Issue #54 sub-task D: new `worktree_sync` tool (mid-task atomic base-pair sync) and the fetch-free `worktree_status` freshness block; route detail lives in the `worktrees/modules` overview.
- 2026-06-10T09:45+02:00 — Issue #54 sub-task C: carryover apply reports `memory_main_advance`, fast-forwarding memory main to the official checkout tip after the carryover commits.
- 2026-06-10T09:30+02:00 — Issue #54 sub-task B: `worktree_start` gained the stale-base preflight (behind/diverged source branches block with `stale_base_choice` recoveries) and the memory source branch auto-template; route detail lives in the `worktrees/modules` overview.
- 2026-06-10T08:39+02:00 — Issue #54 sub-task A: added `kernel/git_freshness.py` (branch-vs-upstream freshness kernel) and the opt-in `context_packet` `include_freshness` section with `ledgerMapsCodeHead`.
- 2026-06-10T08:15+02:00 — No route impact: package version bumped to 2.7.0 (`pyproject.toml`, `SERVER_VERSION` fallback) for the GitHub #53/#58 release; route behavior unchanged.
- 2026-06-10T07:40+02:00 — GitHub #53/#58: added the background-observability invariant (async worktree provider setup with durable heartbeat progress, stale projection, retry path) and the container-form argv invariant; shared context helpers moved to `providers/context_common.py` (facade re-entrancy fix).
- 2026-06-10T06:05+02:00 — No route impact: package version bumped to 2.6.0 (`pyproject.toml`, `SERVER_VERSION` fallback) for the GitHub #56 release; route behavior unchanged.
- 2026-06-10T05:50+02:00 — Issue #56 sub-task 3: the Hot Path Summary now records carryover route-overview candidates and guarded official-side index regeneration (`memory/carryover.py`).
- 2026-06-10T05:30+02:00 — Route body caught up with the 2.5.0–2.5.2 releases: content-gated provider readiness, the stdio subprocess invariant (#49), stall-watchdog doctrine, and the tool-report response-budget layer. Previous closeouts had only stamped the verification header (developer-flagged gap).
- 2026-06-10T05:20+02:00 — No route impact: sub-task 2 extended the body gates to route overviews and the c-05 skill doctrine; the route surface described in the sub-task 1 entry already covers both gates and the markers.
- 2026-06-10T04:47+02:00 — Issue #56 sub-task 1: added `kernel/onboarding_doc.py` (shared doc parsing + body/history classification) and the four-case sidecar body gate with in-band no-impact attestation markers to the route surface.
- 2026-06-09T14:52+02:00: Refreshed the MCP route overview against MCP 2.4.1 `main`; added the canonical root runtime asset sync boundary for package data.
- 2026-06-08T09:57+02:00: Re-verified the MCP package route after PR-39 restored context-packet provider-summary validation and made skipped-provider summaries a modeled optional-null contract.
- 2026-06-06T12:15: Re-verified against the current MCP package surface; corrected stale `mcp/tools.py` and provider lifecycle module references after the `mcp/tools/` package split and provider-first lifecycle packages.
- 2026-05-31T12:40+02:00: Removed the deleted `providers/integrity.py` runner-integrity prose and reference row after the provider-runner integrity feature was removed in the 1.0.0 remediation; `providers/status.py` no longer checks runner integrity.
- 2026-05-29T08:53+02:00: Updated after `server.py` began installing the `mcp/compact_content.py` shim that minifies tool-result text mirrors, and after dev-time tool-response conformance tests landed.
- 2026-05-28T19:52+02:00: Updated after public MCP response payloads were wired through Pydantic models, context packets moved to compact V2, provider diagnostics became the detail boundary, and controllers split by domain.
- 2026-05-28T13:40+02:00: Tightened MCP provider invariants to forbid CGC host `venvRoot`, host executable, and site-packages patch fallback paths.
- 2026-05-28T12:32+02:00: Updated after provider operator logs moved into the central `logs/` tree and provider status began writing current-state snapshots under `logs/providers/status/`.
- 2026-05-25T19:16+02:00: Updated after the legacy `provider_lifecycle.py` facade was deleted and `providers.lifecycle` became the sole lifecycle facade.
- 2026-05-25T19:01+02:00: Updated after provider lifecycle split into focused modules and GrepAI runtime became Docker-only without `_bin`, `_venvs`, host GrepAI, or host Ollama fallback.
- 2026-05-24T02:47+02:00: Updated after drift moved into `memory_quality.integrity` and `memory_quality_check` became the closeout quality gate.
- 2026-05-23T04:29+02:00: Created for the MCP package route after Phase 3 added MCP-owned runtime installation, provider layout convergence, and runner integrity checks.
