# l-01-agent-lifecycles/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-09T12:04+02:00 |
| lastVerifiedCommitHash | `04f78993c54ef6f98773b0208e66e97d19686be8` |
| lastVerifiedCommitDate | 2026-07-09T12:35:59+02:00|

## Purpose

The spine of the unified `l-01-agent-lifecycles` skill: lifecycle and job are ONE entity (one lifecycle per agent type). This file is the router + the minimal frame + the shared invariants; the per-role lifecycles live in `roles/`, the lenses in `lenses.md`, the report templates in `templates/`. It supersedes and replaces BOTH `l-01-session-job-lifecycle` and `l-02-agent-orchestration` (converged 2026-07-05, series 260703-L9).

## Code Commentary

### Logic

Sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical `skills/l-01-agent-lifecycles/SKILL.md`. HFX-L6 adds the **architect** as the developer-facing owner seat and reframes the **orchestrator** as a spawned backend seat; L6R3 adds **curator** as the dedicated onboarding writer. The router still has exactly three conditions, in order: (1) `AR_SPAWN_ROLE` env set -> run `roles/<value>.md`; (2) a fresh-session role brief -> run that role; (3) otherwise the session is developer-facing -> run `roles/architect.md`. Solo hat-collapse belongs only to the architect. The minimal frame is the only shared machinery: the six `lifecycle_*` signals, fleeting->persistent promotion at `worktree_start`, `awaiting-developer` auto-resume on the next AR call, server-side identity; a spawned role that never touches mutating AR tools never instantiates a lifecycle (designed shape), and a spawned role never adopts its spawner's lifecycle - the session<->leaf association is the catalog binding via the QUALIFIED leaf key `<repository>/<master>/<docId>`. Shared invariants: continuity in task_doc + durable artifacts (never transcripts); the escalation ladder worker -> manager -> orchestrator -> architect -> developer with no rung skipped; role-seat immutability for dashboard-owned sessions (roles expand horizontally into new chats, sub-agents drill vertically inside one seat); the manager -> builder -> reviewer -> curator leaf closeout chain; and the minimal decision-item relay over the existing operator inbox (one item at a time: decision/options/consequences/evidence refs, with a durable ruling back). Also carries the knob-block resolution (role-file defaults < global agentic settings < repo-local settings — since 260703-L13 the settings home is the GLOBAL agentic settings file `<coordination-root>/system/settings.json` with `<code-repo>/system/settings.json` overrides, not the MCP authority file), the as-built settings documentation (`orchestration.gateDelegation` parsed + enforced by `controlplane/gate_policy.py`, boot-snapshot from the global file with a one-cycle warned authority fallback; `roles`/`concurrency`/`spawn`/`loops` PARSED per-use by `kernel/agentic_settings.py` — the backlog closed; `spawn_agent_session` resolves spend settings as repo-local level override > global level override > repo-local role default > global role default > detection-gated; legacy caller-supplied harness/model/effort, direct launch/session controls, spawn model/effort env, and harness-native spend/endpoint env keys refuse with `spend-override-unsupported`; since 260703-L16 the resolved knobs are APPLIED at the harness boundary: model/effort ride `AR_SPAWN_MODEL`/`AR_SPAWN_EFFORT` env AND map onto the launch argv per-harness via the effective registry, unknown effort values REFUSE at dispatch naming the harness's vocabulary (claude's two-vehicle set incl. the session-level `ultracode` delivered as a post-launch `/effort` paste), the free-form escape hatch (`launchArgs`/`promptKeywords`/`sessionCommands`) is settings-owned, never validated, and only recorded in spawn provenance, `orchestration.rolesPerLevel` expresses per-LEVEL agent sets, and `orchestration.harnesses` teaches new TUIs / pre-customizes builtin launches — manual `docs/reference/harnesses.md`; example harness ids are registry ids claude/codex), a 6-line super-branch orientation diagram (the full topology's single home is `roles/orchestrator.md`), and the credits lineage (260619 spec -> Archon / agent-control-plane).

