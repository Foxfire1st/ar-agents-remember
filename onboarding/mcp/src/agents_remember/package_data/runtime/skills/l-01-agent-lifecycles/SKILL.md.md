# l-01-agent-lifecycles/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-07T21:40+02:00 |
| lastVerifiedCommitHash | `2c464cf4c29b60165fecae722bf76c307aaac6f1` |
| lastVerifiedCommitDate | 2026-07-07T22:59:19+02:00|

## Purpose

The spine of the unified `l-01-agent-lifecycles` skill: lifecycle and job are ONE entity (one lifecycle per agent type). This file is the router + the minimal frame + the shared invariants; the per-role lifecycles live in `roles/`, the lenses in `lenses.md`, the report templates in `templates/`. It supersedes and replaces BOTH `l-01-session-job-lifecycle` and `l-02-agent-orchestration` (converged 2026-07-05, series 260703-L9).

## Code Commentary

### Logic

Sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical `skills/l-01-agent-lifecycles/SKILL.md`. HFX-L6 adds the **architect** as the developer-facing owner seat and reframes the **orchestrator** as a spawned backend seat; L6R3 adds **curator** as the dedicated onboarding writer. The router still has exactly three conditions, in order: (1) `AR_SPAWN_ROLE` env set -> run `roles/<value>.md`; (2) a fresh-session role brief -> run that role; (3) otherwise the session is developer-facing -> run `roles/architect.md`. Solo hat-collapse belongs only to the architect. The minimal frame is the only shared machinery: the six `lifecycle_*` signals, fleeting->persistent promotion at `worktree_start`, `awaiting-developer` auto-resume on the next AR call, server-side identity; a spawned role that never touches mutating AR tools never instantiates a lifecycle (designed shape), and a spawned role never adopts its spawner's lifecycle - the session<->leaf association is the catalog binding via the QUALIFIED leaf key `<repository>/<master>/<docId>`. Shared invariants: continuity in task_doc + durable artifacts (never transcripts); the escalation ladder worker -> manager -> orchestrator -> architect -> developer with no rung skipped; role-seat immutability for dashboard-owned sessions (roles expand horizontally into new chats, sub-agents drill vertically inside one seat); the manager -> builder -> reviewer -> curator leaf closeout chain; and the minimal decision-item relay over the existing operator inbox (one item at a time: decision/options/consequences/evidence refs, with a durable ruling back). Also carries the knob-block resolution (role-file defaults < global agentic settings < repo-local settings — since 260703-L13 the settings home is the GLOBAL agentic settings file `<coordination-root>/system/settings.json` with `<code-repo>/system/settings.json` overrides, not the MCP authority file), the as-built settings documentation (`orchestration.gateDelegation` parsed + enforced by `controlplane/gate_policy.py`, boot-snapshot from the global file with a one-cycle warned authority fallback; `roles`/`concurrency`/`spawn`/`loops` PARSED per-use by `kernel/agentic_settings.py` — the backlog closed; `spawn_agent_session` resolves its knobs explicit args > repo-local level override > global level override > repo-local role default > global role default > detection-gated — since 260703-L16 the knobs are APPLIED at the harness boundary: model/effort ride `AR_SPAWN_MODEL`/`AR_SPAWN_EFFORT` env AND map onto the launch argv per-harness via the effective registry, unknown effort values REFUSE at dispatch naming the harness's vocabulary (claude's two-vehicle set incl. the session-level `ultracode` delivered as a post-launch `/effort` paste), the free-form escape hatch (`launchArgs`/`promptKeywords`/`sessionCommands`) is never validated only recorded in spawn provenance, `orchestration.rolesPerLevel` expresses per-LEVEL agent sets, and `orchestration.harnesses` teaches new TUIs / pre-customizes builtin launches — manual `docs/reference/harnesses.md`; example harness ids are registry ids claude/codex), a 6-line super-branch orientation diagram (the full topology's single home is `roles/orchestrator.md`), and the credits lineage (260619 spec -> Archon / agent-control-plane).

As of the L8 de-harnessing pass there are deliberately NO per-harness role files (developer decision 2026-07-05): knob resolution is role-file defaults < settings.json orchestration block (the variant layer is gone), harness ABILITIES are capability-conditional doctrine inside the portable files, and harness PREFERENCE is deployment configuration in settings. As of HFX-L6/L6R3 the registry lists EIGHT portable role files — architect, orchestrator, designer, strategist, manager, worker, curator, reviewer — with the strategist row still spawn-first and mandatory before any orchestrated run, the curator row dedicated to fresh per-leaf onboarding writes, and the reviewer row extending to the loop-reviewer seat (the two seams AND any three-party loop's review, criteria catalogs bound per review type).

As of 260703-L12 the file is also the **three-party-loop doctrine's single home** (a new section between Shared Invariants and the knob block, referenced per seat): OWNER → BUILDER → REVIEWER at every level that owns work (leaf/master/portfolio table); complexity-scored tiers at dispatch (direct / builder-verified / full loop, scored on blast radius · novelty · size; round 2 glosses direct as no-loop-machinery through the level's ordinary build channel — hands-on at session scale, the leaf's worker under a manager — so it cannot read manager-implements; a master whose leaves all score direct = workflow-free manager); the HARD 3-round cap where ONLY full end-to-end rounds count (delta-verifies by the SAME reviewer close rounds; fix rounds resume the SAME builder); the CONVERGENCE rule (every round must shrink the finding set — a non-shrinking round escalates immediately; the cap is the backstop); escalation one seat up the ladder with the full round history attached; the written QUO-VADIS criterion (a high-blast-radius truth escalates immediately; presentation-grade never); the criteria-catalog binding (`criteria/` — code-seam · doctrine · onboarding-memory · report-verification · plan-review) and the per-level agent sets (knobs in `orchestration.loops`, schema in `docs/reference/settings-json.md`, stored in the global agentic file with repo-local override and parsed by the kernel loader since L13 — the strategist's mandatory pre-run is doctrine, not a knob).

As of cycle 4 the router decides its edge cases in writing (unresolvable AR_SPAWN_ROLE falls through to the brief; a briefless role-env session announces itself on the inbox and waits; AR_SPAWN_ROLE=orchestrator is takeover-only), the brief header form is canonical (`ROLE BRIEF — <role>` or a templates/*-brief.md shape), the hat/seat exception to the no-cross-reading rule is stated, the reviewer registry row carries spawn value `reviewer` -> roles/reviewer.md, the six lifecycle signals are enumerated by name, the dead variant rung is gone from the precedence line, and the as-built settings text documents the wired requireReviewerVerdictAtSeams + the named policy routing the handover to the orchestrator.

As of cycle 5: the takeover pointer names the real section (Profile check (takeover), The Event Loop); the no-cross-reading exception says 'above'; the capability paragraph states the spawn-as-fan-out backdoor (DBMS principle). As of cycle 7 the Companion Files template registry lists all nine on-disk templates: `manager-brief` joins the line with its header-consistent description (`ROLE BRIEF — manager`; the orchestrator compiles a manager's session start from it) — the ninth template added in cycle 4 without extending the registry (AR4-5). As of 260703-L12 the Companion Files registry lists TEN templates (`orchestration-task` — the strategist's sprint plan — joins) plus the new `criteria/…` line (the five reviewer criteria catalogs), and the as-built settings paragraph documents `orchestration.loops` as documented-schema-with-L13-storage. As of HFX-L6/L6R3 the frontmatter description says eight role lifecycles and developer-facing sessions are architect sessions.

## Cross-Repo Evidence

No sibling repository evidence is needed for this doctrine file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

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
