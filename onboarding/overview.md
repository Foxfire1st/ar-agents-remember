# agents-remember — Onboarding Overview

| Field | Value |
|---|---|
| sourceRoute | . |

## What This Repo Is

`agents-remember` is the source repository of the Agents Remember system: the skills, the MCP server
with its tools, the dashboard and the design documents that agents use to keep onboarding knowledge
beside code. A source file's note lives at a deterministic mirror path in the memory repository, so
an agent that holds a file reaches its note without search. The `c-04-retrieval-strategy-router`
skill names three retrieval substrates. Semantics serves a concept whose location is unknown and
prefers GrepAI over the memory repositories. Relationship serves a known anchor whose callers,
callees or dependencies are unknown and prefers CodeGraphContext over the code repository. Intent
serves a known location whose contracts are unknown and prefers the `read_ar_files` tool, which
reads a source file together with its onboarding. The two providers are optional and run in Docker.
The by-path memory works without them, and provider results help to locate files while Markdown and
source code remain the truth.

The system's hosted sessions are Paseo-native. AR resolves the role hierarchy, the role's folder,
the task capsule and the report scope through the launcher seam in `cli/role_launch_routes.py`,
chooses the agent id and records the launch; Paseo owns the actor and workspace identity and the
agent session, and the receipt retains only that execution reference. The reader config of a
call that carries a task context comes from the leaf's admitted enclosure
(`application/task_scoped_mcp.py`). Execution completion, review, curation, semantic acceptance and
paired publication remain separate facts, and a task-local qualification or draft artifact is
neither a source-memory branch nor a published result.

Durable memory lives in a memory repository of its own, under
`ar-coordination/memory-repos/ar-<repo>/`. `kernel/memory_mode.py` declares the supported memory
modes of a worktree contract, `external` and `disabled`, and the one supported topology,
`external`. The removed repo-local mode, a memory root at `<code repository>/ar-memory`, is refused
by name with a message that carries the supported set and the way out. It is never substituted with
`external`, and existing state that records it is reported with its exact artifact and left
untouched.

The `c-08-ar-coordination-context-resolver` skill resolves the context of a code repository; its
outputs include `code_repository_name`, `code_repository_root`, `coordination_root`, `memory_root`,
`task_root` and `temp_root`. The `c-09-git-worktree-manager` skill creates, attaches to, reports
on, integrates, finalizes and cleans up worktree-backed tasks, and it documents `task_reopen`, which
is a state reset and creates no worktree. The `c-12-closeout` skill owns closeout and the
policy-gated, branch-addressed `direct_landing` of a leaf delivered without its own worktree
enclosure. The `c-10-adopt-memory-baseline` skill adopts existing external-memory onboarding as the
first Git-attributed baseline.

Provider authority comes from the MCP settings file, which lies outside the coordination root. The
GrepAI provider (`grepai-memory`) indexes the memory roots, one per configured repository, with a
PostgreSQL database and a Dockerized Ollama for embeddings. The CodeGraphContext provider
(`codegraphcontext-code`) uses a FalkorDB database in Docker. Under the coordination root, database
data lives in `providers/data/<provider>/<instance id>/`, image locks and requirement files in
`providers/requirements/`, and CodeGraphContext patches in `providers/patches/codegraphcontext/`.

## Feature Inventory

This is the inventory of the system surface. Each row names what a feature offers and where it
lives; the route overviews and the file cards carry the detail. When a feature is added, removed,
renamed or moved, this section is updated in the same onboarding pass.

