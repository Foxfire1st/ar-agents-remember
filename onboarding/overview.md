# agents-remember — Onboarding Overview

| Field | Value |
|---|---|
| repository | agents-remember |
| doc_type | `repo-overview` |
| sourceRoute | . |
| lastUpdated | 2026-09-07T00:34+02:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|

> **Status:** active baseline

## Memory Preparation And Final Certification

Memory quality is useful before gate admission: a contract-scoped full request observes the exact code/memory pair and candidate trees, runs quality checks, and builds an enclosure-local curator worklist covering repair findings, commit-owned findings, missing onboarding, stale route indexes and source drift. Use that worklist to perform the authorized semantic onboarding updates before entering the expensive certification sequence. It is not necessary to obtain code-gate certificates merely to discover the memory work.

Preparation does not grant a final certificate. The interactive catalog projection explicitly lacks affected-closure and code-prefix authority. The existing prepared-memory adapter consumes the selected four original code terminals and exact prepared candidate, runs the final memory producer, publishes its physical result and selects Gate 5 through the normal owner. Finalization requires that selected original fifth certificate and its bound memory inputs. MCAR continues from these existing owners; this overview does not declare the unfinished master accepted or create a second final proof path.

Candidate capture uses an isolated add-all index and stable observed HEAD, leaving the user's real index unchanged. External-memory identity binds configured repositories, worktree roots, branches, bases, onboarding root, ledger and contract digest. A changed pair or candidate must refuse stale publication. Metadata stamping and ledger alignment cannot substitute for semantic memory repair.

## Development And Certification Policy

Ordinary Python development is supported directly through `mcp/.venv/bin/python -m pytest`; four workers run the isolated unit population. `-m integration` selects the small real-boundary population and `-m ""` selects both. Focused file/node execution, including serial debugging, is valid development work and does not acquire certification authority. The repository declares budgets of 1,000 unit and 150 integration parametrized collected cases. Extend or consolidate distinct behavior protection before adding cases; do not restore deleted matrices, private-branch tests or unused fixture machinery because an old milestone names them.

Coverage, including changed-line coverage, is diagnostic only. No percentage floor requires additional tests. Production-only CRAP retains 20 as a review trigger, not a delivery blocker; tests and verification support are excluded. Lint, formatting, typing, structural rules and test failures still enforce. Diagnostic-tool execution errors remain visible failures distinct from metric findings. There is no coverage baseline, score-exception registry or ratchet.

Only genuine Dagger admission and the existing lifecycle owners can issue immutable candidate-bound certifying evidence. A host pytest pass, copied report, green helper result or use of Dagger alone is insufficient. Reuse the existing shared engine and preserve process identity, disposable state, credential isolation, exact candidate and publication ownership. Full-suite execution and whole-master independent review belong to the master aggregation boundary under the current execution policy; this overview does not impose either on every leaf. Focused development evidence remains useful without pretending to be final acceptance.

## Historical Frontend Quality Milestone

The earlier frontend milestone introduced broader static measurement and a changed-lines coverage floor. The floor is retired by current diagnostic-only policy; static, type, build and behavior failures remain meaningful. Historical population counts are not current requirements.

## What This Repo Is