As of the L8 de-harnessing pass there are deliberately NO per-harness role files (developer decision 2026-07-05): knob resolution is role-file defaults < settings.json orchestration block (the variant layer is gone), harness ABILITIES are capability-conditional doctrine inside the portable files, and harness PREFERENCE is deployment configuration in settings. As of HFX-L6/L6R3 the registry lists EIGHT portable role files — architect, orchestrator, designer, strategist, manager, worker, curator, reviewer — with the strategist row still spawn-first and mandatory before any orchestrated run, the curator row dedicated to fresh per-leaf onboarding writes, and the reviewer row extending to the loop-reviewer seat (the two seams AND any three-party loop's review, criteria catalogs bound per review type).

As of 260707-HFX-L7 (provider degradation protocol) the registry grows to **NINE** portable role
files: a new `system-specialist` row is inserted after `curator` and before the adversarial
reviewer — "backend provider-degradation investigator; report first, fixes only after explicit
orchestrator order; spawn value `system-specialist`" — pointing at `roles/system-specialist.md`.
The frontmatter `description` and the "Companion Files" sentence are both updated in lockstep
("architect, orchestrator, designer, strategist, manager, worker, curator, system-specialist,
adversarial reviewer" / "the nine self-contained role lifecycles"), so a reader scanning either
the frontmatter or the companion-files footer sees the same count as the registry table. The
shared-invariants escalation-ladder bullet, which previously stated only the single chain
`worker -> manager -> orchestrator -> architect -> developer`, now carries a second clause for the
new seat: "worker → manager → orchestrator → architect → developer; system-specialist →
orchestrator" — `system-specialist` is NOT inserted into the main worker-ladder chain (it never
sits between manager and orchestrator in the normal build sense); it is a standalone one-rung
escalation like the designer/reviewer/strategist rungs documented in
`controlplane/orchestration_artifacts.py`'s `_ROLE_ESCALATION` map. The as-built settings-block
worked example (`orchestration.roles.<role>`) gains a `system-specialist` entry
(`{"harness": "claude", "model": "fable", "effort": "high"}`) alongside the existing
architect/strategist/reviewer/curator/worker rows, giving the reader a concrete spawn-knob shape
for the new role rather than only the registry mention.

As of 260703-L12 the file is also the **three-party-loop doctrine's single home** (a new section between Shared Invariants and the knob block, referenced per seat): OWNER → BUILDER → REVIEWER at every level that owns work (leaf/master/portfolio table); complexity-scored tiers at dispatch (direct / builder-verified / full loop, scored on blast radius · novelty · size; round 2 glosses direct as no-loop-machinery through the level's ordinary build channel — hands-on at session scale, the leaf's worker under a manager — so it cannot read manager-implements; a master whose leaves all score direct = workflow-free manager); the HARD 3-round cap where ONLY full end-to-end rounds count (delta-verifies by the SAME reviewer close rounds; fix rounds resume the SAME builder); the CONVERGENCE rule (every round must shrink the finding set — a non-shrinking round escalates immediately; the cap is the backstop); escalation one seat up the ladder with the full round history attached; the written QUO-VADIS criterion (a high-blast-radius truth escalates immediately; presentation-grade never); the criteria-catalog binding (`criteria/` — code-seam · doctrine · onboarding-memory · report-verification · plan-review) and the per-level agent sets (knobs in `orchestration.loops`, schema in `docs/reference/settings-json.md`, stored in the global agentic file with repo-local override and parsed by the kernel loader since L13 — the strategist's mandatory pre-run is doctrine, not a knob).

