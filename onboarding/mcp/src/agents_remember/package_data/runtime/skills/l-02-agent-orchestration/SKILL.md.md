# l-02-agent-orchestration/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-04T13:03+02:00                      |
| lastVerifiedCommitHash | `5ab7550b256fe4cd82514b81f455aa9026c0d7de` |
| lastVerifiedCommitDate | 2026-07-04T13:10:34+02:00|

## Purpose

This file is the entry contract for the `l-02-agent-orchestration` skill — **the frame**: the
developer-invoked, never-self-spawning runtime that houses the five orchestration-family jobs
(designer, orchestrator, manager, worker, adversarial reviewer). It is not an executor and not a job
itself; it guarantees only the thin contact points every housed job shares — **context → job selection
→ housed job execution → wrap-up** — and lets each job's own flow take over from there. `SKILL.md`
carries the frame doctrine plus the shared runtime conventions (the job registry, the coordination-leaf
convention, the escalation ladder, the two adversarial seams, the gate-delegation doctrine, the knob
block + per-harness variant resolution, the settings.json orchestration schema block, the full super
integration branch topology, and the credits) so an agent entering at any seat gets the whole runtime
contract from the entry file, with each seat's meat deferred to `jobs/<role>.md`. The topology now
spells out the strict branch stack (super from main, masters from super, leaves from masters), C-11 as
the universal integration mechanic, the orchestrator's master-to-super worktree flow, the two conflict
resolution modes, leaf-move decision-log duties, the memory-ledger invariant, and the sequenced
260630-derived follow-ups.

## Code Commentary

### Logic

This packaged file is a sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
`skills/l-02-agent-orchestration/SKILL.md`; the authored skill source owns the wording, and this is the
synced runtime mirror the installer ships.

The skill frames orchestration as a **container/runtime**, decomposing the historical "Eierlegende
Wollmilchsau" build lifecycle (one implicit role doing a bit of everything minus orchestration, the
developer wearing the orchestrator + manager hats) down to thin **contact points**: `context → job
selection + execution → wrap-up`. The FRAME model on the FlowTab canvas
(`dashboard/src/panels/flowModels.ts`) — together with the `designer`, `orchestrator`, `manager`,
`worker`, `reviewer`, and `comms` models — is the behavioral spec this skill and its job files
implement.

- **Entry rule.** The frame is the **single entry point** into the orchestration runtime, entered
  **only** on an explicit developer request; no job self-spawns into it and no agent promotes itself
  into an orchestrator or manager seat. The developer talks to **one orchestrator** as the single
  point of contact (design decision D15); managers and workers stay reachable via their attached chats,
  but the standing relay is developer ↔ orchestrator.
- **Contact Point 1 — Context (trust checkpoint).** Every session at any seat runs the same trust
  checkpoint the `l-01-session-job-lifecycle` skill owns (`context_packet` with `include_providers`,
  `include_drift`, `include_freshness`; memory/provider trustworthiness a precondition). The frame adds
  nothing but **guarantees** the checkpoint runs identically for every seat; `lifecycle_start` promotes
  the fleeting lifecycle as in the single-session case.
- **Contact Point 2 — Job selection (profile-fit).** A two-step check against the **job registry**:
  (1) which job? — the request + the coordination-leaf role marker name the seat; (2) profile-fit? —
  compare the session's harness/model/effort to the job's resolved knob block. **Wrong profile → a
  takeover spawn**: `spawn_agent_session(<role>)` on the correct profile, handing the successor a
  **conversation-handover packet** (`templates/conversation-handover-packet.md`) so it onboards from
  **state, not the transcript**. The one handover-packet schema serves master handover, role takeover,
  and worker respawn alike. `spawn_agent_session` is the orchestration spawn tool authored in **leaf
  L2** of this series — **not yet implemented**; until L2 lands, every reference is the *contract* a
  takeover/dispatch will call, and the frame owns the doctrine of the spawn seam, not its
  implementation.
- **Contact Point 3 — Housed job execution.** The job file's own flow takes over; the frame guarantees
  only the sockets it plugs into (observability, gates, escalation, durable artifacts) and carries the
  runtime conventions below.
- **Contact Point 4 — Wrap-up.** The durable artifact is written, the work lands per the **job's own
  path**, and `lifecycle_end` records the terminal state; continuity always lives in the `task_doc` +
  durable artifacts, never in the transcript — which is why short-lived workers/reviewers are safe.

Runtime conventions carried inline by `SKILL.md`:

- **Coordination-leaf convention.** Coordination seats are ordinary `subTask` **leaves with no
  enclosure** (no worktree, no schema change) distinguished by a **role marker**. The **first
  coordination leaf of the series = the orchestrator seat** (worktree-less at rest, but it acquires an
  orchestrator worktree to integrate a master into super); **one coordination leaf per manager**; work
  leaves are unchanged (each gets its own enclosure/worktree). The series is scaffolded via `task_doc`
  in that order.