`agents-remember` is the source repository for the Agents Remember workflow system. It defines the doctrine, skills, MCP tools, task workflows, and design references that agents use to maintain durable onboarding knowledge beside code. Durable memory is reached through three retrieval substrates routed by `c-04-retrieval-strategy-router` skill: **by path** (a source file's deterministic one-to-one onboarding unit, verified against Git history), **by meaning** (semantic memory search over the onboarding), and **by relationship** (a code-relationship graph). By-path notes are the core and need no provider; meaning and relationship are served by opt-in Docker providers (GrepAI, CodeGraphContext) and return candidate routing evidence, not proof. Overviews and entity catalogs use route scopes or curated evidence fingerprints before an agent relies on them. The earlier sidecar-only, anti-retrieval positioning (no embeddings / no vector store) predated those providers and has been retired from the public spine and from this overview's framing.

The current checked-in guidance distinguishes `ar-memory/` as durable internal memory from `ar-coordination/` as local coordination. `c-08-ar-coordination-context-resolver` skill exposes that split through `code_repository_name`, `code_repository_root`, `memory_root`, and `coordination_root`; `c-09-git-worktree-manager` skill owns worktree lifecycle mutation, ordinary series integration back to source branches, and the narrowly policy-gated branch-addressed landing of an explicitly selected leaf implemented without an enclosure. It also documents `task_reopen` — reopening a fully landed leaf task in place under its exact leaf id — while `c-10-adopt-memory-baseline` skill provides the adoption path for existing external-memory onboarding that needs an initial `memory.md` ledger.

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
| File and entity onboarding maintenance | File-level sidecars, inline onboarding adapter rules, repo entity catalogs, deterministic entity fingerprints, reference health checks, and generated route indexes driven by one Git/path-rule census. | `c-05-create-or-update-onboarding-files` skill, `route_index_refresh`, `kernel/route_index.py`, `kernel/route_index_census.py` |
| Findings capture | Confirmed current-state findings are routed to durable task-local artifacts and can be propagated into onboarding after verification and approval. | `c-01-findings-capture` skill |
| Workflow modes | The `l-01-agent-lifecycles` architect lifecycle's build decision at `decide`: a research-only exit for no-code answers, otherwise a `w-02-light-task-workflow` skill task — chat is never a build route, so one-session edits take the minimal artifact — escalating to a master + light sub-task series for larger phased work (the retired heavy workflow and the retired chat build are no longer modes). | `l-01-agent-lifecycles` skill, `w-02-light-task-workflow` skill |
| Agent lifecycles (one per role) | Developer-requested multi-agent series run through the unified `l-01-agent-lifecycles` skill. Spawn-role env and fresh briefs select role seats; otherwise free chat remains a launcher. Ordinary role-shaped work compiles the canonical architect brief and calls `dispatch_agent` once on the sprint document; an explicit developer-declared task-seat takeover instead targets the named role at its canonical altitude. The identity-free call uses target-document/role-altitude authority; after handoff, hosted seats use plane identity and direct-child scope, with no plane-to-ambient fallback. Architect owns the initial plan loop and recommends the developer-approved strategist when the evidence-backed topology/classification reasoning is missing or stale — graph absence alone is not a trigger. A reviewed graph-less atomic-sequential choice is valid: one source-pair-selected atomic master is active for implementation while other live masters are paused and preserved, and a selection remains `reconciling` until its exact code/memory sources are current. A sanctioned strategist skip transfers the complete dependency, route, seam, classification, priority, and topology-reasoning duty to the orchestrator, which adopts a graph only when present. One effective priority governs a candidate (candidate override, otherwise master default), while the orchestrator retains portfolio comparison. Graph adoption from a graph-less sprint first attaches every master, then publishes one complete nodes-plus-evidence-edges batch. Exact proposed completion candidates are reviewed before refs move; handover cites canonical candidate/code ancestry/memory ancestry/per-leaf ledger refs rather than copying maps, and failed review routes to a leaf rather than an integration workbench. | `l-01-agent-lifecycles` skill, `skills/l-01-agent-lifecycles/templates/architect-brief.md`, `skills/l-01-agent-lifecycles/roles/architect.md`, `skills/l-01-agent-lifecycles/roles/orchestrator.md`, `skills/l-01-agent-lifecycles/roles/reviewer.md`, `system/git-workflow.md` |
| Approval-gated closeout | Applicable authority gates for implementation, worktree-backed closeout, memory refresh, memory quality, and ledger alignment: standalone/final work uses explicit developer approval, while subordinate accepted-series work can proceed under recorded delegated series authority. Closeout itself is worktree-only — the retired direct current-checkout closeout path remains removed (issue #62). The separate `direct_landing` operation is only the explicitly selected delivery route for a leaf implemented without its own enclosure; ordinary master/series closeout and integration never require `directExecutionEnabled`. Since 260731-EFA-L4, where the quality gate runs it first resets the index and stages the whole task worktree, so the gate is shown the commit's content rather than only the paths already tracked; two refusals guard that step (not a task worktree, or unresolved merge conflicts). Body/history gates reject header-only or unmarked history-only onboarding refreshes for changed sources and their nearest-governing route overviews; explicit `No content impact:` / `No route impact:` Update History markers attest reviewed-no-impact and are surfaced in closeout payloads. | `c-09-git-worktree-manager` skill, `c-12-closeout` skill, `worktree_closeout_*`, `direct_landing` |
| Worktree lifecycle | Worktree start, attach, status, closeout preview/apply, integration, lifecycle finalization, cleanup, task contracts, replay/fast-forward integration, and external-memory compatibility checks. Atomic implementation admission uses one disposable selector per exact code/external-memory source pair: switching preserves and pauses the previous live master, publishes the selected master as `reconciling`, and exposes it as active only after sync. Sync evidence survives in the enclosure-root journal and pinned Git refs; real conflicts are retained for staged `continue`, while explicit `cancel` restores operation-owned pre-sync heads. | `c-09-git-worktree-manager` skill, `lifecycle_finalize_task`, `worktree_*`, `worktrees/` |
| Observable session lifecycle | The observer event log and projection retain trust provenance, lifecycle status, metrics, attention and task context. Public tool completion passes through application-owned enrichment and the single model finalizer; `nextStep` is bounded and optional, rather than attached unconditionally to every response. Lifecycle gate decisions and turn-end notification have distinct contracts. | `agents_remember.observer`, `application/tool_response.py`, `models/tool_response.py`, `mcp/tools/base.py` |
| JSON-primary task documents | The `ar-task-document/v1` document is the source of truth for a task's plan + progress and `task.md` is its deterministic render. Sprint documents carry the canonical `executionGraph`; master documents carry explicit `executionNature` (`organizational` or `atomic`). A sprint without an `executionGraph` uses the atomic-sequential default, whose runtime admission is source-pair selection rather than a task-authoring lock or permanent series lane. Task mutations publish their authored state; field classification invalidates closeout evidence for semantic/readiness changes, while observation-only updates do not invalidate task intent. `task_doc.author_execution_graph` bootstraps or edits the graph, and there is no implicit inference or compatibility reader. The `task_doc` MCP tool validates cross-document graph references, authors/replaces documents, and republishes the affected JSON/Markdown set atomically; observer projection exposes the same topology. | `agents_remember.tasks`, `task_doc` tool, `tasks/` route overview |
| Gate control plane | The durable, attributed record of decision points on a lifecycle (closeout/integration/cleanup approvals, agent questions, alarm acks): an append-only `ar-gate-record/v1` `GateRecord` + `GateStore` co-located with the observer event log. The public agent-facing MCP junction is `lifecycle_gate`: it creates the typed durable gate, blocks the active lifecycle with the developer-facing ask, waits for a developer decision or gate-specific inbox response, and can carry `required_decision`; lower-level gate payloads/stores remain the implementation substrate. `controlplane/enforcement.py` binds `worktree_closeout_apply` to a developer-approved `closeout-approval` gate, or to an opt-in delegated orchestration approval that passes the `gate_policy.py` rules; model self-approval and owner lifecycle self-approval remain non-binding. The default policy is all-human, human-pinned integration/push/cleanup gates are not configurable away, and delegated decisions can require reviewer-verdict evidence refs that surface on gate records/projections. Task 19 adds the single-current-gate invariant (new lifecycle gates expire older open lifecycle gates) plus targeted dashboard decisions via `gate_decide_for_lifecycle`. Lifecycle skills now raise `lifecycle_gate(kind=...)`, handle the returned developer decision or operator-inbox message from that public junction, and clear with `lifecycle_resume`, split across plan/worktree/closeout/push/integration/cleanup/agent-question gate kinds. Dashboard gate projection is live and now renders human-readable previews with raw JSON as diagnostics. | `agents_remember.controlplane`, `lifecycle_gate`, `gate_*` stores/tools, `controlplane/` route overview |
| Dashboard serving layer | `agents-remember dashboard` serves projection snapshots/deltas, raw retained events, typed operator actions, the packaged frontend, and hosted harness sessions. The serving package composes protocol, catalog, submission, conversation and bridge authorities as well as HTTP/WebSocket transport. Controlled chats use a structured conversation surface with a read-only diagnostic line log. Optional settings discovery, supervised daemon start/status/stop, and version-aware daemon reconciliation remain CLI/runtime concerns. | `agents_remember.serving`, `agents-remember dashboard`, `serving/overview.md`, `dashboard/src/overview.md` |
| Dashboard frontend | The root React dashboard exposes Operations and the canonical Chats cockpit, plus task, requirement, artifact, lifecycle, event and provider views. Controlled sessions submit through the typed submission authority and render structured conversation history; inspector tabs retain evidence and capabilities without inventing missing telemetry. Grammar components and route-local overviews own the detailed current layout and behavior. Earlier slice-by-slice frontend descriptions are retained below as historical development context. | `dashboard/src/overview.md`, `dashboard/src/panels/overview.md`, `dashboard/src/data/overview.md`, `dashboard/src/grammar/overview.md` |
| Sessions live set controls (260715-FEUI-L4) | The Sessions cockpit now re-fetches the exact live-session capability snapshot, derives effort only from the selected model row's session-settable options, and keeps requested, pending, echo-evidenced effective, and readback-confirmed values separate across all five SetResult acceptances. Model+effort changes serialize model → evidence/readback → effort; unknown/queued outcomes promote by readback; shared worded chips, per-seat ledger/rail attention, collapsed background toasts, cycle-effort commands, and polite/assertive live regions carry the evidence. | `dashboard/src/data/{sessionCapabilities,setAcceptance,pairChange,setClient,setChips,setControlsCopy,announcer}.ts`, `dashboard/src/panels/session-cockpit/` overview |
| Hosted chat task attachment | The operator HTTP `attach-task` route changes a hosted session’s canonical `taskDocumentRef` and role binding subject to catalog, role and altitude validation. Agent-facing creation and messaging use structural task/role addresses; the old public `attach_terminal_session_to_leaf` tool is retired. | `serving/_app_terminal_routes.py`, `serving/response_contract.py`, `serving/terminal_catalog.py` |
| Agent-facing session dispatch | One MCP tool — `dispatch_agent` — is the sole public spawn surface for plane-hosted seats and identity-free ambient launchers; `spawn_agent_session` is retained only as an internal primitive and wire identity. Caller kind is derived from process context, never a request field: plane identity selects seat/direct-child authority and cannot fall back to ambient, while absent identity selects canonical target-document and role-altitude validation. Ordinary ambient work targets the sprint architect; only an explicit developer-declared task-seat takeover targets another named role at its canonical altitude. Both modes submit the same target document, role, complete brief, and optional label, then share settings resolution, creation/reconciliation, readiness, exact brief pinning, rollback, and canonical seat publication in one transaction. Settings resolve one complete typed harness/model/effort selection; role-table `dispatch` and `tools` rows describe structural authority/capability rather than override keys. The own adapter discovers its token-free per-install/account catalog, validates effort under the selected model, and applies native Claude/Codex/Pi initial configuration before the real vendor session starts. The same exact-session bridge serializes `set_model` and `set_effort` with prompt submission and returns a normalized `SetResult` whose acceptance is one of `echo-verified`, `immediate`, `queued`, `unknown`, or `unsupported`. Spawn model/effort env stays provenance, explicit free-form launch/session controls remain separate, caller spend overrides refuse before side effects, and neither initial nor mid-session selection is composer-pasted. Each spawned session is its own harness process, and dashboard and agent-facing launches still share one opener. | `dispatch_agent`; `spawn_agent_session` (internal primitive), `skills/l-01-agent-lifecycles/templates/architect-brief.md`, `serving.harness_launch`, `serving.harness_control_runner`, `serving.harness_control_bridge`, `serving.harness_submission_authority`, `serving.terminal_opener`, `operator_inbox_*`, `mcp/tools/terminal.py`, `models/terminal.py` |
| Daemon harness capability and control API | The serving daemon exposes the own-adapter contract without ACP transport: dynamic token-free pre-session catalogs use an install-aware bounded cache with explicit auth refresh; terminal open accepts an optional complete native model/effort pair; exact live sessions advertise and return honest model/effort `SetResult` evidence; whole-message submit and same-id reconciliation use the native control socket with no paste fallback. Live reopen reports immutable process truth or conflicts, failed refresh quarantines stale data, duplicate request ids are idempotent, public responses omit adapter-private raw payloads, and liveness is established before 404/409 support classification. | `serving.harness_capability_catalog`, `serving.harness_control_api`, `serving.harness_control_client`, `serving.terminal_opener`, `serving.app` |
| Reliable controlled-session submission (260715-FEUI-L5) | One `HarnessSubmissionAuthority` per bridge generation owns prompt/model/effort ordering, immutable request/source/payload idempotency, atomic queued-withdraw versus dispatch, exact full-operation-ref completion, early-terminal dominance, raw-free status, and bounded privacy-aware retention. The dashboard's shared CodeMirror composer keeps one epoch/id/text through retry/reconcile, treats only the exact pre-dispatch certificate as retry-safe, and implements authoritative Alt+Up pop-back with revision-CAS recovery. Claude, Codex, and Pi dispatch now under guarded write seams; no adapter/native queue or PTY-paste fallback is authority. | `serving.harness_submission_authority`, `serving.harness_control_{api,bridge,client,models}`, `serving.harness_submission_authority`, `dashboard/src/data/{submitMachine,submitClient,submissionLifecycleClient,submitRetention}.ts`, `dashboard/src/panels/SessionComposer.tsx` |
| Sessions inspector and status integration (260715-FEUI-L7) | The Sessions cockpit completes its end-to-end operator audit with stable-mounted accessible Evidence / Capabilities / Bus tabs and a persistent StatusLine. Evidence retains explicit-mark-seen set outcomes and terminate/retire residuals after source-row removal; exact-session capability truth stays separate from pre-session launch catalogs; the fleet-global pending Bus preserves entry-keyed reply state across filters, virtualization, and hidden tabs, and reverse replies address only the projected sender without consuming the source. The status footer keeps its contractual fact order and literal empty UA-5 context/cost slot rather than inventing telemetry. | `dashboard/src/panels/session-cockpit/{SeatInspector,EvidencePane,CapabilitiesPane,BusPane,BusDeveloperReply,VirtualizedInspectorList,StatusLine}.tsx`, `dashboard/src/panels/session-cockpit/` overview |
| Canonical Chats cockpit and hardening (260715-FEUI-L8) | One product-facing `Chats` destination now uses the keep-alive session cockpit; the old Chats component, session-list grouping, and separate Sessions navigation are retired. Operations remains the default and RailChat remains contextual. The inspector defaults closed, is toggleable and responsive without losing deliberate intent; authoritative launch, attach, highlight routing, landed cleanup, ended/restored states, accessibility, scenario coverage, and performance/fetch tripwires are pinned end to end. At FEUI-L8 controlled sessions still exposed the runner line-log in xterm because UA-1 structured transcript/history authority was not yet implemented; **260718-CHATS-L4 supersedes that** — controlled sessions now default to the structured conversation surface and the line-log is demoted to a read-only diagnostics drawer (see the 260718-CHATS-L4 narrative below). | `dashboard/src/panels/session-cockpit/` overview, `dashboard/src/data/` overview, `docs/design/dashboard/{scenario-catalog,session-cockpit-upstream-register,session-cockpit-closeout-evidence}.md` |
| Agent orchestration communications | Durable messages address canonical task/role seats and survive vacancies until a matching generation can receive them. Hosted delivery uses the controlled harness bridge; physical delivery or a transport acknowledgement alone is not task completion. Consume attribution and terminal message state remain durable. Runtime session identifiers are private correlation data. | `mcp/registration/orchestration.py`, `serving/inbox_delivery.py`, `controlplane/` |
| Event River lifecycle task labels | Event River readable history rows translate lifecycle-bound activity into task-facing context. When a retained event still has a lifecycle id but its live lifecycle projection is gone, the formatter uses projected task documents to show the task title before falling back to raw enclosure or lifecycle ids. The panel waits for raw-stream hydration before showing an empty feed and renders all retained rows it receives; backend lifecycle retention owns the cutoff. | `dashboard/src/panels/eventSummary.ts`, `dashboard/src/data/taskIdentity.ts`, `dashboard/src/panels/EventRiver.test.tsx` |
| Authoritative browser session open | Every dashboard raw or harness create entrance crosses one `POST /api/terminal` client, validates exact request/response identity, and materializes only the accepted server row. Network, HTTP, protocol, identity, or server-declared failure creates no registry row, focus change, readiness/submit transition, or dependent context delivery. | `dashboard/src/data/terminalOpen.ts`, `dashboard/src/data/sessions.ts`, dashboard data/panels/session-cockpit overviews |
| Runtime and skill installation | MCP-owned install of coordinator `AGENTS.md` templates, packaged skills, system defaults, provider defaults, optional benchmark fixtures, and harness skill layouts. | `runtime_install`, `skills_install`, `install/`, `package_data/runtime/` |
| Harness starter packages | Harness-native first-run packages for Claude Code, Codex, Cursor, Antigravity, VS Code + Copilot, Hermes, Pi.dev, and OpenClaw. Each package carries MCP settings templates, skill folders, and either startup hooks or always-on instruction files that load the coordinator first-action directive. | `.claude/`, `.codex/`, `.cursor/`, `.agents/`, `.github-vscode/`, `.vscode/`, `.hermes/`, `.pi/`, `.openclaw/`, `docs/install/` |
| MCP server and authority settings | Installable stdio MCP server with trusted settings outside the coordinator root, allowed repo/provider scopes, timeout caps, transcript roots, and path containment. Since 260731-EFA-L3 it also **starts with no network egress**: the `o200k_base` tokenizer vocabulary ships inside the package under `package_data/tiktoken/` instead of being downloaded while the tool surface imports, so a fresh container, an offline machine, and a hermetic CI job can all start the server. | `agents-remember-mcp`, `mcp/config.py`, `mcp/server.py`, `models/tokens.py`, `package_data/tiktoken/` |
| Public MCP response contracts | Pydantic models for every public MCP tool response, registry coverage for the tool surface, compact strict contracts where the repo owns shape, flexible envelopes where provider/service-native details are intentionally passed through, and token metadata fields for later cost accounting. | `mcp/src/agents_remember/models/`, `PUBLIC_TOOL_RESPONSE_MODELS`, `test_models.py` |
| Provider lifecycle and discovery tools | Docker-managed GrepAI memory search/trace, CodeGraphContext symbol/caller/callee/dependency/complexity/visualization queries, compact provider status, dedicated provider diagnostics, watcher lifecycle, and current-state snapshots. Readiness is content-gated (2.5.0/2.5.1): graph/workspace content probes drive `indexed`/`indexing`/`empty`/`backend-unreachable` states for both providers, empty/unreachable targets degrade the global packet `ok`, crash-looping containers are not ready, and healthy-but-busy targets surface in the compact summary's `indexing` list. Provider launch is contained since 260707-HFX-L1: launch-capable operations (watcher start/restart/index rebuild, one-shot query runners, worktree provider setup, benchmark provider synthesis, the install rebind) re-read the on-disk MCP authority fail-closed — the boot snapshot is not launch authority, so `providers: {}` on disk is a live fleet-wide kill-switch — while stop/status/cleanup stay ungated; provider setup is serialized fleet-wide (one non-dry-run prepare at a time); and the dashboard daemon samples per-container containment metrics (label-discovered, read-only, dockerless-safe) that ride `provider_status`. | `provider_status`, `provider_diagnostics`, `provider_watchers`, `grepai_*`, `cgc_*`, `providers/`, `providers/metrics.py` |
| Tool response token budgets | Verbose tools (`runtime_install`, `provider_diagnostics`, `provider_watchers`, carryover plan/apply) keep compact outcomes inline and file bulk diagnostics under `temp/tool-reports/<tool>/` with an inline `reportPath` (keep-last-5 / 7-day write-time prune, secret redaction); budget tests are the regression line (2.5.1/2.5.2). | `mcp/tool_reports.py`, `compact_*_payload` builders, `test_tool_response_budgets.py` |
| Memory baseline adoption | One-time adoption of existing external-memory onboarding into the first ledgered baseline after drift/status review. | `c-10-adopt-memory-baseline` skill, `memory_baseline_*`, `memory/baseline.py` |
| Branch memory carryover | Carry richer onboarding from a source branch into official memory only after the corresponding code has landed. Candidates cover file sidecars and route overviews (route-keyed, `kind`-tagged): overviews whose route covers a landed path auto-carry only when branch and official content are identical (metadata re-verification), otherwise they are always review-required; official-side `overview.index.json` files are regenerated after carry — never copied — guarded on a clean official-ref checkout. | `c-11-memory-carryover-from-branch` skill, `memory_carryover_*`, `memory/carryover.py` |
| Branch-gated cross-repo context | Optional cross-repo context inclusion guarded by configured branch and memory-ledger checks. | `c-08-ar-coordination-context-resolver` skill, `crossRepo.allow` |
| Benchmark harness | Package-owned Codex benchmark fixtures, workspace preparation, paired source-only versus memory-enabled runs, JSONL/result capture, and metric summaries. | `codex_benchmark_prepare`, `codex_benchmark_run`, `benchmarks/` |
| Source quality tooling | Ordinary isolated pytest supports development; the existing pinned Dagger/lifecycle publication is the sole certifying authority. Coverage is diagnostic and production CRAP20 prompts review without blocking. Current master execution uses focused development checks and final aggregation/review; historical per-leaf acceptance procedures are not imposed here. Exact candidate, runtime and immutable publication bindings remain required. | `docs/design/python-pytest-bootstrap.md`, `docs/design/python-test-evidence.md`, `mcp/certification-profile-v1.json` |
| Self-hosted harness configuration | The nine dogfooded harness configuration trees (`.claude/`, `.codex/`, `.cursor/`, `.github-vscode/` + `.vscode/`, `.hermes/`, `.openclaw/`, `.pi/`, `.agents/`) are **generated from one source and checked**, not eight independent copies. `scripts/harness/` holds the fragment libraries and shared bodies; `scripts/sync-harness.py` fans out 45 files three ways (verbatim, composed body + per-harness framing, and programs assembled from named fragments with derived imports). `--check` verifies generated projection drift. `scripts/harness/README.md` is the ruled classification of genuine per-harness requirements versus drift. | `scripts/sync-harness.py`, `scripts/harness/` |
| Public docs and harness guides | User-facing setup, concepts, architecture, workflows, references, guides, and install notes for Codex, Claude Code, Cursor, Antigravity, VS Code Copilot, Hermes, Pi, and OpenClaw. | `docs/`, `README.md` |
| Canonical runtime and skills asset sync | Root runtime asset folders (`agents-md-files/`, `benchmarks/`, `providers/`, `system/`) are canonical editable assets synced into MCP package data by `scripts/sync-runtime.py`; root `skills/` is the canonical skill tree synced into package data plus every harness starter skill folder by `scripts/sync-skills.py`. Both carry `--check` and both local hook tiers run those deterministic checks. The pull-request-only GitHub workflow invokes `_gate.sh targeted`, so generated-copy drift is checked without running tests or Dagger. The production projection owners remain separate from the reduced retained test population. | `scripts/sync-runtime.py`, `scripts/sync-skills.py`, `.githooks/_gate.sh`, `.github/workflows/quality-checks.yml` |
| Dashboard bundle release build | The built cockpit (`dashboard/dist/`) is placed into `package_data/dashboard/` by `scripts/sync-dashboard.py`. This is a **release build step, not a sync check**: the bundle is a generated artifact that is **not in version control** (master decision OQ6, 2026-07-31), so there is no `--check` mode and no hook runs it. The release job builds the frontend, runs the placement, packages, and asserts the wheel and sdist both carry the bundle plus its `dashboard.fingerprint` sidecar. Placement refuses an absent `dist` and refuses a `dist` that does not carry the current build-input fingerprint Vite compiled into it, so it cannot stamp over a stale artifact. | `scripts/sync-dashboard.py`, `.github/workflows/publish-mcp-to-pypi.yml`, `dashboard/vite.config.ts` |

Task 10 external-chat inbox current state spans three route families: the control-plane inbox
(`OperatorInboxEntry` / `OperatorInboxStore` plus the `operator_inbox_*` MCP tools), the dashboard
serving endpoint (`POST /api/operator-inbox`, trusted developer/dashboard attribution), and the
dashboard Gate Respond fallback (`GateResponder` calls `data/operatorInbox.postOperatorInbox` when no
hosted chat session is attached). Hosted chat injection remains preferred; the inbox is the pull-based
return channel for external agents that cannot receive direct dashboard injection.

Task 23/24 changes the lifecycle of those gate/inbox interactions: prompts, responses, pending pickup
signals, and attention-queue gate rows are disposable interaction data. Explicit dismiss/clear paths
delete immediately; inbox consume records a terminal audit snapshot, and passive TTL cleanup removes
it at the 24-hour interaction window. The only durable lifecycle records are
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

HFX2-L12 updates the root runtime-scaling story for mission-control operation: supervisor signal and
expectation stores compact on read while escalation/cooldown budgets bound repeated work; raw Event
River data is startup-compacted and served through bounded/offloaded paths; projection hot paths cache
lifecycle, task-document, gate, and Git-status reads while guarding task-document body payload size;
terminal catalog/liveness reads batch and compact active sessions; and provider metric/degradation logs
compact instead of growing without reclamation. Remaining follow-up scope is explicit: live Event River
compaction, full task-document body windowing/on-demand retrieval, and heartbeat coalescing are routed to
the next HFX2 leaf rather than claimed complete here. Detail lives in the `mcp/`, `controlplane/`,
`observer/`, `serving/`, and provider route overviews plus their file sidecars.

The current Chats registry is structurally keyed by canonical task document plus role: sprint roles
occupy the sprint document, managers the master, and worker/reviewer/curator their leaf documents.
The left rail projects that real task hierarchy and resolves the current hosted occupant; replacement
does not change the row address. Qualified leaf keys remain only for leaf display/context helpers,
not seat identity. This supersedes the earlier leaf-keyed registry described in semantic history.
The operations-dashboard **polish** surface also includes resizable
persisted rails, drill-state that survives a view switch, the File/Diff viewer rendering opened route
overviews as markdown and the corrected Change-Set selected-row highlight, the Hangar filtering archived
enclosures, and faint siege-tank/battlecruiser empty-state backdrops). L5 also lands a **lifecycle
event-retention correctness fix** at the observer boundary: the durable enclosure — not the prunable
lifecycle event log — is the source of truth for liveness, so a running worktree no longer vanishes from
the Engine Room when its log ages out, and a not-yet-retired master series protects every leaf's event
history from the inactivity TTL until the series is archived plus a one-week grace. **L6** keeps the chat
assignment timing explicit: when an operator starts an agent chat on the displayed leaf or attaches a free
chat through task assignment, the right-rail chat may still inject projected leaf task/worktree context
once for the successful bind. That context package is not addressing authority. Detail lives in the
`observer/`, `serving/`, and `dashboard/src/` route overviews.

## Hot Path Summary

Use [MCP package](mcp/overview.md) for composed services, [memory quality](mcp/src/agents_remember/memory_quality/overview.md) for preparation/final checks and [worktrees](mcp/src/agents_remember/worktrees/overview.md) for contract-owned lifecycle and protected refs. The retained [test route](mcp/tests/overview.md) describes present assertions and distinguishes helper-only files from suites. Exact source/pair identity, durable owner journals and original physical publications govern acceptance; a historical test name does not.

## Architecture At A Glance

```text
agents-remember/
  AGENTS.md
    source checkout instructions and installed-runtime handoff
  README.md
    public setup and conceptual model
  layers.toml
    enforced top-level package dependency order and package charters
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
| Package dependency contract | [layers.toml](agents-remember/layers.toml) | Declares one fail-closed top-level package order and one charter per package. The repository-neutral `certification` contract is rank 3 between wire models and the stateful control plane; later integer ranks shift without changing their package charters or runtime behavior. |
| MCP package          | [mcp](agents-remember/mcp)                                                                                                                                                       | Package-managed MCP server exposing context, runtime install, skills install, provider, worktree, memory, benchmark, settings-derived lifecycle, and memory quality tools. |
| Core skills (C-*)    | [mcp/src/agents_remember/package_data/runtime/skills](agents-remember/mcp/src/agents_remember/package_data/runtime/skills)                                                                                                           | Resolver, memory quality control, repo bootstrap, onboarding maintenance, and related support skills — flat directly under `skills/`. |
| Lifecycle + task workflow | [mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles) and [mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow) | The unified agent lifecycles (router + minimal frame + per-role lifecycles), and the durable light task workflow (which escalates to a master + light sub-task series for larger work). |
| Runtime AGENTS templates | [mcp/src/agents_remember/package_data/runtime/agents-md-files](agents-remember/mcp/src/agents_remember/package_data/runtime/agents-md-files)                                                                                                        | Package-owned coordinator, skills, system, and tasks `AGENTS.md` templates for runtime installation.           |
| System defaults      | [mcp/src/agents_remember/package_data/runtime/system/defaults/examples](agents-remember/mcp/src/agents_remember/package_data/runtime/system/defaults/examples)                                                                                          | Example settings, sources, and tools files used as scaffolding material.                                       |

## Functional Areas

### Source Checkout Contract

`AGENTS.md` is the authoritative behavioral contract for agents operating on this source checkout. It now starts by separating the package source repository from the installed `ar-coordination` runtime: when the file is reached through a workspace-level pointer during sibling-repository work, agents should use the installed runtime `AGENTS.md` instead. For work on this repository itself, it keeps `agents-remember` as the resolver target, routes sessions by role through the `l-01-agent-lifecycles` skill (a spawned role follows its brief; a developer session starts in free chat, answers research inline, or durably pins a complete architect brief and dispatches the architect on the sprint; explicit seat takeovers use the named role and canonical task document), requires `c-08-ar-coordination-context-resolver` skill resolution plus `c-02-memory-quality-control` skill memory quality control before relying on onboarding, separates implementation approval from commit approval, and points active settings reads at the resolved memory layer rather than a root-level source checkout `system/` directory.

### Package Layer Contract

`layers.toml` is the fail-closed authority for allowed top-level package knowledge, not a snapshot
of whichever imports happen to exist today. Order position is rank: a package may import only a
lower-ranked package, and undeclared packages or upward edges fail the layering rail without a
baseline or exception. The generic certification domain is explicitly rank 3 in the sequence
`errors < kernel < models < certification < controlplane`. That keeps its immutable registry,
planning, bounded-admission, and typed-result contracts below their future stateful consumers while
leaving concrete repository profiles, executors, lifecycle terminalization, and memory gates with
their higher-layer owners. `controlplane` consequently remains the lowest stateful interaction
service rather than the lowest domain contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| The order declares `certification` between `models` and `controlplane`, and those package tables carry matching ranks 3 and 4. | "order = ["; "[package.certification]"; "[package.controlplane]" | layers.toml:19-59; layers.toml:105-126 |
| The production checker loads that one contract, rejects undeclared package directories, and reports invalid dependency direction. | `load_contract`; `undeclared_dirs`; `build_report` | mcp/test_support/agents_remember_test_support/code_quality/layering.py:63-68; mcp/test_support/agents_remember_test_support/code_quality/layering.py:122-141; mcp/test_support/agents_remember_test_support/code_quality/layering.py:280-340 |

### Public Documentation

The public README is now intentionally short: product positioning, a fast Core Features pitch, a core path-derived memory example, one generic quickstart, a ToC-linked **Run The Dashboard** section (260703 L3 — unpinned `uv tool install agents-remember-mcp` as the first-class install, flag-free discovery-backed `agents-remember dashboard`, daemon mode + the `dashboard.autoStart` key, pinning as the debugging path, one rc-period pre-release note; the PyPI `mcp/README.md` Install And Run carries the same story), harness install links, docs links, and a compact source/runtime layout. Detailed user-facing material moved under `docs/`: `docs/features.md` is the concentrated product tour, `docs/README.md` is the documentation index, `getting-started.md`, `concepts.md`, `architecture.md`, `workflows.md`, and `FAQ.md` own core narrative, `docs/install/` owns harness-specific setup, `docs/guides/` owns operational tasks, and `docs/reference/` owns exact runtime/settings/skill behavior. Its Status section states the current version (bumped every release) and that the 3.0 cockpit arc has shipped — the dashboard is served from the MCP package via the `agents-remember dashboard` CLI. A separate `docs/design/` subtree holds developer-facing design specs for in-flight major work — distinct from the user-facing pages above and from the historical `roadmap/` notes. Its entries include `docs/design/observable-lifecycle.md` (the approved 3.0 design for an observable, controllable session lifecycle — the browser-dashboard direction, issues #2/#43), `docs/design/harness-matrix.md`, and the **engine-room** design language: `docs/design/engine-room/engine-room-visual-language.html` (the canonical living spec for the engine-room visual primitives — state colours, motion, glow, timing) and `docs/design/engine-room/podstage.html` (the prototype the production canvas was built from). Historically slice 05k admitted design documents into onboarding. The current recovery memory’s `system/settings.json` excludes `docs/**`; retained design/reference overviews preserve prior knowledge and do not imply present one-to-one file-card eligibility. README onboarding and governing overviews carry the applicable implementation account.

### Harness Starter Packages

The hidden root packages `.claude/`, `.codex/`, `.cursor/`, `.agents/`, `.github-vscode/`, `.vscode/`, `.hermes/`, `.pi/`, and `.openclaw/` are source-owned starter packages even though current path rules exclude their one-to-one file sidecars. Their first-action surfaces defer to spawn-role env or a fresh role brief; otherwise they open the developer-facing free-chat launcher. Research-only questions stay inline, while role-shaped work spawns a clean architect with the settings-owned profile. Backend orchestrators remain spawned seats and relay developer decisions through the architect. Canonical skill content is synchronized into these mirrors; the package-data runtime copy is the eligible onboarding evidence.

### Runtime AGENTS Templates

`mcp/src/agents_remember/package_data/runtime/agents-md-files/` is the package-owned source for installed coordinator instructions. The current package has four installable templates: `coordinator/AGENTS.md` for the coordinator root, `skills/AGENTS.md` for compact C-* skill routing, `system/AGENTS.md` for the hard onboarding maintenance gate, and `tasks/AGENTS.md` for task-folder collaboration doctrine. `runtime_install` MCP tool installs those templates to `ar-coordination/AGENTS.md`, `ar-coordination/skills/AGENTS.md`, `ar-coordination/system/AGENTS.md`, and `ar-coordination/tasks/AGENTS.md`. Memory repos are not expected to provide a root-level `AGENTS.md`; repo-specific memory guidance lives in the memory layer's `system/*` files.

### Core Resolver And Memory Quality Control

`c-08-ar-coordination-context-resolver` skill resolves the active coordination context: topology, code repository, `coordination_root`, `memory_root`, onboarding/docs/system roots, settings paths, repo-specific task root, temporary artifact root, contract path, worktree group, ledger path, storage settings, path rules, and branch-gated cross-repo allowances. Without a task name, `task_root` is the repository namespace under `ar-coordination/tasks/<repo>/`; with a task name or contract, it is the concrete task folder. Path-rule defaults in `system/settings.json` now carry the standard generated/vendor/build/cache/IDE/env/Zone.Identifier excludes. For worktree-backed task names, `c-08-ar-coordination-context-resolver` skill resolves current wrapper folders first and persisted `*-ar` task folders second. `c-02-memory-quality-control` skill consumes that context and owns memory quality control: task-start drift verifies file-level onboarding metadata, overview `sourceRoute` metadata, inline digests, and repo entity `git-blob-set-v1` fingerprints against the current source state; pre-code-commit checks catch newly added files without onboarding; closeout checks combine drift integrity with memory style. Drift reports are temporary coordination artifacts under `temp_root`; even explicit report paths inside the durable memory repo should be redirected back to coordination temp.

### Onboarding Maintenance

`c-05-create-or-update-onboarding-files` skill owns file-level onboarding and repo-level entity catalogs. It is the maintenance path for creating or updating onboarding artifacts; `c-02-memory-quality-control` skill detects memory quality issues but does not rewrite onboarding content. File-level onboarding now records the nearest governing `overview.md` when route-local overview coverage exists, while remaining self-sufficient for the concrete source file. Entity catalogs carry one deterministic fingerprint row per entity over a small curated evidence file set; `c-05-create-or-update-onboarding-files` skill chooses and refreshes those paths after review. After closeout memory edits, `memory_quality_check` combines drift integrity with style checks such as newest-first update history ordering before the memory content commit. `c-05-create-or-update-onboarding-files` skill also detects route-level create, refresh, move, and deletion cleanup cases and routes those structural changes to `c-03-repo-bootstrap` skill `existing-memory-slice-maintenance`. Generated `overview.index.json` files live beside route overviews and expose route scope, covered sidecars, child routes, copied hot-path summaries, and mechanically derived source-anchor hints so `c-04-retrieval-strategy-router` skill can route cheaply before opening full overview prose.

### MCP And Context Provider Runtime

The runtime has optional local discovery providers, but they remain accelerators rather than proof. The MCP settings file, not coordinator `system/settings.json`, declares allowed providers and repositories for the MCP path. That file is also the LIVE provider launch authority (260707-HFX-L1): launch-capable operations re-read it from disk fail-closed instead of trusting a server's boot snapshot, so disabling providers on disk bites running servers immediately; stopping, status, and cleanup stay legal, non-dry-run provider setup runs one-at-a-time host-wide behind a HOST-scoped setup lock in the system temp dir (outside every prunable coordination root and benchmark workspace — the guarded resource is the host), and the dashboard daemon samples labeled provider containers into a central containment metrics store under `logs/observer/providers/` that `provider_status` attaches even while providers are disabled. `context_packet` reports provider and watcher state, `runtime_install` installs runtime assets and provider dependencies from package-local code, and `skills_install` copy-installs packaged skills into harness skill roots. Managed provider installs should be coordination-owned without host executable fallbacks: pinned requirements under `providers/requirements/`, provider instances under `providers/runners/`, durable databases under `providers/data/`, operator logs under `logs/providers/`, MCP transcripts under `logs/mcp/`, and patches under `providers/patches/`. `providers/_bin/` and `providers/_venvs/` are stale-artifact cleanup targets, not runtime authority. Database, native-binary, and daemon infrastructure should be Docker-wrapped rather than installed as host services.

GrepAI runs in workspace mode with explicit `{ projectId, path }` roots generated from MCP repository/memory settings. Current managed mode indexes live memory roots in place and git-ignores GrepAI's per-root `.grepai/` working directory instead of mirroring roots under a separate index-root tree. Its runtime config, state, cache, and home artifacts belong under `providers/runners/grepai/`; its shared PostgreSQL/pgvector Docker data belongs under `providers/data/grepai/postgres/`; and `.grepai/` content should not be treated as durable memory. Managed GrepAI prefers non-conflicting auto host ports (`61432` for Postgres, `61434` for Ollama) while keeping the Docker container service ports (`5432` and `11434`) inside the provider network. Worktree isolation clones the source GrepAI database into a worktree-scoped PostgreSQL backend and rewrites provider settings so containers, logs, and runtime paths are isolated while the logical workspace key remains reusable. CodeGraphContext keeps one provider instance per configured repo under `providers/runners/codegraphcontext/<repo-id>/.codegraphcontext/`, with all instances sharing the FalkorDB Docker data root under `providers/data/codegraphcontext/falkordb/`; worktree setup seeds CGC by exporting, path-rewriting, and importing an existing graph bundle. Seed/clone operations are guarded by stall watchdogs (kill on zero progress), never total-duration caps — the copy-instead-of-reindex mechanic is what makes rapid worktree provider deployment viable and it scales with index size by design; the CGC seed accepts relatable HEAD divergence and hands additions/modifications to post-watcher catch-up; deletions and rename sources remain explicit residual staleness, while unrelatable heads refuse seeding. On stdio transport, package subprocesses must never inherit the server's protocol pipes (`stdin=DEVNULL` or piped input, AST-guarded; the 2.5.1 fix for the multi-minute tool hangs).

### Code Quality And Refactor Baseline

Current development commands, diagnostic metrics and certification authority are described in Development And Certification Policy above. Static product/verification ownership remains explicit; uncovered lines do not create a test obligation and CRAP findings do not block delivery.

### Task Workflows

`w-02-light-task-workflow` skill is the compact durable-task workflow used by the current worktree-support task stack. It creates a task wrapper folder and `task.md` once task class and naming are clear, stops for implementation approval, then treats the checklist, onboarding propagation, checks, and worktree-backed commit approval handoff as one implementation cycle. When refreshed external-memory onboarding is part of intake, the memory content and ledger are committed before `c-09-git-worktree-manager` skill starts worktrees.

Requirement delivery history is append-only without turning every implementation/test rerun into a
formal attempt. Semantic revisions advance only through explicit developer approval; workers mint
delivery attempts only when handing an exact candidate to independent review or after reviewer
rejection. Internal runs stay in a separate protocol-event log. Per-requirement journal records are
lightweight and link a content-addressed frozen expanded-evidence artifact; rebuildable master
summaries exclude protocol events and never gate task authoring, lifecycle, closeout, integration,
or queue work.

### Bootstrap Memory Build

`c-03-repo-bootstrap` skill now treats the root repo overview as the minimum successful bootstrap and scales through route-local overview construction pillars, evidence packs, file cards, onboarding waves, curator reviews, and handoff artifacts. Its templates live beside the skill under `mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/` and define the shape of input ledgers, state files, coverage plans, governing route maps, overview cards, route-local overviews, docs packs, boundary packs, file cards, wave manifests, curator reviews, and final handoffs. Route-local overviews are durable memory in the mirrored onboarding hierarchy directly under the resolved onboarding root, not detached area appendices, and file-level onboarding links back to the nearest governing overview. Existing-memory slice maintenance handles added, moved, deleted, refreshed, and newly important routes without pretending the repo is blank; automated bootstrap starts after source inventory intake and stops at handoff before separate closeout approval.

### Worktree Support

The worktree and cross-repo roadmap specs are still useful design references, but core implementation now exists for the first support slice: memory ledger parsing/writing, worktree contract parsing/writing, `c-08-ar-coordination-context-resolver` skill contract-aware facts, the `c-09-git-worktree-manager` skill `start`, `attach`, `status`, `closeout`, `integrate`, `lifecycle_finalize_task`, and `cleanup` command surface, and the `c-10-adopt-memory-baseline` skill `status`/`adopt` adoption workflow for pre-existing external-memory onboarding. `c-00-initialize-memory-repo` skill initializes missing memory roots before `c-09-git-worktree-manager` skill worktree use. `c-09-git-worktree-manager` skill external-memory start blocks dirty source memory repos so a refreshed onboarding pass cannot be accidentally stranded outside the ledgered baseline. `c-09-git-worktree-manager` skill closeout dry-run is the non-mutating preview path before explicit commit approval. Real external-memory closeout runs the explicit repository-profile Dagger lane before the accepted code commit, then applies the separately owned memory/ledger lifecycle boundaries — since 260731-EFA-L4 over the *staged* task worktree, which is the one index mutation that precedes the gate; missing profile authority, CRAP at or above threshold, or a failing required rail fails closed. Only after that gate passes does closeout commit code, use `c-02-memory-quality-control` skill memory quality control to produce the maintenance worklist, refresh affected onboarding verification metadata and entity fingerprints, run `memory_quality_check`, then commit memory content and ledger when clean. `lifecycle_finalize_task` is the terminal lifecycle operation after the branch edge has landed: it proves the landed commit is reachable from the local parent/source branch, verifies memory carryover, runs or verifies cleanup, and reconciles the JSON-primary leaf task plus immediate parent row to `Completed`; it does not attempt squash equivalence or recursively complete ancestors. Closeout is worktree-only: the former direct-closeout current-checkout path was removed (issue #62), so every closeout runs against a task contract.

### Historical Observable Session Lifecycle Build-up

This section preserves tasks 27–29 as historical development context. Current tool-response enrichment, structural seats, and lifecycle decision ownership are described in the feature inventory and the application/lifecycle, MCP/tools, and serving overviews. Statements below about every response receiving a hint or parked public gates are not current API guarantees.

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
the **lifecycle next-step hint engine** ([next_step.py](agents-remember/mcp/src/agents_remember/application/next_step.py)):
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
lists to creation order without interpreting filename or task-slug prefixes.

The execution-topology extension separates that organizational task tree from Git scheduling
facts. Each commanded master declares `organizational` or `atomic`, while the sprint document owns
the canonical reasoned AON graph. Membership, cycles, and derived waves are mechanical and
projected to the dashboard; priority and rescheduling judgment remain orchestrator concerns.

This relates to — but does not build — the parked neutral-repo task/contract sharing substrate
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
`GET /api/state` returns the projection once. The reducer owns projected state interpretation; serving also composes the controlled-session and operator-action authorities. Coordination paths are resolved through `McpRuntimeConfig` +
`observer.paths` (North-Star #5), never raw host paths. Local-first: bound to `127.0.0.1`,
no auth in v1. The **frontend** is a root-level sub-project (`dashboard/`) whose built bundle
ships as `package_data/dashboard/`, placed there by `scripts/sync-dashboard.py`. Since
260731-EFA-L1 that placement happens **in the release job**, not at commit time: the bundle is
git-ignored, no hook and no CI job checks it, and the frontend rail in CI proves only that
`npm run build` still succeeds. A checkout with no build serves 503 with the build command from
`serving/static.py` rather than a placeholder — the slice-04 hand-authored placeholder is gone and
must not return. Slice 4b added
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
effects isolated in `index.css`. A dev `/dev/bench` gallery plus `/dev/reference` mc2 mount drive
the screenshot-annotate review loop. The former `build_rich_sim.py` 35-lifecycle generator was
later retired because no maintained product or acceptance consumer used it; do not restore a
self-validating generator/test pair as evidence.
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
never a zombie row), post-spawn identity rename (`POST /api/terminal/{session}/rename`, label only,
never role), and a live turn-state badge (working/turn-ended/awaiting-input/stale) classified from
pane text on the existing liveness-sweep cadence. **260707-HFX2-L11** reverses the leaf-integrate
and master-finalize completion edges' automated behavior: a successful worker/reviewer/manager seat
is no longer auto-retired there — it is **landed** (`status:"landed"`, kept alive, non-terminated,
inspectable in a dashboard "landed archive" group with a group-cleanup control), since successful
completion is not chat cleanup (ruled design constraint 10); explicit `session_retire` or that
cleanup control are what actually reclaim chat volume. Detail
lives in the `serving/` + `observer/` + `dashboard/src/` route overviews.

## Cross-Repo References

This repository is selected into an external coordination workspace by configured path rules, but onboarding content should cite same-repo files for repository behavior and task files only as planning references.

| Finding | Anchor | Source |
| --- | --- | --- |
| The source checkout distinguishes installed runtime work from sibling-repo work and keeps implementation approval separate from commit approval. | "ar-coordination/AGENTS.md"; "Implementation approval is not commit approval" | AGENTS.md:10-10; AGENTS.md:145-145 |
| Repository instructions define certifying delivery, enforcing checks, and diagnostic-only coverage and production CRAP. | `## Code Quality Instructions` | AGENTS.md:150-206 |
| The docs index owns the start-here, install, operational, and reference map. | "Start Here"; "Install Guides"; "Getting Started"; "Onboard an Existing Repo"; "MCP Tool Reference"; "Release Checklist" | docs/README.md:23-23; docs/README.md:25-25; docs/README.md:33-33; docs/README.md:46-46; docs/README.md:56-56; docs/README.md:65-65 |
| Runtime asset sync treats root runtime folders as canonical and exposes a check form. | `sync_targets` | scripts/sync-runtime.py:189-202 |
| GitHub runs the deterministic non-test gate on pull requests only; tag publishing proves main reachability instead of regating. | "pull_request:"; "Refuse a tag whose commit has not landed on main" | .github/workflows/quality-checks.yml:3-7; .github/workflows/publish-mcp-to-pypi.yml:28-34 |
| Closeout imports the staged-quality boundary, which refuses unsafe linked/conflicted worktrees, binds the accepted candidate tree, stages exactly what will commit, and invokes targeted Dagger quality. | "gate_staged_code as _gate_staged_code" | mcp/src/agents_remember/worktrees/modules/closeout.py:105-105 |
| The staged-quality owner enforces its exact-candidate delivery boundary. | `gate_staged_code` | mcp/src/agents_remember/worktrees/queue/closeout_staged_quality.py:139-165 |
| Contributor guidance separates host feedback from Dagger-owned certifying evidence and defines the retained protection policy. | `## Quality gates` | CONTRIBUTING.md:63-110 |
| Provider guidance keeps provider runtime paths under configured provider roots. | "providers/runners/grepai" | mcp/src/agents_remember/package_data/runtime/system/defaults/examples/coordinator/settings.md:95-95 |
| The MCP settings example declares repository and coordination authority. | `coordinationRoot` | examples/mcp/settings.example.json:3-3 |
| The memory-repo tools example provides the `Code Quality` section. | "Code Quality" | mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/tools.md:11-11 |

HFX2-L21 advances the existing Dashboard frontend feature: the Chats session rail is now a
persisted, pointer- and keyboard-adjustable 220–560 px sidebar instead of a fixed 16 rem column. The
resize separator preserves terminal working width and adds no new route or serving behavior.

260712-TRH-L1 restores the existing Dashboard task reader's functional contract without enlarging
the recurring projection: the selected document hydrates its complete body on demand before notes or
change-set counters mount, shows honest loading/fallback state, and caches by path plus body revision.
The implementation stays within the established `dashboard/src/data` and `dashboard/src/panels`
routes and ships through the existing generated-dashboard package boundary.

## Historical 260712-TRH-L4 Route Impact (later structural dispatch supersedes session-id addressing)

Repository onboarding now records spawned-unbriefed → harness-ready → briefed hosted dispatch, exact session-id continuity, delivered-plus-harness-log-confirmed assignment, canonical l-01 ownership with generated mirrors, and fully serialized catalog writers with lock-free atomic readers.


### 260713-PHA-L5 Route Contract Review

The route remains governed by the shared hosted protocol bridge: exact adapter snapshots provide
readiness and liveness, correlated receipts sit beneath durable inbox rows, interactions use durable
gates, legacy/custom sessions are explicit unsupported states, and pane/log signals are diagnostic
only. Dashboard and packaged projections remain additive and synchronized.

## Historical milestone context: 260718-CHATS-L5I Current Repo Impact

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

The interactive Chats round strengthens the repository's runtime-truth contract across the cockpit and serving daemon. Persistent chat and terminal surfaces preserve local state across view changes; active conversation streams recover from server-minted cursors instead of retrying unusable coordinates; structured questions and native interrupts are exact-session operations with explicit evidence; and dashboard state serving avoids repeated whole-tree walks and repeated projection serialization. These changes retain the existing rule that optimistic browser activity, transport acknowledgement, and terminal settlement are different facts.

The historical Chats commit-gate delta first made the wrapper mandatory at closeout, pre-push,
and CI. L23 supersedes that cadence: targeted Dagger acceptance runs once at leaf closeout, full
Dagger acceptance runs once at master integration, pre-push is deterministic non-test feedback,
and GitHub validation is pull-request-only and non-test. The enforcement topology in the Hot Path
Summary is authoritative. Canonical hooks, workflows, setup/public docs, root skill mirrors, and
generated dashboard assets are pathRules-disabled onboarding subjects; their current contract is
represented here and in eligible README, MCP package authorities, route cards, and memory-system
guidance rather than by duplicate sidecars.

## Historical 260731-EFA-L1 Repository Impact — The Gate Now Runs

This leaf's subject was enforcement itself, and it changes facts a future agent will otherwise get
wrong. The durable contracts:

1. **The cockpit bundle is built at release and is NOT in version control.**
   `package_data/dashboard/` and `package_data/dashboard.fingerprint` are git-ignored, as are
   `mcp/build/` and `mcp/dist/`. `scripts/sync-dashboard.py` lost its `--check` mode along with the
   subject it compared against; it now refuses an absent `dist` and refuses a `dist` that does not
   carry the build-input fingerprint `vite.config.ts` compiled into it as `__AR_DASHBOARD_BUILD__`.
   The fingerprint sidecar is therefore a value read *out of* the bundle, never stamped over it.
2. **The pre-commit hook gates staged content on a fast tier; pre-push repeats deterministic
   non-test checks.** `.githooks/pre-commit` and `.githooks/pre-push` are thin wrappers over
   `.githooks/_gate.sh <fast|targeted>`. The fast tier isolates the index with
   `git stash --keep-index --include-untracked`
   under restore traps, and skips isolation when the tree already matches the index or a sequencer
   operation is in progress.
3. **GitHub validation is pull-request-only and deterministic.** It runs generated-copy,
   formatting, lint, and type checks; ordinary pushes launch no duplicate and GitHub invokes
   neither host tests nor Dagger acceptance.
4. **The publish workflow verifies landed provenance instead of regating.** A tag must point to a
   commit reachable from `origin/main`; the workflow then builds the dashboard and package and
   asserts the wheel and sdist each contain the bundle and fingerprint sidecar.
5. **The closeout quality gate is no longer hard-coded to one repository name.** Applicability is
   decided by whether the target checkout carries `mcp/test_support/agents_remember_test_support/code_quality/check.py`;
   a checkout without it is reported as `wrapper-unavailable` rather than silently skipped.

What follows for anyone reading older material: `--no-verify` was routine here precisely because
the pre-commit hook could not pass, and any statement that pre-commit runs the full wrapper, that
CI is scoped to `main`, or that the shipped bundle is committed describes the world before this
leaf.

## Historical 260731-EFA-L4 Repository Impact — Closeout Stages Before It Gates

This leaf's subject was wire contracts and typed vocabularies, and most of it is route-local. Three
things changed about the **repository's** shape and rules, and a future agent will get them wrong
otherwise.

**1. Closeout resets the index and stages the whole task worktree before the quality gate runs, and
does not put it back.** Every rail of the gate reads the index — `derive_scope` lists what ruff and
pyright are handed with `git ls-files`, and `diff_coverage` diffs the base against the tracked tree
— while closeout commits with `git add -A`. Everything in that gap, meaning every path a task
*created* rather than edited, went into the commit with no rail of the gate having read a line of
it, and the gate reported green. **Leaf 3's `abc7cbcc` — the commit this leaf is cut from — shipped
four files that way.** `worktrees/modules/closeout.py::_gate_staged_code` now runs
`git reset --mixed HEAD` then `git add -A` and hands the gate exactly what the commit will contain.
The mixed reset is not tidiness: `git add -A` applies ignore rules only to paths git does not
already track or hold staged, so a file staged by a refused attempt stays staged after the leaf adds
it to `.gitignore` and the retry commits it anyway. Resetting first makes every run recompute the
index from the working tree under the ignore rules in force at that moment, which is what makes a
retry equivalent to a first run rather than merely asserted to be.

The end state after a refusal is **staged, not rolled back**, and that is deliberate. The checkout
is the task's own disposable worktree — created by `worktree_start`, destroyed by
`lifecycle_finalize_task` — so nobody is holding a partial staging in it, and `commit_if_dirty` was
going to `add -A` over it moments later regardless. An earlier attempt saved the index file aside
and copied it back; that machinery is **gone rather than fixed**, because it could not survive
`core.splitIndex` or a `SIGTERM` (which is how an MCP server actually dies), and every guarantee it
offered was about a person who is never in that checkout. So "closeout fails **without mutation**"
is no longer the accurate phrasing anywhere it appears — the accurate phrasing is "without any
**commit**".

Two refusals guard the staging step, and because they guard it they run exactly where the gate runs
— when code would commit **and** this checkout carries
`mcp/test_support/agents_remember_test_support/code_quality/check.py`. They are **not** closeout-wide preconditions: a
consuming repository with no wrapper runs no gate, is not staged early, and reaches the ordinary
commit step's own `git add -A` exactly as before; the preview reports that as `wrapper-unavailable`.
Where the gate does run, closeout refuses **before staging anything** when

- the code checkout is **not a task worktree**. The test is git's own — `--git-dir` equal to
  `--git-common-dir` is what a repository's own checkout looks like — rather than the contract's
  `kind`, because that is the property the safety argument rests on: `kind` is a label beside the
  path, the git-dir comparison constrains the path about to be written. This is reachable, not
  hypothetical: `default_series_contract` records `code_worktree = code.repo_path`, so a
  series/master contract reaching `worktree_closeout_apply` would otherwise stage in a checkout a
  person works in — overwriting a partial `git add -p` selection and writing a durable blob for a
  deliberately untracked file. Close out the leaf contract instead.
- the code worktree has **unresolved merge conflicts**. `git add -A` over an unmerged index does not
  refuse; it resolves every conflict to whatever the working tree holds and closeout commits the
  `<<<<<<<` markers. Both refusals run before the reset as well as before the add, because
  `git reset` drops the unmerged entries and `MERGE_HEAD` and would silently disarm the second one.

All **nine** `c-12-closeout/SKILL.md` copies carry this — the canonical `skills/c-12-closeout/`
plus the eight per-harness mirrors — and they are byte-identical after the edit (verified with
`md5sum` and `cmp` across all nine, plus the tenth copy under
`mcp/src/agents_remember/package_data/runtime/skills/`, all `e7279e57604ea6c1871ff918cf713449`, all
mode 644). They are generated, not hand-copied: `scripts/sync-skills.py` fans root `skills/` into
those nine targets (the eight harness roots plus the MCP package-data tree), and drift is caught by
`scripts/sync-skills.py --check` inside `_gate.sh`'s `generated_copy_checks`, which **both** local
hook tiers call. **The hooks are no longer the only net.**
`mcp/tests/test_sync_scripts.py::RealTreeDriftTests` reads the real trees in this checkout:
`test_every_skill_copy_matches_the_canonical_tree` iterates all nine `sync-skills.TARGETS` and
`test_every_runtime_package_asset_matches_its_source` iterates all four `sync-runtime.TARGETS`, both
through the shared module-level `drifted_files()` reader over each script's `diff_target`, which
rebases every entry onto the target so a failure names the copy that has to be fixed rather than the
path it shares with eight others; the assertion message names the `python3 scripts/sync-skills.py`
that repairs it.
Because it is a plain `unittest` class under `mcp/tests/` — the sole `testpaths` entry pytest is
given — it runs in the quality wrapper's pytest step, so a hand-edited mirror now fails at pre-push,
at closeout, and in CI, whether or not the contributor ever installed the hooks.
**Know exactly where that stops.** CI still does not invoke `--check` at all (no workflow runs
`_gate.sh` or any `scripts/sync-*.py`, and the wrapper does not either); the guarantee arrives
through the pytest step, not through a workflow wiring. And the tests are only as strong as
`TARGETS`: nothing asserts that set is complete, so a tenth skill mirror added without registering it
would still drift unseen. `test_sync_runtime.py::test_default_targets_only_write_to_mcp_package_data`
pins the runtime target set exactly that way — `sync-skills.TARGETS` has no equivalent.
The six temp-directory cases in `ReplaceTreeTests` were not replaced and still earn their place: they
test `replace_tree`'s crash-safe copy-then-swap semantics, a different property from real-tree drift.
This now matches the harness trees, where
`test_sync_harness.py::test_every_generated_harness_file_matches_its_source` reads the real
generated files and therefore fails in CI too — the test `RealTreeDriftTests` is explicitly
modelled on.

**2. `.gitignore` gained `.dmypy.json` and `.mypy_cache/`, and the reason is item 1.** Because
closeout now stages the whole worktree, any tool dropping left in the tree becomes staged content
and then committed — it is no longer merely "ignored by ruff". `dmypy` writes a `.dmypy.json`
holding a pid and a socket path next to whatever it was pointed at, and it landed in `mcp/src/`
twice during this task's tooling evaluation; one such file reached this leaf's own first commit by
exactly the path-dependence the mixed reset now removes. The rule and its reason are recorded inline
in `.gitignore` itself.

**3. The production E2E spec now type-checks its happy-path payloads against the wire mirrors, and
its fault-injection payloads deliberately stay untyped.** `dashboard/e2e-production/cockpit.production.spec.ts`
fulfils every endpoint itself, so it faced the same question as a unit fixture: is what it serves a
payload the server could produce? Its happy-path terminal payloads now carry
`satisfies TerminalCatalogRow` / `satisfies TerminalOpenSuccessBody`, which found real drift — the
open response omitted `controlEndpoint` and `controlProtocol` (both declared required by
`TerminalOpenSuccessBody`) and spread `harness`/`controlState` conditionally where the server always
sends the key with `null` when unset, so a client bug behind those keys could not have been caught
there. The `missing`/`malformed`/`contradictory` and 4xx/5xx bodies are left untyped **on purpose
and must stay that way**: their entire job is to be shapes the server should never send, and a
`satisfies` there would delete the test. The third answer is the one to quote back at anyone who
reads the spec as producer-verified: the projection is read whole from `src/fixtures/snapshot.json`,
and the spec's own comment says that is **reuse, not provenance** — the biggest payload in the file
is exactly as unverified as a hand-written one, merely unverified in one place instead of many.

**Be precise about what each artifact pins.** `dashboard/src/fixtures/snapshot.json` remains a
hand-maintained sampled payload. `dashboard/src/types/projection.ts`, however, is generated from
`WorkspaceProjection.model_json_schema()` plus the served projection tail, and
the code-quality `stale_generated_files` comparison detects schema and TypeScript bytes that differ from the generator cit:([`stale_generated_files`], mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:602-608). Fixture builders are type-checked against that
generated mirror, `wireFixtureGuard` refuses fixture-side opt-outs, and `contract.test.ts` measures
how completely the manual sample exercises the mirror. The human-maintained boundary is sample
coverage, not the producer-to-TypeScript contract.

## Historical milestone context: 260727-CHATS-IM-L2 Repository Impact

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

The structured Chats path now keeps parent control and siblings usable when one selected child's
history is unavailable or exceeds a bounded source contract. The active projector was decomposed
by mutable authority, and workspace projection ticks gained exact domain invalidation plus
per-file task parsing. The repository's public capability, task, and dashboard surfaces are
unchanged; ownership and failure containment are now explicit in their route overviews.

## Historical milestone context: 260731-EFA-L7 — File-Size Rail And In-Place Facade Splits

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

This master leaf armed the file-size detector (`code_quality/file_size.py`, hard limit 1,200 / architectural failure 2,000+ / emergency cleanup 4,000+, `wc -l` counting, enforced in the project wrapper via `file_size_armed`) and closed the standard's scope loophole (Python source + tests + `dashboard/src` TS/TSX; narrowed "explicitly boring" exception). Over-limit modules were split in place into facades plus private responsibility modules under `kernel/`, `observer/snapshots_impl/`, `observer/reducer_impl/`, and `serving/`, each facade surface pinned mechanically. The test tree was split into in-place families (79 new modules) and the historical CRAP/coverage scope included test roots. Current CCR profile authority separates product measurement from verification inputs: lint/type checks cover both, while product CRAP/coverage does not measure test code.

## Historical Quality Altitude Milestone

The earlier altitude split reduced repeated master-wide work, but its per-leaf acceptance procedure and coverage floor are superseded. Current work uses focused development checks and master-end full aggregation/review without weakening certification owners.

## Historical milestone context: 260731-EFA-L9 Change — First Structural Leaf

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

260731-EFA-L9 is the first leaf that moves code: both serving model monoliths split into the new
`models/conversations/` route (plus `models/terminal_catalog.py` and `models/task_document.py`),
the kernel gained the `kernel/primitives/` vocabulary route, `serving/projections/` took over
the observer projection readers, and `code_quality/layering.py` was built and ARMED as the
package-layering gate (rank violations, cycles, undeclared dirs/imports all fail closed with no
baseline). The move ledger and pre-change serialization baseline prove zero wire drift.

## Historical milestone context: L23 Source-Lineage Enforcement Slice

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

Structural task admission now derives code and external-memory ancestry from
canonical sprint/master/leaf documents and enclosure contracts. The control
plane proves super-to-master and, for leaf roles, master-to-leaf before exposing
a checkout or mutating lifecycle state. Operations projects the same strict
evidence and contract-addressed recovery; no agent must remember a commit,
branch, runtime, or occupant id.

## Historical milestone context: L23 Detached Operation Authority Boundary

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

Checkout isolation now distinguishes four explicit process classes without
turning live coordination into a general CLI capability: long-lived MCP and
dashboard daemons, the plane-owned detached lifecycle-operation worker, tests,
and undeclared checkout execution. The detached worker alone declares
`lifecycle-operation` before loading its services/config because it must claim
and finalize the task's accepted durable closeout or integration operation. It
does not acquire either daemon writer role; an ordinary unpublished checkout
command remains confined to its leaf-local development coordinator and report
root.

## Historical milestone context: L23 Task-Derived Lineage Enforcement

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

Canonical sprint/master/leaf documents and their enclosure contracts remain the sole identity for
source-lineage enforcement. The same transitive code and external-memory ancestry proof now guards
start/resume, the manager's final pre-curator boundary, closeout, and integration. Rechecks after
long quality work and immediately before claim/merge prevent stale work from being documented,
approved, or merged; no agent-supplied runtime or commit identifier becomes control-plane
authority.

## Historical milestone context: R39 Acceptance Topology

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

The repository now has one test-capable environment and two lifecycle acceptance altitudes.
Nonce-attested Dagger runs targeted once at leaf closeout and full once at master integration.
Leaf integration, series/master closeout, hooks, push, pull-request, tag, and publish do not rerun
acceptance. Pull requests keep deterministic non-test validation, and the tag workflow proves main
reachability before publishing. Generic runtime doctrine resolves each repository's concrete
acceptance policy from its own memory rather than embedding this repository's Dagger command.

## IAS Source-Pair Activation And Disposable Queue Boundary

The task topology has a mechanistic closeout-door surface, but the queue is only a disposable
projection of current task truth and current waiting door generations. It owns ordering and
schedulability, not selection, claim, commit, certification, integration, recovery, or terminal
evidence. An otherwise-valid task mutation never waits on queue or activation state: publication
completes first, invalidates the affected projection to explicit invalid-empty, and rebuilds waiting
candidates from authoritative task/door inputs.

Atomic implementation admission belongs to one replace-in-place selector per normalized code and
external-memory source pair. Selecting another live master preserves the former and makes it
observably paused; the selected master enters `reconciling` until its exact source pair is current,
then becomes `active`. Missing or malformed selector authority fails closed only for affected
runtime admission/projection. Normal readers never reconstruct it from task prose, queue rows,
legacy files, or ambient Git.

## IAS Sync And Protected-Source Authority Boundary

Integration and sync remain journaled Git transactions over task-derived protected source refs, but
task-document publication is not serialized behind their long-lived state. A source-pair selection
starts or resumes a contract-addressed sync whose durable record lives at the worktree enclosure
root and whose exact base, source, and pre-sync commits are pinned in Git refs. Automatic sync is
only phase one: a genuine code or memory merge conflict is retained for agent resolution and staged
`continue`; explicit `cancel` restores provably operation-owned pre-sync heads. Cleanup vacates only
the exact selected terminal contract before its canonical pointer is removed.

## Historical milestone context: 260815-DAG-L14 Sprint Structure Route Impact

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

The sprint document now carries first-class seats and typed master links: `SubTaskRef.masterRef`
rows point at the commanded master document and render as real relative links (sprint → master →
leaf click path in markdown and dashboard), `TaskDocument.seats`/`SprintSeat` make sprint seats
structure rather than seat task documents, and `attach_master`/`detach_master` write the typed row,
membership slug, and graph node as one atomic validated batch (L14-R4). Consistency validation
(`validate_sprint_linkage`) hard-fails new-shape drift while legacy shapes surface as facts through
`linkage_report`/`linkageFacts` (L14-R5/R7). The MCP `task_doc` surface registers the new
operations and the dashboard projection carries `seats` + `masterRef`.


## Historical milestone context: 260815-DAG-L12 Route Impact

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

The execution-graph render is now human-readable end to end: `tasks/render.py` emits a deterministic mermaid `flowchart TD` diagram (subgraph per master, lump nodes for atomic masters, labeled edges) joined with real titles via the new `tasks/execution_graph_titles.py`, and `observer/projection_graph.py` builds the render-ready per-node `executionGraphView` the dashboard's new sprint-graph wave-grid panel renders directly (pure CSS grid, no layout library — the documented L12-R3 fallback). New sprint-graph sidecars and test sidecars carry the detail.


## Historical milestone context: 260815-DAG-L15 Route Impact

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

L15 (hygiene sweep and review-doctrine repair) landed across the mcp application/tasks/controlplane routes: the served-build preflight gate (`tasks/serving_preflight.py`), the async memory-quality surface (`application/memory_quality_runs.py` + `wait`/`run_id` registration), the typed authoring dialect (judgment-required, move-retargets-edge, node-kind order, named cycle members), `create=False` dry-run locks, and the L7 `worktrees/orchestration_portfolio.py` deletion (recorded decision: doctrine + queue mechanism). The review-doctrine repair (no self-review, evidence-type matching, PR-8, RV-1 extension, D-6 bounded requirement ids) was folded into the memory-repo canonical `system/coding-guidelines.md` Source Comment Scope rule at master level.

## Historical milestone context: 260815-DAG Master Full-Gate Repair Route Impact

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

Thirty-two modules moved into four new packages (`application/task_docs/`, `models/queue/`, `worktrees/queue/`, `worktrees/integration/`); the `task_doc` special ops gained declared `TaskDocResponse` wire fields with the `_sprint_doc_identity` merge (the strict-envelope rejection bug class); `worktrees/modules/closeout.py` and `worktrees/reopen.py` refactored (`_closeout_quality_facts`, `_reopened_contract`); the orchestration-task template heading restored; the dashboard snapshot gained execution-graph/super-to-leaf fixture coverage.

## 260821-CLIVE-L2 Historical Intermediate Architecture

At repository level, L2 established one total configured-contract admission API and one root-local
journal that owns generations, mutation/termination/legacy/direct-landing evidence.
Retry/recover/cancel/revise are task-addressed and evidence-derived. Bounded schema-1 migration and
pre-locator enclosure adoption are explicit, removable tools, never fallback readers. The
selected/in-flight/certified queue rows described by the L2 handoff were removed by L3; current
scheduling is the disposable waiting-door projection described in the Hot Path Summary.

The committed package layout mirrors those owners: public adapters are under `application/lifecycle/`; durable operation authority is under `worktrees/integration/lifecycle/`; direct landing and bounded legacy repair have isolated sibling packages; tool response models live under `models/tools/`; and start collaborators live under `worktrees/modules/startup/`. No former flattened path is retained as a compatibility surface.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| Closed admission and one public projector. | `admit_configured_contract`; `project_configured_contract_refusal` | mcp/src/agents_remember/application/lifecycle/configured_contract_admission.py:96-169; mcp/src/agents_remember/application/lifecycle/configured_contract_admission.py:326-364 |
| Root manifest/journal location authority. | `LifecycleOperationLocation`; `resolve_lifecycle_operation_location` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_location.py:78-113; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_location.py:473-517 |
| Task-addressed lifecycle controls. | `control_operation` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_controls.py:155-225 |
| Retained-generation projection derives public legal controls and recovery surfaces without owning evidence. | `operation_projection` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py:145-172 |

## Historical milestone context: 260824-PDLS — Python Evidence Altitudes

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

The repository has one pinned Dagger environment for Python investigation and lifecycle acceptance.
Candidate A's host command, sealed cohort, static closure analyzer, and self-proof were removed
after representative exact-candidate measurement failed to earn their maintenance cost. Its seven
unique product assertions remain ordinary explicit-lane pytest regressions and form the pure cohort
inside the non-accepting representative measurement route. The same master establishes a durable
evidence lifecycle/cadence catalog, product-only Coverage/CRAP, one dependency-ownership graph for
selection and retry, and owner-level causal failure localization. Its package route is documented
at `onboarding/mcp/test_support/agents_remember_test_support/testing/overview.md`; durable workflow
guidance is in `system/tools.md`. Host pytest, direct coverage, and the quality wrapper remain
prohibited, with no compatibility fallback.


## Update History
- 2026-09-06T22:41:21+00:00: Generated citation repair: "gate_staged_code as _gate_staged_code" repointed to mcp/src/agents_remember/worktrees/modules/closeout.py:105-105. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-07T00:34+02:00 — Reconciled current source anchors and diagnostic/four-worker policy; removed obsolete test-proof claims without altering verification pins.


- 2026-09-06T21:56+00:00 — Reconciled d3610903 development/certification and pre-gate memory preparation policy while preserving the production feature inventory, ownership narratives, invariants and original historical entries. Retired obsolete test citations and marked milestone procedures historical; verification pins remain closeout-owned.


- 2026-09-06T04:32:25+00:00 — L32 private-candidate curation: Updated the current citation-repair boundary from the retained L30 defect to source-reviewed private C b34f4a59. Existing unrelated route/history content is preserved; this is not an aggregate acceptance or delivery statement.

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-05T22:23+00:00 — L30 route-impact review against `6e4ab81f6ae52bce35003377bb3aec7877554ed7`: Reconciled actual L30 publication and lock ownership while preserving L32 and production lifecycle obligations; unchanged route knowledge remains preserved.

- 2026-09-05T07:40+00:00 — L31 cumulative source review at ea35964985f30080488270e71ac81657ac40682b: reconciled current profile, intent, publication, dispatch and provider contracts; preserved prior frontend/lifecycle milestones as history; recorded R10/R21 and unconstructed certification consumers. Verification records source review, not execution or acceptance.

### Historical feature entries retained from the prior 0506b57a source-review baseline

The following entries are the original development narrative, preserved for provenance. Current behavior is stated in the feature inventory above; these entries are not current API, layout or delivery guarantees.

> | Observable session lifecycle | The 3.0 browser-dashboard substrate: an append-only `ar-observer-event/v1` event log with trust provenance, an ambient process-singleton lifecycle (six `lifecycle_*` signals, heartbeat, TTL sweep, tool-call attribution), and a pure projection reducer that folds events + file snapshots into resolved state (lifecycle tree, metrics, staleness, per-lifecycle token fuel gauge, drift/sidecar/setup/route/ledger analytical surfaces, precomputed action availability, and a server-computed attention queue). Task 27 adds a **lifecycle next-step hint engine** — every MCP tool response now carries a `nextStep` computed from the projected lifecycle state at the `_tool_payload` choke point (a one-time front-half prose rundown from `lifecycle_start`, then a linear per-tool chain that delegates to the worktree `guidance.lifecycle_guidance` state machine and points at the existing `lifecycle_gate` at gate junctions; built on the existing gate, with auto-firing a later step). Task 28 makes **NOTIFY-AND-CONTINUE** the active turn-end model: a new public `lifecycle_turn_end_notification` tool + a non-terminal `awaiting-developer` lifecycle state (notify the developer and stop — no gate, no wait — and the next AR tool call auto-resumes at the `_tool_payload` choke point), the next-step hints repoint off `lifecycle_gate` onto it, a one-line reducer dedup collapses the duplicate gate-open/blocked-gate attention item, and the old `lifecycle_gate`/inbox stack is parked (kept, un-hinted). Task 29 makes throwaway event/runtime surfaces lifecycle-aware: raw Event River lifetime is backend-retained by lifecycle state rather than frontend count caps, worktree provider/runtime facts require active enclosures, and actionable-drift attention carries repo/branch/source/memory provenance with targetless dismissal. | `agents_remember.observer`, `lifecycle_*` tools, `next_step.py`, `observer/` route overview, `docs/design/observable-lifecycle.md` |

> | Dashboard serving layer | The local mission-control server: `agents-remember dashboard` runs a FastAPI app over the observer projection — a multiplexed `state` SSE stream (snapshot + per-entity deltas), a one-shot state endpoint, a raw `event` SSE channel with byte-offset resume and a `ready` hydration marker after retained backlog replay, a POST action plane (slice 6b records gate-decision verbs as developer-attributed gate decisions; lifecycle transitions stay no-mutation; targetless actionable-drift dismissals persist acknowledgements), sim-mode replay, and the static cockpit bundle. Slice 6d begins **Mode B2** (the dashboard-hosted terminal): 6d-1 lands the terminal-host backend (`serving.terminal` — a `TerminalHost` registry of tmux-wrapped stdlib-`pty` sessions launching the harness render-not-scrape, fixed-argv/OS-user/localhost); 6d-2 adds the `/api/terminal/{session}` WebSocket bridge (PTY ↔ browser; + the `websockets` core dep), with the xterm.js visual (6e) to follow. Transport only (reads via the one coordination-state path abstraction); the frontend lives at the root-level `dashboard/` sub-project. Task 26 adds a **hot-reload dev env** — a `--reload` flag on the `agents-remember dashboard` CLI. 260703 L1 makes `--config` **optional** on that CLI: `cli/discovery.py` discovers the trusted settings by walking upward from the working directory (the settings convention before an `.mcp.json` registration's recorded path; nearest wins; a semantic usability probe keeps the repo's tracked placeholder template from shadowing real settings). 260703 L2 gives it **daemon mode**: `--daemon` detaches a supervised dashboard that survives the terminal (`--status`/`--stop` manage it; state + rotated log under `<coordinationRoot>/logs/dashboard/`; identity-checked liveness so pid reuse never resurrects a foreign process), and the fail-loud `dashboard` settings object (`autoStart`, `port`) has every MCP server boot ensure the daemon — adopt healthy, spawn absent, **restart on version mismatch** — through a threaded, total, stderr-only hook that can never break the stdio handshake. | `agents_remember.serving`, `agents-remember dashboard` CLI, `serving/` route overview, root `dashboard/` |

> | Dashboard frontend (mission-control cockpit) | The browser cockpit (`dashboard/src/`): a near-read-only Vite + React 19 + TS-strict UI over the observer projection — model-C shell (top bar + rails + switchable viewport + event river + mode bar), cockpit panels plus the slice-6e Chats terminal, and a shared grammar/primitives library. Styled with the layered blueprint (slice 5d): **Panda CSS** (typed tokens + build-time/zero-runtime recipes) for styling + **React Aria** (headless a11y — the mode bar / pivot `ToggleButtonGroup`s and the lifecycle `ListBox`); the CRT effects layer isolated. Now a memory citizen (`dashboard/src/**` onboarded). As of slice 5e the **Engine Room** is an enclosure-centered, state-backed process map (`panels/engine-room/`) that makes the worktree manager's operating model legible — official line → code/memory worktrees → contract coupler → CGC/GrepAI engines — with observed/derived/planned/missing fact-state honesty, fed by a new server `analytics.engineProcesses` projection. **Slices 5f–5g** animate it as a worktree-lifecycle state machine on the prototype's **bird's-eye podracer canvas**: boot choreography (center-out engine charge + travelling conduit packets), failure overlays (steady blocked gates · isolated engine fault flicker · amber reindex reroute), and the **live/teardown** states (sync block · a terminal integration-conflict STOP · abandon dissolve); engines read **green when active** (empty off · cyan booting · red fault · amber reindex). The successful-landing arc (closeout train · PR/push · carryover · cleanup teardown) landed in **5h**; **5i** then made the canvas a dev scenario-player-driven build-up/tear-down stage; and **05k** completed the motion property-split onto GSAP timelines (`useEngineTimeline`) + Motion (`AnimatePresence`), CSS static. A **visual-parity pass** then completes the prototype fidelity: the atmospheric blueprint backdrop (5g G6) + a cockpit Effects/Calm toggle, the full HUD decal layer (canopy frame, engine spine + petals, the **left official-line engines** + conduits + coupler, lane annotations), and a fixed-height room layout via a `Panel` `fill` variant (the centre canvas + right panel stop resizing per selection; the side columns scroll). **Slice 05o** opens the engine room's **failure-mode** choreography (lifting the `podstage.html` non-happy-path scenes the canvas didn't yet drive, one mode at a time): **mode 1 (T3B memory/ledger block)** adds the **scan-ring** (the cyan pre-block ledger-verify sweep) + **ghosted-lane** (the held memory lane dims+desaturates while the code lane stays solid) primitives and the `memory-block` player scenario (verify → block → reconcile → provider clone → nominal), with a coupled engine-gauge polish (flat gold bezel, constant-gold petals). **Slice 05o Mode 2 (T1B stale-base block)** adds the **pruned-base-node** primitive plus the big red **fleeting-enclosure** box, and a failure-indicator polish pass anchors the verify/block pointers **ON the repository node** (topmost layer) and gives every alert overlay a Motion fade/pop transition. **Slice 05o completes the failure-mode library** — the canvas now drives all eight `podstage.html` failure modes (memory/ledger block, stale base, provider-plan block, seed fault, reindex reroute, live sync, integration conflict, abandon) on a shared set of node-anchored failure primitives (steady gate, scan ring, ghosted lane, pruned node, refused-conduit flash, moved badge, engine-dropout, terminal STOP, dissolve) with Motion fade/pop transitions. On the Task-6 control-plane branch the cockpit also gains its first interactive surfaces: **Slice 6e** adds the visible **Mode B2 terminal** — a full-bleed **Chats** view (`panels/Chats.tsx` + a code-split `Terminal.tsx` xterm.js wrapper) that renders the 6d PTY stream over the `/api/terminal` WebSocket (`data/terminal.ts` — keystrokes/resize ↔ raw PTY bytes), the cockpit's first bidirectional surface. **Slice 6e-2a** makes it a **create** surface: a "＋ Terminal" control spawns a **dashboard-owned** shell at the workspace root via the `POST /api/terminal` opener (`TerminalHost.open`, server-resolved command) — the dashboard owns the session it created. **Slice 6e-2b** adds per-harness launch buttons — a detection-driven button per *installed* harness (Claude Code / Codex / Pi.dev, via the new `GET /api/harnesses` + the `serving.harnesses` registry) beside ＋ Terminal, each spawning that agent at the workspace root. **Slice 6e-2c** moves the open sessions into a dedicated left-rail **session switcher** (`panels/SessionList.tsx` — a React Aria `GridList`, single-select = active session, per-row close ✕), replacing the horizontal tab strip, and unifies the harness buttons onto ＋ Terminal's golden look. **Slice 6e-3** adds **context injection** — a `SessionComposer` docked below the terminal sends a block of text into the active session's stdin as a bracketed paste (the on-ramp to 6f highlight→feedback). **Slice 6e-4** hardens terminal persistence — the open-session registry moves into a `data/sessions` store, and a live terminal survives both a cockpit *view* switch and a *session-tab* switch (kept mounted, hidden via CSS, never unmounted), while the backend PTY spawn gains a controlling terminal (`os.login_tty`) so tmux honors resize. **Slice 6f-1** adds the **highlight → context-package** composer — a cockpit text selection raises a React Aria popover to send the selection + a message into a chat session's stdin (single chat / a selector / create-on-Enter when none is open + ＋ new chat), reusing the live stdin channel; no silent action, not ACP. **Slice 6g** turns the detail panel into a **task-document reader**: a series **master** shows its overview (objective + ordered sections) + a clickable **sub-task index** with in-panel **drill-in** into each slice (the back/parent up-link in the sticky panel header), **markdown-rendered** task prose (a new `grammar/Markdown` primitive — react-markdown + remark-gfm, memoized), and **cross-master "→" navigation** that jumps between series lifecycles (a master links to a parallel/child series via the contract-paired projection). A **slice 07b polish** extends the engine-room G6 atmosphere to empty panels: a shared `panels/EmptyStateBackdrop` puts a faint, effects-gated boomerang-video backdrop behind the no-selection (detail) and no-session (chats) empty states — pure atmosphere (aria-hidden, absent under the Effects/Calm toggle / reduced-motion), the message always shown. Task 12 refines the topology constellation so backend-supplied repo coverage parents workspace provider satellites to repo nodes while worktree providers stay bound to their worktree groups; GrepAI `targetRepos` are addressable project targets inside one aggregate provider instance, not separate provider processes. **Task 33** scopes the topology to active work — an active-enclosure constellation (`workspace → source checkouts → active worktree enclosures`) that folds each lifecycle into its enclosure node and filters on a new served `activeWorktreeGroups` set (shared with the Engine Room's active admission). Task 29 S7 hides the former **Lifecycle Flow** tab from the cockpit while leaving `panels/FlowTab.tsx` dormant in source. **260715-FEUI-L1** opens the react-tui-cockpit series: a new full-bleed keep-alive **Sessions** cockpit view (`panels/session-cockpit/` — rail/stage/inspector shell + cmdk command palette; pure command-registry/layout modules in `data/commands.ts`/`data/sessionLayout.ts` and the tinykeys keyboard-zone contract in `data/keymap/` with the PTY reserved set's five-source collision-verification records). Its skin is a **scoped WebTUI layer** (OQ-D = adopt): `@webtui/css@0.1.9` exact-pinned, ONE mapping file `styles/webtui.css`, a `webtui` cascade layer slotted between effects and tokens, build-time prefixer confinement under `[data-view="sessions"]`, guarded by the standing `test/webtuiSpike.test.ts` assertions. **260715-FEUI-L2** fills the Sessions cockpit's data layer, rail, and stage: the 2500 ms catalog poll HOISTED to a shared refcounted driver (`data/catalogPoll.ts` — Chats is now a consumer; the poll stays the authoritative session-row reconciler), a gated `/api/events` seat-event pre-apply layer (`data/seatEvents.ts` — retire/land/rename/turn-state, riding the Event River's one EventSource behind a per-connection backlog gate), the FULL catalog wire mirror (`types/terminalCatalog.ts`, re-exported by `data/terminal.ts`), the per-seat cockpit client store with honesty invariants (`data/sessionCockpitStore.ts` — requested ≠ effective, queued never moves the five-tier launch evidence), THE one seat-state dot grammar (`data/stateGrammar.ts` + `StateDot` — 2.4 s ease-in-out pulse ruling, blocked-on-human steady), and the RULED role-driven rail hierarchy + fleet attention + stage HeaderStrip/inspector card (`data/railModel.ts`, `panels/session-cockpit/{SessionRail,SessionStage,HeaderStrip,SeatInspector}.tsx`); one open sev-3 developer ruling on status-chip vocabulary width. **260715-FEUI-L6** fills the cockpit's PTY stage surface, structured interactions, and session lifecycle actions: keep-alive REAL xterm panes (`panels/session-cockpit/PtySurface.tsx` over the shared `panels/Terminal.tsx` — DOM renderer BY MEASUREMENT via the in-repo `/dev/pty-bench` harness, 12-pane 60 Hz lock; webgl a lazy escalation path; `@xterm/addon-webgl` + `@xterm/addon-serialize` exact-pinned), two server-truth pane archetypes (controlled line-log vs legacy raw; client-side observe-only OSC/bell harvesting for legacy raw only — `data/ptyHarvest.ts`), the ONE structured-interaction axis whose answers ride ONLY the landed gate channel (`InteractionBar` + `data/interactionAnswer.ts` → `POST /api/actions/approve`, answer as decision note; never a terminal write), the WorkingLine turn theater (working-only, welded UA-7-gated stop), honest terminate flows with verbatim failures + informational stop residuals that outlive tombstoned rows (`data/sessionLifecycle.ts`, focus-independent retire-residual sweep; retire itself stays agent-side — the cockpit renders it), per-pane screen-reader opt-in + always-named terminal landmarks. **260715-FEUI-L3** adds the Sessions cockpit's **capability catalog client + launch flow**: a memory-only per-harness capability-envelope store over `GET /api/harnesses/{h}/capabilities` (`data/capabilityCatalog.ts` — dynamic-only, envelope dropped on any error, verbatim error surfaces, honest refresh semantics, generic miss-cost copy), the pure launch machines + classifying open client (`data/launchFlow.ts` — advertised-order efforts, model-switch re-gating, the BOTH-knobs-or-NEITHER launch selection posted through `data/terminal.ts`'s extended open body, uniform fail-loud 200/400/409/outcome-unknown paths), the pure launch-evidence tier machine (`data/launchEvidence.ts` — Claude launch pairs never exceed model-validated) rendered by the new five-glyph `grammar/EvidenceBadge`, the capability/open wire mirrors (`types/{harnessCapabilities,terminalOpen}.ts`), the R3 contract fixture pack + conformance suite (`test/fixtures/{capabilityEnvelopes,controlMessages,openResponses}.ts`, `test/contractCapabilities.test.ts`), and the cockpit launch surfaces (`panels/session-cockpit/{LaunchFlow,FailedLaunchBanner}.tsx` — palette-opened launch overlay; verbatim failed-seat refusals with Retire via the operator terminate route + corrected relaunch). | root `dashboard/`, `dashboard/src/` route overview, `@xterm/xterm`, `react-aria-components`, `@pandacss/dev` |

> | Hosted chat leaf reassignment | Running dashboard-hosted chats can move their durable `leafKey` after creation without respawning their tmux/xterm session. The dashboard route and the public `attach_terminal_session_to_leaf` MCP tool share the same server-authoritative catalog policy, surface `leaf-taken` without local mutation, and broadcast/rehydrate `"leaf"` catalog changes so open tabs stay synchronized. | `attach_terminal_session_to_leaf`, `serving.terminal_leaf_assignment`, `dashboard/src/data/sessions.ts`, `dashboard/src/panels/Chats.tsx`, `dashboard/src/panels/RailChat.tsx` |

> | Agent orchestration communications | Durable agent-to-agent inbox messages address orchestrator/manager/worker roles, carry message-kind and artifact metadata, and remain pollable while also attempting hosted-session stdin push through the echo-confirmed paste seam. Consume is a monotonic terminal snapshot: a concurrent in-flight delivery may append stale physical evidence but cannot resurrect pending/redelivery state. Turn reports and master handovers have typed artifact helpers/templates; inactivity or missing report nudges are rate-limited, logged as `orchestration.nudge`, and delivered to manager inboxes. | `operator_inbox_*`, `orchestration_nudge_manager`, `serving.inbox_delivery`, `controlplane/orchestration_artifacts.py`, `controlplane/orchestration_nudges.py`, `l-01-agent-lifecycles` templates |



- 2026-09-05T06:12+00:00 — Composed retained CCR route contributions without replacing sibling knowledge; preserved prior source-verification metadata and historical entries.

- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 route impact: re-anchored the retained-generation projection row to the current `operation_projection` definition span after the L18 projection rewrite grew `lifecycle_operation_projection.py`. Verified at code commit f93ac631ca161e5880db3a937728cb256686b13b.


- 2026-09-01T11:33+02:00 — No route impact: CCR-L11 Attempt 10 preserves the rank-3
  `certification` package boundary and root repository structure. Its changes are bounded internal
  contract forcing, one dominated-refusal deletion, and exact verification-input ownership; no
  executor, repository profile, lifecycle, or memory-gate authority moved. Verification remains
  closeout-owned.

- 2026-09-01T05:28+02:00 — CCR-L11 Attempt 9 surfaced the root `layers.toml` authority and the
  explicit rank-3 `certification` boundary. Later rank integers shift to preserve order/index
  identity; no executor, repository profile, lifecycle-terminalization, or memory-gate ownership
  moved into the generic certification package. Verification remains closeout-owned.

- 2026-08-31T20:30+02:00 — 260831-DER: removed the obsolete direct-current-checkout wording and
  recorded the actual boundary: closeout remains worktree-only, ordinary series integration is
  independent of `directExecutionEnabled`, and direct landing is reserved for an explicitly
  selected leaf delivered without an enclosure.

- 2026-08-30T12:34+02:00 — 260821-ARSPAWN-L3 separated ordinary ambient architect bootstrap from
  explicit named-role takeover and clarified that role-table dispatch/tool rows describe fixed
  structural authority rather than settings overrides. Verification remains closeout-owned.

- 2026-08-29T16:13+02:00 — Reconciled repository-wide execution authority to the single Python
  3.13 line and canonical exact 3.13.15 source build; the former `py311` floor is retained only as
  historical context. Verification remains closeout-owned.

- 2026-08-28T15:52:15+02:00 — No route impact: the hook now selects only the MCP-local
  environment and refuses missing quality dependencies; the focused regression test does not
  change repository architecture, ownership, or routing.

- 2026-08-28T10:03:40+02:00 — Reconciled the repository-wide quality summary with Candidate A's
  deletion: Python investigation remains Dagger-owned and no direct wrapper/compatibility route exists.

- 2026-08-28T05:10+02:00 — Replaced the obsolete two-route description with measured Candidate A
  retirement, ordinary preservation of its seven assertions, and one Dagger Python environment.
- 2026-08-27T22:15+02:00 — Clarified attempt-journal recovery: malformed rows before review are
  preserved non-attempt corrections; handed-off rows require independent rejection.
- 2026-08-27T21:53+02:00 — M40@v2/M44@v2 task-workflow impact: separated formal review-handoff
  attempts from internal protocol events and replaced repeated evidence bodies with lightweight
  content-addressed journal records; summaries remain non-gating.
- 2026-08-26T15:20+02:00 — No route impact: the IAS ledger-history repair changes MCP worktree
  lifecycle semantics only; root repository ownership and routing remain unchanged.

- 2026-08-26T08:18+02:00 — Reconciled the root authority map with source-pair atomic activation,
  pause/reconcile switching, retained sync-conflict continuation/cancellation, unlocked task
  authoring, disposable queue invalidation/rebuild, and exact terminal selector release. Real
  commit verification remains closeout-owned.

- 2026-08-25T01:56+02:00 — 260824-PDLS reconciled the explicit cohort, durable evidence lifecycle,
  product-only scoring, dependency-owned selection/retry, and causal localization; retired the
  unused rich-sim generator and task/date model-split snapshot.
- 2026-08-24T21:23+02:00 — 260824-PDLS added the bounded Python diagnostic route and preserved
  Dagger as sole acceptance authority.

- 2026-08-24T16:00+02:00 — Final cumulative closeout audit: replaced the last live
  pre-L3 queue wording with the implemented disposable scheduling projection and preserved the L2
  state only as explicit migration history.

- 2026-08-24T13:51:26+02:00 — 260821-DAGQC-L4: reconciled the root inventory and
  governing doctrine for NUL-safe untracked review evidence, effective priority, graph-optional
  planning, atomic graph adoption, canonical handover references, and direct targeted Vitest as
  diagnostic-only. Canonical/generated sync is reported green; Dagger acceptance remains pending
  and closeout-owned.
- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: recorded the final package ownership map, repaired root evidence paths, and verified the L2 repository overview at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: refreshed current route intent and source evidence for the accepted full L2 candidate; verification provenance and contract-scoped quality enforcement remain architect-closeout-owned.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1 candidate-11 curation rebind: refreshed the
  formatter-moved `gate_staged_code` source coordinate against accepted tree `4241908c`.
  Verification metadata remains pinned until governed closeout.

- 2026-08-21T02:50+02:00 — 260821-ARSPAWN-L1 root route impact: the Agent-facing session dispatch inventory row now names `dispatch_agent` as the one public spawn tool (plane + ambient caller kinds) with `spawn_agent_session` the internal primitive; full vocabulary adoption across skills/docs is the L3 leaf scope. Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair route impact: task-document, closeout-queue, and integration modules moved into the new `application/task_docs`, `models/queue`, `worktrees/queue`, `worktrees/integration` packages; the `TaskDocResponse` special-op wire fields + `_sprint_doc_identity` fix; closeout/reopen refactors; orchestration-task template phrase restore. Verified at code commit e5cb139f.


- 2026-08-20T21:30+02:00 — 260815-DAG-L15 route impact: served-build preflight, async memory-quality surface, typed authoring dialect, create=False dry-run locks, L7 orchestration_portfolio deletion, and the review-doctrine repair (D-6 folded into the canonical system/coding-guidelines.md at master level). Verified at code commit de3a0fd9.



- 2026-08-20T10:45+02:00 — 260815-DAG-L12:   L12 render-ready sprint graph: mermaid document diagram + dashboard wave-grid view with the primitives-only projection builder and shared title join. Verified at code commit b7f2c8e2.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16 route impact: seat-independent task-execution fallback
  (declared caller on the closeout-queue and structural gate tools when no plane seat exists;
  hosted seat wins; conflict refuses), the branch-addressed `record_route_review` binding
  (L16-R6), the `direct_landing` operation (L16-R8), and the recovery-naming refusal dialect
  (L16-R9). Verified at code commit a9d50e08.


- 2026-08-20T05:00+02:00 — 260815-DAG-L14 route impact: the sprint document gains first-class
  `seats`, typed `masterRef` links, and the atomic `attach_master`/`detach_master` operations;
  consistency validation and the read-only `linkage_report` surface are wired; doctrine files
  updated to the new flow. Verified at code commit 8071a644.

- 2026-08-19T22:32+02:00 — 260815-DAG-L13 route impact: the JSON-primary task documents row now
  records the atomic-sequential default for graph-less sprints and the
  `author_execution_graph` bootstrap/edit seam; the explicit-migration sentence is gone with the
  removed `migrate_execution_topology` operation. Verification remains closeout-owned.
- 2026-08-19T04:20+02:00 — No route impact: 260815-DAG-L10 moved series closeout reports (operation log, citation source-index cache, Dagger test sandbox) from the task enclosures root to the master worktree group `worktrees/<repo>/<master>-ar`; the repository overview purpose is unchanged.
- 2026-08-18T12:00:00+00:00 — No route impact: 260815-DAG-L9 added the read-only execution-topology migration inventory and the operator migration/rollback reference; the repository overview purpose is unchanged.
- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-17T12:30+02:00 — No route impact: 260815-DAG-L5 added the organizational direct-super topology across the worktree integration path; the repository overview purpose is unchanged.

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: reconciled this governing route with the frozen integration-authority implementation and forcing surface. Verification remains closeout-owned.

- 2026-08-15T13:27+02:00 — No route impact: L3's Pyright repair adds one test narrowing and does
  not alter repository behavior or execution topology.
- 2026-08-15T13:18+02:00 — No route impact: L3's repository-format pass changed only Python
  layout; the dependency-aware queue feature and execution topology are unchanged.
- 2026-08-15T13:08+02:00 — No route impact: L3's fast-hook repair only normalizes imports and
  private test bindings; repository features and execution topology are unchanged.
- 2026-08-15T12:53+02:00 — 260815-DAG-L3 route impact: completed the exact evidence, atomic
  landing, durable-state, and lifecycle-recovery forcing for the same pre-closeout queue design;
  repository routing and the mechanical-versus-judgment boundary are unchanged.
- 2026-08-15T09:10+02:00 — 260815-DAG-L3 route impact: documented the durable pre-closeout
  candidate queue, the manager/orchestrator authority split, exact evidence binding, atomic blockers,
  and lifecycle-owned closeout/integration seams. Verification remains pinned to the leaf base until
  closeout stamps the candidate commit.

- 2026-08-15T02:42:41+02:00 — No route-model change: the L1 review repair closes task-document
  identity and writer-census bypasses inside the already documented execution-topology route; the
  repository inventory and the separation between mechanical topology and scheduling judgment stay
  unchanged.
- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1 route impact: task documents now persist an explicit
  organizational/atomic master nature and a sprint-owned reasoned AON graph. The server validates
  exact commanded membership, derives waves mechanically, and projects the contract to generated
  dashboard clients; scheduling judgment remains outside this foundation leaf.

- 2026-08-14T14:03:04+02:00 — No route impact: R46 changes only the assertion spelling for an
  existing test timeout and removes its intentionally untaken local branch. Production,
  repository inventory, route structure, and authority boundaries are unchanged; verification
  remains pinned to the last committed source until closeout.

- 2026-08-14T13:41:27+02:00 — No route impact: R45 removed only the tracked
  `dashboard/node_modules` absolute symlink. That machine-local dependency link is excluded from
  onboarding and route coverage, so the repository inventory, route model, and authority map are
  unchanged; verification is pinned to the exact deletion commit `aeca9a2839c965218a61a3040e15cb84367ebeca`.

- 2026-08-14T11:29+02:00 — R39 curator: reconciled the root route with exact-once lifecycle
  acceptance, workflow de-duplication, and repository-generic runtime doctrine. Verification
  remains closeout-owned.

- 2026-08-14T06:10+02:00 — L23 curator: reconciled the repository inventory and authority map
  with exact-candidate, Dagger-only acceptance, fail-closed host suites, and the extracted staged
  quality owner. Verification provenance remains closeout-owned.

- 2026-08-13T12:26+02:00 — No route impact: final L23 stabilization extracted one internal
  closeout helper, narrowed registrar naming, made five test package-root imports deterministic,
  and rendered the already-durable lifecycle command in Hangar. Repository architecture and
  authority boundaries remain unchanged; verification provenance remains closeout-owned.


- 2026-08-13T09:05+02:00 — L23 integration-gate follow-up: source-lineage enforcement now spans
  start/resume, the mandatory pre-curator boundary, closeout, and integration, including
  post-quality and final pre-claim/pre-merge rechecks. Detailed package moves and proofs live in
  the MCP, lifecycle-role, and test routes; the repository's task-derived identity and
  code/external-memory architecture remain unchanged. Final provenance remains closeout-owned.
- 2026-08-13T00:07+02:00 — 260731-EFA-L23 post-closeout worker-authority repair: recorded the repository-level process-authority split. The detached lifecycle-operation worker may reach its plane-owned live operation without becoming an MCP/dashboard daemon, and undeclared checkout CLI isolation remains fail-closed. The owner reports 46 focused tests, Ruff clean, and diff-check clean. Verification remains closeout-owned.
- 2026-08-12T20:20+02:00 — L23 curator: added the repository-wide source-lineage admission and operator-visibility boundary; verification remains closeout-owned.

- 2026-08-12T15:19+02:00 — L23 curator: documented the pinned observable Dagger quality path and its enclosure-owned reports at repository altitude; verification provenance remains closeout-owned.
- 2026-08-12T10:08+02:00 — No route impact: the rc7 release leaf changes only the public
  README version pin and existing package-version authorities; repository routes and subsystem
  ownership are unchanged. Verification metadata remains pinned until closeout.

- 2026-08-12T09:20+02:00 — No route impact: the 260731-EFA-L20 reopen removes one intentionally unreachable test body after the master coverage gate identified it; repository architecture and routing remain unchanged.
- 2026-08-12T08:41+02:00 — No route impact: 260731-EFA-L20 changes only regression implementation and direct boundary coverage needed by the existing master quality contract; repository architecture and routing remain unchanged.
- 2026-08-12T07:10+02:00 — 260731-EFA-L24: changed the master full-
  gate resource default from an artificial ceiling to host-managed RAM/swap,
  kept pytest `-n=auto`, and retained the hard cap only as an explicit
  constrained-environment setting. Verification metadata remains pinned until
  closeout stamps L24.

- 2026-08-12T01:38+02:00 — No route impact: 260731-EFA-L22 repairs master-quality enforcement,
  removes cache-only layering false positives, and splits three oversized test modules; the
  repository feature inventory and top-level subsystem boundaries are unchanged.

- 2026-08-12T00:20+02:00 — Corrected parallel-execution ownership to root pytest `addopts`, shared
  by raw and wrapped runs; `-n=0` remains the explicit serial diagnostic override. Verification
  metadata remains pinned until closeout.

- 2026-08-11T23:56+02:00 — Recorded automatic pytest-xdist worker selection, the matching
  checkout/package dependency boundary, and retry-proof invalidation across executor-version
  changes. Verification metadata remains pinned until closeout.

- 2026-08-11T19:58+02:00 — 260731-EFA-L19 curator: reconciled the repository overview with the
  enforcement-first separation between structural task-document/role control and private
  plane-owned runtime addressing; implementation detail remains routed to the affected children.

- 2026-08-10T19:57:55+02:00 — No route impact: 260731-EFA-L21 confines undeclared
  checkout CLI coordination to the linked worktree's disposable provider-runtime root. The
  repository inventory and top-level feature routing remain unchanged; current mechanics live in
  the `mcp/`, application, kernel/primitives, controlplane, and tests route documentation.
  Verification metadata remains pinned until closeout stamps the L21 code commit.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 route impact: recorded the model extraction, kernel
  primitives, projections move, and armed layering rail at the repo level. Verification metadata
  pinned until closeout stamps the L9 code commit.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 route impact: recorded the quality altitude ladder
  (targeted leaf contract, once-per-master full wrapper at the master integration gate with the
  settings-owned memory cap, per-leaf `memory_quality_check` carve-out, loud refusal shapes).
  Verification metadata stays pinned until closeout stamps the 260731-EFA-L17 commit.

- 2026-08-07T23:35:00+02:00 — 260731-EFA-L7 route impact (trace delta): recorded the armed file-size rail, the scope closure, and the in-place facade/test-family splits. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: added the Frontend Rail section (ESLint rail, size splits, coverage/budget/knip/trap, Playwright, hooks, Python ripple). Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-05T22:30+02:00 — No route impact: 260731-EFA-L16 (the cross-store lock-order repair, its forcing tests, and the coding-guidelines/spawn-doctrine skill chain) is recorded in the `mcp/` and `skills/l-01-agent-lifecycles/` route overviews and their children; this root inventory was reviewed and is unchanged. Verification metadata pinned until closeout stamps the L16 code commit.
- 2026-08-04T13:15:12+02:00 — 260731-EFA-L6 S18-B02 curator: extended the code-quality and docs-index claims through their operative sections and regenerated the final ranges with the scoped fixer.

- 2026-08-03T23:26:43+02:00 — 260731-EFA-L6 S18-T3: superseded the deferred-codegen account.
  `types/projection.ts` is generated and stale-checked from the Pydantic projection schema;
  `snapshot.json` remains a manual sample whose coverage is measured separately. New ranges are
  ranges were normalized by the scoped fixer.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No route impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` (14 modules), moved `worktrees/status.py` in as `application/worktree_status.py`, and renamed `mcp/tests/test_controller_guards.py` to `test_application_guards.py`. The repo's structure, feature inventory, and functional areas this overview describes are unchanged — the rename replaces MVC vocabulary that described nothing about the contents with the layer the package actually is; the vocabulary is "the application layer" for the package and "an application entry point" for one function. Reviewed this overview's body: it does not name the renamed package outside dated history entries, which are preserved verbatim. Detail lives in the `mcp/` package overview, the new `application/` route overview, and the file sidecars. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T11:40+02:00 — 260731-EFA-L4 curator (correction pass): **corrected three passages this
  same leaf wrote and this same leaf then falsified.** The 00:50 entry below correctly found that
  nothing outside the locally-installed `.githooks/_gate.sh` checked the ten byte-identical skill
  copies or the four runtime asset targets, and recorded it in the `Canonical runtime and skills
  asset sync` capability row, in the `260731-EFA-L4 Repository Impact` section, and in that entry
  itself. **The gap was then closed later in the same leaf and all three passages were left stating
  the old world.** Re-derived from `mcp/tests/test_sync_scripts.py` rather than from the review lead:
  a new `RealTreeDriftTests` class holds
  `test_every_skill_copy_matches_the_canonical_tree`, which iterates all **nine**
  `sync-skills.TARGETS` (mcp package data + eight harness roots in `scripts/sync-skills.py`),
  and `test_every_runtime_package_asset_matches_its_source`, which iterates all **four**
  `sync-runtime.TARGETS`; both read through one module-level `drifted_files()` helper over
  each script's `diff_target`, rebasing each entry onto its target so a failure names the copy to
  repair, and both assert against `[]` with the repair command in the message. It is a plain
  `unittest` class under `mcp/tests/`, which `[tool.pytest.ini_options] testpaths` declares as the
  suite root, so it runs in the quality wrapper's pytest step — `.githooks/pre-push` (`_gate.sh full`),
  worktree closeout, and `.github/workflows/quality-checks.yml`'s
  `python -m agents_remember_test_support.code_quality.check`. **Kept both honest limits rather than trading one
  overclaim for another:** CI still never invokes `--check` (verified — the only `sync-*` string under
  `.github/workflows/` is a comment), so the enforcement is via pytest, not a workflow step; and there
  is **no completeness assertion on `sync-skills.TARGETS`**, so a tenth mirror added without
  registering it would pass (verified by grep across `mcp/tests/`) — unlike
  `test_sync_runtime.py::test_default_targets_only_write_to_mcp_package_data`, which pins
  the runtime label set to `{agents-md-files, benchmarks, providers, system}`. Also recorded that the
  six pre-existing `ReplaceTreeTests` temp-directory cases are **unchanged and not superseded** —
  they cover `replace_tree`'s crash-safe copy-then-swap contract, a different property — and rewrote
  the "that is the opposite of the harness trees" contrast, since `RealTreeDriftTests` is modelled on
  `test_sync_harness.py::test_every_generated_harness_file_matches_its_source` and the three sync
  scripts now behave alike. The 00:50 entry's own sentence is left as the record of what was true then,
  marked superseded and pointing here. Verification metadata untouched; closeout stamps it.

- 2026-08-01T00:50+02:00 — 260731-EFA-L4 curator. Eleven changed files have no closer governor
  (`.gitignore`, the canonical `c-12-closeout/SKILL.md` plus its eight per-harness mirrors, and
  `dashboard/e2e-production/cockpit.production.spec.ts`), and all of them are about the same three
  repository-level facts, now recorded in a new **260731-EFA-L4 Repository Impact** section.
  **(1) Closeout stages before it gates.** `worktrees/modules/closeout.py::_gate_staged_code` runs
  `git reset --mixed HEAD` then `git add -A` in the task worktree and hands the wrapper exactly the
  commit's content — because every rail of the gate reads the index while closeout commits with
  `add -A`, so a file the task *created* was previously committed unread with the gate green (leaf
  3's own `abc7cbcc` shipped four such files). Recorded that the staging is deliberately **not**
  rolled back on refusal (the checkout is disposable, and the index-copy machinery an earlier attempt
  used is removed rather than fixed — it could not survive `core.splitIndex` or `SIGTERM`), that the
  mixed reset is what makes a retry equal a first run, and the two gate-scoped refusals (git-dir vs
  git-common-dir, which `default_series_contract` violates; an unmerged index, which `add -A` would
  resolve to the conflict markers) with their ordering constraint. **Corrected three places that said
  closeout fails "without mutation"** — the accurate phrasing is now "without any **commit**", since
  the index write is a mutation that precedes the gate on purpose: the `Source quality tooling` and
  `Approval-gated closeout` inventory rows, the `Code Quality And Refactor Baseline` paragraph, and
  the `Worktree Support` paragraph. **(2) `.gitignore` gained `.dmypy.json` and `.mypy_cache/`** for
  that exact reason, verified from the diff and the inline comment: a tool dropping is now staged
  content rather than something ruff merely skips, and one reached this leaf's own first commit.
  **(3) The production E2E spec** now `satisfies`-checks its happy-path terminal payloads against the
  wire mirrors (which surfaced the absent `controlEndpoint`/`controlProtocol` and the conditionally
  spread `harness`/`controlState`) while its fault-injection payloads stay untyped on purpose.
  **Verified the nine `c-12-closeout/SKILL.md` copies are byte-identical after the edit** —
  `md5sum`/`cmp` over all nine plus the tenth package-data copy give one hash
  (`e7279e57604ea6c1871ff918cf713449`) and mode 644 throughout. **Corrected a false claim about how
  that identity is enforced**, in the `Canonical runtime and skills asset sync` inventory row and in
  the new section: the row said both `--check` forms "run in **both** hook tiers and in CI" and that
  both scripts are "covered by `mcp/tests/test_sync_*`". Neither half holds for skills or runtime
  assets — no workflow under `.github/workflows/` invokes `_gate.sh` or any `scripts/sync-*.py`, the
  quality wrapper does not either, and **as of this entry** `test_sync_scripts.py`/`test_sync_runtime.py`
  only exercised `replace_tree`/`diff_target` over temp fixtures rather than the real trees.
  Skill-mirror drift was therefore caught by the local hooks alone, unlike harness-tree drift, which
  `test_sync_harness.py::test_every_generated_harness_file_matches_its_source` reads off the real
  files and so fails in CI as well. **[Superseded later in this same leaf — see the 11:40 entry: the
  gap was closed by `test_sync_scripts.py::RealTreeDriftTests`, which reads the real skill and
  runtime trees in the pytest step, so the "hooks alone" conclusion no longer holds.]** Added four invariants, five evidence rows, and a paragraph stating the
  mirror boundary precisely: `snapshot.json` and the TypeScript mirrors are hand-maintained, **no
  generator exists**, fixture ⊆ mirror is enforced and mirror ⊆ server is enforced by nothing.
  **Citations:** re-checked the 13 range-bearing rows in `Cross-Repo References` and repaired the two stale ones — `tool_registry.py` `L1-L85` →
  **L108-L185** (the row names the response-model registry, and `TOOL_RESPONSE_MODELS` is at L111
  with `PUBLIC_TOOL_RESPONSE_MODELS` at L181, so the old range contained neither symbol; the file is
  185 lines) and the harness starter-instruction group citation `L1-L37`, which was out of bounds for
  nine of its ten files (12-18 lines each) and is now stated as whole-file. Verification metadata
  pinned until closeout stamps the commit.

- 2026-07-31T22:12+02:00 — 260731-EFA-L3 curator (re-verification pass after the fix workers):
  **corrected the `.gitattributes` `-text` claim, which was false.** It said tiktoken verifies the
  vocabulary's SHA-256 on load and re-downloads any copy whose bytes differ, so an autocrlf clone
  would "restore the cold-start download on those clones alone". Read against the current code:
  `models/tokens.py::_verify_vendored_vocabulary` hashes the file against
  `VENDORED_VOCABULARY_SHA256` itself and raises `TokenizerVocabularyError` — such a clone
  cannot start the server at all, and nothing is re-downloaded. Recorded why the check moved into
  this package (`tiktoken.load.read_file_cached` verifies but does not fail closed: it deletes the
  file and downloads a replacement over it, which inside an installed package is a startup fetch
  plus a rewrite of the installed tree, or a `PermissionError` on a read-only install), and that the
  entry is a **literal filename** — `.gitattributes` L13 names
  `package_data/tiktoken/fb374d419588a4632f3f557e76b4b70aebbca790`, so a refresh renames both and
  `test_cold_start.py::test_the_gitattributes_entry_names_the_shipped_file` holds them
  together. `.gitattributes` carries its own corrected comment for the same reason. Also
  made the cold-start hot-path sentence say *absent or byte-wrong* rather than only absent, and
  added the invariant that a downstream integrity check which repairs itself is not a check. The
  `blank-at-eol` half of the paragraph and the one-git-runner half were re-read and are unchanged.
  Verification metadata pinned until closeout stamps the code commit.

- 2026-07-31T21:05+02:00 — 260731-EFA-L3 curator: recorded the leaf's two repository-wide runtime
  facts and corrected the one root claim it falsified. Added a **Runtime integrity** hot-path
  paragraph (the server starts with no network egress now that the `o200k_base` vocabulary is
  vendored rather than downloaded at import; six drifted private git runners consolidated onto
  `kernel/git_command.py::run_git`, only one of which had scrubbed the `GIT_DIR`-family selectors
  while the unguarded one sat behind `reset --hard` / `branch -D` / `worktree remove --force` /
  `push origin --delete`), and extended the MCP-server feature row with the cold-start property.
  **Corrected the `.gitattributes` note**, which said the file's only rule was the inert
  `blank-at-eol` exception over a git-ignored path: it now has a second rule, and that one has a
  tracked subject — the vendored vocabulary is marked `-text` because a `core.autocrlf=true` clone
  would otherwise break the checksum tiktoken verifies and restore the download on those clones
  alone. Added two durable invariants (a guard that lives in one copy of a duplicated function is
  not a guard; nothing on the import path may reach the network, and a mitigation that lives in
  `conftest.py` can hide the defect it mitigates). Detail stays in the `mcp/` and `mcp/tests/`
  route overviews.
  Verification metadata pinned until closeout stamps the code commit.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator (final state). **Retired every mid-leaf claim that
  rested on the complexity baseline, which the developer's no-deferral ruling deleted**: the
  Source-quality feature row's five-step list and threshold of 30, contract 1's shrink-only ratchet
  with a 2026-10-31 burn-down, contract 4's "CRAP is statement-based until that reader is moved",
  contract 5's shrink-only allowlists in `test_gate_scope.py` (all three were empty and were
  deleted outright), the "two things deliberately not changed with named owners" paragraph
  (`PLR0913` and the CRAP threshold were both paid instead), the fast tier's complexity-baseline
  step, and the "prefer a ratchet with an owner" lesson — which is now the opposite rule. Added the
  seventh contract: the 100% changed-lines coverage floor in `diff_coverage.py`, with the evidence
  that rules out 80/85/90/95. Recorded CRAP at 20.0 against branch coverage with a report lacking
  branch data refused, `PLR0913` armed at 5 args with the single AST-guarded tool-signature
  carve-out, the eight now-applied integration markers with their CI and local runners, and CI's
  load-bearing `fetch-depth: 0`. Verification metadata pinned to the leaf's reformat commit until
  closeout stamps the code commit.

- 2026-07-31T06:30+02:00 — 260731-EFA-L2 curator (mid-leaf): recorded gate honesty as six durable contracts
  in the Hot Path Summary (baselined complexity rules, Radon reports but is CRAP's engine, branch
  coverage with its honest caveat, `git ls-files`-derived scope, and the nine generated harness
  trees), plus the two deliberately-open items with named owners (`PLR0913`, the CRAP threshold).
  **Retired falsified claims:** the Source-quality feature row's "wrapper for Ruff, Radon, pytest
  coverage, and CRAP"; "the current `pyproject.toml` makes … Radon responsible for complexity
  scouting" and its "better reviewed through Radon" ignore rationale; "run Ruff, Pyright, and
  Radon after Python implementation work" in both the prose and the lessons list; the lesson
  "Radon owns complexity scouting"; and the fast-tier step list, which now includes the formatter,
  the complexity baseline, the harness generated-copy check, and its own `git ls-files` derivation.
  Added a Self-hosted harness configuration feature row and four new lessons (unselected limits,
  ratchets with owners, deferral to non-enforcing tools, derive-never-enumerate scope).
  Verification metadata pinned to the leaf's reformat commit until closeout stamps the code commit.

- 2026-07-31T04:28+02:00 — 260731-EFA-L1 curator: refreshed the repository spine for the
  enforcement-first leaf. Recorded the enforcement topology as the durable home for the
  pathRules-disabled hooks and workflows: the shared `.githooks/_gate.sh` in a fast staged-content
  tier and a full pre-push tier, CI on every branch and pull request with the frontend rail
  required by the ruleset, `publish-mcp-to-pypi.yml` gated on `quality-checks.yml` through
  `workflow_call`, and the closeout gate applying to any checkout that carries the wrapper rather
  than to one repository name. Recorded that the cockpit bundle and its fingerprint sidecar left
  version control (master decision OQ6) and are built at release. Corrected the falsified claims
  in place: the Source-quality feature row, the dashboard-sync feature row (split into an asset-sync
  row and a release-build row), the wrapper-enforcement paragraph, the Dashboard Serving Layer
  paragraph, the `--check` parity statements in the FEUI-MX-FIX-2 / HFX2-L16 / HFX2-L17 summaries,
  the `.gitattributes` hot-path note (now an inert rule over an untracked path), and the
  pre-commit citation row. Verification metadata remains pinned until closeout.

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: updated the repository
  onboarding spine for the active-projector package split, runtime-probed bounded Codex history,
  child-local failure containment, explicit projection-domain invalidation, and per-file task
  document parse reuse. Detailed ownership remains in the MCP, observer, serving/conversation,
  and dashboard route overviews. Verification metadata remains pinned until closeout.

- 2026-07-24T14:31Z — 260718-CHATS-L5I incremental CRAP/commit-gate curation:
  recorded the mandatory default CRAP threshold and four enforcement seams,
  corrected closeout ordering to quality-before-mutation, and documented the
  pathRules boundary for disabled generated/public surfaces. Verification metadata
  and entity fingerprints remain pre-commit.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the root behavioral inventory for the combined frontend/backend interactive-session delta. Verification metadata remains pre-commit.

- 2026-07-21T12:00+02:00 — No route impact: reviewed 260718-CHATS-L5P (cockpit chrome visual polish,
  PASS-WITH-NOTES) against the repo body. Dashboard-only, zero backend edits: it closes the developer
  visual-findings file + the FB7 terminal-identity directive against the composed app (the terminal well
  + gutter grammar, the responsive rail-row grammar, collapse-or-explain chrome, humanized durations, and
  the load-bearing `@webtui/css` `word-break: break-all` root-override lesson). No repo-level feature
  inventory changed — detail routes to the `dashboard/src/`, `dashboard/src/panels/`, `.../session-cockpit/`,
  `.../session-cockpit/conversation/`, and `dashboard/src/data/conversation/` governors; the regenerated
  `package_data/dashboard/` bundle is shipped output under the `mcp/` overview's sync mechanism.
  Verification metadata unchanged.
- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: corrected the CHATS-L1 narrative's now-false
  "claude `unverified` at the installed-vs-locked version mismatch" to the never-probed contract reason
  — 260718-CHATS-L5F R4 (developer ruling 2026-07-21) removed all capability version gating (THE
  CONTRACT IS THE ONLY GATE). The half-time functional fixes (R1 codex notification identity, R2 claude
  acceptance, R3 claude 2.1.216 frame contracts, R4 version-gate removal, R5 per-session bounds/release,
  R6 exit-note + metrics timeout, R7 durable `dashboard/e2e-chats/` suite) are detailed in the `serving/`,
  `serving/conversation/*`, `mcp/`, `mcp/tests/`, and `dashboard/` overviews. Verification stays pinned
  until L5F closeout stamps the candidate commit.
- 2026-07-21T11:00+02:00 — No route impact: reviewed the 260718-CHATS-L5 production-E2E gate plus
  bounded hardening (the terminal-liveness per-row synchronizer quarantine, the conversation
  projection-store input-authority pin, the projector's disjoint-id-namespace twin suppression, and
  new/extended regression suites incl. the installed F1 real-wire regression and the 10k renderer
  tripwire) against the repo body. No repo-level feature inventory changed — L5 hardens the
  already-landed structured Chats surfaces against their proven production faults rather than
  adding a product surface; detail routes to the `serving/`, `conversation/`, `conversation/active/`,
  `conversation/projectors/`, `mcp/tests/`, and `dashboard/…/session-cockpit/conversation/` governors.
  Master-exit carries recorded by the reviewer: the F3 completion-correlation disposition, the L3.7
  IPC-flake investigation, and the R5.1 ≥12-session real-browser residual. Verification metadata
  unchanged.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: added the ancestor-routing narrative paragraph
  for the landed structured Chats renderer (reviewer FINAL PASS, 26/26 closed) and amended the stale
  260715-FEUI-L8 feature-inventory clause — controlled sessions no longer expose the runner line-log
  as the primary body; the structured `ConversationSurface` over two reconstructable browser
  projections is the controlled default, the interrupt rides the WorkingLine `conversation.stop`
  chord, and the read-only PTY is a default-off diagnostics drawer. Detail routes to the new
  `dashboard/src/data/{conversation,conversation-library}/` and
  `dashboard/src/panels/session-cockpit/{conversation,conversation-library}/` overviews (which carry
  the L5-Facing Register). No backend/MCP source changed — the `package_data/dashboard/` bundle is
  regenerated output. Verification metadata stays pinned to the L3 tip (`0be0099`) until L4 closeout
  stamps the candidate commit.
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: reviewed the root body against the leaf diff and
  added the ancestor-routing paragraph for the implemented authoritative control API (seventeen
  routes — interrupt, source-aware queue with cockpit-only withdrawal recovery, typed attachments,
  read-only policy, evidence-bound telemetry — over the closed L2E/L3E substrate); detail routes to
  the new `conversation/control/overview.md` and the `serving/`, `mcp/`, and `mcp/tests/` governors,
  and no feature-inventory surface changed. Verification metadata stays pinned until L3 closeout
  stamps the candidate commit.
- 2026-07-20T00:08+02:00 — 260718-CHATS-L2E curator: reviewed the root body against the leaf diff
  and added the ancestor-routing paragraph for the additive native control-plane substrate
  (interrupt write, paged never-bodies timeline, digest-verified asset channel, once-only
  withdrawal recovery); detail routes to the `serving/`, `mcp/`, and `mcp/tests/` governors and no
  feature-inventory surface changed. Verification metadata remains pinned until closeout stamps
  the candidate commit.
- 2026-07-19T18:25+02:00 — 260718-CHATS-L1 curator (memory rebase): union-merged the landed L2
  ancestor routing with the L1 active-serving routing after the master memory branch advanced;
  both implemented slices are routed at repository level — detail to the `serving/`,
  `conversation/`, `conversation/active/`, `conversation/projectors/`, `conversation/library/`,
  `native_helpers/conversation_library/`, `mcp/`, and `mcp/tests/` governors. No
  feature-inventory surface changed. Verification metadata remains pinned until L1 closeout
  stamps the candidate commit.
- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: reviewed the root body against the leaf diff
  and added the repository-level ancestor routing for the implemented active conversation
  serving — the two authorized routes, signed cursor authority, bounded projectors over native
  authority, the canonical status service single-sourcing Chats and orchestration, and the pure
  per-harness mapper grammars — with detail routed to the `serving/`, `conversation/`,
  `conversation/active/`, `conversation/projectors/`, `mcp/`, and `mcp/tests/` governors. No
  feature-inventory surface changed. Verification metadata remains pinned until closeout stamps
  the candidate commit.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: reviewed the root body against the leaf diff
  and added the repository-level ancestor routing for the implemented native conversation
  library — authorized list/read routes, live capability gates, the per-app signed token
  authority, and the idempotent exact open with honest retirement — with detail routed to the
  `serving/`, `conversation/`, `conversation/library/`, `native_helpers/conversation_library/`,
  `mcp/`, and `mcp/tests/` governors. No feature-inventory surface changed. Verification metadata
  remains pinned until closeout stamps the candidate commit.
- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: reviewed the root body against the leaf diff
  and added the repository-level ancestor routing for the native evidence and resume substrate —
  reserved-key evidence diversion with byte-identical projections, the three additive epoch-scoped
  private-socket reads, and the codex-only resume channel — with detail routed to the `serving/`,
  `mcp/`, and `mcp/tests/` governors. No feature-inventory surface changed. Verification metadata
  remains pinned until closeout stamps the candidate commit.
- 2026-07-19T00:37+02:00 — 260718-CHATS-L0 curator: reviewed the root body against the leaf diff
  and added the repository-level ancestor routing for the conversation runtime composition repair
  — install-once immutable runtime plus server-resolved local-operator ruling under the existing
  harness-control registration, with detail routed to the `mcp/`, `serving/`, `conversation/`, and
  `mcp/tests/` governors. No feature-inventory surface changed. Verification metadata remains
  pinned until closeout stamps the candidate commit.
- 2026-07-18T21:05+02:00 — FEUI-MX-FIX-5 root route impact: documented Vite as the semantic
  generated-byte owner, raw sync as the byte-equality boundary, the rejection of generic EOL
  normalization, and the root attribute's direct shipped-JavaScript-only `blank-at-eol` exception.
  Recorded retained authored/near-miss whitespace checks plus two clean byte/fingerprint-identical
  build/sync passes; generated assets remain excluded from file-level onboarding.
- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4 route impact: route indexes now derive source identity and eligibility from one deterministic Git/path-rule census; callers pass resolved repository/storage authority explicitly, and official-memory carryover refuses missing or semantically empty write authority before mutation.
- 2026-07-18T15:22+02:00 — FEUI-MX-FIX-2 ancestor route repair: added the repository-level sole
  browser open authority and zero-ghost accepted-row invariant, while retaining synchronized
  package dashboard files as generated output rather than a second implementation source.
  Verification metadata remains pinned pending candidate closeout.

- 2026-07-18T13:04+02:00 — 260715-FEUI-L9R ancestor route repair: added the repository-level
  dashboard/serving routing boundary for browser build identity and recovery, pre-session harness
  discovery, raw-event record handling, HTML revalidation, and tmux client identity. Detailed
  client behavior stays under `dashboard/src/`; server behavior and proof stay under
  `mcp/src/agents_remember/serving/` and `mcp/tests/`; synchronized dashboard package data remains
  generated output rather than a competing source authority.
- 2026-07-18T07:43+02:00 — 260715-FEUI-L8 route impact: added the repository-level canonical Chats
  cockpit feature and its root `dashboard/` test/config boundary. One Chats destination now owns the
  session cockpit, Operations remains default, RailChat remains contextual, and the toggleable inspector
  defaults closed. The expanded Playwright/performance configuration is a regression gate for that product
  contract; it does not fill the explicitly absent UA-1 structured transcript/history authority. Detailed
  component/data routing stays in the new strategic dashboard overviews and design evidence set.
- 2026-07-18T00:08+02:00 — 260715-FEUI-L7 curator closeout delta: added the repository-level
  Sessions inspector/status integration inventory for stable-mounted accessible tabs, the complete
  post-removal evidence audit, separated exact-session capability authority, fleet-global pending
  Bus reply semantics and 100/101 virtualization boundary, and the honest contractual StatusLine.
  Detailed component routing remains in the `dashboard/src/panels/session-cockpit/` overview.
- 2026-07-17T21:39+02:00 — 260715-FEUI-L5 curator: added the repository-level reliable submission
  feature, end-to-end hot path, and sole-authority invariant covering epoch/idempotency, guarded
  dispatch/withdrawal, full refs, raw-free bounded status, no-resend reconciliation, and revision-
  safe pop-back.
- 2026-07-17T08:33+02:00 — 260715-FEUI-L4 curator: added the repository inventory entry for
  exact-session model/effort controls, the five-state evidence/readback contract, serialized pair
  changes, shared worded outcomes, ledger/rail/toast attention, cycle-effort, and live regions.
  Final reviewer verdict is PASS after three fix rounds; six nonblocking sev-4 observations remain
  preserved on the governing file cards. No MCP/package-data route was refreshed because the
  dashboard bundle was not synced. Verification metadata is pinned to the contract base until the
  code commit exists.
- 2026-07-17T06:35+02:00 — 260715-FEUI-L3 curator: refreshed the dashboard-frontend inventory row
  for the sessions cockpit's capability-catalog/launch-flow slice — the memory-only dynamic-only
  capability-envelope store with verbatim error honesty, the pure launch machines
  (both-knobs-or-neither selection, uniform fail-loud response paths), the launch-evidence tier
  machine + five-glyph EvidenceBadge, the capability/open wire mirrors, the R3 contract fixture
  pack + conformance suite, and the LaunchFlow/FailedLaunchBanner cockpit surfaces (review FINAL
  PASS after two fix rounds; upstream ask: an operator retire actor identity for
  provenance-recording retires). Repo-level routing, feature surfaces, and architecture are
  otherwise unchanged by this frontend-only leaf; detail lives in the `dashboard/src/` route
  overviews and the touched sidecars. Verification metadata remains pinned until closeout stamps
  the L3 code commit.
- 2026-07-17T04:20+02:00 — 260715-FEUI-L6 curator: extended the dashboard-frontend inventory row
  for the cockpit's PTY-stage/interaction/lifecycle slice — keep-alive real xterm panes with the
  measured DOM-renderer decision (webgl kept as a lazy escalation path; two xterm addons
  exact-pinned), the two server-truth pane archetypes with legacy-raw-only observe-only
  harvesting, the gate-channel-only structured-interaction answer path, the WorkingLine turn
  theater, honest terminate flows with verbatim failures and informational, never-dropped stop
  residuals (retire stays agent-side; the cockpit renders it), and the accessibility layer
  (screen-reader opt-in, always-named terminal landmarks) (review FINAL PASS; 1 sev-3 + 5 sev-4
  all CLOSED in fix round 1). Repo-level routing, feature surfaces, and architecture are
  otherwise unchanged by this frontend-only leaf; detail lives in the `dashboard/src/` route
  overviews and the touched sidecars. Two upstream asks recorded for the developer: a
  gate-id-only projection surface for interactions on lifecycle-less seats, and an actor-seat
  path if an operator retire UI is ever required. Verification metadata remains pinned until
  closeout stamps the L6 code commit.
- 2026-07-17T02:30+02:00 — 260715-FEUI-L2 curator: refreshed the dashboard-frontend inventory row
  for the sessions cockpit's data-layer/rail/stage slice — the hoisted shared catalog poll driver,
  the gated seat-event pre-apply layer over the existing events channel, the full catalog wire
  mirror, the honesty-invariant cockpit client store, the single seat-state dot grammar with the
  ruled 2.4 s pulse, and the ruled role-driven rail + stage HeaderStrip/inspector card (review
  FINAL PASS; one open sev-3 chip-vocabulary ruling). Repo-level routing, feature surfaces, and
  architecture are otherwise unchanged by this frontend-only leaf; detail lives in the
  `dashboard/src/` route overviews and the touched sidecars. Verification metadata remains pinned
  until closeout stamps the L2 code commit.
- 2026-07-17T00:45+02:00 — 260715-FEUI-L1 curator: refreshed the dashboard-frontend inventory row
  for the sessions-cockpit view slice — the keep-alive full-bleed Sessions view
  (`panels/session-cockpit/`), the pure keyboard/command/layout data modules
  (`data/keymap/`, `data/commands.ts`, `data/sessionLayout.ts`), and the adopted scoped WebTUI skin
  (`styles/webtui.css`, the `webtui` cascade layer, exact pins, spike assertions). Repo-level
  routing, feature surfaces, and architecture are otherwise unchanged by this frontend-only leaf;
  detail lives in the `dashboard/src/` route overviews and the touched sidecars. Verification
  metadata remains pinned until closeout stamps the L1 code commit.
- 2026-07-16T06:26+02:00 — 260714-ACPUI-L4 curator: added the frozen daemon capability/control
  boundary, bounded install-aware advertise cache with failed-refresh quarantine, complete-pair
  launch carriage, truthful live reopen, exact-session set/submit/reconcile, first-byte ambiguity,
  idempotent request correlation, raw-free public responses, and liveness-first status ordering.
  Preserved settings-owned role spawn and the durable inter-agent inbox/brief bus. Verification
  metadata remains pinned until closeout stamps the L4 code commit.
- 2026-07-16T01:34+02:00 — 260714-ACPUI-L3 curator: completed the root own-adapter capability
  contract with queue-ordered same-session setters, exact five-value `SetResult` truth, truthful
  Claude/Codex/Pi acceptance semantics, the no-paste boundary, and the current dynamic Fable
  correction. Preserved settings-owned role spawn and the durable inter-agent inbox/brief bus;
  daemon capability/request exposure remains L4. Verification metadata remains pinned until
  closeout stamps the L3 code commit.
- 2026-07-15T23:31+02:00 — 260714-ACPUI-L2 closeout-preview delta: refreshed the root dispatch
  feature and hot path for complete settings-owned role selection, dynamic model-local catalogs,
  native Claude/Codex/Pi launch channels, honest failed/rejected evidence, and the preserved durable
  inbox/brief bus. Removed the superseded claim that normalized model/effort is session-command
  injection; L3 mutation and L4 daemon exposure remain future boundaries.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: refreshed the root route body for the
  negotiated harness contract, bounded rolling inbox compatibility, and deferred R10 boundary.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed route impact for the accepted hosted cutover.
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: recorded the repository-level routing impact of
  the new unregistered Pi RPC protocol slice; detailed behavior remains in the serving and tests
  route overviews and nine file sidecars. Verification metadata remains pinned until closeout.

- 2026-07-12T13:36+02:00 — No route impact: 260712-TRH-L2 body review confirms the changeset and dashboard reader refinements are fully documented in their existing child routes; the repository-level onboarding route model is unchanged. Verification metadata remains pinned until closeout.
- 2026-07-12T12:28+02:00 — 260712-TRH-L1 root route impact: documented body-first complete task
  hydration, delayed ancillary reader requests, honest loading/fallback state, revision caching, and
  the unchanged source-to-package dashboard boundary. The public release pin advances to rc5.

- 2026-07-10T22:18+02:00 — 260707-HFX2-L20 root route impact: recorded monotonic consumed inbox
  state across concurrent hosted delivery; public communication surfaces remain unchanged.

- 2026-07-10T21:59+02:00 — 260707-HFX2-L21 root route impact: recorded the adjustable Chats
  sidebar on the existing Dashboard frontend surface. The change is frontend-local; the MCP route
  only receives the verified generated bundle and fingerprint.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17 root route impact: documented current
  `(leafKey, seatRole)` identity, provenance/binding separation, multi-role coexistence, explicit
  hand-opened role claim, and the source/build/serve package boundary. Clarified that per-role
  one-leaf/one-session lifecycle prose is role-local, not global uniqueness. Verification metadata
  remains pinned until closeout stamps L17.

- 2026-07-10T13:41+02:00 — 260707-HFX2-L16 root route impact: recorded the sprint-local chat rail,
  honest task-reader fallback/single-step behavior, and final L15+L16 source-to-package proof. The
  generated dashboard asset route stays excluded from file-level onboarding; sync/static boundary
  docs carry the release-significant evidence. Verification metadata stays pinned until closeout.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15 root route impact: added the log-backed dispatch,
  duplicate-safe retry, settings-pinned knob provenance, replacement-leaf chain credit, and one-row
  supervisor redelivery contract. Verification metadata remains pinned until closeout stamps the
  eventual L15 code commit.

- 2026-07-10T02:39+02:00 — HFX3/L14 combined root impact: reconciled the lifecycle entity,
  root hot-path summary, and harness-starter description with the free-chat launcher,
  developer-approved strategist pass plus sanctioned-skip authoring, architect terminal custody,
  and dependency-graph parallel-by-default rule. Kept canonical and excluded generated mirror
  boundaries explicit. Verification metadata remains pinned until closeout stamps the eventual
  two-parent code commit.

- 2026-07-10T01:27+02:00 — 260707-HFX2-L13 closeout-follow-up root route impact: replaced the
  former future-residual routing note with current end-to-end L13 behavior across MCP observer,
  serving, control-plane, tests, and dashboard routes. Recorded live virtual-cursor compaction,
  heartbeat coalescing/reclamation, bounded task summaries plus on-demand bodies, manager-first wake,
  chain-aware suppression, and rung pacing; preserved S1 as HFX2-L14 S7 and the separate HFX3 retro
  gate. Verification metadata remains pinned until closeout stamps the eventual L13 code commit.

- 2026-07-09T19:41+02:00 — 260707-HFX2-L12 root route impact: refreshed the root runtime-scaling
  story for the store-scaling and reclamation audit. The overview now routes HFX2-L12's bounded
  supervisor signal/expectation stores, startup Event River compaction, projection/task-document hot
  path bounds, terminal catalog/liveness batching, and provider metric/degradation log compaction to
  the already-updated `mcp/`, `controlplane/`, `observer/`, `serving/`, and provider route sidecars.
  It also records the explicit residual boundary for HFX2-L13: live Event River compaction, full
  task-document body windowing/on-demand retrieval, and heartbeat coalescing. Verification metadata
  pinned until closeout stamps the 260707-HFX2-L12 commit.
- 2026-07-09T14:05+02:00 — 260707-HFX2-L11 root route impact: reverses the prior (260707_hotfix-
  orchestration-stack HFX-L8) auto-retire-on-success completion edge — successful worker/reviewer/
  manager seat completion now lands the seat (inspectable, non-terminated) instead of retiring it;
  manual explicit retire and its authority policy are unchanged. Ruled design constraint 10 records
  this reversal at the master level. Per-file/route detail lives in the already-updated `mcp/`,
  `dashboard/src/`, and `dashboard/src/panels/` sub-route overviews and file sidecars. Verification
  metadata pinned until closeout stamps the 260707-HFX2-L11 commit.
- 2026-07-09T12:04+02:00 — 260707-HFX2-L10 root route impact: refreshed the Agent-facing session
  dispatch inventory row so spawned-seat spend is settings-resolved and caller spend overrides refuse
  before side effects with `spend-override-unsupported`. Detailed behavior remains under the `mcp/`
  and `mcp/tools/` route overviews plus the terminal/test/doc sidecars. Verification metadata pinned
  until closeout stamps the 260707-HFX2-L10 commit.

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

- 2026-07-08T23:59+02:00 — No route impact: reviewed the repo overview as the nearest governing
  overview for `docs/reference/settings-json.md` (the `docs/reference` route has no local overview).
  The source doc gained the already-route-local `orchestration.supervisor.redeliverBudget` table row
  for HFX2-L8; this does not change the root feature inventory or routing model. A file-level sidecar
  now covers the settings reference directly. Verification metadata pinned until closeout stamps the
  260707-HFX2-L8 commit.

- 2026-07-08T15:45+02:00 — No route impact: 260707-HFX2-L7 release tail bumps README/package
  version strings to 3.0.0rc4, refines the l-01 Developer Clarification Triage wording to classify
  note-only vs immediate implementation from the active queue/current diff fit, and fixes the
  supervisor redelivery-vs-escalation boundary. The root overview's feature inventory remains
  accurate at this altitude; detail lives in the `mcp/` and `serving/` route overviews plus the
  touched file sidecars.
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
  lifecycle next-step engine ([next_step.py](agents-remember/mcp/src/agents_remember/application/next_step.py)) —
  a `blocked` lifecycle now hints `lifecycle_resume`, carrying the chain through the open gate. The
  feature is already in this root inventory and the repo route model is unchanged (detail in the file
  sidecar). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T18:43+02:00 — Tasks 26+27 root route impact: surfaced two new features in the feature
  inventory. **Task 27** adds the **lifecycle next-step hint engine**
  ([next_step.py](agents-remember/mcp/src/agents_remember/application/next_step.py)) — every MCP tool
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

## Historical milestone context: 260821-DAGQC-L4 Doctrine And Review Closure

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

Review inventory is NUL-safe and treats every untracked entry as hostile filesystem evidence:
inspect no-follow type, mode, bounded content eligibility, explicit disposition, and race limits
instead of silently following or omitting it. Planning has one effective candidate priority
(candidate override, otherwise master default), while the orchestrator still compares the
portfolio. Graph-less atomic-sequential is a valid ruled topology; strategist skip transfers the
full reasoning duty, and graph adoption from graph-less attaches every master before one complete
nodes-plus-evidence-edges publication batch.

Handover points receivers at the canonical candidate, code ancestry, memory ancestry, and per-leaf
ledger references so they revalidate instead of trusting copied maps. Existing `add_edge` examples
already carried `judgmentId`; no fabricated fix, lifecycle evidence, fake nonce, bypass, shadow
configuration, fallback, or compatibility route was added. Delegated-authority redesign,
disabled-memory behavior, mandatory-graph runtime, and declared-caller trust redesign remain out
of scope.

## Build And Development Reference

Ordinary Python development is supported directly through `mcp/.venv/bin/python -m pytest`; four workers run the isolated unit population. `-m integration` selects the small real-boundary population and `-m ""` selects both. Focused file/node execution, including serial debugging, is valid development work and does not acquire certification authority. The repository declares budgets of 1,000 unit and 150 integration parametrized collected cases. Extend or consolidate distinct behavior protection before adding cases; do not restore deleted matrices, private-branch tests or unused fixture machinery because an old milestone names them.

Coverage, including changed-line coverage, is diagnostic only. No percentage floor requires additional tests. Production-only CRAP retains 20 as a review trigger, not a delivery blocker; tests and verification support are excluded. Lint, formatting, typing, structural rules and test failures still enforce. Diagnostic-tool execution errors remain visible failures distinct from metric findings. There is no coverage baseline, score-exception registry or ratchet.

Only genuine Dagger admission and the existing lifecycle owners can issue immutable candidate-bound certifying evidence. A host pytest pass, copied report, green helper result or use of Dagger alone is insufficient. Reuse the existing shared engine and preserve process identity, disposable state, credential isolation, exact candidate and publication ownership. Full-suite execution and whole-master independent review belong to the master aggregation boundary under the current execution policy; this overview does not impose either on every leaf. Focused development evidence remains useful without pretending to be final acceptance.

## Repo-Internal References

These current source and policy ranges establish the development/certification distinction and the existing memory preparation surfaces. A citation is source evidence, not a recorded test execution.

| Finding | Anchor | Source |
| --- | --- | --- |
| Development commands, budgets, diagnostic metrics and isolation. | `# Python test policy and commands` | docs/design/python-pytest-bootstrap.md:1-50 |
| Certifying publication and accepting consumers. | `# Python Test Evidence Authority` | docs/design/python-test-evidence.md:1-65 |
| Exact contract scope, full check and curator worklist publication. | `_resolve_execution`; `_execute_memory_quality`; `_attach_curator_checklist` | mcp/src/agents_remember/application/memory_quality/controller.py:295-441 |
| Interactive catalog names missing authority without eligibility. | `_attach_final_full_catalog` | mcp/src/agents_remember/application/memory_quality/controller.py:444-480 |
| Final memory adapter requires the selected four-code-terminal prefix. | `PreparedMemoryCertificationAdapter` | mcp/src/agents_remember/memory_quality/prepared_certification.py:396-437 |
| Finalization consumes original selected fifth-certificate inputs. | `PreparedCloseoutContinuation` | mcp/src/agents_remember/worktrees/integration/closeout/preparation/continuation.py:18-45 |

## Key Invariants

- Controlled prompt delivery has one epoch-bound authority. Request identity/payload is immutable;
  only certified pre-dispatch failure retries; full operation refs complete work; pop-back is an
  atomic server withdrawal of an explicit queued row; PTY paste and adapter/native queues are never
  fallback authority.

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
- Route indexes are generated availability metadata, not hand-authored truth; overview `## Hot Path Summary` sections and file sidecars are the maintained inputs, and `c-04-retrieval-strategy-router` skill should infer missing sidecars from `sourceScope` plus `coveredFiles`. One validated Git snapshot supplies both repository membership and path-rule eligibility so counts, coverage, and generated bytes cannot observe different filesystem moments; carryover requires explicit official-memory storage authority rather than parser defaults before it may refresh indexes.
- Generated dashboard JavaScript may contain runtime-significant whitespace-only lines. Preserve the
  Vite bytes through raw package sync; only direct shipped `assets/*.js` disable `blank-at-eol`, while
  authored source, generated near misses, and all other whitespace diagnostics remain strict.
- Repo entity catalogs use deterministic `git-blob-set-v1` fingerprints over curated load-bearing evidence files so `c-02-memory-quality-control` skill can flag stale entity memory without semantic guessing.
- The package-owned runtime `AGENTS.md` template set is currently `coordinator`, `skills`, `system`, and `tasks`; memory repos use `system/*` files rather than a root-level `AGENTS.md`.
- Runtime, provider, benchmark, route-index, memory quality, memory, worktree, and skill-install behavior belongs in MCP package modules. Repository `scripts/` still owns build, synchronization and clean-room verification tooling; it is not a competing installed runtime.
- **Ruff owns complexity enforcement as well as hygiene; Radon only scouts.** (Superseded 2026-07-31 by 260731-EFA-L2: this line used to say Radon owned complexity scouting, which was read as a reason to ignore three Ruff complexity rules — deferring enforcement to a tool that exits 0 whatever it finds.) `C901`, `PLR0911`, `PLR0912`, `PLR0915` and `PLR0913` are enforced by `ruff` directly with no baseline behind them; Radon's findings feed refactor planning and must never be recorded as a pass.
- **A configured limit whose rule is unselected is not a limit, and a rule ignored in deference to a tool that cannot enforce is not delegation.** Both patterns were individually invisible and collectively hollowed out this gate. When a suppression cites another tool, check that the other tool can fail.
- **Ratchets, baselines, grandfather lists and burn-down schedules are forbidden in this repository's gates — fix the finding instead.** (Developer ruling, 2026-07-31, overruling this leaf's own plan.) 260731-EFA-L2 built the well-shaped version of that idea — a `quality/complexity-baseline.txt` failing in *both* directions, with an auto-tightening cap, a named owner and a dated burn-down — and then deleted it along with three empty allowlists in `test_gate_scope.py`. The reasoning is that **an exemption list, even an empty one, is a place to put the next offender**; all 67 complexity findings, 274 of 293 long signatures and all 46 CRAP offenders were paid instead. The one surviving carve-out (`PLR0913` on published MCP tool signatures) is a category the coding standard already exempts, is scoped by path rather than by entry, and is held shut by an AST test that fails if it widens.
- Test case budgets are explicit and bounded; growth needs a distinct-protection and runtime tradeoff. Coverage percentages impose no acceptance floor.

- **Derive scope from the tree, never enumerate it.** Every hand-written scope constant in this repository had fallen behind: the wrapper's, the pre-commit hook's, and Pyright's `include`, each silently narrower than the last. `git ls-files` plus a test that asserts the *real* argument vectors reach every tracked path is what makes "the gate covers everything" a fact rather than an intention.
- **A safety guard that lives in one copy of a duplicated function is not a guard.** Six copies of the git runner drifted apart and only one scrubbed the `GIT_DIR`-family repository selectors, which is why every `git` subprocess in the package now goes through `kernel/git_command.py::run_git` and an AST sweep fails the suite if a second spawner appears (260731-EFA-L3). Wrapping the one runner is fine; re-implementing it is not.
- **Nothing on the server's import path may reach the network, and a mitigation must not live only in the test harness.** The tool surface is imported while the MCP handshake is starting, so an import-time download is a startup dependency on egress; the `o200k_base` vocabulary is vendored and a missing one raises instead of downloading. The same rule applies to test scaffolding: `conftest.py` stripped the git selectors at import, which made the production defect *undetectable by any test*, so the redirection tests re-set them inside their own scope on purpose.
- **A gate must be shown the content that will be committed, not the content that happens to be
  tracked.** Every rail of the quality wrapper reads the git index, and closeout commits with
  `git add -A`, so until closeout staged first, a file the task *created* was committed unread while
  the gate reported green (260731-EFA-L4; leaf 3's `abc7cbcc` shipped four such files). The same
  asymmetry runs the other way: an unstaged deletion left a path in `git ls-files` that no longer
  existed on disk.
- **`git add -A` is not idempotent across attempts, so a step that stages must reset first.** Git
  applies ignore rules only to paths it does not already track or hold staged, so a file staged by a
  refused attempt survives being added to `.gitignore` and is committed by the retry. A `--mixed`
  reset before the add is index-only and is what makes a retry mean the same thing as a first run
  rather than merely be asserted to.
- **Staging is safe in a task worktree and unsafe in a checkout a person works in, so the guard must
  test the property, not the label.** A linked worktree is disposable scratch space that
  `worktree_start` creates and `lifecycle_finalize_task` destroys; a repository's own checkout can
  hold a partial `git add -p` selection, deliberately untracked files, and an in-progress merge.
  The refusal compares git's own `--git-dir` against `--git-common-dir` rather than the contract's
  `kind`, because `kind` is a label beside the path while the git-dir comparison constrains the path
  about to be written — and `default_series_contract` records `code_worktree = code.repo_path`, so
  the unsafe shape is producible.
- **A generated contract and a manual sample have different jobs.** The dashboard TypeScript mirror
  is generated and stale-checked from the Pydantic schema; fixture builders plus the fixture guard
  bind tests to it. `dashboard/src/fixtures/snapshot.json` remains hand-maintained, and the contract
  suite measures its coverage. Never describe the sample itself as generated or treat sample
  completeness as the producer-to-TypeScript authority.
- **A downstream integrity check is not a check if the downstream repairs itself.** tiktoken verifies the vendored vocabulary's SHA-256 and then answers a mismatch by deleting the file and re-downloading it, so "tiktoken verifies it" was never the guarantee it read as — inside an installed package that repair is a startup download plus a rewrite of the installed tree. `models/tokens.py` hashes the file itself before handing it over and raises `TokenizerVocabularyError`, which is what makes corruption behave like absence (260731-EFA-L3). When delegating verification, check what the verifier does on failure, not just that it looks.
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

| Finding | Anchor | Source |
| --- | --- | --- |


## What To Explore Next

| Priority | Area / Path                                                                                                               | Why Next                                                                                                            |
| -------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| high     | [mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager) | External workflow metadata and richer task-intake variables are the next likely worktree lifecycle polish area.     |
| high     | MCP-backed scheduled coordination and agent inbox direction                                                                | Future multi-harness coordination could use Agents Remember as a central inbox where Codex, Claude Code, Hermes, and cheaper/background harnesses pick up scheduled or queued work. Do not implement ad hoc timers for current tasks, but when an implementation would strongly benefit from periodic checks, queued work pickup, weekly evals, or scheduled refactors, record that as evidence for a future scheduler/poller system. |
| medium   | [mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow)                                     | The master + light sub-task escalation in the `w-02-light-task-workflow` skill (which absorbed the retired heavy workflow) may need a separate onboarding pass if worktree-backed task folders become common. |
| medium   | [mcp/src/agents_remember/package_data/runtime/system/defaults](agents-remember/mcp/src/agents_remember/package_data/runtime/system/defaults)                                                     | Add richer settings fixtures if cross-repo v2 behavior needs more than the current example files.                   |

## Needs Verification

- An older review recorded unrelated `resolve_auto_editor` checks in coordinator tools guidance. This is historical and was not reasserted against live coordination during isolated L31 recovery.
- The current source registry is useful as a discovery index but has no direct external domain evidence for this repo's own skill/workflow mechanics.
- External-memory onboarding for `agents-remember` is ledgered; future closeouts must keep the code-to-memory mapping current.
- The memory quality package is now the home for drift integrity and update-history style checks; further quality checks should be added under `memory_quality/style` or `memory_quality/integrity`.

## Historical Review Notes

Updated 2026-08-10T19:57:55+02:00 — No route impact: 260731-EFA-L21 changes the
checkout-only coordination boundary inside the existing MCP package routes; the repo-level
inventory and feature routing remain current. Verification metadata remains pinned until closeout
stamps the L21 code commit.

Updated 2026-08-05T22:30+02:00 — No route impact: 260731-EFA-L16 (the cross-store lock-order repair, its forcing tests, and the coding-guidelines/spawn-doctrine skill chain) is recorded in the `mcp/` and `skills/l-01-agent-lifecycles/` route overviews and their children; this root inventory is unchanged. Verification metadata pinned until closeout stamps the L16 code commit.

Updated 2026-06-28T07:43+02:00 — task 29 S7: refreshed the root Event River, actionable-drift, and dashboard frontend inventory for backend-retained raw events, raw-stream hydration, no frontend count cap, targetless actionable-drift dismissal, and the hidden Lifecycle Flow tab. Route detail lives in the `mcp/`, `observer/`, `serving/`, `controlplane/`, `memory_quality/`, `dashboard/src/`, and `dashboard/src/panels/` route overviews. Verification metadata pinned until closeout stamps the task-29 code commit.

Updated 2026-06-27T22:00+02:00 — task 28 (NOTIFY-AND-CONTINUE turn end): refreshed the Observable session lifecycle inventory row + functional-area section for the new public `lifecycle_turn_end_notification` tool, the non-terminal `awaiting-developer` state, the next-step hint repoint off the now-parked `lifecycle_gate`, and the reducer gate-open/blocked-gate dedup. Route detail lives in the `observer/`, `mcp/tools/`, and `models/` route overviews and their file sidecars. Verification metadata pinned until closeout stamps the code commit.

Updated 2026-06-17T22:45+02:00 after the Engine Room visual-parity pass enriched the dashboard-frontend Feature Inventory row (the 5g G6 atmospheric backdrop + Effects/Calm toggle, the restored HUD decal layer, and the fixed-height `Panel fill` layout); verification metadata stays pinned until closeout commits the source. (Prior: 2026-06-06T12:28+02:00 after adding the public `docs/features.md` tour, replacing README `## Core Model` with `## Core Features`, and documenting the Claude Code root `.mcp.json` detection caveat. Prior: 2026-06-04T10:29+02:00 — documented hidden harness starter packages as source-owned surfaces in the main overview and noted their `l-01` deep-research retrieval-strategy tally requirement. Prior: 2026-05-29T17:30+02:00 — re-spined the public docs and this overview's "What This Repo Is" framing around the three retrieval substrates (by path / by meaning / by relationship) and retired the sidecar-only anti-retrieval positioning. Prior: 2026-05-28T19:52+02:00 — added the Pydantic public response-contract model surface, compact `ContextPacketV2` boundary, and dedicated provider diagnostics feature inventory entries.)

## Historical milestone context: 260821-ARSPAWN-L2 Repository Feature Impact

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

Agent-facing session dispatch keeps `dispatch_agent` as its one public spawn tool, but its durable
identity is now explicitly the canonical `(taskDocumentRef, role)` seat rather than a runtime
session. Same-seat retries converge through pinned-brief evidence, vacancy-safe messages wait on
the address, and staged replacement is resolved only at delivery. Runtime ids remain private
generation/correlation data and are absent from public structural results.

## Historical milestone context: 260821-ARSPAWN-L3 Repository Feature Impact

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

The installed vocabulary now makes that runtime contract learnable: free chat compiles the
canonical architect brief and invokes `dispatch_agent` once; role tables say which seats are
plane-hosted callers and which are target-only; product and harness documentation repeat the same
two caller kinds and the no-fallback boundary. Canonical skills and generated package/harness
copies are synchronized projections, not competing authorities.

## Historical milestone context: 260821-ARSPAWN-L5 Repository Feature Impact

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

The repository now carries a dedicated `scripts/e2e_harness/` clean-room acceptance route for the
failure that motivated this master. The Dagger graph runs real Codex 0.151.0 against the candidate
MCP server and a deterministic localhost Responses provider, twice from fresh state with no retry.
It proves normally advertised `dispatch_agent` discovery for ambient and hosted callers, byte-exact
architect bootstrap, the ambient-to-worker structural chain, canonical manager addressing through
a real vacancy/replacement, actionable failure evidence, and complete teardown. Production starter
commands remain self-updating; the static pin belongs only to reproducible candidate acceptance.

## Update History

- 2026-08-30T21:25+02:00 — 260821-ARSPAWN-L5 added the real Codex 0.151.0 twice-fresh ambient/hosted spawning harness, connected-tool startup gate, canonical replacement-routing proof, and route-local onboarding. Verification remains closeout-owned.

- 2026-08-30T11:47+02:00 — 260821-ARSPAWN-L3 recorded one public spawn verb, the disjoint
  plane/ambient caller-kind matrix, one-call architect bootstrap, explicit role caller contexts,
  and canonical-to-generated projection ownership. Verification remains closeout-owned.

- 2026-08-29T09:45+02:00 — MCAR-L02 root reference reconciliation: repaired the exact closeout
  import citation after the canonical curator-coherence validator shifted the import boundary.
  Repository-level behavior and navigation remain unchanged, but the authored reference change is
  traced here rather than mislabeled as a no-route-impact attestation.

- 2026-08-26T12:30+02:00 — 260821-ARSPAWN-L2 root impact: reconciled idempotent canonical seats, durable
  brief evidence, vacancy/replacement delivery, and runtime-id-free public outcomes into the
  repository feature inventory. Verification remains closeout-owned.

- 2026-08-15T04:32+02:00 — 260815-DAG-L2 route impact: recorded the ruled fact/judgment split,
  architect-owned initial plan loop, organizational versus atomic lifecycle topology,
  ready-frontier orchestration, and exact pre-landing completion boundary. This leaf updates
  doctrine and synchronized assets; later leaves own mechanical cutover. Verification remains
  closeout-owned.
- 2026-08-13T14:32+02:00 — L23 final repository-route review: recorded Dagger-only acceptance,
  targeted leaf/focused versus once-per-master full altitude, mandatory explicit diff base,
  generated help, and diagnostic-only host pytest/wrapper execution. Verification remains
  closeout-owned.
