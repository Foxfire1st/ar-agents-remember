# agents-remember — Onboarding Overview

| Field | Value |
|---|---|
| repository | agents-remember |
| doc_type | `repo-overview` |
| sourceRoute | . |
| lastUpdated | 2026-07-08T23:59+02:00 |
| lastVerifiedCommitHash | `8dce306e203c35ffc95f84e610b4d3683e9521b5` |
| lastVerifiedCommitDate | 2026-07-09T11:38:39+02:00|

> **Status:** active baseline

## What This Repo Is

`agents-remember` is the source repository for the Agents Remember workflow system. It defines the doctrine, skills, MCP tools, task workflows, and design references that agents use to maintain durable onboarding knowledge beside code. Durable memory is reached through three retrieval substrates routed by `c-04-retrieval-strategy-router` skill: **by path** (a source file's deterministic one-to-one onboarding unit, verified against Git history), **by meaning** (semantic memory search over the onboarding), and **by relationship** (a code-relationship graph). By-path notes are the core and need no provider; meaning and relationship are served by opt-in Docker providers (GrepAI, CodeGraphContext) and return candidate routing evidence, not proof. Overviews and entity catalogs use route scopes or curated evidence fingerprints before an agent relies on them. The earlier sidecar-only, anti-retrieval positioning (no embeddings / no vector store) predated those providers and has been retired from the public spine and from this overview's framing.

The current checked-in guidance distinguishes `ar-memory/` as durable internal memory from `ar-coordination/` as local coordination. `c-08-ar-coordination-context-resolver` skill exposes that split through `code_repository_name`, `code_repository_root`, `memory_root`, and `coordination_root`, `c-09-git-worktree-manager` skill owns worktree lifecycle mutation, direct current-checkout closeout for approved micro edits, integration back to source branches, and (since L11) documents `task_reopen` — reopening a fully landed leaf task in place under its exact leaf id, and `c-10-adopt-memory-baseline` skill provides the adoption path for existing external-memory onboarding that needs an initial `memory.md` ledger.

The provider runtime guidance now routes through the MCP/package boundary:
MCP settings outside the coordinator are authority, coordinator files can only
teach the model what to ask for, and provider runtime state lives under one
coordinator provider root plus a central log root. Managed provider containers
run memory-capped since L12 (watchers 512m; a runaway OOM-recycles itself instead
of exhausting the host). Managed providers use
`providers/runners/` for provider instances, `providers/data/` for durable
provider database data, `logs/mcp/` for MCP transcripts, and `logs/providers/`
for provider operator logs/status/setup summaries. `providers/_bin/` and
`providers/_venvs/` are not managed executable contracts. Providers that need
databases, native binaries, or daemons should use Docker-wrapped managed mode;
GrepAI uses a workspace-mode PostgreSQL/pgvector Docker backend for multiple
memory roots, and CGC uses a Docker runner plus FalkorDB Docker backend for
configured code roots.

## Feature Inventory

This is the maintained current-state inventory of the system surface. When a
feature is added, removed, renamed, or moved between skills, MCP tools, package
modules, runtime assets, or public docs, update this section in the same
onboarding pass.

| Feature | What It Offers | Primary Surface |
| --- | --- | --- |
| Path-derived onboarding memory | Deterministic Markdown memory beside source files, plus route overviews and repo entity catalogs for larger scopes. | `README.md`, `onboarding/`, `c-05-create-or-update-onboarding-files` skill |
| Internal and external memory roots | Repo-local `ar-memory/` by default, selected external memory repos under `ar-coordination/memory-repos/ar-<repo>/`, and `memory.md` ledgers for code/memory alignment. | `c-00-initialize-memory-repo` skill, `c-08-ar-coordination-context-resolver` skill, `c-09-git-worktree-manager` skill, `c-10-adopt-memory-baseline` skill, `kernel/memory_ledger.py` |
| Context resolution and startup packets | Resolved code, coordination, memory, onboarding, task, temp, ledger, storage, path-rule, cross-repo, provider-summary, worktree, Git, and optional drift facts through compact `ContextPacketV2`; detailed provider state is intentionally excluded. | `c-08-ar-coordination-context-resolver` skill, `resolve_context`, `context_packet`, `ContextPacketV2` |
| Memory quality control | Task-start drift classification, closeout memory quality, new-file missing-onboarding checks, overview/entity fingerprint checks, and update-history style checks. | `c-02-memory-quality-control` skill, `drift_check`, `memory_quality_check`, `check_missing_onboarding` |
| Retrieval routing | Semantics, Relationship, and Intent routing across provider accelerators, route indexes, onboarding, and bounded source confirmation. | `c-04-retrieval-strategy-router` skill, `overview.index.json`, GrepAI tools, CGC tools |
| Onboarding bootstrap and slice maintenance | Repo bootstrap, route-local overview creation, evidence packs, file cards, onboarding waves, curator review artifacts, and route/slice refresh or deletion cleanup. | `c-03-repo-bootstrap` skill, `c-05-create-or-update-onboarding-files` skill |
| File and entity onboarding maintenance | File-level sidecars, inline onboarding adapter rules, repo entity catalogs, deterministic entity fingerprints, reference health checks, and generated route indexes. | `c-05-create-or-update-onboarding-files` skill, `route_index_refresh`, `kernel/route_index.py` |
| Findings capture | Confirmed current-state findings are routed to durable task-local artifacts and can be propagated into onboarding after verification and approval. | `c-01-findings-capture` skill |
| Workflow modes | The `l-01-agent-lifecycles` architect lifecycle's build decision at `decide`: a research-only exit for no-code answers, otherwise a `w-02-light-task-workflow` skill task — chat is never a build route, so one-session edits take the minimal artifact — escalating to a master + light sub-task series for larger phased work (the retired heavy workflow and the retired chat build are no longer modes). | `l-01-agent-lifecycles` skill, `w-02-light-task-workflow` skill |
| Agent lifecycles (one per role) | Developer-requested multi-agent series run through the unified `l-01-agent-lifecycles` skill: architect/backend orchestrator/designer/strategist/manager/worker/curator/system-specialist/reviewer role lifecycles (routed by AR_SPAWN_ROLE, a fresh role brief, or the architect default since 260707-HFX-L6; the 260707-HFX-L7 `system-specialist` role is the investigate-first provider-degradation responder — dispatched by the orchestrator on a `degradation-alert`, reports before any fix, escalates directly to the orchestrator; a spawn-first strategist run — the orchestration task, the sprint plan/scope — is the mandatory precondition for any orchestrated run since 260703-L12, and the reviewer runs standing criteria catalogs under the three-party-loop doctrine: 3-full-round cap, convergence rule, quo-vadis escalation), master-granular dependency dispatch, super integration branches off main, master branches off super, leaf branches off masters, C-11 carry-over at every edge, orchestrator worktree integration for master-to-super, final super-to-main PR plus main-memory carry-over, and two adversarial exit seams where reviewer verdict artifacts attach to handover gates as `reviewer-verdict` evidence. | `l-01-agent-lifecycles` skill, `skills/l-01-agent-lifecycles/roles/architect.md`, `skills/l-01-agent-lifecycles/roles/orchestrator.md`, `skills/l-01-agent-lifecycles/roles/reviewer.md`, `system/git-workflow.md` |
| Approval-gated closeout | Applicable authority gates for implementation, worktree-backed closeout, memory refresh, memory quality, and ledger alignment: standalone/final work uses explicit developer approval, while subordinate accepted-series work can proceed under recorded delegated series authority. Closeout is worktree-only — the direct current-checkout path was removed (issue #62). Body/history gates reject header-only or unmarked history-only onboarding refreshes for changed sources and their nearest-governing route overviews; explicit `No content impact:` / `No route impact:` Update History markers attest reviewed-no-impact and are surfaced in closeout payloads. | `c-09-git-worktree-manager` skill, `c-12-closeout` skill, `worktree_closeout_*` |
| Worktree lifecycle | Worktree start, attach, status, closeout preview/apply, integration, lifecycle finalization, cleanup, task contracts, replay/fast-forward integration, and external-memory compatibility checks. | `c-09-git-worktree-manager` skill, `lifecycle_finalize_task`, `worktree_*`, `worktrees/` |
| Observable session lifecycle | The 3.0 browser-dashboard substrate: an append-only `ar-observer-event/v1` event log with trust provenance, an ambient process-singleton lifecycle (six `lifecycle_*` signals, heartbeat, TTL sweep, tool-call attribution), and a pure projection reducer that folds events + file snapshots into resolved state (lifecycle tree, metrics, staleness, per-lifecycle token fuel gauge, drift/sidecar/setup/route/ledger analytical surfaces, precomputed action availability, and a server-computed attention queue). Task 27 adds a **lifecycle next-step hint engine** — every MCP tool response now carries a `nextStep` computed from the projected lifecycle state at the `_tool_payload` choke point (a one-time front-half prose rundown from `lifecycle_start`, then a linear per-tool chain that delegates to the worktree `guidance.lifecycle_guidance` state machine and points at the existing `lifecycle_gate` at gate junctions; built on the existing gate, with auto-firing a later step). Task 28 makes **NOTIFY-AND-CONTINUE** the active turn-end model: a new public `lifecycle_turn_end_notification` tool + a non-terminal `awaiting-developer` lifecycle state (notify the developer and stop — no gate, no wait — and the next AR tool call auto-resumes at the `_tool_payload` choke point), the next-step hints repoint off `lifecycle_gate` onto it, a one-line reducer dedup collapses the duplicate gate-open/blocked-gate attention item, and the old `lifecycle_gate`/inbox stack is parked (kept, un-hinted). Task 29 makes throwaway event/runtime surfaces lifecycle-aware: raw Event River lifetime is backend-retained by lifecycle state rather than frontend count caps, worktree provider/runtime facts require active enclosures, and actionable-drift attention carries repo/branch/source/memory provenance with targetless dismissal. | `agents_remember.observer`, `lifecycle_*` tools, `next_step.py`, `observer/` route overview, `docs/design/observable-lifecycle.md` |
| JSON-primary task documents | The `ar-task-document/v1` document is the source of truth for a task's plan + step/substep progress; `task.md` is a deterministic render of it. The `task_doc` MCP tool authors documents, including a schema-validated full-document `replace` operation for task resets/replans, and re-renders the markdown without parsing it back; the observer projects leaf docs per lifecycle (what a lifecycle is doing, including creation timestamp for reader ordering) and series **masters** folder-keyed (R1 — whole-series progress and authored master content, so a master is observable on the dashboard). Series leaf rows expose structured leaf `createdAt` metadata for oldest-first display without parsing task-name prefixes. Closes the machine-readable-task-registry gap (note-03 #8). | `agents_remember.tasks`, `task_doc` tool, `tasks/` route overview |
| Gate control plane | The durable, attributed record of decision points on a lifecycle (closeout/integration/cleanup approvals, agent questions, alarm acks): an append-only `ar-gate-record/v1` `GateRecord` + `GateStore` co-located with the observer event log. The public agent-facing MCP junction is `lifecycle_gate`: it creates the typed durable gate, blocks the active lifecycle with the developer-facing ask, waits for a developer decision or gate-specific inbox response, and can carry `required_decision`; lower-level gate payloads/stores remain the implementation substrate. `controlplane/enforcement.py` binds `worktree_closeout_apply` to a developer-approved `closeout-approval` gate, or to an opt-in delegated orchestration approval that passes the `gate_policy.py` rules; model self-approval and owner lifecycle self-approval remain non-binding. The default policy is all-human, human-pinned integration/push/cleanup gates are not configurable away, and delegated decisions can require reviewer-verdict evidence refs that surface on gate records/projections. Task 19 adds the single-current-gate invariant (new lifecycle gates expire older open lifecycle gates) plus targeted dashboard decisions via `gate_decide_for_lifecycle`. Lifecycle skills now raise `lifecycle_gate(kind=...)`, handle the returned developer decision or operator-inbox message from that public junction, and clear with `lifecycle_resume`, split across plan/worktree/closeout/push/integration/cleanup/agent-question gate kinds. Dashboard gate projection is live and now renders human-readable previews with raw JSON as diagnostics. | `agents_remember.controlplane`, `lifecycle_gate`, `gate_*` stores/tools, `controlplane/` route overview |
| Dashboard serving layer | The local mission-control server: `agents-remember dashboard` runs a FastAPI app over the observer projection — a multiplexed `state` SSE stream (snapshot + per-entity deltas), a one-shot state endpoint, a raw `event` SSE channel with byte-offset resume and a `ready` hydration marker after retained backlog replay, a POST action plane (slice 6b records gate-decision verbs as developer-attributed gate decisions; lifecycle transitions stay no-mutation; targetless actionable-drift dismissals persist acknowledgements), sim-mode replay, and the static cockpit bundle. Slice 6d begins **Mode B2** (the dashboard-hosted terminal): 6d-1 lands the terminal-host backend (`serving.terminal` — a `TerminalHost` registry of tmux-wrapped stdlib-`pty` sessions launching the harness render-not-scrape, fixed-argv/OS-user/localhost); 6d-2 adds the `/api/terminal/{session}` WebSocket bridge (PTY ↔ browser; + the `websockets` core dep), with the xterm.js visual (6e) to follow. Transport only (reads via the one coordination-state path abstraction); the frontend lives at the root-level `dashboard/` sub-project. Task 26 adds a **hot-reload dev env** — a `--reload` flag on the `agents-remember dashboard` CLI. 260703 L1 makes `--config` **optional** on that CLI: `cli/discovery.py` discovers the trusted settings by walking upward from the working directory (the settings convention before an `.mcp.json` registration's recorded path; nearest wins; a semantic usability probe keeps the repo's tracked placeholder template from shadowing real settings). 260703 L2 gives it **daemon mode**: `--daemon` detaches a supervised dashboard that survives the terminal (`--status`/`--stop` manage it; state + rotated log under `<coordinationRoot>/logs/dashboard/`; identity-checked liveness so pid reuse never resurrects a foreign process), and the fail-loud `dashboard` settings object (`autoStart`, `port`) has every MCP server boot ensure the daemon — adopt healthy, spawn absent, **restart on version mismatch** — through a threaded, total, stderr-only hook that can never break the stdio handshake. | `agents_remember.serving`, `agents-remember dashboard` CLI, `serving/` route overview, root `dashboard/` |
| Dashboard frontend (mission-control cockpit) | The browser cockpit (`dashboard/src/`): a near-read-only Vite + React 19 + TS-strict UI over the observer projection — model-C shell (top bar + rails + switchable viewport + event river + mode bar), cockpit panels plus the slice-6e Chats terminal, and a shared grammar/primitives library. Styled with the layered blueprint (slice 5d): **Panda CSS** (typed tokens + build-time/zero-runtime recipes) for styling + **React Aria** (headless a11y — the mode bar / pivot `ToggleButtonGroup`s and the lifecycle `ListBox`); the CRT effects layer isolated. Now a memory citizen (`dashboard/src/**` onboarded). As of slice 5e the **Engine Room** is an enclosure-centered, state-backed process map (`panels/engine-room/`) that makes the worktree manager's operating model legible — official line → code/memory worktrees → contract coupler → CGC/GrepAI engines — with observed/derived/planned/missing fact-state honesty, fed by a new server `analytics.engineProcesses` projection. **Slices 5f–5g** animate it as a worktree-lifecycle state machine on the prototype's **bird's-eye podracer canvas**: boot choreography (center-out engine charge + travelling conduit packets), failure overlays (steady blocked gates · isolated engine fault flicker · amber reindex reroute), and the **live/teardown** states (sync block · a terminal integration-conflict STOP · abandon dissolve); engines read **green when active** (empty off · cyan booting · red fault · amber reindex). The successful-landing arc (closeout train · PR/push · carryover · cleanup teardown) landed in **5h**; **5i** then made the canvas a dev scenario-player-driven build-up/tear-down stage; and **05k** completed the motion property-split onto GSAP timelines (`useEngineTimeline`) + Motion (`AnimatePresence`), CSS static. A **visual-parity pass** then completes the prototype fidelity: the atmospheric blueprint backdrop (5g G6) + a cockpit Effects/Calm toggle, the full HUD decal layer (canopy frame, engine spine + petals, the **left official-line engines** + conduits + coupler, lane annotations), and a fixed-height room layout via a `Panel` `fill` variant (the centre canvas + right panel stop resizing per selection; the side columns scroll). **Slice 05o** opens the engine room's **failure-mode** choreography (lifting the `podstage.html` non-happy-path scenes the canvas didn't yet drive, one mode at a time): **mode 1 (T3B memory/ledger block)** adds the **scan-ring** (the cyan pre-block ledger-verify sweep) + **ghosted-lane** (the held memory lane dims+desaturates while the code lane stays solid) primitives and the `memory-block` player scenario (verify → block → reconcile → provider clone → nominal), with a coupled engine-gauge polish (flat gold bezel, constant-gold petals). **Slice 05o Mode 2 (T1B stale-base block)** adds the **pruned-base-node** primitive plus the big red **fleeting-enclosure** box, and a failure-indicator polish pass anchors the verify/block pointers **ON the repository node** (topmost layer) and gives every alert overlay a Motion fade/pop transition. **Slice 05o completes the failure-mode library** — the canvas now drives all eight `podstage.html` failure modes (memory/ledger block, stale base, provider-plan block, seed fault, reindex reroute, live sync, integration conflict, abandon) on a shared set of node-anchored failure primitives (steady gate, scan ring, ghosted lane, pruned node, refused-conduit flash, moved badge, engine-dropout, terminal STOP, dissolve) with Motion fade/pop transitions. On the Task-6 control-plane branch the cockpit also gains its first interactive surfaces: **Slice 6e** adds the visible **Mode B2 terminal** — a full-bleed **Chats** view (`panels/Chats.tsx` + a code-split `Terminal.tsx` xterm.js wrapper) that renders the 6d PTY stream over the `/api/terminal` WebSocket (`data/terminal.ts` — keystrokes/resize ↔ raw PTY bytes), the cockpit's first bidirectional surface. **Slice 6e-2a** makes it a **create** surface: a "＋ Terminal" control spawns a **dashboard-owned** shell at the workspace root via the `POST /api/terminal` opener (`TerminalHost.open`, server-resolved command) — the dashboard owns the session it created. **Slice 6e-2b** adds per-harness launch buttons — a detection-driven button per *installed* harness (Claude Code / Codex / Pi.dev, via the new `GET /api/harnesses` + the `serving.harnesses` registry) beside ＋ Terminal, each spawning that agent at the workspace root. **Slice 6e-2c** moves the open sessions into a dedicated left-rail **session switcher** (`panels/SessionList.tsx` — a React Aria `GridList`, single-select = active session, per-row close ✕), replacing the horizontal tab strip, and unifies the harness buttons onto ＋ Terminal's golden look. **Slice 6e-3** adds **context injection** — a `SessionComposer` docked below the terminal sends a block of text into the active session's stdin as a bracketed paste (the on-ramp to 6f highlight→feedback). **Slice 6e-4** hardens terminal persistence — the open-session registry moves into a `data/sessions` store, and a live terminal survives both a cockpit *view* switch and a *session-tab* switch (kept mounted, hidden via CSS, never unmounted), while the backend PTY spawn gains a controlling terminal (`os.login_tty`) so tmux honors resize. **Slice 6f-1** adds the **highlight → context-package** composer — a cockpit text selection raises a React Aria popover to send the selection + a message into a chat session's stdin (single chat / a selector / create-on-Enter when none is open + ＋ new chat), reusing the live stdin channel; no silent action, not ACP. **Slice 6g** turns the detail panel into a **task-document reader**: a series **master** shows its overview (objective + ordered sections) + a clickable **sub-task index** with in-panel **drill-in** into each slice (the back/parent up-link in the sticky panel header), **markdown-rendered** task prose (a new `grammar/Markdown` primitive — react-markdown + remark-gfm, memoized), and **cross-master "→" navigation** that jumps between series lifecycles (a master links to a parallel/child series via the contract-paired projection). A **slice 07b polish** extends the engine-room G6 atmosphere to empty panels: a shared `panels/EmptyStateBackdrop` puts a faint, effects-gated boomerang-video backdrop behind the no-selection (detail) and no-session (chats) empty states — pure atmosphere (aria-hidden, absent under the Effects/Calm toggle / reduced-motion), the message always shown. Task 12 refines the topology constellation so backend-supplied repo coverage parents workspace provider satellites to repo nodes while worktree providers stay bound to their worktree groups; GrepAI `targetRepos` are addressable project targets inside one aggregate provider instance, not separate provider processes. **Task 33** scopes the topology to active work — an active-enclosure constellation (`workspace → source checkouts → active worktree enclosures`) that folds each lifecycle into its enclosure node and filters on a new served `activeWorktreeGroups` set (shared with the Engine Room's active admission). Task 29 S7 hides the former **Lifecycle Flow** tab from the cockpit while leaving `panels/FlowTab.tsx` dormant in source. | root `dashboard/`, `dashboard/src/` route overview, `@xterm/xterm`, `react-aria-components`, `@pandacss/dev` |
| Hosted chat leaf reassignment | Running dashboard-hosted chats can move their durable `leafKey` after creation without respawning their tmux/xterm session. The dashboard route and the public `attach_terminal_session_to_leaf` MCP tool share the same server-authoritative catalog policy, surface `leaf-taken` without local mutation, and broadcast/rehydrate `"leaf"` catalog changes so open tabs stay synchronized. | `attach_terminal_session_to_leaf`, `serving.terminal_leaf_assignment`, `dashboard/src/data/sessions.ts`, `dashboard/src/panels/Chats.tsx`, `dashboard/src/panels/RailChat.tsx` |
| Agent-facing session dispatch | One MCP tool spawns a role-configured, leaf-attached, context-primed hosted agent session by composing the existing session primitives — the shared serving opener (create + optional server-arbitrated leaf attach, `leaf-taken` surfaced never overridden), model/effort/env role knobs injected at `tmux new-session -e`, an echo-confirmed context-packet paste with optional submit (a worker auto-starts, a draft stays a draft), and spawned-by provenance on the catalog row for the dashboard orchestration tree. Each spawned session is its own harness process (the ambient-lifecycle singleton is untouched). No parallel spawn path: the dashboard route and this tool share one opener. | `spawn_agent_session`, `serving.terminal_opener`, `serving.terminal_paste`, `POST /api/terminal/{session}/paste`, `mcp/tools/terminal.py`, `models/terminal.py` |
| Agent orchestration communications | Durable agent-to-agent inbox messages address orchestrator/manager/worker roles, carry message-kind and artifact metadata, and remain pollable while also attempting hosted-session stdin push through the echo-confirmed paste seam. Turn reports and master handovers have typed artifact helpers/templates; inactivity or missing report nudges are rate-limited, logged as `orchestration.nudge`, and delivered to manager inboxes. | `operator_inbox_*`, `orchestration_nudge_manager`, `serving.inbox_delivery`, `controlplane/orchestration_artifacts.py`, `controlplane/orchestration_nudges.py`, `l-01-agent-lifecycles` templates |
| Event River lifecycle task labels | Event River readable history rows translate lifecycle-bound activity into task-facing context. When a retained event still has a lifecycle id but its live lifecycle projection is gone, the formatter uses projected task documents to show the task title before falling back to raw enclosure or lifecycle ids. The panel waits for raw-stream hydration before showing an empty feed and renders all retained rows it receives; backend lifecycle retention owns the cutoff. | `dashboard/src/panels/eventSummary.ts`, `dashboard/src/data/taskIdentity.ts`, `dashboard/src/panels/EventRiver.test.tsx` |
| Runtime and skill installation | MCP-owned install of coordinator `AGENTS.md` templates, packaged skills, system defaults, provider defaults, optional benchmark fixtures, and harness skill layouts. | `runtime_install`, `skills_install`, `install/`, `package_data/runtime/` |
| Harness starter packages | Harness-native first-run packages for Claude Code, Codex, Cursor, Antigravity, VS Code + Copilot, Hermes, Pi.dev, and OpenClaw. Each package carries MCP settings templates, skill folders, and either startup hooks or always-on instruction files that load the coordinator first-action directive. | `.claude/`, `.codex/`, `.cursor/`, `.agents/`, `.github-vscode/`, `.vscode/`, `.hermes/`, `.pi/`, `.openclaw/`, `docs/install/` |
| MCP server and authority settings | Installable stdio MCP server with trusted settings outside the coordinator root, allowed repo/provider scopes, timeout caps, transcript roots, and path containment. | `agents-remember-mcp`, `mcp/config.py`, `mcp/server.py` |
| Public MCP response contracts | Pydantic models for every public MCP tool response, registry coverage for the tool surface, compact strict contracts where the repo owns shape, flexible envelopes where provider/service-native details are intentionally passed through, and token metadata fields for later cost accounting. | `mcp/src/agents_remember/models/`, `PUBLIC_TOOL_RESPONSE_MODELS`, `test_models.py` |
| Provider lifecycle and discovery tools | Docker-managed GrepAI memory search/trace, CodeGraphContext symbol/caller/callee/dependency/complexity/visualization queries, compact provider status, dedicated provider diagnostics, watcher lifecycle, and current-state snapshots. Readiness is content-gated (2.5.0/2.5.1): graph/workspace content probes drive `indexed`/`indexing`/`empty`/`backend-unreachable` states for both providers, empty/unreachable targets degrade the global packet `ok`, crash-looping containers are not ready, and healthy-but-busy targets surface in the compact summary's `indexing` list. Provider launch is contained since 260707-HFX-L1: launch-capable operations (watcher start/restart/index rebuild, one-shot query runners, worktree provider setup, benchmark provider synthesis, the install rebind) re-read the on-disk MCP authority fail-closed — the boot snapshot is not launch authority, so `providers: {}` on disk is a live fleet-wide kill-switch — while stop/status/cleanup stay ungated; provider setup is serialized fleet-wide (one non-dry-run prepare at a time); and the dashboard daemon samples per-container containment metrics (label-discovered, read-only, dockerless-safe) that ride `provider_status`. | `provider_status`, `provider_diagnostics`, `provider_watchers`, `grepai_*`, `cgc_*`, `providers/`, `providers/metrics.py` |
| Tool response token budgets | Verbose tools (`runtime_install`, `provider_diagnostics`, `provider_watchers`, carryover plan/apply) keep compact outcomes inline and file bulk diagnostics under `temp/tool-reports/<tool>/` with an inline `reportPath` (keep-last-5 / 7-day write-time prune, secret redaction); budget tests are the regression line (2.5.1/2.5.2). | `mcp/tool_reports.py`, `compact_*_payload` builders, `test_tool_response_budgets.py` |
| Memory baseline adoption | One-time adoption of existing external-memory onboarding into the first ledgered baseline after drift/status review. | `c-10-adopt-memory-baseline` skill, `memory_baseline_*`, `memory/baseline.py` |
| Branch memory carryover | Carry richer onboarding from a source branch into official memory only after the corresponding code has landed. Candidates cover file sidecars and route overviews (route-keyed, `kind`-tagged): overviews whose route covers a landed path auto-carry only when branch and official content are identical (metadata re-verification), otherwise they are always review-required; official-side `overview.index.json` files are regenerated after carry — never copied — guarded on a clean official-ref checkout. | `c-11-memory-carryover-from-branch` skill, `memory_carryover_*`, `memory/carryover.py` |
| Branch-gated cross-repo context | Optional cross-repo context inclusion guarded by configured branch and memory-ledger checks. | `c-08-ar-coordination-context-resolver` skill, `crossRepo.allow` |
| Benchmark harness | Package-owned Codex benchmark fixtures, workspace preparation, paired source-only versus memory-enabled runs, JSONL/result capture, and metric summaries. | `codex_benchmark_prepare`, `codex_benchmark_run`, `benchmarks/` |
| Source quality tooling | Repository-owned quality wrapper for Ruff, Radon, pytest coverage, and CRAP-Calculator risk scoring. | `python -m agents_remember.code_quality.check`, `code_quality/` |
| Public docs and harness guides | User-facing setup, concepts, architecture, workflows, references, guides, and install notes for Codex, Claude Code, Cursor, Antigravity, VS Code Copilot, Hermes, Pi, and OpenClaw. | `docs/`, `README.md` |
| Canonical runtime, skills, and dashboard asset sync | Root runtime asset folders (`agents-md-files/`, `benchmarks/`, `providers/`, `system/`) are canonical editable assets synced into MCP package data by `scripts/sync-runtime.py`; root `skills/` is the canonical skill tree synced into MCP package data plus every harness starter skill folder by `scripts/sync-skills.py`; the built dashboard cockpit (`dashboard/dist/`) syncs into `package_data/dashboard/` by `scripts/sync-dashboard.py`. These sync checks are gated by githooks + CI and covered by `mcp/tests/test_sync_*`; the dashboard `--check` is source-aware — it fingerprints the build inputs into a sibling `dashboard.fingerprint`, so a `dashboard/src` change shipped without a rebuild is flagged at the commit gate, not only at push. | `scripts/sync-runtime.py`, `scripts/sync-skills.py`, `scripts/sync-dashboard.py`, `mcp/tests/test_sync_runtime.py`, `mcp/tests/test_sync_dashboard.py`, `.githooks/` |

Task 10 external-chat inbox current state spans three route families: the control-plane inbox
(`OperatorInboxEntry` / `OperatorInboxStore` plus the `operator_inbox_*` MCP tools), the dashboard
serving endpoint (`POST /api/operator-inbox`, trusted developer/dashboard attribution), and the
dashboard Gate Respond fallback (`GateResponder` calls `data/operatorInbox.postOperatorInbox` when no
hosted chat session is attached). Hosted chat injection remains preferred; the inbox is the pull-based
return channel for external agents that cannot receive direct dashboard injection.

Task 23/24 changes the lifecycle of those gate/inbox interactions: prompts, responses, pending pickup
signals, and attention-queue gate rows are disposable interaction data. They disappear when the
developer responds, dismisses a gate, clears the attention queue, the agent consumes the inbox entry,
or passive TTL cleanup reaches the 24-hour interaction window. The only durable lifecycle records are
the task/worktree documents, commits, contracts, and ledger rows.

Task 31 updates the root dashboard/provider current-state story: live dashboard projection now refreshes
provider current-state before serving snapshots, worktree provider stacks can be inspected from their
isolated runtime settings, and Engine Room renders expected provider roles as observed, configured-only,
failed/degraded, or missing instead of letting empty provider containers imply no expectation. The detail is
route-local under `mcp/`, `mcp/src/agents_remember/observer/`, `mcp/src/agents_remember/serving/`, and
`dashboard/src/panels/engine-room/`.

Task 29 S7 updates the root Event River and attention-queue story: raw events are retained by the
backend lifecycle policy and the frontend no longer hides rows with its own short cap, `/api/events`
emits a ready marker after retained backlog replay, actionable-drift notices name the affected
repository/memory pair, and only actionable drift can be dismissed without a lifecycle/worktree target.
The former Lifecycle Flow tab is hidden from the cockpit; `FlowTab.tsx` remains dormant source.

The 260628_operations-integration series (L1–L4 covered above under the files/Change-Set surfaces) adds
**L5**: the **sidebar leaf-keyed chat registry** — chat sessions are keyed to leaf enclosures and shown
in a left-rail switcher with a leaf-attach picker (`panels/RailChat.tsx`, `panels/LeafAttachPicker.tsx`,
`data/sessions.ts`/`taskIdentity.ts`) — plus an operations-dashboard **polish** pass (resizable
persisted rails, drill-state that survives a view switch, the File/Diff viewer rendering opened route
overviews as markdown and the corrected Change-Set selected-row highlight, the Hangar filtering archived
enclosures, and faint siege-tank/battlecruiser empty-state backdrops). L5 also lands a **lifecycle
event-retention correctness fix** at the observer boundary: the durable enclosure — not the prunable
lifecycle event log — is the source of truth for liveness, so a running worktree no longer vanishes from
the Engine Room when its log ages out, and a not-yet-retired master series protects every leaf's event
history from the inactivity TTL until the series is archived plus a one-week grace. **L6** keeps the chat
assignment timing explicit: when an operator starts an agent chat on the displayed leaf or attaches a free
chat through the leaf picker, the right-rail chat injects projected leaf task/worktree context into that
chat once for the successful bind. Detail lives in the `observer/`, `serving/`, and `dashboard/src/` route
overviews.

## Hot Path Summary

Use the root index to route quickly: `AGENTS.md` and `README.md` cover the source-checkout and public contracts, `mcp/` covers the package-managed MCP server, context packet, runtime install, skills install, provider lifecycle/setup, benchmark tools, settings, route-index generation, memory quality, worktree services, and memory services, `mcp/src/agents_remember/package_data/runtime/agents-md-files` covers installed instruction templates, the hidden harness starter package roots (`.claude/`, `.codex/`, `.cursor/`, `.agents/`, `.github-vscode/`, `.vscode/`, `.hermes/`, `.pi/`, `.openclaw/`) cover first-run harness files and startup directives, the flat `mcp/src/agents_remember/package_data/runtime/skills/C-*` skills cover core support (resolver, memory quality control, bootstrap, onboarding, route-index, memory, and worktree tasks), `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles` is the unified agent-lifecycles skill (the three-condition router — architect default since 260707-HFX-L6 — + minimal frame + the three-party-loop doctrine + nine `roles/` lifecycles (260707-HFX-L7 adds `system-specialist`) + `lenses.md` + ten report templates + the `criteria/` reviewer catalogs; there are deliberately no per-harness role files since the L8 de-harnessing; the canonical source is the root `skills/` tree synced by `scripts/sync-skills.py`), and `mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow` is the durable task workflow. Since L13 the kernel also hosts `agentic_settings.py` — the per-use two-layer agentic-settings loader (global `ar-coordination/system/settings.json` merged with `<repo>/system/settings.json`; the L12 orchestration knobs' parser; gateDelegation global-layer-only). Since L16 the repo also ships `docs/reference/harnesses.md` — the spawn-parameters manual (harness registry defaults + the `orchestration.harnesses` settings extension, every role knob and its delivery vehicle, the worked add-hermes example). For route-index behavior start at `mcp/src/agents_remember/kernel/route_index.py`, the `route_index_refresh` MCP tool, `c-05-create-or-update-onboarding-files` skill, and `c-04-retrieval-strategy-router` skill.

## Architecture At A Glance

```text
agents-remember/
  AGENTS.md
    source checkout instructions and installed-runtime handoff
  README.md
    public setup and conceptual model
  mcp/
    package-managed MCP server, runtime/skills install, provider lifecycle/setup, benchmark tools, settings, and integrity checks
  mcp/src/agents_remember/package_data/runtime/
    agents-md-files/
      coordinator/AGENTS.md
      skills/AGENTS.md
      system/AGENTS.md
      tasks/AGENTS.md
    skills/
      flat c-* core maintenance and resolver skills
      the `l-01-agent-lifecycles` skill and the `w-02-light-task-workflow` skill (the retired heavy workflow and its phase skills are no longer present)
    system/defaults/examples/
      coordinator and memory-repo example settings, sources, and tools files
  roadmap/
    design specs and historical planning notes

workspace ar-coordination/
  AGENTS.md
  skills/
  memory-repos/ar-agents-remember/
    memory.md
    onboarding/
      current onboarding baseline for this repo
  tasks/
    durable planning artifacts for worktree-support rollout
  temp/
    temporary generated artifacts such as drift reports
```

## Code Structure

| Area                 | Path                                                                                                                                                                            | Purpose                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Source checkout instructions | [AGENTS.md](agents-remember/AGENTS.md)                                                                                                                               | Defines how agents work on this source checkout and when to hand off to the installed runtime instructions.    |
| Public documentation | [README.md](agents-remember/README.md) and [docs](agents-remember/docs)                                                                                       | Keeps the root README as the public front door while focused docs pages own setup, concepts, architecture, workflows, install guides, guides, and reference material. |
| MCP package          | [mcp](agents-remember/mcp)                                                                                                                                                       | Package-managed MCP server exposing context, runtime install, skills install, provider, worktree, memory, benchmark, settings-derived lifecycle, and memory quality tools. |
| Core skills (C-*)    | [mcp/src/agents_remember/package_data/runtime/skills](agents-remember/mcp/src/agents_remember/package_data/runtime/skills)                                                                                                           | Resolver, memory quality control, repo bootstrap, onboarding maintenance, and related support skills — flat directly under `skills/`. |
| Lifecycle + task workflow | [mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles) and [mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow) | The unified agent lifecycles (router + minimal frame + per-role lifecycles), and the durable light task workflow (which escalates to a master + light sub-task series for larger work). |
| Roadmap and specs    | [roadmap](agents-remember/roadmap)                                                                                                                                           | Design specs, migration notes, and historical task plans. These are references, not onboarding substitutes.    |
| Runtime AGENTS templates | [mcp/src/agents_remember/package_data/runtime/agents-md-files](agents-remember/mcp/src/agents_remember/package_data/runtime/agents-md-files)                                                                                                        | Package-owned coordinator, skills, system, and tasks `AGENTS.md` templates for runtime installation.           |
| System defaults      | [mcp/src/agents_remember/package_data/runtime/system/defaults/examples](agents-remember/mcp/src/agents_remember/package_data/runtime/system/defaults/examples)                                                                                          | Example settings, sources, and tools files used as scaffolding material.                                       |

## Functional Areas

### Source Checkout Contract

`AGENTS.md` is the authoritative behavioral contract for agents operating on this source checkout. It now starts by separating the package source repository from the installed `ar-coordination` runtime: when the file is reached through a workspace-level pointer during sibling-repository work, agents should use the installed runtime `AGENTS.md` instead. For work on this repository itself, it keeps `agents-remember` as the resolver target, routes sessions by role through the `l-01-agent-lifecycles` skill (a spawned role follows its brief; a developer session runs the architect lifecycle on the request → trust-checkpoint → reframe-research → decide → build → close axis, whose build decision at `decide` is a research-only exit or a durable `w-02-light-task-workflow` skill task — chat is never a build route), requires `c-08-ar-coordination-context-resolver` skill resolution plus `c-02-memory-quality-control` skill memory quality control before relying on onboarding, separates implementation approval from commit approval, and points active settings reads at the resolved memory layer rather than a root-level source checkout `system/` directory.

### Public Documentation

The public README is now intentionally short: product positioning, a fast Core Features pitch, a core path-derived memory example, one generic quickstart, a ToC-linked **Run The Dashboard** section (260703 L3 — unpinned `uv tool install agents-remember-mcp` as the first-class install, flag-free discovery-backed `agents-remember dashboard`, daemon mode + the `dashboard.autoStart` key, pinning as the debugging path, one rc-period pre-release note; the PyPI `mcp/README.md` Install And Run carries the same story), harness install links, docs links, and a compact source/runtime layout. Detailed user-facing material moved under `docs/`: `docs/features.md` is the concentrated product tour, `docs/README.md` is the documentation index, `getting-started.md`, `concepts.md`, `architecture.md`, `workflows.md`, and `FAQ.md` own core narrative, `docs/install/` owns harness-specific setup, `docs/guides/` owns operational tasks, and `docs/reference/` owns exact runtime/settings/skill behavior. Its Status section states the current version (bumped every release) and that the 3.0 cockpit arc has shipped — the dashboard is served from the MCP package via the `agents-remember dashboard` CLI. A separate `docs/design/` subtree holds developer-facing design specs for in-flight major work — distinct from the user-facing pages above and from the historical `roadmap/` notes. Its entries include `docs/design/observable-lifecycle.md` (the approved 3.0 design for an observable, controllable session lifecycle — the browser-dashboard direction, issues #2/#43), `docs/design/harness-matrix.md`, and the **engine-room** design language: `docs/design/engine-room/engine-room-visual-language.html` (the canonical living spec for the engine-room visual primitives — state colours, motion, glow, timing) and `docs/design/engine-room/podstage.html` (the prototype the production canvas was built from). As of slice 05k, `docs/design/` is **in onboarding scope** — a `docs/design`-scoped `pathRules` rule (listed first; first-match-wins) onboards its `.html` + `.md`, registered in `system/sources.md` as Domain Documentation, while the rest of `docs/**` stays excluded — so the design specs are now first-class onboarded memory under `onboarding/docs/design/` rather than summarized only here. (The general `docs/` user-facing pages remain onboarding-excluded; README onboarding + this overview carry their durable summary.)

### Harness Starter Packages

The hidden root packages `.claude/`, `.codex/`, `.cursor/`, `.agents/`, `.github-vscode/`, `.vscode/`, `.hermes/`, `.pi/`, and `.openclaw/` are source-owned starter packages even though they do not have one-to-one file-level onboarding under the current path rules. They provide harness-native MCP registration templates, MCP authority settings templates, copied skill folders, and the first-action instruction surface for each harness. The authoritative startup directive is architect-exclusive on EVERY first-action surface across the nine packages (orchestrator-exclusive under 260703-L10; inverted by 260707-HFX-L6): a session with `AR_SPAWN_ROLE` set or a role brief as first message ignores the notice entirely — the brief is its session start — while a developer-facing session is the ARCHITECT and reads `ar-coordination/AGENTS.md`, then runs `skills/l-01-agent-lifecycles/roles/architect.md` with the trust checkpoint before relying on memory, `read_ar_files` (paired source+onboarding) until the build decision, the retrieval-strategy tally as evidence, and notify-and-stop at every developer hand-off. Backend orchestrators are spawned seats (`AR_SPAWN_ROLE=orchestrator`) that never converse with the developer; they relay decision items to the architect. The four hook `.md` files (`.claude`, `.codex`, `.cursor`, `.github-vscode`; emitters read the sibling `.md`) are byte-identical; the `.cursor/rules/agents-remember.mdc` and `.github-vscode/copilot-instructions.md` directive bodies are byte-identical to their package's hook (so the cursor/vscode-copilot install-doc "same directive" sentences hold); the instruction-file-only packages (`.agents/GEMINI.md`, `.hermes/HERMES.md`, `.openclaw/workspace/AGENTS.md`) and the Pi emitter (`.pi/extensions/agents-remember-start.ts`, which hardcodes the directive with the rendered workspace root) carry the same text placeholder-adjusted (`<PATH/TO/YOUR/PROJECTS_FOLDER>/ar-coordination/AGENTS.md`). Claude Code has one extra detection caveat in the install guide: copy `.claude/mcp/mcp.json` to the workspace-root `.mcp.json`, because Claude Code does not detect the MCP registration when that file only lives under `.claude/mcp/`.

### Runtime AGENTS Templates

`mcp/src/agents_remember/package_data/runtime/agents-md-files/` is the package-owned source for installed coordinator instructions. The current package has four installable templates: `coordinator/AGENTS.md` for the coordinator root, `skills/AGENTS.md` for compact C-* skill routing, `system/AGENTS.md` for the hard onboarding maintenance gate, and `tasks/AGENTS.md` for task-folder collaboration doctrine. `runtime_install` MCP tool installs those templates to `ar-coordination/AGENTS.md`, `ar-coordination/skills/AGENTS.md`, `ar-coordination/system/AGENTS.md`, and `ar-coordination/tasks/AGENTS.md`. Memory repos are not expected to provide a root-level `AGENTS.md`; repo-specific memory guidance lives in the memory layer's `system/*` files.

### Core Resolver And Memory Quality Control

`c-08-ar-coordination-context-resolver` skill resolves the active coordination context: topology, code repository, `coordination_root`, `memory_root`, onboarding/docs/system roots, settings paths, repo-specific task root, temporary artifact root, contract path, worktree group, ledger path, storage settings, path rules, and branch-gated cross-repo allowances. Without a task name, `task_root` is the repository namespace under `ar-coordination/tasks/<repo>/`; with a task name or contract, it is the concrete task folder. Path-rule defaults in `system/settings.json` now carry the standard generated/vendor/build/cache/IDE/env/Zone.Identifier excludes. For worktree-backed task names, `c-08-ar-coordination-context-resolver` skill resolves current wrapper folders first and persisted `*-ar` task folders second. `c-02-memory-quality-control` skill consumes that context and owns memory quality control: task-start drift verifies file-level onboarding metadata, overview `sourceRoute` metadata, inline digests, and repo entity `git-blob-set-v1` fingerprints against the current source state; pre-code-commit checks catch newly added files without onboarding; closeout checks combine drift integrity with memory style. Drift reports are temporary coordination artifacts under `temp_root`; even explicit report paths inside the durable memory repo should be redirected back to coordination temp.

### Onboarding Maintenance

`c-05-create-or-update-onboarding-files` skill owns file-level onboarding and repo-level entity catalogs. It is the maintenance path for creating or updating onboarding artifacts; `c-02-memory-quality-control` skill detects memory quality issues but does not rewrite onboarding content. File-level onboarding now records the nearest governing `overview.md` when route-local overview coverage exists, while remaining self-sufficient for the concrete source file. Entity catalogs carry one deterministic fingerprint row per entity over a small curated evidence file set; `c-05-create-or-update-onboarding-files` skill chooses and refreshes those paths after review. After closeout memory edits, `memory_quality_check` combines drift integrity with style checks such as newest-first update history ordering before the memory content commit. `c-05-create-or-update-onboarding-files` skill also detects route-level create, refresh, move, and deletion cleanup cases and routes those structural changes to `c-03-repo-bootstrap` skill `existing-memory-slice-maintenance`. Generated `overview.index.json` files live beside route overviews and expose route scope, covered sidecars, child routes, copied hot-path summaries, and mechanically derived source-anchor hints so `c-04-retrieval-strategy-router` skill can route cheaply before opening full overview prose.

### MCP And Context Provider Runtime

The runtime has optional local discovery providers, but they remain accelerators rather than proof. The MCP settings file, not coordinator `system/settings.json`, declares allowed providers and repositories for the MCP path. That file is also the LIVE provider launch authority (260707-HFX-L1): launch-capable operations re-read it from disk fail-closed instead of trusting a server's boot snapshot, so disabling providers on disk bites running servers immediately; stopping, status, and cleanup stay legal, non-dry-run provider setup runs one-at-a-time host-wide behind a HOST-scoped setup lock in the system temp dir (outside every prunable coordination root and benchmark workspace — the guarded resource is the host), and the dashboard daemon samples labeled provider containers into a central containment metrics store under `logs/observer/providers/` that `provider_status` attaches even while providers are disabled. `context_packet` reports provider and watcher state, `runtime_install` installs runtime assets and provider dependencies from package-local code, and `skills_install` copy-installs packaged skills into harness skill roots. Managed provider installs should be coordination-owned without host executable fallbacks: pinned requirements under `providers/requirements/`, provider instances under `providers/runners/`, durable databases under `providers/data/`, operator logs under `logs/providers/`, MCP transcripts under `logs/mcp/`, and patches under `providers/patches/`. `providers/_bin/` and `providers/_venvs/` are stale-artifact cleanup targets, not runtime authority. Database, native-binary, and daemon infrastructure should be Docker-wrapped rather than installed as host services.

GrepAI runs in workspace mode with explicit `{ projectId, path }` roots generated from MCP repository/memory settings. Current managed mode indexes live memory roots in place and git-ignores GrepAI's per-root `.grepai/` working directory instead of mirroring roots under a separate index-root tree. Its runtime config, state, cache, and home artifacts belong under `providers/runners/grepai/`; its shared PostgreSQL/pgvector Docker data belongs under `providers/data/grepai/postgres/`; and `.grepai/` content should not be treated as durable memory. Managed GrepAI prefers non-conflicting auto host ports (`61432` for Postgres, `61434` for Ollama) while keeping the Docker container service ports (`5432` and `11434`) inside the provider network. Worktree isolation clones the source GrepAI database into a worktree-scoped PostgreSQL backend and rewrites provider settings so containers, logs, and runtime paths are isolated while the logical workspace key remains reusable. CodeGraphContext keeps one provider instance per configured repo under `providers/runners/codegraphcontext/<repo-id>/.codegraphcontext/`, with all instances sharing the FalkorDB Docker data root under `providers/data/codegraphcontext/falkordb/`; worktree setup seeds CGC by exporting, path-rewriting, and importing an existing graph bundle. Seed/clone operations are guarded by stall watchdogs (kill on zero progress), never total-duration caps — the copy-instead-of-reindex mechanic is what makes rapid worktree provider deployment viable and it scales with index size by design; the CGC seed refuses when workspace and worktree HEADs differ and falls back to a full reindex. On stdio transport, package subprocesses must never inherit the server's protocol pipes (`stdin=DEVNULL` or piped input, AST-guarded; the 2.5.1 fix for the multi-minute tool hangs).

### Code Quality And Refactor Baseline

The source checkout now explicitly tells agents to run Ruff, Pyright, and Radon after Python implementation work, then use the resolved memory layer's `system/tools.md` for exact validation commands and `system/coding-guidelines.md` for repository-specific style rules. Coordinator-level tools examples keep global commands separate from repo-specific code quality tools, and the memory-repo tools example reserves a `Code Quality` section for lint, format, typecheck, test, build, and smoke-check commands.

The current `pyproject.toml` makes Ruff responsible for import/style/static hygiene and Radon responsible for complexity scouting. Ruff ignores line-length wrapping, high-branch/high-return/high-statement complexity warnings, and numeric sentinel warnings that are better reviewed through Radon or code review. Test files have targeted ignores for unused patched-callable arguments and import-path setup. Radon is configured to show `B` through `F` cyclomatic complexity, visible complexity scores, total/average output, and maintainability-index pressure points while excluding generated, cache, virtualenv, build, dist, and test paths.

The last quality sweep passed Ruff, Ruff format check, compile checks, MCP unit tests, and diff whitespace checks after safe formatting and cleanup. It also found refactor pressure that should feed Phase 06 rather than be hidden by formatter churn: `parse_settings_block` in `coordination_context_resolver.py` was the highest-complexity function seen in the sweep, and provider lifecycle/setup plus worktree and benchmark modules remain large enough to need package-level analysis before code motion.

### Task Workflows

`w-02-light-task-workflow` skill is the compact durable-task workflow used by the current worktree-support task stack. It creates a task wrapper folder and `task.md` once task class and naming are clear, stops for implementation approval, then treats the checklist, onboarding propagation, checks, and worktree-backed commit approval handoff as one implementation cycle. When refreshed external-memory onboarding is part of intake, the memory content and ledger are committed before `c-09-git-worktree-manager` skill starts worktrees.

### Bootstrap Memory Build

`c-03-repo-bootstrap` skill now treats the root repo overview as the minimum successful bootstrap and scales through route-local overview construction pillars, evidence packs, file cards, onboarding waves, curator reviews, and handoff artifacts. Its templates live beside the skill under `mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/` and define the shape of input ledgers, state files, coverage plans, governing route maps, overview cards, route-local overviews, docs packs, boundary packs, file cards, wave manifests, curator reviews, and final handoffs. Route-local overviews are durable memory in the mirrored onboarding hierarchy directly under the resolved onboarding root, not detached area appendices, and file-level onboarding links back to the nearest governing overview. Existing-memory slice maintenance handles added, moved, deleted, refreshed, and newly important routes without pretending the repo is blank; automated bootstrap starts after source inventory intake and stops at handoff before separate closeout approval.

### Worktree Support

The worktree and cross-repo roadmap specs are still useful design references, but core implementation now exists for the first support slice: memory ledger parsing/writing, worktree contract parsing/writing, `c-08-ar-coordination-context-resolver` skill contract-aware facts, the `c-09-git-worktree-manager` skill `start`, `attach`, `status`, `closeout`, `integrate`, `lifecycle_finalize_task`, and `cleanup` command surface, and the `c-10-adopt-memory-baseline` skill `status`/`adopt` adoption workflow for pre-existing external-memory onboarding. `c-00-initialize-memory-repo` skill initializes missing memory roots before `c-09-git-worktree-manager` skill worktree use. `c-09-git-worktree-manager` skill external-memory start blocks dirty source memory repos so a refreshed onboarding pass cannot be accidentally stranded outside the ledgered baseline. `c-09-git-worktree-manager` skill closeout dry-run is the non-mutating preview path before explicit commit approval, and real external-memory closeout commits code first, uses `c-02-memory-quality-control` skill memory quality control to produce the maintenance worklist, refreshes affected onboarding verification metadata and entity fingerprints, runs `memory_quality_check`, then commits memory content and ledger when clean. `lifecycle_finalize_task` is the terminal lifecycle operation after the branch edge has landed: it proves the landed commit is reachable from the local parent/source branch, verifies memory carryover, runs or verifies cleanup, and reconciles the JSON-primary leaf task plus immediate parent row to `Completed`; it does not attempt squash equivalence or recursively complete ancestors. Closeout is worktree-only: the former direct-closeout current-checkout path was removed (issue #62), so every closeout runs against a task contract.

### Observable Session Lifecycle

The `agents_remember.observer` package is the 3.0 browser-dashboard direction: it
makes a working session a first-class, observable entity. The **write side** is an
append-only, replayable `ar-observer-event/v1` event log with trust provenance
(declared vs observed vs inferred), an ambient process-singleton lifecycle (the six
`lifecycle_*` signal tools, a heartbeat ticker, and a TTL project-and-prune sweep),
and a `_tool_payload` emission hook that attributes every tool call. The **read
side** is a pure projection reducer — the single owner of interpretation — that
folds the event logs plus file snapshots into resolved state for any client
(dashboard, future TUI, or agent): the lifecycle/enclosure/provider tree, metrics,
staleness, the per-lifecycle token fuel gauge, the analytical surfaces (drift read
from a persisted snapshot, sidecar staleness, provider setup, route coverage, tool
reports, ledger currency), and precomputed action availability, written atomically.
The lifecycle-signal and gate substrates are now **adopted by the lifecycle
skills**, so the agent's behavior — not just the dashboard's reads — makes the
session observable: the `l-01-agent-lifecycles` developer-facing lifecycle (the
orchestrator pre-HFX-L6; the architect since the seat split, with spawned backend
orchestrators parking durable gates and relaying decision items) carries a **Gate
Choreography** (every approval junction calls public `lifecycle_gate`, which
blocks the ambient lifecycle, creates the durable kind-typed gate, and initializes
wait state; the **developer** resolves or sends a message — never the agent's own
model-attributed `gate_decide` — and the agent always *clears* with
`lifecycle_resume`), with the junctions split by kind across
the skills: `plan-approval`/`push-approval` (l-01), `worktree-intent` +
`integration-approval`/`cleanup-approval` (the `c-09-git-worktree-manager` skill),
and `closeout-approval` — which **is** the single commit gate — (the
`c-12-closeout` skill, now extended to the full raise→wait→clear pattern). This
completes the observable-lifecycle gate story end-to-end. Detailed per-file routing
lives in the `observer/` route overview; the full design (lifecycle entity, event
schema, enforced gates, the cockpit) is `docs/design/observable-lifecycle.md`. The
serving layer and the cockpit UI are later slices of the same series. **Task 27** adds
the **lifecycle next-step hint engine** ([next_step.py](agents-remember/mcp/src/agents_remember/mcp/tools/next_step.py)):
every MCP tool response now carries a `nextStep` computed from the projected lifecycle
state at the `_tool_payload` choke point — a one-time front-half prose rundown from
`lifecycle_start`, then a linear per-tool chain that delegates to the worktree
`guidance.lifecycle_guidance` state machine and points at the existing `lifecycle_gate`
at gate junctions; it is built on the existing gate, with auto-firing left to a later step.
**Task 28** then makes **NOTIFY-AND-CONTINUE** the active turn-end model: a new public
`lifecycle_turn_end_notification` tool drives a non-terminal `awaiting-developer` lifecycle
state (the agent notifies the developer and stops — no gate, no wait — and the next AR tool
call auto-resumes at the `_tool_payload` choke point via `resume_from_await`), the next-step
ACTIVE hints repoint off `lifecycle_gate` onto it, and a one-line reducer dedup
(`_lifecycle_attention`'s `... and lifecycle.gate is None`) collapses the duplicate
gate-open/blocked-gate attention item; the `lifecycle_gate`/inbox stack stays valid but
parked (un-hinted). Detail lives in the `observer/`, `mcp/tools/`, and `models/` route overviews.
Task 28 is also a **doctrine reframe** across the root skill trees (`skills/` and its mirrors
`.claude/skills/`, `.agents/skills/`, `.hermes/…`, `.codex/…`, `.cursor/…`, … = the `.` route): the
active-developer hand-off in `l-01-agent-lifecycles`, `c-09-git-worktree-manager`, and
`c-12-closeout` now teaches **notify-and-continue** at every junction (reframe / plan / worktree-intent /
commit-closeout / push / integration / cleanup / turn-end) — dry-run → chat report →
`lifecycle_turn_end_notification(summary=…)` + STOP, with the next turn's first AR tool call auto-resuming —
and parks block-and-wait `lifecycle_gate` (+ `lifecycle_resume`) and the operator inbox as the fallback. The
packaged bundle copies under `mcp/src/agents_remember/package_data/runtime/skills/` are propagated from the
canonical `skills/` by `scripts/sync-skills.py`.

### JSON-Primary Task Documents

The `agents_remember.tasks` package makes the task document machine-readable: the
persisted `ar-task-document/v1` JSON (status, info, requirements, step/substep
progress, decisions) is the source of truth, and `task.md` is a deterministic render
of it (the `w-02-light-task-workflow` `template.md` is the render spec). The `task_doc`
MCP tool authors documents — create, full-document replace for task resets/replans,
set status, set a step/substep, append a decision — and re-renders the markdown on
every write; the markdown is never parsed back. This
closes note-03 gap #8 (no machine-readable task registry) and is the per-lifecycle
work-content layer the observer projects (keyed by the contract's `lifecycle_id`) so
the dashboard can show step/substep progress. Scope covers `light`, `subTask`, **and**
`master` documents — a master carries a structured `subTasks` series index + an ordered
`sections` passthrough that preserves its bespoke prose, so a series wrapper is
machine-readable too; live adoption follows the runtime shipping `task_doc`. **R1 (masters
observable):** the observer now also projects `master` docs **folder-keyed**
(`read_series_documents` → `Analytics.series`), aggregating the declared `subTasks` checkboxes into
whole-series progress — so clicking a series master on the dashboard shows its overall progress, not
just per-lifecycle leaves. Task 17 extends that surface with master `objective` and structured leaf
`createdAt` metadata; dashboard readers can therefore show authored master content and default leaf
lists to creation order without interpreting filename or task-slug prefixes. It relates
to — but does not build — the parked neutral-repo task/contract sharing substrate
(issue #79). Detail lives in the `tasks/` route overview. (Slice 3c: commit 1 = engine +
tool; commit 2 = the `w-02-light-task-workflow` JSON-primary adoption and the observer
reader; commit 3 = master JSON support; reopened R1 = the folder-keyed series projection; reopened R2 = the heading-vs-outcome renderer fix (distinct `Step.outcome`); reopened R3 = the deferred-examples honesty field (`codeExamplesNote`); reopened R4 = leaf-doc fidelity (`statusNote`/`headerNotes`/freeform leaf sections) — all landed.)

### Dashboard Serving Layer

The `agents_remember.serving` package is the 3.0 dashboard's transport spine (slice 04): a
FastAPI app, launched by `agents-remember dashboard` (the new umbrella `agents-remember` CLI),
that serves the observer projection live. One shared projector ticks `project_and_write`,
diffs each projection against the last, and fans **per-entity deltas** out to every client
over a single multiplexed SSE stream (`GET /api/stream`: an `event:snapshot` then named
`lifecycle`/`enclosure`/`provider`/`metrics`/`analytics` upserts and `*.removed` markers);
`GET /api/state` returns the projection once. It is transport only — no interpretation, which
the reducer owns — and reads coordination state exclusively through `McpRuntimeConfig` +
`observer.paths` (North-Star #5), never raw host paths. Local-first: bound to `127.0.0.1`,
no auth in v1. The **frontend** is a root-level sub-project (`dashboard/`) whose built bundle
ships as `package_data/dashboard/` via `scripts/sync-dashboard.py` (mirroring
`sync-runtime.py`); slice 04 shipped a placeholder, and slice 05 (5a) now ships the real Vite/React cockpit, synced by `scripts/sync-dashboard.py` and gated by `sync-dashboard --check` in both githooks + CI. Slice 4b added
the raw `event` SSE channel (`GET /api/events`, byte-offset `Last-Event-ID` resume), sim-mode
replay (a replay clock + fixture feeder over the projector's `now`/`before_tick` seams, so the
frontend cannot tell sim from live), and the `POST /api/actions/{action}` plane
(validated against the reducer's `ActionAvailability`; slice 6b records gate-decision verbs as
developer-attributed gate decisions via `gate_decide_for_lifecycle`, lifecycle transitions stay no-mutation). Slice 05 (5b)
builds the read-only **cockpit** on this stream — the four core panels (attention queue, live
session strip, the two-axis BY REPO | BY LIFECYCLE operation tree, and the detail panel with the
Request→Close phase stepper + display-only gate banner) on the podracer state-grammar, fed the
server-computed `Analytics.attentionQueue`. **Slice 05 (5c)** then rebuilt the cockpit to represent
the real model (notes 01/03/06): the **lifecycle is the unit** — paused persistent lifecycles
synthesized from worktree contracts show even when idle — in one de-duped BY REPO | BY PHASE list; a
**task reader** rendering the full task document; a **per-worktree engine room** (each worktree's
CGC↔code / GrepAI↔memory stack); the lifecycle → worktree → provider spine; and the topology
constellation. This drove a projection correction (per-worktree provider stacks, full task content on
`TaskDocNode`, persistent-lifecycle synthesis) detailed on the `observer/` route, plus a `serving/`
sim/events fix. **Slice 05 (5d)** then re-architected the React/TS frontend and brought `dashboard/src/**` **into
memory scope** (now onboarded, governed by the `dashboard/src/` route overview): the ~1,200-line
global `tokens.css` monolith was retired into the layered blueprint — **Panda CSS** (typed tokens +
build-time/zero-runtime recipes) for styling and **React Aria** (`react-aria-components`) for headless
behavior/a11y (the mode bar + pivot `ToggleButtonGroup`s, the lifecycle `ListBox`), with the CRT
effects isolated in `index.css`. A dev `/dev/bench` gallery + `/dev/reference` mc2 mount + the
`build_rich_sim.py` 35-lifecycle stress fixture drive the screenshot-annotate review loop.
**Slice 6d** begins **Mode B2** — the dashboard-hosted terminal: 6d-1 lands the `serving.terminal`
host (a `TerminalHost` registry of tmux-wrapped stdlib-`pty` sessions that launch the real harness
render-not-scrape — raw VT bytes for xterm.js, fixed-argv with no shell-injection surface, OS-user
creds, localhost; the PTY/tmux spawn seam is injectable so CI drives a real kernel PTY without tmux),
6d-2 bridges it to the browser over the `/api/terminal/{session}` WebSocket — binary PTY bytes
out, JSON `stdin`/`resize` in, `{type:exit}` on child exit (the `websockets` dep is uvicorn's WS
impl); the xterm.js Chats tab (6e) follows. Task 22 makes those dashboard terminal sessions durable:
the serving layer persists a terminal catalog, rehydrates cataloged tmux sessions after browser
refresh/server restart, lets multiple browser tabs attach independent tmux clients to the same chat,
and keeps explicit `End`/terminate hidden across later exit bookkeeping. **Task 26** adds a
**hot-reload dev env** — a `--reload` flag on the `agents-remember dashboard` CLI. Task 29 S7 hides the
former **Lifecycle Flow** tab from the cockpit while leaving
[FlowTab.tsx](agents-remember/dashboard/src/panels/FlowTab.tsx) dormant in source.
**260707-HFX-L8** adds explicit seat lifecycle management on top of the catalog: server-authoritative
retirement (`POST /api/terminal/{session}/retire`, authority-policy-checked, provenance-stamped,
never a zombie row) with automated cleanup at the leaf-integrate and master-finalize completion
edges, post-spawn identity rename (`POST /api/terminal/{session}/rename`, label only, never role),
and a live turn-state badge (working/turn-ended/awaiting-input/stale) classified from pane text on
the existing liveness-sweep cadence. Detail
lives in the `serving/` + `observer/` + `dashboard/src/` route overviews.

## Cross-Repo References

This repository is currently selected into the workspace `/home/foxfire/Projects/ar-coordination` coordinator by path rules in the coordinator settings, but onboarding content should cite same-repo files for repository behavior and task files only as planning references.

| Finding                                                                                                                                                                                                                       | Citations            | Source Path                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ----------------------------------------- |
| The source checkout instructions distinguish this repository from the installed runtime, hand sibling-repo work to `ar-coordination/AGENTS.md`, keep `c-08-ar-coordination-context-resolver` skill plus `c-02-memory-quality-control` skill memory quality control as the context gate for this repo, and separate implementation approval from commit approval. | L1-L14; L28-L53; L84-L91 | [AGENTS.md](agents-remember/AGENTS.md) |
| The installed runtime system template defines the hard start-of-task onboarding trust gate: resolve context, call `context_packet` when configured, run drift detection, classify update candidates versus dirty work-in-progress, ask whether to update candidates, rerun drift after updates, and never silently drop or ignore onboarding after drift detection. | L1-L48 | [system AGENTS template](agents-remember/mcp/src/agents_remember/package_data/runtime/agents-md-files/system/AGENTS.md) |
| The source checkout instructions route repo-specific code quality checks through resolved memory-layer `system/tools.md`, tell agents to run Ruff, Pyright, and Radon after Python implementation work, and use `system/coding-guidelines.md` when present. | L60-L62; L90-L96 | [AGENTS.md](agents-remember/AGENTS.md) |
| The README now presents the public front door, a Core Features pitch, the generic quickstart, links to harness install pages, and a compact source/runtime layout.                                                                                                   | L1-L191            | [README.md](agents-remember/README.md) |
| The docs index owns the expanded documentation map for start-here docs, install guides, operational guides, and reference pages, and now includes `docs/features.md` as the concentrated product tour.                                                                                                   | L1-L46            | [docs/README.md](agents-remember/docs/README.md) |
| The source checkout carries hidden harness starter packages whose hook, rule, context, or extension startup surfaces load the coordinator first-action directive and now require the `l-01` deep-research retrieval-strategy evidence tally; the Claude Code install page also documents the required copy from `.claude/mcp/mcp.json` to root `.mcp.json` for MCP detection. | README L95-L119; Claude install L18-L31; install README L1-L25; starter instruction files L1-L37 | [README.md](agents-remember/README.md); [docs/install/claude-code.md](agents-remember/docs/install/claude-code.md); [docs/install/README.md](agents-remember/docs/install/README.md); [.claude hook](agents-remember/.claude/hooks/agents-remember-session-start.md); [.codex hook](agents-remember/.codex/hooks/agents-remember-session-start.md); [.cursor hook](agents-remember/.cursor/hooks/agents-remember-session-start.md); [.cursor rule](agents-remember/.cursor/rules/agents-remember.mdc); [.agents GEMINI.md](agents-remember/.agents/GEMINI.md); [.github-vscode hook](agents-remember/.github-vscode/hooks/agents-remember-session-start.md); [.github-vscode instructions](agents-remember/.github-vscode/copilot-instructions.md); [.hermes HERMES.md](agents-remember/.hermes/HERMES.md); [.openclaw workspace AGENTS.md](agents-remember/.openclaw/workspace/AGENTS.md); [.pi extension](agents-remember/.pi/extensions/agents-remember-start.ts) |
| The current feature inventory is supported by the public Core Features pitch, the full `docs/features.md` tour, runtime/tool-surface docs, MCP `PUBLIC_TOOLS`, response model registry, packaged skill reference, runtime layout, benchmark methodology, and source quality wrapper. | README L32-L48; features L1-L471; MCP README L64-L90; tools L50-L86; model registry L1-L85; skills L15-L46; runtime layout L1-L118; benchmarks L1-L31; quality wrapper L1-L140 | [README.md](agents-remember/README.md); [docs/features.md](agents-remember/docs/features.md); [mcp/README.md](agents-remember/mcp/README.md); [mcp/tools/](agents-remember/mcp/src/agents_remember/mcp/tools/); [tool_registry.py](agents-remember/mcp/src/agents_remember/models/tool_registry.py); [skills reference](agents-remember/docs/reference/skills.md); [runtime layout](agents-remember/docs/reference/runtime-layout.md); [benchmark methodology](agents-remember/docs/benchmarks-methodology.md); [check.py](agents-remember/mcp/src/agents_remember/code_quality/check.py) |
| Runtime asset sync treats root runtime folders as canonical and copies them into package data; the pre-commit hook runs the check form so package data does not silently drift from canonical assets. | sync-runtime L1-L168; test L1-L69; hook L1-L29 | [sync-runtime.py](agents-remember/scripts/sync-runtime.py); [test_sync_runtime.py](agents-remember/mcp/tests/test_sync_runtime.py); [pre-commit hook](agents-remember/.githooks/pre-commit) |
| MCP provider guidance requires Docker-wrapped provider backends instead of host-level services, live GrepAI memory roots, runtime artifacts under `providers/runners/grepai/`, PostgreSQL data under `providers/data/grepai/postgres/`, and `.grepai/` working directories treated as runtime artifacts rather than durable memory. | L79-L99 | [mcp/src/agents_remember/package_data/runtime/system/defaults/examples/coordinator/settings.md](agents-remember/mcp/src/agents_remember/package_data/runtime/system/defaults/examples/coordinator/settings.md) |
| The MCP settings example declares the external authority surface for repositories, provider ids, timeout caps, transcript roots, and package-derived provider runtime paths, replacing the removed coordinator `system/settings.json` provider template. | L1-L31 | [examples/mcp/settings.example.json](agents-remember/examples/mcp/settings.example.json) |
| The repository quality configuration leaves Ruff on import/style/static hygiene, delegates branch/statement complexity pressure to Radon, gives tests targeted patched-callable/import-setup ignores, and configures Radon to report `B` through `F` complexity plus maintainability pressure. | L1-L39; L59-L68 | [pyproject.toml](agents-remember/pyproject.toml) |
| The coordinator tools example says repo-specific code quality tools belong in the selected memory layer, while the memory-repo tools example provides a `Code Quality` section for lint, format, typecheck, test, build, and smoke-check commands. | L6-L7; L5-L14 | [mcp/src/agents_remember/package_data/runtime/system/defaults/examples/coordinator/tools.md](agents-remember/mcp/src/agents_remember/package_data/runtime/system/defaults/examples/coordinator/tools.md); [mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/tools.md](agents-remember/mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/tools.md) |

## Update History

- 2026-07-08T23:59+02:00 — No route impact: reviewed the repo overview as the nearest governing
  overview for `docs/reference/settings-json.md` (the `docs/reference` route has no local overview).
  The source doc gained the already-route-local `orchestration.supervisor.redeliverBudget` table row
  for HFX2-L8; this does not change the root feature inventory or routing model. A file-level sidecar
  now covers the settings reference directly. Verification metadata pinned until closeout stamps the
  260707-HFX2-L8 commit.

- 2026-07-08T15:27+02:00 — 260707-HFX2-L6 doctrine impact: the root approval-gated
  closeout row now reflects applicable authority rather than unconditional explicit approval:
  standalone/final work remains developer-approved, while subordinate accepted-series work can
  proceed under recorded delegated series authority. The synced runtime skill copies add
  task-seat takeover, developer clarification triage (close/current/small clarifications get
  implemented in the active leaf), and delegated series authority across l-01, c-09, and c-12.
  No repository structure, MCP tool signature, controller, provider, or serving route behavior
  changed. Detail lives in the `mcp/` route overview and touched skill sidecars.

- 2026-07-08T05:10+02:00 — No route impact: 260707-HFX2-L5 (doctrine inversion: "Monitor
  the worker"/"monitor turn-report artifacts" duty language across `skills/l-01-agent-lifecycles/
  {SKILL.md, roles/manager.md, roles/orchestrator.md, roles/worker.md, templates/turn-report.md}`
  rewritten to a passive process-and-ack contract, a new "no seat-local watcher" invariant
  (uniform-mechanism ruling 2026-07-07), and "idle is safe" framing — mechanically synced by
  `scripts/sync-skills.py` to the 9 downstream package copies — plus the new
  `mcp/tests/test_liveness_simulations.py`) is a doctrine consistency/wording pass formalizing an
  already-existing HFX2-L1..L4 supervisor-sweep/escalation-ladder mechanism this root overview does
  not itself narrate at any altitude. It changes HOW a seat reacts to missing signals (passive
  wake-and-ack vs. hand-rolled watching), not any package/route structure, and it does not touch the
  Observable Session Lifecycle paragraph's notify-and-continue interaction model this root overview
  already carries (that model — gate choreography, `lifecycle_turn_end_notification` — is unaffected;
  this leaf only bans ad hoc watchers layered on top of it). Route detail (the doctrine paragraphs,
  the new liveness-simulation test coverage, the Supervisor Sweep entity) lives in the `mcp/` route
  overview, `onboarding/entities.md`, and the touched file sidecars.
- 2026-07-08T04:25+02:00 — No route impact: 260707-HFX-L12 (master-exit fix leaf) closes a schema
  gap in the operator-inbox `AgentRole`/`InboxMessageKind` Literals so the ARCHITECT/ORCHESTRATOR
  decision-item relay this root overview's Agent lifecycles row already describes actually
  round-trips through the inbox — the row's own prose was already correct about the DESIGN; this
  leaf makes the CODE match it. No new role, no role-census change, no repository structure or
  routing delta. Route detail (the two new Literal members, the new round-trip test) lives in the
  `mcp/` route overview and the touched file sidecars.
- 2026-07-08T03:05+02:00 — 260707-HFX-L8 root route impact (seat lifecycle: retirement + live
  identity + turn-state, issues #12/#4): the Dashboard Serving Layer paragraph now records
  server-authoritative seat retirement (authority-policy-checked, provenance-stamped, automated at
  the leaf-integrate and master-finalize completion edges), post-spawn identity rename, and a live
  turn-state badge riding the existing L5 liveness-sweep cadence. Detailed behavior lives in the
  `serving/` route overview and the touched file sidecars.
- 2026-07-08T02:10+02:00 — No route impact: 260707-HFX-L11 (curator activation: change-set feeding
  + c-12/c-05 process rewiring) is entirely doctrine/dispatch-template prose inside `skills/`
  (roles/curator.md, roles/manager.md, templates/manager-brief.md, the new
  templates/curator-brief.md, c-12-closeout/SKILL.md, c-05-create-or-update-onboarding-files/SKILL.md,
  the l-01 SKILL.md companion-files list) — it changes WHICH SEAT writes onboarding and WHEN, not
  any package/route structure or public surface this root overview describes. Route detail (the
  new curator-brief template, the c-12/c-05 seat-routing wording) lives in the `mcp/` route
  overview's package_data/runtime/skills pillar and the touched file sidecars.
- 2026-07-08T01:00+02:00 — 260707-HFX-L7 curator memory pass (body): the Agent lifecycles Feature
  Inventory row and the root-index l-01 paragraph now name all nine role lifecycles including
  **system-specialist** (the investigate-first provider-degradation responder dispatched by the
  orchestrator on a `degradation-alert`, reporting before any fix, escalating directly to the
  orchestrator) — up from the HFX-L6 eight-role census. Route detail (the detector, the
  `providerDegradation` settings surface, the inbox `system-specialist` role/`degradation-alert`
  kind, and the doctrine additions to `roles/manager.md`/`roles/orchestrator.md`) lives in the
  `mcp/`, `serving/`, and `controlplane/` route overviews plus their file sidecars. Verification
  metadata pinned until closeout stamps the HFX-L7 commit.
- 2026-07-08T00:05+02:00 — No route impact: 260707-HFX-L5 (catalog liveness hysteresis) is
  serving-internal — the dashboard terminal catalog's stale-row handling moved from immediate
  exit marks to the evidence-scaled hysteresis owned by `serving.terminal_liveness`; this
  repo-overview's dashboard/terminal framing (Task 22 durability, Mode B2) stays accurate at this
  altitude, and the detail lives in the `mcp/` and `serving/` route overviews + file sidecars.
  Body reviewed, no change needed; route indexes regenerated for the HFX-L5 sidecar additions.
- 2026-07-07T23:05+02:00 — 260707-HFX-L6 curator follow-up (body): remaining pre-split routing
  wording corrected to the HFX-L6 seat split — the Workflow modes row's build decision belongs to
  the architect lifecycle; the Agent lifecycles row lists the eight role lifecycles
  (architect/backend orchestrator/designer/strategist/manager/worker/curator/reviewer, architect
  default) and now also references `roles/architect.md`; the root-index l-01 line reads eight
  `roles/` lifecycles with the architect-default router; the Source Checkout Contract paragraph
  routes a developer session to the architect lifecycle; the observable-lifecycle paragraph
  attributes the developer-facing Gate Choreography to the developer-facing seat (orchestrator
  pre-HFX-L6, architect since the split, backend orchestrators park gates and relay decision
  items). Historical entries untouched. Verification metadata pinned until closeout stamps the
  HFX-L6 commit.
- 2026-07-07T22:50+02:00 — 260707-HFX-L6 curator memory pass (body): the Harness Starter
  Packages paragraph now states the architect-exclusive startup directive — a developer-facing
  session routes to the ARCHITECT (`roles/architect.md`) per the HFX-L6 router inversion, while
  backend orchestrators are spawned, never-developer-facing seats relaying decision items to the
  architect. Closes reviewer finding F1 (the paragraph previously narrated the superseded
  260703-L10 orchestrator-exclusive directive). Verification metadata pinned until closeout
  stamps the HFX-L6 commit.
- 2026-07-07T21:05+02:00 — No route impact: 260703-L18 changes root-scope files only in place — skills/l-01 criteria catalogs gain candidate/standing tier updates (described in their package_data mirror sidecars) and docs/reference/settings-json.md + harnesses.md gain one rule sentence each (null refusal; effortSessionCommand template); the code fixes live in their own child routes (mcp, dashboard/src). The root route model and this overview's descriptions are unaffected.
- 2026-07-07T17:40+02:00 — 260707-HFX-L1 review fixes (delta): the setup lock is HOST-scoped in
  the system temp dir (not `providers/.setup.lock` — that root is pruned by `runtime_install`
  and benchmark roots are per-workspace), and the benchmark filter's no-authority default is
  fail-closed with an explicit env escape. Root prose corrected to match; detail in the `mcp/`
  and `runner_modules/` routes and the file sidecars. Verification metadata pinned until
  closeout stamps the HFX-L1 commit.
- 2026-07-07T16:50+02:00 — 260707-HFX-L1 (provider containment) body review: the provider feature
  row and the MCP/provider runtime area now carry the containment story — the on-disk authority
  is the live provider launch authority (fail-closed re-read for launch-capable operations; the
  boot snapshot is not launch authority; stop/status/cleanup ungated), provider setup is
  serialized fleet-wide, and the dashboard daemon samples label-discovered containment metrics
  (`providers/metrics.py`, new) that ride `provider_status`. Detail lives under the `mcp/`,
  `controllers/`, `serving/`, and `runner_modules/` route overviews and the file sidecars.
  Verification metadata pinned until closeout stamps the HFX-L1 commit.
- 2026-07-07T12:55+02:00 — L16 route impact (body): the root index names docs/reference/harnesses.md, the new spawn-parameters manual (the docs/reference route has no onboarding overview of its own — pre-existing gap, follow-up registered). Verification metadata pinned until closeout stamps the L16 commit.

- 2026-07-07T06:10+02:00 — No route impact: PR #100 merged the 260703_agent-orchestration series
  to main (`e358c4a`); the post-575a9a4 delta is two review fixes inside `mcp/` (agentic-settings
  empty-list refusal; reconciliation memory-source-branch guard) plus tests. Repo surface and
  Feature Inventory unchanged (detail under `mcp/`). Post-merge onboarding refresh, developer-approved.
- 2026-07-06T23:59:58+02:00 — No route impact: L14 is dashboard + mcp-internal (insignia, command tree, additive doc/session fields) — the repo surface this root overview describes is unchanged; details live in the dashboard/src and mcp sub-route overviews.

- 2026-07-06T23:55+02:00 — L13 owner follow-up (body): the root index names kernel/agentic_settings.py, the new two-layer agentic-settings loader (the builder's entry was history-only for this route). Verification metadata pinned until closeout stamps the L13 commit.

- 2026-07-06T15:40+02:00 — 260703-L12 route impact (three-party loops): the Agent lifecycles body row now names the strategist (spawn-first sprint planner; mandatory pre-run producing the orchestration task) and the loop doctrine (criteria catalogs, 3-full-round cap, convergence, quo-vadis); the root-index l-01 line updated to the six-role/ten-template/criteria census — and its stale "per-harness variants" phrase (dead since the L8 de-harnessing) removed. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-06T13:40+02:00 — 260703-L10 round 2 route impact (adversarial review L10R-1/L10R-2): the directive flip is now COMPLETE — the six remaining first-action surfaces (`.agents/GEMINI.md`, `.hermes/HERMES.md`, `.openclaw/workspace/AGENTS.md`, `.pi/extensions/agents-remember-start.ts` hardcoded block, `.cursor/rules/agents-remember.mdc`, `.github-vscode/copilot-instructions.md`) carry the orchestrator-exclusive text placeholder/format-adjusted per harness, restoring the cursor/vscode-copilot install-doc "same directive" claims; and the pre-convergence "build/job decision" compound was swept from the coordinator template (+ mirror), `c-04` SKILL.md (+ 9 mirrors), `mcp/server.py`'s `read_ar_files` docstring, and `docs/reference/mcp-tools.md`. The Harness Starter Packages paragraph above now states the full-surface coverage. Verification metadata pinned until closeout stamps the L10 commit.
- 2026-07-06T12:10+02:00 — 260703-L10 route impact (one-vocabulary sweep): the public surfaces now speak only the converged `l-01-agent-lifecycles` vocabulary — root `AGENTS.md` and the coordinator/skills templates route by role (Start Here — Route By Role; orchestrator plan gate; reframe-research phase), the four harness session-start hooks carry the orchestrator-exclusive directive (spawned roles ignore it; their brief is the session start), and `docs/**` (workflows, getting-started, features, llms.txt, FAQ, concepts, reference/skills with the l-02 row removed, reference/runtime-layout, install/claude-code, docs/README) plus the root README drop the dead `orient → ground → frame → decide` axis, the retired skill names, and the retired chat build (chat is never a build route). Body rows (Workflow modes, Source Checkout Contract, Harness Starter Packages) updated to match. Verification metadata pinned until closeout stamps the L10 commit.
- 2026-07-05T19:55+02:00 — No route impact: repo-level rows remain accurate — 260703-L8 cycle 7 is the adversarial-review-4 remediation (enclosure address validation + warning, dry-run guard reporting, canvas/doctrine/registry alignment), all inside existing routes. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T19:10+02:00 — No route impact: repo-level rows remain accurate — 260703-L8 cycle 6 is the adversarial-review-3 remediation (enforcement re-addressing, raise hygiene, doctrine/template/canvas alignment), all inside existing routes. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T18:24+02:00 — No route impact: repo-level rows remain accurate — 260703-L8 cycle 5 is the seam-channel remediation (server + doctrine internals documented at their routes) and the settings-json.md gate-delegation paragraph update. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T16:32+02:00 — 260703-L8 route impact (cycle 4, seam ruling): the master-exit handover gate is now the delegable `master-handover-approval` kind — the manager raises it with the reviewer verdict attached, the ORCHESTRATOR decides (human review concentrates at the super gate); `requireReviewerVerdictAtSeams` is wired (binds delegated seam decisions to verdict evidence); the reviewer role file is `roles/reviewer.md` (renamed to the server vocabulary, spawn value `reviewer`); templates gain `manager-brief.md`; the FlowTab canvas draws the converged doctrine (ROUTER in, FRAME/BUILD-JOB out). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T04:40+02:00 — No route impact: 260703-L8 de-harnessing pass is internal to the unified lifecycle skill (no per-harness role files); repo-level rows remain accurate — no repository structure or routing change.

- 2026-07-05T04:16+02:00 — No route impact: 260703-L8 reopened pass is internal restructuring of the unified lifecycle skill's role files; the repo-level feature rows (Agent lifecycles, Workflow modes) remain accurate as written — no repository structure or routing change.

- 2026-07-05T01:32+02:00 — 260703-L9 route impact: lifecycle convergence — `l-01-session-job-lifecycle` and `l-02-agent-orchestration` merged into the single `l-01-agent-lifecycles` skill (three-condition router + minimal frame in SKILL.md; `roles/` from jobs/; `lenses.md` from job-variants.md; templates gain worker-brief.md and the relocated deep-research-report.md); body rows, tree lines, and AGENTS.md description updated to the unified name and router semantics. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T23:43+02:00 — No route impact: L8 fixes the master change-set net diff resolver inside the existing MCP dashboard serving layer; the repo-wide feature inventory and top-level runtime subsystem boundaries are unchanged. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-04T13:16+02:00 — No route impact: 260703-L6 sharpened existing orchestration skill
  doctrine/templates for the two adversarial seams — master-exit and super-exit reviewer rubrics,
  verdict artifact variants under `notes/reports/`, and `reviewer-verdict` handover gate evidence refs.
  The repo feature inventory row now names that seam evidence contract; no top-level route or runtime
  subsystem was added. Verification metadata pinned until closeout stamps the L6 commit.
- 2026-07-04T13:03+02:00 — 260703-L5 route impact: added the Agent orchestration
  frame inventory row for the super integration branch topology: super from main,
  masters from super, leaves from masters, C-11 carry-over at every edge,
  orchestrator worktree integration for master-to-super, and final super-to-main
  PR plus main-memory carry-over. Verification metadata pinned until closeout
  stamps the L5 commit.
- 2026-07-04T12:32+02:00 — 260703-L4 route impact: the Gate control plane
  inventory now records opt-in delegated approvals, all-human defaults,
  human-pinned integration/push/cleanup gates, no owner self-approval, and
  reviewer-verdict evidence refs on gate records/projections. Verification
  metadata pinned until closeout stamps the L4 commit.
- 2026-07-04T12:31+02:00 - L3 route impact: added the Agent orchestration
  communications feature row for agent-to-agent inbox delivery, turn-report and
  handover artifact helpers, and rate-limited manager nudges. Verification
  metadata pinned until closeout stamps the L3 commit.
- 2026-07-04T11:20+02:00 — 260703-L1 route impact (small): the canonical `skills/` tree and every synced mirror gained `l-02-agent-orchestration` (the orchestration frame: SKILL.md + five jobs + two claude-code variants + six report templates); the root index enumeration now names it beside l-01/w-02. Runtime behavior unchanged (doctrine only). Verification metadata pinned until closeout stamps the L1 commit.
- 2026-07-04T11:10+02:00 — agent-orchestration L2 route impact: added the **Agent-facing session
  dispatch** feature — the public `spawn_agent_session` MCP tool that composes the existing session
  primitives (shared serving opener + optional leaf attach + echo-confirmed context paste + optional
  submit) to spawn a role-configured, leaf-attached, context-primed hosted session with model/effort/env
  knob injection and spawned-by provenance, so orchestrators spawn managers and managers spawn workers
  without dashboard clicks. New `serving.terminal_opener`/`serving.terminal_paste` modules + a
  `POST /api/terminal/{session}/paste` endpoint back it; no parallel spawn path. Added a Feature Inventory
  row; detail lives in the `mcp/tools/`, `models/`, and `serving/` route overviews. Verification metadata
  pinned until closeout stamps the L2 commit. (Distinct from the 260703-L2 daemon-supervision entry below.)
- 2026-07-03T12:59+02:00 — No route impact: 260703 L4 releases the series as MCP 3.0.0rc2 (version
  strings only: pyproject, SERVER_VERSION fallback, README Status; the Public Documentation
  paragraph's version reference became generic). Repo structure and behavior unchanged.
- 2026-07-03T12:58+02:00 — 260703 L3 route impact: the public README gains the ToC-linked
  `## Run The Dashboard` section (unpinned install first-class, daemon usage, autoStart key,
  pinning as debugging, rc-period note) and the PyPI `mcp/README.md` Install And Run carries the
  same story; commands verified against real PyPI resolution. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-07-03T12:57+02:00 — 260703 L2 route impact: the dashboard gains daemon mode
  (`--daemon`/`--status`/`--stop`, state under `logs/dashboard/`) and MCP-boot supervision via the
  new fail-loud `dashboard` settings object (`autoStart`, `port`) — adopt healthy, spawn absent,
  restart on version mismatch. Verification metadata pinned until closeout stamps the code commit.
- 2026-07-03T12:55+02:00 — 260703 L1 route impact: `agents-remember dashboard` runs flag-free —
  the new `cli/discovery.py` resolves the trusted settings from the working directory upward when
  `--config` is omitted. Verification metadata pinned until closeout stamps the code commit.
- 2026-07-03T12:50+02:00 — No route impact: L15 push-gate fixups — mechanical ruff/pyright compliance so the series passes its own pre-push quality gate; no behavior change anywhere.
- 2026-07-03T11:20+02:00 — L14 route impact: the repo is released as MCP 3.0.0rc1 — the first version serving the mission-control dashboard from the MCP package via the agents-remember dashboard CLI; README Status states the shipped 3.0 arc.
- 2026-07-03T02:58+02:00 — No route impact: L13 reopen drill second cycle (marker comment extension only).
- 2026-07-03T02:40+02:00 — No route impact: L13 reopen drill: a test-conftest marker comment only, used to live-fire the L11 task_reopen cycle.
- 2026-07-03T01:55+02:00 — L12 route impact: provider memory caps in the compose templates and CGC watch hygiene (enriched ignore rules reach the live watcher; timer-pop patch; package_data bundle excluded from watch/index).
- 2026-07-03T00:35+02:00 — L11 route impact: task_reopen tool (reopen a completed leaf in place; exact leaf id, no -rN forks) added to the MCP surface and documented in the c-09 skill; dashboard and observer stop special-casing suffixed reopens.
- 2026-07-02T21:45+02:00 — No route impact: the L10 enclosure-to-doc binding repair stays inside the
  observer projection join (`snapshots.py`) and the sidebar admission (`panels/LifecycleList.tsx`);
  the repo-wide feature inventory is unchanged at this granularity. Detail lives in the observer and
  panels route overviews and the changed file sidecars. Verification metadata pinned until closeout
  stamps the L10 commit.
- 2026-07-02T20:55+02:00 — No route impact: the L8-r1 correction stays inside
  `dashboard/src/panels/HighlightComposer` (+ tests) plus the regenerated package-data bundle; the
  repo-wide feature inventory is unchanged at this granularity. Detail lives in the
  `dashboard/src/panels` overview and the changed file sidecars. Verification metadata pinned until
  closeout stamps the L8-r1 commit.
- 2026-07-02T20:15+02:00 — No route impact: operations-integration L8 stays inside the dashboard
  frontend (`dashboard/src/panels` + `dashboard/src/data` + the cockpit shell wiring) plus the
  regenerated package-data bundle; the repo-wide feature inventory is unchanged at this granularity.
  Detail lives in the `dashboard/src` and `dashboard/src/panels` overviews and the changed file
  sidecars. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-02T18:40+02:00 — No route impact: operations-integration L7 corrected the CGC dependency
  guidance at the canonical `skills/` root (`analyze deps <module>` instead of the stale
  `analyze dependencies`) and re-ran `sync-skills` so every generated harness package copy matches;
  the wrapper argv fix itself lives in `controllers/provider_tools.py`. The repo-wide feature
  inventory is unchanged at this granularity. Verification metadata pinned until closeout stamps the
  L7 commit.
- 2026-07-02T17:25+02:00 — No route impact: the reopened-L6 copy-mode escape is confined to the
  serving terminal host's stdin path; the repo-wide feature inventory is unchanged at this
  granularity. Detail lives in the `mcp/src/agents_remember/serving` overview and the changed file
  sidecars. Verification metadata pinned until closeout stamps the follow-up commit.
- 2026-07-02T17:04+02:00 — L9 feature inventory impact: added hosted chat leaf reassignment as a surfaced
  feature spanning the public MCP tool, serving catalog move helper, and dashboard session/RailChat
  synchronization path. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-02T16:35+02:00 — No route impact: the reopened-L6 wheel/paste fixes stay inside the existing
  dashboard `Terminal`/session-delivery surfaces and the serving terminal host (per-session tmux mouse
  mode); the repo-wide feature inventory is unchanged at this granularity. Detail lives in the
  `dashboard/src`, `dashboard/src/panels`, `mcp/src/agents_remember/serving`, and changed file
  sidecars. Verification metadata pinned until closeout stamps the follow-up commit.
- 2026-07-02T15:03+02:00 — No route impact: the L6 alternate-buffer wheel follow-up is limited to the
  existing dashboard `Terminal` wrapper and the generated package-data dashboard bundle. The repo-wide
  feature inventory is unchanged at this granularity; detail lives in the `dashboard/src`,
  `dashboard/src/panels`, `mcp`, and changed file sidecars. Verification metadata pinned until closeout
  stamps the follow-up commit.
- 2026-07-02T13:16+02:00 — No route impact: reopened L6 frontend follow-up stays inside the existing
  dashboard frontend/session and panels routes; repo-level feature inventory is unchanged. The behavioral
  detail lives in the `dashboard/src`, `dashboard/src/panels`, and changed file sidecars. Verification
  metadata pinned until closeout stamps the L6 follow-up commit.
- 2026-07-01T01:43+02:00 — No route impact: L6 added bind-time context handoff to the existing
  right-rail leaf chat and rebuilt/re-synced the generated dashboard package bundle. The repo-wide feature
  inventory's dashboard/frontend/MCP package model is unchanged at this granularity; detail lives in the
  `dashboard/src`, `dashboard/src/panels`, and `mcp` route overviews plus the changed file sidecars.
  Verification metadata pinned until closeout stamps the L6 commit.
- 2026-06-30T00:00:00+02:00 — operations-integration L5 route impact: added the L5 paragraph to the Observable session
  lifecycle narrative — the sidebar leaf-keyed chat registry (`RailChat`/`LeafAttachPicker`/`sessions`/
  `taskIdentity`), the operations-dashboard polish pass (resizable persisted rails, view-switch-durable
  drill-state, File/Diff viewer markdown overview rendering + corrected Change-Set row highlight, Hangar
  archived-enclosure filter, empty-state backdrops), and the lifecycle event-retention correctness fix
  (durable enclosure is the liveness source of truth; a live master series protects its leaves' event
  history from the inactivity TTL until archived + a one-week grace). Detail lives in the `observer/`,
  `serving/`, and `dashboard/src/` route overviews + file sidecars. Verification metadata pinned until
  closeout stamps the L5 code commit.
- 2026-06-29T23:18+02:00 — No route impact: `worktree_start` now records the memory base from the source branch tip (not the repo HEAD) deep under `mcp/`; nothing at the repo-overview level changes (detail in the start.py file sidecar; task 260629_post-landing-cleanup L3).
- 2026-06-29T22:57+02:00 — No route impact: `task_doc` gained a `remove_subtask` op deep under `mcp/`; nothing at the repo-overview level changes (detail in the task_doc_tools.py file sidecar; task 260629_post-landing-cleanup L2).
- 2026-06-29T17:00+02:00 — No route impact: operations-integration L4 review follow-up — the Change-Set Viewer's series/master view is now the inspectable NET diff (`git diff <master-base>..<series-tip>`, via `master_file_diff`), and the shared code view gained comment/operator readability + a split-diff scroll fix — documented in the `dashboard/src/`, `panels/changeset/`, `panels/file-viewer/`, and `serving/` route overviews + file sidecars. The repo-wide feature inventory's Dashboard frontend summary is unchanged at this granularity. Verification metadata pinned until closeout stamps the L4 follow-up commit.
- 2026-06-29T16:40+02:00 — No route impact: operations-integration L4 added the **Change-Set Viewer** screen (`dashboard/src/panels/changeset/`) — a task-scoped takeover consuming the L3 `GET /api/changeset/*` API with a CodeMirror `@codemirror/merge` diff, reusing L2's panes — documented in the `dashboard/src/`, `panels/`, and new `panels/changeset/` route overviews + file sidecars. The repo-wide feature inventory's Dashboard frontend summary (a near-read-only cockpit with switchable centre views) is unchanged at this granularity. Verification metadata pinned until closeout stamps the L4 code commit.
- 2026-06-29T15:30+02:00 — No route impact: operations-integration L3 added the read-only change-set backend (`serving/changeset.py` → `GET /api/changeset/{task,file-diff,master}`: per-file code+memory diff counts, before/after content, master accumulation) over the L1 scope resolution, plus the `serving/scope.py` extraction and a `worktrees/modules/git.py` counts primitive — documented in the `serving/` and `worktrees/modules/` route overviews + file sidecars. The repo-wide feature inventory's Dashboard serving layer summary is unchanged at this granularity. Verification metadata pinned until closeout stamps the L3 code commit.
- 2026-06-29T09:06+02:00 — No route impact: operations-integration L2 added the **File Viewer** centre tab (`dashboard/src/panels/file-viewer/`) — a read-only, dual-pane code+onboarding browser that is the first consumer of the L1 read-only `GET /api/files/*` API — documented in the `dashboard/src/`, `panels/`, and new `panels/file-viewer/` route overviews + file sidecars. The repo-wide feature inventory's Dashboard frontend summary (a near-read-only cockpit with switchable centre views) is unchanged at this granularity. Verification metadata pinned until closeout stamps the L2 code commit.
- 2026-06-28T22:41+02:00 — No route impact: operations-integration L1 added the read-only `GET /api/files/*` dashboard files API (a serving-layer addition documented in the `serving/` route overview); the repo-wide feature inventory's Dashboard serving layer summary is unchanged. Verification metadata pinned until closeout stamps the L1 code commit.
- 2026-06-28T20:30+02:00 — No route impact: a `find_worktree_contract` archive-skip + docstring fix deep under `mcp/`; nothing at the repo-overview level changes (detail in the contracts.py file sidecar; task 260628_post-landing-cleanup).
- 2026-06-28T16:17+02:00 — Task 35 route impact: the dashboard asset sync gate (`scripts/sync-dashboard.py
  --check`, run by `.githooks/`) became source-aware — it fingerprints the dashboard build inputs into a
  sibling `dashboard.fingerprint` and flags a `dashboard/src` change shipped without a rebuild, the way the
  skill gate flags a changed skill; the frontend `LifecycleList` reopen-task nesting fix is covered by the
  `dashboard/src` route overview. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-28T13:54+02:00 — No route impact: task 34 changed activity-decaying heartbeat emission,
  inactivity-keyed raw Event River retention, the `/api/events` single-scan / heartbeat-filtered /
  chunked-backlog channel, and the dashboard event-store sliding window + Event River virtualization
  within child files (covered by their file-level sidecars and the `observer/`, `serving/`,
  `dashboard/src/`, and `dashboard/src/panels/` route overviews); this route's purpose/structure is
  unchanged.
- 2026-06-28T07:45+02:00 — Task 33 route impact (light): the dashboard-frontend feature row notes the
  active-enclosure topology scoping that landed in leaf 33 (an `activeWorktreeGroups` projection field,
  shared with the Engine Room's active admission, with the lifecycle/task rim folded into the enclosure
  node). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-28T07:43+02:00 — Task 29 S7 root route impact: surfaced the current Event River boundary
  (backend lifecycle retention, raw-stream `ready`, no frontend count cap), actionable-drift
  provenance/targetless dismissal, optimistic attention suppression, and the hidden Lifecycle Flow tab.
  Route detail lives under `mcp/`, `observer/`, `serving/`, `controlplane/`, `memory_quality/`,
  `dashboard/src/`, and `dashboard/src/panels/`. Verification metadata pinned until closeout stamps the
  task-29 code commit.
- 2026-06-28T03:33+02:00 — No route impact: task 32 is scoped to mcp-internal drift snapshot
  retention for the observer/worktree cleanup surface; the top-level feature inventory already routes
  this behavior through the MCP/observer/worktree entries, and no repository-level surface changes here.
  Verification metadata pinned until closeout stamps the task-32 code commit.
- 2026-06-28T03:21+02:00 — Task 31 route impact: refreshed the root overview body for dashboard/provider
  current-state honesty: live projection refreshes provider state, isolated worktree provider containers are
  inspected, and Engine Room keeps expected-but-missing provider roles visible. Route detail lives in the
  MCP, observer, serving, and dashboard panel overviews. Verification metadata pinned until closeout stamps
  the task-31 code commit.
- 2026-06-27T22:00+02:00 — Task 28 SKILL / doctrine reframe (`.` root route): the active-developer
  hand-off taught by the root skill trees (`skills/` plus the mirrors `.claude/skills/`, `.agents/skills/`,
  `.hermes/…`, `.codex/…`, `.cursor/…`, `.github-vscode/…`, `.openclaw/…`) moved from block-and-wait
  `lifecycle_gate` to **notify-and-continue** `lifecycle_turn_end_notification` across
  `l-01-session-job-lifecycle`, `c-09-git-worktree-manager`, and `c-12-closeout` — every junction (reframe /
  plan / worktree-intent / commit-closeout / push / integration / cleanup / turn-end) now runs dry-run →
  report → notify-and-stop, with the next turn's first AR tool call auto-resuming and auto-dismissing the
  attention item (no `lifecycle_resume`); `next_step.py` repoints onto the notification and the
  `lifecycle_gate`/operator-inbox stack is parked as the fallback. The packaged bundle copies under
  `mcp/src/agents_remember/package_data/runtime/skills/` are sync-propagated from canonical `skills/` via
  `scripts/sync-skills.py`. Acknowledged in the root overview body; junction-level detail lives in the
  l-01/c-09/c-12 skill sidecars. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T20:16+02:00 — No route impact: the task-27 follow-up adds a gate-await branch to the
  lifecycle next-step engine ([next_step.py](agents-remember/mcp/src/agents_remember/mcp/tools/next_step.py)) —
  a `blocked` lifecycle now hints `lifecycle_resume`, carrying the chain through the open gate. The
  feature is already in this root inventory and the repo route model is unchanged (detail in the file
  sidecar). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T18:43+02:00 — Tasks 26+27 root route impact: surfaced two new features in the feature
  inventory. **Task 27** adds the **lifecycle next-step hint engine**
  ([next_step.py](agents-remember/mcp/src/agents_remember/mcp/tools/next_step.py)) — every MCP tool
  response now carries a `nextStep` computed from the projected lifecycle state at the `_tool_payload`
  choke point (a one-time front-half prose rundown from `lifecycle_start`, then a linear per-tool chain
  that delegates to the worktree `guidance.lifecycle_guidance` state machine and points at the existing
  `lifecycle_gate` at gate junctions; built on the existing gate, auto-firing a later step); refreshed
  the Observable session lifecycle row + Observable Session Lifecycle functional area. **Task 26** adds
  the dev-facing **Lifecycle Flow** tab ([FlowTab.tsx](agents-remember/dashboard/src/panels/FlowTab.tsx))
  visualizing the build-job lifecycle and a **hot-reload dev env** (`--reload` on the dashboard CLI);
  refreshed the Dashboard frontend + Dashboard serving Feature Inventory rows and the Dashboard Serving
  Layer functional area. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T15:24+02:00 — Task 22 root route impact: the Dashboard Serving Layer paragraph now records
  durable terminal catalog persistence, refresh/server restart rehydration, multi-tab terminal attach,
  and sticky explicit termination as repo-level dashboard serving behavior. Detailed behavior lives in
  the serving route overview, dashboard source route, and file sidecars. Verification metadata pinned
  until closeout stamps the follow-up code commit.
- 2026-06-26T19:40+02:00 — Task 20 reopened root route impact: added the Event
  River lifecycle task label feature-inventory row so retained event-history
  rows whose live lifecycle projection is gone are still documented as
  task-title-first. Detailed behavior lives in the dashboard source route,
  panel route, and file sidecars. Verification metadata pinned until closeout
  stamps the reopened task-20 code commit.
- 2026-06-26T18:43+02:00 — Regression fix: root gate-control-plane row now
  states that `lifecycle_gate` blocks until a developer decision or gate-specific
  inbox response and ignores stale lifecycle-scoped inbox rows for a new gate.
- 2026-06-26T18:23+02:00 — No route impact: task 20 is scoped to the Event River
  frontend under `dashboard/src/panels/` plus the generated `package_data/dashboard/` bundle sync.
  The root feature inventory and functional-area model stay unchanged; detailed behavior lives in the
  dashboard panels overview and file sidecars. Verification metadata pinned until closeout stamps the
  code commit.
- 2026-06-26T17:12+02:00 — Regression fix: root gate-control-plane row now
  states that `lifecycle_gate` performs the bounded gate/inbox wait itself
  after creating the gate and blocking the lifecycle.
- 2026-06-26T16:15+02:00 — Task 25 closeout verification: refreshed the root
  gate-control-plane wording to the unified public `lifecycle_gate` junction (including
  `required_decision`) and verified the task-document replacement summary against the
  source branch's `task_doc replace` operation at `2017434`.
- 2026-06-26T15:33+02:00 — No route impact: task 25 preserves the source branch's
  `task_doc replace` operation; lifecycle-gate API consolidation is documented in the scoped
  observer, control-plane, model, and MCP-tool sidecars, so the root task-document inventory remains
  the replacement-repair wording.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-25T13:20+02:00 — Task 23/24: root overview now records gate/inbox interactions as disposable data with response, dismiss, clear, consume, and TTL cleanup paths.
- 2026-06-25T09:55+02:00 — Root provider runtime summary now records GrepAI's non-conflicting preferred auto host ports (`61432`/`61434`) and preserves the distinction from container service ports (`5432`/`11434`).
- 2026-06-25T07:26+02:00 — Task 19 gate interaction polish: root inventory now records
  `gate_response_wait`, single-current gate expiration, targeted dashboard decisions with rejection
  notes, message-only Chat responses, and human-readable dashboard gate previews. Verification metadata
  pinned until closeout stamps the code commit.
- 2026-06-24T18:13+02:00 - No route impact: the empty-state backdrop zoom-stability pass is scoped to
  the existing dashboard panels route and tracked SC2 media assets. The repository-level dashboard
  feature inventory already describes these as shared, effects-gated boomerang-video empty-state
  backdrops; the panels route overview and file sidecars own the current static direct-video and
  media-owned zoom contract.
- 2026-06-24T12:31+02:00 — Task 17 root inventory refresh: the JSON-primary task-documents row and
  functional area now record that leaf task docs and folder-keyed series masters expose structured
  creation metadata for reader ordering, and that the series master projection carries authored master
  content for the dashboard reader.
- 2026-06-24T09:53+02:00 - No route impact: slice 16 is scoped to the dashboard Engine Room/detail
  reader implementation and its file/route sidecars; the repository-level feature inventory and
  invariants remain accurate.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: root inventory refreshed for the workflow change from task-root `contract.md` files to one `ar-series-contract/v1` schema: root series contracts represent integration branches, leaf enclosure contracts represent worktrees, and observer/dashboard projections carry leaf identity separately from task roots. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T23:04+02:00 — Dashboard task 14 adds `lifecycle_finalize_task` as the terminal worktree lifecycle operation. Refreshed the Worktree lifecycle Feature Inventory row and Worktree Support narrative: closeout remains commit-only, finalization proves one local parent-child branch edge after landing/carryover, runs or verifies cleanup, updates the leaf task plus immediate parent row, and deliberately does not model squash-merge equivalence.
- 2026-06-23T22:31+02:00 — Task 12 S2 clarification: the Dashboard frontend Feature Inventory row now
  distinguishes GrepAI process aggregation from target addressability, so repo-scoped provider dots can
  represent `targetRepos` without implying separate provider processes.
- 2026-06-23T22:09+02:00 — Task 12 S2 correction: the Dashboard frontend Feature Inventory row still
  describes provider parenting generically, but the backend source of repo coverage is now explicit:
  CGC watcher rows and GrepAI configured `targetRepos` parent workspace provider satellites to repo
  nodes, while worktree providers remain worktree-group scoped.
- 2026-06-23T21:58+02:00 — Task 12 S2 refreshed the Dashboard frontend Feature Inventory row for the
  topology constellation's provider-parenting correction: repo-covered workspace provider nodes now
  parent to repo nodes, while worktree providers remain worktree-group scoped. Detail lives in the
  `mcp/` observer route and the root `dashboard/src/topology/` route.
- 2026-06-23T15:05+02:00 — Task 10 external-chat inbox: added a root feature note tying the control-plane inbox, the dashboard serving `POST /api/operator-inbox` endpoint, and the `GateResponder` no-hosted-session fallback together as the current pull-based return channel for external agents. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-23T07:39+02:00 — slice 09 closes the **observable-lifecycle gate story** by adopting the
  lifecycle-signal + gate substrate into the lifecycle skills: touched the **Observable Session
  Lifecycle** functional area and the **Gate control plane** Feature Inventory row to record the
  `l-01-session-job-lifecycle` skill's new **Gate Choreography** (every approval junction raises an
  ambient `lifecycle_block` + a durable kind-typed `gate_create`, `gate_wait`s, the **developer**
  resolves — never the agent's model-attributed `gate_decide` — and the agent always clears with
  `lifecycle_resume`), with junctions split by kind across the skills (`plan-approval`/`push-approval`
  in l-01; `worktree-intent`/`integration-approval`/`cleanup-approval` in the `c-09-git-worktree-manager`
  skill; `closeout-approval` = the single commit gate in the `c-12-closeout` skill; `agent-question`
  catch-all). The agent's behavior — not just the dashboard's reads — now makes the session observable.
  The same slice refreshed the empty-state backdrop atmosphere: the shared `EmptyStateBackdrop` video
  became a `motion.video` with a slow 12s scale-yoyo zoom (`1`→`1.03`, no CSS per the animation
  doctrine, shared by both backdrops, effects-gated), and the battle-cruiser clip was re-sourced into the
  same `sc2-battlecruiser-boomerang.mp4` path. Per the root-overview-surfaces-emerging-features lesson
  these are surfaced here as they land; per-file detail lives in the skill mirror sidecars + the
  `dashboard/src/panels/` route overview + sidecars. Verification metadata pinned until closeout stamps
  the code commit.
- 2026-06-23T04:35+02:00 — slice 07b targeted polish extends the engine-room **G6 video-backdrop
  atmosphere** to the cockpit's empty-state canvases: a new shared `EmptyStateBackdrop` panel
  (`dashboard/src/panels/`) renders a faint, effects-gated, forward+reverse **boomerang** clip behind
  centered empty-state text — the operations DetailPanel no-selection state shows the battle cruiser and
  the chats no-session state shows the adjutant. New atmosphere assets land under `dashboard/public/assets/`
  (`sc2-battlecruiser-boomerang.mp4`, `sc2-adjutant-boomerang.mp4`, plus a spare
  `sc2-siegetank-blueprint-video.mp4`); the backdrop honors `useShouldAnimate` (absent under calm-cockpit /
  reduced-motion) and is `aria-hidden`. Per the root-overview-surfaces-emerging-features lesson this growing
  cockpit atmosphere is surfaced here as it lands; per-file detail lives in the `dashboard/src/panels/` route
  overview + sidecars. Verification metadata pinned until closeout stamps the 07b code commit.
- 2026-06-23T00:53+02:00 — No route impact: slice 07 S4+S5 is doctrine/docstring text only — the `read_ar_files`
  tool docstring now states its research-phase-read role (read managed-repo source through it until the
  build/job decision; native read = the edit precondition once building begins), the `read_files.py` +
  `served_store.py` docstrings retarget the compact-reset producer to the post-3.0 agentic-control-plane (no
  session-hook producer; consumer + `refresh` kept as defensive scaffolding), and the synced runtime mirrors
  under `mcp/.../package_data/runtime/` carry that research-phase-read doctrine. No MCP tool surface, schema, or
  subsystem changed, so the repo's feature inventory / functional areas this overview describes are unchanged —
  detail lives in the `mcp/` package overview + the `controllers/` / `observer/` route overviews + file
  sidecars. Verification metadata pinned until closeout stamps the slice-07 code commit.
- 2026-06-22T11:00+02:00 — slice 05o completes the engine-room **failure-mode library**: enriched the
  "Dashboard frontend (mission-control cockpit)" Feature Inventory row to surface the canvas now driving
  **all eight** `podstage.html` failure modes (memory/ledger block, stale base, provider-plan block, seed
  fault, reindex reroute, live sync, integration conflict, abandon) on a shared set of node-anchored failure
  primitives — steady gate, scan ring, ghosted lane, pruned node, refused-conduit flash, moved badge,
  engine-dropout, terminal STOP, and dissolve — each entering/exiting with a Motion fade/pop transition. Per
  the root-overview-surfaces-emerging-features lesson this growing cockpit subsystem is surfaced here as it
  lands, not marked no-route-impact. The change is scoped to `dashboard/src/panels/engine-room/` +
  `dashboard/src/dev/` (their route overviews + sidecars carry the per-file detail); the repo's other
  functional areas are unchanged. Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-22T10:45+02:00 — slice 05o Mode 2 (engine-room failure modes, mode 2 = T1B stale-base block): enriched the
  "Dashboard frontend (mission-control cockpit)" Feature Inventory row to surface the next failure-mode beat —
  the **pruned-base-node** primitive (a stale local base, behind upstream, reads DORMANT/pruned over its
  fact-state box) plus the big red **fleeting-enclosure** box (a born-blocked / pre-contract worktree footprint
  replacing the dashed-amber border, BLOCKED title + reason + recovery chips), and a failure-indicator polish
  pass that anchors the verify/block pointers **ON the repository node** as the topmost layer (the gate +
  reason badge straddle the checked node's top edge, "pointing at" the blocked repo) and gives every alert
  overlay (gate, reason, attention, chips, STOP, the block pointer) a Motion fade/pop enter/exit transition.
  Per the root-overview-surfaces-emerging-features lesson this growing cockpit subsystem is surfaced here as it
  lands, not marked no-impact. The change is internal to `dashboard/src/panels/engine-room/` +
  `dashboard/src/dev/` + the `docs/design/engine-room/` living spec (their overviews + sidecars carry the
  detail); the repo's other functional areas are unchanged. Verification metadata pinned until closeout stamps
  the 05o code commit.
- 2026-06-22T00:29+02:00 — slice 05o (engine-room failure modes, mode 1 = T3B memory/ledger block): enriched the
  "Dashboard frontend (mission-control cockpit)" Feature Inventory row to surface the new **failure-mode**
  choreography — the **scan-ring** + **ghosted-lane** primitives and the `memory-block` player scenario (verify
  → block → reconcile → **provider clone** → nominal, mirroring `podstage.html` T3B), plus the coupled
  engine-gauge polish (flat gold bezel, constant-gold petals). Per the root-overview-surfaces-emerging-features
  lesson this growing cockpit subsystem is surfaced here as it lands, not marked no-impact. The change is
  internal to `dashboard/src/panels/engine-room/` + `dashboard/src/dev/` + the `docs/design/engine-room/` living
  spec (their overviews + sidecars carry the detail); the repo's other functional areas are unchanged.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-21T23:35+02:00 — slice 05k (docs/design onboarding inclusion + engine-room tear-down/refinements): **`docs/design/` is now in onboarding scope.** `system/settings.json` `pathRules` became a two-rule list — a `docs/design`-scoped rule (first; first-match-wins) onboards `.html` + `.md` there, the root rule unchanged (so a stray non-design `.html` like `dashboard/src/dev/reference/mc2.html` still falls through and is *not* onboarded) — and `system/sources.md` registers `docs/design/` as Domain Documentation. The engine-room design language (`engine-room-visual-language.html` living spec + `podstage.html` prototype) + `observable-lifecycle.md`/`harness-matrix.md` are now first-class memory under `onboarding/docs/design/` (2 new file sidecars + the `docs/design/` + `docs/design/engine-room/` route overviews). Updated the Public Documentation functional area + the Build & Dev `sources.md` note accordingly. The accompanying engine-room dashboard work (5k tear-down dispose sequence + power-down diagnostics + active/settled flow language, and the design-review refinements: the second-loop engine-fill fix, the three-column re-spacing, the closeout-train breadcrumb, the memory integration arrow) is internal to `dashboard/src/panels/engine-room/` (its overview + sidecars) and already surfaced in the Dashboard frontend Feature Inventory row. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-21T02:44+02:00 — Slice 6g: the **Dashboard frontend** Feature Inventory row now records **task-document navigation** — the detail panel renders a series master (overview + clickable sub-task index) with in-panel drill-in into each slice (back/parent up-link in the sticky panel header), markdown-rendered task prose (new `grammar/Markdown` primitive), and cross-master "→" navigation between series lifecycles. Per the root-overview-surfaces-emerging-features lesson the dashboard surface is described here as it grows. Verification metadata pinned until closeout stamps the 6g code commit.
- 2026-06-21T02:26+02:00 — slice 05k (dashboard engine-room motion): the engine-room canvas motion completed its 05f §8 property-split — moved off interim CSS onto a new `useEngineTimeline` GSAP hook (draw-ons + the repeating fx) + Motion (`AnimatePresence` enter/exit), CSS static; the "Dashboard frontend (mission-control cockpit)" Feature Inventory row now surfaces this (plus the 5h landing arc + the 5i scenario player), per the root-overview-surfaces-emerging-features lesson. The change is internal to `dashboard/src/panels/engine-room/` + `dashboard/src/index.css` (their overviews + sidecars); the repo's other functional areas are unchanged. A known D5 (`cleanup-pending`) landing-tier retraction follow-up is tracked in the engine-room overview. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T15:59+02:00 — Task 6 slice 6f-1: the **Dashboard frontend** Feature Inventory row now records the **highlight → context-package** composer — a cockpit text selection raises a React Aria popover to send the selection + a message into a chat session's stdin (single/selector/create-on-Enter + ＋ new chat), reusing the live stdin channel; no silent action, not ACP. Per the root-overview-surfaces-emerging-features lesson the chat surface is described here as it grows. Verification metadata pinned until closeout stamps the 6f-1 code commit.
- 2026-06-19T14:05+02:00 — Task 6 slice 6e-4: the **Dashboard frontend** Feature Inventory row now records the terminal/session **hardening** — the open-session registry moved into a `data/sessions` store, and a live terminal survives a cockpit *view* switch (`Cockpit` keeps `<Chats>` mounted, hidden via CSS) and a *session-tab* switch (`Chats` keeps every session's `<Terminal>` mounted) instead of being unmounted ("tabbing away bricked the session"); the backend PTY spawn (`serving/terminal.py`) gained a controlling terminal (`os.login_tty`) so tmux honors resize. Per the root-overview-surfaces-emerging-features lesson the chat surface is described here as it grows. Verification metadata pinned until closeout stamps the 6e-4 code commit.
- 2026-06-19T07:23+02:00 — No route impact: slice 3c R5 adds the `task_doc` `dry_run`/preview op (render + diff + would-lose without writing) — the adoption safety partner to R4; an mcp-internal tool-op addition, so the repo's feature inventory / functional areas this overview describes are unchanged — detail in the `controllers/`/`models/`/`mcp/tools/` overviews + sidecars. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T06:39+02:00 — No route impact: an engine-room dashboard crash fix (the `landing` read guarded for pre-5h/persisted projections) under `dashboard/src/` + the rebuilt `package_data/dashboard/` bundle; the repo's feature inventory / functional areas this overview describes are unchanged — detail in the `dashboard/src/panels/engine-room/` overview + sidecars. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T06:03+02:00 — Slice 3c reopened (R4, leaf-doc fidelity): recorded in the JSON-primary task-documents Functional Area slice tracker — leaf docs gain `statusNote`/`headerNotes` + freeform `sections` so a real hand file round-trips content-complete (the escape hatch; the standard sections stay the backbone), `DocStatus` stays strict, and the w-02 skill documents the extensions. A schema-fidelity refinement within the `tasks/` route; detail in the `tasks/` overview. Verification metadata pinned until closeout stamps the R4 code commit.
- 2026-06-19T05:48+02:00 — Task 6 slice 6e-3: the **Dashboard frontend** Feature Inventory row now records **context injection** — a `SessionComposer` docked below the Chats terminal sends a block of text into the active session's stdin as a bracketed paste (the on-ramp to 6f). Per the root-overview-surfaces-emerging-features lesson the chat surface is described here as it grows. Verification metadata pinned until closeout stamps the 6e-3 code commit.
- 2026-06-19T05:15+02:00 — Slice 3c reopened (R3, deferred-examples honesty): recorded in the JSON-primary task-documents Functional Area slice tracker — an optional `codeExamplesNote` lets a planning slice that defers its examples render as *deferred* rather than "none needed", and the w-02 skill now teaches it. A small format-honesty refinement within the `tasks/` route; detail in the `tasks/` overview. Verification metadata pinned until closeout stamps the R3 code commit.
- 2026-06-19T04:38+02:00 — Task 6 slice 6e-2c: the **Dashboard frontend** Feature Inventory row now records the **session switcher** — the Chats view's open sessions moved into a dedicated left-rail `SessionList` (a React Aria `GridList`: single-select = active session, per-row close ✕), replacing the horizontal tab strip, plus the harness buttons unified onto ＋ Terminal's golden look. Per the root-overview-surfaces-emerging-features lesson the chat surface is described here as it grows, not no-impacted. Verification metadata pinned until closeout stamps the 6e-2c code commit.
- 2026-06-19T04:18+02:00 — Slice 3c reopened (R2, heading-vs-outcome): recorded the task-document renderer fix in the JSON-primary task-documents Functional Area slice tracker — `Step.outcome` is now distinct from the heading `title` (a bare step renders heading-only). A small render-fidelity refinement within the `tasks/` route; detail in the `tasks/` overview. Verification metadata pinned until closeout stamps the R2 code commit.
- 2026-06-19T03:17+02:00 — Slice 3c reopened (R1, masters observable): the observer now projects series **masters** folder-keyed (`read_series_documents` → `Analytics.series`), aggregating the declared `subTasks` checkboxes into whole-series progress so a master is observable on the dashboard (click a master → overall progress, not just per-lifecycle leaves). Refreshed the JSON-primary task-documents Feature Inventory row + Functional Area; per the root-overview-surfaces-emerging-features lesson this growing dashboard subsystem is surfaced here, not marked no-impact. Verification metadata pinned until closeout stamps the R1 code commit.
- 2026-06-18T21:27+02:00 — Task 6 slice 6e-2b: the **Dashboard frontend** Feature Inventory row now records the **per-harness launch buttons** — a detection-driven button per *installed* harness (Claude Code / Codex / Pi.dev) beside ＋ Terminal, via the new `GET /api/harnesses` detection endpoint + the `serving.harnesses` registry (a harness id on the wire, the fixed argv server-side). Per the root-overview-surfaces-emerging-features lesson this lands here as it ships. Verification metadata pinned until closeout stamps the 6e-2b code commit.
- 2026-06-18T17:40+02:00 — Task 6 slice 6e-2a: the **Dashboard frontend** Feature Inventory row now records the **create + own** capability — a "＋ Terminal" control spawns a dashboard-owned shell at the workspace root via the new `POST /api/terminal` opener (`TerminalHost.open`, server-resolved command); the dashboard owns the session it created (the Chats view no longer just attaches). Per-harness launch buttons (Claude Code / Codex / Pi.dev) are 6e-2b. Verified live (POST → real shell → WS). Per the root-overview-surfaces-emerging-features lesson this lands here as it ships. Verification metadata pinned until closeout stamps the 6e-2a code commit.
- 2026-06-18T16:50+02:00 — Task 6 slice 6e-1: surfaced the visible **Mode B2 terminal** on the **Dashboard frontend** Feature Inventory row — a full-bleed **Chats** view (`panels/Chats.tsx` + a code-split `Terminal.tsx` xterm.js wrapper over the `data/terminal.ts` WebSocket client) rendering the 6d PTY stream (keystrokes/resize ↔ PTY bytes), the cockpit's first bidirectional surface; reviewed against a dev mock socket, the real launch is 6e-2. Per the root-overview-surfaces-emerging-features lesson this lands here as it ships. Verification metadata pinned until closeout stamps the 6e-1 code commit.
- 2026-06-18T16:10+02:00 — Task 6 slice 6d-2: the **Dashboard serving layer** Feature Inventory row + Dashboard Serving Layer functional area now record Mode B2's `/api/terminal/{session}` WebSocket bridge (PTY ↔ browser — binary out, JSON `stdin`/`resize` in, `{type:exit}` on child exit; attach-only + tmux-persistent) landing in `serving.app`, plus the new `websockets` core dep. The xterm.js Chats tab (6e) still follows. Per the root-overview-surfaces-emerging-features lesson this subsystem is tracked here as it lands. Verification metadata pinned until closeout stamps the 6d-2 code commit.
- 2026-06-18T15:40+02:00 — Task 6 slice 6d-1: surfaced **Mode B2** (the dashboard-hosted terminal) on the **Dashboard serving layer** Feature Inventory row + Dashboard Serving Layer functional area — 6d-1 lands the `serving.terminal` host (a `TerminalHost` registry of tmux-wrapped stdlib-`pty` sessions launching the harness render-not-scrape; fixed-argv/OS-user/localhost; injectable PTY/tmux spawn). Per the root-overview-surfaces-emerging-features lesson this new subsystem is surfaced here as it lands, not marked no-impact; the WebSocket bridge (6d-2) + xterm.js visual (6e) follow. (Task 6 runs in its own worktree off the slice-5 tip, reconciling at the series integration gate.) Verification metadata pinned until closeout stamps the 6d-1 code commit.
- 2026-06-18T12:10+02:00 — Task 6 slice 6b: the **Gate control plane** became enforcing — `controlplane/enforcement.py` binds `worktree_closeout_apply` to a developer-approved gate (model self-approval rejected; gateless lifecycles unchanged), and the dashboard POST plane records that approval (`gate_decide_for_lifecycle`). Refreshed the Gate control plane + Dashboard serving Feature Inventory rows and the Dashboard Serving Layer area; per the root-overview-surfaces-emerging-features lesson this growing subsystem is surfaced here as it lands. (Task 6 runs in its own worktree off the slice-5 tip, reconciling at the series integration gate.) Verification metadata pinned until closeout stamps the 6b code commit.
- 2026-06-18T01:05+02:00 — Task 6 slice 6a: surfaced the new **Gate control plane** subsystem as a Feature Inventory row — the `agents_remember.controlplane` gate-record substrate (`GateRecord` + `GateStore`) and the four `gate_*` MCP tools. Per the root-overview-surfaces-emerging-features lesson this growing subsystem is surfaced here as it lands, not marked no-impact. (Task 6 runs in its own worktree off the slice-5 work-branch tip, reconciling at the series integration gate.) Verification metadata pinned until closeout stamps the 6a code commit.
- 2026-06-17T22:45+02:00 — Slice 5g (visual-parity / G6): enriched the "Dashboard frontend (mission-control cockpit)" Feature Inventory row to surface the completed bird's-eye fidelity — the 5g G6 atmospheric backdrop + the cockpit Effects/Calm toggle, the restored HUD decal layer (canopy frame, engine spine + petals, the left official-line engines + conduits + coupler, lane annotations), and the fixed-height room layout (the `grammar/Panel` `fill` variant). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-17T16:15+02:00 — Slice 5g (G1–G5): the dashboard **Engine Room** was reworked into the design
  prototype's **bird's-eye podracer canvas** and now renders the whole worktree lifecycle — boot
  choreography, failure overlays (blocked gates · engine fault flicker · reindex reroute), and the
  **live/teardown** states (sync block · a terminal integration-conflict STOP · abandon dissolve) — with
  engines reading **green when active**. Refreshed the Dashboard frontend Feature Inventory row; per the
  root-overview-surfaces-emerging-features lesson this growing cockpit subsystem is surfaced here as it
  lands, not marked no-impact. The successful-landing choreography (needs a `projection.py` addition) is
  split to the `05h` follow-up. Verification metadata pinned until closeout stamps the G5 code commit.
- 2026-06-17T01:49+02:00 — No route impact: adds the engine-room **pod-stage design prototype sandbox** under `dashboard/public/_proto/` (a standalone choreography reference — `podstage.html` + `SCENARIOS.md`/`DESIGN.md` + the blueprint boomerang backdrop), the design source iterated on Open Design for the forthcoming **5g** engine-room dashboard implementation. This is a design-reference *sandbox*, not feature code: `dashboard/public/**` is outside the memory/route scope, no governed source changed, and the repository's top-level surface this overview describes is unchanged. Distinct from the 5a–5f entries (which surfaced shipped serving/panel/projection work) — when the **5g implementation** lands (evolving `panels/engine-room/EnclosureProcessMap` into the prototype's bird's-eye podracer canvas) it WILL be surfaced here as it lands, per the root-overview-surfaces-emerging-features lesson. Verification metadata pinned until closeout stamps the sandbox code commit.
- 2026-06-16T02:30+02:00 — Slice 5f (S0–S1): the dashboard **Engine Room** is becoming an animated worktree-lifecycle state machine — S0 landed the honest-motion gate (`useShouldAnimate`), SVG conduits, and `worktreeGroup` keying (visual parity); S1 gave the room a full-width 3-zone **full-bleed** layout (the rails hide for the Engine Room / Topology machine-map views). Refreshed the Dashboard frontend Feature Inventory row; per the root-overview-surfaces-emerging-features lesson this growing cockpit subsystem is surfaced here, not marked no-impact. Verification metadata pinned until closeout stamps the S1 code commit.
- 2026-06-15T19:35+02:00 — Slice 5e: reworked the dashboard **Engine Room** into an enclosure-centered, state-backed process map (a new `analytics.engineProcesses` server projection + the `panels/engine-room/` module + pre-contract `worktree_start` observability, §5.4); refreshed the Dashboard frontend Feature Inventory row. Verification metadata pinned until closeout stamps the 5e code commit.
- 2026-06-15T17:00+02:00 — Slice 05 (5d): the React/TS **frontend was re-architected** and `dashboard/src/**` brought **into memory scope** — now onboarded with a new `dashboard/src/` route overview (+ `panels/` + `grammar/` route overviews + 19 file sidecars). The ~1,200-line global `tokens.css` monolith was retired into the layered blueprint: **Panda CSS** (typed tokens + build-time/zero-runtime recipes) for styling, **React Aria** (`react-aria-components`) for headless behavior/a11y (the mode bar + pivot `ToggleButtonGroup`s, the lifecycle `ListBox`), CRT effects isolated in `index.css`. Added a **Dashboard frontend** Feature Inventory row and refreshed the Dashboard Serving Layer functional area (the frontend is no longer out-of-memory-scope). Verification metadata pinned until closeout stamps the 5d code commit.
- 2026-06-14T23:30+02:00 — Slice 05 (5c): the cockpit was rebuilt to represent the real Agents Remember model — lifecycle as the unit (paused persistent lifecycles synthesized from worktree contracts), one de-duped BY REPO | BY PHASE lifecycle list, an in-dashboard **task reader** (full task-document content), a **per-worktree engine room**, the lifecycle → worktree → provider spine, and the topology constellation. This drove a **projection correction** under `observer/` (per-worktree provider stacks, full task content on `TaskDocNode`, persistent-lifecycle synthesis) plus a `serving/` sim/events fix. Refreshed the Dashboard Serving Layer functional area. The cockpit UI is the out-of-scope root `dashboard/`, surfaced here per the root-overview-surfaces-emerging-features lesson. Verification metadata pinned until closeout stamps the 5c code commit.
- 2026-06-14T17:28+02:00 — Slice 05 (5b): surfaced the **server-computed attention queue** (`AttentionItem` + the derived `Analytics.attentionQueue`, reducer `build_attention_queue`) on the Observable Session Lifecycle inventory row, and noted the read-only **cockpit panels** (attention queue, live session strip, two-axis operation tree, detail panel + phase stepper / display-only gate banner) on the Dashboard Serving Layer area. The React/TS panels live in the out-of-memory-scope `dashboard/`, so the durable summary lives here per the root-overview-surfaces-emerging-features lesson. Verification metadata pinned until closeout stamps the 5b code commit.
- 2026-06-14T15:52+02:00 — Slice 05a: the **real** Vite/React mission-control cockpit now ships under the root `dashboard/` sub-project (the slice-04 placeholder is replaced; built bundle synced into `package_data/dashboard/` by `scripts/sync-dashboard.py`, gated by `sync-dashboard --check` in both githooks + a new frontend CI job). Refreshed the **Dashboard Serving Layer** functional area + the canonical-asset-sync Feature Inventory row. Per the root-overview-surfaces-emerging-features lesson the cockpit is surfaced here as it lands; its React/TS sources live in the out-of-memory-scope `dashboard/`, so the durable summary lives on this overview. Verification metadata pinned until closeout stamps the 5a code commit.
- 2026-06-14T11:30+02:00 — Slice 04 commit 4b: refreshed the **dashboard serving layer** Feature Inventory row + functional area — the serving layer now carries the raw `event` SSE channel (byte-offset resume), sim-mode replay, and the no-mutation POST action skeleton (slice 06 enforces). Per the root-overview-surfaces-emerging-features lesson this growing subsystem is refreshed here as it lands, not marked "No route impact." Verification metadata pinned until closeout stamps the 4b code commit.
- 2026-06-14T11:30+02:00 — Slice 04 commit 4a: surfaced the **dashboard serving layer** (`agents_remember.serving` + the umbrella `agents-remember dashboard` CLI) as a Feature Inventory row and a "Dashboard Serving Layer" functional area, naming the root-level `dashboard/` frontend sub-project. Per the root-overview-surfaces-emerging-features lesson, the serving layer is surfaced here as it lands (4a), not deferred to the cockpit. Verification metadata pinned until closeout stamps the 4a code commit.
- 2026-06-14T00:16+02:00 — Slice 3c commit 3: surfaced master JSON support (`kind:"master"` — a `subTasks` series index + ordered `sections`) in the "JSON-Primary Task Documents" functional area; the format now covers every task-doc kind. Verification metadata pinned until closeout stamps the 3c commit-3 code commit.
- 2026-06-13T23:10+02:00 — Slice 3c commit 2: the JSON-primary task-document feature is complete — the `w-02-light-task-workflow` skill adopted authoring via the `task_doc` tool (synced to package data + harness packages) and the observer reader (`read_task_documents`, keyed by lifecycle) landed; updated the "JSON-Primary Task Documents" functional-area note. Verification metadata pinned until closeout stamps the 3c commit-2 code commit.
- 2026-06-13T22:34+02:00 — Addition: surfaced **JSON-primary task documents** (the `agents_remember.tasks` package + `task_doc` tool, slice 3c) on this entry-point overview as a Feature Inventory row and a "JSON-Primary Task Documents" functional area, pointing down to the new `tasks/` route overview. Per the root-overview-surfaces-emerging-features lesson, this growing dashboard-series subsystem is surfaced at the root as it lands (commit 1: engine + tool), not deferred until the cockpit ships. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
- 2026-06-13T20:48+02:00 — Correction + addition: surfaced the **observable session lifecycle (`observer`)** on this entry-point overview as a Feature Inventory row and an "Observable Session Lifecycle" functional area, pointing down to the `observer/` route overview and `docs/design/observable-lifecycle.md` for detail. This **corrects** the earlier dashboard-series entries (2a–3a below), which marked their changes "No route impact" on this root because the work was mcp-internal: the observable-lifecycle subsystem has in fact been a growing top-level feature since 2a (event substrate → ambient lifecycle → save gate → projection read side → 3b analytical surfaces) and should have been surfaced here as it grew, not deferred "until the cockpit ships." Per append-only history the earlier entries are preserved; this entry is the correction of record. Verification metadata pinned until closeout stamps the 3b code commit.
- 2026-06-13T19:30+02:00 — No route impact: slice 3a of the 3.0 browser-dashboard series adds the observable-lifecycle **projection read side** (the mcp-internal `observer` reducer/schema/structural snapshot readers/atomic projection store, plus the shared `observer_root`/`timeutil`); per the 2a/2b/2c framing the subsystem detail lives in the `mcp`/`observer` route overviews, and the repository's top-level surface this overview describes is unchanged until the cockpit ships.
- 2026-06-13T18:45+02:00 — No route impact: slice 2c of the 3.0 browser-dashboard series adds the observable-lifecycle resume + save gate (mcp-internal `observer.save_gate`, ambient `promote`/`attach`, the contract `lifecycle_id` anchor) and the per-harness matrix doc; per the 2a/2b framing the subsystem detail lives in the `mcp`/`observer`/`mcp/tools` route overviews, and the repository's top-level surface this overview describes is unchanged until the cockpit ships.
- 2026-06-13T16:41+02:00 — No route impact: slice 2b of the 3.0 browser-dashboard series adds the mcp-package-internal ambient lifecycle and the six `lifecycle_*` MCP signal tools (plus the `_tool_payload` emission hook) under the `agents_remember.observer` domain. Per the slice-2a framing, the observable-lifecycle subsystem's detail lives in the `mcp`, `observer`, and `mcp/tools` route overviews; the repository's top-level surface this overview describes is unchanged until the cockpit ships.
- 2026-06-13T11:15+02:00 — No route impact: slice 2a of the 3.0 browser-dashboard series adds the mcp-package-internal `agents_remember.observer` event-substrate write side (envelope, ULID, store) under a new `mcp/src/agents_remember/observer/` route, and amends `docs/design/observable-lifecycle.md` (TTL project-and-prune). The repository's top-level surface this overview describes is unchanged; the new subsystem's detail lives in the `mcp` and `observer` route overviews.
- 2026-06-13T10:48+02:00 — Added `docs/design/` as the home for developer-facing design specs of in-flight major work (first entry: `docs/design/observable-lifecycle.md`, the approved 3.0 observable-lifecycle design — lifecycle entity, `ar-observer-event/v1` substrate, enforced gates, the browser-dashboard cockpit). Recorded it in the Public Documentation area as distinct from the user-facing `docs/` pages and the historical `roadmap/` specs; `docs/**` stays onboarding-excluded, so this overview is where the routing convention lives. No source-code structure change.
- 2026-06-12T19:06+02:00 — No route impact: root-level changes for issue #83 are the README status version string (2.9.1) and the synced c-12-closeout and l-01-session-job-lifecycle skill doctrine copies (canonical `skills/` plus harness directories; issue #83 doctrine and the two-turn gate protocol); the repository structure and routing this overview describes are unchanged.
- 2026-06-12T12:25+02:00 — No route impact: README Status section rewritten from the per-release narrative chain into a two-paragraph current-state + direction statement at `2.9.0` (release history routed to GitHub Releases; direction = observable/steerable sessions toward the browser cockpit, #2/#43); the README remains the short public front door this overview describes, and the repo surface is unchanged.
- 2026-06-11T15:20+02:00 — No route impact: the carryover artifact-coverage change is contained in mcp/ (carryover kinds, drift git_ops ref parameter, c-11 skill doc, version bump); repo-root route structure is unchanged.
- 2026-06-11T14:07+02:00: No route impact: re-verified against merged main `c2c2dcb` after the upstream doc-link/typo merges (PRs #69-#73) and the repository rename from `agents-remember-md` to `agents-remember`; card content already matched the source.
- 2026-06-11T06:47+02:00 — Issue #62 removed the direct-closeout path: closeout is worktree-only. Updated the approval-gated closeout inventory row (dropped `direct_closeout_*` identifiers), the Worktree Support narrative (command surface and the closing sentence now state the worktree-only rule), the c-09 boundary bullet, and removed the `direct closeout` glossary term.
- 2026-06-10T10:26+02:00 — No route impact: README Status section bumped to 2.8.0 with the GitHub #54 release sentence, and the canonical root skills (l-01/c-09/c-11) gained the freshness-checkpoint doctrine in lockstep with their packaged copies; the repo surface this overview describes is unchanged.
- 2026-06-10T09:56+02:00 — No route impact: issue #54 sub-task D is mcp-package-internal (worktree_sync tool + status freshness); the mcp and worktrees/modules route overviews carry the content updates, and the repo surface this overview describes is unchanged.
- 2026-06-10T09:45+02:00 — No route impact: issue #54 sub-task C is mcp-package-internal (carryover memory-main advance); the mcp route overview carries the content update, and the repo surface this overview describes is unchanged.
- 2026-06-10T09:30+02:00 — No route impact: issue #54 sub-task B is mcp-package-internal (worktree_start stale-base preflight + memory branch auto-template); the mcp and worktrees/modules route overviews carry the content updates, and the repo surface this overview describes is unchanged.
- 2026-06-10T08:39+02:00 — No route impact: issue #54 sub-task A is mcp-package-internal (freshness kernel + context_packet section); the mcp route overview carries the content update, and the repo surface this overview describes is unchanged.
- 2026-06-10T08:15+02:00 — No route impact: README Status section bumped to 2.7.0 with the GitHub #53/#58 release sentence; the repo surface this overview describes is unchanged.
- 2026-06-10T06:05+02:00 — No route impact: README Status section bumped to 2.6.0 with the GitHub #56 release sentence; the repo surface this overview describes is unchanged.
- 2026-06-10T05:50+02:00 — Issue #56 sub-task 3: the branch memory carryover inventory row now records route-overview candidates (identical→auto re-verify, differing→always review-required) and guarded official-side route-index regeneration.
- 2026-06-10T05:30+02:00 — Root overview body caught up with the 2.5.0–2.5.2 releases: content-gated provider readiness + `indexing` busy list in the feature inventory, a new tool-response-budget inventory row, and stall-watchdog/seed-fallback/stdio-subprocess doctrine in the provider runtime narrative. Previous closeouts had only stamped the verification header (developer-flagged gap).
- 2026-06-10T05:20+02:00 — Issue #56 sub-tasks 1-2: the approval-gated closeout inventory row now records the body/history gates and the `No content impact:` / `No route impact:` reviewed-no-impact markers enforced for sidecars and nearest-governing route overviews.
- 2026-06-09T14:52+02:00: Refreshed the root overview against MCP 2.4.1 `main` after runtime asset canonical sync landed; recorded the hard installed-runtime onboarding trust gate and the canonical root-to-package runtime asset sync path.
- 2026-06-08T09:57+02:00: Re-verified the repository overview against the PR-39 branch head after the branch merged current `main` and the skipped-provider context-packet contract was corrected.

## Build & Dev

- Source-checkout Python implementation work should run Ruff, Pyright, and Radon from the `agents-remember/` root; exact command details belong in the resolved memory layer's `system/tools.md`.
- The MCP package tests under `mcp/tests` cover `c-08-ar-coordination-context-resolver` skill, `c-02-memory-quality-control` skill, `c-09-git-worktree-manager` skill, ledger, contract, provider, benchmark, runtime install, and skills install behavior through package modules.
- `system/sources.md` registers `docs/design/` as the Domain Documentation routing index (added when `docs/design/` was brought into onboarding scope, slice 05k); `system/tools.md` is unchanged.

## Key Invariants

- Onboarding should describe current repository state; task files describe planned or in-progress future work.
- `c-08-ar-coordination-context-resolver` skill owns topology and path resolution facts; it must not perform Git worktree operations.
- `c-02-memory-quality-control` skill owns memory quality control: task-start drift detects file-level, overview, inline, and per-entity fingerprint drift; pre-code-commit checks catch new files without onboarding; closeout checks combine integrity and style. It must not update onboarding itself or write temporary reports into durable memory repos.
- `c-05-create-or-update-onboarding-files` skill creates and maintains onboarding artifacts; it must use actual evidence sources rather than citing source registries as proof.
- Task workflows must stop for developer approval before implementation.
- Worktree-backed task workflows must stop again for applicable closeout authority before `c-09-git-worktree-manager` skill closeout creates commits: explicit developer approval for standalone/final/unclear work, or recorded delegated series authority for subordinate accepted-series work.
- The installed runtime `system/AGENTS.md` start-of-task onboarding gate is hard: after drift detection, agents must not silently drop, ignore, or stop using onboarding; they must report update candidates and dirty-source findings, update approved candidates through `c-05-create-or-update-onboarding-files`, rerun drift, and only then continue.
- `c-09-git-worktree-manager` skill wraps task workflows with worktree lifecycle state; it does not replace `w-02-light-task-workflow` skill, starts external-memory worktrees only from a clean committed memory baseline, does not commit, integrate, or clean up without the relevant applicable authority, uses `c-02-memory-quality-control` skill memory quality control after the code commit, refreshes memory, runs `memory_quality_check` before the memory commit, and runs cleanup only after successful integration.
- `c-10-adopt-memory-baseline` skill is an adoption wrapper for existing external-memory onboarding; it does not refresh onboarding and it does not overwrite an existing ledger.
- `c-03-repo-bootstrap` skill bootstrap memory must keep durable route-local overviews in the mirrored onboarding hierarchy under the resolved onboarding root, use root `bootstrap/` artifacts as temporary promotion/review artifacts, keep low-confidence claims out of durable fact sections, apply candidate excludes before scouting, and hand file-level onboarding semantics to `c-05-create-or-update-onboarding-files` skill.
- `c-05-create-or-update-onboarding-files` skill file-level onboarding remains strict one-to-one with source files and must not collapse file-specific facts into a generic route overview reference; structural route changes route to `c-03-repo-bootstrap` skill rather than becoming disconnected file edits.
- Route indexes are generated availability metadata, not hand-authored truth; overview `## Hot Path Summary` sections and file sidecars are the maintained inputs, and `c-04-retrieval-strategy-router` skill should infer missing sidecars from `sourceScope` plus `coveredFiles`.
- Repo entity catalogs use deterministic `git-blob-set-v1` fingerprints over curated load-bearing evidence files so `c-02-memory-quality-control` skill can flag stale entity memory without semantic guessing.
- The package-owned runtime `AGENTS.md` template set is currently `coordinator`, `skills`, `system`, and `tasks`; memory repos use `system/*` files rather than a root-level `AGENTS.md`.
- Runtime, provider, benchmark, route-index, memory quality, memory, worktree, and skill-install behavior belongs in MCP package modules; the source checkout no longer keeps parallel `installer/`, top-level `scripts/`, `runtime/scripts/`, skill-local `scripts/`, `_shared`, or skill-local `tests` execution routes.
- Ruff owns source hygiene and Radon owns complexity scouting for this repository; high-complexity results should feed refactor planning and coding-guideline updates rather than being buried through broad local suppressions.
- Managed provider mode should wrap provider databases and daemon infrastructure in Docker instead of requiring host-level PostgreSQL, FalkorDB, OS service managers, launch agents, package-manager services, or global user daemons.
- Provider runtime artifacts are not durable memory or source data: GrepAI config/state/cache/home files belong under `providers/runners/grepai/`, GrepAI per-root `.grepai/` working directories are git-ignored runtime artifacts, CGC runtime files belong under `providers/runners/codegraphcontext/<repo-id>/.codegraphcontext/`, durable provider database data belongs under `providers/data/`, and MCP/provider operator logs belong under `logs/`.

## Glossary Terms

| Term                     | Meaning                                                                                                       | Notes                                                                                                                                               |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| onboarding unit          | A deterministic documentation unit for one source file or one repo-level entity catalog.                      | File-level units mirror source paths and carry verification metadata.                                                                               |
| entity fingerprint       | A deterministic hash over the load-bearing files that define a repo entity.                                  | `c-05-create-or-update-onboarding-files` skill curates the evidence paths; `c-02-memory-quality-control` skill recomputes `git-blob-set-v1` and flags drift.                                                                 |
| coordination context     | The resolved root/path/settings facts returned by `c-08-ar-coordination-context-resolver` skill for a code repository.                                 | Current implementation exposes `code_repository_name`, `code_repository_root`, `memory_root`, `coordination_root`, repo-specific `task_root`, and `temp_root`. |
| pathRules                | Include/exclude eligibility rules that decide which source paths and file types are managed.                  | Storage and eligibility are separate concepts.                                                                                                      |
| drift report             | A `c-02-memory-quality-control` skill memory quality artifact that classifies onboarding trust.                                              | It is temporary evidence under `temp/drift-reports`, not durable repo behavior; explicit memory-root report paths are redirected to temp.           |
| memory quality check     | The MCP closeout gate that combines drift integrity and memory style checks.                                  | It runs after onboarding refresh and before the memory content commit; task-start work uses the drift-control subset of `c-02-memory-quality-control` skill.                       |
| worktree contract        | Local runtime state file for worktree-backed tasks.                                                           | The parser/writer lives in `mcp/src/agents_remember/worktrees/worktree_contract.py`; `c-09-git-worktree-manager` skill creates and consumes contracts beside the task wrapper's `task.md`. |
| worktree integration     | The approved `c-09-git-worktree-manager` skill phase that lands closed task work back onto source branches.                                | `ff-only` requires unchanged source ancestry; `replay` supports parallel non-overlapping work and blocks conflicts before main moves.               |
| memory baseline adoption | The one-time action of turning current external-memory onboarding into the first ledgered `memory.md` baseline. | `c-10-adopt-memory-baseline` skill checks drift first, requires explicit drift acceptance when needed, and delegates ledger creation to `c-09-git-worktree-manager` skill.                                     |
| runtime AGENTS template  | A package-owned `AGENTS.md` source under `mcp/src/agents_remember/package_data/runtime/agents-md-files/`.                                             | Current templates are coordinator, skills, system, and tasks; there is no memory-repo `AGENTS.md` template or expected memory-repo root instruction file. |
| MCP runtime settings     | A trusted settings file outside the coordinator root that controls the MCP server.                              | It provides `coordinationRoot`, `workspaceRoot`, allowed repos/providers, timeout caps, and optional contract paths; coordinator files do not grant authority. |

## Docs References

Same-repository files remain the direct evidence for Agents Remember's own runtime and memory behavior. Public install pages now also link official harness documentation for volatile skill-location claims.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Claude Code, Cursor, Antigravity, VS Code Copilot, Pi, Hermes, and OpenClaw install pages link official docs for their current instruction and skill discovery behavior. | n/a | [Claude Code skills](https://code.claude.com/docs/en/skills); [Cursor Agent Skills](https://cursor.com/docs/skills.md); [Antigravity IDE Skills](https://antigravity.google/docs/ide-skills); [VS Code Agent Skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills); [Pi Skills](https://pi.dev/docs/latest/skills); [Hermes Context Files](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files/); [OpenClaw Agent Workspace](https://docs.openclaw.ai/concepts/agent-workspace) |
| No external documentation is needed to prove the repository's own runtime, resolver, drift, onboarding, or workflow structure; same-repository files remain the direct evidence. | n/a | n/a |

## What To Explore Next

| Priority | Area / Path                                                                                                               | Why Next                                                                                                            |
| -------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| high     | [mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager) | External workflow metadata and richer task-intake variables are the next likely worktree lifecycle polish area.     |
| high     | MCP-backed scheduled coordination and agent inbox direction                                                                | Future multi-harness coordination could use Agents Remember as a central inbox where Codex, Claude Code, Hermes, and cheaper/background harnesses pick up scheduled or queued work. Do not implement ad hoc timers for current tasks, but when an implementation would strongly benefit from periodic checks, queued work pickup, weekly evals, or scheduled refactors, record that as evidence for a future scheduler/poller system. |
| medium   | [mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow)                                     | The master + light sub-task escalation in the `w-02-light-task-workflow` skill (which absorbed the retired heavy workflow) may need a separate onboarding pass if worktree-backed task folders become common. |
| medium   | [mcp/src/agents_remember/package_data/runtime/system/defaults](agents-remember/mcp/src/agents_remember/package_data/runtime/system/defaults)                                                     | Add richer settings fixtures if cross-repo v2 behavior needs more than the current example files.                   |

## Needs Verification

- The coordinator `ar-coordination/system/tools.md` currently lists checks for `resolve_auto_editor`, not this repo.
- The current source registry is useful as a discovery index but has no direct external domain evidence for this repo's own skill/workflow mechanics.
- External-memory onboarding for `agents-remember` is ledgered; future closeouts must keep the code-to-memory mapping current.
- The memory quality package is now the home for drift integrity and update-history style checks; further quality checks should be added under `memory_quality/style` or `memory_quality/integrity`.

## Update History

- 2026-07-09T11:45+02:00 — No route impact: 260707-HFX2-L9 (supervisor redelivery cadence + signal
  throttling) touches `docs/reference/settings-json.md` (documents the 900s redelivery floor,
  `signalCooldownSeconds`, and the current supervisor kill-switch mitigation status) and the
  `mcp/`, `controlplane/`, and `serving/` sub-routes. This is a doctrine/reference-doc and sub-route
  behavior change, not a change to the root's own structure or routing; per-file detail lives in the
  already-updated sidecars and sub-route overviews (curator pass, 260707-HFX2-L9). Verification
  metadata pinned until closeout stamps the 260707-HFX2-L9 commit.
- 2026-07-09T11:25+02:00 — No route impact: 260707-HFX2-L8 (stability/bounded-resource/
  guaranteed-reclamation doctrine) adds one cross-reference sentence to root `AGENTS.md`'s Code
  Quality Instructions section (naming the new `system/coding-guidelines.md` Stability/Reclamation
  section as MUST-READ before adding/editing a store, loop-over-a-store, queue, or append-only log)
  and candidate reviewer criteria (CS-6, PR-6) to the canonical `skills/l-01-agent-lifecycles/
  criteria/` catalogs. This is a doctrine/cross-reference content addition, not a change to the
  root's own structure, routing, or module responsibilities described by this overview; per-file
  detail lives in the already-updated `AGENTS.md`/`code-seam.md`/`plan-review.md` sidecars (curator
  pass, 260707-HFX2-L8). Verification metadata pinned until closeout stamps the 260707-HFX2-L8
  commit.

## Last Verified

Updated 2026-06-28T07:43+02:00 — task 29 S7: refreshed the root Event River, actionable-drift, and dashboard frontend inventory for backend-retained raw events, raw-stream hydration, no frontend count cap, targetless actionable-drift dismissal, and the hidden Lifecycle Flow tab. Route detail lives in the `mcp/`, `observer/`, `serving/`, `controlplane/`, `memory_quality/`, `dashboard/src/`, and `dashboard/src/panels/` route overviews. Verification metadata pinned until closeout stamps the task-29 code commit.

Updated 2026-06-27T22:00+02:00 — task 28 (NOTIFY-AND-CONTINUE turn end): refreshed the Observable session lifecycle inventory row + functional-area section for the new public `lifecycle_turn_end_notification` tool, the non-terminal `awaiting-developer` state, the next-step hint repoint off the now-parked `lifecycle_gate`, and the reducer gate-open/blocked-gate dedup. Route detail lives in the `observer/`, `mcp/tools/`, and `models/` route overviews and their file sidecars. Verification metadata pinned until closeout stamps the code commit.

Updated 2026-06-17T22:45+02:00 after the Engine Room visual-parity pass enriched the dashboard-frontend Feature Inventory row (the 5g G6 atmospheric backdrop + Effects/Calm toggle, the restored HUD decal layer, and the fixed-height `Panel fill` layout); verification metadata stays pinned until closeout commits the source. (Prior: 2026-06-06T12:28+02:00 after adding the public `docs/features.md` tour, replacing README `## Core Model` with `## Core Features`, and documenting the Claude Code root `.mcp.json` detection caveat. Prior: 2026-06-04T10:29+02:00 — documented hidden harness starter packages as source-owned surfaces in the main overview and noted their `l-01` deep-research retrieval-strategy tally requirement. Prior: 2026-05-29T17:30+02:00 — re-spined the public docs and this overview's "What This Repo Is" framing around the three retrieval substrates (by path / by meaning / by relationship) and retired the sidecar-only anti-retrieval positioning. Prior: 2026-05-28T19:52+02:00 — added the Pydantic public response-contract model surface, compact `ContextPacketV2` boundary, and dedicated provider diagnostics feature inventory entries.)