| Feature | What It Offers | Primary Surface |
| --- | --- | --- |
| Path-derived onboarding memory | A note for each source file at a deterministic mirror path, route overviews for larger scopes, and one entity catalog per repository (`entities.md`). | `README.md`, `c-05-create-or-update-onboarding-files` skill |
| External memory and the disabled mode | `external` and `disabled` are the supported memory modes; the removed repo-local mode is refused with the status `memory-mode-unsupported`. The consumer ledger `memory.md` is a disposable view: it is derived from the `Code-Commit` trailers of the memory commits and is kept out of memory-content commits. | `kernel/memory_mode.py`, `kernel/memory_attribution.py`, `kernel/memory_cache.py`, `kernel/memory_ledger.py`, `c-00-initialize-memory-repo` skill |
| Context resolution and startup packets | The `c-08` skill resolves the roots and settings of a code repository. `context_packet` returns the typed `ContextPacketV2` with the blocks repo, paths, memory, worktree, providers, drift, freshness and diagnostics. | `c-08-ar-coordination-context-resolver` skill, `resolve_context`, `context_packet`, `models/context_packet.py` |
| Memory quality control | `drift_check` qualifies existing onboarding at task start when it is requested. The curator runs the complete `memory_quality_check`: it never changes code or memory, a full contract-scoped call replaces the curator checklist with its attestation and publishes the structural census, and `curatorActionableCount` and `qualityChecklistStatus` are the repair-loop gate. `curator_coherence` publishes the coherence authority when the checklist requires it. On converted memory the run also reports the knowledge validator's findings, the change-to-knowledge worklist and the verdict of the knowledge gate. | `c-02-memory-quality-control` skill, `drift_check`, `memory_quality_check`, `curator_coherence` |
| Maintained knowledge records | Invariants, families, decisions and assumptions as text records under `knowledge/`, realization and proof entries in card sidecars, history files, a validator, a derived read index and a mandatory gate at closeout. | `agents-remember knowledge-*` commands, `knowledge_read`, `read_ar_files`, `application/knowledge_writer/`, `application/knowledge_worklist/`, `application/knowledge_gate/`, `memory_quality/knowledge_validator/`, `models/knowledge_files/` |
| Retrieval routing | The three substrates of the `c-04` skill, with the generated route indexes `overview.index.json` for cheap routing. The `read_ar_files` call also carries the repository's published intent: the invariants already recorded about the requested paths, without needing a task. | `c-04-retrieval-strategy-router` skill, `overview.index.json`, `grepai_*` tools, `cgc_*` tools, `read_ar_files` |
| Onboarding bootstrap | Bootstraps onboarding for undocumented repositories and for existing memory slices: root overviews, route-local overviews, evidence packs, file cards, onboarding waves, cleanup of deleted slices, curator reviews and handoff. | `c-03-repo-bootstrap` skill |
| File and entity onboarding maintenance | Creates and maintains file-level onboarding and the repository entity catalog, with strict one-to-one source mapping and governing-overview links; it routes create, refresh, move and delete cases of a package, module or source slice to the `c-03` skill. `route_index_refresh` regenerates the route indexes. | `c-05-create-or-update-onboarding-files` skill, `route_index_refresh`, `kernel/route_index.py`, `kernel/route_index_census.py` |
| Findings capture | Captures confirmed findings, routes them to a durable task-local path, and propagates factual current-state clarifications into onboarding when allowed. | `c-01-findings-capture` skill |
| Workflow modes | The build decision is taken at `decide`: a research-only exit for answers that change no code, otherwise a durable `w-02-light-task-workflow` task. Chat is never a build route. Small code work takes the minimal `w-02` artifact, and work that outgrows a single-page plan escalates to a master with a light sub-task series. | `AGENTS.md`, `l-01-agent-lifecycles` skill, `w-02-light-task-workflow` skill |
| Agent lifecycles (one per role) | The `l-01-agent-lifecycles` skill is a role-capsule router: a role agent receives exactly one role file and one operation file, selected by the role and operation that the AR role launcher or the `role_start` tool supplies, with the canonical task references in the handover. The launcher offers seven roles: architect, system-specialist, orchestrator, manager, worker, reviewer and curator; the manifest keeps designer, strategist and bootstrap as entries that the router does not launch. Paseo hosts each role agent, and role agents start and message each other with `role_start` and `role_message`. An architect or a system specialist can be started without a task. `core/` is metadata for the capsule compiler and is not injected into a role capsule. The master-handover packet cites the candidate tree, code ancestry, memory ancestry and the accepted Git commit pair of every leaf. | `skills/l-01-agent-lifecycles/SKILL.md`, `composition-manifest.json`, `roles/`, `operations/`, `templates/master-handover-packet.md` |
| Closeout | Closeout is worktree-only: every change that affects the code repository runs through a dual worktree (code and memory), and there is no direct-checkout closeout path. The apply tool takes an `intent_note` that records the authority, either explicit developer commit approval or delegated accepted-series authority, and every enabled commit leg needs its own commit message. `direct_landing` is the policy-gated, branch-addressed route for a leaf delivered without its own worktree enclosure. On converted memory the closeout preview and the apply ask the mandatory knowledge gate. | `c-12-closeout` skill, `worktree_closeout_preview`, `worktree_closeout_apply`, `direct_landing` |
| Worktree lifecycle | Start, attach, status, sync, pause, closeout, integration, landing record, finalization, abandon and cleanup of worktree-backed tasks. `worktree_pause` releases one master's atomic-series activation selection and publishes nothing; `worktree_checkpoint_landing` is the separate, explicitly requested publication of an unfinished master. The activation record is one durable, replace-in-place snapshot per canonical series contract, so two atomic masters that share one protected source pair never share that state. A sync is a resumable transaction whose record is `reports/sync-operation.json` of the worktree group and whose commits are pinned by Git refs. | `c-09-git-worktree-manager` skill, `worktree_*` tools, `lifecycle_finalize_task`, `task_reopen`, `worktrees/` |
| Observable session lifecycle | The observer holds the append-only `ar-observer-event/v1` event log, the ambient lifecycle with its `lifecycle_*` signals, and the reducer, which is the single owner of interpretation and folds events and file snapshots into the projection. `application/tool_response.py` completes each tool result: it selects the wire model, attaches lifecycle-wide state, finalizes the token count and records the call. A tool response can carry a `nextStep` hint computed from the projected lifecycle state. | `agents_remember.observer`, `application/tool_response.py`, `models/tools/tool_response.py`, `application/next_step.py` |
| JSON-primary task documents | The `ar-task-document/v1` JSON is the source of truth and `task.md` is its deterministic render; the Markdown is never parsed back. The `task_doc` tool authors `subTask` and `master` documents and refuses to author a `light` document, a kind the schema still reads. A sprint document can carry an `executionGraph`, and a master an `executionNature` (`organizational` or `atomic`). A mutation classed as topology, intent or completion readiness invalidates the closeout queue projection. | `agents_remember.tasks`, `task_doc` tool, `application/task_docs/` |
| Gate control plane | Gates are durable records: a `GateRecord` in an append-only `GateStore` beside the observer event log. A mutating tool writes the `applied` transition when it consumes an approval. A human approval is always binding; an approval decided by the model does not satisfy enforcement; a non-human orchestration approval binds only when the policy delegates that gate kind to the deciding role and the decider is not the lifecycle that owns the gate. A lifecycle with no gate of the requested kind is gateless, and the existing approval channel governs. The lifecycle skills hand a developer decision off with `lifecycle_turn_end_notification`, and the first tool call of the next turn resumes the lifecycle; `lifecycle_gate` still works when it is raised. The dashboard records a developer's decision on a lifecycle's gate through `record_lifecycle_gate_decision`. | `agents_remember.controlplane`, `controlplane/enforcement.py`, `controlplane/gate_decisions.py`, `lifecycle_gate`, `gate_decide`, `gate_list`, `lifecycle_turn_end_notification` |
| Dashboard serving layer | `agents-remember dashboard` runs a FastAPI app over the observer projection. One shared projector fans the snapshot and per-entity deltas out to every client over one multiplexed server-sent event stream; the layer is transport and adds no interpretation. It also serves the built frontend and hosts harness sessions. `--daemon`, `--status` and `--stop` supervise a detached server, and the MCP settings key `dashboard.autoStart` starts one at server boot. | `agents_remember.serving`, `cli/dashboard.py`, `serving/daemon.py` |
| Dashboard frontend | The React application under `dashboard/src/`. `cockpit/Cockpit.tsx` is the shell; Chats is its opening view (260928-MIK-L79), and the Chats view mounts the role chats pane `cockpit/RoleChats.tsx`. | `dashboard/src/cockpit/`, `dashboard/src/panels/`, `dashboard/src/data/` |
| Controlled sessions: capabilities, set controls and submission | `serving/harness_capability_catalog.py` discovers capabilities before a session exists, without tokens, with a bounded install-aware cache. `serving/harness_control_api.py` holds the harness-neutral routes for advertise, live set and reliable submit. A model or effort set returns a result whose acceptance is one of `echo-verified`, `immediate`, `queued`, `unknown` or `unsupported`. In the dashboard the options of a live session come only from `GET /api/terminal/{session}/capabilities`, and a model-plus-effort change is serialized: set the model, wait for its acceptance evidence, then set the effort; an `unknown` result holds the step until one snapshot readback. One submission authority per hosted bridge is the only prompt queue: it linearizes withdrawal against dispatch and pins an accepted operation until an exactly correlated completion releases it. A repeated request id with the same source and payload is idempotent, and with another payload it is a conflict. | `serving/harness_capability_catalog.py`, `serving/harness_control_api.py`, `serving/harness_capabilities.py`, `serving/harness_submission_authority.py`, `dashboard/src/data/{sessionCapabilities,setAcceptance,pairChange,submitMachine}.ts` |
| Session dispatch and open | `dispatch_agent` is the public tool that dispatches a hosted role. `serving/terminal_opener.py` is the one spawn path that the dashboard route `POST /api/terminal/{session}` and the internal `spawn_agent_session` primitive behind `dispatch_agent` share. The uniqueness of a structural seat is arbitrated by the server: a taken seat is answered `seat-taken`. `serving/task_binding.py` is the fail-closed task-binding preflight of every spawn path; the roles `chat`, `terminal`, `bootstrap` and `curator` are admitted without a task document. | `dispatch_agent`, `serving/terminal_opener.py`, `serving/task_binding.py`, `serving/structural_dispatch.py`, `dashboard/src/data/terminalOpen.ts` |
| Task seats of hosted sessions | A hosted session is assigned to a role seat of a canonical task document. Sprint roles (architect, orchestrator, strategist, designer, system-specialist) sit on the sprint document, the manager on the master document, workers and curators on their leaf documents, and a reviewer on the leaf, master or sprint document it reviews. | `serving/terminal_task_assignment.py`, `tasks/document.py`, `POST /api/terminal/{session}/attach-task` |
| Agent messaging and the operator inbox | `message_parent` and `message_child` are the public messaging tools between seats; `role_start` and `role_message` are the public tools that start and message role agents. Delivery goes through the harness protocol adapter of the exact session. A pending inbox row waits for at most 48 hours, a terminal row is kept for 48 hours, and the folded inbox is capped at 500 rows. The dashboard's gate responder posts a developer's response to the inbox, except for a gate that carries a hosted adapter interaction, where the gate decision itself is the response. Gate and inbox interactions are short-lived records with a retention policy; the `applied` snapshot of an approval that a mutation consumed is an authority record and is kept. | `mcp/registration/orchestration.py`, `serving/inbox_delivery.py`, `controlplane/operator_inbox_store.py`, `controlplane/interaction_retention.py`, `dashboard/src/panels/GateResponder.tsx` |
| Event stream and Event River | `GET /api/events` streams the raw `ar-observer-event/v1` records of the append-only event logs verbatim, with resume by byte offset. The dashboard panel `EventRiver.tsx` shows observer events, with labels from `eventSummary.ts`. | `serving/events.py`, `dashboard/src/panels/EventRiver.tsx`, `dashboard/src/panels/eventSummary.ts` |
| Cross-repository context | The `c-08` skill returns the branch-gated allowed adjacent repositories from the `crossRepo` data of the memory layer's settings. | `c-08-ar-coordination-context-resolver` skill, `system/settings.json` |
| Runtime and skill installation | `runtime_install` installs the runtime assets of the package into the coordination root, among them the four `AGENTS.md` templates. `skills_install` copies the packaged skills into harness skill roots. | `runtime_install`, `skills_install`, `install/runtime.py`, `install/skills.py`, `package_data/runtime/` |
| Harness starter packages | Starter packages for Claude Code, Codex, Cursor, Antigravity, VS Code Copilot, Hermes, Pi.dev and OpenClaw carry the MCP settings, skills, hooks, rules and instruction files each harness needs. | `.claude/`, `.codex/`, `.cursor/`, `.agents/`, `.github-vscode/`, `.vscode/`, `.hermes/`, `.pi/`, `.openclaw/`, `docs/install/` |
| MCP server and settings | A stdio MCP server. `kernel/primitives/runtime_config.py` loads the trusted settings file; the example names the coordination root, the workspace root, the transcript root, the repositories, the providers, the timeout caps and the dashboard, provider-degradation and retirement settings. `mcp/public_surface.py` validates that the public tool inventory, the response registry, the live registration and the dispatch schema agree. The `o200k_base` tokenizer vocabulary ships inside the package under `package_data/tiktoken/`, so token counting needs no download. | `mcp/server.py`, `mcp/public_surface.py`, `kernel/primitives/runtime_config.py`, `models/tokens.py`, `examples/mcp/settings.example.json` |
| Tool response contracts | Every tool payload is validated against the response model registered for it, and its token count is finalized. Responses whose shape the package owns use strict models; responses that embed provider-native detail use flexible models on purpose. | `models/tools/tool_registry.py`, `models/tools/tool_response.py` |
| Provider lifecycle and discovery tools | GrepAI search and trace over memory, CodeGraphContext symbol, caller, callee, dependency, complexity and visualization queries, provider status, diagnostics and watcher lifecycle. The CodeGraphContext graph probe answers `indexed`, `empty`, `backend-unreachable` or `unknown`; the GrepAI state is `unavailable`, `noWorkspace`, `indexing`, `indexed` or `unknown`. Launch-capable operations re-read the providers map from the settings file on disk and treat an unreadable file as no launch authority; stopping and cleanup are never gated. A provider `prepare` that is not a dry run runs behind one host-scoped lock in the system temporary directory; the `install` action and dry runs do not take it. Container metrics are sampled read-only into one store under the observer root. | `provider_status`, `provider_diagnostics`, `provider_watchers`, `grepai_*`, `cgc_*`, `providers/` |
| Tool report files | Verbose tool payloads go to report files under `temp/tool-reports/<tool>/`; the response keeps the outcome and a `reportPath`. Retention is applied when a report is written. | `kernel/primitives/tool_reports.py` |
| Memory baseline adoption | Adopts existing external-memory onboarding as an attributed Git baseline; actionable drift blocks the adoption unless the developer accepts the onboarding as the baseline. | `c-10-adopt-memory-baseline` skill, `memory_baseline_status`, `memory_baseline_adopt`, `memory/baseline.py` |
| Branch memory carryover | Carries the onboarding of a landed branch into the memory worktree of an ordinary external-memory recovery leaf. Its candidate kinds are file sidecar, route overview, entity catalog and memory-only document. `memory_carryover_apply` refuses a converted memory tree. | `c-11-memory-carryover-from-branch` skill, `memory_carryover_plan`, `memory_carryover_apply`, `memory/carryover.py` |
| Benchmark harness | Benchmark preparation and runs for Codex; the MCP setting `benchmarksEnabled` switches the tools on. | `codex_benchmark_prepare`, `codex_benchmark_run`, `benchmarks/` |
| Source quality tooling | Ordinary pytest supports development; only the pinned Dagger graph and the lifecycle owners produce certifying evidence. Coverage is diagnostic, and production CRAP at 20 is a review trigger, not a delivery blocker. | `AGENTS.md`, `docs/design/python-pytest-bootstrap.md`, `docs/design/python-test-evidence.md` |
| Self-hosted harness configuration | `scripts/harness/` is the single source of the self-hosted harness starter packages; `scripts/sync-harness.py` generates them, and `scripts/harness/README.md` records which differences between harnesses are genuine requirements. | `scripts/sync-harness.py`, `scripts/harness/` |
| Public docs and harness guides | The documentation index, the getting-started, concepts, architecture, workflows, features and FAQ pages, and the install, guides, reference and design folders. | `docs/`, `README.md` |
| Canonical runtime and skills asset sync | The root folders `agents-md-files/`, `benchmarks/`, `providers/`, `system/` and `eve_runtime/` are canonical and are copied into the MCP package data by `scripts/sync-runtime.py`. Root `skills/` is the canonical skill tree; `scripts/sync-skills.py` copies it into the package data and into the harness starter packages. The hook gate checks the generated copies of skills, runtime, harness and projection types. | `scripts/sync-runtime.py`, `scripts/sync-skills.py`, `scripts/sync-harness.py`, `scripts/sync-projection-types.py`, `.githooks/_gate.sh` |
| Dashboard bundle release build | `scripts/sync-dashboard.py` places the Vite output `dashboard/dist/` into `package_data/dashboard/`, which is not under version control, and refuses a `dist` that does not carry the fingerprint of the current build inputs. Its `--check` mode writes nothing and reports whether the placed bundle still matches `dashboard/dist`. No hook runs the script. A checkout without a bundle answers `503` on the static surface and names the build command. | `scripts/sync-dashboard.py`, `serving/static.py` |