- **Escalation ladder.** **worker → manager → orchestrator → developer**, no level skipped; each level
  resolves within its own view first, and only a stumped orchestrator raises to the developer. The
  **spirit test governs autonomy at exactly one rung, the orchestrator, and only there** (design
  correction 2026-07-04) — managers/workers get no creative-liberty prompting in either direction; the
  default agent behavior stands and any plan delta beyond blank-filling escalates.
- **Two adversarial review seams.** Adversarial review spawns at **exactly two seams** (developer
  decision 2026-07-03), never per-leaf: **master-exit** (before a manager hands its master to the
  orchestrator) and **super-exit** (before the orchestrator hands super to the developer). Each spawns
  an `adversarial-reviewer` over three lenses (completion vs docs · code quality per `system/tools.md`
  · onboarding-vs-code = paired `read_ar_files` + `memory_quality_check` + drift); the verdict is a
  templated artifact (`templates/verdict.md`) that attaches to the handover gate as **evidence, never a
  decision**, and a blocking verdict must decompose into fix leaves.
- **Gate-delegation doctrine (enforcement is L4).** Leaf plan/closeout gates become **delegable to a
  configured role**; the invariant is sharpened, not weakened — *the owning agent never self-approves; a
  distinct, configured role may.* Delegated decisions are **attributed** (`decidedBy: <manager
  lifecycle>`, `decidedVia: orchestration`) and dashboard-visible; human review concentrates at the
  master/super integration branch (+ push). The skill **describes** this doctrine but **does not enforce
  it** — the kind-generic gate policy, the judge rung, and the delegation attribution are implemented in
  **leaf L4**; until L4 lands, gates behave as `l-01-session-job-lifecycle` defines them.
- **Knob block + per-harness variant resolution.** Job files are model-interpreted markdown, never an
  executor (borrowed D6). Each carries a portable **knob block** (harness/model/effort/tools — D7) the
  terminal host injects at spawn. Resolution order (borrowed D12): `jobs/<R>.md` (portable base)
  overlaid by `jobs/<R>.<H>.md` (harness variant) overlaid by the settings.json orchestration block. A
  variant carries only what is harness-specific and never restates the role's duties; two exemplars
  ship (`jobs/orchestrator.claude-code.md`, `jobs/worker.claude-code.md`).
- **settings.json orchestration block (SCHEMA DOC ONLY — parsing deferred to L4).** Machine/user
  overrides layer **over** the job-file defaults, in the MCP authority settings file (not the memory
  `system/settings.json`); precedence job-file defaults < settings.json. The block documents
  `orchestration.roles.<role>` knob overrides, `orchestration.concurrency.*` caps (`maxParallelMasters`,
  `maxParallelLeaves`, `maxSubAgents`; `0` = unlimited per the `timeoutCaps` convention), and
  `orchestration.gateDelegation` as a **pointer** to the L4 gate policy. Nothing in this skill reads it
  yet.
- **Comms protocol.** Three composing channels (inbox = durable queue via
  `operator_inbox_post`/`_poll`/`_consume` generalized to agent→agent addressing; stdin push = delivery
  via echo-confirmed paste; turn-report artifacts = reporting), plus nudging on trustworthy inactivity
  signals. The comms substrate is implemented in **leaf L3**; the skill describes the protocol it
  realizes.
- **Super integration branch topology.** An **accumulative** super integration branch owned by the
  orchestrator: super bases from `main`, master integration branches base from the current super tip,
  and leaf branches base from their owning master branch. **C-11 is the universal integration mechanic
  at every level** (leaf -> master, master -> super, super -> main), and every edge carries memory so
  the ledger maps the accumulated code commits. The orchestrator dependency-orders managers from the
  master DAG, integrates each completed master into super from an orchestrator worktree sourced at
  super, and only then releases downstream masters. Independent masters may run in parallel and
  reconcile against a moved super base. Conflict resolution has exactly two modes: up-front
  foundation-master extraction when overlap is visible during streamlining, or post-hoc code dedup plus
  memory single-siding on the super worktree. Not-yet-started leaf moves are real moves with
  decision-log entries on both affected masters. The 260630-derived master finalize/archive and
  parallel-master reconcile primitives remain sequenced follow-ups; until they land, the orchestrator
  performs those edges manually with existing C-09/C-11 primitives and records them in durable notes.
- **Credits.** Vocabulary/structure adopted from the parked `260619_agentic-control-plane` spec (D6,
  D7, D10, D11, D12, the judge rung, short-lived workers with structured handoff, the orchestrate lens,
  D15), which in turn credits **Archon** and the **agent-control-plane** project for the orchestration
  vocabulary (D14); that credit carries forward here.

### Conventions

The frontmatter `name` is lowercase (`l-02-agent-orchestration`) so the flat-layout installer accepts
it, and the skill directory uses the same lowercase ID. The skill is multi-file like the
`w-02-light-task-workflow` skill: the frame stays deliberately thin in `SKILL.md`, and the payloads live
in companion `jobs/<role>.md` files (with optional `jobs/<role>.<harness>.md` overlays), reusable
artifact shapes in `templates/<name>.md`. The lens vocabulary continues the `l-01-session-job-lifecycle`
job lenses (research · triage · bug · feature): "spine unchanged, lens specializes" (borrowed 260619 S8)
— a housed job still runs the ordinary build spine, the lens tunes it, it does not fork it. The skill
extends — never replaces — the coordinator `AGENTS.md`, the `l-01-session-job-lifecycle` skill, the
`w-02-light-task-workflow` skill, and the memory layer.