As of 260707-HFX2-L5 (doctrine inversion: active vigilance → passive process-and-ack) the Shared
Invariants section gains a new "Notify-and-stop is safe by design" paragraph right after the
lifecycle-adoption sentence: ending a turn on `lifecycle_turn_end_notification`, or simply stopping
once the artifact is written and nothing is pending, is never a liveness gap, because the HFX2-L2
supervisor sweep evaluates every expected artifact/signal on its own mechanical tick and the
HFX2-L4 escalation ladder (renudge → skip-level → developer attention, then respawn) handles
inactivity. The paragraph states the **watcher ban** in the same breath (uniform-mechanism ruling
2026-07-07: no role watches, polls, or nudges on its own initiative — that is a banned seat-local
mechanism) and the inversion this leaf drives through every role file: **every role's own liveness
duty inverts to passive** — be woken with pending signals, process and ack every item, then end the
turn. This is the doctrine's canonical home for the literal phrase "notify-and-stop"; it did not
appear anywhere in this skill before this leaf. The role files this doctrine touches
(`roles/manager.md`, `roles/orchestrator.md`, `roles/worker.md`) and the mandatory
`templates/turn-report.md` artifact each carry their own matching inversion, documented in their own
sidecars.

As of 260707-HFX2-L6 the router carries three linked doctrine corrections. First,
Developer-Declared Task-Seat Takeover: when the developer says "you are the
orchestrator/manager/worker for task X", the named task leaf is the seat. The agent opens the
named task doc first, resolves the qualified leaf key `<repository>/<master>/<docId>`, uses the
dashboard terminal catalog session id (not `CLAUDE_CODE_SESSION_ID` or `CODEX_THREAD_ID`), calls
`attach_terminal_session_to_leaf`, renames the session to the expected seat label, and verifies the
terminal catalog/dashboard row before continuing lifecycle work. Second, Developer Clarification
Triage: during an active task, close/current/small developer clarifications that fit the same
doctrine or code path are implemented in the current leaf instead of downgraded into future notes;
future/larger/unclear items are queued or clarified with the developer. Third, Delegated Series
Authority: once the developer accepts an orchestrated series/portfolio plan, managers and the
orchestrator govern subordinate closeout, integration, finalization, and cleanup under that
standing series authority, while final super/PR-carryover, raised human-pinned gates, scope changes,
red checks outside scope, and quo-vadis decisions still stop for the developer. This is operational
doctrine only; no runtime attachment behavior changed in this leaf.

As of 260707-HFX-L11 (curator activation, R1/R4) the Companion Files `templates/…` list gains
`curator-brief` — the first dedicated curator dispatch-pack template
(`skills/l-01-agent-lifecycles/templates/curator-brief.md`, new file), documented as: `ROLE BRIEF —
curator`; the manager compiles a curator's session start from it, feeding the leaf's landed change
set + task doc + notes/ — never spawned before builder code and the reviewer verdict exist. Before
this leaf the curator role file (HFX-L6/L6R3) had no matching template, so "change-set feeding"
was a doctrine sentence with no concrete brief shape; this closes that gap the same way
`worker-brief.md`/`manager-brief.md` closed it for their seats.