## Hot Path Summary

A leaf's closeout commits its code and its memory content. A memory commit names its code commit in a `Code-Commit` trailer, and the consumer ledger `memory.md` is derived from those trailers and never committed as content.

Use [MCP package](mcp/overview.md) for composed services, [memory quality](mcp/src/agents_remember/memory_quality/overview.md) for the memory-quality run and the knowledge validator, and [worktrees](mcp/src/agents_remember/worktrees/overview.md) for the worktree lifecycle. The [test route](mcp/tests/overview.md) says how a test run is composed, states the test policy and describes the two test catalogs.

## Architecture At A Glance

```text
agents-remember/
  AGENTS.md
    source checkout instructions and installed-runtime handoff
  README.md
    public setup and conceptual model
  layers.toml
    top-level package dependency order and package charters
  .gitattributes
    whitespace exemption, binary marking and union merge for the two test catalogs
  .githooks/
    the hook gate and its pre-commit and pre-push tiers
  mcp/
    the MCP package: source under src/agents_remember/, test support under test_support/, tests under tests/
  mcp/src/agents_remember/package_data/runtime/
    agents-md-files/
      coordinator/AGENTS.md
      skills/AGENTS.md
      system/AGENTS.md
      tasks/AGENTS.md
    skills/
      c-* skills, l-01-agent-lifecycles and w-02-light-task-workflow
    system/defaults/examples/
      coordinator and memory-repo example settings, sources and tools files
  skills/, agents-md-files/, providers/, system/, benchmarks/, eve_runtime/
    canonical editable sources of the generated package-data copies
  dashboard/
    React dashboard frontend
  scripts/
    synchronization and runtime tooling
  docs/
    public documentation and design documents

workspace ar-coordination/
  AGENTS.md
  skills/
  memory-repos/ar-agents-remember/
    onboarding/
      cards, sidecars and route overviews for this repository
    knowledge/
      invariant, family, decision and assumption records and the history files
    system/
      settings and repository-specific guidance
  tasks/
    task documents and enclosure contracts
  temp/
    temporary generated artifacts such as drift reports and tool reports
```

