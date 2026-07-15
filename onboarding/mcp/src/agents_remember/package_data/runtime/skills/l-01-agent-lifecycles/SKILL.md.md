# l-01-agent-lifecycles/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-15T23:16+02:00 |
| lastVerifiedCommitHash | `5fa7026c644edfb4eb884173b64d31c9a14a6585` |
| lastVerifiedCommitDate | 2026-07-15T23:33:30+02:00|
| governingOverview      | `../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../overview.md)

## Purpose

The spine of the unified `l-01-agent-lifecycles` skill: lifecycle and job are ONE entity (one lifecycle per agent type). This file is the router + the minimal frame + the shared invariants; the per-role lifecycles live in `roles/`, the lenses in `lenses.md`, the report templates in `templates/`. It supersedes and replaces BOTH `l-01-session-job-lifecycle` and `l-02-agent-orchestration` (converged 2026-07-05, series 260703-L9).

## Code Commentary

### 260714-ACPUI-L2 Dynamic Native Launch Doctrine

This generated runtime copy now gives every illustrative role a complete harness/model/effort
selection and labels those values as install/account-specific examples. The launch doctrine routes
the settings selection through token-free model-gated advertise and the native initial-config
channel: Claude `--model`/`--effort`, Pi provider-qualified `--model` plus `--thinking`, and Codex
`thread/start` model plus `model_reasoning_effort`. `AR_SPAWN_MODEL`/`AR_SPAWN_EFFORT` are retained
as provenance only. Missing, stale, unsupported, or conflicting native selections fail loud, and
normalized model/effort is never converted into composer paste or generated session commands.
Explicit free-form commands remain user-authored.

### Logic

Sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical `skills/l-01-agent-lifecycles/SKILL.md`. The router has exactly three conditions, in order: (1) `AR_SPAWN_ROLE` selects the matching role; (2) a fresh-session role brief selects that role; (3) otherwise the session remains a research-capable **free-chat launcher** and spawns a clean architect with the settings-owned profile for role-shaped work. The spawned architect owns the developer conversation; the orchestrator remains backend-only; curator remains the dedicated onboarding writer. Solo hat-collapse belongs only to the architect after the developer approves the short-root question. The minimal frame is the only shared machinery: the six `lifecycle_*` signals, fleeting-to-persistent promotion at `worktree_start`, `awaiting-developer` auto-resume on the next AR call, and server-side identity. A spawned role that never touches mutating AR tools never instantiates a lifecycle, and no role adopts its spawner's lifecycle. Shared invariants include durable-artifact continuity, architect terminal custody, role-seat immutability, the manager -> builder -> reviewer -> curator leaf chain, the decision relay, and dependency-graph scheduling: independent work runs in parallel by default up to the applicable `orchestration.concurrency` cap; serial execution must name a gate, shared-file one-writer dependency, or explicit ruling. The architect proposes a strategist pass and it runs only after developer approval; settings cannot auto-run it.

As of the L8 de-harnessing pass there are deliberately NO per-harness role files (developer decision 2026-07-05): knob resolution is role-file defaults < settings.json orchestration block (the variant layer is gone), harness ABILITIES are capability-conditional doctrine inside the portable files, and harness PREFERENCE is deployment configuration in settings. The registry has nine portable role files. The strategist is spawn-first only after developer approval of the architect's propose-first question; the curator is dedicated to fresh per-leaf onboarding writes; and the reviewer covers both exit seams and applicable three-party loops.

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

As of 260703-L12 the file is also the **three-party-loop doctrine's single home**: OWNER → BUILDER → REVIEWER at every level that owns work; complexity-scored tiers at dispatch; the hard three-full-round cap; same-reviewer delta verification; same-builder fix rounds; convergence and quo-vadis escalation; standing criteria catalogs; and per-level agent sets. HFX3 supersedes the old unconditional strategist sentence: Job P is approval-gated, and a developer-sanctioned skip authorizes the orchestrator to author and adopt the orchestration task from the ruled plan.

As of 260707-HFX2-L17 the catalog binding that identifies a task seat is explicitly the pair
`(qualified leaf key, seat role)`, not the leaf key alone. Developer-declared takeovers resolve the
claimed lifecycle role, pass it with the qualified leaf key to
`attach_terminal_session_to_leaf`, and verify the exact pair in the terminal catalog/dashboard.
Different roles may coexist on one canonical leaf; only a second live owner of the same pair
collides. This is the packaged runtime copy of the canonical doctrine propagated by
`scripts/sync-skills.py`.

As of 260707-HFX2-L5 (doctrine inversion: active vigilance → passive process-and-ack) the Shared
Invariants section gains a new "Notify-and-stop is safe by design" paragraph right after the
lifecycle-adoption sentence: ending a turn on `lifecycle_turn_end_notification`, or simply stopping
once the artifact is written and nothing is pending, is never a liveness gap, because the HFX2-L2
supervisor sweep evaluates every expected artifact/signal on its own mechanical tick and the
HFX2-L4 escalation ladder (renudge → skip-level → architect custody/architect attention, then respawn) handles
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
named task doc first, resolves the qualified leaf key `<repository>/<master>/<docId>` and claimed
role, uses the dashboard terminal catalog session id (not `CLAUDE_CODE_SESSION_ID` or
`CODEX_THREAD_ID`), calls `attach_terminal_session_to_leaf` with both leaf and role, renames the
session to the expected seat label, and verifies the exact pair in the terminal catalog/dashboard
before continuing lifecycle work. Second, Developer Clarification
Triage: during an active task, the seat reads the active queue (current leaf, parent/master,
neighboring leaves, decision log, open questions, in-flight branch state) before choosing a
note-only path. Close/current/small clarifications that fit the same task, doctrine, code path, or
current diff are implemented in the current leaf instead of downgraded into future notes, while
future/larger/dependency-blocked items are queued and unclear fit asks the developer directly.
Third, Delegated Series Authority: once the developer accepts an orchestrated series/portfolio plan, managers and the
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

As of cycle 5: the takeover pointer names the real section (Profile check (takeover), The Event Loop); the no-cross-reading exception says 'above'; the capability paragraph states the spawn-as-fan-out backdoor (DBMS principle). As of cycle 7 the Companion Files template registry lists all nine on-disk templates. As of 260703-L12 it lists ten templates plus the five reviewer criteria catalogs. HFX3 aligns the frontmatter summary with the body: condition 3 is the otherwise-free-chat launcher, not an architect default.

### Conventions

Canonical doctrine is edited under root `skills/` and propagated with `scripts/sync-skills.py`.
Package-data copies are eligible onboarding evidence; dot-prefixed harness mirrors remain excluded by
path rules.

### Invariants And Boundaries

- Free chat launches roles but is not itself a role seat.
- Strategist dispatch is propose-first and developer-approved; a sanctioned skip never blocks Job O.
- The escalation ladder terminates in architect custody, not a developer mailbox.
- Independent work is parallel by default within configured caps; sequential work names its reason.
- Task-seat identity is `(qualified leaf key, seat role)`; different roles may share one leaf, but
  the same live pair may not have two owners.

### Todos

Reviewer notes N1-N5 and N-d1 remain nonblocking/out of scope for this curation pass.

## Docs References

No external domain documentation is configured for this repository-local lifecycle doctrine.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The packaged source carries the launcher, approval-gated strategist, architect-custody, and parallel-by-default invariants. | L12-L38; L90-L96; L156-L177; L229-L235 | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md) |
| Canonical skills are propagated into package data and harness mirrors by the sync script. | L14-L55 | [scripts/sync-skills.py](agents-remember/scripts/sync-skills.py) |

## Cross-Repo References

No sibling repository evidence is needed for this doctrine file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## 260712-TRH-L4 Generated-Copy Doctrine

This sidecar describes the generated runtime copy, not canonical ownership. It is synchronized from canonical l-01-agent-lifecycles doctrine. L4 defines spawned-unbriefed → harness-ready → briefed: spawn is creation only, exact-session readiness proves the target harness is ready, and durable dispatch-brief advances the seat only with delivered plus harness-log-confirmed proof. Spawned-only or not-ready is not active work; sessionCommands remain launch configuration and promptKeywords apply once after readiness.


### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

## Update History
- 2026-07-15T23:16+02:00 — 260714-ACPUI-L2 curator: documented the synchronized dynamic
  model-gated launch doctrine, complete role examples, native per-harness launch channels,
  provenance-only spawn env, and the no-normalized-paste boundary; final-audited the nearest MCP
  governing overview backlink. Verification metadata remains pinned until closeout stamps the L2
  code commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.
+## 260712-TRH-L4 Generated-Copy Doctrine

This sidecar describes the generated runtime copy, not canonical ownership. The source is synchronized from the canonical l-01-agent-lifecycles doctrine by the skill-sync process. L4 defines spawned-unbriefed → harness-ready → briefed: spawn is creation only, exact-session readiness proves the target harness is ready, and one durable dispatch-brief advances the seat only with delivered plus harness-log-confirmed proof. Spawned-only or not-ready is not active work; sessionCommands remain launch configuration and promptKeywords apply once after readiness.

- 2026-07-10T15:48+02:00 — 260707-HFX2-L17 generated-runtime doctrine delta: documented
  task-seat identity as `(qualified leaf key, seat role)`, made developer-declared takeover pass
  and verify the claimed role with the qualified leaf, and recorded same-pair-only live collision.
  Sync-propagated bundle copy; verification metadata remains pinned until closeout stamps the L17
  commit.

- 2026-07-10T02:39+02:00 — HFX3/L14 combined curation: reconciled the free-chat launcher,
  settings-owned architect spawn, propose-first strategist approval, sanctioned-skip Job O path,
  architect terminal custody, and dependency-graph parallel-by-default invariant. Added the
  governing overview and required reference/boundary sections. Verification metadata remains
  pinned until closeout stamps the eventual two-parent code commit.

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

- 2026-07-08T15:45+02:00 — 260707-HFX2-L7 doctrine refinement: Developer Clarification Triage now
  explicitly reads the active queue before choosing note-only handling; a small clarification that
  plainly fits the same task/current diff is a strong immediate-implementation signal, true future
  queue is recorded durably, and unclear fit asks the developer directly. Sync-propagated bundle
  copy of the canonical `skills/l-01-agent-lifecycles/SKILL.md`.

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