As of cycle 4 the router decides its edge cases in writing (unresolvable AR_SPAWN_ROLE falls through to the brief; a briefless role-env session announces itself on the inbox and waits; AR_SPAWN_ROLE=orchestrator is takeover-only), the brief header form is canonical (`ROLE BRIEF — <role>` or a templates/*-brief.md shape), the hat/seat exception to the no-cross-reading rule is stated, the reviewer registry row carries spawn value `reviewer` -> roles/reviewer.md, the six lifecycle signals are enumerated by name, the dead variant rung is gone from the precedence line, and the as-built settings text documents the wired requireReviewerVerdictAtSeams + the named policy routing the handover to the orchestrator.

As of cycle 5: the takeover pointer names the real section (Profile check (takeover), The Event Loop); the no-cross-reading exception says 'above'; the capability paragraph states the spawn-as-fan-out backdoor (DBMS principle). As of cycle 7 the Companion Files template registry lists all nine on-disk templates: `manager-brief` joins the line with its header-consistent description (`ROLE BRIEF — manager`; the orchestrator compiles a manager's session start from it) — the ninth template added in cycle 4 without extending the registry (AR4-5). As of 260703-L12 the Companion Files registry lists TEN templates (`orchestration-task` — the strategist's sprint plan — joins) plus the new `criteria/…` line (the five reviewer criteria catalogs), and the as-built settings paragraph documents `orchestration.loops` as documented-schema-with-L13-storage. As of HFX-L6/L6R3 the frontmatter description says eight role lifecycles and developer-facing sessions are architect sessions.

## Cross-Repo Evidence

No sibling repository evidence is needed for this doctrine file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-09T12:04+02:00 — 260707-HFX2-L10 (spawn settings authority): the lifecycle skill spine now
  states that ordinary spawned seats use settings as the spend surface, with role/level declared on
  `spawn_agent_session`; legacy caller spend fields and maintained harness-native spend/env keys
  refuse with `spend-override-unsupported`. Sync-propagated bundle copy of the canonical skill.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L10 commit.

- 2026-07-08T23:59+02:00 — 260707-HFX2-L5 (doctrine rewrite, active vigilance → passive
  process-and-ack): Shared Invariants section gains the new "Notify-and-stop is safe by design"
  paragraph — ending a turn once the artifact is written is never a liveness gap because the
  HFX2-L2 sweep + HFX2-L4 escalation ladder supervise silence; states the watcher ban
  (uniform-mechanism ruling 2026-07-07) and the passive-duty inversion every role file now carries.
  Doctrine-only change set (5 canonical `skills/` files, propagated by `scripts/sync-skills.py` to 9
  downstream package copies, 0 Python); sync-propagated bundle copy of the canonical
  `skills/l-01-agent-lifecycles/SKILL.md`. Verification metadata pinned until closeout stamps the
  260707-HFX2-L5 commit.

- 2026-07-08T15:27+02:00 — 260707-HFX2-L6 (task-seat takeover + delegated authority
  doctrine): added Developer-Declared Task-Seat Takeover, Developer Clarification Triage, and
  Delegated Series Authority sections to the lifecycle router. A developer-declared role takeover
  anchors on the named task leaf and verifies dashboard terminal attachment before lifecycle work.
  Close/current/small developer clarifications that fit the active leaf are implemented now rather
  than filed as future notes. Accepted orchestrated series authority lets owning seats close out,
  integrate, finalize, and clean up subordinate edges without repeated developer formality, while
  final super/PR-carryover, raised human-pinned gates, scope changes, red checks outside scope, and
  quo-vadis decisions remain developer stops. Doctrine-only change set propagated by
  `scripts/sync-skills.py`; no runtime attachment path changed. Verification metadata pinned until
  closeout stamps the 260707-HFX2-L6 commit.

- 2026-07-08T02:10+02:00 — 260707-HFX-L11 curator activation: Companion Files template registry
  gains `curator-brief` (new file, R1/R4) with its header-consistent description. Doctrine-only
  change set (7 canonical `skills/` files across 6 edits + 1 new template, synced to 9 mirrors, 0
  Python touched); sync-propagated bundle copy of the canonical `skills/l-01-agent-lifecycles/SKILL.md`.
  Verification metadata pinned — no commit yet on `ar/260707-hfx-l11-curator-activation`
  (working-tree change, synced onto the landed HFX-L7 base).

- 2026-07-08T01:00+02:00 — 260707-HFX-L7 (provider degradation protocol): the role registry table
  gains the `system-specialist` row (backend provider-degradation investigator; spawn value
  `system-specialist`; points at the new `roles/system-specialist.md`); frontmatter `description`
  and the Companion Files sentence both now say nine role lifecycles (was eight); the escalation
  ladder bullet gains a standalone `system-specialist -> orchestrator` clause beside the existing
  worker->manager->orchestrator->architect->developer chain; the settings-block worked example
  gains a `system-specialist` roles entry (`claude`/`fable`/`high`). Sync-propagated bundle copy of
  the canonical `skills/l-01-agent-lifecycles/SKILL.md`. Verification metadata pinned until
  closeout stamps the HFX-L7 commit.
- 2026-07-07T21:40+02:00 — 260707-HFX-L6R3 curator seat: added curator to the
  l-01 registry/settings example as the fresh per-leaf onboarding writer, and recorded the
  manager -> builder -> reviewer -> curator closeout chain. Sync-propagated bundle copy.
  Verification metadata pinned until closeout stamps the HFX-L6 commit.

- 2026-07-07T21:00+02:00 — 260707-HFX-L6 architect/orchestrator split: added the
  architect role to the registry and router; condition 3 now routes developer-facing sessions
  to `roles/architect.md`; condition 2 is fresh-session role briefs only; the orchestrator is
  a spawned backend seat; escalation is worker -> manager -> orchestrator -> architect ->
  developer; dashboard-owned role-seat immutability and the minimal one-at-a-time decision-item
  relay over the existing operator inbox are doctrine. Sync-propagated bundle copy. Verification
  metadata pinned until closeout stamps the HFX-L6 commit.

- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application): the settings.json Orchestration
  Block example gains the `strategist` free-form row (`effort: ultracode` + `promptKeywords`), the
  `reviewer` economics row, and the `rolesPerLevel` block; the roles comment names the three-layer
  knob model (validated harness/model/effort · free-form launchArgs/promptKeywords/sessionCommands);
  the as-built paragraph becomes L13+L16 — the knob chain now APPLIES at the harness boundary
  (per-harness argv mapping via the effective registry, dispatch-time effort refusal, the session
  vehicle for `ultracode`, the `level` dispatch input with provenance, `orchestration.harnesses`
  openness) with `docs/reference/harnesses.md` as the manual. Sync-propagated bundle copy of the
  canonical skill. Verification metadata pinned until closeout stamps the L16 commit.

- 2026-07-06T22:56+02:00 — 260703-L13 (settings unification): the settings.json
  Orchestration Block section re-homes the knobs to the global agentic settings file with
  repo-local override (fixing the authority-file contradiction), the example uses registry
  harness ids and gains `orchestration.spawn`, and the as-built paragraph documents the
  kernel loader (per-use reads, fail-loud family), the boot-snapshot gateDelegation with
  legacy fallback, and the spawn resolution chain. Sync-propagated bundle copy of the
  canonical `skills/l-01-agent-lifecycles/SKILL.md`. Verification metadata pinned until
  closeout stamps the L13 commit.

- 2026-07-06T17:35+02:00 — 260703-L12 round 2 (L12R-4 ripple): the loop home's direct-tier gloss now names the level's ordinary build channel (hands-on at session scale; the leaf's worker under a manager) instead of the ambiguous "owner implements". Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-06T15:35+02:00 — 260703-L12 (three-party loops): the strategist joins the role registry (spawn-first, mandatory pre-run, spawn value `strategist`); a new The Three-Party Loop section becomes the loop doctrine's single home (tiers · 3-full-round cap · delta-verify/builder-resume · convergence rule · quo-vadis · criteria catalogs · per-level agent sets); Companion Files list 10 templates + the `criteria/` catalogs; the settings paragraph documents `orchestration.loops`. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-05T19:55+02:00 - L8 builder cycle 7: Companion Files template registry gains the manager-brief row — all 9 on-disk templates listed (AR4-5). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): the takeover pointer names the real section (Profile check (takeover), The Event Loop). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T16:20+02:00 - L8 seam-ruling remediation (cycle 4): router edge cases written; six signals enumerated; variant rung removed; at-seams flag documented as wired. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T04:40+02:00 - L8 de-harnessing pass: per-harness variant layer removed from the resolution order; registry overlay mentions dropped. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T04:15+02:00 - L8 orchestrator routes rework: registry row marks the designer as a hat the orchestrator pulls (separate chair optional); router condition 1 notes AR_SPAWN_ROLE=designer as the same hat in another chair; router condition 3 states solo = the three jobs with hats collapsed, task doc first. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T01:30+02:00 - L9 lifecycle convergence: SKILL.md is now the unified-skill spine (router + minimal frame + shared invariants); body rewritten accordingly; supersedes the two retired skill spines. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T13:16+02:00 — 260703-L6 documented the adversarial seam procedures end to end: manager
  spawn at master-exit, orchestrator spawn at super-exit, `notes/reports/` verdict placement,
  `reviewer-verdict` gate evidence refs, policy-required verdict evidence, and block-to-fix-leaf routing
  back to the owning manager/orchestrator. Verification metadata pinned until closeout stamps the L6
  commit.
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