## Code Structure

| Area | Path | Purpose |
| --- | --- | --- |
| Source checkout instructions | `AGENTS.md` | Says how agents work on this source checkout and when to use the installed runtime instructions instead. |
| Public documentation | `README.md` and `docs/` | The README is the public front door; the pages and folders under `docs/` hold setup, concepts, architecture, workflows, install guides, guides, reference and design. |
| Package dependency contract | `layers.toml` | One strict order over the top-level packages and one charter per package. A module of a package may import another package only when that package's rank is lower. |
| MCP package | `mcp/` | The MCP server, its tool surface and the package-owned runtime services. |
| Skills | `mcp/src/agents_remember/package_data/runtime/skills/` | The generated package copy of the skill tree: the `c-*` skills, `l-01-agent-lifecycles` and `w-02-light-task-workflow`. |
| Lifecycle skill | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/` | A router `SKILL.md`, a `core/` that is metadata for the capsule compiler and is not injected into a role capsule, one file per role under `roles/`, operation blocks under `operations/`, the routing metadata `composition-manifest.json`, and reference-only material under `reference/`, `criteria/` and `templates/`. |
| Runtime AGENTS templates | `mcp/src/agents_remember/package_data/runtime/agents-md-files/` | The coordinator, skills, system and tasks `AGENTS.md` templates that `runtime_install` installs. |
| System defaults | `mcp/src/agents_remember/package_data/runtime/system/defaults/examples/` | Example settings, sources and tools files for a coordinator and for a memory repository. |

## Functional Areas

### Source Checkout Contract

`AGENTS.md` is the instruction file for agents that work on this source checkout. It first separates the source package from the installed runtime: an agent that reaches the file through a workspace-level pointer while it works on a sibling repository uses the installed `ar-coordination/AGENTS.md` instead. For work on this repository it names `agents-remember` as the resolver target, routes sessions by role through the `l-01-agent-lifecycles` skill, asks for `c-08-ar-coordination-context-resolver` resolution and a `c-02-memory-quality-control` run before reasoning from onboarding or source, and says that the checkout has no active root-level `system/` settings: the settings are read from the resolved memory layer. It separates implementation approval from commit approval.

### Package Layer Contract

`layers.toml` declares one strict order over the top-level packages of `agents_remember` and one
charter per package. A module in package P may import package Q only when the rank of Q is
lower than the rank of P; the contract carries no baseline and no exception. The order begins
`errors`, `kernel`, `models`, `certification`, `controlplane`. The charter of `certification` calls
it the repository-neutral certification contract (rail and profile schemas, validation,
deterministic planning, content identity, bounded admission and typed terminal gate results) and
keeps concrete repository profiles, executors and lifecycle terminalization with their owners. The
charter of `controlplane` calls it the lowest of the stateful interaction services. The layering
checker in `mcp/test_support/agents_remember_test_support/code_quality/layering.py` loads the
contract and reports package directories that it does not declare.

### Public Documentation

The README has the sections Why It Exists, Core Features, What It Looks Like In Practice, Live
Demo, Requirements, Quickstart, Run The Dashboard, Documentation, Repository Layout, Status,
Stability and Contributing. `docs/` holds the documentation index `README.md`, the pages
`getting-started.md`, `concepts.md`, `architecture.md`, `workflows.md`, `features.md` and `FAQ.md`,
and the folders `install/`, `guides/`, `reference/` and `design/`. The memory path rules exclude
`docs/**`, so a document has no one-to-one card; the `docs/design/` overview describes the design
documents.

### Harness Starter Packages

The hidden root folders `.claude/`, `.codex/`, `.cursor/`, `.agents/`, `.github-vscode/`, `.vscode/`, `.hermes/`, `.pi/` and `.openclaw/` are the harness starter packages. `scripts/harness/` is their single source and `scripts/sync-harness.py` generates them; a file that a starter package owns alone, such as `.codex/config.toml`, is edited in place. No include rule covers these folders, and an exclude rule names `.vscode/**`, so their files have no cards. The skill folders inside them are copies of the root `skills/` tree, written by `scripts/sync-skills.py`.

### Runtime AGENTS Templates

`mcp/src/agents_remember/package_data/runtime/agents-md-files/` is the generated package copy of the root `agents-md-files/` folder. `runtime_install` installs `coordinator/AGENTS.md` as `AGENTS.md` of the coordination root, and `system/AGENTS.md`, `skills/AGENTS.md` and `tasks/AGENTS.md` under the same names. The coordinator template says that a memory repository is not expected to provide a root-level `AGENTS.md`: repository-specific guidance lives in the memory layer's `system/*` files. The system template is the start-of-task onboarding trust gate: it requires context resolution, the context packet, a drift check, and a classification of the findings that is reported to the developer before work continues.

### Core Resolver And Memory Quality Control

The `c-08-ar-coordination-context-resolver` skill resolves, for one code repository, the coordination root, the memory root, the task root and the temporary root. Without a task name, `task_root` is the repository's task namespace; with a task name or a contract it is the task's folder. The `c-02-memory-quality-control` skill owns the diagnostic procedure and reports and routes memory quality work; it does not rewrite onboarding prose itself. The path rules of this memory live in `system/settings.json`: they include `AGENTS.md`, `README.md`, `dashboard/src/**`, `examples/mcp/**`, `installer/**`, `mcp/**`, `runtime/**` and `scripts/**`, and they exclude `docs/**` together with generated, vendor, build, cache, IDE and environment paths. A drift report is written under `drift-reports/` of the temporary root.

### Onboarding Maintenance

The `c-05-create-or-update-onboarding-files` skill creates and maintains file-level onboarding and the repository entity catalog `entities.md`. File-level onboarding is strictly one-to-one with source files and links to its governing overview. The entity catalog uses deterministic `git-blob-set-v1` fingerprints over curated evidence paths. The skill routes the create, refresh, move and delete cases of a package, module or source slice to the `c-03-repo-bootstrap` skill. `overview.index.json` beside a route overview is generated metadata: it holds the route's `sourceScope`, `childRoutes`, `coveredFiles`, `coverageCounts`, `routingTerms` and the `hotPath` summary copied from the overview, and the `c-04` skill reads it before it opens the overview prose.

On converted memory a card states what its file does in present tense and has no metadata table and no Update History; Git keeps its history. Its evidence is written as a citation table, and the citation fixer turns each row into a numbered reference in the card's JSON sidecar, with the anchor's blob and content hash taken at the code working tree. The skill's `workflows/converted-card-workflow.md` is the procedure.

### Knowledge Records And The Closeout Gate

The memory repository of this project is converted: `knowledge/layout.json` marks the tree, and
knowledge is text. Prose is Markdown and structured facts are canonical JSON: cards and route
overviews with their sidecars under `onboarding/`, and global records under `knowledge/`
(invariants, families, decisions and assumptions). `knowledge/history/` holds one history file per
owner, where an owner is a leaf, a migration wave or a crossing sync, and one more per attempt of a
reopened leaf. The database file `knowledge.sqlite` that the tree still holds is frozen and is not
read.

**Writing.** The curator file writer creates and updates records, realization and proof entries and
history rows. `agents-remember knowledge-ingest` runs it on a leaf's enclosure contract, and
`agents-remember knowledge-bootstrap` runs it for a repository's first records without a leaf;
`knowledge-ingest --crossing` is the route of a master line's crossing sync. The writer takes a
hand-off list, fills every mechanical field (identifiers, anchors with blob and content hash at the
code candidate, revisions, canonical formatting), validates the whole resulting tree and only then
writes. Without `--commit` a run plans, validates and reports, and writes nothing. The mounted
`knowledge_change` tool writes nothing and names the write route. The references of a card are
written by the citation fixer (`agents-remember memory-citations --fix`, or the `citation_fix` tool),
and the closeout closes the leaf's history file.

**Admission.** Every new invariant, family and decision record states the admission criterion it
meets with a justification in one sentence, and the knowledge validator refuses a new record without
one. A decision names at least two alternatives, exactly one of them chosen, and each rejected or
deferred alternative says when to reconsider it. A family owns its routes, the directories where its
code lives (`.` for the repository root). Routes that do not cover every member's realization, and a
route that holds none, are refused by every commit route; inside the writer the same rules are
reported and not refused, so a leaf can repair them before closeout.

**Reading.** `read_ar_files`, and `knowledge_read` with the view `source_context` and a
`sourcePath`, return for a file its own invariants, every family that contains them with its
guarantee, routes and members, and then one compact row per family whose route lies on the file's
directory or an ancestor. The read goes through an index derived from the memory tree. A knowledge
read is cut to a threshold of 8,000 tokens, which the response states, and `knowledge_read` accepts
the continuation token of a page. The `invariant` and `family` views carry the tests that prove an
invariant.

**The gate.** Every closeout of a leaf on converted memory passes the mandatory knowledge gate: the
knowledge validator, the onboarding gate and the change-to-knowledge worklist. The onboarding gate
asks, for every changed source file under the path rules, that its card and its nearest governing
overview carry either a counted change (Markdown, or a sidecar field other than an anchor's blob,
line numbers and content) or an `onboarding_trace` row with the disposition `no_impact` in the
leaf's history file. The worklist lists what the curator answers: a change that no recorded entry
covers, an invariant the change touches, an invariant whose entry was already stale at the base, a
family it reaches, a family whose routes it breaks, a planned knowledge effect that was not
delivered, and a rejected alternative whose reconsideration link names something the leaf changed.
`worktree_closeout_preview` asks the gate and answers `knowledge-gate-refused` with the findings
instead of `would-closeout` when the gate refuses, and the apply asks the same gate before it
commits a leaf's memory.

**Unconverted lines.** A memory line without the layout marker, in a repository that holds converted
memory, is only read. The cutover lock refuses its writes, memory-quality runs, managed memory syncs
other than a crossing sync, closeouts and landings, and names the crossing sync.

The curator role and the curator hand-off template say how records, entries, proofs and history rows
are authored. The authored copies are under `skills/`; `scripts/sync-skills.py` writes the package
copy and the harness starter copies.

### The Reviewer's Comparison

On converted memory the Intent Reviewer's comparison of a leaf is four Git trees: the code base, the
code candidate, the memory base and the memory candidate. The memory base is the memory commit that
the worklist pairs with the code base, so the reviewer and the worklist compare the same sides. An
uncommitted candidate is pinned by a ref `refs/ar/review/<task-id>/<leaf-id>/<n>` in its own
repository before the comparison is published; a comparison whose four trees equal the leaf's
latest recorded one reuses that record. Each memory side is read through the derived index of its
tree, and no database copy is created or read. A comparison reopens from the tree ids of its record;
a tree that Git can no longer produce is named as `unavailable-history`, and today's tree is never
substituted. A request to freeze a tree comparison into a dataset generation is refused.

### MCP And Context Provider Runtime

The providers are accelerators, and the MCP settings file is their authority. A server loads its settings once, so launch-capable provider operations read the providers map from the file on disk again: an operator who empties the map on disk stops launches on running servers, an unreadable file means no launch authority, and stopping and cleanup are never gated. A provider `prepare` that is not a dry run takes a host-scoped lock in the system temporary directory, because the guarded resource is the host's memory and Docker daemon, shared by every coordination root and every benchmark workspace. `runtime_install` installs the runtime assets, and `skills_install` copies the packaged skills into harness skill roots.

GrepAI indexes the memory roots, one per configured repository. Its database data lives under `providers/data/grepai/<instance id>/postgres`, and the CodeGraphContext database under `providers/data/codegraphcontext/<instance id>/falkordb`. A worktree gets its providers by copying existing index data: the GrepAI clone is guarded by a stall watchdog and has no total-duration cap, and the export and import of the CodeGraphContext seed are bounded by the provider-setup timeout cap. `run_git` gives a Git child `stdin=DEVNULL` unless input text is passed, because under the stdio transport the parent's standard input is the JSON-RPC request pipe.

### Task Workflows

The `w-02-light-task-workflow` skill is the durable-task workflow. It creates the task wrapper folder with its requirement corpus first, and creates `task.md` only after the developer has approved that corpus. No implementation begins before explicit developer approval, and implementation approval is separate from commit approval. Refreshed external-memory onboarding is committed, with the computed ledger cache excluded, before the `c-09-git-worktree-manager` skill starts worktrees.

A requirement's `ID@version` states semantic intent and changes only through explicit developer
approval. A delivery attempt is a separate identity: the builder advances it only when it hands an
exact candidate to independent review, or when a reviewer's rejection requires a successor handoff.
Implementation, test and evidence reruns mint no attempt; they are kept as protocol events.

### Bootstrap Memory Build

The `c-03-repo-bootstrap` skill bootstraps onboarding for a repository with little or no memory coverage, and for an adopted memory repository whose source slices need targeted creation, refresh, move handling or cleanup. Its minimum result is one root `overview.md` under the resolved onboarding root. For larger repositories it works route by route and in waves: area research, a coverage plan, a governing route map, route-local overviews, evidence packs, file cards, file-level onboarding waves, curator review and handoff.

### Worktree Support

The `c-09-git-worktree-manager` skill and the `worktree_*` tools carry a task from start and attach through status, sync, closeout and integration to `lifecycle_finalize_task` and cleanup. A master's `series-contract.md` lies at the root of its task folder, and each leaf's contract at `enclosures/<leaf-id>/series-contract.md` under it. An external-memory start requires the memory repository and the task-derived memory source branch to exist, and it creates the memory worktree from that branch; it does not inspect uncommitted files of the source checkout. `lifecycle_finalize_task` proves the landed parent-child branch edge, runs the cleanup unless the contract already records it as completed, and updates the task and its row on the immediate parent. A leaf's parent is the one it declares, and otherwise the master in the folder's `task.json` when that master lists it; a leaf without a parent finalizes standalone. The finalizer does not complete the parent itself.

Integration has the strategies `ff-only` and `replay`. When a source branch moved after the leaf closed, neither strategy lands and no replay commit is created: `ff-only` answers `blocked-non-ff` and names the remedy (sync the leaf with `worktree_sync`, settle any retained conflict, close out again), and `replay` answers `integration-resolution-planning-required`.

### Activation, The Waiting Queue And Sync

The closeout queue is disposable scheduling output: a projection that is rebuilt from the task
documents and the waiting closeout-door generations. A valid `task_doc` mutation is applied during
every closeout phase. After it publishes, the affected sprint projections are made non-admitting
(`invalid-empty`) and rebuild from task truth; a task write is never rolled back or delayed because
a closeout operation exists.

Atomic implementation admission belongs to one durable, replace-in-place activation record per
canonical series contract, with the states `vacant`, `reconciling` and `active`. The record carries
a fingerprint of its contract, so two atomic masters that share one protected source pair never
share this state: each tracks only its own transition from `reconciling` to `active`. Real wave
dependencies are the sprint execution graph's job, and task-document mutation never reads the
record.

A sprint without an `executionGraph` declares no dependencies, so nothing serializes its masters:
`resolve_scheduling_mode` returns the mode `atomic-sequential`, in which every commanded master
executes atomically whatever nature it declares. With a graph the mode is `dag`, and the declared
nature of each master rules.

`worktree_sync` is a resumable, contract-addressed transaction over both repository sides. Its
record is `reports/sync-operation.json` of the leaf's worktree group, and its commits are pinned by
Git refs. A sync that retains merge conflicts ends its automatic phase; the resolution actions are
`continue`, `cancel` and `reconcile`.

### Terminal Task States And Landing Routes

`DocStatus` has two terminal values, `Completed` and `abandoned`. `abandoned` records a decision,
not a failure: on a master it means that nothing of that master integrated, and on a master's row it
means that the leaf's work was not taken while the master still completed. The reason belongs to the
declaring operation's audit trail. `models/task_document.py` publishes
`RESOLVED_MASTER_ROW_STATUSES`. `tasks/readiness.py::master_is_terminal` is the judgement of a
terminal master that the task routes and the closeout queue read; the observer's graph projection
reads `RESOLVED_MASTER_ROW_STATUSES` and the master's status directly.

`worktree_record_landing` is the public tool for the pull-request route: a pull request lands on the
remote and never moves refs locally, so `worktree_integrate` cannot express it. Both routes record
the landing through `record_landed_integration` in `worktrees/modules/landing_record.py`.

### JSON-Primary Task Documents

The `agents_remember.tasks` package owns the schema, the renderer and the store of the
`ar-task-document/v1` document. Every write persists the JSON and its rendered Markdown atomically,
and the Markdown is never parsed back. The `task_doc` tool takes an operation, among them `create`,
`replace`, `set_status`, `set_step`, `append_decision`, `author_execution_graph`, `attach_master`
and `detach_master`. It authors `subTask` and `master` documents; a create with the kind `light` is
refused. A master takes `subTasks` and ordered sections instead of steps. The dashboard projection
reads every task document under `tasks/<repository>/<task>/`, with the lifecycle as optional
context, and projects a master both as a task document and on the series surface.

### Dashboard Serving Layer

The `agents_remember.serving` package is the dashboard's transport: a FastAPI app, launched by
`agents-remember dashboard`, that serves the observer projection. `GET /api/state` and the
server-sent event stream `GET /api/stream` serve the projection, `GET /api/events` the retained raw
events, and `POST /api/actions/{action}` the operator actions. The reducer owns the interpretation
of projected state. The server binds to `127.0.0.1` by default. `/api/terminal/{session}` and its
sub-routes host harness sessions: open, submit, rename, retire, terminate and the model and effort
controls, with a WebSocket on the same path for the terminal bytes.

The frontend is the root-level `dashboard/` project. Its built bundle ships as
`package_data/dashboard/`, placed there by `scripts/sync-dashboard.py`; the bundle is git-ignored,
and a checkout with no build answers `503` and names the build command. `--reload` on the dashboard
command is the development hot-reload mode, and `--sim` replays a recorded observer fixture through
the same serving path.

### Root Trees Outside The Path Rules

The canonical `skills/` tree, the `eve_runtime/` application and the other root runtime asset
folders are outside the include set of the path rules, so the census asks for no card of theirs. The
maintained cards of a skill are on its generated package copy under
`mcp/src/agents_remember/package_data/runtime/skills/`, which the rules cover. The root
`eve_runtime/` tree has no cards; the cards of the eve application are on its generated mirror
`mcp/src/agents_remember/package_data/runtime/eve-runtime/`, which `scripts/sync-runtime.py` writes
and which is never edited by hand.

The onboarding tree also holds cards and overviews under `onboarding/skills/` for files of three
root skill folders. No path rule covers their sources, so the census never asks for them. The
memory-quality run still checks them: it walks every Markdown file under `onboarding/`, these
included, and reports the state of their references.

## Development And Certification Policy

**Runtime.** The current source and wheels built from it admit every Python 3.14 release (`requires-python >=3.14,<3.15`); the managed development and CI runtime is pinned to the exact release 3.14.8 by `scripts/python-runtime-contract.env`, and the installer and the venv bootstrap select the interpreter binary from that contract's minor value. The published `3.0.0rc8` artifact is the historical Python 3.13 release. The runtime checker refuses any interpreter other than the pinned exact release with the named refusal before it can import a newer standard-library module.

Ordinary Python development runs `mcp/.venv/bin/python -m pytest`, which selects the unit population with four workers. `-m integration` selects the integration population and `-m ""` selects both. The root `pyproject.toml` declares the case budgets `unit_case_budget` and `integration_case_budget`; a run whose collected population exceeds a budget is refused. A new case protects a distinct user operation, a consequential failure or an actual regression, and overlapping tests are extended, consolidated or replaced before a case is added.

Coverage is diagnostic only: there is no mandatory percentage, no changed-line floor and no test obligation that follows from an uncovered line. CRAP is reported for production functions only, and its threshold of 20 is a review trigger, not a delivery blocker. Lint, formatting, typing, structural rules and test failures enforce. There is no score-exception registry, coverage ratchet or baseline mechanism.

Only the pinned Dagger graph and the lifecycle owners produce certifying evidence; ordinary pytest does not acquire that authority.

The Git hooks run `.githooks/_gate.sh` in two tiers. The `fast` tier (pre-commit) checks the staged content: the generated copies, Ruff lint, Ruff format, Pyright, the validator of the two test catalogs and the dashboard checks. The `targeted` tier (pre-push) repeats those checks without staging or stashing. Neither tier runs tests, and the `full` tier refuses a host run and names the Dagger command. When the working tree differs from the index, the fast tier first parks unstaged and untracked content with `git stash push --keep-index --include-untracked` and restores it on every exit with `git reset --hard` and `git stash pop --index`; it refuses to restore when the top of the stash moved meanwhile and prints the recovery command. During a merge, rebase, cherry-pick or revert it does not stash and checks the working tree as it is. The stash is shared by all worktrees of a repository, so a stash entry with the message `agents-remember pre-commit gate: staged-content isolation` belongs to a running or interrupted gate.

### Test Catalogs And Git Attributes

The two test catalogs, `mcp/tests/test-evidence-lanes.toml` (the lane of every test file) and
`mcp/tests/evidence-lifecycle.toml` (the governed test artifacts and their consumers), are kept in
one canonical form, and Git merges them as unions of both sides' added lines: the repository-root
`.gitattributes` declares `merge=union` for both files. A change that adds a test file adds one line
to its lane and runs
`python -m agents_remember_test_support.testing.evidence_lifecycle --project-root . --write`. The
command orders both catalogs, removes duplicate lines, sets the consumer list of an `exact` or
`exact-source` row to the set derived from the source tree when the tree shows a consumer, and
removes the list lines of files that no longer exist, except in a row none of whose listed consumers
exists: that row is left as written and named. It adds and removes no row, never assigns a lane, and
refuses, without writing, a catalog in a form it does not read. The same command without `--write`
validates both catalogs; the Git hook gate and the quality plan run it. Test selection reads both
versions of the lifecycle catalog through the same shared reader, so an invalid base-revision
catalog is refused by name instead of with a parser error. The module is importable
when `mcp/test_support` and `mcp/src` are on `PYTHONPATH`, which the hook gate sets.

A union merge can leave a line twice, leave a list out of order, bring back a line that one side
deleted, and interleave two rows that two changes added at the same place. Both loaders refuse a
duplicate line, a list or row that is out of order, a list that is not written one path per line
and the line of a file that no longer exists; a finding that the command repairs names the command.
A catalog that no longer parses is refused with the sentence that two rows may have been interleaved
and that the file is restored from the landed commit. The lane loader runs at every test collection.
The lifecycle loader runs in the validator command, in the selection graph and in a test of the
default unit run. No byte digest and no row count of a catalog is pinned.

`.gitattributes` holds two more entries. Generated dashboard chunks
(`mcp/src/agents_remember/package_data/dashboard/assets/*.js`) are exempt from the
trailing-whitespace check, because they can hold whitespace-only lines inside template literals. The
vendored tiktoken vocabulary file is marked `-text`, so no line-ending conversion can change the
bytes whose SHA-256 `mcp/src/agents_remember/models/tokens.py` checks.

## Memory Preparation And Final Certification

`memory_quality_check` prepares memory before certification admission and never changes code or memory. A full contract-scoped call replaces the one curator checklist at `reports/curator-memory-quality.md` of the worktree enclosure together with its `.json` attestation; subset and unscoped calls write neither. Every contract-scoped run publishes the structural census to `reports/memory-census.json`. The worklist needs no code-gate result and certifies no semantic decision. The run is bound to one candidate pair: the pair identity names the repository, the contract, the code and memory roots, the source and work branches, the base commits and the onboarding root, and its `contractDigest` covers those cells and excludes the ledger path.

Once the raw checklist is `ready-for-closeout`, the combined status `coherence-required` means that the caller prepares, publishes and validates the `curator_coherence` authority. `prepare` returns the code, memory, task-topology, attestation and predecessor identities and the source candidates. `publish` requires those identities unchanged, one judgment with disposition, rationale and evidence reference for every candidate, and the two delivery identities `semantic_requirement_revision` and `delivery_attempt`, which `prepare` does not derive. `validate` is the same validator that memory preflight and closeout admission use.

`memory_quality/final_certification/` is the final full memory-coherence certification (Gate 5 of the five-gate closeout certification): it certifies memory coherence over one exact code and memory candidate pair from the complete final catalog, the prerequisite of gates 1 to 4, the coherence record and the candidate-pair binding, and it never changes code or memory. The prepared-memory adapter refuses unless exactly four code terminals are selected. An interactive memory-quality run reports the same catalog with the items it cannot settle marked `blocked`.

A candidate tree is captured through a private index file: the tree is `HEAD` with every staged, unstaged and eligible untracked change applied, and the worktree's own index and files are never changed.

## Key Invariants

- **Nothing serializes a graph-less sprint.** A sprint without an `executionGraph` declares no
  dependencies; `atomic-sequential` says that every commanded master executes atomically, and
  activation is per canonical series contract.
- **One prompt queue per hosted bridge.** The submission authority is the only prompt queue; an
  adapter dispatches at once and never owns a second one.
- **The reducer is the single owner of interpretation.** The serving layer adds no interpretation to the projection it serves; it also records the operator's gate decisions and hosts the harness sessions.
- The `c-02-memory-quality-control` skill reports and routes memory quality work; it does not
  rewrite onboarding prose itself.
- No implementation begins before explicit developer approval, and implementation approval is not
  commit approval. A closeout apply records its authority: explicit developer commit approval, or
  delegated accepted-series authority.
- File-level onboarding is strictly one-to-one with source files.
- Route indexes are generated metadata, not hand-authored truth.
- Generated dashboard JavaScript can contain whitespace-only lines that matter at run time; only the
  shipped `assets/*.js` are exempt from the trailing-whitespace check.
- A generated copy is never edited directly: skills are edited under root `skills/`, runtime assets
  under their root folder, and harness starter files under `scripts/harness/`, each followed by its
  sync script.
- **Ruff enforces complexity; Radon only reports.** `C901`, `PLR0911`, `PLR0912` and `PLR0915` are
  enforced by Ruff with no baseline, and `radon` exits 0 whatever it finds. `PLR0913` is ignored by
  path for the MCP registration modules, and some functions carry a `# noqa` for `PLR0911`,
  `PLR0913` or `PLR0915`.
- **No ratchet and no baseline.** There is no score-exception registry, coverage ratchet or baseline
  mechanism. `AGENTS.md` asks that a complexity finding be cleared by changing the code, not by a
  `# noqa`, a per-file ignore or a widened limit.
- **Scope is derived from the tree.** The quality wrapper and the hook gate take their Python scope
  from `git ls-files`, and the hook gate refuses an empty scope.
- **`run_git` is the package's Git runner.** `kernel/git_command.py::run_git` gives the child
  `stdin=DEVNULL` unless input text is passed. `install/experiment.py` and `mcp/tools/knowledge.py`
  call `git` through `subprocess.run` directly.
- **Token counting needs no network.** `models/tokens.py` reads the vendored vocabulary and checks
  its SHA-256 itself before it hands the file to tiktoken, because tiktoken answers a hash mismatch
  by deleting the file and downloading a replacement. A missing or damaged vendored file raises
  `TokenizerVocabularyError`.
- **A staged gate stages first, and only in a task worktree.** The staged-quality preparation
  refuses a checkout whose Git directory is the repository's own, and an index with conflicts; it
  then resets the index and stages the whole worktree, so a retry cannot carry paths from a refused
  attempt.

## Glossary Terms

| Term | Meaning | Notes |
| --- | --- | --- |
| onboarding card | The Markdown note of one source file, at the mirror path of that file under `onboarding/`. | On converted memory a card with references has a JSON sidecar that holds the references and the realization entries; the sidecar of a test file also holds proof entries. |
| entity fingerprint | A deterministic `git-blob-set-v1` hash over the curated evidence paths of an entity in `entities.md`. | The `c-05-create-or-update-onboarding-files` skill chooses and refreshes the paths. |
| coordination context | The roots and settings that the `c-08-ar-coordination-context-resolver` skill resolves for a code repository. | Among them `code_repository_root`, `coordination_root`, `memory_root`, `task_root` and `temp_root`. |
| pathRules | The include and exclude rules in `system/settings.json` that decide which source paths have onboarding. | At the onboarding gate a changed file outside the rules raises no item for a card of its own; it still raises the item of its nearest governing overview. |
| drift report | The report of a drift check. | It is written under `drift-reports/` of the temporary root. |
| memory quality check | The MCP tool that runs the memory checks and writes the curator checklist. | On converted memory it reports the knowledge validator, the worklist and the gate verdict. |
| knowledge gate | The mandatory check of a leaf's closeout on converted memory: validator, onboarding gate and change-to-knowledge worklist. | The closeout preview answers `knowledge-gate-refused` when it refuses. |
| worktree contract | The `series-contract.md` of a master (at the task root) or of a leaf (under `enclosures/<leaf-id>/`). | The parser and writer are in `mcp/src/agents_remember/worktrees/worktree_contract.py`. |
| worktree integration | The phase that lands closed task work on its source branches. | When a source moved, `ff-only` answers `blocked-non-ff` and asks for a sync and a new closeout, `replay` answers `integration-resolution-planning-required`, and neither creates a replay commit. |
| memory baseline adoption | Adopting existing external-memory onboarding as the first Git-attributed baseline. | The `c-10-adopt-memory-baseline` skill checks drift first. |
| runtime AGENTS template | An `AGENTS.md` source under `agents-md-files/`. | The templates are coordinator, skills, system and tasks. |
| MCP runtime settings | The settings file outside the coordination root that the MCP server and the dashboard load. | It names `coordinationRoot`, `workspaceRoot`, `transcriptRoot`, the repositories, the providers and the timeout caps. |

## Evidence

Onboarding cites files of this repository for repository behavior. A citation is source evidence,
not a recorded test execution.

- The source checkout separates installed-runtime work from work on this repository and keeps implementation approval separate from commit approval. [33]
- Repository instructions define certifying delivery, enforcing checks, and diagnostic-only coverage and production CRAP. [34]
- The docs index owns the start-here, install, operational and reference map. [35]
- Runtime asset sync treats the root runtime folders as canonical and has a check form. [36]
- GitHub runs the deterministic non-test gate on pull requests only; tag publishing proves reachability from main. [37]
- The staged-quality owner prepares the staged candidate, runs the targeted quality gate and requires published evidence for exactly that tree. [39]
- Contributor guidance separates host feedback from Dagger-owned certifying evidence. [40]
- Development commands, budgets, diagnostic metrics and isolation. [44]
- Certifying publication and accepting consumers. [45]
- Exact contract scope, the full check and the curator worklist publication. [46]
- The interactive catalog names missing authority without eligibility. [47]
- The final memory adapter requires the selected four-code-terminal prefix. [48]
- Git attribution is the source of the consumer ledger. [50]
- Closeout writes or reuses one memory-content output; on converted memory it first closes the leaf's history file and validates and gates the exact tree. [51]
- Integration proves exact memory source ancestry independently of cache rows. [52]
- The order declares `certification` between `models` and `controlplane`. [31]
- The layering checker loads that one contract, rejects undeclared package directories and reports an invalid dependency direction. [32]
- Text files in the memory repository are the source of truth for knowledge. [19]
- The curator file writer refuses a memory tree that is not converted. [22]
- The mounted `knowledge_change` tool refuses and names the write route. [30]
- The hand-off template's file-writer section. [21]
- The hand-off template's admission rule for new records. [9]
- The hand-off template's decision-record section. [6]
- The hand-off template's family-routes subsection. [23]
- The retrieval skill's paragraph on the family-complete read of a path. [8]
- The retrieval skill's paragraph on the families of the route chain. [4]
- The retrieval skill's route for continuing a bounded page through `knowledge_read`. [14]
- A converted memory tree is selected as a tree, and the database file inside it is not read. [25]
- The ordinary paired read carries the published intent block. [61]
- Proofs are read back for the invariant and family views, and the invariants without proof are listed. [18]
- A changed source file's card and its governing overview need a counted change or a history row. [16]
- The curator role's step for converted memory. [68]
- The three attribute entries and their reasons. [69]
- The rewrite that the `--write` command runs. [70]
- The command entry: validation of both catalogs on one source graph, or the rewrite. [71]
- The converted-card workflow of the `c-05` skill. [67]
- The worktree skill's paragraph on how the finalizer derives a leaf's master. [1]
- The page threshold of a knowledge read. [73]
- The cutover lock refuses an unconverted memory line and names the crossing sync. [74]
- The closeout preview asks the mandatory gate and answers with the refusal when the gate refuses. [75]
- The two declared case budgets. [76]
- The scheduling mode of a sprint without an execution graph. [77]
- The statuses that resolve a master's row. [78]
- The runtime asset targets, with the eve application as a generated mirror. [80]

- The MCP settings example: coordination root, workspace root, transcript root, repositories, providers, timeout caps, and the dashboard, provider-degradation and retirement settings. [42]
- The judgement of a terminal master that the task routes and the closeout queue read. [79]
- The supported memory modes and the refusal of the removed one. [83]
- The three retrieval substrates. [84]

- The role-capsule router's selection rule and its unsupported-field refusal. [85]

- Dispatch is one transaction with two caller kinds, and a plane refusal never falls back to ambient. [86]
- Closeout is worktree-only, and the apply records its authority. [87]
- The branch-addressed landing of a leaf without its own enclosure. [88]
- The pause releases one master's activation selection and publishes nothing. [89]
- The activation record is one replace-in-place snapshot per canonical series contract. [90]
- Where the record of a sync transaction lies. [91]
- The locations of a master's contract and of a leaf's enclosure contract. [92]
- An external-memory start requires the memory repository and its source branch and creates the worktree. [93]
- A moved source blocks `ff-only`, and `replay` asks for a resolution instead of creating a replay commit. [94]
- Gate enforcement: a model-decided approval does not satisfy it, and a lifecycle without a gate of the kind is gateless. [95]
- The retention of inbox rows and the approval kinds whose applied snapshot is an authority record. [96]
- The roles of each task altitude; a reviewer sits on a leaf, master or sprint document. [97]
- The task tool refuses to author a light document. [98]
- Under a sprint without a graph every commanded master executes atomically whatever it declares. [99]
- The mutation classes that invalidate the closeout queue projection. [100]
- The observer's graph projection reads the resolved row statuses directly. [101]
- A review comparison on converted memory is four Git trees pinned by refs. [102]
- The route rules are reported inside the writer and refused by every commit route. [103]
- The file-writer route of the two commands and the crossing route. [104]
- The worklist kind for an invariant that was already stale at the base. [105]
- The host-scoped provider setup lock. [107]
- The data roots of the two provider databases. [108]
- The GrepAI clone has a stall watchdog and no total-time cap. [109]
- The CodeGraphContext seed export is bounded by the provider-setup cap. [110]
- The states of the CodeGraphContext graph probe. [111]
- The GrepAI indexing states. [112]
- The carryover target, its candidate kinds and its refusal of converted memory. [143]
- The submission authority is the only prompt queue. [114]
- A repeated request id is idempotent only with the same source and payload. [115]
- The opener is the one spawn path of the dashboard and of internal dispatch. [116]
- The serving layer is transport over the observer projection. [117]
- The dashboard records a lifecycle gate decision through the control plane. [118]
- The gate responder posts a response to the inbox, except for an adapter interaction. [119]
- The serialized model-and-effort change. [120]
- The dashboard bundle placement, its freshness proof and its check mode. [121]
- The hook gate's tiers. [122]
- The fast tier parks unstaged and untracked content and restores it on every exit. [123]
- The fast tier's checks, with the validator of the two test catalogs. [124]
- The staged-quality preparation refuses a checkout that is not a task worktree, then resets and stages. [125]
- A candidate tree is captured through a private index. [126]
- The pair identity of a memory candidate and what its digest covers. [127]
- The final full memory-coherence certification. [128]
- The charters of the certification and control-plane packages. [129]
- Ruff's complexity rules and the one per-file ignore. [130]
- The Git runner gives the child no standard input unless text is passed. [131]
- The vendored vocabulary is verified before tiktoken reads it. [132]
- The task workflow creates the requirement corpus before the task document. [133]
- Requirement revisions and delivery attempts are separate. [134]
- The start-of-task onboarding trust gate. [135]
- The templates that the runtime install places in the coordination root. [136]
- The launcher seam: AR resolves the role hierarchy, task capsule and report scope, Paseo owns the agent session, and the receipt updates no AR state. [137]
- The reader config of a call that carries a task context comes from the leaf's admitted enclosure. [138]

- The subcommands of the `agents-remember` command. [139]
- The lane loader refuses a catalog that is not in canonical form. [140]
- The lifecycle loader refuses a catalog that is not in canonical form. [141]
- Launch-capable provider operations re-read the providers map from disk. [142]