### Invariants And Boundaries

The frame is entered only on an explicit developer request and is never self-spawning; it is the single
entry point into the orchestration runtime. Every session at any seat runs the same trust checkpoint
before trusting analysis. The developer talks to one orchestrator (single point of contact). A wrong
profile forces a takeover spawn with a conversation-handover packet, so successors onboard from state,
not the transcript. Coordination leaves are enclosure-less `subTask` leaves with a role marker; the
first is the orchestrator seat, one per manager, work leaves unchanged. The escalation ladder skips no
level, and the spirit test is orchestrator-only — do not port it down the ladder. Adversarial review
spawns at exactly two seams; a verdict is evidence, never a decision, and a blocking verdict decomposes
into fix leaves. The owning agent never self-approves a gate; a distinct configured role may, with
attribution. Continuity lives in the `task_doc` + durable artifacts, never in the transcript. Two
capabilities are **contract only** in this skill: `spawn_agent_session` (implemented in L2) and gate
delegation + the settings.json orchestration block parsing (implemented in L4); the comms substrate is
implemented in L3. The L5 topology doctrine is live skill text, while the master finalize/archive and
parallel-master reconcile primitives named by the doctrine stay sequenced backlog until their
task-doc-tooling leaves land.

### Todos

No current todo is recorded in this skill file. The deferred implementations (spawn tool L2, comms L3,
gate policy + settings parsing L4, full topology L5, adversarial reviews L6, orchestrated pilot L7) are
tracked as the series' downstream leaves, not as in-file todos.

### Docs References

No external domain documentation applies to this repository-local orchestration skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

`l-02-agent-orchestration` is the multi-agent runtime a whole series runs inside; it sequences the
housed job files, builds on the `l-01-session-job-lifecycle` build spine, and scaffolds the series in
the `w-02-light-task-workflow` task format.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `SKILL.md` is the frame; each housed job's flow lives in its own `jobs/<role>.md` payload, resolved by profile-fit against the job registry. | L24-L52; L79-L114 | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/SKILL.md) |
| The orchestrator job owns the portfolio, dependency-ordered dispatch, the super integration branch, and the orchestrator-only spirit test. | n/a | [jobs/orchestrator.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/jobs/orchestrator.md) |
| The L5 topology doctrine defines the super/main/master/leaf branch stack, C-11 at every edge, dependency-ordered dispatch, orchestrator worktree integration, conflict modes, leaf-move logs, ledger mapping, and the sequenced 260630 follow-ups. | L263-L358 | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/SKILL.md) |
| The Claude Code overlay carries the sub-agent fan-out mechanic (durable reports; AR mutations stay in the main loop) on top of the portable orchestrator job. | n/a | [jobs/orchestrator.claude-code.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/jobs/orchestrator.claude-code.md) |
| Every housed job's trust checkpoint and build spine are the `l-01-session-job-lifecycle` skill's; the frame only guarantees the checkpoint runs identically at every seat. | L69-L77 | [l-01 SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/SKILL.md) |
| The series is scaffolded in the `w-02-light-task-workflow` task format, which the frame extends rather than replaces. | L342-L347 | [w-02 SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this repository-local orchestration skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-04T13:03+02:00 — 260703-L5 expanded the frame's super integration branch topology from a
  summary into doctrine: super branches from main, masters branch from super, leaves branch from their
  master, C-11 is universal at every edge, dependent managers dispatch only after dependencies
  integrate into super, independent masters reconcile a moved super base, master-to-super integration
  runs in an orchestrator worktree, conflict resolution is either up-front foundation-master extraction
  or post-hoc super-worktree dedup with memory single-siding, leaf moves carry decision-log entries,
  and the final super-to-main PR includes main-memory carry-over plus push. Also recorded the
  260630-derived master finalize/archive and parallel-master reconcile items as sequenced follow-ups,
  not implemented behavior. Verification metadata pinned until closeout stamps the L5 commit.
- 2026-07-04T11:00+02:00 — Created file-level onboarding for the new `l-02-agent-orchestration` skill
  (leaf 260703-L1), the developer-invoked, never-self-spawning frame that houses the five
  orchestration-family jobs via the four thin contact points (context → job selection → housed job
  execution → wrap-up). Captured the frame doctrine, the job registry, the coordination-leaf
  convention, the escalation ladder + orchestrator-only spirit test, the two adversarial seams, the
  gate-delegation doctrine (enforcement deferred to L4), the knob block + per-harness variant
  resolution, the settings.json orchestration schema block (schema doc only; parsing deferred to L4),
  the super integration branch topology summary (full topology owned by L5), the comms protocol
  (substrate implemented in L3), and the credits; noted `spawn_agent_session` is the L2 tool (not yet
  implemented). Sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
  `skills/l-02-agent-orchestration/SKILL.md`. Verification metadata pinned until closeout stamps the L1
  commit.
